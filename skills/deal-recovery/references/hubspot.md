# HubSpot adapter and evidence reader

## Connection and schema

Use the connected HubSpot plugin's current tools. Call `get_user_details` before the first CRM operation in a run; check account and required read/write availability. Use the installed HubSpot skill when available, otherwise current tool descriptions. Discover tools instead of assuming a fixed MCP namespace or direct API credentials.

Use `search_properties` with at most five keywords and `get_properties` to verify names, writable fields, pipeline/stage values, task enums, and owner IDs through appropriate metadata. Use `discover_hubspot_schema` for ambiguous types. A field visible in the UI or listed as default does not prove its populated body is retrievable.

Retain the verified mapping in catalog configuration. Starting candidates:

| Object | Candidate properties | Purpose |
|---|---|---|
| DEAL | `dealname`, `description`, `pipeline`, `dealstage`, `hubspot_owner_id`, `closedate` | Context, scope, owner, recorded outcome. |
| NOTE | `hs_note_body`, `hs_timestamp` | Observations and saved state. |
| CALL | `hs_call_title`, `hs_call_body`, `hs_timestamp`; supported outcome/status | Call details and occurrence. |
| EMAIL | `hs_email_subject`; verified body, time, direction/status | Logged evidence. Do not assume `hs_email_text` exists or HTML body represents inbound mail. |
| MEETING_EVENT | `hs_meeting_title`, `hs_meeting_body`, `hs_meeting_start_time`; supported outcome | Notes and scheduled-versus-held distinction. |
| TASK | `hs_task_subject`, `hs_task_body`, `hs_task_status`, `hubspot_owner_id`; supported date/type/priority | Planned/completed work and duplicate checks. |
| CONTACT | `firstname`, `lastname`, `email`; available relevant role fields | Targeted identity lookup. |

No dedicated risk property is required. A configured risk field can contribute evidence; do not invent an At Risk stage or write inferred risk into commercial fields. LinkedIn/SMS logs are usable only if the actual type/body is exposed. A note describing an interaction is note evidence with its stated provenance, not a direct external-app read.

## Read one deal story

1. Fetch known IDs with `get_crm_objects`; use `search_crm_objects` for scoped searches and association filters. Respect actual tool ID types. If a configured name prefix is only searchable with a broader contains filter, verify the exact prefix locally before including a deal.
2. Retrieve configured activity types directly associated with this deal, with pagination. Avoid pulling every company/contact activity into every deal. Report unavailable types and failed/truncated retrieval.
3. Keep exact selected fields for fingerprints; normalize a compact timeline with object type/ID, deal ID, event time, actor/direction/status if available, content, and source link. Use occurrence time when documented: a log's creation time may be later. Preserve uncertainty about ordering.
4. Exclude assistant catalog/review notes and generated tasks using known IDs and body markers, including HTML-rendered markers, `Tracking reference: DR-…`, and legacy `RECOVERY_ASSISTANT_TASK v1` receipts. Keep generated tasks in a separate ledger for duplicate checks. Ordinary rep-authored notes remain eligible evidence.
5. Distinguish plans, actual actions, and buyer responses. A completed task is a rep-reported completion signal, not proof of buyer response or causality. Generated drafts are never evidence of performed work.

Use relevant fields only. Aggregate last activity/modified timestamps can change when this skill writes notes/tasks; exclude them from inactivity rules and fingerprints. Base any elapsed-time condition on underlying relevant events, distinguishing seller outreach from buyer response.

For large histories, process bounded chronological chunks and retain cited facts needed for the current issue. Do not call a truncated sample complete. Keep retrieval coverage separate from a conclusion about risk.

## Notes, writes, and links

Notes have their own IDs and appear on associated timelines; no custom object is needed. Place the label on the first line of `hs_note_body`. Use supported timestamps. A note can be associated with multiple selected deals; verify associations after creation.

Follow current connector confirmation rules for all note/task writes: show exact properties and associations, obtain applicable approval, and use the correct confirmation state. Existing approval carries only its actual scope. A config field cannot waive confirmation. Limit write batches to ten objects. Preserve rep-entered context and avoid duplicate managed notes.

Keep JSON readable after HTML rendering: escape appropriately in a plain/preformatted section, and decode HTML entities on read. Read back initial saved bodies to verify round trips. If data is corrupt or its schema unsupported, retain the readable record and report the needed repair rather than silently overwriting it.

Use returned record URLs where available. Without an activity-specific URL, link its associated deal and include object type/ID. Follow required URL/UTM conventions from current tool guidance; do not invent deep links or tracking values. Report actual filters, coverage, and totals or partial counts.
