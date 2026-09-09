# Deal Recovery

Make effective responses to difficult deals easier for every AE to reuse.

Deal Recovery learns from selected troubled-but-won HubSpot deals, reviews current deals for relevant signals, and prepares useful next steps. The rep approves specific proposals before CRM tasks are created.

## Install and connect

The plugin includes the Deal Recovery skill, its supporting references and identity helper, and a required HubSpot app declaration. Installing the plugin installs its bundled skill; there is no separate skill installation step.

Recommended: install the official HubSpot plugin and connect your own HubSpot account first. Then install Deal Recovery from your configured marketplace and start a new Work conversation. If you install Deal Recovery first, complete the HubSpot connection when prompted or connect it separately in Plugins, then start a new conversation. CRM operations require a completed connection. A recipient must authenticate their own HubSpot connection and have access to the selected deals and activities. Existing connection state is not transferred in this package. [Using plugins](https://learn.chatgpt.com/docs/plugins).

## 1. Build your catalog

Choose a small set of previously troubled deals that eventually closed won and have activity histories documenting what the AE actually did. Decide which open deals you want future reviews to cover.

Example request:

> Use Deal Recovery to learn from these historical HubSpot deals: [deal links]. Review their records and associated activities. My active-deal scope is [pipeline and owners or other explicit scope]. Prepare a shared recovery catalog note for my approval.

Review the lessons and their supporting evidence before saving. The catalog links each signal to one or more observed actions, relevant context, and limitations. A won outcome supplies a precedent; it does not establish that a particular tactic caused the win.

The assistant returns the saved catalog note link and a reusable Review prompt containing its actual ID. Keep that prompt for subsequent chats and any schedule.

## 2. Review current deals

> Use Deal Recovery to review open deals using catalog note [saved ID]. Show supported recommendations and the exact task proposals for my approval. Include any review-note saves needed to retain the assessment and proposal state.

Each proposal explains the unresolved obstacle, the applicable historical lesson, why the next step fits this deal, and what the rep should do. Resolved concerns, unsupported matches, and existing equivalent work should not generate a new task.

The skill can attempt discovery when no catalog ID is supplied, but asks you when results are ambiguous or discovery is unavailable. Explicit IDs provide the most predictable cross-chat behavior.

## 3. Approve and carry out the work

Approve the displayed proposal labels individually or as a batch. You can request changes before approval. The assistant checks for equivalent tasks immediately before creating and verifying the approved task and its deal association.

Tasks contain a short action title, reason, usable steps or draft, source links, and a compact tracking footer. The deal review note holds the detailed processing state when saving is authorized. The rep owns execution and completion status.

## Optional recurring review

After a successful manual Review, request a schedule with its cadence, time, timezone, catalog ID, and scope. The host scheduler triggers Review. Each run returns recommendations; it does not authorize CRM tasks. Saving review notes unattended depends on connector permissions and existing authorization; otherwise the run returns its report without CRM writes. [Scheduling documentation](https://learn.chatgpt.com/docs/automations).

Use the same catalog until you deliberately request a refresh with selected historical deals. This release does not automatically discover newly recovered deals, evaluate tactic effectiveness, or promote new lessons. A recurring reminder to review the catalog is a possible separate schedule; automatic continuous learning is outside this version.

## What this version promises

- Read the selected deal histories and available associated activities in HubSpot.
- Recommend the earliest useful action supported by current context and historical evidence.
- Keep pending, declined, and logged proposals distinct when state is saved.
- Check for duplicate work, including equivalent tasks written by humans and legacy Deal Recovery tasks.
- Report missing evidence, incomplete reads, and unsuccessful writes.
