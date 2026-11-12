# Microsoft Ecosystem Daily Brief - 2026-11-12

> Status: Fresh at generation. Current freshness is tracked in `reports/status.json`.
> Generated: 2026-11-12 20:57 UTC - Window: 26.7h from 2026-11-11 18:15 UTC to 2026-11-12 20:57 UTC.
> 141 repo(s) moved - 818 commit(s) - 38 release item(s) - 25 high-signal repo(s).

## Plain-English Summary

- Azure, PowerShell led the visible product-area activity in this window.
- 38 release item(s) were detected during the window.
- Security-related changes appeared in Azure/azure-sdk-for-rust, Azure/azure-sdk-for-python, microsoft/content-processing-solution-accelerator.
- Start with human-authored changes in Azure/azure-sdk-for-rust, Azure/azure-sdk-for-python, microsoft/content-processing-solution-accelerator, microsoft/Conversation-Knowledge-Mining-Solution-Accelerator.
- 151 event(s) look automated, bot-heavy, dependency, or generated; review the curated sections before raw volume.

## Headline Metrics

| Metric | Value |
| --- | ---: |
| Inventory repositories | 16780 |
| Repositories after filters | 2567 |
| `pushed_at` candidates | 219 |
| Enrichment candidates | 219 |
| Repositories with movement | 141 |
| Default-branch commits | 818 |

## What Changed That Matters

| Repository | Score | Change | Actor | Noise | Headline | Time |
| --- | ---: | --- | --- | --- | --- | --- |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 100 | security_fix | human | low | [Add GitHubActionsCredential to azure_identity](https://github.com/Azure/azure-sdk-for-rust/pull/5588) | `2026-11-12T19:06:44Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 100 | security_fix | human | low | [[Identity] Fix blocking OIDC requests in async AzurePipelinesCredential](https://github.com/Azure/azure-sdk-for-python/pull/49831) | `2026-11-12T18:17:12Z` |
| [microsoft/content-processing-solution-accelerator](https://github.com/microsoft/content-processing-solution-accelerator) | 100 | security_fix | human | low | [fix: restrict Azure authentication and image publishing to non-PR runs](https://github.com/microsoft/content-processing-solution-accelerator/pull/727) | `2026-11-12T17:24:53Z` |
| [microsoft/Conversation-Knowledge-Mining-Solution-Accelerator](https://github.com/microsoft/Conversation-Knowledge-Mining-Solution-Accelerator) | 100 | security_fix | human | low | [fix: Add fork guard to workflow_run deploy and drop production env for PR …](https://github.com/microsoft/Conversation-Knowledge-Mining-Solution-Accelerator/pull/1075) | `2026-11-12T17:24:33Z` |
| [Azure/kars](https://github.com/Azure/kars) | 100 | security_fix | human | low | [ci(headlamp): verify webpack dev middleware compatibility](https://github.com/Azure/kars/pull/619) | `2026-11-12T17:03:32Z` |
| [MicrosoftDocs/dynamics365smb-docs](https://github.com/MicrosoftDocs/dynamics365smb-docs) | 100 | security_fix | human | low | [Refresh security and privacy (#5278)](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/2533bf80fa5ced6ba979842f11447aee85712faf) | `2026-11-12T14:29:22Z` |
| [microsoft/SPARROW](https://github.com/microsoft/SPARROW) | 100 | security_fix | human | low | [deps: patch security alerts in certifi, urllib3, Pillow, filelock](https://github.com/microsoft/SPARROW/pull/92) | `2026-11-12T13:13:27Z` |
| [Azure/dacs](https://github.com/Azure/dacs) | 100 | security_fix | human | low | [ci: scan all built images and upgrade Runai packages](https://github.com/Azure/dacs/pull/181) | `2026-11-11T20:43:56Z` |
| [microsoftgraph/microsoft-graph-docs-contrib](https://github.com/microsoftgraph/microsoft-graph-docs-contrib) | 100 | security_fix | human | low | [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10093) | `2026-11-11T19:06:54Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | 100 | release | unknown | low | [sdk/storage/azfile/v1.8.0-beta.1](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/storage/azfile/v1.8.0-beta.1) | `2026-11-12T20:39:08Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | 100 | release | unknown | low | [sdk/storage/azblob/v1.9.0-beta.1](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/storage/azblob/v1.9.0-beta.1) | `2026-11-12T20:15:23Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 100 | release | unknown | low | [@azure/ai-projects_2.11.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/ai-projects_2.11.0) | `2026-11-12T20:03:34Z` |
| [dotnet/docs](https://github.com/dotnet/docs) | 100 | release | human | low | [Update .NET 11 release documentation](https://github.com/dotnet/docs/pull/56871) | `2026-11-12T18:49:07Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 100 | release | human | low | [[@azure-rest/ai-vision-image-analysis] Change v1.0.0 release date back to Unreleased](https://github.com/Azure/azure-sdk-for-js/pull/40775) | `2026-11-12T18:23:59Z` |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 100 | release | unknown | low | [Release v5.1018.0](https://github.com/Azure/LogicAppsUX/releases/tag/v5.1018.0) | `2026-11-12T17:05:58Z` |

## Product Areas

| Product area | Signal | Repos | Events | Releases | Security | Top links |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Azure | 173 | 59 | 226 | 34 | 6 | [Add GitHubActionsCredential to azure_identity](https://github.com/Azure/azure-sdk-for-rust/pull/5588); [[Identity] Fix blocking OIDC requests in async AzurePipelinesCredential](https://github.com/Azure/azure-sdk-for-python/pull/49831); [fix: restrict Azure authentication and image publishing to non-PR runs](https://github.com/microsoft/content-processing-solution-accelerator/pull/727) |
| Unmapped Activity | 70 | 32 | 103 | 3 | 1 | [deps: patch security alerts in certifi, urllib3, Pillow, filelock](https://github.com/microsoft/SPARROW/pull/92); [Persona Workshop 0.7.1 — native Windows startup repair](https://github.com/microsoft/amplifier-persona-workshop/releases/tag/v0.7.1); [Persona Workshop 0.7.0](https://github.com/microsoft/amplifier-persona-workshop/releases/tag/v0.7.0) |
| PowerShell | 19 | 8 | 20 | 0 | 0 | [feat(open-data): Add meter category to Services to split shared resou…](https://github.com/microsoft/finops-toolkit/commit/6ebd06573435168952b62c048f85ea46d8a2b30a); [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/5e9f6b370edf9a1a56b84d54f1aba5d8b6bf3179); [Update Lab 1D: standardize Cloud Shell and portal wording](https://github.com/MicrosoftLearning/mslearn-sec-identity/pull/28) |
| Microsoft Graph | 17 | 10 | 30 | 0 | 1 | [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10093); [ci: upgrade ESRP release task to v14](https://github.com/microsoftgraph/msgraph-sdk-java/pull/2714); [Document Microsoft Threat Intelligence API rate limit](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10091) |
| .NET | 17 | 17 | 44 | 0 | 0 | [Update .NET 11 release documentation](https://github.com/dotnet/docs/pull/56871); [Add Popup support for AppTheme](https://github.com/MicrosoftDocs/CommunityToolkit/pull/664); [CommunityToolkit.Maui Docs Updates for Device Tests Fixes + Findings](https://github.com/MicrosoftDocs/CommunityToolkit/pull/665) |
| Identity | 15 | 3 | 15 | 0 | 1 | [Refresh security and privacy (#5278)](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/2533bf80fa5ced6ba979842f11447aee85712faf); [docs: add Resource Policy built-in roles (#14780)](https://github.com/MicrosoftDocs/entra-docs/commit/4d1cfd8890e24b3b822d77c485175604b3ae6ad9); [Add video link to early-access-preview-edit-with-copilot.md (#8152)](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/dc20aa40c75ef8638f6de97dfd6be1eae23e96a2) |
| Developer Tools | 12 | 3 | 12 | 1 | 0 | [v0.6.4](https://github.com/microsoft/vscode-custom-data/releases/tag/v0.6.4); [Revise customization guide to use annotated code blocks](https://github.com/microsoft/vscode-docs/pull/10642); [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11492) |
| Microsoft 365 | 12 | 6 | 18 | 0 | 0 | [Add check preflight and check announcement-draft to the release skill](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3212); [Add a Prod validation stage before the Lockbox approval](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3207); [Redirect fixes](https://github.com/MicrosoftDocs/teams-ai-library/commit/4052df1948e8bf060c971c5ab4b6a86aea11e327) |

## Today's Top Links

| Priority | Repository | Why read it |
| ---: | --- | --- |
| 1 | [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | [Security-related change: Add GitHubActionsCredential to azure_identity](https://github.com/Azure/azure-sdk-for-rust/pull/5588) |
| 2 | [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [Security-related change: [Identity] Fix blocking OIDC requests in async AzurePipelinesCredential](https://github.com/Azure/azure-sdk-for-python/pull/49831) |
| 3 | [microsoft/content-processing-solution-accelerator](https://github.com/microsoft/content-processing-solution-accelerator) | [Security-related change: fix: restrict Azure authentication and image publishing to non-PR runs](https://github.com/microsoft/content-processing-solution-accelerator/pull/727) |
| 4 | [microsoft/Conversation-Knowledge-Mining-Solution-Accelerator](https://github.com/microsoft/Conversation-Knowledge-Mining-Solution-Accelerator) | [Security-related change: fix: Add fork guard to workflow_run deploy and drop production env for PR …](https://github.com/microsoft/Conversation-Knowledge-Mining-Solution-Accelerator/pull/1075) |
| 5 | [Azure/kars](https://github.com/Azure/kars) | [Security-related change: ci(headlamp): verify webpack dev middleware compatibility](https://github.com/Azure/kars/pull/619) |
| 6 | [MicrosoftDocs/dynamics365smb-docs](https://github.com/MicrosoftDocs/dynamics365smb-docs) | [Security-related change: Refresh security and privacy (#5278)](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/2533bf80fa5ced6ba979842f11447aee85712faf) |
| 7 | [microsoft/SPARROW](https://github.com/microsoft/SPARROW) | [Security-related change: deps: patch security alerts in certifi, urllib3, Pillow, filelock](https://github.com/microsoft/SPARROW/pull/92) |
| 8 | [Azure/dacs](https://github.com/Azure/dacs) | [Security-related change: ci: scan all built images and upgrade Runai packages](https://github.com/Azure/dacs/pull/181) |

## Noise and Automation

- 151 event(s) look automated, bot-heavy, dependency, generated, or medium/high noise.
- Top noisy repositories: microsoft/kiota-abstractions-go, MicrosoftDocs/architecture-center, Azure/azure-sdk-for-net, Azure-Samples/Legacy-Modernization-Agents, microsoft/kiota-samples.
- Noise mix: Dependency: 70, Docs: 52, SDK: 13, CI/Infra: 10, Release: 3, Sample: 3.

<details>
<summary>Show collection settings and diagnostics</summary>

## Collection Settings

- Categories: `docs, reference, samples, training`
- Include archived: `False`
- Include forks: `False`
- State window: `True`
- Events prefilter: `off`

## Collection Efficiency

| Metric | Value |
| --- | ---: |
| GraphQL mode | two-stage |
| Batch size | 35 |
| Count batches | 7 |
| Detail batches | 5 |
| Repos counted | 219 |
| Repos enriched | 141 |

</details>

<details>
<summary>Show supporting signal, release, and lifecycle tables</summary>

## High-Signal Items

| Repository | Score | Tags |
| --- | ---: | --- |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 160 | docs, human-authored, product:Azure SDK, release, security, watchlist |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 144 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 140 | docs, human-authored, release, release-language, watchlist |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | 139 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 139 | human-authored, product:Azure AI, product:Azure SDK, release, release-language, samples, watchlist |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 136 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 129 | human-authored, release, release-language, samples, watchlist |
| [Azure/kars](https://github.com/Azure/kars) | 122 | docs, human-authored, security, watchlist |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 116 | docs, human-authored, release, watchlist |
| [MicrosoftDocs/dynamics365smb-docs](https://github.com/MicrosoftDocs/dynamics365smb-docs) | 109 | docs, human-authored, security, watchlist |
| [microsoftgraph/microsoft-graph-docs-contrib](https://github.com/microsoftgraph/microsoft-graph-docs-contrib) | 105 | docs, human-authored, product:Microsoft Graph, security, watchlist |
| [microsoft/SPARROW](https://github.com/microsoft/SPARROW) | 105 | human-authored, security, training, watchlist |
| [Azure/dacs](https://github.com/Azure/dacs) | 104 | human-authored, samples, security, watchlist |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 104 | docs, human-authored, product:Azure SDK, security, watchlist |
| [microsoft/content-processing-solution-accelerator](https://github.com/microsoft/content-processing-solution-accelerator) | 101 | human-authored, samples, security, watchlist |

## Watchlist Hits

| Repository | Score | Matches |
| --- | ---: | --- |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 160 | products: Azure SDK; repos: Azure/azure-sdk-for-python; orgs: Azure; keywords: sdk |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 144 | products: Azure SDK; repos: Azure/azure-sdk-for-java; orgs: Azure; keywords: release, sdk |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 140 | orgs: Azure; keywords: release |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | 139 | products: Azure SDK; orgs: Azure; keywords: release, sdk |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 139 | products: Azure AI, Azure SDK; orgs: Azure; keywords: agent, foundry, release, sdk |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 136 | products: Azure SDK; repos: Azure/azure-sdk-for-js; orgs: Azure; keywords: release, sdk |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 129 | keywords: release |
| [Azure/kars](https://github.com/Azure/kars) | 122 | orgs: Azure; keywords: security |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 116 | orgs: Azure |
| [MicrosoftDocs/dynamics365smb-docs](https://github.com/MicrosoftDocs/dynamics365smb-docs) | 109 | orgs: MicrosoftDocs; keywords: security |
| [microsoftgraph/microsoft-graph-docs-contrib](https://github.com/microsoftgraph/microsoft-graph-docs-contrib) | 105 | products: Microsoft Graph; orgs: microsoftgraph; keywords: graph, security |
| [microsoft/SPARROW](https://github.com/microsoft/SPARROW) | 105 | keywords: security |
| [Azure/dacs](https://github.com/Azure/dacs) | 104 | orgs: Azure |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 104 | products: Azure SDK; orgs: Azure; keywords: copilot, sdk |
| [microsoft/content-processing-solution-accelerator](https://github.com/microsoft/content-processing-solution-accelerator) | 101 | keywords: security |

## Releases

| Repository | Release | Published |
| --- | --- | --- |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/storage/azfile/v1.8.0-beta.1](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/storage/azfile/v1.8.0-beta.1) | `2026-11-12T20:39:08Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/storage/azblob/v1.9.0-beta.1](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/storage/azblob/v1.9.0-beta.1) | `2026-11-12T20:15:23Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/ai-projects_2.11.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/ai-projects_2.11.0) | `2026-11-12T20:03:34Z` |
| [microsoft/amplifier-persona-workshop](https://github.com/microsoft/amplifier-persona-workshop) | [Persona Workshop 0.7.1 — native Windows startup repair](https://github.com/microsoft/amplifier-persona-workshop/releases/tag/v0.7.1) | `2026-11-12T18:04:50Z` |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | [Release v5.1018.0](https://github.com/Azure/LogicAppsUX/releases/tag/v5.1018.0) | `2026-11-12T17:05:58Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.Provisioning.AppContainers_1.3.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Provisioning.AppContainers_1.3.0) | `2026-11-12T16:44:57Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure+azure-sdk-bom_1.3.10](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-sdk-bom_1.3.10) | `2026-11-12T15:39:39Z` |
| [microsoft/amplifier-persona-workshop](https://github.com/microsoft/amplifier-persona-workshop) | [Persona Workshop 0.7.0](https://github.com/microsoft/amplifier-persona-workshop/releases/tag/v0.7.0) | `2026-11-12T15:09:38Z` |
| [microsoft/vscode-custom-data](https://github.com/microsoft/vscode-custom-data) | [v0.6.4](https://github.com/microsoft/vscode-custom-data/releases/tag/v0.6.4) | `2026-11-12T14:43:56Z` |
| [microsoft/amplifier-acp-lab](https://github.com/microsoft/amplifier-acp-lab) | [Lab 0.4.1 — self-contained native packages](https://github.com/microsoft/amplifier-acp-lab/releases/tag/v0.4.1) | `2026-11-12T13:03:57Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-mgmt-containerservice_41.9.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-containerservice_41.9.0) | `2026-11-12T12:22:26Z` |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | [azd-ext-azure-ai-agents_1.1.0](https://github.com/Azure/azure-dev/releases/tag/azd-ext-azure-ai-agents_1.1.0) | `2026-11-12T11:27:22Z` |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | [azd-ext-azure-ai-projects_1.1.0](https://github.com/Azure/azure-dev/releases/tag/azd-ext-azure-ai-projects_1.1.0) | `2026-11-12T10:58:47Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [managedcleanroom 1.0.0b11](https://github.com/Azure/azure-cli-extensions/releases/tag/managedcleanroom-1.0.0b11) | `2026-11-12T10:32:52Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-mgmt-koreaiartemis_1.0.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-koreaiartemis_1.0.0b1) | `2026-11-12T10:29:26Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-containerinstance_10.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-containerinstance_10.0.0) | `2026-11-12T10:21:11Z` |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | [azd-ext-azure-ai-toolboxes_1.1.0](https://github.com/Azure/azure-dev/releases/tag/azd-ext-azure-ai-toolboxes_1.1.0) | `2026-11-12T10:19:06Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [cosmosdb-preview 2.0.0](https://github.com/Azure/azure-cli-extensions/releases/tag/cosmosdb-preview-2.0.0) | `2026-11-12T10:09:03Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-mgmt-containerinstance_11.0.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-containerinstance_11.0.0) | `2026-11-12T09:27:54Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/resourcemanager/containerservicefleet/armcontainerservicefleet/v3.1.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/containerservicefleet/armcontainerservicefleet/v3.1.0) | `2026-11-12T09:13:05Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure.resourcemanager+azure-resourcemanager-containerservicefleet_1.4.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-containerservicefleet_1.4.0) | `2026-11-12T09:00:11Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure.resourcemanager+azure-resourcemanager-containerinstance_2.55.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-containerinstance_2.55.0) | `2026-11-12T08:37:23Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.Security.KeyVault.Secrets_4.13.0-beta.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Security.KeyVault.Secrets_4.13.0-beta.1) | `2026-11-12T08:04:41Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.Security.KeyVault.Certificates_4.11.0-beta.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Security.KeyVault.Certificates_4.11.0-beta.1) | `2026-11-12T08:02:34Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.Security.KeyVault.Keys_4.11.0-beta.6](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Security.KeyVault.Keys_4.11.0-beta.6) | `2026-11-12T08:01:45Z` |

## Repository Lifecycle

| Change | Count |
| --- | ---: |
| archived_changed | 2 |
| category_changed | 0 |
| default_branch_changed | 2 |
| fork_changed | 0 |
| new_repos | 10 |
| removed_repos | 0 |

## Category Summary

| Category | Repositories |
| --- | ---: |
| docs | 88 |
| samples | 43 |
| training | 10 |

## Organization Summary

| Org | Repositories |
| --- | ---: |
| microsoft | 40 |
| MicrosoftDocs | 37 |
| Azure | 21 |
| Azure-Samples | 16 |
| dotnet | 16 |
| microsoftgraph | 4 |
| MicrosoftLearning | 3 |
| OfficeDev | 3 |
| SharePoint | 1 |

</details>

<details>
<summary>Show raw repository activity</summary>

## Busiest Repositories

| Repository | Signal | Category | Commits | Releases | Newest commit |
| --- | ---: | --- | ---: | ---: | --- |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 160 | docs | 20 | 5 | `2026-11-12T20:55:34Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 144 | docs | 19 | 4 | `2026-11-12T20:56:48Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 140 | docs | 15 | 5 | `2026-11-12T10:31:48Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | 139 | docs | 14 | 5 | `2026-11-12T20:49:30Z` |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 139 | samples | 14 | 3 | `2026-11-12T14:52:50Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 136 | docs | 11 | 5 | `2026-11-12T18:23:59Z` |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 129 | samples | 4 | 1 | `2026-11-12T01:40:30Z` |
| [Azure/kars](https://github.com/Azure/kars) | 122 | docs | 22 | 0 | `2026-11-12T17:03:32Z` |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 116 | docs | 1 | 1 | `2026-11-12T18:19:09Z` |
| [MicrosoftDocs/dynamics365smb-docs](https://github.com/MicrosoftDocs/dynamics365smb-docs) | 109 | docs | 9 | 0 | `2026-11-12T19:03:39Z` |
| [microsoftgraph/microsoft-graph-docs-contrib](https://github.com/microsoftgraph/microsoft-graph-docs-contrib) | 105 | docs | 5 | 0 | `2026-11-12T15:12:38Z` |
| [microsoft/SPARROW](https://github.com/microsoft/SPARROW) | 105 | training | 5 | 0 | `2026-11-12T13:45:56Z` |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 104 | docs | 4 | 0 | `2026-11-12T19:31:19Z` |
| [Azure/dacs](https://github.com/Azure/dacs) | 104 | samples | 4 | 0 | `2026-11-11T20:43:56Z` |
| [microsoft/content-processing-solution-accelerator](https://github.com/microsoft/content-processing-solution-accelerator) | 101 | samples | 1 | 0 | `2026-11-12T17:24:53Z` |
| [microsoft/Conversation-Knowledge-Mining-Solution-Accelerator](https://github.com/microsoft/Conversation-Knowledge-Mining-Solution-Accelerator) | 101 | samples | 1 | 0 | `2026-11-12T17:24:33Z` |
| [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs) | 100 | docs | 43 | 0 | `2026-11-12T18:18:05Z` |
| [Azure-Samples/Legacy-Modernization-Agents](https://github.com/Azure-Samples/Legacy-Modernization-Agents) | 100 | samples | 26 | 0 | `2026-11-12T14:47:19Z` |
| [MicrosoftDocs/learn](https://github.com/MicrosoftDocs/learn) | 95 | docs | 20 | 0 | `2026-11-12T18:19:45Z` |
| [MicrosoftDocs/fabric-docs](https://github.com/MicrosoftDocs/fabric-docs) | 95 | docs | 20 | 0 | `2026-11-12T15:15:11Z` |

## Repository Details

### dotnet/runtime (48 commit(s), signal 65)

Tags: `docs, human-authored`

- [Preserve exception order when head merging ordered statements (#137254)](https://github.com/dotnet/runtime/commit/c4cecc4ce5973bb62b85590f6be473ba8c70372d) - `2026-11-12T20:20:28Z` - Nino Floris (@NinoFloris) - PR: [Preserve exception order when head merging ordered statements](https://github.com/dotnet/runtime/pull/137254)
- [JIT: preserve exception order after hoist rejection (#137118)](https://github.com/dotnet/runtime/commit/68b16fb02735b0002495191823371f9e494ce489) - `2026-11-12T19:24:05Z` - Andy Ayers (@AndyAyersMS) - PR: [JIT: preserve exception order after hoist rejection](https://github.com/dotnet/runtime/pull/137118)
- [[wasm][coreclr] Check WBT crossgen2 debug-info arguments by evaluatio…](https://github.com/dotnet/runtime/commit/c721e68776f4804beb01b6e9c5be121e04fba59a) - `2026-11-12T19:14:22Z` - Larry Ewing (@lewing) - PR: [[wasm][coreclr] Check WBT crossgen2 debug-info arguments by evaluation](https://github.com/dotnet/runtime/pull/137360)
- [Use SRM 10 for ILAssembler's downlevel dependency (#137405)](https://github.com/dotnet/runtime/commit/ec82c3f1e58d979155d7aa05f95c6918d5d18726) - `2026-11-12T18:48:02Z` - Jeremy Koritzinsky (@jkoritzinsky) - PR: [Use SRM 10 for ILAssembler's downlevel dependency](https://github.com/dotnet/runtime/pull/137405)
- [[wasm] Remove dead BuildOnlyAfterPublish option from Wasm.Build.Tests…](https://github.com/dotnet/runtime/commit/bd67423b1f1e4d5d0c545be3f8ca8488c0cd966e) - `2026-11-12T18:47:24Z` - Larry Ewing (@lewing) - PR: [[wasm] Remove dead BuildOnlyAfterPublish option from Wasm.Build.Tests](https://github.com/dotnet/runtime/pull/137370)

### MicrosoftDocs/azure-docs (43 commit(s), signal 100)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-do…](https://github.com/MicrosoftDocs/azure-docs/commit/725e3aa1aff84373da86de1b0b2dc0746b1086c6) - `2026-11-12T18:18:05Z` - Learn Build Service GitHub App
- [Merge pull request #322477 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-docs/commit/f9bdbced4af0580f6746dc0268314195a8d41073) - `2026-11-12T18:17:07Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Async delete (#321123)](https://github.com/MicrosoftDocs/azure-docs/commit/41015c21afa88ed02bfb3314b807076f9394f47e) - `2026-11-12T18:00:36Z` - Manish Chabbria (@netapp-manishc)
- [[DO NOT MERGE before November 12, 2026] Add Azure Data Share retireme…](https://github.com/MicrosoftDocs/azure-docs/commit/db0c5bc6320b42043dc42605808d3bca4c39abd5) - `2026-11-12T17:03:09Z` - Sita Dontharaju (@sidontha)
- [Merging changes synced from https://github.com/MicrosoftDocs/azure-do…](https://github.com/MicrosoftDocs/azure-docs/commit/cc2c4fe5aab1380cc931e4bd64f5ec1154205310) - `2026-11-12T06:09:26Z` - Learn Build Service GitHub App

### Azure-Samples/Legacy-Modernization-Agents (26 commit(s), signal 100)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Merge pull request #205 from Azure-Samples/pr/05-docs](https://github.com/Azure-Samples/Legacy-Modernization-Agents/commit/948e08919c16c38c831f6b1aa46983125b38feb8) - `2026-11-12T14:47:19Z` - Gustav Kaleta (@gkaleta) - PR: [Parser tooling: REKT patches, dependency evidence and source identity tools](https://github.com/Azure-Samples/Legacy-Modernization-Agents/pull/201)
- [Docs: same-file chunks convert in order](https://github.com/Azure-Samples/Legacy-Modernization-Agents/commit/3ebe63eb5ba229f777dac6561e28c4854084a088) - `2026-11-12T14:42:55Z` - Gustav Kaleta (@gkaleta) - PR: [Parser tooling: REKT patches, dependency evidence and source identity tools](https://github.com/Azure-Samples/Legacy-Modernization-Agents/pull/201)
- [Docs: explicit Spring selection; score without regenerating prompts](https://github.com/Azure-Samples/Legacy-Modernization-Agents/commit/d2a89912d6d6558727742b2d76884afcc179d27c) - `2026-11-12T14:42:54Z` - Gustav Kaleta (@gkaleta) - PR: [Parser tooling: REKT patches, dependency evidence and source identity tools](https://github.com/Azure-Samples/Legacy-Modernization-Agents/pull/201)
- [Address Copilot review on docs](https://github.com/Azure-Samples/Legacy-Modernization-Agents/commit/2ea491c9d4c72511cd90699c399efb2fe8482f2b) - `2026-11-12T14:42:54Z` - Gustav Kaleta (@gkaleta) - PR: [Parser tooling: REKT patches, dependency evidence and source identity tools](https://github.com/Azure-Samples/Legacy-Modernization-Agents/pull/201)
- [Docs: portal demo GIFs, guides and changelog](https://github.com/Azure-Samples/Legacy-Modernization-Agents/commit/d93a0b8766178029db03183e14eab82c49b1aa49) - `2026-11-12T14:42:54Z` - Gustav Kaleta (@gkaleta) - PR: [Parser tooling: REKT patches, dependency evidence and source identity tools](https://github.com/Azure-Samples/Legacy-Modernization-Agents/pull/201)

### Azure/kars (22 commit(s), signal 122)

Tags: `docs, human-authored, security, watchlist`

- [Merge pull request #619 from Azure/pallakatos-headlamp-security-valid…](https://github.com/Azure/kars/commit/6dd79763ecc8d1cb295cc2ebc109c76824208f1e) - `2026-11-12T17:03:32Z` - Pal Lakatos-Toth (@pallakatos) - PR: [ci(headlamp): verify webpack dev middleware compatibility](https://github.com/Azure/kars/pull/619)
- [test(headlamp): isolate start watch-copy smoke test](https://github.com/Azure/kars/commit/c9fe3f824be16f5be282fba3f785c7a3701238e1) - `2026-11-12T11:10:40Z` - pallakatos (@pallakatos) - PR: [ci(headlamp): verify webpack dev middleware compatibility](https://github.com/Azure/kars/pull/619)
- [fix(headlamp): bind smoke snapshots to file handles](https://github.com/Azure/kars/commit/3924dfd389e1656c85cff1561fa0ca29efe18b77) - `2026-11-12T10:46:07Z` - pallakatos (@pallakatos) - PR: [ci(headlamp): verify webpack dev middleware compatibility](https://github.com/Azure/kars/pull/619)
- [test(headlamp): verify start watch and copy flow](https://github.com/Azure/kars/commit/534539560c49e279d86866b0195e77db2e82d270) - `2026-11-12T10:33:53Z` - pallakatos (@pallakatos) - PR: [ci(headlamp): verify webpack dev middleware compatibility](https://github.com/Azure/kars/pull/619)
- [test(headlamp): verify start build-watch workflow](https://github.com/Azure/kars/commit/54f634499b711bd19dee76b48f571747df589c9f) - `2026-11-12T10:20:24Z` - pallakatos (@pallakatos) - PR: [ci(headlamp): verify webpack dev middleware compatibility](https://github.com/Azure/kars/pull/619)

### Azure/azure-sdk-for-python (20 commit(s), signal 160)

Tags: `docs, human-authored, product:Azure SDK, release, security, watchlist`

- Release: [azure-mgmt-containerservice_41.9.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-containerservice_41.9.0) - `2026-11-12T12:22:26Z`
- Release: [azure-mgmt-koreaiartemis_1.0.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-koreaiartemis_1.0.0b1) - `2026-11-12T10:29:26Z`
- Release: [azure-mgmt-containerinstance_11.0.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-containerinstance_11.0.0) - `2026-11-12T09:27:54Z`
- Release: [azure-data-ai_1.0.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-data-ai_1.0.0) - `2026-11-12T03:05:37Z`
- Release: [azure-mgmt-containerservicefleet_4.1.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-containerservicefleet_4.1.0) - `2026-11-12T01:36:16Z`
- [Update apiview-properties.json and tsp-location.yaml with new model m…](https://github.com/Azure/azure-sdk-for-python/commit/423b7bf59adcc7849e42d6e0e420c4b372a5c316) - `2026-11-12T20:55:34Z` - Howie Leung (@howieleung) - PR: [Update apiview-properties.json and tsp-location.yaml with new model mappings and commit reference](https://github.com/Azure/azure-sdk-for-python/pull/49989)
- [Skip corehttp DNS-dependent streaming tests (#49991)](https://github.com/Azure/azure-sdk-for-python/commit/a0fb1b1ed691683a3711e3b651ebf5a353e016eb) - `2026-11-12T20:47:31Z` - Libba Lawrence (@l0lawrence) - PR: [[Core] Skip corehttp DNS-dependent streaming tests for 1ES proxy](https://github.com/Azure/azure-sdk-for-python/pull/49991)
- [[Core] skip DNS-dependent streaming tests for 1ES proxy (#49900)](https://github.com/Azure/azure-sdk-for-python/commit/43d332bc1261f4959238a275778d75398474074f) - `2026-11-12T18:40:38Z` - Libba Lawrence (@l0lawrence) - PR: [[Core] skip DNS-dependent streaming tests for 1ES proxy](https://github.com/Azure/azure-sdk-for-python/pull/49900)
- [[Identity] Fix blocking OIDC requests in async AzurePipelinesCredenti…](https://github.com/Azure/azure-sdk-for-python/commit/aa076afa4330928641976e4ced5377ccc3331ae2) - `2026-11-12T18:17:12Z` - jenny (@JennyPng) - PR: [[Identity] Fix blocking OIDC requests in async AzurePipelinesCredential](https://github.com/Azure/azure-sdk-for-python/pull/49831)
- [[Key Vault] Regenerated Keys and Administration SDKs (#49983)](https://github.com/Azure/azure-sdk-for-python/commit/09a176ef34d4190ccda0fc5688ee2eee81d4f426) - `2026-11-12T17:36:24Z` - Nicola Camillucci (@ncamillucci) - PR: [[Key Vault] Regenerated Keys and Administration SDKs](https://github.com/Azure/azure-sdk-for-python/pull/49983)

### MicrosoftDocs/architecture-center (20 commit(s), signal 45)

Tags: `bot-only, docs, watchlist`

- [Merge pull request #17369 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/architecture-center/commit/c75323268bb51a7711d4185b8a8a686c13a6b777) - `2026-11-12T18:33:30Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #17363 from MicrosoftDocs/quality-signals/packet-w…](https://github.com/MicrosoftDocs/architecture-center/commit/072b323b951b88dfeb8b4ec396220623cdbbe328) - `2026-11-12T13:32:30Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #17361 from MicrosoftDocs/quality-signals/clarify-…](https://github.com/MicrosoftDocs/architecture-center/commit/a69f5118ce6a255877834fc0ed1fe10db84897b7) - `2026-11-12T13:29:55Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Clarify design-specific packet walk references](https://github.com/MicrosoftDocs/architecture-center/commit/e5168ecf164cec8458401402684e358104665a9c) - `2026-11-12T09:49:04Z` - azure-patterns-practices-assistant[bot] (@azure-patterns-practices-assistant[bot])
- [Merge pull request #17362 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/architecture-center/commit/70823d67947d3b0506a5a27766fc6dfe0b0bc749) - `2026-11-12T06:01:52Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### MicrosoftDocs/learn (20 commit(s), signal 95)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/6cffbe5d9662d13617d0b0d0b2e8a3d6b2a8d658) - `2026-11-12T18:19:45Z` - Learn Build Service GitHub App
- [Merge pull request #56817 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/learn/commit/4a8fce337877cc98ae6d9a5094d78924bf1d3c32) - `2026-11-12T18:10:43Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #56771 from v-antonyvieira/removing-reference-gith…](https://github.com/MicrosoftDocs/learn/commit/cede6a21d5f4e050e71b4be579529bd186e22f0c) - `2026-11-12T16:19:47Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/af8305f2aa97a004fe7667484a7e1f4ede3d0937) - `2026-11-12T12:19:56Z` - Learn Build Service GitHub App
- [Merge pull request #56812 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/learn/commit/78d1cb701cdf139da5165758104f54bfbd61e9ef) - `2026-11-12T12:09:42Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### MicrosoftDocs/fabric-docs (20 commit(s), signal 95)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #3513 from MicrosoftDocs/main639300932931625366syn…](https://github.com/MicrosoftDocs/fabric-docs/commit/3ae7afc73169ac57b874d5aee09217bb35a4f8fc) - `2026-11-12T15:15:11Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3513)
- [Merging changes synced from https://github.com/MicrosoftDocs/fabric-d…](https://github.com/MicrosoftDocs/fabric-docs/commit/86e28e7b449ea7ec2ba7f9f72d2b4f3c5611666f) - `2026-11-12T15:14:50Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3513)
- [Merge pull request #17374 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/fabric-docs/commit/e14874fe0c003106e77f488d658f6df9d93d7981) - `2026-11-12T15:11:14Z` - Ryan Thompson (@thomps23) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3513)
- [Revert "Scripting functions v3 (#17344)" (#17373)](https://github.com/MicrosoftDocs/fabric-docs/commit/282cbb25e4c599b36819f526d32220b79442f706) - `2026-11-12T15:08:18Z` - Ryan Thompson (@thomps23) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3513)
- [Merge pull request #3511 from MicrosoftDocs/main639300604188656815syn…](https://github.com/MicrosoftDocs/fabric-docs/commit/b80844ffe57bdb9eac3cd7e4c75831cdf4bb32ea) - `2026-11-12T06:07:15Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3511)

### Azure/azure-sdk-for-java (19 commit(s), signal 144)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [com.azure+azure-sdk-bom_1.3.10](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-sdk-bom_1.3.10) - `2026-11-12T15:39:39Z`
- Release: [com.azure.resourcemanager+azure-resourcemanager-containerservicefleet_1.4.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-containerservicefleet_1.4.0) - `2026-11-12T09:00:11Z`
- Release: [com.azure.resourcemanager+azure-resourcemanager-containerinstance_2.55.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-containerinstance_2.55.0) - `2026-11-12T08:37:23Z`
- Release: [com.azure.resourcemanager+azure-resourcemanager-containerservice_2.67.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-containerservice_2.67.0) - `2026-11-12T07:07:37Z`
- [[Storage] Fix and consolidate beginCopy option validation in File Sha…](https://github.com/Azure/azure-sdk-for-java/commit/e88719dccf37c22f736f122605845df4355630b3) - `2026-11-12T20:56:48Z` - Isabelle (@ibrandes) - PR: [[Storage] Fix and consolidate beginCopy option validation in File Share clients](https://github.com/Azure/azure-sdk-for-java/pull/51218)
- [[Core] Add opt-in streaming of BinaryData responses to async RestProx…](https://github.com/Azure/azure-sdk-for-java/commit/2dd8568beede881908105612f2bcda778e3309b2) - `2026-11-12T20:21:35Z` - Isabelle (@ibrandes) - PR: [[Core] Add opt-in streaming of BinaryData responses to async RestProxy](https://github.com/Azure/azure-sdk-for-java/pull/51222)
- [Fix Cosmos metadata monitor subscription cleanup (#50593)](https://github.com/Azure/azure-sdk-for-java/commit/c56983eca66126fada8c1ecb7d5fcbec7ee0ff5b) - `2026-11-12T18:08:25Z` - nkokitkar (@nkokitkar) - PR: [Fix Cosmos metadata monitor subscription cleanup](https://github.com/Azure/azure-sdk-for-java/pull/50593)
- [Update BOM to version 1.3.10 and refresh dependency versions (#51216)](https://github.com/Azure/azure-sdk-for-java/commit/c86950b1f3a9b1b1eb6d5f25fe849ace0fba5e6e) - `2026-11-12T14:37:29Z` - Jair Myree (@jairmyree) - PR: [Update BOM to version 1.3.10 and refresh dependency versions](https://github.com/Azure/azure-sdk-for-java/pull/51216)
- [Prepare Web PubSub Chat beta.2 release notes (#51229)](https://github.com/Azure/azure-sdk-for-java/commit/af1d0f516a74dadab66cf2c9f49183ffd26ae3fd) - `2026-11-12T14:10:48Z` - yzt (@Y-Sindo) - PR: [Prepare Web PubSub Chat 1.0.0-beta.2 release notes](https://github.com/Azure/azure-sdk-for-java/pull/51229)

### Azure/azure-sdk-for-net (19 commit(s), signal 94)

Tags: `bot-only, docs, product:Azure SDK, release, release-language, watchlist`

- Release: [Azure.Provisioning.AppContainers_1.3.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Provisioning.AppContainers_1.3.0) - `2026-11-12T16:44:57Z`
- Release: [Azure.Security.KeyVault.Secrets_4.13.0-beta.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Security.KeyVault.Secrets_4.13.0-beta.1) - `2026-11-12T08:04:41Z`
- Release: [Azure.Security.KeyVault.Certificates_4.11.0-beta.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Security.KeyVault.Certificates_4.11.0-beta.1) - `2026-11-12T08:02:34Z`
- Release: [Azure.Security.KeyVault.Keys_4.11.0-beta.6](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Security.KeyVault.Keys_4.11.0-beta.6) - `2026-11-12T08:01:45Z`
- Release: [Azure.Security.KeyVault.Administration_4.9.0-beta.5](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Security.KeyVault.Administration_4.9.0-beta.5) - `2026-11-12T08:01:40Z`
- [Increment version for privatedns releases (#64861)](https://github.com/Azure/azure-sdk-for-net/commit/515a1f7193a0f514dd0b4215f6f511977dd987bc) - `2026-11-12T18:28:09Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment version for privatedns releases](https://github.com/Azure/azure-sdk-for-net/pull/64861)
- [Increment package version after release of Azure.ResourceManager.Sove…](https://github.com/Azure/azure-sdk-for-net/commit/0b218e06fe24bead6945e0168a3dee8c465b73d3) - `2026-11-12T18:27:06Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment version for sovereign releases](https://github.com/Azure/azure-sdk-for-net/pull/64873)
- [Increment package version after release of Azure.ResourceManager.Redi…](https://github.com/Azure/azure-sdk-for-net/commit/7c0c51683b90708d3c162d6e6e1172e4196836b3) - `2026-11-12T18:26:43Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment version for redisenterprise releases](https://github.com/Azure/azure-sdk-for-net/pull/64878)
- [Increment package version after release of Azure.ResourceManager.Comp…](https://github.com/Azure/azure-sdk-for-net/commit/abfd3f2c71bcca534844b43a643cbff84756c4db) - `2026-11-12T18:26:04Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment version for computerecommender releases](https://github.com/Azure/azure-sdk-for-net/pull/64895)
- [Increment version for keyvault releases (#64897)](https://github.com/Azure/azure-sdk-for-net/commit/15bef480997023ebd6e4a98bff357c0ff534e717) - `2026-11-12T18:24:09Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment version for keyvault releases](https://github.com/Azure/azure-sdk-for-net/pull/64897)

### microsoft/onnxruntime (15 commit(s), signal 90)

Tags: `human-authored, product:Microsoft Graph, samples, watchlist`

- [cap SBGEMM non-packed K stride at Strides.K (#34146)](https://github.com/microsoft/onnxruntime/commit/6596e0c865fffe234426429a3277a5d27f07706d) - `2026-11-12T20:15:09Z` - Andreas Eriksen (@andreer) - PR: [cap SBGEMM non-packed K stride at Strides.K](https://github.com/microsoft/onnxruntime/pull/34146)
- [Pin patched cryptography for dashboard dependencies (#33942)](https://github.com/microsoft/onnxruntime/commit/a8246c0d094f1ab0d6bf236228e5e67683321cd7) - `2026-11-12T18:22:20Z` - eserscor (@eserscor) - PR: [Pin patched cryptography for dashboard dependencies](https://github.com/microsoft/onnxruntime/pull/33942)
- [Fix OneCore CRT selection for Spectre builds (#33139)](https://github.com/microsoft/onnxruntime/commit/06a9e6a692e69d45446e80ac279fd4f67c951153) - `2026-11-12T17:50:36Z` - adrastogi (@adrastogi) - PR: [Fix OneCore CRT selection for Spectre builds](https://github.com/microsoft/onnxruntime/pull/33139)
- [Widen CUDA tolerance for chained DQ->MatMulNBits fusion test (#32388)](https://github.com/microsoft/onnxruntime/commit/80d281cc521cfe1630da487042e22d9e1bdcf005) - `2026-11-12T17:35:29Z` - Arne H Juul (@arnej27959) - PR: [Widen CUDA tolerance for chained DQ->MatMulNBits fusion test](https://github.com/microsoft/onnxruntime/pull/32388)
- [Bump microsoft/onnxruntime-github-actions/run-build-script-in-docker …](https://github.com/microsoft/onnxruntime/commit/cc8a72e1009d32295b23e666d7eebd9350e1e2b4) - `2026-11-12T15:33:58Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump microsoft/onnxruntime-github-actions/run-build-script-in-docker from 0.0.12 to 0.0.14](https://github.com/microsoft/onnxruntime/pull/34133)

### MicrosoftDocs/powerapps-docs (15 commit(s), signal 90)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/powerapp…](https://github.com/MicrosoftDocs/powerapps-docs/commit/b2b1c76b51484d3d8b3293fc0e2bc95409bb3f90) - `2026-11-12T19:06:28Z` - Learn Build Service GitHub App
- [Merge pull request #12852 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/powerapps-docs/commit/887e65730860519cb84ecef9966d6976369276dd) - `2026-11-12T19:04:19Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Remove Azure Synapse Link configuration transport article (#12850)](https://github.com/MicrosoftDocs/powerapps-docs/commit/218eb06fe07fe1cf5967505c151468ebbbb87bd9) - `2026-11-12T18:05:39Z` - Anirudha Bakore (@anibakore-msft)
- [Modern fluent design updates](https://github.com/MicrosoftDocs/powerapps-docs/commit/7ede7b147efe2dd13d264b962357b8aa1d368efc) - `2026-11-12T16:18:11Z` - Jason Green (@jasongre)
- [Rename GHCP to Microsoft harness (#12789)](https://github.com/MicrosoftDocs/powerapps-docs/commit/90f2a63ef6a1f50d65c08976004d0bd3f78ba9ed) - `2026-11-12T15:46:57Z` - Nathalie Laroche (@nathlaroche)

### Azure/azure-cli-extensions (15 commit(s), signal 140)

Tags: `docs, human-authored, release, release-language, watchlist`

- Release: [managedcleanroom 1.0.0b11](https://github.com/Azure/azure-cli-extensions/releases/tag/managedcleanroom-1.0.0b11) - `2026-11-12T10:32:52Z`
- Release: [cosmosdb-preview 2.0.0](https://github.com/Azure/azure-cli-extensions/releases/tag/cosmosdb-preview-2.0.0) - `2026-11-12T10:09:03Z`
- Release: [storage-discovery 1.1.0b1](https://github.com/Azure/azure-cli-extensions/releases/tag/storage-discovery-1.1.0b1) - `2026-11-12T06:41:36Z`
- Release: [elastic-san 2.0.0b1](https://github.com/Azure/azure-cli-extensions/releases/tag/elastic-san-2.0.0b1) - `2026-11-12T04:32:54Z`
- Release: [storage-mover 1.4.0](https://github.com/Azure/azure-cli-extensions/releases/tag/storage-mover-1.4.0) - `2026-11-11T22:52:53Z`
- [[Release] Update index.json for extension [ managedcleanroom-1.0.0b11 ]](https://github.com/Azure/azure-cli-extensions/commit/cbe44b45a414fe2d3250f98118e864f39214e25d) - `2026-11-12T10:31:48Z` - Azure CLI Team (@azclibot)
- [[ManagedCleanroom] Support CGS as secure key release authority for CP…](https://github.com/Azure/azure-cli-extensions/commit/7273727aa40849b8040c3386e9670c40657748ec) - `2026-11-12T10:14:21Z` - imddanish (@imddanish) - PR: [[ManagedCleanroom] Support CGS as secure key release authority for CPK datasets](https://github.com/Azure/azure-cli-extensions/pull/10545)
- [[Release] Update index.json for extension [ cosmosdb-preview-2.0.0 ]](https://github.com/Azure/azure-cli-extensions/commit/a825484701c3d5e2b2639623af74b84ce4094b01) - `2026-11-12T10:07:59Z` - Azure CLI Team (@azclibot)
- [[CosmosDB] Default copy jobs to source hosting with destination opt-o…](https://github.com/Azure/azure-cli-extensions/commit/1c0d4a5828aeeaab2e7ee4fa53e1314330225221) - `2026-11-12T09:50:34Z` - aditishree1 (@aditishree1) - PR: [[CosmosDB] Default copy jobs to source hosting with destination opt-out](https://github.com/Azure/azure-cli-extensions/pull/10564)
- [[Release] Update index.json for extension [ storage-discovery-1.1.0b1 ]](https://github.com/Azure/azure-cli-extensions/commit/71db6483c3ba8abab0730e3947d657e7591897df) - `2026-11-12T06:40:36Z` - Azure CLI Team (@azclibot)

### Azure/azure-sdk-for-go (14 commit(s), signal 139)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [sdk/storage/azfile/v1.8.0-beta.1](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/storage/azfile/v1.8.0-beta.1) - `2026-11-12T20:39:08Z`
- Release: [sdk/storage/azblob/v1.9.0-beta.1](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/storage/azblob/v1.9.0-beta.1) - `2026-11-12T20:15:23Z`
- Release: [sdk/resourcemanager/containerservicefleet/armcontainerservicefleet/v3.1.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/containerservicefleet/armcontainerservicefleet/v3.1.0) - `2026-11-12T09:13:05Z`
- Release: [sdk/resourcemanager/containerinstance/armcontainerinstance/v3.0.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/containerinstance/armcontainerinstance/v3.0.0) - `2026-11-12T07:52:53Z`
- Release: [sdk/resourcemanager/cosmos/armcosmos/v4.1.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/cosmos/armcosmos/v4.1.0) - `2026-11-12T04:32:39Z`
- [Update azdatalake to azblob v1.9.0-beta.1 (#28031)](https://github.com/Azure/azure-sdk-for-go/commit/7d0928704d6b9a7e958ac9fcff330329db1d3ce7) - `2026-11-12T20:49:30Z` - gunjansingh-msft (@gunjansingh-msft) - PR: [[Storage] Update azdatalake to azblob v1.9.0-beta.1](https://github.com/Azure/azure-sdk-for-go/pull/28031)
- [azcosmos: Escape and validate Cosmos resource IDs (#27997)](https://github.com/Azure/azure-sdk-for-go/commit/dffaa791a8ef8084fe9d7d92cb1bc36e252a0657) - `2026-11-12T20:00:08Z` - Simon Moreno (@simorenoh) - PR: [azcosmos: Escape and validate Cosmos resource IDs](https://github.com/Azure/azure-sdk-for-go/pull/27997)
- [Add Skip.LiveTests CI varaible (#28029)](https://github.com/Azure/azure-sdk-for-go/commit/ac9aab7db7e954228f35202ccb5459bfe0569fd8) - `2026-11-12T19:14:44Z` - Joel Hendrix (@jhendrixMSFT) - PR: [Add Skip.LiveTests CI varaible](https://github.com/Azure/azure-sdk-for-go/pull/28029)
- [azcosmos: fix ReadManyItems partition key routing (#28027)](https://github.com/Azure/azure-sdk-for-go/commit/7da5550a3e7dab9cd299ecbd67c61417882e6dee) - `2026-11-12T19:01:05Z` - Simon Moreno (@simorenoh) - PR: [azcosmos: fix ReadManyItems partition key routing](https://github.com/Azure/azure-sdk-for-go/pull/28027)
- [Prepare azfile 1.8.0-beta.1 for release (#28026)](https://github.com/Azure/azure-sdk-for-go/commit/4ebf26430f7924be0644418101ccfd74da1ed917) - `2026-11-12T13:57:54Z` - gunjansingh-msft (@gunjansingh-msft) - PR: [[Storage] Prepare azfile 1.8.0-beta.1 for release](https://github.com/Azure/azure-sdk-for-go/pull/28026)

### Azure/azure-dev (14 commit(s), signal 139)

Tags: `human-authored, product:Azure AI, product:Azure SDK, release, release-language, samples, watchlist`

- Release: [azd-ext-azure-ai-agents_1.1.0](https://github.com/Azure/azure-dev/releases/tag/azd-ext-azure-ai-agents_1.1.0) - `2026-11-12T11:27:22Z`
- Release: [azd-ext-azure-ai-projects_1.1.0](https://github.com/Azure/azure-dev/releases/tag/azd-ext-azure-ai-projects_1.1.0) - `2026-11-12T10:58:47Z`
- Release: [azd-ext-azure-ai-toolboxes_1.1.0](https://github.com/Azure/azure-dev/releases/tag/azd-ext-azure-ai-toolboxes_1.1.0) - `2026-11-12T10:19:06Z`
- [Publish microsoft.foundry 1.1.0 to extension registry (#10919)](https://github.com/Azure/azure-dev/commit/3b30d4adcd009fc979d6cf7019eac2fe2ad12053) - `2026-11-12T14:52:50Z` - Hui Miao (@huimiu) - PR: [Publish microsoft.foundry 1.1.0 to extension registry](https://github.com/Azure/azure-dev/pull/10919)
- [[azure.ai.agents] Registry update for 1.1.0 (#10918)](https://github.com/Azure/azure-dev/commit/595bab781873ac6b1971fd822d1baf1b6fdd2f1d) - `2026-11-12T12:00:22Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[azure.ai.agents] Registry update for 1.1.0](https://github.com/Azure/azure-dev/pull/10918)
- [[azure.ai.projects] Registry update for 1.1.0 (#10917)](https://github.com/Azure/azure-dev/commit/d02a40d652700aa999856799fb1f8a0d88b300fe) - `2026-11-12T11:24:32Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[azure.ai.projects] Registry update for 1.1.0](https://github.com/Azure/azure-dev/pull/10917)
- [[azure.ai.toolboxes] Registry update for 1.1.0 (#10916)](https://github.com/Azure/azure-dev/commit/35701097e4cc6c68add86c847403cf9533738006) - `2026-11-12T10:46:35Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[azure.ai.toolboxes] Registry update for 1.1.0](https://github.com/Azure/azure-dev/pull/10916)
- [feat: prepare Foundry extension releases for 1.1.0 (#10914)](https://github.com/Azure/azure-dev/commit/43e086e5fad9aac2034ea7e38aeabcb7081706c6) - `2026-11-12T09:18:23Z` - Hui Miao (@huimiu) - PR: [Prepare Foundry extension releases for 1.1.0](https://github.com/Azure/azure-dev/pull/10914)

### Azure-Samples/ms-events-session-guide (13 commit(s), signal 53)

Tags: `human-authored, samples`

- [Add event-specific registration with a persistent event action (#10)](https://github.com/Azure-Samples/ms-events-session-guide/commit/6d169113add4a5ca632f916f93d4ab06f1815eaf) - `2026-11-12T20:54:06Z` - Artem Lovan (@artlovan) - PR: [Add official event registration and a persistent registration action](https://github.com/Azure-Samples/ms-events-session-guide/pull/10)
- [Report browser regression automatically on pull requests (#9)](https://github.com/Azure-Samples/ms-events-session-guide/commit/0cf377f7a965dee01affe2014d881f35aeb38927) - `2026-11-12T19:30:24Z` - Artem Lovan (@artlovan) - PR: [Report browser regression automatically on pull requests](https://github.com/Azure-Samples/ms-events-session-guide/pull/9)
- [Stabilize hosted browser regression and toast interactions (#8)](https://github.com/Azure-Samples/ms-events-session-guide/commit/9afa43648e7466ade1f708b35b377d10c55ef2a1) - `2026-11-12T19:17:47Z` - Artem Lovan (@artlovan) - PR: [Stabilize hosted browser regression and toast interactions](https://github.com/Azure-Samples/ms-events-session-guide/pull/8)
- [Run full browser regression only on demand (#7)](https://github.com/Azure-Samples/ms-events-session-guide/commit/c5a7b2514f2dfca7494c630a107d1e58ffc5f886) - `2026-11-12T18:24:41Z` - Artem Lovan (@artlovan) - PR: [Run full browser regression only on demand](https://github.com/Azure-Samples/ms-events-session-guide/pull/7)
- [Refresh DevEx branding and add layered regression coverage (#6)](https://github.com/Azure-Samples/ms-events-session-guide/commit/2c06e210b72cf1db9e52c2d373dfa5ec99bd9005) - `2026-11-12T18:16:16Z` - Artem Lovan (@artlovan) - PR: [Refresh DevEx branding and add layered regression coverage](https://github.com/Azure-Samples/ms-events-session-guide/pull/6)

### dotnet/android-api-docs (13 commit(s), signal 53)

Tags: `docs, human-authored`

- [Enable campaign auto-merge when PRs open (#1347)](https://github.com/dotnet/android-api-docs/commit/bd04d28b386b1e5a3e9cd0617c0a7b49f76254a5) - `2026-11-12T19:57:48Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Enable campaign auto-merge when PRs open](https://github.com/dotnet/android-api-docs/pull/1347)
- [Document Android.Hardware.Biometrics (#1329)](https://github.com/dotnet/android-api-docs/commit/f24f14f05e1f05bf243e419f19d8a2e7a82b9d68) - `2026-11-12T19:24:15Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Document Android.Hardware.Biometrics](https://github.com/dotnet/android-api-docs/pull/1329)
- [Document Android.App.Admin placeholders (#1328)](https://github.com/dotnet/android-api-docs/commit/60b997138567c10b14b3807aab55246428202a85) - `2026-11-12T18:59:54Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Document Android.App.Admin placeholders](https://github.com/dotnet/android-api-docs/pull/1328)
- [Complete Android.Media.TV XML documentation (#1341)](https://github.com/dotnet/android-api-docs/commit/52a5e55b5098300b281ae346ab83da7fb7535562) - `2026-11-12T17:58:07Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Complete Android.Media.TV XML documentation](https://github.com/dotnet/android-api-docs/pull/1341)
- [Complete Android.Telecom XML documentation (#1342)](https://github.com/dotnet/android-api-docs/commit/bbcc565a3f1d80094b01705a03f2603531aef12b) - `2026-11-12T17:57:24Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Complete Android.Telecom XML documentation](https://github.com/dotnet/android-api-docs/pull/1342)

### MicrosoftDocs/azure-docs-sdk-dotnet (12 commit(s), signal 87)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/e90490b76ee54277800ad8284009912065ced3fd) - `2026-11-12T17:04:12Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/e8ae77141bd7b996640284ec952ac413033cd5b8) - `2026-11-12T08:17:59Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/64ff8b7f616d71cc6cfbf7006ffb0572ba031dfa) - `2026-11-12T08:16:27Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/e6d902c2227c99f1df6390a915bb2465bf716cf9) - `2026-11-12T08:12:58Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/c05acd04b2f2d8008eae36f023104b450effdf7b) - `2026-11-12T08:11:10Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/power-platform (11 commit(s), signal 86)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/5e9f6b370edf9a1a56b84d54f1aba5d8b6bf3179) - `2026-11-12T19:04:24Z` - Learn Build Service GitHub App
- [Merge pull request #12180 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-platform/commit/be0c24ffa52e1b6ccc9535f44c0277b2b3ee5b23) - `2026-11-12T19:02:50Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update important-changes-coming.md (#12178)](https://github.com/MicrosoftDocs/power-platform/commit/9faa8c22ae58c2ffb915e1d36119118c59a492e7) - `2026-11-12T17:45:44Z` - Cyril Anderson (@cyrilanderson)
- [Update capacity-storage.md (#12177)](https://github.com/MicrosoftDocs/power-platform/commit/853479cafbe0357effc8d81373637ef87bdf3cd0) - `2026-11-12T15:50:45Z` - Ritu Joshi (@rijoshi1)
- [Update Copilot harness terminology - publish before Ignite (#12097)](https://github.com/MicrosoftDocs/power-platform/commit/f841ebc740c2e11cbce4c9dc42f0d2bbcb28fe7c) - `2026-11-12T15:27:45Z` - Nathalie Laroche (@nathlaroche)

### Azure/azure-sdk-for-js (11 commit(s), signal 136)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [@azure/ai-projects_2.11.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/ai-projects_2.11.0) - `2026-11-12T20:03:34Z`
- Release: [@azure/arm-containerinstance_10.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-containerinstance_10.0.0) - `2026-11-12T10:21:11Z`
- Release: [@azure/arm-recoveryservices_7.3.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-recoveryservices_7.3.0) - `2026-11-12T05:50:41Z`
- Release: [@azure/arm-recoveryservices-siterecovery_7.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-recoveryservices-siterecovery_7.0.0) - `2026-11-12T04:29:00Z`
- Release: [@azure/arm-chaos_2.1.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-chaos_2.1.0) - `2026-11-12T02:08:19Z`
- [[@azure-rest/ai-vision-image-analysis] Change v1.0.0 release date bac…](https://github.com/Azure/azure-sdk-for-js/commit/9b56c9054d5e21a950340c67013bb795b4447e3a) - `2026-11-12T18:23:59Z` - Jeremy Meng (@jeremymeng) - PR: [[@azure-rest/ai-vision-image-analysis] Change v1.0.0 release date back to Unreleased](https://github.com/Azure/azure-sdk-for-js/pull/40775)
- [[EngSys] Clean up invalid CODEOWNERS entries (#40746)](https://github.com/Azure/azure-sdk-for-js/commit/f7eddad00ac8b9db3a971d3d37bd7ae93b14b3ab) - `2026-11-12T17:24:34Z` - Jeremy Meng (@jeremymeng) - PR: [[EngSys] Clean up invalid CODEOWNERS entries](https://github.com/Azure/azure-sdk-for-js/pull/40746)
- [Add ARM SDK reviewers as lockfile code owners (#40771)](https://github.com/Azure/azure-sdk-for-js/commit/4cf92f445296afa6f408632180cc2756052a303b) - `2026-11-12T17:15:33Z` - Jialin Huang (@JialinHuang803) - PR: [Add ARM SDK reviewers as lockfile code owners](https://github.com/Azure/azure-sdk-for-js/pull/40771)
- [[AutoPR @azure-arm-containerinstance]-generated-from-SDK Generation -…](https://github.com/Azure/azure-sdk-for-js/commit/7681a2ba5cc076d09a54fe12b43791e4a48b155f) - `2026-11-12T09:20:23Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR @azure-arm-containerinstance]-generated-from-SDK Generation - JS-6547220](https://github.com/Azure/azure-sdk-for-js/pull/39239)
- [[AutoPR @azure-arm-recoveryservices]-generated-from-SDK Generation - …](https://github.com/Azure/azure-sdk-for-js/commit/c62dca5756ddc23a3050153f8ec809ecd2c82ccf) - `2026-11-12T05:17:27Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR @azure-arm-recoveryservices]-generated-from-SDK Generation - JS-7020640](https://github.com/Azure/azure-sdk-for-js/pull/40579)

### MicrosoftDocs/azure-docs-sdk-python (11 commit(s), signal 86)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/4588d8cdc18a13a6b5fac02b92a6a840369baae9) - `2026-11-12T17:55:01Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/0570b1fc4e88ccad0cf6c1c58224c70467c626ac) - `2026-11-12T12:42:40Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/ba7eb498ac10c1657b0be498e84729fcbb5f352e) - `2026-11-12T10:48:02Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/a185b110c578a484a285123ed0a6226a23802982) - `2026-11-12T09:46:42Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/2c639bc2bbccaa5ba381787048c75784b4351b21) - `2026-11-12T03:26:00Z` - azure-sdk (@azure-sdk)

### microsoft/vscode-docs (11 commit(s), signal 86)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Revise customization guide to use annotated codeblock (#10642)](https://github.com/microsoft/vscode-docs/commit/3dff05fe6cf540599cebe831ee404ff69622258f) - `2026-11-12T16:27:01Z` - Nick Trogh (@ntrogh) - PR: [Revise customization guide to use annotated code blocks](https://github.com/microsoft/vscode-docs/pull/10642)
- [Merge pull request #10641 from microsoft/docs/remove-local-create-sho…](https://github.com/microsoft/vscode-docs/commit/cea1e7141b88f0d87a3ae646eed20d63c0deb4e9) - `2026-11-12T15:31:32Z` - Nick Trogh (@ntrogh) - PR: [Remove /create-* commands](https://github.com/microsoft/vscode-docs/pull/10641)
- [Remove /create-* commands](https://github.com/microsoft/vscode-docs/commit/d1d8d8779de3c56ff49ee6b735d67bfd1a432b1d) - `2026-11-12T15:26:07Z` - Nick Trogh (@ntrogh) - PR: [Remove /create-* commands](https://github.com/microsoft/vscode-docs/pull/10641)
- [Merge pull request #10640 from microsoft/ntrogh/cleanup-customizations](https://github.com/microsoft/vscode-docs/commit/69df8ebeb3d9006327963861f6299325647560a7) - `2026-11-12T15:00:27Z` - Nick Trogh (@ntrogh) - PR: [Remove unused agents and skills from docs repo](https://github.com/microsoft/vscode-docs/pull/10640)
- [Remove unused agents and skills from docs repo](https://github.com/microsoft/vscode-docs/commit/c8f532514a4b0ae2c0c6edfa6878a003d92c4663) - `2026-11-12T14:58:58Z` - Nick Trogh (@ntrogh) - PR: [Remove unused agents and skills from docs repo](https://github.com/microsoft/vscode-docs/pull/10640)

### dotnet/roslyn (10 commit(s), signal 85)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [[main] Update dependencies from dotnet/roslyn (#86358)](https://github.com/dotnet/roslyn/commit/68ef2ac0ca4f1a04b5f79328fc84d4bb8b305e05) - `2026-11-12T19:48:57Z` - dotnet-maestro[bot] (@dotnet-maestro[bot]) - PR: [[main] Update dependencies from dotnet/roslyn](https://github.com/dotnet/roslyn/pull/86358)
- [Unsafe evolution: avoid resolving nullable type arguments (#86407)](https://github.com/dotnet/roslyn/commit/122e185e4e42d31cf1c1547652de387a612a5157) - `2026-11-12T15:04:23Z` - Jan Jones (@jjonescz) - PR: [Unsafe evolution: avoid resolving nullable type arguments](https://github.com/dotnet/roslyn/pull/86407)
- [Terminate multiline C# attribute values when formatting Razor (#86310)](https://github.com/dotnet/roslyn/commit/b907b90240f9f22873227aa510794dd280d61f57) - `2026-11-12T06:37:20Z` - David Wengier (@davidwengier) - PR: [Terminate multiline C# attribute values when formatting Razor](https://github.com/dotnet/roslyn/pull/86310)
- [Indent Razor by indent_size under dotnet format (#86307)](https://github.com/dotnet/roslyn/commit/7493dcf929d42728e618b832990060de1fc189bb) - `2026-11-12T05:12:42Z` - David Wengier (@davidwengier) - PR: [Indent Razor by indent_size under dotnet format](https://github.com/dotnet/roslyn/pull/86307)
- [[main] Source code updates from dotnet/dotnet (#86422)](https://github.com/dotnet/roslyn/commit/42f8f01ef39803baa63a49d90b8221e7ae01f57e) - `2026-11-12T03:41:35Z` - dotnet-maestro[bot] (@dotnet-maestro[bot]) - PR: [[main] Source code updates from dotnet/dotnet](https://github.com/dotnet/roslyn/pull/86422)

### microsoft/kiota-abstractions-go (10 commit(s), signal 85)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #324 from hardikkaurani/fix/add-query-parameters-d…](https://github.com/microsoft/kiota-abstractions-go/commit/43b8b508bf00fd97f6280952a357f8cca6c38b8c) - `2026-11-12T19:41:19Z` - Vincent Biret (@baywet) - PR: [fix(abstractions): support direct scalar fields in AddQueryParameters](https://github.com/microsoft/kiota-abstractions-go/pull/324)
- [test(abstractions): test pointer struct and custom numeric scalar que…](https://github.com/microsoft/kiota-abstractions-go/commit/9a8c10b52d45ada244a8e0f04032caf19feea8c0) - `2026-11-12T16:30:37Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(abstractions): support direct scalar fields in AddQueryParameters](https://github.com/microsoft/kiota-abstractions-go/pull/324)
- [test(abstractions): test direct and pointer temporal scalar query par…](https://github.com/microsoft/kiota-abstractions-go/commit/488c1d2723ee7244b9cdd7526edcbc4da8fb9254) - `2026-11-12T16:29:53Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(abstractions): support direct scalar fields in AddQueryParameters](https://github.com/microsoft/kiota-abstractions-go/pull/324)
- [test(abstractions): test zero-value direct scalar query parameters](https://github.com/microsoft/kiota-abstractions-go/commit/49b5bf15b75bdd43f905983d7e347c5eadfd6225) - `2026-11-12T16:29:33Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(abstractions): support direct scalar fields in AddQueryParameters](https://github.com/microsoft/kiota-abstractions-go/pull/324)
- [test(abstractions): test GetUri expansion with mixed direct scalar qu…](https://github.com/microsoft/kiota-abstractions-go/commit/ebc4f198e31ae2c6b4a4a2dc7e76467e8972d7f1) - `2026-11-12T16:29:07Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(abstractions): support direct scalar fields in AddQueryParameters](https://github.com/microsoft/kiota-abstractions-go/pull/324)

### microsoft/terraform-provider-power-platform (10 commit(s), signal 85)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Chore(deps): Bump github.com/Azure/azure-sdk-for-go/sdk/azcore (#1322)](https://github.com/microsoft/terraform-provider-power-platform/commit/9973a0d9db05c72cd161a084115cd727039a6bfe) - `2026-11-12T16:58:03Z` - dependabot[bot] (@dependabot[bot]) - PR: [Chore(deps): Bump github.com/Azure/azure-sdk-for-go/sdk/azcore from 1.23.3 to 1.24.0](https://github.com/microsoft/terraform-provider-power-platform/pull/1322)
- [fix: retry environment creation on transient GraphServerError (#1300)](https://github.com/microsoft/terraform-provider-power-platform/commit/6c93e81cd40e28ee43b2d0d7af9d59b0962d1d76) - `2026-11-12T13:55:49Z` - Mateusz Wasilewski (@mawasile) - PR: [fix: retry environment creation on transient GraphServerError](https://github.com/microsoft/terraform-provider-power-platform/pull/1300)
- [feat(data_record): add opt-in relationship_removal_behavior to disass…](https://github.com/microsoft/terraform-provider-power-platform/commit/8103fad6e45317e4b31cd62382f042aa57909ea0) - `2026-11-12T13:34:50Z` - Mateusz Wasilewski (@mawasile) - PR: [feat(data_record): add opt-in relationship_removal_behavior to disassociate removed relationship items](https://github.com/microsoft/terraform-provider-power-platform/pull/1306)
- [fix(solution): wait for a new Dataverse organization to assign the ca…](https://github.com/microsoft/terraform-provider-power-platform/commit/b88faae7747683cc64c6a8fb7e729dab960b9b4f) - `2026-11-12T13:27:11Z` - Mateusz Wasilewski (@mawasile) - PR: [fix(solution): wait for a new Dataverse organization to assign the caller its roles before staging](https://github.com/microsoft/terraform-provider-power-platform/pull/1317)
- [fix: harden nightly acceptance runs: environment create timeouts, lif…](https://github.com/microsoft/terraform-provider-power-platform/commit/7d004e5e22afb61da127aefb962919ab0ae91c69) - `2026-11-12T13:27:10Z` - Mateusz Wasilewski (@mawasile) - PR: [fix: harden nightly acceptance runs: environment create timeouts, lifecycle polling, Dataverse 401 on new environments, tenant isolation OperationNotFound](https://github.com/microsoft/terraform-provider-power-platform/pull/1308)

### dotnet/AspNetCore.Docs (10 commit(s), signal 50)

Tags: `docs, human-authored`

- [Archive error handling docs (#38135)](https://github.com/dotnet/AspNetCore.Docs/commit/61b7413aaac83515f4ca8c550792bd9c2250f616) - `2026-11-12T16:56:28Z` - Genevieve Warren (@gewarren) - PR: [Archive error handling docs](https://github.com/dotnet/AspNetCore.Docs/pull/38135)
- [Archive hosted services and http.sys docs (#38134)](https://github.com/dotnet/AspNetCore.Docs/commit/f06195091560b7a4fea90350d65a3f0b64bc0262) - `2026-11-12T16:56:00Z` - Genevieve Warren (@gewarren) - PR: [Archive hosted services and http.sys docs](https://github.com/dotnet/AspNetCore.Docs/pull/38134)
- [Archive older docs (#38133)](https://github.com/dotnet/AspNetCore.Docs/commit/69e81c2d93d6577fc0263c3b25907f29f2fd25ac) - `2026-11-12T16:55:26Z` - Genevieve Warren (@gewarren) - PR: [Archive factory-based middleware activation docs](https://github.com/dotnet/AspNetCore.Docs/pull/38133)
- [Bump Microsoft.Extensions.Logging.Debug across 7 directories (#38145)](https://github.com/dotnet/AspNetCore.Docs/commit/e4dccc27340c261c36ca3b21641c8913986bf5b5) - `2026-11-12T05:51:00Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Extensions.Logging.Debug across 7 directories](https://github.com/dotnet/AspNetCore.Docs/pull/38145)
- [Bump Microsoft.EntityFrameworkCore.SqlServer across 18 directories (#…](https://github.com/dotnet/AspNetCore.Docs/commit/e87fa65e9d0b662ec4eaf48868643484d3d42fd9) - `2026-11-12T05:44:27Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.EntityFrameworkCore.SqlServer across 18 directories](https://github.com/dotnet/AspNetCore.Docs/pull/38144)

### MicrosoftDocs/azure-compute-docs (10 commit(s), signal 85)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #4362 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-compute-docs/commit/ed7f906a89ea960f5cda838387ac5fac4bb3888c) - `2026-11-12T07:02:24Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update Pv2 regional list (#4360)](https://github.com/MicrosoftDocs/azure-compute-docs/commit/b3b460feedcce5ba1ee3e471c2b6d2340288fa6c) - `2026-11-12T00:33:05Z` - Raymond Lui (@raymond-azure-disks)
- [Merge pull request #4357 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-compute-docs/commit/006d1a97ca764184864271c3f10ec04f42147df1) - `2026-11-11T23:03:26Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Zonal VMSS Flex Aligned Fault Domains (#2918)](https://github.com/MicrosoftDocs/azure-compute-docs/commit/54bbcc47aa970ec5ebcd1773285bb8e6fd8c411a) - `2026-11-11T21:59:50Z` - Fitzgerald Steele (@fitzgeraldsteele)
- [Merge pull request #4356 from suzuber/vmss-standby-pool-monitor-intro](https://github.com/MicrosoftDocs/azure-compute-docs/commit/95930d2b3b2692b5c0d8ad9fcd1874e5d8f373df) - `2026-11-11T21:35:38Z` - prmerger-automator[bot] (@prmerger-automator[bot])

### MicrosoftDocs/azure-docs-sdk-java (9 commit(s), signal 84)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update CODEOWNERS to add new reviewers](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/d26f255e9fe16fcc8bff0b382dd1b9cd01025935) - `2026-11-12T19:55:15Z` - Laurent Mazuel (@lmazuel)
- [Add known issue for Java SDK (#2664)](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/c30824ecd22665949245bbf86ae15396ed0097ef) - `2026-11-12T19:53:59Z` - Isabelle (@ibrandes) - PR: [Add known issue for Java SDK](https://github.com/MicrosoftDocs/azure-docs-sdk-java/pull/2664)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/2268d15d2b13b3a500ed912f8a67776badc5e7e9) - `2026-11-12T09:31:05Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/37ef504f0eae7669bb4956bde7c9de45374edb7b) - `2026-11-12T08:58:20Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/77d4693ba0dbe94cee40f3858714fd47e4030043) - `2026-11-12T07:36:32Z` - azure-sdk (@azure-sdk)

### microsoft/amplifier-persona-workshop (9 commit(s), signal 89)

Tags: `human-authored, release, training`

- Release: [Persona Workshop 0.7.1 — native Windows startup repair](https://github.com/microsoft/amplifier-persona-workshop/releases/tag/v0.7.1) - `2026-11-12T18:04:50Z`
- Release: [Persona Workshop 0.7.0](https://github.com/microsoft/amplifier-persona-workshop/releases/tag/v0.7.0) - `2026-11-12T15:09:38Z`
- [Preserve native update journals while status is read (#13)](https://github.com/microsoft/amplifier-persona-workshop/commit/74355ccdbf77aedcbf67b6efdd6d0cc7ff744d52) - `2026-11-12T19:45:47Z` - Brian Krabach (@bkrabach) - PR: [Preserve native update journals while status is read (0.7.2)](https://github.com/microsoft/amplifier-persona-workshop/pull/13)
- [Fix native Windows sign-in startup (0.7.1) (#12)](https://github.com/microsoft/amplifier-persona-workshop/commit/a176426b309425eda8bfb8922ed647d97ef296f7) - `2026-11-12T18:02:05Z` - Brian Krabach (@bkrabach) - PR: [Fix native Windows sign-in startup (0.7.1)](https://github.com/microsoft/amplifier-persona-workshop/pull/12)
- [Clarify bundled document prerequisites (#11)](https://github.com/microsoft/amplifier-persona-workshop/commit/3a51acc07d3b0ddeb7a32e98974de1a30d66db03) - `2026-11-12T15:36:36Z` - Brian Krabach (@bkrabach) - PR: [Clarify bundled document prerequisites](https://github.com/microsoft/amplifier-persona-workshop/pull/11)
- [Preserve native update recovery and qualify desktop startup (#10)](https://github.com/microsoft/amplifier-persona-workshop/commit/e409546baa9d96caab1ff8def1e1db0c50d32475) - `2026-11-12T15:05:26Z` - Brian Krabach (@bkrabach) - PR: [Preserve native update recovery and qualify desktop startup](https://github.com/microsoft/amplifier-persona-workshop/pull/10)
- [Add explicit native app updates and state-preserving recovery (#9)](https://github.com/microsoft/amplifier-persona-workshop/commit/35eb28e545abe579a052ef6e2b940cf118468100) - `2026-11-12T13:51:21Z` - Brian Krabach (@bkrabach) - PR: [Add explicit native app updates and state-preserving recovery](https://github.com/microsoft/amplifier-persona-workshop/pull/9)

### MicrosoftDocs/dynamics365smb-docs (9 commit(s), signal 109)

Tags: `docs, human-authored, security, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/63b153c765c680bc521ba67af7c56ed3f0c61306) - `2026-11-12T19:03:39Z` - Learn Build Service GitHub App
- [Merge pull request #5280 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/aeb78fd01d1d37ecdd53982d0449e7ace289573f) - `2026-11-12T19:02:47Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Refresh security and privacy (#5278)](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/2533bf80fa5ced6ba979842f11447aee85712faf) - `2026-11-12T14:29:22Z` - jswymer (@jswymer)
- [Audit article contributors (#5276)](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/f947427c621801ec7e372539841fdc0ae9275bcd) - `2026-11-12T13:12:04Z` - Brent Holtorf (@brentholtorf)
- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/3f4fd87fc695f82c39fbf2b5bd86f6c69b5e2192) - `2026-11-12T13:04:04Z` - Learn Build Service GitHub App

### MicrosoftDocs/entra-docs (9 commit(s), signal 84)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merge pull request #14899 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/entra-docs/commit/744d48fb9049295f00281b03752013782f75825e) - `2026-11-12T18:33:22Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [docs: add Resource Policy built-in roles (#14780)](https://github.com/MicrosoftDocs/entra-docs/commit/4d1cfd8890e24b3b822d77c485175604b3ae6ad9) - `2026-11-12T17:37:25Z` - Dan Kershaw [MSFT] (@dkershaw10)
- [Merge pull request #14869 from diegojerezba/diegojerezba-add-custom-u…](https://github.com/MicrosoftDocs/entra-docs/commit/b73acae0ab262a0a3385f09339adc48f9df27804) - `2026-11-12T17:35:06Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #14888 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/entra-docs/commit/4b7154093b7c80593fafe5131c9d4d3ad61c9f9f) - `2026-11-11T23:36:34Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #14883 from markwahl-msft/mwahl-gov-agents-link](https://github.com/MicrosoftDocs/entra-docs/commit/358e99c5f05abcb1c0d88bfd0cffac458d65e7c2) - `2026-11-11T19:59:48Z` - prmerger-automator[bot] (@prmerger-automator[bot])

### microsoft/voice-agent (9 commit(s), signal 94)

Tags: `docs, human-authored, product:Azure AI, release-language, watchlist`

- [Change Voice Agent status to Generally Available (#131)](https://github.com/microsoft/voice-agent/commit/c6b17cd5ecc489e50f4e70ef6e82f1df4579ce00) - `2026-11-12T14:25:37Z` - szhaomsft (@szhaomsft) - PR: [Change Voice Agent status to Generally Available](https://github.com/microsoft/voice-agent/pull/131)
- [docs: document full Foundry, quota, and Application Insights RBAC set…](https://github.com/microsoft/voice-agent/commit/f6046b0a52b3bec111e685958ea671b5f5427acb) - `2026-11-12T10:36:14Z` - mengyou03042 (@mengyou03042) - PR: [docs: document full Foundry, quota, and Application Insights RBAC setup](https://github.com/microsoft/voice-agent/pull/122)
- [Bump fast-xml-parser from 5.11.2 to 5.12.0 in /samples/gpt_live/js (#…](https://github.com/microsoft/voice-agent/commit/52253743b70d1b330dae40fa002ee5dac325c502) - `2026-11-12T10:34:19Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump fast-xml-parser from 5.11.2 to 5.12.0 in /samples/gpt_live/js](https://github.com/microsoft/voice-agent/pull/127)
- [Add Genesys Audio Connector voice agent sample (#129)](https://github.com/microsoft/voice-agent/commit/00db92135337a2ebc0b5aecfc0b6379f0add0e1e) - `2026-11-12T10:33:29Z` - liangxu (@21eutidyt9d67r1) - PR: [Add Genesys Audio Connector voice agent sample](https://github.com/microsoft/voice-agent/pull/129)
- [Auto-detect transcription languages by default (#130)](https://github.com/microsoft/voice-agent/commit/3011a979d4eaa6d3ec1baa6b8df8c9da6c1ed3a6) - `2026-11-12T10:33:04Z` - szhaomsft (@szhaomsft) - PR: [Default transcription to automatic language detection](https://github.com/microsoft/voice-agent/pull/130)

### Azure-Samples/azure-finops-agent (9 commit(s), signal 94)

Tags: `human-authored, product:Azure AI, release-language, samples, watchlist`

- [docs: changelog for the dependency updates](https://github.com/Azure-Samples/azure-finops-agent/commit/31e6fcea428019afc6108f05ea48d824b85f0faa) - `2026-11-12T11:19:58Z` - Ali Reza Farahnak (@alfarahn)
- [Bump @playwright/test from 1.64.1 to 1.65.0 in /src/frontend (#151)](https://github.com/Azure-Samples/azure-finops-agent/commit/1e609ed73d57d68d4ed414a67afcd70128a6f97c) - `2026-11-12T11:18:31Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump @playwright/test from 1.64.1 to 1.65.0 in /src/frontend](https://github.com/Azure-Samples/azure-finops-agent/pull/151)
- [Bump vite in /src/frontend in the vue group across 1 directory (#155)](https://github.com/Azure-Samples/azure-finops-agent/commit/2b77e8e31ea8a2eb40650e9889237481a7239c08) - `2026-11-12T11:16:42Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump vite from 8.3.6 to 8.3.7 in /src/frontend in the vue group across 1 directory](https://github.com/Azure-Samples/azure-finops-agent/pull/155)
- [Bump the otel group with 2 updates (#153)](https://github.com/Azure-Samples/azure-finops-agent/commit/c152bedc454c8cc2ef90fbaa2c46baa96b62c081) - `2026-11-12T11:16:38Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the otel group with 2 updates](https://github.com/Azure-Samples/azure-finops-agent/pull/153)
- [Upgrade Agent Framework to 1.27 preview and clean up](https://github.com/Azure-Samples/azure-finops-agent/commit/2a8c5829d53927f73aa71cb0dd64d65d4064864a) - `2026-11-12T10:55:57Z` - Ali Reza Farahnak (@alfarahn)

### microsoft/kiota-samples (9 commit(s), signal 84)

Tags: `docs, human-authored, product:Microsoft Graph, watchlist`

- [Merge pull request #9365 from microsoft/upgrade/dotnet-net11](https://github.com/microsoft/kiota-samples/commit/bebe9a10b7ac98704bc671c645405c956e132cc9) - `2026-11-11T20:11:35Z` - Vincent Biret (@baywet) - PR: [chore(dotnet): upgrade remaining .NET samples to net11](https://github.com/microsoft/kiota-samples/pull/9365)
- [feat(dotnet-dependency-injection): restore Swagger UI using only the …](https://github.com/microsoft/kiota-samples/commit/aaf68cf3ac9129d0f10c5a433723f6887831f705) - `2026-11-11T20:07:38Z` - Vincent Biret (@baywet) - PR: [chore(dotnet): upgrade remaining .NET samples to net11](https://github.com/microsoft/kiota-samples/pull/9365)
- [style(dotnet-dependency-injection): format and simplify GitHubClientF…](https://github.com/microsoft/kiota-samples/commit/83e5fd738ea767fdbac2cbb3ebdd7c39a9271b62) - `2026-11-11T20:03:35Z` - Vincent Biret (@baywet) - PR: [chore(dotnet): upgrade remaining .NET samples to net11](https://github.com/microsoft/kiota-samples/pull/9365)
- [refactor(dotnet-dependency-injection): replace Swashbuckle with nativ…](https://github.com/microsoft/kiota-samples/commit/f13abeae38582d643ab91ab80de55553a0e5c8bb) - `2026-11-11T20:01:38Z` - Vincent Biret (@baywet) - PR: [chore(dotnet): upgrade remaining .NET samples to net11](https://github.com/microsoft/kiota-samples/pull/9365)
- [chore(dotnet): upgrade remaining .NET samples to net11](https://github.com/microsoft/kiota-samples/commit/55f019e5be05a6f0605ff98395e2f382d4c08c26) - `2026-11-11T19:57:27Z` - Vincent Biret (@baywet) - PR: [chore(dotnet): upgrade remaining .NET samples to net11](https://github.com/microsoft/kiota-samples/pull/9365)

### MicrosoftDocs/azure-docs-sdk-node (8 commit(s), signal 83)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/f0763df15fc4205145d881c18b1a1091687aed7b) - `2026-11-12T20:15:28Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/18fc994b7f146596401e5c911a7e25ae4d33eb11) - `2026-11-12T10:29:42Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/cefe059221edfd1819b840c1c183a135ceca91c6) - `2026-11-12T06:03:55Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/db498879d5c12f4dd5dad61e251611d68b5aa342) - `2026-11-12T04:38:39Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/3e67845cae6dc6be343ddb3e745105f7f41b3ab4) - `2026-11-12T02:25:03Z` - azure-sdk (@azure-sdk)

### microsoft/WindowsCloudAcademy (8 commit(s), signal 83)

Tags: `human-authored, product:Azure AI, training, watchlist`

- [Fix formatting and update README content](https://github.com/microsoft/WindowsCloudAcademy/commit/970273fbb6e40de3dc9e6ce7e9e5a1fdf199f7b7) - `2026-11-12T12:46:12Z` - Daniel Weppeler (@dweppeler-msft)
- [Revise challenge instructions for Windows 365 agents](https://github.com/microsoft/WindowsCloudAcademy/commit/331adcd51787cecca454243d0080f12407288928) - `2026-11-12T12:43:30Z` - Daniel Weppeler (@dweppeler-msft)
- [Revise Windows 365 Flex shared mode documentation](https://github.com/microsoft/WindowsCloudAcademy/commit/95247e3ba38a7d54252a3940a25b325108193edb) - `2026-11-12T12:40:36Z` - Daniel Weppeler (@dweppeler-msft)
- [Revise RDP properties documentation for clarity](https://github.com/microsoft/WindowsCloudAcademy/commit/ff39b3b79f8247cae7964dcbf9aa1b028b709324) - `2026-11-12T12:29:48Z` - Daniel Weppeler (@dweppeler-msft)
- [Revise Windows 365 provisioning instructions and links](https://github.com/microsoft/WindowsCloudAcademy/commit/43dce65567709e1b076b2188ec100a64278df26e) - `2026-11-12T12:20:14Z` - Daniel Weppeler (@dweppeler-msft)

### Azure/ResiliencyInAzure (8 commit(s), signal 93)

Tags: `docs, human-authored, release-language, watchlist`

- [Fix grammatical error in prerequisites list](https://github.com/Azure/ResiliencyInAzure/commit/6222da16deac37c741f176ec4e39ebd77cdc8119) - `2026-11-12T09:04:03Z` - kalyaninamuduri (@kalyaninamuduri)
- [Update RBAC requirements for Azure Infrastructure Resiliency](https://github.com/Azure/ResiliencyInAzure/commit/9ae97e285e650a8524cc06cc6724cf264f812359) - `2026-11-12T09:01:38Z` - kalyaninamuduri (@kalyaninamuduri)
- [Fix formatting in Prerequisites.md header](https://github.com/Azure/ResiliencyInAzure/commit/3acaf10b633ef32b2f938f012572f7287ee49c62) - `2026-11-12T05:03:58Z` - kalyaninamuduri (@kalyaninamuduri)
- [Update prerequisites for Azure Resiliency preview](https://github.com/Azure/ResiliencyInAzure/commit/3429ccaa642d83cb7b0fa515a8e8baefee8ac99e) - `2026-11-12T05:03:15Z` - kalyaninamuduri (@kalyaninamuduri)
- [Refactor ViewResiliencePosture.md for clarity](https://github.com/Azure/ResiliencyInAzure/commit/6bbe78f602169195b8924da6492b7606ffe036c8) - `2026-11-12T04:59:53Z` - kalyaninamuduri (@kalyaninamuduri)

### microsoft/WhatTheHack (8 commit(s), signal 83)

Tags: `human-authored, product:Azure AI, product:Azure SDK, samples, watchlist`

- [[Hack Update] 076 GHCP Cost Optimization updates (#1298)](https://github.com/microsoft/WhatTheHack/commit/2a29ab427f8c4abe455a1abc2544c0a63f71cea6) - `2026-11-12T03:25:38Z` - Peter C. Laudati (@jrzyshr) - PR: [[Hack Update] 076 GHCP Cost Optimization updates](https://github.com/microsoft/WhatTheHack/pull/1298)
- [[WTH Core] Update wth publishing skill (#1297)](https://github.com/microsoft/WhatTheHack/commit/8a9128f0ea36ea757987e3991e88f724dd7937bf) - `2026-11-12T03:04:53Z` - Peter C. Laudati (@jrzyshr) - PR: [[WTH Core] Update wth publishing skill](https://github.com/microsoft/WhatTheHack/pull/1297)
- [Bump lodash from 4.17.23 to 4.18.1 in /068-AzureOpenAIApps/Student/Re…](https://github.com/microsoft/WhatTheHack/commit/bba282c669523de4856d7cfcff9b8e5472184b55) - `2026-11-12T02:04:31Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump lodash from 4.17.23 to 4.18.1 in /068-AzureOpenAIApps/Student/Resources/ContosoAIAppsFrontend](https://github.com/microsoft/WhatTheHack/pull/1296)
- [Bump fast-xml-parser and @aws-sdk/xml-builder in /075-MongoDB2Documen…](https://github.com/microsoft/WhatTheHack/commit/2cc7ce81d5f1c8b7e2477a97cd370b0514e46713) - `2026-11-12T02:00:36Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump fast-xml-parser and @aws-sdk/xml-builder in /075-MongoDB2DocumentDB/Student/Resources/MFlix](https://github.com/microsoft/WhatTheHack/pull/1293)
- [Bump mongoose from 8.24.1 to 8.24.7 in /063-IntroToAzureRedHatOpenshi…](https://github.com/microsoft/WhatTheHack/commit/e8344096ce8ab326e91b6de1ab728f3f68ab19c0) - `2026-11-12T01:59:55Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump mongoose from 8.24.1 to 8.24.7 in /063-IntroToAzureRedHatOpenshift/Student/Resources/Challenge-02/rating-api](https://github.com/microsoft/WhatTheHack/pull/1292)

### MicrosoftDocs/dynamics-365-unified-operations-public (7 commit(s), signal 82)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/Dynamics…](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/57cf88a6250f5aef216a0c786b441a31d072f304) - `2026-11-12T19:05:28Z` - Learn Build Service GitHub App
- [Merge pull request #22852 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/96eb573707f53d111431a8db04638d6c461fa757) - `2026-11-12T19:03:00Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Consolidate procurement troubleshooting guidance (#22834)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/4f9ee6c6cbc54f007a907b07df0fc8d3d9959d87) - `2026-11-12T15:54:23Z` - Karl Maybach (@kamaybac)
- [Add value chain configuration documentation (#22713)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/25b38030353b1d09e58e5ad2230d5a3bdca2d34b) - `2026-11-12T15:07:18Z` - Jinnie Wong (@jinniew)
- [Demand Planning v 1.5 (#22840)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/b58cd8e42330d8acbcf2d8fb501e25de525d0c01) - `2026-11-12T13:10:41Z` - Karl Maybach (@kamaybac)

### MicrosoftLearning/mslearn-sec-identity (7 commit(s), signal 82)

Tags: `human-authored, product:PowerShell, training, watchlist`

- [Merge pull request #28 from v-absamim/update/lab-1d-cloudshell-wording](https://github.com/MicrosoftLearning/mslearn-sec-identity/commit/8293fc00e1eebd243d8c846bcc6a2a7b485a6a40) - `2026-11-12T18:40:02Z` - v-absamim (@v-absamim) - PR: [Update Lab 1D: standardize Cloud Shell and portal wording](https://github.com/MicrosoftLearning/mslearn-sec-identity/pull/28)
- [Merge pull request #26 from v-absamim/update/lab-1a-pim-steps](https://github.com/MicrosoftLearning/mslearn-sec-identity/commit/f3ea29c98e1c7ffb62cdf306d9ed2517b16a6649) - `2026-11-12T18:34:25Z` - v-absamim (@v-absamim) - PR: [Update Lab 1A: reorder PIM activation/assignment steps and refine wording](https://github.com/MicrosoftLearning/mslearn-sec-identity/pull/26)
- [Revise PIM role assignment and activation instructions](https://github.com/MicrosoftLearning/mslearn-sec-identity/commit/0ced2972c30fe4533d7c8377d30f40badb30e178) - `2026-11-12T18:15:22Z` - v-absamim (@v-absamim) - PR: [Update Lab 1A: reorder PIM activation/assignment steps and refine wording](https://github.com/MicrosoftLearning/mslearn-sec-identity/pull/26)
- [Update PIM role assignment instructions](https://github.com/MicrosoftLearning/mslearn-sec-identity/commit/0618239a1a3a1ae8430f44a46d45da70bc415354) - `2026-11-12T17:33:46Z` - v-absamim (@v-absamim) - PR: [Update Lab 1A: reorder PIM activation/assignment steps and refine wording](https://github.com/MicrosoftLearning/mslearn-sec-identity/pull/26)
- [Revise steps for Conditional Access Administrator setup](https://github.com/MicrosoftLearning/mslearn-sec-identity/commit/23770746c30f0428fd54207e0b4522fb60298d0b) - `2026-11-12T17:31:01Z` - v-absamim (@v-absamim) - PR: [Update Lab 1A: reorder PIM activation/assignment steps and refine wording](https://github.com/MicrosoftLearning/mslearn-sec-identity/pull/26)

### microsoft/winget-cli (7 commit(s), signal 82)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Broaden elevated process limitations (#6634)](https://github.com/microsoft/winget-cli/commit/57d424f360608411e871c44c7d0ba21d848bcab6) - `2026-11-12T18:28:36Z` - JohnMcPMS (@JohnMcPMS) - PR: [Broaden elevated process limitations](https://github.com/microsoft/winget-cli/pull/6634)
- [Verify ZIP symlink data only after its bounds check in PureLib (#6675)](https://github.com/microsoft/winget-cli/commit/11e5d8b7c953485a9e947ddcb7201a36a425ba48) - `2026-11-12T04:59:46Z` - AmirMS (@AmelBawa-msft) - PR: [Verify ZIP symlink data only after its bounds check in PureLib](https://github.com/microsoft/winget-cli/pull/6675)
- [Bump github/gh-aw-actions/setup from 1.0.1 to 1.2.0 in the github-act…](https://github.com/microsoft/winget-cli/commit/3ad37651c5136e72f3f9245bad4cbc41efdb9d14) - `2026-11-12T01:08:13Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump github/gh-aw-actions/setup from 1.0.1 to 1.2.0 in the github-actions group](https://github.com/microsoft/winget-cli/pull/6674)
- [Report upgrades skipped as not applicable (#6637)](https://github.com/microsoft/winget-cli/commit/7d60ce618e3e78f72ba688c2589c48355955b0f3) - `2026-11-12T01:07:20Z` - Slai.life (@huong8373tt-beep) - PR: [Report upgrades skipped as not applicable](https://github.com/microsoft/winget-cli/pull/6637)
- [Source agreement state (#6612)](https://github.com/microsoft/winget-cli/commit/362a8cc950db5c5b32523616171e80436bc45993) - `2026-11-12T00:38:18Z` - JohnMcPMS (@JohnMcPMS) - PR: [Source agreement state](https://github.com/microsoft/winget-cli/pull/6612)

### MicrosoftDocs/SupportArticles-docs (7 commit(s), signal 82)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/478017e30e623d86a72eb1bb1bf67044d12b89ae) - `2026-11-12T18:07:14Z` - Learn Build Service GitHub App
- [Merge pull request #12836 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/0e2a96fbd9d7e5e6c7a3dbeb84ee5e2a4098851e) - `2026-11-12T18:05:22Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add Tracking tile to Customer Insights Journeys troubleshooting (#12835)](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/c4d885cf5d1422e07bc8449be57cfb2d43bd68bc) - `2026-11-12T17:52:56Z` - petrjantac (@petrjantac)
- [AB#13392 - Consolidate procurement troubleshooting guidance (#12800)](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/a8558d9c37edfe5ebce3e9999c700d632decf159) - `2026-11-12T15:54:54Z` - Sloan Haywood (@haywoodsloan)
- [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/ec9f74ee1187591c2b457124b1e6cd9ad65e7f4c) - `2026-11-11T22:08:46Z` - Learn Build Service GitHub App

### MicrosoftDocs/azure-management-docs (7 commit(s), signal 92)

Tags: `docs, human-authored, product:Azure AI, release-language, watchlist`

- [Merge pull request #3064 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-management-docs/commit/7e790c558a5c2599b18cb3c0ee47a1d1ca1193aa) - `2026-11-12T15:56:28Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [release-agentic-rag -> main - TBD (#3059)](https://github.com/MicrosoftDocs/azure-management-docs/commit/84a34d3c3cb3ec75eaa43cdfd15fbdd2da173dcf) - `2026-11-12T15:50:14Z` - Bowen Yang (@Albertyang0)
- [Merge pull request #3062 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-management-docs/commit/f16d8d35e43ebbd5137338c84ba3dbff366126e6) - `2026-11-11T23:08:10Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update add-public-cloud.md (#3050)](https://github.com/MicrosoftDocs/azure-management-docs/commit/b159ec774502cde975d63e80704a4f1d908c4587) - `2026-11-11T20:34:19Z` - Jalen McGee (@JalenMcG)
- [Merge pull request #3056 from yhussein896/verify-software-assurance](https://github.com/MicrosoftDocs/azure-management-docs/commit/a58e8bf61ea3010668f0be532f030212708636fb) - `2026-11-11T20:21:39Z` - prmerger-automator[bot] (@prmerger-automator[bot])

### OfficeDev/microsoft-teams-library-js (7 commit(s), signal 92)

Tags: `docs, human-authored, release-language, watchlist`

- [Run the weekly SDF beta on a schedule, skipping Prod weeks and no-cha…](https://github.com/OfficeDev/microsoft-teams-library-js/commit/32a3f3bb393154914c954505d143c2c88af3a149) - `2026-11-12T05:23:30Z` - Patrick Latter (@palatter) - PR: [Run the weekly SDF beta on a schedule, skipping Prod weeks and no-change weeks](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3208)
- [Add check preflight and check announcement-draft to the release skill…](https://github.com/OfficeDev/microsoft-teams-library-js/commit/f7e5fa4708509bd9b4966cfa9881df5a4fd2c49b) - `2026-11-12T04:21:11Z` - Patrick Latter (@palatter) - PR: [Add check preflight and check announcement-draft to the release skill](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3212)
- [Add a Prod validation stage before the Lockbox approval (#3207)](https://github.com/OfficeDev/microsoft-teams-library-js/commit/44c7b72889bedd3cc3e2d117f0aaf5880bb1ac2a) - `2026-11-12T03:21:07Z` - Patrick Latter (@palatter) - PR: [Add a Prod validation stage before the Lockbox approval](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3207)
- [Add a verify-only workflow for published releases (#3206)](https://github.com/OfficeDev/microsoft-teams-library-js/commit/99cdab1fbd5995a800d100e025729875289d0b99) - `2026-11-12T02:11:14Z` - Patrick Latter (@palatter) - PR: [Add a verify-only workflow for published releases](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3206)
- [Remove the force-pushing prerelease workflow (#3202)](https://github.com/OfficeDev/microsoft-teams-library-js/commit/9c3e25292922a32de665b8040132e6258b249e6c) - `2026-11-12T01:08:38Z` - Patrick Latter (@palatter) - PR: [Remove the force-pushing prerelease workflow](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3202)

### MicrosoftDocs/visualstudio-docs (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merge pull request #11492 from MicrosoftDocs/main639300964368491245sy…](https://github.com/MicrosoftDocs/visualstudio-docs/commit/e696d1dcf088713b0e667554b63894b9f7eb908d) - `2026-11-12T16:07:35Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11492)
- [Merging changes synced from https://github.com/MicrosoftDocs/visualst…](https://github.com/MicrosoftDocs/visualstudio-docs/commit/92cdc091fdc1e6c5cdd0754c8c9e89d7c567df0d) - `2026-11-12T16:07:13Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11492)
- [Merge pull request #15818 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/visualstudio-docs/commit/388d0307ad858ffca36a11351d5db0ca2e4d4f61) - `2026-11-12T16:04:40Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11492)
- [Merge pull request #15810 from MicrosoftDocs/copilot/update-documenta…](https://github.com/MicrosoftDocs/visualstudio-docs/commit/f5a84aff4ff99c127dcf86c8bd40efbd8576b730) - `2026-11-11T23:07:30Z` - prmerger-automator[bot] (@prmerger-automator[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11492)
- [docs: resolve layout article validation warnings](https://github.com/MicrosoftDocs/visualstudio-docs/commit/cf9cc921e63a73e31170bdc301992f28edf120a5) - `2026-11-11T23:00:06Z` - copilot-swe-agent[bot] (@Copilot) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11492)

### MicrosoftDocs/dynamics-365-contact-center (6 commit(s), signal 81)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/0b5213e153c05bf835cc115dfe5829871288b611) - `2026-11-12T13:03:43Z` - Learn Build Service GitHub App
- [Merge pull request #818 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/f554e89f7ad5b8ddb4333133f083f99a945c0ada) - `2026-11-12T13:03:20Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add AI disclosure section for voice experiences (#815)](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/5d9657e9825dce047af4cb7d6f158fe67c428a3e) - `2026-11-12T08:53:44Z` - Neeraja Nellimarla (@neeranelli)
- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/bc3b06bc4da900bbb53032b22e097cb8e52f8854) - `2026-11-12T07:03:11Z` - Learn Build Service GitHub App
- [Merge pull request #817 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/0411c4ad6125c37adc44884cf1225abca5c3d407) - `2026-11-12T07:02:47Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### MicrosoftDocs/azure-dev-docs (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-de…](https://github.com/MicrosoftDocs/azure-dev-docs/commit/98f35b90ec6f2d8b01289e7909c6529fb69cca10) - `2026-11-12T00:06:25Z` - Learn Build Service GitHub App
- [Merge pull request #9987 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-dev-docs/commit/558ddd42c2c6f0902efb69eafd75678a67c2ea7d) - `2026-11-12T00:04:50Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #9984 from MicrosoftDocs/diberry-patch-2](https://github.com/MicrosoftDocs/azure-dev-docs/commit/36fd9f1eac927b1c1f6868029a0446b16e514e90) - `2026-11-11T22:35:46Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #9983 from MicrosoftDocs/diberry-patch-1](https://github.com/MicrosoftDocs/azure-dev-docs/commit/ce8eb1af7bc1a3bac0e53302fde65f3ed12ddd92) - `2026-11-11T22:35:14Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Add author information to Azure SDK library index](https://github.com/MicrosoftDocs/azure-dev-docs/commit/f36779b232d7b6a5b264ad1560143791cb19ab15) - `2026-11-11T22:29:18Z` - Dina Berry (MSFT) (@diberry)

### MicrosoftDocs/azure-aks-docs (6 commit(s), signal 81)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-ak…](https://github.com/MicrosoftDocs/azure-aks-docs/commit/cc9553c0e2d71ab45021ff07cafb0508ebd29d34) - `2026-11-11T23:06:15Z` - Learn Build Service GitHub App
- [Merge pull request #4187 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-aks-docs/commit/56b6d19091b03b6c988948225dc4ff99153418aa) - `2026-11-11T23:05:40Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [docs: update Azure Managed Lustre CSI guidance for 0.7.0 (#4180)](https://github.com/MicrosoftDocs/azure-aks-docs/commit/c823a9e4cceea610226fa1ff985ecb5304aca274) - `2026-11-11T21:21:27Z` - Jeff Bearer (@jeffbearer)
- [MIG single and mixed strategy feature updates (#4014)](https://github.com/MicrosoftDocs/azure-aks-docs/commit/a9f2766f2b84118a02fb7607e7e8336da2bbc782) - `2026-11-11T19:07:54Z` - Sachi Desai (@sdesai345)
- [Add Capacity reservation group details for NAP (#4173)](https://github.com/MicrosoftDocs/azure-aks-docs/commit/a3a1360d2d1394522ec4881c87268b1d68058bee) - `2026-11-11T19:01:07Z` - Wilson (@wdarko1)

### MicrosoftDocs/CommunityToolkit (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [MediaElement: display video inside a Border on Android 10 and 11 (#671)](https://github.com/MicrosoftDocs/CommunityToolkit/commit/51f4ecaf98db1eced16cd29500ed53f1e6184b16) - `2026-11-12T17:48:11Z` - Marcelo Moresco (@marcelomoresco) - PR: [MediaElement: display video inside a Border on Android 10 and 11](https://github.com/MicrosoftDocs/CommunityToolkit/pull/671)
- [CommunityToolkit.Maui Docs Updates for .NET 11 (#670)](https://github.com/MicrosoftDocs/CommunityToolkit/commit/6c3f0fb2121a4e68ed0e6b0674e7ce8bce6cdc81) - `2026-11-11T20:24:32Z` - Brandon Minnick (@TheCodeTraveler) - PR: [CommunityToolkit.Maui Docs Updates for .NET 11](https://github.com/MicrosoftDocs/CommunityToolkit/pull/670)
- [CommunityToolkit.Maui Docs Updates for Device Tests Fixes + Findings …](https://github.com/MicrosoftDocs/CommunityToolkit/commit/04829a318904e944a1d285a565852144b208d78d) - `2026-11-11T20:18:18Z` - Brandon Minnick (@TheCodeTraveler) - PR: [CommunityToolkit.Maui Docs Updates for Device Tests Fixes + Findings](https://github.com/MicrosoftDocs/CommunityToolkit/pull/665)
- [Add Popup support for AppTheme (#664)](https://github.com/MicrosoftDocs/CommunityToolkit/commit/8f703b755d86918d02e1f506d4f48df050aad420) - `2026-11-11T18:28:21Z` - Brandon Minnick (@TheCodeTraveler) - PR: [Add Popup support for AppTheme](https://github.com/MicrosoftDocs/CommunityToolkit/pull/664)
- [Document StartVideoRecording start-acknowledgment return semantics (#…](https://github.com/MicrosoftDocs/CommunityToolkit/commit/3b13b95bb21078c000d7c540b27f95d721464965) - `2026-11-11T18:24:57Z` - Brandon Minnick (@TheCodeTraveler) - PR: [Document StartVideoRecording start-acknowledgment return semantics](https://github.com/MicrosoftDocs/CommunityToolkit/pull/669)

### microsoftgraph/microsoft-graph-docs-contrib (5 commit(s), signal 105)

Tags: `docs, human-authored, product:Microsoft Graph, security, watchlist`

- [docs: document Microsoft Threat Intelligence API rate limit (#10091)](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/dcfc99885e5d87feb36ad14daa59169efa181e53) - `2026-11-12T15:12:38Z` - Yoni Nave (@YoniN-Mic) - PR: [Document Microsoft Threat Intelligence API rate limit](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10091)
- [Merge pull request #10093 from microsoftgraph/main639300414121928919s…](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/cfc84ff73fb93db5ab5b34dc0aeff26db3bdee09) - `2026-11-12T00:50:30Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10093)
- [Merging changes synced from https://github.com/microsoftgraph/microso…](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/dc6ec050867692e94d711477c6daefbd4bc0b8fc) - `2026-11-12T00:50:06Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10093)
- [Merge pull request #29907 from microsoftgraph/main](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/4f0d5017be67b8c0c11e170d5e844f8cef9d938c) - `2026-11-12T00:42:22Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10093)
- [docs: Add public beta security content management repositories API (#…](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/c09604569f3140ef2f79a7a8e05a242fd065c112) - `2026-11-11T19:06:54Z` - Alex Brohshtut (@AlexBrohshtut) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10093)

### microsoft/SPARROW (5 commit(s), signal 105)

Tags: `human-authored, security, training, watchlist`

- [Merge pull request #85 from microsoft/dependabot/github_actions/githu…](https://github.com/microsoft/SPARROW/commit/6bc0523a7ce1ba932ac0f2cb495795223db4c74f) - `2026-11-12T13:45:56Z` - Carl Chalmers (@Clamps251) - PR: [chore(deps): bump the github-actions group with 2 updates](https://github.com/microsoft/SPARROW/pull/85)
- [Merge pull request #92 from microsoft/security-dependency-bumps](https://github.com/microsoft/SPARROW/commit/8fa31e8b1396b76efabca4a8294188881a6cf121) - `2026-11-12T13:36:22Z` - Bruno Demuro (@brucedemuro) - PR: [deps: patch security alerts in certifi, urllib3, Pillow, filelock](https://github.com/microsoft/SPARROW/pull/92)
- [deps: patch security alerts in certifi, urllib3, Pillow, filelock](https://github.com/microsoft/SPARROW/commit/c8261f2931853bd5ef45603b24e209effbe9bc41) - `2026-11-12T13:13:27Z` - Carl Chalmers - PR: [deps: patch security alerts in certifi, urllib3, Pillow, filelock](https://github.com/microsoft/SPARROW/pull/92)
- [Merge pull request #91 from microsoft/rename-robin-to-sparrow-mini](https://github.com/microsoft/SPARROW/commit/f3684bf74aea854abb51e1061796f6f6e4084322) - `2026-11-12T13:11:08Z` - Bruno Demuro (@brucedemuro) - PR: [setup: rename ROBIN to SPARROW Mini](https://github.com/microsoft/SPARROW/pull/91)
- [setup: rename ROBIN to SPARROW Mini](https://github.com/microsoft/SPARROW/commit/c072c393b50ce32f9bfd33fe62e8d0cd7cab5ded) - `2026-11-12T13:05:31Z` - Carl Chalmers - PR: [setup: rename ROBIN to SPARROW Mini](https://github.com/microsoft/SPARROW/pull/91)

### MicrosoftDocs/dynamics365smb-devitpro-pb (5 commit(s), signal 90)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/a8bab753f2a6988e0d07d4f222f25b38f0ea2510) - `2026-11-12T13:04:04Z` - Learn Build Service GitHub App
- [Merge pull request #8154 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/9076ce5ffb315a4b4725b8a15e4ab8298c2e9924) - `2026-11-12T13:03:22Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add video link to early-access-preview-edit-with-copilot.md (#8152)](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/dc20aa40c75ef8638f6de97dfd6be1eae23e96a2) - `2026-11-12T08:44:18Z` - jswymer (@jswymer)
- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/2fff6d8462857117becf24abeafa53f0e77f46b2) - `2026-11-11T19:03:49Z` - Learn Build Service GitHub App
- [Merge pull request #8153 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/2a0a855157fa5c6682512da2c2a0273b7288bfd3) - `2026-11-11T19:03:04Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### OfficeDev/Microsoft-Teams-Samples (5 commit(s), signal 45)

Tags: `human-authored, samples`

- [Merge pull request #2410 from OfficeDev/v-hrajandira/UpdateReadme](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/3149f69b80c653c3c2a74ecf3af892bf9c01d087) - `2026-11-12T12:02:12Z` - Harikrishnan-MSFT (@Harikrishnan-MSFT) - PR: [docs: Improve README formatting for bot-signalr-default-mode sample](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2410)
- [docs: Improve README formatting for bot-signalr-default-mode sample](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/fd51d3193d6ac37cb5daaeab6fde765540b0f667) - `2026-11-12T11:55:13Z` - Harikrishnan Rajandiran (Tata Consultancy Services Limi) (@Harikrishnan-MSFT) - PR: [docs: Improve README formatting for bot-signalr-default-mode sample](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2410)
- [Merge pull request #2409 from OfficeDev/v-hrajandira/bot-signalr-defa…](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/4a2cc6a95cf9a86f5c4e5896af533609e2e3a2cf) - `2026-11-12T10:02:19Z` - Harikrishnan-MSFT (@Harikrishnan-MSFT) - PR: [Add Teams bot sample using Azure SignalR default-mode socket delivery](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2409)
- [Updated Package Lock](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/a28eb02e0549f662c2fdccbd495c10a119a58ba4) - `2026-11-12T07:19:00Z` - Harikrishnan Rajandiran (Tata Consultancy Services Limi) (@Harikrishnan-MSFT) - PR: [Add Teams bot sample using Azure SignalR default-mode socket delivery](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2409)
- [Replaced APX to ACS](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/077ab44d632038ef1baa68184617d1ba1b985920) - `2026-11-12T07:16:16Z` - Harikrishnan Rajandiran (Tata Consultancy Services Limi) (@Harikrishnan-MSFT) - PR: [Add Teams bot sample using Azure SignalR default-mode socket delivery](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2409)

### MicrosoftDocs/sql-docs (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/sql-docs…](https://github.com/MicrosoftDocs/sql-docs/commit/b2c0f105ac46c2886471d04548b55bdc2d7409e4) - `2026-11-11T23:37:06Z` - Learn Build Service GitHub App
- [Merge pull request #38594 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/sql-docs/commit/c0c288e4815604d342d61fe470737c4b67feec15) - `2026-11-11T23:34:51Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Confirm merge from FromPublicRepo to main to sync with https://github…](https://github.com/MicrosoftDocs/sql-docs/commit/cabd62871339e0bba970a07251a9055b00312eeb) - `2026-11-11T22:03:24Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merging changes synced from https://github.com/MicrosoftDocs/sql-docs…](https://github.com/MicrosoftDocs/sql-docs/commit/e27f113863bcd43a73118993bd9ec2c2cb46a37f) - `2026-11-11T18:37:14Z` - Learn Build Service GitHub App
- [Merge pull request #38593 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/sql-docs/commit/53d78a8892182a29659a7e742b9c013abd758c4b) - `2026-11-11T18:34:37Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### MicrosoftDocs/azure-stack-docs (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #4597 from MicrosoftDocs/main639300351057787027syn…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/ebe16c13d47c7799c67576fb6f3aec56dbd65f89) - `2026-11-11T23:05:17Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4597)
- [Merging changes synced from https://github.com/MicrosoftDocs/azure-st…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/f7eee3f2c8718d987347ed868ca818b14a5db39a) - `2026-11-11T23:05:01Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4597)
- [Merge pull request #22010 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-stack-docs/commit/ecb37e68574eb0b18d52d39e5c184141126e244c) - `2026-11-11T23:03:14Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4597)
- [Disconnected operations 2610 updates (#21981)](https://github.com/MicrosoftDocs/azure-stack-docs/commit/b46e7849c74d2137a5f856afb90a8e5fd21e050e) - `2026-11-11T20:16:27Z` - Manika Dhiman (@ManikaDhiman) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4597)
- [Merge pull request #22006 from arduppal/arduppal/edit-2ikgqk](https://github.com/MicrosoftDocs/azure-stack-docs/commit/e819137b4408e20e748a9a62dbc2da18af751faa) - `2026-11-11T19:20:57Z` - prmerger-automator[bot] (@prmerger-automator[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4597)

### microsoft/web-iq-samples (5 commit(s), signal 80)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Bump vite from 7.3.6 to 7.3.8 in /samples/python/foundry-voice-agent …](https://github.com/microsoft/web-iq-samples/commit/e57f92e8a2dd306772d6219a7e6db70bc72ca6b8) - `2026-11-11T21:20:32Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump vite from 7.3.6 to 7.3.8 in /samples/python/foundry-voice-agent](https://github.com/microsoft/web-iq-samples/pull/18)
- [Bump tinypool and vitest in /samples/python/foundry-voice-agent (#19)](https://github.com/microsoft/web-iq-samples/commit/77a845af57cc31fd2bcefb3ef2a51d20dfd511ad) - `2026-11-11T21:09:20Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump tinypool and vitest in /samples/python/foundry-voice-agent](https://github.com/microsoft/web-iq-samples/pull/19)
- [Bump source-map-js in /samples/python/foundry-voice-agent (#17)](https://github.com/microsoft/web-iq-samples/commit/d594a84678aca39ba1da3652be8be2f3c35f36fa) - `2026-11-11T21:07:27Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump source-map-js from 1.2.1 to 1.2.2 in /samples/python/foundry-voice-agent](https://github.com/microsoft/web-iq-samples/pull/17)
- [Add Auto claim check Python sample (#16)](https://github.com/microsoft/web-iq-samples/commit/df4708c844881fdb42dd5a7d5f25b5b0f1a07d02) - `2026-11-11T18:59:51Z` - Luis Gonzalez (@LuigiDiMaui) - PR: [Add Auto claim check Python sample](https://github.com/microsoft/web-iq-samples/pull/16)
- [Add Web IQ + Foundry Voice Agent Python sample (#12)](https://github.com/microsoft/web-iq-samples/commit/f92dfe6cdd8e1b84afbb49078cfbae6f20a18148) - `2026-11-11T18:55:18Z` - Dushan Tharmal (@dtharmal) - PR: [Add Web IQ + Foundry Voice Agent Python sample](https://github.com/microsoft/web-iq-samples/pull/12)

### Azure/azure-quickstart-templates (5 commit(s), signal 80)

Tags: `human-authored, samples, watchlist`

- [Ouldmo/copilot model (#14921)](https://github.com/Azure/azure-quickstart-templates/commit/7eb06a1456463338ef2074ceca9c56e7af2492c3) - `2026-11-11T20:11:44Z` - Ould (@ouldsid) - PR: [Ouldmo/copilot model](https://github.com/Azure/azure-quickstart-templates/pull/14921)
- [FinOps toolkit 15.0 - optimization-workbook update (#14900)](https://github.com/Azure/azure-quickstart-templates/commit/1c02b96771d4a80c5bdcc3adb2fca1e6f2873c22) - `2026-11-11T19:00:43Z` - Michael Flanakin (@flanakin) - PR: [FinOps toolkit 15.0 - optimization-workbook update](https://github.com/Azure/azure-quickstart-templates/pull/14900)
- [FinOps toolkit 15.0 - governance-workbook update (#14899)](https://github.com/Azure/azure-quickstart-templates/commit/9971bc0c9df56129b6d59c96c98c43578cd1b91b) - `2026-11-11T19:00:36Z` - Michael Flanakin (@flanakin) - PR: [FinOps toolkit 15.0 - governance-workbook update](https://github.com/Azure/azure-quickstart-templates/pull/14899)
- [FinOps toolkit 15.0 - finops-hub update (#14898)](https://github.com/Azure/azure-quickstart-templates/commit/1cc86bac3441ab63fa1442f4ad2a7e8ee7ea488f) - `2026-11-11T19:00:29Z` - Michael Flanakin (@flanakin) - PR: [FinOps toolkit 15.0 - finops-hub update](https://github.com/Azure/azure-quickstart-templates/pull/14898)
- [Mitigate pull_request_target as GitHub will automatically block it in…](https://github.com/Azure/azure-quickstart-templates/commit/6ba82dde1831b083c98336ad3281276d5c731497) - `2026-11-11T18:34:00Z` - Ould (@ouldsid) - PR: [Ouldmo/pull target](https://github.com/Azure/azure-quickstart-templates/pull/14902)

### microsoft/kiota-serialization-form-go (4 commit(s), signal 89)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #170 from hardikkaurani/fix/union-and-intersection…](https://github.com/microsoft/kiota-serialization-form-go/commit/ec6aaad8307a7d041678011688f2debadb52a448) - `2026-11-12T19:56:31Z` - Vincent Biret (@baywet) - PR: [fix(form): allow root delegation in WriteObjectValue for union and intersection types](https://github.com/microsoft/kiota-serialization-form-go/pull/170)
- [fix(form): reject non-empty object keys in WriteObjectValue regardles…](https://github.com/microsoft/kiota-serialization-form-go/commit/793ba6d3427daade507acfe358e08da99946e6b2) - `2026-11-12T15:45:45Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(form): allow root delegation in WriteObjectValue for union and intersection types](https://github.com/microsoft/kiota-serialization-form-go/pull/170)
- [Merge pull request #171 from microsoft/dependabot/github_actions/code…](https://github.com/microsoft/kiota-serialization-form-go/commit/f3ca4e70861bc6620fe6177a036d424d07f5e950) - `2026-11-11T20:11:08Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump the codeql group with 3 updates](https://github.com/microsoft/kiota-serialization-form-go/pull/171)
- [build(deps): bump the codeql group with 3 updates](https://github.com/microsoft/kiota-serialization-form-go/commit/9e7c6edefae0b77ee311337dff904b1c0a09825a) - `2026-11-11T19:55:34Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump the codeql group with 3 updates](https://github.com/microsoft/kiota-serialization-form-go/pull/171)

### Azure/azure-sdk-for-rust (4 commit(s), signal 104)

Tags: `docs, human-authored, product:Azure SDK, security, watchlist`

- [Bump github/gh-aw-actions/setup-cli from 1.0.1 to 1.2.0 in the github…](https://github.com/Azure/azure-sdk-for-rust/commit/4e0804582bb1e205fdfa3eae129fe03c47bec387) - `2026-11-12T19:31:19Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump github/gh-aw-actions/setup-cli from 1.0.1 to 1.2.0 in the github-actions group](https://github.com/Azure/azure-sdk-for-rust/pull/5592)
- [Add GitHubActionsCredential to azure_identity (#5588)](https://github.com/Azure/azure-sdk-for-rust/commit/403d597280cc140f7bb8020882c9c92482df9655) - `2026-11-12T19:06:44Z` - Copilot (@Copilot) - PR: [Add GitHubActionsCredential to azure_identity](https://github.com/Azure/azure-sdk-for-rust/pull/5588)
- [Cosmos: Make ORDER BY pages binary-aware (#5409)](https://github.com/Azure/azure-sdk-for-rust/commit/efe3108185c19cfb77ec3d2b4203cd7ec51cf8a5) - `2026-11-12T18:40:33Z` - Simon Moreno (@simorenoh) - PR: [Cosmos: Make ORDER BY pages binary-aware](https://github.com/Azure/azure-sdk-for-rust/pull/5409)
- [Load session topology on demand (#5585)](https://github.com/Azure/azure-sdk-for-rust/commit/735401bec4b83868b6737bc9a9911b656fb96aed) - `2026-11-12T18:19:59Z` - Tomas Varon (@tvaron3) - PR: [Load session topology on demand](https://github.com/Azure/azure-sdk-for-rust/pull/5585)

### dotnet/docs (4 commit(s), signal 89)

Tags: `docs, human-authored, release-language, watchlist`

- [Update .NET 11 release documentation (#56871)](https://github.com/dotnet/docs/commit/c3377f5f732f604c8f9bffc14d814dd35c99f3c0) - `2026-11-12T18:49:07Z` - Copilot (@Copilot) - PR: [Update .NET 11 release documentation](https://github.com/dotnet/docs/pull/56871)
- [Everyday C#: Consolidate namespace coverage (#56771)](https://github.com/dotnet/docs/commit/678c15c744ffe9f18ad6d721a9553635f755db41) - `2026-11-12T17:56:33Z` - Bill Wagner (@BillWagner) - PR: [Everyday C#: Consolidate namespace coverage](https://github.com/dotnet/docs/pull/56771)
- [Update .NET version filters and date in API index (#56873)](https://github.com/dotnet/docs/commit/2c4951ce076e32e303dd5d3844f2989f9c555065) - `2026-11-12T16:46:58Z` - Genevieve Warren (@gewarren) - PR: [Update .NET version filters and date in API index](https://github.com/dotnet/docs/pull/56873)
- [Update snippets 5000 container (#56874)](https://github.com/dotnet/docs/commit/abe4b551044157a7b74911c21ca64f2657f291ee) - `2026-11-12T16:41:08Z` - Bill Wagner (@BillWagner) - PR: [Update snippets 5000 container](https://github.com/dotnet/docs/pull/56874)

### microsoft/Biodiversity (4 commit(s), signal 44)

Tags: `human-authored, training`

- [Merge pull request #667 from microsoft/fix/docs-deploy-python](https://github.com/microsoft/Biodiversity/commit/0ebe0551309bd2cd256d53c8ce47d856b3a0619c) - `2026-11-12T17:37:46Z` - Zhongqi Miao (@zhmiao) - PR: [ci(docs): build the docs site with Python 3.12](https://github.com/microsoft/Biodiversity/pull/667)
- [ci(docs): build the docs site with Python 3.12](https://github.com/microsoft/Biodiversity/commit/a68ee875f4ad889f7f3c4e375f4cde3bf9795d26) - `2026-11-12T17:37:33Z` - zhmiao (@zhmiao) - PR: [ci(docs): build the docs site with Python 3.12](https://github.com/microsoft/Biodiversity/pull/667)
- [Merge pull request #666 from microsoft/chore/sparrow-playground-trans…](https://github.com/microsoft/Biodiversity/commit/5846e7bdcb12a8a03560b0389301e3f6a2b9e721) - `2026-11-12T17:34:02Z` - Zhongqi Miao (@zhmiao) - PR: [docs: PyTorch-Wildlife is now SPARROW Playground](https://github.com/microsoft/Biodiversity/pull/666)
- [docs: announce PyTorch-Wildlife is now SPARROW Playground](https://github.com/microsoft/Biodiversity/commit/b25b014b0eff39d1158c46ebc345380266510d10) - `2026-11-12T17:33:46Z` - zhmiao (@zhmiao) - PR: [docs: PyTorch-Wildlife is now SPARROW Playground](https://github.com/microsoft/Biodiversity/pull/666)

### microsoft/viva-insights-sample-code (4 commit(s), signal 79)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Merge pull request #44 from martinctc/docs/query-reference-icons](https://github.com/microsoft/viva-insights-sample-code/commit/7e3fd590b8b0e862bb007f7080e31ef9fc614504) - `2026-11-12T14:07:59Z` - Martin Chan (@martinctc) - PR: [feat(frontier): add analysis prompts and query icons](https://github.com/microsoft/viva-insights-sample-code/pull/44)
- [docs(frontier): make coding-agent quick start actionable](https://github.com/microsoft/viva-insights-sample-code/commit/213ffd4aedf1df02f4a24a704f627cd9afa3ad82) - `2026-11-12T14:03:06Z` - Martin Chan (@martinctc) - PR: [feat(frontier): add analysis prompts and query icons](https://github.com/microsoft/viva-insights-sample-code/pull/44)
- [docs(frontier): reference external collaboration query icon](https://github.com/microsoft/viva-insights-sample-code/commit/d7f689c2d6dd10b5000f75f5151399daf81c52a5) - `2026-11-12T12:32:23Z` - Martin Chan (@martinctc) - PR: [feat(frontier): add analysis prompts and query icons](https://github.com/microsoft/viva-insights-sample-code/pull/44)
- [Merge pull request #45 from microsoft/dependabot/github_actions/githu…](https://github.com/microsoft/viva-insights-sample-code/commit/3734205b7ff71d5117177ba4bb7d0952c596c2a9) - `2026-11-12T10:09:36Z` - Martin Chan (@martinctc) - PR: [build(deps): bump the github-actions group with 2 updates](https://github.com/microsoft/viva-insights-sample-code/pull/45)

### Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob (4 commit(s), signal 0)

Tags: `bot-only, dependency-noise, samples`

- [Bump minimatch and rimraf in /src (#26)](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob/commit/14e385b7bf52b7cf64ea1e7b6b2d9e8d5e71dae2) - `2026-11-12T03:10:15Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump minimatch and rimraf in /src](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob/pull/26)
- [Bump brace-expansion from 5.0.7 to 5.0.13 in /src (#27)](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob/commit/02b43f24545d0a9bed8e8bd171257353a7bb382f) - `2026-11-12T03:09:08Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump brace-expansion from 5.0.7 to 5.0.13 in /src](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob/pull/27)
- [Bump @azure/msal-node and @azure/identity in /src (#28)](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob/commit/e37cdd49e245648cc9e33be0814638a09ae76102) - `2026-11-12T03:07:41Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump @azure/msal-node and @azure/identity in /src](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob/pull/28)
- [Bump fast-xml-parser from 5.9.0 to 5.12.0 in /src (#25)](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob/commit/7c965aaf45185181451f5d5067d509ee01367dcd) - `2026-11-12T03:02:09Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump fast-xml-parser from 5.9.0 to 5.12.0 in /src](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob/pull/25)

### Azure-Samples/azuresandbox (4 commit(s), signal 129)

Tags: `human-authored, release, release-language, samples, watchlist`

- Release: [Azure Sandbox v6.0.8](https://github.com/Azure-Samples/azuresandbox/releases/tag/v6.0.8) - `2026-11-12T01:43:32Z`
- [Merge pull request #1046 from Azure-Samples/vnext](https://github.com/Azure-Samples/azuresandbox/commit/3ab2d77a7711d905ef65aefd216fe57fa2037381) - `2026-11-12T01:40:30Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Release vnext to main](https://github.com/Azure-Samples/azuresandbox/pull/1046)
- [Retry RoleAssignmentExists after grant-jit-roles.sh --force removal (…](https://github.com/Azure-Samples/azuresandbox/commit/fa6ed13b6e4becbecc5c604fe07df942f77b0559) - `2026-11-11T22:32:04Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Retry RoleAssignmentExists after grant-jit-roles.sh --force removal (#1044)](https://github.com/Azure-Samples/azuresandbox/pull/1045)
- [Don't fail the sandbox job or release gate on evidence upload failure…](https://github.com/Azure-Samples/azuresandbox/commit/d9e228adffdf95ea33850cb2c8c48e9efeaa3400) - `2026-11-11T21:22:21Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Maintenance: don't fail release gate on evidence upload failure (#1040)](https://github.com/Azure-Samples/azuresandbox/pull/1042)
- [Don't fail the sandbox job or release gate on evidence upload failure…](https://github.com/Azure-Samples/azuresandbox/commit/ead0f01f35a4e68ae20b837c7de5882ed86baddf) - `2026-11-11T21:17:37Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Don't fail the sandbox job or release gate on evidence upload failure (#1040)](https://github.com/Azure-Samples/azuresandbox/pull/1041)

### microsoft/kiota-java (4 commit(s), signal 29)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #2248 from microsoft/dependabot/github_actions/act…](https://github.com/microsoft/kiota-java/commit/54ec7b4ec0cd17c0b46b3b7f4f794066c8c0b972) - `2026-11-12T00:40:11Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(deps): bump actions/setup-java from 6.1.0 to 6.2.0](https://github.com/microsoft/kiota-java/pull/2248)
- [Merge pull request #2247 from microsoft/dependabot/github_actions/cod…](https://github.com/microsoft/kiota-java/commit/c5f00b8742e794d16059dc58476000b0be1d6722) - `2026-11-12T00:39:17Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(deps): bump the codeql group with 3 updates](https://github.com/microsoft/kiota-java/pull/2247)
- [chore(deps): bump actions/setup-java from 6.1.0 to 6.2.0](https://github.com/microsoft/kiota-java/commit/16e72423005fb6e704074f15e945e9cc456348f2) - `2026-11-11T22:32:49Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump actions/setup-java from 6.1.0 to 6.2.0](https://github.com/microsoft/kiota-java/pull/2248)
- [chore(deps): bump the codeql group with 3 updates](https://github.com/microsoft/kiota-java/commit/637a200bd92b1419ca8602374a79666b11107122) - `2026-11-11T22:32:42Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump the codeql group with 3 updates](https://github.com/microsoft/kiota-java/pull/2247)

### microsoft/zerotrustassessment (4 commit(s), signal 44)

Tags: `human-authored, samples`

- [updating ZTW AI Pillar (#1640)](https://github.com/microsoft/zerotrustassessment/commit/970ccfed76bba1923a111acc39ed00b8426deac8) - `2026-11-11T23:27:18Z` - Anton Staykov (@astaykov) - PR: [updating ZTW AI Pillar](https://github.com/microsoft/zerotrustassessment/pull/1640)
- [New Updates (#1639)](https://github.com/microsoft/zerotrustassessment/commit/87ba7d16fb4cc2c59c15907677b6b2a40d7e7942) - `2026-11-11T22:59:48Z` - Tyler Chan (@tylchan) - PR: [New Updates](https://github.com/microsoft/zerotrustassessment/pull/1639)
- [New Updates](https://github.com/microsoft/zerotrustassessment/commit/03b867d2e3331a41f32c27ecb2c8fbfcd467ce03) - `2026-11-11T21:01:03Z` - Tyler Chan (@tylchan) - PR: [New Updates](https://github.com/microsoft/zerotrustassessment/pull/1639)
- [New Updates](https://github.com/microsoft/zerotrustassessment/commit/8f283fe1fb2874dc8a0c06eadea34adc1e35f44c) - `2026-11-11T19:15:15Z` - Tyler Chan (@tylchan) - PR: [New Updates](https://github.com/microsoft/zerotrustassessment/pull/1639)

### MicrosoftDocs/azure-monitor-docs (4 commit(s), signal 89)

Tags: `docs, human-authored, release-language, watchlist`

- [Merge pull request #5780 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/2148a72c7bd1cf60bf12a54f07907e9f20f73d21) - `2026-11-11T23:10:06Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #5779 from Nathan-Mangum/docs/pipeline-verificatio…](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/1c3cb6c3a114e6a404b486cb633d2bc7d30f16aa) - `2026-11-11T21:20:24Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Fix Azure Monitor pipeline deployment verification](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/08c2d31809500615656857434d297f393ade2849) - `2026-11-11T21:10:00Z` - Nathan Mangum
- [Document Azure Monitor pipeline on Linux VMs and Arc (preview) (#5732)](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/87e5426f5a66423d35da2fca0a6f94b4c6f74c6d) - `2026-11-11T19:31:14Z` - Nathan Mangum (@Nathan-Mangum)

### Azure/dacs (4 commit(s), signal 104)

Tags: `human-authored, samples, security, watchlist`

- [fix(build): patch native image critical vulnerabilities](https://github.com/Azure/dacs/commit/27ec57c7df9de9c507ce1c997e33b2d0d27630ce) - `2026-11-11T20:43:56Z` - Joshua Long (@jmclong) - PR: [ci: scan all built images and upgrade Runai packages](https://github.com/Azure/dacs/pull/181)
- [fix: scan all built images and upgrade Runai packages](https://github.com/Azure/dacs/commit/a4988f19e3f5b983bf19703c36690a5662ef8302) - `2026-11-11T20:43:56Z` - Joshua Long (@jmclong) - PR: [ci: scan all built images and upgrade Runai packages](https://github.com/Azure/dacs/pull/181)
- [ci(deps): bump the github-actions group with 4 updates](https://github.com/Azure/dacs/commit/944fb4c5e668089cb99da70f6732e8db0b369278) - `2026-11-11T19:10:17Z` - dependabot[bot] (@dependabot[bot]) - PR: [ci(deps): bump the github-actions group with 4 updates](https://github.com/Azure/dacs/pull/180)
- [build(deps): bump the docker group across 2 directories with 1 update](https://github.com/Azure/dacs/commit/dd2df8d03bd5a4472f63304377c0bc0f4bdd445a) - `2026-11-11T19:09:51Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump the docker group across 2 directories with 1 update](https://github.com/Azure/dacs/pull/179)

### Azure-Samples/confidential-computing (3 commit(s), signal 43)

Tags: `human-authored, samples`

- [Merge pull request #46 from vinfnet/aks-gpu-example](https://github.com/Azure-Samples/confidential-computing/commit/83eb7c397a649f0563198115fab22b67aad96b43) - `2026-11-12T16:29:03Z` - Simon Gallagher (@vinfnet) - PR: [Add guide-only confidential H100 AKS worker automation](https://github.com/Azure-Samples/confidential-computing/pull/46)
- [Signpost the confidential H100 AKS worker sample](https://github.com/Azure-Samples/confidential-computing/commit/3768050708f438c76b21d24ea72791db6e659e8b) - `2026-11-12T16:26:08Z` - Simon Gallagher (@sgallagherMS) - PR: [Add guide-only confidential H100 AKS worker automation](https://github.com/Azure-Samples/confidential-computing/pull/46)
- [Replace experimental GPU worker with guide-only AKS automation](https://github.com/Azure-Samples/confidential-computing/commit/28f5729b3bd70912b343cbe3012783e1bc43a730) - `2026-11-12T15:00:20Z` - Simon Gallagher (@sgallagherMS) - PR: [Add guide-only confidential H100 AKS worker automation](https://github.com/Azure-Samples/confidential-computing/pull/46)

### MicrosoftLearning/trainer-demo-deploy (3 commit(s), signal 78)

Tags: `human-authored, training, watchlist`

- [Merge pull request #178 from MicrosoftLearning/post-merge-93-metadata…](https://github.com/MicrosoftLearning/trainer-demo-deploy/commit/dc563139e6edd78ddbcf287e973ef6ddaed011fc) - `2026-11-12T15:38:50Z` - Rob Foulkrod (@rob-foulkrod) - PR: [Fix ToDo template catalog metadata](https://github.com/MicrosoftLearning/trainer-demo-deploy/pull/178)
- [Fix ToDo template catalog metadata](https://github.com/MicrosoftLearning/trainer-demo-deploy/commit/62fef2de43d7aeca4b410b0ceb6fadc0534062ac) - `2026-11-12T15:18:24Z` - rob foulkrod - PR: [Fix ToDo template catalog metadata](https://github.com/MicrosoftLearning/trainer-demo-deploy/pull/178)
- [Merge pull request #93 from massimobonanni/AddTodoListRazorFunctions](https://github.com/MicrosoftLearning/trainer-demo-deploy/commit/ff2127d750598ac824793a7629de4a5fb49b0672) - `2026-11-12T14:59:50Z` - Rob Foulkrod (@rob-foulkrod) - PR: [Add todo list razor pages + functions + table storage demo](https://github.com/MicrosoftLearning/trainer-demo-deploy/pull/93)

### microsoft/amplifier-acp-lab (3 commit(s), signal 83)

Tags: `human-authored, release, training`

- Release: [Lab 0.4.1 — self-contained native packages](https://github.com/microsoft/amplifier-acp-lab/releases/tag/v0.4.1) - `2026-11-12T13:03:57Z`
- [Run ACP Lab from self-contained native packages (#8)](https://github.com/microsoft/amplifier-acp-lab/commit/083e600bb8232b1e1db7016ca3912e132b426cf2) - `2026-11-12T13:01:04Z` - Brian Krabach (@bkrabach) - PR: [Run ACP Lab from self-contained native packages](https://github.com/microsoft/amplifier-acp-lab/pull/8)
- [Separate Lab experiment promises from execution reference (#7)](https://github.com/microsoft/amplifier-acp-lab/commit/a0f6f8c8a1fb263a4f9e9a20c92be66d7d1a02d4) - `2026-11-11T23:54:40Z` - Brian Krabach (@bkrabach) - PR: [Separate Lab promises from its execution reference](https://github.com/microsoft/amplifier-acp-lab/pull/7)
- [docs: align Lab vision and relocate execution contracts (#6)](https://github.com/microsoft/amplifier-acp-lab/commit/a4324d0d7c83602e9f28c07b4368bc76933fdec8) - `2026-11-11T19:39:32Z` - Brian Krabach (@bkrabach) - PR: [docs: clarify Lab vision and execution contract ownership](https://github.com/microsoft/amplifier-acp-lab/pull/6)

### Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample (3 commit(s), signal 43)

Tags: `human-authored, samples`

- [Support branch-specific BYOT packages (#98)](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/commit/8529c9ed25b28b4b3322ae6992d66a69659deca6) - `2026-11-11T23:59:29Z` - siyixian (@siyixian) - PR: [Support branch-specific BYOT packages](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/pull/98)
- [Configure Infobip voice sender and single TTS requests (#96)](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/commit/de48803122d797b164c5b6cf876e5bd7fd408161) - `2026-11-11T21:50:22Z` - siyixian (@siyixian) - PR: [Configure Infobip voice sender and single TTS requests](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/pull/96)
- [Bump the github-actions group across 1 directory with 2 updates (#92)](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/commit/1eb72069260fcd7b20b9b0bdaed6addf60574b57) - `2026-11-11T19:44:05Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the github-actions group across 1 directory with 2 updates](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/pull/92)

### MicrosoftDocs/m365copilot-docs (3 commit(s), signal 88)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/m365copi…](https://github.com/MicrosoftDocs/m365copilot-docs/commit/8dee3989a22f3218d174f8ba36db7a720ce3f652) - `2026-11-11T21:59:56Z` - Learn Build Service GitHub App
- [Merge pull request #1805 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/m365copilot-docs/commit/655be250e6c197fc07517be694880210e35b9185) - `2026-11-11T21:59:28Z` - Jason Johnston (@jasonjoh)
- [Document generally available Copilot Chat skills (#1801)](https://github.com/MicrosoftDocs/m365copilot-docs/commit/74a7890bb0c89018759e6f711a60960428694acc) - `2026-11-11T20:06:24Z` - Jason Johnston (@jasonjoh)

### MicrosoftDocs/teams-ai-library (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [11/11 publish (#93)](https://github.com/MicrosoftDocs/teams-ai-library/commit/f01e912434ba4ea174d3e164b5bb2273bdaf81e9) - `2026-11-11T21:43:33Z` - Nick Walker (@nickwalkmsft)
- [Redirect fixes](https://github.com/MicrosoftDocs/teams-ai-library/commit/4052df1948e8bf060c971c5ab4b6a86aea11e327) - `2026-11-11T21:35:20Z` - Nick Walker (@nickwalkmsft)
- [Redirects (#91)](https://github.com/MicrosoftDocs/teams-ai-library/commit/540cb977702ac4065e48f611e78da41e95345b05) - `2026-11-11T21:20:40Z` - Nick Walker (@nickwalkmsft)

### MicrosoftDocs/cpp-docs (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #5981 from MicrosoftDocs/main639300189200887463syn…](https://github.com/MicrosoftDocs/cpp-docs/commit/af4947c4bdf5993dcaee98e63d55a2d7a5744d7d) - `2026-11-11T18:35:30Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/cpp-docs/pull/5981)
- [Merging changes synced from https://github.com/MicrosoftDocs/cpp-docs…](https://github.com/MicrosoftDocs/cpp-docs/commit/7636e580806b50dad169d01c27cd36c9ec65795d) - `2026-11-11T18:35:16Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/cpp-docs/pull/5981)
- [Merge pull request #6860 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/cpp-docs/commit/5a314b331201c5bae4d271a32247317e9f11a67c) - `2026-11-11T18:34:04Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/cpp-docs/pull/5981)

### Azure/azure-relay-node (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #129 from Azure/fix-hyco-https-accept-crash](https://github.com/Azure/azure-relay-node/commit/ae155284a50c8f9da48c93c3ef763d80a96ceec5) - `2026-11-12T20:18:07Z` - Kala Anantharaman (@kalkeea) - PR: [hyco-https accept crash fix](https://github.com/Azure/azure-relay-node/pull/129)
- [Use Relay-prefixed WebSocket rejection parameters](https://github.com/Azure/azure-relay-node/commit/2c4aa3a6f069450c11d6536b187e261ee6dbcdf1) - `2026-11-11T19:12:53Z` - Jacob (@jbjordan) - PR: [hyco-https accept crash fix](https://github.com/Azure/azure-relay-node/pull/129)

### Azure-Samples/semantic-kernel-customer-assistant-demo-java (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Merge pull request #98 from Azure-Samples/dependabot/github_actions/g…](https://github.com/Azure-Samples/semantic-kernel-customer-assistant-demo-java/commit/d3817ecf7e3c6258be5ab2cb6e189b1abae68349) - `2026-11-12T20:04:58Z` - Martijn Verburg (@karianna) - PR: [Bump actions/setup-java from 6.1.0 to 6.2.0 in the github-actions group](https://github.com/Azure-Samples/semantic-kernel-customer-assistant-demo-java/pull/98)
- [Bump actions/setup-java from 6.1.0 to 6.2.0 in the github-actions group](https://github.com/Azure-Samples/semantic-kernel-customer-assistant-demo-java/commit/902253d949ad7a477fd49e916bc17ba11207ebef) - `2026-11-12T14:34:34Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-java from 6.1.0 to 6.2.0 in the github-actions group](https://github.com/Azure-Samples/semantic-kernel-customer-assistant-demo-java/pull/98)

### MicrosoftDocs/windows-iot-public (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #732 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/windows-iot-public/commit/1690dfb1bf9ecb2aea1195ffc60705a3b93c6b01) - `2026-11-12T19:04:22Z` - Valentyna Filimonova (@v-fvalentyna)
- [Adding AI at the edge of IoT documentation (#731)](https://github.com/MicrosoftDocs/windows-iot-public/commit/84c04fb3a9943f3ffa4c485e3eaa968376b5dc64) - `2026-11-12T18:42:20Z` - Valentyna Filimonova (@v-fvalentyna)

### microsoftgraph/msgraph-sample-react-native (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, product:Azure SDK, product:Microsoft Graph, samples, watchlist`

- [Merge pull request #191 from microsoftgraph/dependabot/github_actions…](https://github.com/microsoftgraph/msgraph-sample-react-native/commit/82c283851d0216c1c087e7b7d55225af92f68a98) - `2026-11-12T19:02:20Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump actions/setup-java from 6.1.0 to 6.2.0 in the github-actions group](https://github.com/microsoftgraph/msgraph-sample-react-native/pull/191)
- [Bump actions/setup-java from 6.1.0 to 6.2.0 in the github-actions group](https://github.com/microsoftgraph/msgraph-sample-react-native/commit/b6391f3ec5b4b1a4fffba614e9a411c4b8321feb) - `2026-11-12T18:55:01Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-java from 6.1.0 to 6.2.0 in the github-actions group](https://github.com/microsoftgraph/msgraph-sample-react-native/pull/191)

### dotnet/blazor-samples (2 commit(s), signal 42)

Tags: `bot-only, dependency-noise, samples, security, watchlist`

- [Bump the nuget group with 3 updates (#691)](https://github.com/dotnet/blazor-samples/commit/f05a64eaa14ed9e98c3b298661cdec136cc86f9d) - `2026-11-12T17:48:12Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the nuget group with 3 updates](https://github.com/dotnet/blazor-samples/pull/691)
- [Bump step-security/harden-runner (#690)](https://github.com/dotnet/blazor-samples/commit/dbfba0248398aff3233854707bdafb4c33866a79) - `2026-11-12T17:47:17Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump step-security/harden-runner from 2.22.3 to 2.22.4 in the github-actions group](https://github.com/dotnet/blazor-samples/pull/690)

### dotnet/docs-actions (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, watchlist`

- [Bump the github-actions group with 3 updates (#46)](https://github.com/dotnet/docs-actions/commit/9b76b6d7ea3fb905fec8564e06523ab669ae0f8c) - `2026-11-12T16:45:29Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the github-actions group with 3 updates](https://github.com/dotnet/docs-actions/pull/46)
- [Bump dotnet/sdk (#45)](https://github.com/dotnet/docs-actions/commit/a72a8d75503f942966e80e86dbc62edeedbd1b2c) - `2026-11-11T23:47:08Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump dotnet/sdk from 10.0 to 11.0 in /dependabot-bot/src/dependabot-bot in the docker group](https://github.com/dotnet/docs-actions/pull/45)

### MicrosoftLearning/c-sharp-minor (2 commit(s), signal 77)

Tags: `human-authored, training, watchlist`

- [Merge pull request #6 from MicrosoftLearning/dependabot/github_action…](https://github.com/MicrosoftLearning/c-sharp-minor/commit/e07376cb38bbebdb38fe8821666509e46906e2bf) - `2026-11-12T15:40:21Z` - Graeme Malcolm (@GraemeMalcolm) - PR: [Bump actions/setup-dotnet from 6.0.0 to 6.1.0 in the github-actions group](https://github.com/MicrosoftLearning/c-sharp-minor/pull/6)
- [Bump actions/setup-dotnet](https://github.com/MicrosoftLearning/c-sharp-minor/commit/2fd84f7fda0771c310ad2a7a86a60748e952f710) - `2026-11-12T14:44:33Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-dotnet from 6.0.0 to 6.1.0 in the github-actions group](https://github.com/MicrosoftLearning/c-sharp-minor/pull/6)

### dotnet/EntityFramework.Docs (2 commit(s), signal 52)

Tags: `docs, human-authored, release-language`

- [Update platforms.md to reflect EOL for EF Core versions (#5519)](https://github.com/dotnet/EntityFramework.Docs/commit/5fa9f7b63ae7ff93d631f4ddc47fdc9f72dcbdc7) - `2026-11-12T13:04:13Z` - Jiri Cincura ↹ (@cincuranet) - PR: [Update platforms.md to reflect EOL for EF Core versions](https://github.com/dotnet/EntityFramework.Docs/pull/5519)
- [Update API reference URL to version 11.0 (#5514)](https://github.com/dotnet/EntityFramework.Docs/commit/6046840965947de880940568c3dfaa3c965f2f02) - `2026-11-12T12:57:17Z` - Jiri Cincura ↹ (@cincuranet) - PR: [Update API reference URL to version 11.0](https://github.com/dotnet/EntityFramework.Docs/pull/5514)

### microsoft/power-pages-samples (2 commit(s), signal 77)

Tags: `human-authored, samples, watchlist`

- [Bump the github-actions group with 2 updates (#224)](https://github.com/microsoft/power-pages-samples/commit/caea20b910cf731725e56c1ad943205ea5a1af18) - `2026-11-12T09:26:04Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the github-actions group with 2 updates](https://github.com/microsoft/power-pages-samples/pull/224)
- [Add manual Copilot authentication smoke test (#225)](https://github.com/microsoft/power-pages-samples/commit/cffdd52ee55cbbb236207048e1803094567a12d5) - `2026-11-12T09:25:33Z` - Priyanshu Agrawal (@priyanshu92) - PR: [Add manual Copilot GITHUB_TOKEN authentication test](https://github.com/microsoft/power-pages-samples/pull/225)

### Azure-Samples/ai-hub-gateway-solution-accelerator (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Merge pull request #183 from mohamedsaif/main](https://github.com/Azure-Samples/ai-hub-gateway-solution-accelerator/commit/ba0674c562099d252680d17222dc004a63019cfc) - `2026-11-12T08:58:55Z` - Mo (@mohamedsaif) - PR: [Bicep critical fixes](https://github.com/Azure-Samples/ai-hub-gateway-solution-accelerator/pull/183)
- [critical fixes to apim provisioning](https://github.com/Azure-Samples/ai-hub-gateway-solution-accelerator/commit/ddfe2a07f0a9e114dd8a1ed7d524f3cb504c53fb) - `2026-11-12T08:55:57Z` - Mo ZEN (@mohamedsaif) - PR: [Bicep critical fixes](https://github.com/Azure-Samples/ai-hub-gateway-solution-accelerator/pull/183)

### Azure-Samples/iot-hub-adr-mqtt5-preview (2 commit(s), signal 87)

Tags: `human-authored, release-language, samples, watchlist`

- [Merge pull request #1 from Azure-Samples/samples/initial-engineering-…](https://github.com/Azure-Samples/iot-hub-adr-mqtt5-preview/commit/4c632f2ed0c3db4d53368d9da18647e88b046a62) - `2026-11-12T06:06:10Z` - Usha Rathnavel (@Usha-Rathnavel)
- [Prepare samples for Microsoft MIT open-source release review](https://github.com/Azure-Samples/iot-hub-adr-mqtt5-preview/commit/bd8719e9b44ef0da7d6f1514b192b7097aea441f) - `2026-11-11T18:42:56Z` - Usha Rathnavel (@Usha-Rathnavel)

### Azure/Connectors-NET-Samples (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, product:Azure SDK, samples, watchlist`

- [Bump Microsoft.Extensions.Logging.Abstractions from 10.0.14 to 10.0.1…](https://github.com/Azure/Connectors-NET-Samples/commit/04fc430e2c70c563ab81b68db155082938c0b744) - `2026-11-12T03:08:45Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Extensions.Logging.Abstractions from 10.0.14 to 10.0.15](https://github.com/Azure/Connectors-NET-Samples/pull/95)
- [Bump Microsoft.Extensions.Options.DataAnnotations from 10.0.14 to 11.…](https://github.com/Azure/Connectors-NET-Samples/commit/adbf25c58fb8e07ee5b6a9bd9a184abd8cf94839) - `2026-11-12T02:44:19Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Extensions.Options.DataAnnotations from 10.0.14 to 11.0.0](https://github.com/Azure/Connectors-NET-Samples/pull/94)

### Azure-Samples/functions-quickstart-javascript-azd-eventgrid-blob (2 commit(s), signal 0)

Tags: `bot-only, dependency-noise, samples`

- [Bump @azure/msal-node and @azure/identity in /src (#16)](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-eventgrid-blob/commit/5db6f579dfba2ca2f21bf0df26c54352aee9f586) - `2026-11-12T03:06:45Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump @azure/msal-node and @azure/identity in /src](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-eventgrid-blob/pull/16)
- [Bump fast-xml-parser from 5.9.0 to 5.12.0 in /src (#15)](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-eventgrid-blob/commit/bc590211f27ec0eb74b37b377d77a163a520aaaf) - `2026-11-12T03:01:21Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump fast-xml-parser from 5.9.0 to 5.12.0 in /src](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-eventgrid-blob/pull/15)

### Azure-Samples/azure-search-openai-demo (2 commit(s), signal 77)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Fix adlsgen2setup.py for provisioned ADLS accounts and native permiss…](https://github.com/Azure-Samples/azure-search-openai-demo/commit/032406de4284ffb92eb73768a250dc61a5ce39ee) - `2026-11-12T00:49:40Z` - Pamela Fox (@pamelafox) - PR: [Fix adlsgen2setup.py for provisioned ADLS accounts and native permission ingestion](https://github.com/Azure-Samples/azure-search-openai-demo/pull/3273)
- [Remove integrated vectorization ingestion option (#3269)](https://github.com/Azure-Samples/azure-search-openai-demo/commit/39c1bd8429617e6635a2fcf97c1dcef14d507c01) - `2026-11-11T22:02:51Z` - Pamela Fox (@pamelafox) - PR: [Remove integrated vectorization ingestion option](https://github.com/Azure-Samples/azure-search-openai-demo/pull/3269)

### microsoft/amplifier-module-provider-gemini (2 commit(s), signal 42)

Tags: `docs, human-authored`

- [Merge pull request #64 from microsoft/fix/native-signature-provenance…](https://github.com/microsoft/amplifier-module-provider-gemini/commit/e040c7cee5561c0b5b2df66a3dc8ac8cd2a4e043) - `2026-11-11T22:41:18Z` - Brian Krabach (@bkrabach) - PR: [fix: preserve Gemini native signature provenance and replay order](https://github.com/microsoft/amplifier-module-provider-gemini/pull/64)
- [fix: recover provenance for matching adapter signature copies](https://github.com/microsoft/amplifier-module-provider-gemini/commit/5cbee8f140e86d46b26362b0ad35aac203409eab) - `2026-11-11T20:17:57Z` - Brian Krabach (@bkrabach) - PR: [fix: preserve Gemini native signature provenance and replay order](https://github.com/microsoft/amplifier-module-provider-gemini/pull/64)

### MicrosoftDocs/win32 (2 commit(s), signal 87)

Tags: `docs, human-authored, release-language, watchlist`

- [Update cng-mldsa-examples.md to remove prerelease note (#2241)](https://github.com/MicrosoftDocs/win32/commit/bc82a65f74ef2c4f2f44a3d7db5f7cfebfdc3583) - `2026-11-11T21:59:14Z` - Emily Zhang (@emilyzhang47) - PR: [Update cng-mldsa-examples.md to remove prerelease note](https://github.com/MicrosoftDocs/win32/pull/2241)
- [Update ML-KEM documentation by removing note (#2240)](https://github.com/MicrosoftDocs/win32/commit/da62b289c58af645f6bec1f638839ee4b41557ad) - `2026-11-11T21:58:53Z` - Emily Zhang (@emilyzhang47) - PR: [Update ML-KEM documentation by removing note](https://github.com/MicrosoftDocs/win32/pull/2240)

### microsoftgraph/msgraph-snippets-typescript (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #449 from microsoftgraph/dependabot/npm_and_yarn/e…](https://github.com/microsoftgraph/msgraph-snippets-typescript/commit/ef0d772378ea0d9e957829162effb82d7f4bd41f) - `2026-11-11T21:24:32Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump eslint from 10.13.0 to 10.14.0](https://github.com/microsoftgraph/msgraph-snippets-typescript/pull/449)
- [Bump eslint from 10.13.0 to 10.14.0](https://github.com/microsoftgraph/msgraph-snippets-typescript/commit/59cb3158ecaf090fec7f066ead012c1f4910cd63) - `2026-11-11T21:23:04Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump eslint from 10.13.0 to 10.14.0](https://github.com/microsoftgraph/msgraph-snippets-typescript/pull/449)

### dotnet/Microsoft.Data.Sqlite.ApiDocs (2 commit(s), signal 42)

Tags: `docs, human-authored`

- [Merge pull request #72 from dotnet/smoke-test](https://github.com/dotnet/Microsoft.Data.Sqlite.ApiDocs/commit/6b183a15f25c8ca10ba68cdf68ead15dd987063b) - `2026-11-11T19:47:41Z` - Alma Jenks (@v-alje) - PR: [CI Update: https://dev.azure.com/msft-skilling/Content/_workitems/edit/643428](https://github.com/dotnet/Microsoft.Data.Sqlite.ApiDocs/pull/72)
- [CI Update](https://github.com/dotnet/Microsoft.Data.Sqlite.ApiDocs/commit/c09a02b232b2bd6952a2713c2b50f727b31657a1) - `2026-11-11T18:29:11Z` - docsreference@microsoft.com - PR: [CI Update: https://dev.azure.com/msft-skilling/Content/_workitems/edit/643428](https://github.com/dotnet/Microsoft.Data.Sqlite.ApiDocs/pull/72)

### Azure-Samples/modernize-bootcamp (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Merge pull request #100 from Azure-Samples/sojorgensen/reorganizing](https://github.com/Azure-Samples/modernize-bootcamp/commit/131fa47af7dad6c763738e19ee63559fff213c77) - `2026-11-11T19:37:22Z` - Sophie Jorgensen (@sophiejorgensen) - PR: [Sojorgensen/reorganizing](https://github.com/Azure-Samples/modernize-bootcamp/pull/100)
- [Organize Skillable labs and infrastructure](https://github.com/Azure-Samples/modernize-bootcamp/commit/b004f3fb4178e67a496b668c28b3a6a3b7128342) - `2026-11-11T19:35:17Z` - Sophie Jorgensen - PR: [Sojorgensen/reorganizing](https://github.com/Azure-Samples/modernize-bootcamp/pull/100)

### microsoft/forge-lab (1 commit(s), signal 41)

Tags: `human-authored, training`

- [Add 10 Windows CVEs to the CVE list](https://github.com/microsoft/forge-lab/commit/3a82b17d0d42b36dbd8c01e36dbc7feedd571023) - `2026-11-12T20:27:38Z` - Cen Zhang (@occia)

### Azure-Samples/functions-connectors-typescript (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add Dataverse samples and polling coverage for OneDrive, Blob, ShareP…](https://github.com/Azure-Samples/functions-connectors-typescript/commit/158d7e9944caa99f12ec481f1a837320720916d6) - `2026-11-12T18:29:18Z` - Swapnil Nagar (@swapnil-nagar) - PR: [Add Dataverse samples and polling coverage for OneDrive, Blob, SharePoint, and Teams](https://github.com/Azure-Samples/functions-connectors-typescript/pull/13)

### Azure/LogicAppsUX (1 commit(s), signal 116)

Tags: `docs, human-authored, release, watchlist`

- Release: [Release v5.1018.0](https://github.com/Azure/LogicAppsUX/releases/tag/v5.1018.0) - `2026-11-12T17:05:58Z`
- [docs: backfill the VS Code extension changelog (#9702)](https://github.com/Azure/LogicAppsUX/commit/ad39e70698a7408e2363479aa6ab194f350b1aa1) - `2026-11-12T18:19:09Z` - Brian Lam (@lambrianmsft) - PR: [docs: backfill the VS Code extension changelog](https://github.com/Azure/LogicAppsUX/pull/9702)

### OfficeDev/office-js-docs-reference (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Automatically generated docs (#2666)](https://github.com/OfficeDev/office-js-docs-reference/commit/0ac155e148ddaff9c9b8e860a090d790e6df1971) - `2026-11-12T18:13:09Z` - Elizabeth Samuel (@ElizabethSamuel-MSFT) - PR: [Automatically generated docs](https://github.com/OfficeDev/office-js-docs-reference/pull/2666)

### microsoft/content-processing-solution-accelerator (1 commit(s), signal 101)

Tags: `human-authored, samples, security, watchlist`

- [Merge pull request #727 from microsoft/psl-security-fix](https://github.com/microsoft/content-processing-solution-accelerator/commit/ed7c389b260209508b8cc1572950bee96b4ccb61) - `2026-11-12T17:24:53Z` - Roopan-Microsoft (@Roopan-Microsoft) - PR: [fix: restrict Azure authentication and image publishing to non-PR runs](https://github.com/microsoft/content-processing-solution-accelerator/pull/727)

### microsoft/Conversation-Knowledge-Mining-Solution-Accelerator (1 commit(s), signal 101)

Tags: `human-authored, samples, security, watchlist`

- [Merge pull request #1075 from microsoft/psl-security-fix](https://github.com/microsoft/Conversation-Knowledge-Mining-Solution-Accelerator/commit/92f532bb803c2e82c469755a386db8d797988ec0) - `2026-11-12T17:24:33Z` - Roopan-Microsoft (@Roopan-Microsoft) - PR: [fix: Add fork guard to workflow_run deploy and drop production env for PR …](https://github.com/microsoft/Conversation-Knowledge-Mining-Solution-Accelerator/pull/1075)

### microsoft/customer-chatbot-solution-accelerator (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Merge pull request #383 from microsoft/psl-icm](https://github.com/microsoft/customer-chatbot-solution-accelerator/commit/bd29886c197d5f8ee7020d00bfb2f700aab04e96) - `2026-11-12T17:22:44Z` - Roopan-Microsoft (@Roopan-Microsoft) - PR: [fix: Update GitHub Actions workflows to prevent production environment usage in pull request](https://github.com/microsoft/customer-chatbot-solution-accelerator/pull/383)

### SharePoint/sp-dev-docs (1 commit(s), signal 86)

Tags: `docs, human-authored, product:PowerShell, release-language, watchlist`

- [Use full SPFx 1.24.0 version in table of contents (#11092)](https://github.com/SharePoint/sp-dev-docs/commit/85ef646ac9b7ee546eabcb2abab9f43973a52820) - `2026-11-12T16:51:35Z` - Garry Trinder (@garrytrinder) - PR: [Use full SPFx 1.24.0 version in table of contents](https://github.com/SharePoint/sp-dev-docs/pull/11092)

### microsoft/finops-toolkit (1 commit(s), signal 76)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [feat(open-data): Add meter category to Services to split shared resou…](https://github.com/microsoft/finops-toolkit/commit/6ebd06573435168952b62c048f85ea46d8a2b30a) - `2026-11-12T16:32:43Z` - Michael Flanakin (@flanakin)

### MicrosoftDocs/windows-driver-docs (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Add Driver Quality Initiative (DQI) overview article (#3333)](https://github.com/MicrosoftDocs/windows-driver-docs/commit/022cd46f712a917e860bfe0ab21f478609d83e6a) - `2026-11-12T16:04:53Z` - rsameser (@rsameser)

### MicrosoftDocs/cloud-adoption-framework (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Add abbreviation for Service Bus topic subscription filter (#1438)](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/c93ec5f40b24e251c89c48480fb27891eeb2a6f3) - `2026-11-12T15:37:25Z` - balazs92117 (@balazs92117) - PR: [Add abbreviation for Service Bus topic subscription filter](https://github.com/MicrosoftDocs/cloud-adoption-framework/pull/1438)

### MicrosoftDocs/azure-docs-cli (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [CI Update](https://github.com/MicrosoftDocs/azure-docs-cli/commit/1c1fcf6fcb78902e348d0bd31d67883de7f02e95) - `2026-11-12T13:33:20Z` - docsreference@microsoft.com

### microsoft/vscode-custom-data (1 commit(s), signal 81)

Tags: `docs, human-authored, release`

- Release: [v0.6.4](https://github.com/microsoft/vscode-custom-data/releases/tag/v0.6.4) - `2026-11-12T14:43:56Z`
- [Prepare web custom data 0.7.0 (#146)](https://github.com/microsoft/vscode-custom-data/commit/bc8d6b025f14320f714711421be81bb904c11db7) - `2026-11-12T13:07:03Z` - Martin Aeschlimann (@aeschli) - PR: [Prepare web custom data 0.7.0](https://github.com/microsoft/vscode-custom-data/pull/146)

### dotnet/msbuild (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Revert "[main] Update dependencies from nuget/nuget.client (#15316)" …](https://github.com/dotnet/msbuild/commit/36212bbe82870bcb230a5b7a5f4366491ec776c4) - `2026-11-12T13:03:49Z` - Veronika Ovsyannikova (@OvesN) - PR: [Revert "[main] Update dependencies from nuget/nuget.client (#15316)"](https://github.com/dotnet/msbuild/pull/15534)

### MicrosoftDocs/windows-powershell-docs (1 commit(s), signal 76)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Update Set-DnsServerDiagnostics logging behavior (#4156)](https://github.com/MicrosoftDocs/windows-powershell-docs/commit/2029b4982aec04afffb01de06fe909997992d3ed) - `2026-11-12T12:34:46Z` - Robin Harwood (@robinharwood) - PR: [Update Set-DnsServerDiagnostics LogFilePath behavior](https://github.com/MicrosoftDocs/windows-powershell-docs/pull/4156)

### microsoft/fabric-terraform-quickstart (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, samples`

- [build(deps): bump the all group across 3 directories with 2 updates (…](https://github.com/microsoft/fabric-terraform-quickstart/commit/46b2158750340c8a13b7797e171da4b38b4aec2c) - `2026-11-12T10:36:58Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump the all group across 3 directories with 2 updates](https://github.com/microsoft/fabric-terraform-quickstart/pull/284)

### microsoft/d365-scm-telemetry (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add Warehouse Mobile App telemetry guide (#10)](https://github.com/microsoft/d365-scm-telemetry/commit/b33dc07cf0bfec4d2d55dbfa7700bfc34a19fdb6) - `2026-11-12T10:22:20Z` - Pedro Augusto Freitas de Souza (@pedroafsouza) - PR: [Add Warehouse Mobile App telemetry guide](https://github.com/microsoft/d365-scm-telemetry/pull/10)

### dotnet/msbuild-api-docs (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [CI Update: https://dev.azure.com/msft-skilling/Content/_workitems/edi…](https://github.com/dotnet/msbuild-api-docs/commit/ce2b653a624eb307756dec99db8c775bbbbd9b34) - `2026-11-12T09:33:35Z` - Alma Jenks (@v-alje) - PR: [CI Update: https://dev.azure.com/msft-skilling/Content/_workitems/edit/643572](https://github.com/dotnet/msbuild-api-docs/pull/75)

### microsoft/azure-devops-go-api (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Merge pull request #199 from danfiedler-msft/danfiedler/pin-actions](https://github.com/microsoft/azure-devops-go-api/commit/b98fd6cf2ea4f73674e9be9e9de1aac7046d187f) - `2026-11-12T09:22:05Z` - Petr Nechvátal (@nechvatalp) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/microsoft/azure-devops-go-api/pull/199)

### microsoft/copilot-extensibility (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Updated videos](https://github.com/microsoft/copilot-extensibility/commit/a473d6d9f9cfeae4e9a0364236f952be0b14b95f) - `2026-11-12T08:55:19Z` - Paolo Pialorsi (@PaoloPia)

### Azure/homebrew-azd (1 commit(s), signal 86)

Tags: `human-authored, product:Azure SDK, release-language, samples, watchlist`

- [Update for azd release 1.38.0-daily.7068363](https://github.com/Azure/homebrew-azd/commit/213033e8c58d204040fbeaa70a2609903942aa5b) - `2026-11-12T08:09:08Z` - azure-sdk (@azure-sdk)

### microsoft/azure-ai-search-foundry-iq-live-knowledge-sources (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Update reviewed dependencies and synchronize MkDocs compatibility (#38)](https://github.com/microsoft/azure-ai-search-foundry-iq-live-knowledge-sources/commit/f4c9985e064e185db18a7d5e9445e2b0fe7c310b) - `2026-11-12T08:07:27Z` - Hyeon Sang Jeon (@hyeonsangjeon) - PR: [Update reviewed dependencies and synchronize MkDocs compatibility](https://github.com/microsoft/azure-ai-search-foundry-iq-live-knowledge-sources/pull/38)

### Azure/azure-devops-cli-extension (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Refactor git and az command execution to use safe path (#1536)](https://github.com/Azure/azure-devops-cli-extension/commit/974106bbef9d923e85736df654ec57393f88f7e9) - `2026-11-12T06:41:10Z` - triptijain2112 (@triptijain2112) - PR: [Refactor git and az command execution to use safe path](https://github.com/Azure/azure-devops-cli-extension/pull/1536)

### dotnet/website-feedback (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Fix No Response workflow cache permissions (#1857)](https://github.com/dotnet/website-feedback/commit/40c76b54fc24a23c2dff16eb0caa43e85fb09c5a) - `2026-11-12T06:04:32Z` - Maira Wenzel (@mairaw) - PR: [Fix No Response workflow cache permissions](https://github.com/dotnet/website-feedback/pull/1857)

### Azure/confidential-computing-cvm-guest-attestation (1 commit(s), signal 76)

Tags: `human-authored, samples, watchlist`

- [Merge pull request #105 from SethBe/main](https://github.com/Azure/confidential-computing-cvm-guest-attestation/commit/1d4aad35201ad2b32393a42e50fb3780f8d38b20) - `2026-11-12T05:42:45Z` - Captain_Levi_Ackerman (@Bab95) - PR: [Skip installation of current pre-requisites installed](https://github.com/Azure/confidential-computing-cvm-guest-attestation/pull/105)

### Azure/awesome-azd (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Unify AI app templates into the Awesome azd catalog UX (#1109)](https://github.com/Azure/awesome-azd/commit/cc300c78ff364ad18cad9d2f82d24f9cac5562c9) - `2026-11-12T03:41:47Z` - hemarina (@hemarina) - PR: [Unify AI app templates into the Awesome azd catalog UX](https://github.com/Azure/awesome-azd/pull/1109)

### MicrosoftDocs/office-docs-powershell (1 commit(s), signal 76)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Clarify synthetic media detection settings in Teams meeting policy do…](https://github.com/MicrosoftDocs/office-docs-powershell/commit/0160cf63b0197f30689e31719fa4c30dfe0617ac) - `2026-11-12T03:35:45Z` - bkeerthivasa (@bkeerthivasa) - PR: [Clarify synthetic media detection settings in Teams meeting policy docs](https://github.com/MicrosoftDocs/office-docs-powershell/pull/13875)

### microsoft/WhatTheHack-Codespaces (1 commit(s), signal 41)

Tags: `human-authored, training`

- [Daily pull of student and resources folders](https://github.com/microsoft/WhatTheHack-Codespaces/commit/32820a721e8d52842925d97d1ede3bc0d6e6c180) - `2026-11-12T01:41:01Z` - GitHub Actions Codespace Automation (@actions-user)

### Azure/setup-azd (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, samples, watchlist`

- [build(deps): bump the github-actions group with 3 updates (#644)](https://github.com/Azure/setup-azd/commit/7e51a984b992a41b5b338d80add8c539680d1ea2) - `2026-11-11T23:56:13Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump the github-actions group with 3 updates](https://github.com/Azure/setup-azd/pull/644)

### dotnet/samples (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, docs`

- [Bump Aspire.Hosting.AppHost from 13.1.0 to 13.6.5 (#7142)](https://github.com/dotnet/samples/commit/3810558800760fc39282cc939bac645735514209) - `2026-11-11T23:34:41Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Aspire.Hosting.AppHost from 13.1.0 to 13.6.5](https://github.com/dotnet/samples/pull/7142)

### MicrosoftDocs/azure-docs-sdk-cpp (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-cpp/commit/695072456b31bd1707d67e2451083dbc63fa9191) - `2026-11-11T23:18:11Z` - azure-sdk (@azure-sdk)

### dotnet/docs-mobile (1 commit(s), signal 41)

Tags: `bot-only, dependency-noise, docs, security, watchlist`

- [Bump step-security/harden-runner from 2.21.1 to 2.22.4 (#159)](https://github.com/dotnet/docs-mobile/commit/f756c4a668c177ad3d1b0d60b4bc2d41ff1c9e0f) - `2026-11-11T22:49:32Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump step-security/harden-runner from 2.21.1 to 2.22.4](https://github.com/dotnet/docs-mobile/pull/159)

### microsoft/TypeAgent (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [memory: reduce repeated topic curation with frozen preparation (#3282)](https://github.com/microsoft/TypeAgent/commit/3317b2a4ab68e15ff6c23050b35e26997ad09105) - `2026-11-11T21:56:32Z` - Hillary Mutisya (@hillary-mutisya) - PR: [memory: reduce repeated topic curation with frozen preparation](https://github.com/microsoft/TypeAgent/pull/3282)

### microsoft/WindowsAppSDK-Samples (1 commit(s), signal 76)

Tags: `human-authored, product:Azure SDK, product:PowerShell, samples, watchlist`

- [Point Windows ML capture-logs to the Windows ML repository (#684)](https://github.com/microsoft/WindowsAppSDK-Samples/commit/128d55b5df1c0de188314a95db69244073ad3245) - `2026-11-11T21:49:10Z` - Siyuan (@sdotpeng) - PR: [Point Windows ML capture-logs to the Windows ML repository](https://github.com/microsoft/WindowsAppSDK-Samples/pull/684)

### dotnet/docs-tools (1 commit(s), signal 51)

Tags: `docs, human-authored, release-language`

- [Change visual studio version (#815)](https://github.com/dotnet/docs-tools/commit/9ca0b703fd60a176daf9d90df798454e4ca977df) - `2026-11-11T21:45:31Z` - Bill Wagner (@BillWagner) - PR: [Change visual studio version](https://github.com/dotnet/docs-tools/pull/815)

### microsoft/kiota (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [ci: adds a script to close pull requests when authors open too many o…](https://github.com/microsoft/kiota/commit/9977f7fb831adbd143aa22a9af6bcff8a4081444) - `2026-11-11T21:15:51Z` - Vincent Biret (@baywet) - PR: [ci: adds a script to close pull requests when authors open too many of them](https://github.com/microsoft/kiota/pull/8584)

### MicrosoftDocs/msteams-docs (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [SDK content migration (#14724)](https://github.com/MicrosoftDocs/msteams-docs/commit/c517690228d355e95b80847c255c8c71f6d88606) - `2026-11-11T21:06:26Z` - Nick Walker (@nickwalkmsft) - PR: [SDK content migration](https://github.com/MicrosoftDocs/msteams-docs/pull/14724)

### microsoft/amplifier-module-provider-anthropic (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Merge pull request #140 from microsoft/fix/thinking-prefix-binding](https://github.com/microsoft/amplifier-module-provider-anthropic/commit/46b0d34557dab8914e8eb897a3da6872475db154) - `2026-11-11T20:58:50Z` - Brian Krabach (@bkrabach) - PR: [fix: preserve Anthropic thinking across prefix-aware continuations](https://github.com/microsoft/amplifier-module-provider-anthropic/pull/140)

### Azure/iot-operations-sdks (1 commit(s), signal 86)

Tags: `docs, human-authored, product:Azure SDK, release-language, watchlist`

- [[Rust][Protocol][Connector] Bump version for 11/11/26 release (#1546)](https://github.com/Azure/iot-operations-sdks/commit/935cd68fcf3c855d538925dff6119fe58f1413c2) - `2026-11-11T20:49:25Z` - Carter Tinney (@cartertinney) - PR: [[Rust][Protocol][Connector] Bump version for 11/11/26 release](https://github.com/Azure/iot-operations-sdks/pull/1546)

### microsoft/nonprofit-agent-pack (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Update README example outputs](https://github.com/microsoft/nonprofit-agent-pack/commit/2d554ef0ac321aef0268653c15e69a0b2c14c5e4) - `2026-11-11T20:31:16Z` - Brett Randby (@brandby915)

### microsoftgraph/msgraph-sdk-java (1 commit(s), signal 86)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [ci: upgrade ESRP release task to v14 (#2714)](https://github.com/microsoftgraph/msgraph-sdk-java/commit/569c464ab1b23e7cdd30d067372c7e658da09033) - `2026-11-11T20:13:11Z` - Treicy Sanchez (@Treicysg) - PR: [ci: upgrade ESRP release task to v14](https://github.com/microsoftgraph/msgraph-sdk-java/pull/2714)

### microsoft/XBOX-Godot-NetRumble (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Fix fail-open voice communication privacy for XR015 (#28)](https://github.com/microsoft/XBOX-Godot-NetRumble/commit/c52cff03e1d5312eb746a63c687b9f0a3870dcff) - `2026-11-11T19:58:38Z` - James Lenell (@jameslen-atg) - PR: [Fix fail-open voice communication privacy for XR015](https://github.com/microsoft/XBOX-Godot-NetRumble/pull/28)

### Azure-Samples/explore-iot-operations (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add WASM operators for media capture and YOLOv8 inference (#228)](https://github.com/Azure-Samples/explore-iot-operations/commit/87f057b31d0f27eeb0bc4c6d17fa0e638768639a) - `2026-11-11T19:00:28Z` - jkarangula1 (@jkarangula1) - PR: [Add WASM operators for media capture and YOLOv8 inference](https://github.com/Azure-Samples/explore-iot-operations/pull/228)

### microsoft/dbt-fabricspark (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [fix: make shortcut updates safe and configurable (#330)](https://github.com/microsoft/dbt-fabricspark/commit/35050e265830cd9ab19cc6251373df5b0c73caa2) - `2026-11-11T18:53:20Z` - Raki (@mdrakiburrahman) - PR: [fix: make shortcut updates safe and configurable](https://github.com/microsoft/dbt-fabricspark/pull/330)

### Azure-Samples/Apim-Samples (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, samples`

- [Bump the github-actions group with 2 updates (#345)](https://github.com/Azure-Samples/Apim-Samples/commit/495438ff0e19fac7e8aac988f43d74c70c421e11) - `2026-11-11T18:53:18Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the github-actions group with 2 updates](https://github.com/Azure-Samples/Apim-Samples/pull/345)

### dotnet/EntityFramework.ApiDocs (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [CI Update (#158)](https://github.com/dotnet/EntityFramework.ApiDocs/commit/5ff4d3da8f3a88fd7586d660dd92da6aa8b09b44) - `2026-11-11T18:26:42Z` - Alma Jenks (@v-alje) - PR: [CI Update: https://dev.azure.com/msft-skilling/Content/_workitems/edit/643427](https://github.com/dotnet/EntityFramework.ApiDocs/pull/158)

### microsoft/kiota-serialization-text-go (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #183 from hardikkaurani/fix/primitive-parsing-and-…](https://github.com/microsoft/kiota-serialization-text-go/commit/8c883d123ec74b3e3d434037eb24887089f0df0e) - `2026-11-11T18:25:58Z` - Vincent Biret (@baywet) - PR: [fix(text): improve primitive parsing robustness, float32 precision, and scalar writer validation](https://github.com/microsoft/kiota-serialization-text-go/pull/183)

</details>
