# Review current deals

## Retrieve current evidence

Read the catalog and verify its account and scope. Query only matching open deals. Retrieve each deal's source story, associated tasks, and assistant review note. Keep catalog and generated reviews/tasks outside the source story. If multiple notes claim to be the same review, report the ambiguity rather than silently merging or overwriting them.

Produce this input for the identity helper:

```json
{
  "deal_id": "actual-deal-id",
  "properties": {},
  "activities": [
    {"object_type": "NOTE", "id": "actual-source-id", "fields": {}}
  ],
  "coverage": {}
}
```

Populate `properties` with exact selected source values, and activity `fields` with exact selected content, time, status, actor, and direction values. Do not hash generated summaries. Deduplicate by object type and ID. Exclude aggregate modification/activity values affected by assistant writes. In `coverage`, record types, pagination completeness, and limitations; omit changing run timestamps and cursors from the fingerprint input.

Execute `python3 <skill-directory>/scripts/identity.py fingerprint <evidence.json>` and retain its returned hash. Local inputs are temporary computation, not persistent memory. Compare the hash and catalog version to saved review state. If unchanged, reuse the assessment and pending proposals; still read task status and check equivalent existing work before presenting or logging a task.

If a configured lesson has a time-based condition, check saved `next_check_at` even when source content is unchanged. No default age threshold exists. A failed or truncated read remains `incomplete`; never cache it as a definitive no-risk review. Declared unavailable activity types remain an explicit limitation on any supported finding.

## Match and draft

Check the signal, context, exclusions, candidate action applicability, and evidence that the issue was already addressed. Use the latest relevant events to distinguish current trouble from resolved objections. Early intervention and rescue use the same matcher.

Return `recommendation_proposed`, `no_matching_lesson`, `no_current_signal`, or `incomplete`. Distinguish risk without a matching tactic from no current signal in the available evidence.

For a supported match, select a useful next action rather than every candidate tactic. Explain why it fits using current evidence and historical precedent. Read [tasks.md](tasks.md) when preparing task drafts for their readable body format, tracking reference, and exact approval presentation. Draft enough for the rep to act: a message, agenda, diagnostic questions, or checklist as appropriate. Drafting an invitation does not send one.

Resolve the task owner from the deal owner and current connector data. Show suggested due dates for approval; leave optional dates unset when unknown. Read associated contacts only when the recommendation needs a specific person, using activity context to identify the relevant role. Keep unresolved identities explicit rather than inventing recipients. A task to identify the right stakeholder can be valid if supported by the lesson.

Before presenting a proposal, check its business logic:

- Identify the current unresolved obstacle and explain how this action could address it; shared words or a shared industry alone are insufficient.
- Respect stage and role differences. Do not imply that an evaluation occurred, results exist, or a stakeholder has authority unless current sources establish it.
- Recommend the earliest useful step whose prerequisites are met. Make later steps conditional; do not copy an entire past sequence onto an earlier-stage deal.
- Check that relevant work is not already done, declined, or covered by an existing task. Preserve the rep's explicit constraints.
- Give the rep something executable and a concrete outcome to capture, such as documented barriers or confirmed decision ownership. State key unknowns rather than filling them with confident prose.

If these checks fail, narrow the action or withhold it and explain the missing evidence. A polished draft is not sufficient evidence of a good recommendation.

## Preserve identity and proposals

Assign a stable `episode_id` based on the earliest qualifying source reference for this live issue. Reuse it while the same issue continues despite new evidence. A documented resolution followed by a new occurrence may start another episode.

Execute `python3 <skill-directory>/scripts/identity.py action-key <identity.json>` with the exact keys `deal_id`, `episode_id`, `lesson_id`, `action_id`, and `target_key`. Use a verified contact ID when applicable, otherwise a consistent role or `deal` target. Also compare semantically against previous proposals and tasks: resolving a role to a contact must not create duplicate work. Reuse the original key for the same action. Changes to title, due date, or draft do not create a new action.

Save a readable assessment and pending task drafts in the deal review note, beginning `RECOVERY_ASSISTANT_REVIEW v1`. Lead with the deal's situation, evidence, applicable lesson, proposed next step, and approval status. Use short paragraphs and lists; keep the human section outside preformatted/code blocks. After a separator labeled **Automation data — for repeat checks**, include an escaped JSON block with:

- `schema_version`, `deal_id`, `catalog_note_id`, `catalog_version`, `reviewed_at`, `source_fingerprint`, `coverage`, `assessment_status`, and nullable `next_check_at`.
- `proposals`: stable key and identity fields, `task_reference` from the Tasks helper, evidence references, exact proposed task properties/associations, status (`pending`, `declined`, `superseded`, or `logged`), and nullable `task_id`. Read legacy entries without `task_reference` by deriving it from their full proposal key.

Keep a `logged` entry only as a receipt/reference; the task owns its work status. Preserve declined and logged keys across reviews. Materially new evidence may justify reconsideration, but explain it to the rep. Preserve rep edits/comments when updating the note. After a task exists, do not overwrite its content, owner, dates, or status during Review.

Apply main-skill note approval rules and skip unchanged writes. Without persistence, show the full proposal in the run report and explain that a later context must retrieve/reconstruct it before approval.

End with proposal IDs, linked deals, rationale, exact task details/drafts, and ask which to log. Do not create placeholder tasks for unapproved recommendations. An unattended review returns reviewable output without waiting for an interactive reply or creating tasks.
