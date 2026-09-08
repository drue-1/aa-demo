#!/usr/bin/env python3
"""Compute stable identities from already-filtered CRM evidence; no CRM I/O."""

import argparse
import hashlib
import json
import re
import sys


ACTION_FIELDS = ("deal_id", "episode_id", "lesson_id", "action_id", "target_key")


def digest(value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"),
                         ensure_ascii=False, allow_nan=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def fingerprint(data):
    if not isinstance(data, dict) or not str(data.get("deal_id") or "").strip():
        raise ValueError("Evidence must be an object with a nonempty deal_id")
    for field in ("properties", "coverage"):
        if not isinstance(data.get(field), dict):
            raise ValueError(f"Evidence {field} must be an object")
    if not isinstance(data.get("activities"), list):
        raise ValueError("Evidence activities must be a list")
    indexed = {}
    for activity in data["activities"]:
        if not isinstance(activity, dict):
            raise ValueError("Each activity must be an object")
        if not activity.get("object_type") or not str(activity.get("id") or "").strip():
            raise ValueError("Each activity needs an object_type and id")
        if not isinstance(activity.get("fields"), dict):
            raise ValueError("Each activity needs a fields object")
        key = (str(activity["object_type"]), str(activity["id"]))
        item = {"object_type": key[0], "id": key[1], "fields": activity["fields"]}
        if key in indexed and indexed[key] != item:
            raise ValueError(f"Conflicting versions of source {key}; reconcile before hashing")
        indexed[key] = item
    return digest({"schema_version": 1, "deal_id": str(data["deal_id"]),
                   "properties": data["properties"], "coverage": data["coverage"],
                   "activities": [indexed[key] for key in sorted(indexed)]})


def action_key(data):
    if not isinstance(data, dict):
        raise ValueError("Action identity must be an object")
    result = {}
    for field in ACTION_FIELDS:
        if not isinstance(data.get(field), (str, int)) or isinstance(data[field], bool):
            raise ValueError(f"{field} must be a nonempty string or integer")
        result[field] = str(data[field]).strip()
        if not result[field]:
            raise ValueError(f"{field} must not be empty")
    return "ra_" + digest(result)


def task_ref(data):
    key = data.get("proposal_key") if isinstance(data, dict) else None
    if not isinstance(key, str) or not re.fullmatch(r"ra_[0-9a-f]{64}", key):
        raise ValueError("proposal_key must be a full lowercase ra_ SHA-256 key")
    return "DR-" + key[3:19]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("fingerprint", "action-key", "task-ref"))
    parser.add_argument("input", help="JSON file path, or - for standard input")
    args = parser.parse_args()
    try:
        if args.input == "-":
            data = json.load(sys.stdin)
        else:
            with open(args.input, encoding="utf-8") as handle:
                data = json.load(handle)
        handlers = {"fingerprint": fingerprint, "action-key": action_key, "task-ref": task_ref}
        print(handlers[args.mode](data))
    except (OSError, ValueError, TypeError) as error:
        parser.exit(2, f"identity: {error}\n")


if __name__ == "__main__":
    main()
