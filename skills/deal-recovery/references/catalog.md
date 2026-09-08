# Build the initial catalog

## Read and select

Use the supplied historical candidate set rather than searching the entire CRM for success stories. Two supplied cases are enough for the prototype. Verify their actual won stage using the configured pipeline; verify that available activity history contains a troubled period followed by an action actually taken. Keep exclusions and missing evidence visible.

Construct each candidate's timestamped story using the shared reader. Extract the problem episode, relevant context, actions taken, subsequent buyer response, and recorded final outcome. Cite source object IDs and links for each material claim. A closed-won deal without a documented recovery action cannot establish a recovery tactic. Retain it as an insufficient case rather than inventing the missing sequence.

Use user-supplied hypothetical facts only when explicitly identified as synthetic exercise data. Label those cases and lessons synthetic. Do not silently fill gaps in real evidence.

## Consolidate lessons

Default to at most two evidence-supported signal families for this prototype. Preserve multiple candidate actions where supported; choose actions during Review according to current context. Do not require a tactic to appear in both cases or label one occurrence a recurring pattern.

Assign stable IDs such as `L1` for a lesson and `L1-A1` for an action. Each lesson contains:

- **Signal:** observable qualifying evidence and contradictions.
- **Context:** relevant stage, stakeholder role, constraint, or situation.
- **Actions:** each observed action's intent, applicability, exclusions, and information needed to propose it.
- **Evidence:** case references and source IDs, including actual action and subsequent response evidence where available.
- **Limitations:** supporting case count, missing response evidence, synthetic status, and uncertain attribution.

Keep compact historical case summaries in the catalog so Review need not retrieve every old activity. Retain source IDs for deeper checks.

For each action, explain the business connection: which observed obstacle it addressed and what subsequent evidence supports reusing it. Keep the seller's explanation, a buyer's direct response, and the recorded won outcome distinct. Do not generalize from incidental details, assume every step in a winning deal was necessary, or call a seller a top performer without evidence. Preserve dependencies between actions so Review can recommend the next feasible step.

## Save one catalog

Write a readable catalog followed by an escaped JSON block in the note body. Start with `RECOVERY_ASSISTANT_CATALOG v1`, then give a human title, scope, and a short entry for each lesson: signal, when it applies, observed actions, linked supporting case, and limits. Use normal paragraphs and lists; do not wrap the whole catalog in a preformatted block. Place technical JSON below a separator labeled **Automation data — saved catalog**. Minimum structure:

```json
{
  "schema_version": 1,
  "catalog_version": "v1",
  "created_at": null,
  "configuration": {
    "account_id": null,
    "historical_deal_ids": [],
    "active_scope": {},
    "activity_field_map": {},
    "deal_property_names": [],
    "run_limit": null
  },
  "cases": [],
  "lessons": []
}
```

Populate actual values before saving. `active_scope` records pipeline, exact open-stage IDs, and user-selected owner filters, deal IDs, or demo prefix; record how filters combine. Use a dynamic scoped search when new matching deals should be discovered. A fixed list intentionally excludes future deals. `run_limit` is an optional user-selected cap, not an assertion that the rest of the pipeline was checked.

`activity_field_map` records verified readable types and their selected content, event-time, and status/direction fields. Keep coverage limitations in the catalog. Include the case and lesson structures described above; empty lists here are a format template, not a ready catalog.

Present the completed note body and exact historical associations for required write approval. Create one note associated with selected cases and read it back. Check that readable content and JSON survived HTML handling. Return its ID/link and a ready-to-copy invocation with the actual returned ID: “Use $deal-recovery to review open deals using catalog note [actual ID]. Propose tasks for my approval.” Explain that the prompt works in another chat with the same HubSpot account connected. Follow [setup.md](setup.md) for catalog discovery or requested recurrence setup; do not activate a schedule just because Learn finished.

For an explicit refresh, retrieve the existing note, show changes, preserve stable IDs for unchanged lessons/actions, and increment the catalog version. Preserve rep-authored text. Ordinary Review runs never rewrite lessons or promote their own outputs into the catalog.
