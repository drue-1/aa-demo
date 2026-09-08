# Deal Recovery — GitHub distribution

Reusable HubSpot deal-recovery workflow by Drue. Learn from selected troubled-but-won deals, review open deals against the saved catalog, and create tasks after the rep approves specific proposals.

## Publish this repository

Extract this archive and commit the CONTENTS of this folder to your GitHub repository root. Include the hidden `.agents` and `.codex-plugin` directories. Commit the unpacked files, not just this ZIP. GitHub Desktop or Git can include the hidden directories reliably.

The repository already contains `.agents/plugins/marketplace.json`, pointing to `./` (the repository root). The marketplace is named `deal-recovery-marketplace`.

The plugin manifest, app declaration, skills, and assets all live directly at the repository root. There is no outer `plugins/` directory. Keep `.agents/plugins/marketplace.json` in its standard location; that nested path is the marketplace metadata location.

## Recipient setup

1. In ChatGPT Plugins, install the official HubSpot plugin and connect your own HubSpot account. Confirm access to the intended portal, deals, activities, notes, and tasks.
2. In a compatible local Codex environment, add this GitHub marketplace, replacing OWNER/REPO with this repository's actual GitHub path:

```bash
codex plugin marketplace add OWNER/REPO
```

3. Open the Plugins directory in the supported desktop app, refresh/restart if needed, select the Deal Recovery marketplace, and install Deal Recovery. In Codex CLI, use `/plugins` to browse the configured marketplace.
4. Start a new Work/Codex conversation with HubSpot tools and Python 3 available.
5. Ask Deal Recovery to learn from your selected historical deals, supplying deal links and the intended open-deal scope. Approve saving the catalog, then keep the returned catalog note ID for future reviews.

For an extracted local repository, the marketplace-add command can instead use its absolute root path. Browser-only users should use their workspace's supported GitHub marketplace import process (admin access may be required); pasting a GitHub URL into an ordinary chat does not guarantee installation.

Connecting HubSpot after Deal Recovery installation is also possible: finish authentication when prompted or connect HubSpot separately in Plugins, then start a new chat. Until that connection is available, Deal Recovery cannot read or write CRM records. Installing this repository does not transfer the author's HubSpot access.

## What the HubSpot ID means

`.app.json` declares the official HubSpot app ID `asdk_app_697acb8e53d88191bf7a79e62012ae14`. This is an integration identifier, not a HubSpot portal ID, user ID, password, or OAuth token. It matches the official HubSpot plugin manifest and was resolved through plugin dependency metadata to the public HubSpot catalog entry on 2026-09-08. Each recipient authenticates their own connection. Their workspace policies and account availability still apply.

HubSpot is required by the workflow. The app declaration uses the validated `id` mapping; marketplace authentication policy is `ON_INSTALL`. Exact prompts depend on the host. No custom MCP server or `.mcp.json` is needed for this connector-based workflow.

## Usage and scope

See [the workflow guide](USAGE.md) for Learn, Review, task approval, and optional scheduling. This repository contains no customer records, saved catalog, account credentials, or active schedule. Installation does not start an automated review.

## Verification

Plugin manifest validation and repository path checks were completed for this package. The HubSpot app ID was checked against the official installed plugin and live canonical dependency metadata. A fresh recipient installation and authentication have not been exercised; after publishing, verify those with a recipient account before promising a one-step installation.

## Official documentation

- [Plugin packaging and Git marketplaces](https://developers.openai.com/plugins/build/plugins)
- [Plugin installation and connection](https://learn.chatgpt.com/docs/plugins)
