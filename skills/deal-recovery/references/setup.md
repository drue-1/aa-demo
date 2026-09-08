# Reuse and scheduling

## Find the saved catalog

Do not rely on another conversation remembering an ID. Keep customer data and account-specific IDs in CRM and the invocation, never in the distributed skill.

1. If the user or invocation supplies a note ID, retrieve it and validate its catalog marker, schema, connected account, and requested scope. A missing, deleted, or mismatched note requires correction; do not silently substitute another catalog.
2. Otherwise search notes associated with supplied historical deals first. If no such restriction was supplied, search the connected CRM for `RECOVERY_ASSISTANT_CATALOG`, paginate results, retrieve candidate bodies, and verify the exact marker and stored account/scope. Searchability depends on the connector; do not assume a zero-result body search proves no catalog exists.
3. Use a single verified catalog compatible with the requested scope, and state which one was selected. If multiple catalogs remain plausible, show their human titles, source deals, and scopes and ask which to use. If discovery is unavailable or inconclusive, ask for a catalog link/ID or a historical source deal. Never choose the newest merely because it is newest.

Keep returned catalog IDs in the reusable review prompt. After a reset, use the newly created ID and update any saved prompt or schedule that referenced the deleted catalog.

## Optional daily review

Explain onboarding as: **Connect HubSpot → Learn from selected deals → Test Review → Optionally schedule Review.** The skill defines the workflow; the host's scheduler supplies the trigger. A skill can guide or carry out schedule setup when explicitly requested and the runtime exposes scheduling tools. Installing or running the skill does not itself start a recurrence.

When the user requests setup, use current host scheduling instructions and tools. Resolve only missing cadence/time/timezone, destination, account/catalog, and scope. Check required connector access and whether approved note maintenance can run unattended. Include the requested model/reasoning when supported by the scheduler; never claim prose alone changed the runtime model. Do not silently replace an unavailable model.

Populate this recurring prompt with actual configuration:

> Use $deal-recovery in Review mode with HubSpot catalog note [actual ID] in account [actual account]. Check open deals matching the catalog's saved scope. Read current evidence and existing tasks. Show supported recommendations, unchanged pending proposals, and material coverage limits in a concise report. Maintain only the specified assistant review notes where already authorized and supported; otherwise return the review without CRM writes. Leave all task creation for the rep's specific approval. Do not relearn or modify the catalog.

Explain that a user can approve selected proposals from the report, or refer to the saved review note in another chat and review the exact payload there. A scheduled result or a stored status never supplies approval by itself.

Test Review manually before scheduling. When creating a schedule, retain and return its actual ID, cadence, timezone, destination, and selected model if verified. An unattended run should report a missing catalog or unavailable permission and finish; it must not wait for a reply, fabricate memory, or repeatedly retry a failed write. Do not create an active schedule when the user only asks how recurrence works.
