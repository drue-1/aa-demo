# Deal Recovery — GitHub distribution

Reusable HubSpot deal-recovery workflow by Drue. Learn from selected troubled-but-won deals, review open deals against the saved catalog, and create tasks after the rep approves specific proposals.


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

## Verification

Plugin manifest validation and repository path checks were completed for this package. The HubSpot app ID was checked against the official installed plugin and live canonical dependency metadata. A fresh recipient installation and authentication have not been exercised; after publishing, verify those with a recipient account before promising a one-step installation.

## Official documentation

- [Plugin packaging and Git marketplaces](https://developers.openai.com/plugins/build/plugins)
- [Plugin installation and connection](https://learn.chatgpt.com/docs/plugins)
