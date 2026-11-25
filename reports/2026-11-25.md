# Microsoft Ecosystem Daily Brief - 2026-11-25

> Status: Fresh at generation. Current freshness is tracked in `reports/status.json`.
> Generated: 2026-11-25 22:37 UTC - Window: 25.5h from 2026-11-24 21:07 UTC to 2026-11-25 22:37 UTC.
> 122 repo(s) moved - 729 commit(s) - 11 release item(s) - 25 high-signal repo(s).

## Plain-English Summary

- Azure, .NET led the visible product-area activity in this window.
- 11 release item(s) were detected during the window.
- Security-related changes appeared in Azure/azure-sdk-for-js, MicrosoftDocs/entra-docs.
- Start with human-authored changes in Azure/azure-sdk-for-js, MicrosoftDocs/entra-docs, Azure/homebrew-azd, Azure/LogicAppsUX.
- 107 event(s) look automated, bot-heavy, dependency, or generated; review the curated sections before raw volume.

## Headline Metrics

| Metric | Value |
| --- | ---: |
| Inventory repositories | 16824 |
| Repositories after filters | 2526 |
| `pushed_at` candidates | 165 |
| Enrichment candidates | 165 |
| Repositories with movement | 122 |
| Default-branch commits | 729 |

## What Changed That Matters

| Repository | Score | Change | Actor | Noise | Headline | Time |
| --- | ---: | --- | --- | --- | --- | --- |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 100 | security_fix | human | low | [[Identity] Isolate DefaultAzureCredential IMDS probe tests from ambient credential env vars](https://github.com/Azure/azure-sdk-for-js/pull/40901) | `2026-11-25T19:34:06Z` |
| [MicrosoftDocs/entra-docs](https://github.com/MicrosoftDocs/entra-docs) | 100 | security_fix | human | low | [Publish GA docs for Baseline Security Mode app controls (#12114)](https://github.com/MicrosoftDocs/entra-docs/commit/a608d81e20fdc2ca6a6d60fb0314c7a38f69c897) | `2026-11-24T22:31:25Z` |
| [Azure/homebrew-azd](https://github.com/Azure/homebrew-azd) | 100 | release | human | low | [Update for azd release 1.40.0](https://github.com/Azure/homebrew-azd/commit/9f78e1a3f44deb24342f6905bbe43530a7323464) | `2026-11-25T21:35:43Z` |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 100 | release | unknown | low | [azure-dev-cli_1.40.0](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.40.0) | `2026-11-25T21:31:27Z` |
| [Azure/homebrew-azd](https://github.com/Azure/homebrew-azd) | 100 | release | human | low | [Update for azd release 1.40.0-daily.7114846](https://github.com/Azure/homebrew-azd/commit/8248c88d2e6133ce3cefd7952f14bf0436d98424) | `2026-11-25T20:57:23Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 100 | release | unknown | low | [com.azure+azure-data-appconfiguration_1.13.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-data-appconfiguration_1.13.0-beta.1) | `2026-11-25T19:52:51Z` |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 100 | release | human | low | [feat(ci): add Azure Pipelines npm publisher and Otto release trigger](https://github.com/Azure/LogicAppsUX/pull/9744) | `2026-11-25T16:46:38Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 100 | release | unknown | low | [@azure/keyvault-keys_4.11.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/keyvault-keys_4.11.0) | `2026-11-25T16:15:53Z` |
| [MicrosoftDocs/dynamics365smb-devitpro-pb](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb) | 100 | release | human | low | [Note that validation messages can mention another release or country/…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/119361794672d1b8fc6eda1044e7c5d637d8501c) | `2026-11-25T09:36:25Z` |
| [Azure/azure-devops-cli-extension](https://github.com/Azure/azure-devops-cli-extension) | 100 | release | human | low | [Post-Release-1.0.12](https://github.com/Azure/azure-devops-cli-extension/pull/1546) | `2026-11-25T06:56:31Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 100 | release | unknown | low | [horizondb 1.0.0b12](https://github.com/Azure/azure-cli-extensions/releases/tag/horizondb-1.0.0b12) | `2026-11-25T06:51:17Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 100 | release | human | low | [[Release] Update index.json for extension [ horizondb-1.0.0b12 ]](https://github.com/Azure/azure-cli-extensions/commit/495db6355c28323c02f06467632f404e4327c69c) | `2026-11-25T06:50:17Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 100 | release | unknown | low | [azure-template_1.0.0b7111123](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-template_1.0.0b7111123) | `2026-11-25T05:27:36Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 100 | release | unknown | low | [Spring Cloud Azure 6.6.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/spring-cloud-azure_6.6.0) | `2026-11-25T04:46:34Z` |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 100 | release | unknown | low | [Release v5.1025.0](https://github.com/Azure/LogicAppsUX/releases/tag/v5.1025.0) | `2026-11-25T01:43:12Z` |

## Product Areas

| Product area | Signal | Repos | Events | Releases | Security | Top links |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Azure | 93 | 71 | 149 | 10 | 1 | [[Identity] Isolate DefaultAzureCredential IMDS probe tests from ambient credential env vars](https://github.com/Azure/azure-sdk-for-js/pull/40901); [Update for azd release 1.40.0](https://github.com/Azure/homebrew-azd/commit/9f78e1a3f44deb24342f6905bbe43530a7323464); [azure-dev-cli_1.40.0](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.40.0) |
| Unmapped Activity | 39 | 14 | 51 | 0 | 0 | [First draft of module in my fork of release branch (#56943) (#56948)](https://github.com/MicrosoftDocs/learn/commit/eae82ad2ed9e73e00880fc49e3f1467ed863dca5); [Add known issue for duplicate rows in sql_pool_insights](https://github.com/MicrosoftDocs/sql-docs/commit/e41a00f877a9fa88ea0477c1c62a819c3930c8a6); [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/50db65e8e5e572fdbe8301c0ec7f976090ca3180) |
| .NET | 22 | 13 | 42 | 0 | 0 | [Put type parameter inference from constraints behind a feature flag.](https://github.com/dotnet/roslyn/pull/86624); [Add comprehensive What's New documentation for F# 7](https://github.com/dotnet/docs/pull/50098); [Add a regression test for #86608](https://github.com/dotnet/roslyn/pull/86625) |
| PowerShell | 13 | 6 | 14 | 1 | 0 | [Windows Package Manager 1.30.310](https://github.com/microsoft/winget-cli/releases/tag/v1.30.310); [Add option to ignore unknown upgrade notices](https://github.com/microsoft/winget-cli/pull/6696); [Fix incorrect (ThrottleRateActionBytesPerSecond) parameter to correct one (ThrottleRateActionBitsPerSecond) in New-NetQosPolicy](https://github.com/MicrosoftDocs/windows-powershell-docs/pull/3700) |
| Identity | 8 | 2 | 8 | 0 | 1 | [Publish GA docs for Baseline Security Mode app controls (#12114)](https://github.com/MicrosoftDocs/entra-docs/commit/a608d81e20fdc2ca6a6d60fb0314c7a38f69c897); [Note that validation messages can mention another release or country/…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/119361794672d1b8fc6eda1044e7c5d637d8501c); [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/431eb7e673b6a9581027f64325467b7516fe81d3) |
| Microsoft 365 | 8 | 4 | 12 | 0 | 0 | [Fix typo and enhance documentation for teams-dev skill](https://github.com/MicrosoftDocs/msteams-docs/pull/14779); [Run the ESRP npm publish on Node 20 with EsrpRelease@13](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3225); [Reorganize top-level TOC a bit](https://github.com/MicrosoftDocs/msteams-docs/pull/14773) |
| Microsoft Graph | 5 | 10 | 27 | 0 | 0 | [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10108); [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10107) |
| Developer Tools | 5 | 1 | 5 | 0 | 0 | [Update AI overview video](https://github.com/microsoft/vscode-docs/pull/10771); [Update banner and landing pages](https://github.com/microsoft/vscode-docs/pull/10772) |

## Today's Top Links

| Priority | Repository | Why read it |
| ---: | --- | --- |
| 1 | [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [Security-related change: [Identity] Isolate DefaultAzureCredential IMDS probe tests from ambient credential env vars](https://github.com/Azure/azure-sdk-for-js/pull/40901) |
| 2 | [MicrosoftDocs/entra-docs](https://github.com/MicrosoftDocs/entra-docs) | [Security-related change: Publish GA docs for Baseline Security Mode app controls (#12114)](https://github.com/MicrosoftDocs/entra-docs/commit/a608d81e20fdc2ca6a6d60fb0314c7a38f69c897) |
| 3 | [Azure/homebrew-azd](https://github.com/Azure/homebrew-azd) | [Release activity: Update for azd release 1.40.0](https://github.com/Azure/homebrew-azd/commit/9f78e1a3f44deb24342f6905bbe43530a7323464) |
| 4 | [Azure/azure-dev](https://github.com/Azure/azure-dev) | [Release activity: azure-dev-cli_1.40.0](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.40.0) |
| 5 | [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [Release activity: com.azure+azure-data-appconfiguration_1.13.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-data-appconfiguration_1.13.0-beta.1) |
| 6 | [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | [Release activity: feat(ci): add Azure Pipelines npm publisher and Otto release trigger](https://github.com/Azure/LogicAppsUX/pull/9744) |
| 7 | [MicrosoftDocs/dynamics365smb-devitpro-pb](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb) | [Release activity: Note that validation messages can mention another release or country/…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/119361794672d1b8fc6eda1044e7c5d637d8501c) |
| 8 | [Azure/azure-devops-cli-extension](https://github.com/Azure/azure-devops-cli-extension) | [Release activity: Post-Release-1.0.12](https://github.com/Azure/azure-devops-cli-extension/pull/1546) |

## Noise and Automation

- 107 event(s) look automated, bot-heavy, dependency, generated, or medium/high noise.
- Top noisy repositories: Azure/azure-sdk, microsoft/aspire-samples, Azure/azure-dev, microsoftgraph/msgraph-snippets-typescript, MicrosoftDocs/azure-docs.
- Noise mix: Dependency: 49, Docs: 39, CI/Infra: 7, Release: 6, Sample: 4, SDK: 1, Training: 1.

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
| Count batches | 5 |
| Detail batches | 4 |
| Repos counted | 165 |
| Repos enriched | 122 |

</details>

<details>
<summary>Show supporting signal, release, and lifecycle tables</summary>

## High-Signal Items

| Repository | Score | Tags |
| --- | ---: | --- |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 143 | docs, human-authored, product:Azure SDK, release, security, watchlist |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 131 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure/iot-operations-sdks](https://github.com/Azure/iot-operations-sdks) | 129 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 128 | docs, human-authored, release, release-language, watchlist |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 128 | docs, human-authored, release, release-language, watchlist |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 125 | human-authored, release, samples, watchlist |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 119 | docs, human-authored, product:Azure SDK, release, watchlist |
| [microsoft/winget-cli](https://github.com/microsoft/winget-cli) | 118 | docs, human-authored, product:PowerShell, release, watchlist |
| [MicrosoftDocs/entra-docs](https://github.com/MicrosoftDocs/entra-docs) | 114 | docs, human-authored, release-language, security, watchlist |
| [dotnet/docs](https://github.com/dotnet/docs) | 104 | docs, human-authored, product:Azure SDK, release-language, watchlist |
| [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs) | 100 | docs, human-authored, watchlist |
| [MicrosoftDocs/fabric-docs](https://github.com/MicrosoftDocs/fabric-docs) | 99 | docs, human-authored, watchlist |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 94 | docs, human-authored, product:Azure AI, product:Azure SDK, release-language, watchlist |
| [MicrosoftDocs/SupportArticles-docs](https://github.com/MicrosoftDocs/SupportArticles-docs) | 91 | docs, human-authored, product:Azure AI, watchlist |
| [Azure/homebrew-azd](https://github.com/Azure/homebrew-azd) | 91 | human-authored, product:Azure SDK, release-language, samples, watchlist |

## Watchlist Hits

| Repository | Score | Matches |
| --- | ---: | --- |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 143 | products: Azure SDK; repos: Azure/azure-sdk-for-js; orgs: Azure; keywords: sdk |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 131 | products: Azure SDK; repos: Azure/azure-sdk-for-python; orgs: Azure; keywords: release, sdk |
| [Azure/iot-operations-sdks](https://github.com/Azure/iot-operations-sdks) | 129 | products: Azure SDK; orgs: Azure; keywords: release, sdk |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 128 | orgs: Azure; keywords: release |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 128 | orgs: Azure; keywords: release |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 125 | orgs: Azure |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 119 | products: Azure SDK; repos: Azure/azure-sdk-for-java; orgs: Azure; keywords: sdk |
| [microsoft/winget-cli](https://github.com/microsoft/winget-cli) | 118 | products: PowerShell; keywords: powershell |
| [MicrosoftDocs/entra-docs](https://github.com/MicrosoftDocs/entra-docs) | 114 | orgs: MicrosoftDocs; keywords: entra, security |
| [dotnet/docs](https://github.com/dotnet/docs) | 104 | products: Azure SDK; keywords: copilot, sdk |
| [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs) | 100 | repos: MicrosoftDocs/azure-docs; orgs: MicrosoftDocs |
| [MicrosoftDocs/fabric-docs](https://github.com/MicrosoftDocs/fabric-docs) | 99 | orgs: MicrosoftDocs |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 94 | products: Azure AI, Azure SDK; repos: Azure/azure-sdk-for-net; orgs: Azure; keywords: agent, release, sdk |
| [MicrosoftDocs/SupportArticles-docs](https://github.com/MicrosoftDocs/SupportArticles-docs) | 91 | products: Azure AI; orgs: MicrosoftDocs; keywords: agent |
| [Azure/homebrew-azd](https://github.com/Azure/homebrew-azd) | 91 | products: Azure SDK; orgs: Azure; keywords: release, sdk |

## Releases

| Repository | Release | Published |
| --- | --- | --- |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | [azure-dev-cli_1.40.0](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.40.0) | `2026-11-25T21:31:27Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure+azure-data-appconfiguration_1.13.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-data-appconfiguration_1.13.0-beta.1) | `2026-11-25T19:52:51Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/keyvault-keys_4.11.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/keyvault-keys_4.11.0) | `2026-11-25T16:15:53Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [horizondb 1.0.0b12](https://github.com/Azure/azure-cli-extensions/releases/tag/horizondb-1.0.0b12) | `2026-11-25T06:51:17Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-template_1.0.0b7111123](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-template_1.0.0b7111123) | `2026-11-25T05:27:36Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [Spring Cloud Azure 6.6.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/spring-cloud-azure_6.6.0) | `2026-11-25T04:46:34Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure.spring+spring-messaging-azure_6.6.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.spring%2Bspring-messaging-azure_6.6.0) | `2026-11-25T02:37:26Z` |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | [Release v5.1025.0](https://github.com/Azure/LogicAppsUX/releases/tag/v5.1025.0) | `2026-11-25T01:43:12Z` |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | [azd-ext-azure-logicappsstandard_0.1.0](https://github.com/Azure/azure-dev/releases/tag/azd-ext-azure-logicappsstandard_0.1.0) | `2026-11-25T01:16:33Z` |
| [Azure/iot-operations-sdks](https://github.com/Azure/iot-operations-sdks) | [[Rust] mqtt@v1.3.1](https://github.com/Azure/iot-operations-sdks/releases/tag/rust/mqtt/v1.3.1) | `2026-11-25T00:21:06Z` |
| [microsoft/winget-cli](https://github.com/microsoft/winget-cli) | [Windows Package Manager 1.30.310](https://github.com/microsoft/winget-cli/releases/tag/v1.30.310) | `2026-11-24T22:13:34Z` |

## Repository Lifecycle

| Change | Count |
| --- | ---: |
| archived_changed | 2 |
| category_changed | 0 |
| default_branch_changed | 0 |
| fork_changed | 0 |
| new_repos | 1 |
| removed_repos | 0 |

## Category Summary

| Category | Repositories |
| --- | ---: |
| docs | 72 |
| samples | 48 |
| training | 2 |

## Organization Summary

| Org | Repositories |
| --- | ---: |
| Azure-Samples | 34 |
| MicrosoftDocs | 24 |
| microsoft | 23 |
| Azure | 22 |
| dotnet | 12 |
| OfficeDev | 3 |
| microsoftgraph | 2 |
| MicrosoftLearning | 1 |
| aspnet | 1 |

</details>

<details>
<summary>Show raw repository activity</summary>

## Busiest Repositories

| Repository | Signal | Category | Commits | Releases | Newest commit |
| --- | ---: | --- | ---: | ---: | --- |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 143 | docs | 3 | 1 | `2026-11-25T19:34:06Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 131 | docs | 6 | 1 | `2026-11-25T18:09:42Z` |
| [Azure/iot-operations-sdks](https://github.com/Azure/iot-operations-sdks) | 129 | docs | 4 | 1 | `2026-11-25T00:18:10Z` |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 128 | docs | 3 | 1 | `2026-11-25T16:46:57Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 128 | docs | 3 | 1 | `2026-11-25T06:50:17Z` |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 125 | samples | 10 | 2 | `2026-11-25T22:08:37Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 119 | docs | 4 | 3 | `2026-11-25T18:08:47Z` |
| [microsoft/winget-cli](https://github.com/microsoft/winget-cli) | 118 | docs | 3 | 1 | `2026-11-25T19:13:56Z` |
| [MicrosoftDocs/entra-docs](https://github.com/MicrosoftDocs/entra-docs) | 114 | docs | 4 | 0 | `2026-11-25T13:37:30Z` |
| [dotnet/docs](https://github.com/dotnet/docs) | 104 | docs | 19 | 0 | `2026-11-25T20:53:20Z` |
| [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs) | 100 | docs | 135 | 0 | `2026-11-25T18:17:59Z` |
| [MicrosoftDocs/fabric-docs](https://github.com/MicrosoftDocs/fabric-docs) | 99 | docs | 24 | 0 | `2026-11-25T12:06:28Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 94 | docs | 9 | 0 | `2026-11-25T20:08:32Z` |
| [MicrosoftDocs/SupportArticles-docs](https://github.com/MicrosoftDocs/SupportArticles-docs) | 91 | docs | 16 | 0 | `2026-11-25T22:06:33Z` |
| [Azure/homebrew-azd](https://github.com/Azure/homebrew-azd) | 91 | samples | 6 | 0 | `2026-11-25T21:35:43Z` |
| [MicrosoftDocs/dynamics365smb-devitpro-pb](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb) | 89 | docs | 4 | 0 | `2026-11-25T13:03:56Z` |
| [MicrosoftDocs/azure-dev-docs](https://github.com/MicrosoftDocs/azure-dev-docs) | 88 | docs | 3 | 0 | `2026-11-25T18:04:24Z` |
| [MicrosoftDocs/learn](https://github.com/MicrosoftDocs/learn) | 88 | docs | 3 | 0 | `2026-11-24T23:21:10Z` |
| [microsoft/vscode-docs](https://github.com/microsoft/vscode-docs) | 87 | docs | 12 | 0 | `2026-11-25T22:04:36Z` |
| [MicrosoftDocs/windows-powershell-docs](https://github.com/MicrosoftDocs/windows-powershell-docs) | 87 | docs | 12 | 0 | `2026-11-25T06:00:45Z` |

## Repository Details

### MicrosoftDocs/azure-docs (135 commit(s), signal 100)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #323111 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-docs/commit/fbb3cdea70027d6f60b84ed53f6eda2a8b98d9e4) - `2026-11-25T18:17:59Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #323109 from VincentLiu777/main](https://github.com/MicrosoftDocs/azure-docs/commit/cf0f344dc82acb58c76fb9968daafcf5372f60a5) - `2026-11-25T18:08:00Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #323106 from MicrosoftDocs/repo_sync_working_branch](https://github.com/MicrosoftDocs/azure-docs/commit/d195eb72c53b46f4d7ec0b269d6b300470f5ca65) - `2026-11-25T17:52:24Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Update publication date and regions in modify-file-share.md](https://github.com/MicrosoftDocs/azure-docs/commit/04136d505fe74c63df0ed5bc6c9b5dbb30aa5d90) - `2026-11-25T17:48:52Z` - Vincent Liu (@VincentLiu777)
- [Merge pull request #322982 from mrm9084/AudinceAutoDetectJava](https://github.com/MicrosoftDocs/azure-docs/commit/a5cd34819479071afd8df9edef870710da4cc695) - `2026-11-25T17:47:25Z` - prmerger-automator[bot] (@prmerger-automator[bot])

### dotnet/android-api-docs (121 commit(s), signal 65)

Tags: `docs, human-authored`

- [Fix documentation errors in AdServices (R008, pass 3) (#1896)](https://github.com/dotnet/android-api-docs/commit/11e93c2c934f896e2bb1c22d6a94ee7755c82bc7) - `2026-11-25T21:40:56Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Fix documentation errors in AdServices (R008, pass 3)](https://github.com/dotnet/android-api-docs/pull/1896)
- [Fix Khronos OpenGL ES documentation (R003, pass 3) (#1894)](https://github.com/dotnet/android-api-docs/commit/79c9b162c5bfae2cc2b6891fc31ab9051c33639a) - `2026-11-25T21:21:47Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Fix Khronos OpenGL ES documentation (R003, pass 3)](https://github.com/dotnet/android-api-docs/pull/1894)
- [Correct Apache HTTP authentication, cancellation, and domain parsing …](https://github.com/dotnet/android-api-docs/commit/ea3aca8632e5c340a063ca1e2443b0e33575e20c) - `2026-11-25T21:05:43Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Fix documentation errors in Apache HTTP implementations (R023, pass 3)](https://github.com/dotnet/android-api-docs/pull/1911)
- [Fix Java Util documentation errors (R022) (#1910)](https://github.com/dotnet/android-api-docs/commit/4bbd51a7b830f5875139a6f2b70f61633fa5aa4c) - `2026-11-25T20:23:24Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Fix Java Util documentation errors (R022, pass 3)](https://github.com/dotnet/android-api-docs/pull/1910)
- [Fix Dalvik opcode documentation (#1905)](https://github.com/dotnet/android-api-docs/commit/46d0be6dbb4bc3f76942f8809c7305ba49e87372) - `2026-11-25T19:24:00Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Fix Dalvik.Bytecode documentation errors (R018, pass 3)](https://github.com/dotnet/android-api-docs/pull/1905)

### OfficeDev/Microsoft-Teams-Samples (51 commit(s), signal 65)

Tags: `human-authored, samples`

- [Merge pull request #2496 from OfficeDev/fix/form-data-boundary-protob…](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/b2276ee1ebd447114510a1a4a6b79cf65c8e8cee) - `2026-11-25T15:34:29Z` - Harikrishnan-MSFT (@Harikrishnan-MSFT) - PR: [Fix 50 critical form-data and protobufjs dependency alerts](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2496)
- [Merge remote-tracking branch 'origin/main' into fix/form-data-boundar…](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/3a01fd696c2edcd94d34a60ee5a54dc32887311f) - `2026-11-25T14:51:46Z` - Harikrishnan-MSFT (@Harikrishnan-MSFT) - PR: [Fix 50 critical form-data and protobufjs dependency alerts](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2496)
- [Merge remote-tracking branch 'refs/remotes/origin/main' into fix/form…](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/dc0096e1cb05198b9a0c8888a65501b3862aba15) - `2026-11-25T14:42:25Z` - Harikrishnan-MSFT (@Harikrishnan-MSFT) - PR: [Fix 50 critical form-data and protobufjs dependency alerts](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2496)
- [Merge pull request #2495 from OfficeDev/fix/axios-ipv4-mapped-ipv6-al…](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/4d1656a2995d72bbb777d2dcdac4a5dcac26f92e) - `2026-11-25T14:40:30Z` - Harikrishnan-MSFT (@Harikrishnan-MSFT) - PR: [Fix 25 Axios IPv4-mapped IPv6 NO_PROXY alerts](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2495)
- [Merge remote-tracking branch 'refs/remotes/origin/main' into fix/axio…](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/7ac95dd4eaa3e6d23ce6d846b6e2f2cd1687815e) - `2026-11-25T14:29:19Z` - Harikrishnan-MSFT (@Harikrishnan-MSFT) - PR: [Fix 25 Axios IPv4-mapped IPv6 NO_PROXY alerts](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2495)

### dotnet/runtime (38 commit(s), signal 65)

Tags: `docs, human-authored`

- [Extend PR failure scan for servicing and infrastructure KBEs (#138158)](https://github.com/dotnet/runtime/commit/4fc48303381826ab92b8fb379d8e573ab397d71c) - `2026-11-25T21:01:34Z` - Viviana Dueñas (@ViveliDuCh) - PR: [Extend PR failure scan for servicing and infrastructure KBEs](https://github.com/dotnet/runtime/pull/138158)
- [Fix ActivityTagsCollection no-op in `Reset()` function (#138299)](https://github.com/dotnet/runtime/commit/210a89c8de442e7d61b440722710423444ac6319) - `2026-11-25T20:09:53Z` - Aaron Franke (@aaronfranke) - PR: [Fix ActivityTagsCollection no-op in `Reset()` function](https://github.com/dotnet/runtime/pull/138299)
- [Fix SmtpFailedRecipientsException constructor base null dereference (…](https://github.com/dotnet/runtime/commit/d07456f570ce5b6f7c7a828c8a1e8b5938063515) - `2026-11-25T20:00:44Z` - Aaron Franke (@aaronfranke) - PR: [Fix SmtpFailedRecipientsException constructor base null dereference](https://github.com/dotnet/runtime/pull/138297)
- [Avoid allocating in TransferCodingHeaderValue.ToString without parame…](https://github.com/dotnet/runtime/commit/555d220b5ccf74423ea50374081eec961b40441b) - `2026-11-25T19:56:43Z` - Asylkhan Azat (@asylkhan-azat) - PR: [Avoid allocating in TransferCodingHeaderValue.ToString without parameters](https://github.com/dotnet/runtime/pull/138284)
- [JIT: Add KnownBits analysis and use it to fold relops (#137936)](https://github.com/dotnet/runtime/commit/a4900e9049df3a94f3617cade7f6da919208620b) - `2026-11-25T19:35:09Z` - Egor Bogatov (@EgorBo) - PR: [JIT: Add KnownBits analysis and use it to fold relops](https://github.com/dotnet/runtime/pull/137936)

### MicrosoftDocs/fabric-docs (24 commit(s), signal 99)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #3544 from MicrosoftDocs/main639312051687482284syn…](https://github.com/MicrosoftDocs/fabric-docs/commit/26fad88331c0abe261e22fd2bbecb81811a4a40e) - `2026-11-25T12:06:28Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3544)
- [Merging changes synced from https://github.com/MicrosoftDocs/fabric-d…](https://github.com/MicrosoftDocs/fabric-docs/commit/a9e4269d3f5208fb91af5b28f656926933558668) - `2026-11-25T12:06:05Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3544)
- [Merge pull request #17549 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/fabric-docs/commit/5747b6d680017a57bd0443d51f311e66cf75da98) - `2026-11-25T12:02:52Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3544)
- [Merge pull request #17548 from RESET-USER/patch-20](https://github.com/MicrosoftDocs/fabric-docs/commit/7c3b7fce414b98b36a144b6c80c3c411a3bd24d9) - `2026-11-25T10:42:32Z` - prmerger-automator[bot] (@prmerger-automator[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3544)
- [Merge pull request #17547 from RESET-USER/patch-19](https://github.com/MicrosoftDocs/fabric-docs/commit/7f63db999a9bb438061f56d33fc188c8ff0d3152) - `2026-11-25T10:42:19Z` - prmerger-automator[bot] (@prmerger-automator[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3544)

### Azure/azure-sdk (23 commit(s), signal 58)

Tags: `bot-only, docs, product:Azure SDK, release-language, watchlist`

- [python release notes for the 2026-12 release (#10436)](https://github.com/Azure/azure-sdk/commit/ef6bbcf6b2bd97c71793440546f84e4be2f3e431) - `2026-11-25T21:34:27Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [python release notes for the 2026-12 release](https://github.com/Azure/azure-sdk/pull/10436)
- [js release notes for the 2026-12 release (#10435)](https://github.com/Azure/azure-sdk/commit/7dd1b2111d3851e66445c08be580b43b3af03bbe) - `2026-11-25T21:34:20Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [js release notes for the 2026-12 release](https://github.com/Azure/azure-sdk/pull/10435)
- [java release notes for the 2026-12 release (#10434)](https://github.com/Azure/azure-sdk/commit/887c5f0bf2e403a5b0abe5bb11892058ade3c0b4) - `2026-11-25T21:34:16Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [java release notes for the 2026-12 release](https://github.com/Azure/azure-sdk/pull/10434)
- [go release notes for the 2026-12 release (#10433)](https://github.com/Azure/azure-sdk/commit/475122f7c0993dfd14d5a41cc5969304fd217b24) - `2026-11-25T21:34:12Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [go release notes for the 2026-12 release](https://github.com/Azure/azure-sdk/pull/10433)
- [dotnet release notes for the 2026-12 release (#10432)](https://github.com/Azure/azure-sdk/commit/b26e65594a1a04d485b2f21e0643929f4377ce13) - `2026-11-25T21:33:49Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [dotnet release notes for the 2026-12 release](https://github.com/Azure/azure-sdk/pull/10432)

### dotnet/docs (19 commit(s), signal 104)

Tags: `docs, human-authored, product:Azure SDK, release-language, watchlist`

- [Update package index with latest published versions (#57022)](https://github.com/dotnet/docs/commit/e9abfc233527cc68f6dbe6262e181d1365f99d40) - `2026-11-25T20:53:20Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Update package index with latest published versions](https://github.com/dotnet/docs/pull/57022)
- [Correct required property guidance with System.Text.Json source gener…](https://github.com/dotnet/docs/commit/90f58e37c1d1e8de40864a687829c17190e9fab2) - `2026-11-25T20:52:17Z` - Manish Kumar (@Manish-1kumar) - PR: [Correct required property guidance with System.Text.Json source generation (Fixes #42480)](https://github.com/dotnet/docs/pull/56645)
- [Add comprehensive What's New documentation for F# 7 (#50098)](https://github.com/dotnet/docs/commit/cbd1f173b3d92fe12481aabb5b9964a7e59c8da8) - `2026-11-25T18:18:34Z` - Copilot (@Copilot) - PR: [Add comprehensive What's New documentation for F# 7](https://github.com/dotnet/docs/pull/50098)
- [Clarify debugging requirements when embedding symbols in NuGet packag…](https://github.com/dotnet/docs/commit/baf3a848bead7f554235be482a8ad6a30db122f5) - `2026-11-25T15:42:49Z` - surya pratap singh (@SkyDevLab) - PR: [Clarify debugging requirements when embedding symbols in NuGet packages](https://github.com/dotnet/docs/pull/56613)
- [Update LangVersion examples to emphasize production explicit versions…](https://github.com/dotnet/docs/commit/95cd0955aa29c1cdecd4b2c9b504471dc5b7bd4b) - `2026-11-25T15:25:07Z` - Manish Kumar (@Manish-1kumar) - PR: [Update LangVersion examples to emphasize production explicit versions over preview (Fixes #54202)](https://github.com/dotnet/docs/pull/56646)

### MicrosoftDocs/SupportArticles-docs (16 commit(s), signal 91)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/50db65e8e5e572fdbe8301c0ec7f976090ca3180) - `2026-11-25T22:06:33Z` - Learn Build Service GitHub App
- [Merge pull request #12973 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/2c8054fdc6deca4d72315549087130cd894c0fe5) - `2026-11-25T22:04:44Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Publish calendar publishing and subscription articles (#12709)](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/d65e7a7be37cdd5a8d93ceb5476aac4b56efebb6) - `2026-11-25T21:44:23Z` - Shane Ferrell (@Shanefe)
- [Update SFTP upload notification message details (#12964)](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/1654d14964a02e7d1c33ba8a53f1fd099c2152b2) - `2026-11-25T21:40:48Z` - Joe Swiercek (@jswiercek)
- [Updated MTRA article filename and TOC entry because the agent kept ov…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/8ba0a03aca47e2ae36177216383acf371e87c038) - `2026-11-25T20:54:03Z` - Meera Krishna (@Cloud-Writer)

### microsoft/vscode-docs (12 commit(s), signal 87)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #10772 from microsoft/ntrogh/main-stingray](https://github.com/microsoft/vscode-docs/commit/00562ad0ea648d0b5062d3f02a748636ecd945f5) - `2026-11-25T22:04:36Z` - Nick Trogh (@ntrogh) - PR: [Update banner and landing pages](https://github.com/microsoft/vscode-docs/pull/10772)
- [Update banner and landing pages](https://github.com/microsoft/vscode-docs/commit/a83cbf0ab40e72a9d5c9fe3e50b44be32332b751) - `2026-11-25T21:58:12Z` - Nick Trogh (@ntrogh) - PR: [Update banner and landing pages](https://github.com/microsoft/vscode-docs/pull/10772)
- [Merge pull request #10771 from microsoft/ntrogh/ai-overview-video](https://github.com/microsoft/vscode-docs/commit/82d337ee23facd3effdcf1736dfd1fe54a8f066f) - `2026-11-25T21:18:07Z` - Nick Trogh (@ntrogh) - PR: [Update AI overview video](https://github.com/microsoft/vscode-docs/pull/10771)
- [feat: add new video overview for building with AI in VS Code](https://github.com/microsoft/vscode-docs/commit/e026ac0e84d109ca9d79af675f221ecad24064c7) - `2026-11-25T20:55:03Z` - Nick Trogh (@ntrogh) - PR: [Update AI overview video](https://github.com/microsoft/vscode-docs/pull/10771)
- [feat: enhance storyboard validation for live AI and workspace controls](https://github.com/microsoft/vscode-docs/commit/df89212170e75813357e952e68a7cfda5c3c056f) - `2026-11-25T20:54:12Z` - Nick Trogh (@ntrogh) - PR: [Update AI overview video](https://github.com/microsoft/vscode-docs/pull/10771)

### MicrosoftDocs/windows-powershell-docs (12 commit(s), signal 87)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Fix ThrottleRateActionBytesPerSecond parameter to (#3700)](https://github.com/MicrosoftDocs/windows-powershell-docs/commit/17e4dc3c48450c1e7100a3983a5e047a986cc60d) - `2026-11-25T06:00:45Z` - Shun Tamura (@MrSaunaHut) - PR: [Fix incorrect (ThrottleRateActionBytesPerSecond) parameter to correct one (ThrottleRateActionBitsPerSecond) in New-NetQosPolicy](https://github.com/MicrosoftDocs/windows-powershell-docs/pull/3700)
- [Update Resolve-DnsName.md to include CheckCache option (#3897)](https://github.com/MicrosoftDocs/windows-powershell-docs/commit/f48f9d47110b2930b0fb0e7c1b8dbb50a582080e) - `2026-11-25T05:51:50Z` - Miguel Reyes (@miguelreyb) - PR: [Update Resolve-DnsName.md to include CheckCache option](https://github.com/MicrosoftDocs/windows-powershell-docs/pull/3897)
- [Fixed an error in the `-Name` description (#4108)](https://github.com/MicrosoftDocs/windows-powershell-docs/commit/00899b8dc420c0c3eaddae178aa44c58b38c23d6) - `2026-11-25T05:02:36Z` - Vladimir Blazhkun (@vblazhkun) - PR: [`-Name` description should list wildcards as supported](https://github.com/MicrosoftDocs/windows-powershell-docs/pull/4108)
- [Fix syntax for TextExtension parameter in example 5 (#4117)](https://github.com/MicrosoftDocs/windows-powershell-docs/commit/075bfab0a2b938f11596da3c73374d150803b64b) - `2026-11-25T04:26:03Z` - kapsiR (@kapsiR) - PR: [Fix syntax for TextExtension parameter in example 5](https://github.com/MicrosoftDocs/windows-powershell-docs/pull/4117)
- [Correct typo in Format-SecureBootUEFI.md (#4035)](https://github.com/MicrosoftDocs/windows-powershell-docs/commit/e7dff5223c41c5357a11170b227fd9a6e16725d9) - `2026-11-25T04:01:51Z` - sircompo (@sircompo) - PR: [Fixed a typo in Format-SecureBootUEFI.md](https://github.com/MicrosoftDocs/windows-powershell-docs/pull/4035)

### MicrosoftDocs/sql-docs (11 commit(s), signal 86)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/sql-docs…](https://github.com/MicrosoftDocs/sql-docs/commit/d25bfc1887b8386b8bdc6e6988f20ad279d223a8) - `2026-11-25T18:39:09Z` - Learn Build Service GitHub App
- [Merge pull request #38668 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/sql-docs/commit/996f93067cc08fb7d6f1409b82f7a50d6e5864b0) - `2026-11-25T18:37:00Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #38667 from mariyaali/sql-pool-insights-duplicate-…](https://github.com/MicrosoftDocs/sql-docs/commit/b70f5749ac22a31932f4295d918ef943105a3bc8) - `2026-11-25T18:24:12Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Add known issue for duplicate rows in sql_pool_insights](https://github.com/MicrosoftDocs/sql-docs/commit/e41a00f877a9fa88ea0477c1c62a819c3930c8a6) - `2026-11-25T18:18:30Z` - mariyaali (@mariyaali)
- [Merge pull request #38666 from RicardoMarques-msft/patch-3](https://github.com/MicrosoftDocs/sql-docs/commit/52772bc58f5fb07b010ec578bdf78598759b41b4) - `2026-11-25T14:55:58Z` - prmerger-automator[bot] (@prmerger-automator[bot])

### Azure/azure-dev (10 commit(s), signal 125)

Tags: `human-authored, release, samples, watchlist`

- Release: [azure-dev-cli_1.40.0](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.40.0) - `2026-11-25T21:31:27Z`
- Release: [azd-ext-azure-logicappsstandard_0.1.0](https://github.com/Azure/azure-dev/releases/tag/azd-ext-azure-logicappsstandard_0.1.0) - `2026-11-25T01:16:33Z`
- [`azd pipeline config`: Show hints under authentication options (#11021)](https://github.com/Azure/azure-dev/commit/17bf0b479c73e482e97cee277cd4e9ab5ed11acf) - `2026-11-25T22:08:37Z` - JeffreyCA (@JeffreyCA) - PR: [`azd pipeline config`: Show hints under authentication options](https://github.com/Azure/azure-dev/pull/11021)
- [Correct structured message graduation target to 1.40.0 (#11010)](https://github.com/Azure/azure-dev/commit/f4b6582b40342f6e546442db8003bb3e7142da81) - `2026-11-25T19:07:54Z` - Victor Vazquez (@vhvb1989) - PR: [Correct structured message graduation target to azd 1.40.0](https://github.com/Azure/azure-dev/pull/11010)
- [chore(deps): bump @hono/node-server in /cli/azd/test/evals (#10928)](https://github.com/Azure/azure-dev/commit/2ba8c54cfaf46ffb8e122cd35655c6712d57a6f8) - `2026-11-25T19:06:52Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump @hono/node-server from 2.1.5 to 2.1.8 in /cli/azd/test/evals](https://github.com/Azure/azure-dev/pull/10928)
- [chore(deps-dev): bump @hono/node-server in /eng/common/scripts/eval (…](https://github.com/Azure/azure-dev/commit/6ec3fa4dd2e8e644ed9b7d5593410bac9e0070ea) - `2026-11-25T19:06:26Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps-dev): bump @hono/node-server from 2.1.1 to 2.1.8 in /eng/common/scripts/eval](https://github.com/Azure/azure-dev/pull/10927)
- [chore(deps): bump zod from 4.4.3 to 4.6.7 in /cli/azd/test/evals (#10…](https://github.com/Azure/azure-dev/commit/c09464ec35f58c8b9332f7e683964554f0663d69) - `2026-11-25T19:04:48Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump zod from 4.4.3 to 4.6.7 in /cli/azd/test/evals](https://github.com/Azure/azure-dev/pull/10725)

### Azure/azure-sdk-for-net (9 commit(s), signal 94)

Tags: `docs, human-authored, product:Azure AI, product:Azure SDK, release-language, watchlist`

- [Make Core ListRequestOrder an extensible enum (#65184)](https://github.com/Azure/azure-sdk-for-net/commit/a2f1935b7ef974743d99f2d5f22eebd0d45c4b28) - `2026-11-25T20:08:32Z` - Shiva S (@Shivakishore14) - PR: [[AgentServer] Core: make ListRequestOrder an extensible enum and pin storage spec](https://github.com/Azure/azure-sdk-for-net/pull/65184)
- [Sync eng/common for Tools PR 17635 (#65181)](https://github.com/Azure/azure-sdk-for-net/commit/c4b2b354dd91047ea90984968705f39cbe92d4c9) - `2026-11-25T18:09:12Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17635](https://github.com/Azure/azure-sdk-for-net/pull/65181)
- [Update azure-typespec/http-client-csharp-mgmt version to prerelease 1…](https://github.com/Azure/azure-sdk-for-net/commit/9f960c414c0269843bc2d6237394a8b5f38f66d8) - `2026-11-25T11:22:03Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Update azure-typespec/http-client-csharp-mgmt version to prerelease 1.0.0-alpha.20261124.1](https://github.com/Azure/azure-sdk-for-net/pull/65158)
- [Update Web PubSub Chat for August 2026 preview APIs (#63836)](https://github.com/Azure/azure-sdk-for-net/commit/a1db94850064886de4f7ca3184e27d6a61e25d3f) - `2026-11-25T09:07:50Z` - yzt (@Y-Sindo) - PR: [[Web PubSub Chat] Add August preview APIs](https://github.com/Azure/azure-sdk-for-net/pull/63836)
- [Validate identifiers when joining Socket.IO rooms (#65141)](https://github.com/Azure/azure-sdk-for-net/commit/e598487a5b8bcb0de2048d19294e3640a810c504) - `2026-11-25T05:12:03Z` - Chenyang Liu (@zackliu) - PR: [Validate identifiers when joining Socket.IO rooms](https://github.com/Azure/azure-sdk-for-net/pull/65141)

### dotnet/efcore (7 commit(s), signal 47)

Tags: `docs, human-authored`

- [Scaffold against a new snapshot instance when the shared one is final…](https://github.com/dotnet/efcore/commit/22471d9d391dbb64ea0d21d41f26e0e85b0302e4) - `2026-11-25T22:22:52Z` - Pieterjan (@PieterjanDeClippel) - PR: [Scaffold against a new snapshot instance when the shared one is finalized](https://github.com/dotnet/efcore/pull/39784)
- [Merge pull request #39802 from richlander/richlander/helix-azurelinux4](https://github.com/dotnet/efcore/commit/58124c8674b15bfce62824406041bdaccb071613) - `2026-11-25T13:50:04Z` - Rich Lander (@richlander) - PR: [Run Helix tests on Azure Linux 4 hosts](https://github.com/dotnet/efcore/pull/39802)
- [Reset the pending indent in IndentedStringBuilder.Clear (#39795)](https://github.com/dotnet/efcore/commit/eb7530a1776f0a98580294652fde4c2e955afdff) - `2026-11-25T11:56:40Z` - İlker amca (@ilkertskn) - PR: [Reset the pending indent in IndentedStringBuilder.Clear](https://github.com/dotnet/efcore/pull/39795)
- [Run Helix tests on Azure Linux 4 hosts](https://github.com/dotnet/efcore/commit/ab37888748246d7e65b283c14ee693de99cfc641) - `2026-11-25T05:35:07Z` - richlander (@richlander) - PR: [Run Helix tests on Azure Linux 4 hosts](https://github.com/dotnet/efcore/pull/39802)
- [Bump System.CommandLine from 2.0.13 to 3.0.0 (#39773)](https://github.com/dotnet/efcore/commit/94d389560b812dd84e4a9768827831c0a0d9c10b) - `2026-11-24T23:00:04Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump System.CommandLine from 2.0.13 to 3.0.0](https://github.com/dotnet/efcore/pull/39773)

### dotnet/roslyn (7 commit(s), signal 82)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Revert "Removing legacy DTL DartLab templates" (#86627)](https://github.com/dotnet/roslyn/commit/20d93666c3abdaa7579c8a0bd452379d58e51ae7) - `2026-11-25T21:56:15Z` - Julia Ni (@nijulia) - PR: [Revert "Removing legacy DTL DartLab templates"](https://github.com/dotnet/roslyn/pull/86627)
- [Revert "Removing legacy DTL DartLab templates"](https://github.com/dotnet/roslyn/commit/53b3ef67378e04fc71abac77e43e322f6ddaea47) - `2026-11-25T19:54:48Z` - Julia Ni (@nijulia) - PR: [Revert "Removing legacy DTL DartLab templates"](https://github.com/dotnet/roslyn/pull/86627)
- [Put type parameter inference from constraints behind a feature flag. …](https://github.com/dotnet/roslyn/commit/07bfd7b8b2083244731a252fc99196beca25c0d5) - `2026-11-25T18:39:31Z` - AlekseyTs (@AlekseyTs) - PR: [Put type parameter inference from constraints behind a feature flag.](https://github.com/dotnet/roslyn/pull/86624)
- [Add a regression test for #86608 (#86625)](https://github.com/dotnet/roslyn/commit/b97c2faae5514e884b86a4e1b25d680b447a68a5) - `2026-11-25T18:03:44Z` - AlekseyTs (@AlekseyTs) - PR: [Add a regression test for #86608](https://github.com/dotnet/roslyn/pull/86625)
- [Document inference dependency breaking change (#86617)](https://github.com/dotnet/roslyn/commit/458d3e8293cda7167070ddb5a55da2543007af39) - `2026-11-25T14:05:33Z` - AlekseyTs (@AlekseyTs) - PR: [Document inference dependency breaking change](https://github.com/dotnet/roslyn/pull/86617)

### Azure-Samples/azure-finops-agent (7 commit(s), signal 82)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Let users choose the Entra tenant before Azure sign-in](https://github.com/Azure-Samples/azure-finops-agent/commit/7f998d92bccf7f99230f772d86fa6403424bd66c) - `2026-11-25T16:40:22Z` - Ali Reza Farahnak (@alfarahn)
- [fix: improve search indexing signals](https://github.com/Azure-Samples/azure-finops-agent/commit/da6310bab23e4a37981b2d6e1e10fecd8354b0f8) - `2026-11-25T14:03:34Z` - Ali Reza Farahnak (@alfarahn)
- [fix: finish custom policy maturity evidence](https://github.com/Azure-Samples/azure-finops-agent/commit/e67db33a81fa075134bcb0ac6369e6f15f201782) - `2026-11-25T13:16:49Z` - Ali Reza Farahnak (@alfarahn)
- [fix: keep AI billing modes mutually exclusive](https://github.com/Azure-Samples/azure-finops-agent/commit/5ba832c450f93928e03e1f7881ecedd2b8cef2a9) - `2026-11-25T12:47:46Z` - Ali Reza Farahnak (@alfarahn)
- [fix: cover the full Copilot usage window](https://github.com/Azure-Samples/azure-finops-agent/commit/d3195fb8db635a03ce6e978208b9be49226adbfc) - `2026-11-25T11:41:44Z` - Ali Reza Farahnak (@alfarahn)

### microsoftgraph/microsoft-graph-docs-contrib (7 commit(s), signal 82)

Tags: `docs, human-authored, product:Microsoft Graph, watchlist`

- [Merge pull request #10108 from microsoftgraph/main639311705481416670s…](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/f725cda6b8c19bacd7aa5a8fb8fa7ed443e16c38) - `2026-11-25T02:29:40Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10108)
- [Merging changes synced from https://github.com/microsoftgraph/microso…](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/c4ee217a09b0e9d03dd499137885b1c2f443dfbc) - `2026-11-25T02:29:02Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10108)
- [Merge pull request #29990 from microsoftgraph/main](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/226dbfca8b7aa861dbb5bdef35a5eab439906d54) - `2026-11-25T02:22:11Z` - Celeste de Guzman (@CelesteDG) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10108)
- [Update MCP server docs for Microsoft MCP Server for IT Admins (#29944)](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/da2c186534d2e83e68c938533d38851a1bed8367) - `2026-11-25T02:07:54Z` - Luca Spolidoro [MSFT] (@Licantrop0) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10108)
- [Merge pull request #10107 from microsoftgraph/main639311640994602993s…](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/1d4570a629cc9a075ba960b4b1152c446fb7a8e5) - `2026-11-25T00:41:59Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10107)

### microsoft/BuildXL (6 commit(s), signal 46)

Tags: `human-authored, samples`

- [Merged PR 978794: Upload BuildXL logs during the build in the Linux i…](https://github.com/microsoft/BuildXL/commit/62a1413ff8c4f6149113cb0e6ec7f2cc306e7262) - `2026-11-25T21:41:23Z` - Viv Siless
- [Merged PR 979119: Dispose lifetime database in updater test](https://github.com/microsoft/BuildXL/commit/68788891558edd0e98f2bcdd302ba753a27a319e) - `2026-11-25T21:04:47Z` - Michael Pysson (@mpysson)
- [Merged PR 979098: Speed up rolling publish with AutoManaged VHD](https://github.com/microsoft/BuildXL/commit/f5d8ab5eca65db63ea820444da2dbd02caa179e0) - `2026-11-25T18:13:12Z` - Michael Pysson (@mpysson)
- [Merged PR 978424: Misc compaction of cache logs](https://github.com/microsoft/BuildXL/commit/e2743bf74b2049db5fffe7577d6dc71f4091dcb7) - `2026-11-25T03:59:08Z` - Michael Pysson (@mpysson)
- [Merged PR 978872: Publish BuildXL packages to the 1ES PT tool feed](https://github.com/microsoft/BuildXL/commit/92a9d517c22aa20c9bb1eb49d73b7682357a43bd) - `2026-11-25T00:42:15Z` - Michael Pysson (@mpysson)

### Azure/homebrew-azd (6 commit(s), signal 91)

Tags: `human-authored, product:Azure SDK, release-language, samples, watchlist`

- [Update for azd release 1.40.0](https://github.com/Azure/homebrew-azd/commit/9f78e1a3f44deb24342f6905bbe43530a7323464) - `2026-11-25T21:35:43Z` - azure-sdk (@azure-sdk)
- [Update for azd release 1.40.0-daily.7114846](https://github.com/Azure/homebrew-azd/commit/8248c88d2e6133ce3cefd7952f14bf0436d98424) - `2026-11-25T20:57:23Z` - azure-sdk (@azure-sdk)
- [Update for azd release 1.40.0-daily.7114842](https://github.com/Azure/homebrew-azd/commit/b48b2b9b81a550f544aec5945dde373c33e3e17e) - `2026-11-25T20:55:22Z` - azure-sdk (@azure-sdk)
- [Update for azd release 1.40.0-daily.7114828](https://github.com/Azure/homebrew-azd/commit/96591e156f6ca8040195a01562e69b6d423b1c47) - `2026-11-25T20:52:29Z` - azure-sdk (@azure-sdk)
- [Update for azd release 1.40.0-daily.7114773](https://github.com/Azure/homebrew-azd/commit/0dc3e7acbc29f7f94813f4391b73a759a26e0440) - `2026-11-25T20:46:20Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/power-automate-docs (6 commit(s), signal 81)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/power-au…](https://github.com/MicrosoftDocs/power-automate-docs/commit/77b4cbcbcc1a061ce30d45521dd698b77fff89cf) - `2026-11-25T19:03:16Z` - Learn Build Service GitHub App
- [Merge pull request #3965 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-automate-docs/commit/8932ae947facd6647d512597a83126ddc64689f8) - `2026-11-25T19:02:12Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Human review required for draft content: Troubleshoot Process Mining …](https://github.com/MicrosoftDocs/power-automate-docs/commit/a3a6aee4702be95ffc1e339af6d775e1a3aae828) - `2026-11-25T14:15:11Z` - Tapan Maniar (@tapanm-MSFT)
- [Merging changes synced from https://github.com/MicrosoftDocs/power-au…](https://github.com/MicrosoftDocs/power-automate-docs/commit/c5ce23df64ee256d9ec0c230eb2e698c5f5407f8) - `2026-11-25T01:03:08Z` - Learn Build Service GitHub App
- [Merge pull request #3963 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-automate-docs/commit/0c12a4a60391278af1278b67dedbd245143a1d6c) - `2026-11-25T01:02:13Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### Azure/azure-sdk-for-python (6 commit(s), signal 131)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [azure-template_1.0.0b7111123](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-template_1.0.0b7111123) - `2026-11-25T05:27:36Z`
- [Sync eng/common for Tools PR 17635 (#50153)](https://github.com/Azure/azure-sdk-for-python/commit/ee37fbf4f13fa9e7606f8d296b48b59215676d63) - `2026-11-25T18:09:42Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17635](https://github.com/Azure/azure-sdk-for-python/pull/50153)
- [[azure-ai-ml] Build endpoint invoke request headers per call (#50147)](https://github.com/Azure/azure-sdk-for-python/commit/28e05754c7809ab066c6f3ac7acc97f82a3c0577) - `2026-11-25T17:42:24Z` - Swarup Chanda (@swarupecenits) - PR: [[azure-ai-ml] Build endpoint invoke request headers per call](https://github.com/Azure/azure-sdk-for-python/pull/50147)
- [Pass manual release-plan IDs as task environment data (#50122)](https://github.com/Azure/azure-sdk-for-python/commit/ae4198e91f21557bc700ceee37807d49fd487261) - `2026-11-25T15:27:42Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17639](https://github.com/Azure/azure-sdk-for-python/pull/50122)
- [[azure-ai-ml] Validate datastore storage account names before creatin…](https://github.com/Azure/azure-sdk-for-python/commit/a75d1b2d04458b4ad2f1ccd100ad411b6d2743d2) - `2026-11-25T10:34:19Z` - Swarup Chanda (@swarupecenits) - PR: [[azure-ai-ml] Validate datastore storage account names before creating storage clients](https://github.com/Azure/azure-sdk-for-python/pull/50129)
- [remove unnecessary sort function that would mask reorder changes in c…](https://github.com/Azure/azure-sdk-for-python/commit/7246059095c9cadcd9df7076c62fb465ef1b3f70) - `2026-11-25T08:38:05Z` - Chenxi Jiang (@ChenxiJiang333) - PR: [remove unnecessary sort function that would mask reorder changes in c…](https://github.com/Azure/azure-sdk-for-python/pull/50135)

### Azure/AI-Landing-Zones (6 commit(s), signal 81)

Tags: `docs, human-authored, watchlist`

- [docs: refresh validated planner prices](https://github.com/Azure/AI-Landing-Zones/commit/3fc681237243d6382f1a7f746a11654481f37c14) - `2026-11-25T15:59:53Z` - github-actions[bot] (@github-actions[bot])
- [Planner: price every public Azure region](https://github.com/Azure/AI-Landing-Zones/commit/ff1c5334c94ca08bb0e384d437f3d4a6c1f3f930) - `2026-11-25T15:54:16Z` - Paulo Lacerda (@placerda)
- [chore: remove automatic issue classification](https://github.com/Azure/AI-Landing-Zones/commit/85ac01cd1afb8c59c9f143acbc61bcd81cc3f1ef) - `2026-11-25T14:57:56Z` - Paulo Lacerda (@placerda)
- [test: cover regional considerations navigation](https://github.com/Azure/AI-Landing-Zones/commit/c6dba3b40585a2615371b35a79b9e013c334dbb4) - `2026-11-25T12:16:15Z` - Paulo Lacerda (@placerda)
- [docs: add regional considerations to planning navigation](https://github.com/Azure/AI-Landing-Zones/commit/1773a7c0190371ff45811edf6a28bb6bd9499253) - `2026-11-25T12:13:20Z` - Paulo Lacerda (@placerda)

### dotnet/msbuild (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Bump agentic workflows to gh-aw v1.4.0 and skip invalid PATs (#15678)](https://github.com/dotnet/msbuild/commit/df20ae8a17fc0b469adfd185fc3016d13ed0b289) - `2026-11-25T14:14:32Z` - Amaury Levé (@Evangelink) - PR: [Bump agentic workflows to gh-aw v1.4.0 and skip invalid PATs](https://github.com/dotnet/msbuild/pull/15678)
- [[main] Update dependencies from dotnet/roslyn (#15643)](https://github.com/dotnet/msbuild/commit/46bf90cec21970b67756a5ece7e2e0c3ffd6cb48) - `2026-11-25T13:57:09Z` - dotnet-maestro[bot] (@dotnet-maestro[bot]) - PR: [[main] Update dependencies from dotnet/roslyn](https://github.com/dotnet/msbuild/pull/15643)
- [Avoid redundant ProjectStarted evaluation payload when telemetry is e…](https://github.com/dotnet/msbuild/commit/386be2a2fa03f94a24891e167beaef11ab892ab2) - `2026-11-25T13:44:52Z` - Aleš Prokop (@AlesProkop) - PR: [Avoid redundant ProjectStarted evaluation payload when telemetry is enabled](https://github.com/dotnet/msbuild/pull/15645)
- [Avoid crashes from orphaned task-host logs (#15622)](https://github.com/dotnet/msbuild/commit/8a26ebcad5ceb5afaceffaed0fe652304d877570) - `2026-11-25T13:44:33Z` - Jan Provazník (@JanProvaznik) - PR: [Avoid crashes from orphaned task-host logs](https://github.com/dotnet/msbuild/pull/15622)
- [Fix undefined OptProf pipeline argument (#15670)](https://github.com/dotnet/msbuild/commit/282975d93fd8a52a70a4438397ea4da99ee38346) - `2026-11-25T13:31:09Z` - Veronika Ovsyannikova (@OvesN) - PR: [Fix undefined OptProf pipeline argument](https://github.com/dotnet/msbuild/pull/15670)

### microsoft/aspire-samples (6 commit(s), signal 0)

Tags: `bot-only, dependency-noise, docs`

- [Bump SkiaSharp from 4.156.1 to 4.157.0 (#2227)](https://github.com/microsoft/aspire-samples/commit/f62aecfa5ec13cab1f22a0900c91c0e2c26974b7) - `2026-11-25T07:34:51Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump SkiaSharp from 4.156.1 to 4.157.0](https://github.com/microsoft/aspire-samples/pull/2227)
- [Bump Scalar.AspNetCore from 3.0.0 to 3.0.1 (#2226)](https://github.com/microsoft/aspire-samples/commit/55775d185880ade15c2c29f68a2e5969dcd1d2ab) - `2026-11-25T07:07:46Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Scalar.AspNetCore from 3.0.0 to 3.0.1](https://github.com/microsoft/aspire-samples/pull/2226)
- [Bump SkiaSharp.NativeAssets.Linux.NoDependencies from 4.154.0 to 4.15…](https://github.com/microsoft/aspire-samples/commit/b96ed52f728b67d99dfeae2448a1311c4c1b7960) - `2026-11-25T07:05:05Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump SkiaSharp.NativeAssets.Linux.NoDependencies from 4.154.0 to 4.157.0](https://github.com/microsoft/aspire-samples/pull/2228)
- [build(deps-dev): Bump the misc-deps group across 1 directory with 3 u…](https://github.com/microsoft/aspire-samples/commit/f9e3a1db44ee021e122f99c1b229f1bcd7bfd0d8) - `2026-11-25T06:50:53Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps-dev): Bump the misc-deps group across 1 directory with 3 updates](https://github.com/microsoft/aspire-samples/pull/2188)
- [build(deps): Bump the misc-deps group (#2223)](https://github.com/microsoft/aspire-samples/commit/142e6bab2b5081cd356f12bccc2ccaf8729ce36e) - `2026-11-25T06:49:39Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): Bump the misc-deps group in /samples/aspire-with-javascript/AspireJavaScript.Vue with 5 updates](https://github.com/microsoft/aspire-samples/pull/2223)

### MicrosoftDocs/msteams-docs (5 commit(s), signal 80)

Tags: `docs, human-authored, product:Microsoft Graph, watchlist`

- [Fix typo and enhance documentation for teams-dev skill (#14779)](https://github.com/MicrosoftDocs/msteams-docs/commit/b5227b91e9c6dc5091ca48e1fda8ea5eb130b10a) - `2026-11-25T21:22:17Z` - Nick Walker (@nickwalkmsft) - PR: [Fix typo and enhance documentation for teams-dev skill](https://github.com/MicrosoftDocs/msteams-docs/pull/14779)
- [Reorganize top-level TOC a bit (#14773)](https://github.com/MicrosoftDocs/msteams-docs/commit/6d9778fa33f3212ed90c22eccf6fbebaabdf94be) - `2026-11-25T00:49:45Z` - Nick Walker (@nickwalkmsft) - PR: [Reorganize top-level TOC a bit](https://github.com/MicrosoftDocs/msteams-docs/pull/14773)
- [Graph and RSC content reorganization (#14772)](https://github.com/MicrosoftDocs/msteams-docs/commit/d6458ce6cd1f558692d594f7d599ba70af7d3356) - `2026-11-24T22:59:15Z` - Nick Walker (@nickwalkmsft) - PR: [Graph and RSC content reorganization](https://github.com/MicrosoftDocs/msteams-docs/pull/14772)
- [Remove deprecation note from documentation (#14771)](https://github.com/MicrosoftDocs/msteams-docs/commit/820e50770eeb31f6527f4d6f93c399abead9b1ca) - `2026-11-24T21:49:50Z` - Nick Walker (@nickwalkmsft) - PR: [Remove deprecation note from documentation](https://github.com/MicrosoftDocs/msteams-docs/pull/14771)
- [Event reference (#14765)](https://github.com/MicrosoftDocs/msteams-docs/commit/c4e924a91db220aa8ec217c6667f888e243f157c) - `2026-11-24T21:22:36Z` - Nick Walker (@nickwalkmsft) - PR: [Event reference](https://github.com/MicrosoftDocs/msteams-docs/pull/14765)

### microsoftgraph/msgraph-snippets-typescript (4 commit(s), signal 19)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #454 from microsoftgraph/dependabot/npm_and_yarn/m…](https://github.com/microsoftgraph/msgraph-snippets-typescript/commit/4fd4101f2a5c99830e1562538a5370139b20a6f8) - `2026-11-25T21:24:41Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump @microsoft/microsoft-graph-client from 3.0.7 to 3.1.0](https://github.com/microsoftgraph/msgraph-snippets-typescript/pull/454)
- [Merge pull request #453 from microsoftgraph/dependabot/npm_and_yarn/p…](https://github.com/microsoftgraph/msgraph-snippets-typescript/commit/0e0bed94d473540d6a32200d9d81ed507ae302d6) - `2026-11-25T21:24:11Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump prettier from 3.10.0 to 3.10.1](https://github.com/microsoftgraph/msgraph-snippets-typescript/pull/453)
- [Bump @microsoft/microsoft-graph-client from 3.0.7 to 3.1.0](https://github.com/microsoftgraph/msgraph-snippets-typescript/commit/640d567e6f294c647657df7187ccc4e19ba702eb) - `2026-11-25T21:23:00Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump @microsoft/microsoft-graph-client from 3.0.7 to 3.1.0](https://github.com/microsoftgraph/msgraph-snippets-typescript/pull/454)
- [Bump prettier from 3.10.0 to 3.10.1](https://github.com/microsoftgraph/msgraph-snippets-typescript/commit/0d87a12aa51ee75be8b2438b1e2272c73f42cd42) - `2026-11-25T21:22:48Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump prettier from 3.10.0 to 3.10.1](https://github.com/microsoftgraph/msgraph-snippets-typescript/pull/453)

### MicrosoftDocs/azure-docs-sdk-java (4 commit(s), signal 79)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/c5af7d052b3d1d410b366cc3415678453c62ac04) - `2026-11-25T20:14:25Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/42ea116af275fd604edc48e6bc2a22218eb5472c) - `2026-11-25T04:08:58Z` - azure-sdk (@azure-sdk)
- [CI Update](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/02854104b8864b7b23580d9f3ec6d82c812a5ccf) - `2026-11-25T01:52:00Z` - docsreference@microsoft.com
- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/18e875939e3577761db7b1fb9603e663530a0308) - `2026-11-24T23:43:20Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/openapi-docs (4 commit(s), signal 79)

Tags: `docs, human-authored, product:Microsoft Graph, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/openapi-…](https://github.com/MicrosoftDocs/openapi-docs/commit/f64f44a00c163023b5c14cf688b5f1e6672bf190) - `2026-11-25T19:03:04Z` - Learn Build Service GitHub App
- [Merge pull request #264 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/openapi-docs/commit/13dc96237e3a208688db35e02d8ea8b564aabb16) - `2026-11-25T19:02:44Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Confirm merge from repo_sync_working_branch to main to sync with http…](https://github.com/MicrosoftDocs/openapi-docs/commit/740fec9aa90db96562cf1fe9c81a47c85012aae6) - `2026-11-25T14:48:16Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [docs(kiota): mark Python request compression as supported (#182)](https://github.com/MicrosoftDocs/openapi-docs/commit/9f1d9f27c6986e2f786372d624ac1cb7454ab83d) - `2026-11-25T14:38:25Z` - Guru R Bharadwaj (@guru-bharadwaj20) - PR: [docs(kiota): mark Python request compression as supported](https://github.com/MicrosoftDocs/openapi-docs/pull/182)

### Azure/azure-sdk-for-java (4 commit(s), signal 119)

Tags: `docs, human-authored, product:Azure SDK, release, watchlist`

- Release: [com.azure+azure-data-appconfiguration_1.13.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-data-appconfiguration_1.13.0-beta.1) - `2026-11-25T19:52:51Z`
- Release: [Spring Cloud Azure 6.6.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/spring-cloud-azure_6.6.0) - `2026-11-25T04:46:34Z`
- Release: [com.azure.spring+spring-messaging-azure_6.6.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.spring%2Bspring-messaging-azure_6.6.0) - `2026-11-25T02:37:26Z`
- [Sync eng/common for Tools PR 17635 (#51419)](https://github.com/Azure/azure-sdk-for-java/commit/198d0b2c3607561f66c7565e78c9f95cef4147ef) - `2026-11-25T18:08:47Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17635](https://github.com/Azure/azure-sdk-for-java/pull/51419)
- [[Spring] Sync Spring Cloud Azure 6.6.0 changelog (#51414)](https://github.com/Azure/azure-sdk-for-java/commit/df8e24095ef832ff82a9454594b4ed44eec0c626) - `2026-11-25T14:32:20Z` - Moary Chen (@moarychan) - PR: [[Spring] Sync Spring Cloud Azure 6.6.0 changelog](https://github.com/Azure/azure-sdk-for-java/pull/51414)
- [[skip ci] [Automation] Generate SDK based on TypeSpec 0.49.2 (#51403)](https://github.com/Azure/azure-sdk-for-java/commit/caa888f2305520b22507d9004eef1261f906f469) - `2026-11-25T01:32:47Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[skip ci] [Automation] Generate SDK based on TypeSpec 0.49.2](https://github.com/Azure/azure-sdk-for-java/pull/51403)
- [[Cosmos Encryption] Encrypt each array element independently for mixe…](https://github.com/Azure/azure-sdk-for-java/commit/f7ec207b3b402819a1b1eaee8416df2588c082a1) - `2026-11-24T23:19:22Z` - Abhijeet Mohanty (@jeet1995) - PR: [[Cosmos Encryption] Encrypt each array element independently for mixed-type arrays](https://github.com/Azure/azure-sdk-for-java/pull/51247)

### microsoft/kiota-authentication-azure-go (4 commit(s), signal 29)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #258 from microsoft/dependabot/github_actions/acti…](https://github.com/microsoft/kiota-authentication-azure-go/commit/460a0eef0c4402674300b1699206735ae92e86d9) - `2026-11-25T17:47:29Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump actions/create-github-app-token from 3.3.0 to 3.4.0](https://github.com/microsoft/kiota-authentication-azure-go/pull/258)
- [Merge pull request #259 from microsoft/dependabot/go_modules/github.c…](https://github.com/microsoft/kiota-authentication-azure-go/commit/2343c1ce3abdae57f1fc327896949246eb8a4b63) - `2026-11-25T17:47:03Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.1 to 1.12.2](https://github.com/microsoft/kiota-authentication-azure-go/pull/259)
- [build(deps): bump github.com/microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-authentication-azure-go/commit/e14a4dbec849d0d10f9ea17b6908791805895d90) - `2026-11-25T17:12:39Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.1 to 1.12.2](https://github.com/microsoft/kiota-authentication-azure-go/pull/259)
- [build(deps): bump actions/create-github-app-token from 3.3.0 to 3.4.0](https://github.com/microsoft/kiota-authentication-azure-go/commit/40556167ac8c3a3223e8ce19559bd0190ce3d4c6) - `2026-11-25T17:12:37Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump actions/create-github-app-token from 3.3.0 to 3.4.0](https://github.com/microsoft/kiota-authentication-azure-go/pull/258)

### dotnet/maui-samples (4 commit(s), signal 54)

Tags: `human-authored, release-language, samples`

- [Anchor version README guidance and keep required CI checks on docs-on…](https://github.com/dotnet/maui-samples/commit/b4cd8d0e0a32bc3d3b6ec1b1b09292a5e791a732) - `2026-11-25T14:41:05Z` - Gerald Versluis (@jfversluis) - PR: [Anchor version README guidance and keep required CI checks on docs-only PRs](https://github.com/dotnet/maui-samples/pull/788)
- [Bump Aspire.Hosting.AppHost from 13.0.0 to 13.6.5 (#784)](https://github.com/dotnet/maui-samples/commit/fc775fb2221e492ba3616871582b86e2dde60cad) - `2026-11-25T14:31:35Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Aspire.Hosting.AppHost from 13.0.0 to 13.6.5](https://github.com/dotnet/maui-samples/pull/784)
- [Simplify .NET 11 sample guidance and remove .NET 9 archive notice (#787)](https://github.com/dotnet/maui-samples/commit/67c02a7048132e6a8a66dbebbc2c1de8b9b06638) - `2026-11-25T14:27:33Z` - Gerald Versluis (@jfversluis) - PR: [Simplify .NET 11 sample guidance and remove .NET 9 archive notice](https://github.com/dotnet/maui-samples/pull/787)
- [Migrate samples to .NET 11 (#786)](https://github.com/dotnet/maui-samples/commit/3281a159e99505143fbb9c933320a97f011c06e3) - `2026-11-25T14:08:21Z` - Gerald Versluis (@jfversluis) - PR: [Migrate samples to .NET 11](https://github.com/dotnet/maui-samples/pull/786)

### MicrosoftDocs/entra-docs (4 commit(s), signal 114)

Tags: `docs, human-authored, release-language, security, watchlist`

- [Merge pull request #15093 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/entra-docs/commit/86a8fe712f8caa727a41bc120c223975a812caba) - `2026-11-25T13:37:30Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Removing the Contentstack provisioning article (#15092)](https://github.com/MicrosoftDocs/entra-docs/commit/4b35dff94d78b0f4999fd40579c443729094f842) - `2026-11-25T08:53:53Z` - Hamsika-45 (@Hamsika-45)
- [Merge pull request #15091 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/entra-docs/commit/6a910dd403830d95ca7e5c3262550ca9af6ba641) - `2026-11-24T23:37:15Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Publish GA docs for Baseline Security Mode app controls (#12114)](https://github.com/MicrosoftDocs/entra-docs/commit/a608d81e20fdc2ca6a6d60fb0314c7a38f69c897) - `2026-11-24T22:31:25Z` - aricrowe57 (@aricrowe57)

### MicrosoftDocs/dynamics365smb-devitpro-pb (4 commit(s), signal 89)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/431eb7e673b6a9581027f64325467b7516fe81d3) - `2026-11-25T13:03:56Z` - Learn Build Service GitHub App
- [Merge pull request #8180 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/48120576c62d02d9d836708230d0cc448b24c7d1) - `2026-11-25T13:03:08Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Docs/660517 eu model guidance (#8178)](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/78a2c03c5f222afd47db6492d07b9453a8243bf9) - `2026-11-25T09:42:02Z` - Susanne Windfeld Pedersen (@SusanneWindfeldPedersen)
- [Note that validation messages can mention another release or country/…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/119361794672d1b8fc6eda1044e7c5d637d8501c) - `2026-11-25T09:36:25Z` - Ihor Handziuk (@IhorHandziuk)

### microsoft/kiota-serialization-text-go (4 commit(s), signal 29)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #199 from microsoft/dependabot/go_modules/github.c…](https://github.com/microsoft/kiota-serialization-text-go/commit/acc04ad6a50aaf78091879f92adfd335e1daa087) - `2026-11-25T10:53:55Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.1 to 1.12.2](https://github.com/microsoft/kiota-serialization-text-go/pull/199)
- [Merge pull request #200 from microsoft/dependabot/github_actions/acti…](https://github.com/microsoft/kiota-serialization-text-go/commit/ffa419867136ab2b634493a3718ab431b6ba058d) - `2026-11-25T10:53:30Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump actions/setup-go from 7.0.0 to 7.1.0](https://github.com/microsoft/kiota-serialization-text-go/pull/200)
- [build(deps): bump actions/setup-go from 7.0.0 to 7.1.0](https://github.com/microsoft/kiota-serialization-text-go/commit/b4f9032932783e5453dcf4f4dd3b4a539491ed94) - `2026-11-25T02:42:38Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump actions/setup-go from 7.0.0 to 7.1.0](https://github.com/microsoft/kiota-serialization-text-go/pull/200)
- [build(deps): bump github.com/microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-serialization-text-go/commit/f1d6dfdba0abc4dc5298676a88cee0d2bb5a77f1) - `2026-11-25T02:42:33Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.1 to 1.12.2](https://github.com/microsoft/kiota-serialization-text-go/pull/199)

### microsoft/kiota-serialization-multipart-go (4 commit(s), signal 29)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #155 from microsoft/dependabot/go_modules/github.c…](https://github.com/microsoft/kiota-serialization-multipart-go/commit/4f8787ee5ab02804d756146cd04883e50bd585da) - `2026-11-25T01:48:01Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.1 to 1.12.2](https://github.com/microsoft/kiota-serialization-multipart-go/pull/155)
- [Merge pull request #156 from microsoft/dependabot/github_actions/acti…](https://github.com/microsoft/kiota-serialization-multipart-go/commit/3f595b44087013a5f36b4960437c1149ea259b53) - `2026-11-25T01:47:41Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump actions/setup-go from 7.0.0 to 7.1.0](https://github.com/microsoft/kiota-serialization-multipart-go/pull/156)
- [build(deps): bump actions/setup-go from 7.0.0 to 7.1.0](https://github.com/microsoft/kiota-serialization-multipart-go/commit/4398140638e99cd851e38263a044184c22081deb) - `2026-11-25T00:42:47Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump actions/setup-go from 7.0.0 to 7.1.0](https://github.com/microsoft/kiota-serialization-multipart-go/pull/156)
- [build(deps): bump github.com/microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-serialization-multipart-go/commit/39764898dd2d2da6114e9c27da6f409422aae7bc) - `2026-11-25T00:42:39Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.1 to 1.12.2](https://github.com/microsoft/kiota-serialization-multipart-go/pull/155)

### Azure/iot-operations-sdks (4 commit(s), signal 129)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [[Rust] mqtt@v1.3.1](https://github.com/Azure/iot-operations-sdks/releases/tag/rust/mqtt/v1.3.1) - `2026-11-25T00:21:06Z`
- [[Rust][MQTT] Version bump 1.3.0 -> 1.3.1 (#1554)](https://github.com/Azure/iot-operations-sdks/commit/c4547807ec77580817629885c054da3730712b96) - `2026-11-25T00:18:10Z` - Carter Tinney (@cartertinney) - PR: [[Rust][MQTT] Version bump 1.3.0 -> 1.3.1](https://github.com/Azure/iot-operations-sdks/pull/1554)
- [[CI][Rust] Add standard 1ES ESRP release pipeline (#1551)](https://github.com/Azure/iot-operations-sdks/commit/ede4e45f2782a20f19d431784b552cb6762f7b75) - `2026-11-25T00:03:40Z` - Carter Tinney (@cartertinney) - PR: [[CI][Rust] Add standard 1ES ESRP release pipeline](https://github.com/Azure/iot-operations-sdks/pull/1551)
- [Bump Rust ms-mqtt-client minimum to 0.1.2 (#1553)](https://github.com/Azure/iot-operations-sdks/commit/d4299d6f15b3be0046f715fe913cb1791b97b31a) - `2026-11-24T23:30:17Z` - Carter Tinney (@cartertinney) - PR: [Bump Rust ms-mqtt-client minimum to 0.1.2](https://github.com/Azure/iot-operations-sdks/pull/1553)
- [[Codegen] Use a single NuGet feed for Dtdl2Wot (#1552)](https://github.com/Azure/iot-operations-sdks/commit/c2f1196c6e7b2ad69bb2c910dee7a19b5ab2daa4) - `2026-11-24T23:13:32Z` - Carter Tinney (@cartertinney) - PR: [[Codegen] Use a single NuGet feed for Dtdl2Wot](https://github.com/Azure/iot-operations-sdks/pull/1552)

### Azure/azure-sdk-for-js (3 commit(s), signal 143)

Tags: `docs, human-authored, product:Azure SDK, release, security, watchlist`

- Release: [@azure/keyvault-keys_4.11.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/keyvault-keys_4.11.0) - `2026-11-25T16:15:53Z`
- [[Identity] Isolate DefaultAzureCredential IMDS probe tests from ambie…](https://github.com/Azure/azure-sdk-for-js/commit/3ae3697e38e48322b780ac569c544c3c1f49e553) - `2026-11-25T19:34:06Z` - Minh-Anh Phan (@minhanh-phan) - PR: [[Identity] Isolate DefaultAzureCredential IMDS probe tests from ambient credential env vars](https://github.com/Azure/azure-sdk-for-js/pull/40901)
- [Sync eng/common directory with azure-sdk-tools for PR 17635 (#40909)](https://github.com/Azure/azure-sdk-for-js/commit/04c12509fc9dce1a9339ace510b5d6524fd3c389) - `2026-11-25T18:08:59Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17635](https://github.com/Azure/azure-sdk-for-js/pull/40909)
- [fix(core-amqp): preserve described body and symbolic property decodin…](https://github.com/Azure/azure-sdk-for-js/commit/25dc8471f493f9eb589e25e997d6e77ceca19d7e) - `2026-11-25T16:57:43Z` - Eldert Grootenboer (@EldertGrootenboer) - PR: [fix(core-amqp): preserve described body and symbolic property decoding](https://github.com/Azure/azure-sdk-for-js/pull/40798)

### microsoft/winget-cli (3 commit(s), signal 118)

Tags: `docs, human-authored, product:PowerShell, release, watchlist`

- Release: [Windows Package Manager 1.30.310](https://github.com/microsoft/winget-cli/releases/tag/v1.30.310) - `2026-11-24T22:13:34Z`
- [Add option to ignore unknown upgrade notices (#6696)](https://github.com/microsoft/winget-cli/commit/86bd3d3dac87cee6a8a119bf0fb5ee1413d9a953) - `2026-11-25T19:13:56Z` - JohnMcPMS (@JohnMcPMS) - PR: [Add option to ignore unknown upgrade notices](https://github.com/microsoft/winget-cli/pull/6696)
- [Additional logging when blocking elevated action (#6708)](https://github.com/microsoft/winget-cli/commit/abcc04f0b8d7203b97172b1edd749c2acf2086ce) - `2026-11-25T19:12:57Z` - JohnMcPMS (@JohnMcPMS) - PR: [Additional logging when blocking elevated action](https://github.com/microsoft/winget-cli/pull/6708)
- [Harden spell-check PR reporting (#6709)](https://github.com/microsoft/winget-cli/commit/16e9164008eb04337243b3dae959185b6412944e) - `2026-11-24T23:27:25Z` - Ruben Guerrero (@msftrubengu) - PR: [Harden spell-check PR reporting](https://github.com/microsoft/winget-cli/pull/6709)

### Azure-Samples/functions-quickstart-python-azd-service-bus (3 commit(s), signal 43)

Tags: `human-authored, samples`

- [Harden Python Service Bus post-provision setup (#4)](https://github.com/Azure-Samples/functions-quickstart-python-azd-service-bus/commit/3b1820399eff82b1135ef1bbb14dc088ec456303) - `2026-11-25T19:01:45Z` - Manvir Kaur (@manvkaur) - PR: [Harden Python Service Bus post-provision setup](https://github.com/Azure-Samples/functions-quickstart-python-azd-service-bus/pull/4)
- [Add post-provision hooks for provision-first workflow (#2)](https://github.com/Azure-Samples/functions-quickstart-python-azd-service-bus/commit/9a8392799d0d6e026124296d5ad4dc561f4a35eb) - `2026-11-25T04:43:29Z` - Glenn Gailey (@ggailey777) - PR: [Add post-provision hooks for provision-first workflow](https://github.com/Azure-Samples/functions-quickstart-python-azd-service-bus/pull/2)
- [Add template descriptor for the Python Service Bus Trigger (#3)](https://github.com/Azure-Samples/functions-quickstart-python-azd-service-bus/commit/eb32c421977cb6416614e6f98513a31c749248cc) - `2026-11-25T04:36:20Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Python Service Bus Trigger](https://github.com/Azure-Samples/functions-quickstart-python-azd-service-bus/pull/3)

### Azure/azure-sdk-for-rust (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Sync eng/common directory with azure-sdk-tools for PR 17635 (#5678)](https://github.com/Azure/azure-sdk-for-rust/commit/24952e0a704e419be3a6970c12328c108435575f) - `2026-11-25T18:09:48Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17635](https://github.com/Azure/azure-sdk-for-rust/pull/5678)
- [Document custom response deserialization (#5674)](https://github.com/Azure/azure-sdk-for-rust/commit/badb2b0e2bfa4c767da3c0e12b5364a28ba22f1b) - `2026-11-25T01:02:29Z` - Heath Stewart (@heaths) - PR: [Document custom response deserialization](https://github.com/Azure/azure-sdk-for-rust/pull/5674)
- [Fix Cosmos live and weekly test failures (#5666)](https://github.com/Azure/azure-sdk-for-rust/commit/bbde01014efdb1f52675195f9e75f6f30608acff) - `2026-11-24T23:31:16Z` - Tomas Varon (@tvaron3) - PR: [Fix Cosmos live and weekly test failures](https://github.com/Azure/azure-sdk-for-rust/pull/5666)

### MicrosoftDocs/azure-dev-docs (3 commit(s), signal 88)

Tags: `docs, human-authored, product:Azure SDK, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-de…](https://github.com/MicrosoftDocs/azure-dev-docs/commit/5164f9e02f35291c8ff30d7abe32a36432da3321) - `2026-11-25T18:04:24Z` - Learn Build Service GitHub App
- [Merge pull request #10029 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-dev-docs/commit/6b0dd2c1be7620517225c4016759ffb204d7f009) - `2026-11-25T18:03:18Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [docs: document released IoT Hub device inspection tools (#10028)](https://github.com/MicrosoftDocs/azure-dev-docs/commit/775d1bf264f723b6f09dff49b1970bd02bffc625) - `2026-11-25T00:26:47Z` - Usha Rathnavel (@Usha-Rathnavel)

### MicrosoftDocs/quantum-docs (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/quantum-…](https://github.com/MicrosoftDocs/quantum-docs/commit/870e0c3c49a4efa3a05590590f5b3d7bb3dc6804) - `2026-11-25T17:02:59Z` - Learn Build Service GitHub App
- [Merge pull request #1721 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/quantum-docs/commit/259119084d8e1cb8d8bc0c220954a012da7dcaf9) - `2026-11-25T17:02:34Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Removed duplicate toc section (#1720)](https://github.com/MicrosoftDocs/quantum-docs/commit/e90b70e6bc596b5021b79684fe3f5533896cf168) - `2026-11-25T16:55:16Z` - Jeremy (@jlehnersd)

### Azure/LogicAppsUX (3 commit(s), signal 128)

Tags: `docs, human-authored, release, release-language, watchlist`

- Release: [Release v5.1025.0](https://github.com/Azure/LogicAppsUX/releases/tag/v5.1025.0) - `2026-11-25T01:43:12Z`
- [feat(designer-v2): add shared monitoring UI, failed-iteration navigat…](https://github.com/Azure/LogicAppsUX/commit/409cf9126378fa6c10b693443e4222036bbf223f) - `2026-11-25T16:46:57Z` - Krrish Mittal (@takyyon) - PR: [feat(designer-v2): add shared monitoring UI, failed-iteration navigation, and built-in glyphs](https://github.com/Azure/LogicAppsUX/pull/9742)
- [feat(ci): add Azure Pipelines npm publisher and Otto release trigger …](https://github.com/Azure/LogicAppsUX/commit/cdc30d4f672c3085e1f8dd320c711c01c2ea10f1) - `2026-11-25T16:46:38Z` - Krrish Mittal (@takyyon) - PR: [feat(ci): add Azure Pipelines npm publisher and Otto release trigger](https://github.com/Azure/LogicAppsUX/pull/9744)
- [fix(ci): migrate MicroBuild pools to VSStable (#9740)](https://github.com/Azure/LogicAppsUX/commit/69acfbf150bc1f432d473a12c549af9bbca4c23f) - `2026-11-25T03:52:43Z` - Brian Lam (@lambrianmsft) - PR: [fix(ci): migrate MicroBuild pools to VSStable](https://github.com/Azure/LogicAppsUX/pull/9740)

### MicrosoftDocs/azure-docs-sdk-node (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/7a5fc5eb272b80392b2afde877f501b12aa2c7a1) - `2026-11-25T16:34:07Z` - azure-sdk (@azure-sdk)
- [CI Update](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/cb1695561990de92eb9cbe3cef87fc9d45bfa0a0) - `2026-11-25T01:37:49Z` - docsreference@microsoft.com
- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/48a212144b11214bb5538a9a39091b9a9580531b) - `2026-11-24T23:07:13Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/dynamics-365-contact-center (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/5ab6dcde705a14cb7a3c8bb8efbf9513ce3de024) - `2026-11-25T07:03:06Z` - Learn Build Service GitHub App
- [Merge pull request #853 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/fe6aab81add2c6389c1d3290302d6b8fead55b71) - `2026-11-25T07:02:44Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update Customer Intent Agent content (#851)](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/139aa85ac9a73ff06397fe37a412ad4b04a83e30) - `2026-11-25T04:46:44Z` - Neeraja Nellimarla (@neeranelli)

### MicrosoftDocs/microsoft-salescopilot-docs (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/viva-doc…](https://github.com/MicrosoftDocs/microsoft-salescopilot-docs/commit/81fd8ae3d2a9d730a74635711044e0fbe4ea76b9) - `2026-11-25T07:02:54Z` - Learn Build Service GitHub App
- [Merge pull request #620 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/microsoft-salescopilot-docs/commit/7778968b8847df39809dc015d05312d47c367e37) - `2026-11-25T07:02:32Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [CRM Notes, Feedback, and Dictation](https://github.com/MicrosoftDocs/microsoft-salescopilot-docs/commit/300c5dd76833fab17ec1c7ddaf4b1f9945f4c000) - `2026-11-25T06:31:50Z` - katielegan (@katielegan)

### Azure/azure-cli-extensions (3 commit(s), signal 128)

Tags: `docs, human-authored, release, release-language, watchlist`

- Release: [horizondb 1.0.0b12](https://github.com/Azure/azure-cli-extensions/releases/tag/horizondb-1.0.0b12) - `2026-11-25T06:51:17Z`
- [[Release] Update index.json for extension [ horizondb-1.0.0b12 ]](https://github.com/Azure/azure-cli-extensions/commit/495db6355c28323c02f06467632f404e4327c69c) - `2026-11-25T06:50:17Z` - Azure CLI Team (@azclibot)
- [{HORIZONDB} Add default parameter-group commands (#10604)](https://github.com/Azure/azure-cli-extensions/commit/a537a5ee5d42a04bac0bdf124ea268d9dc17319a) - `2026-11-25T06:34:57Z` - Alex Hughes (@alxhghs) - PR: [{HORIZONDB} Add default parameter-group commands](https://github.com/Azure/azure-cli-extensions/pull/10604)
- [feat: add MacOS support to confcom (#10380)](https://github.com/Azure/azure-cli-extensions/commit/33750f3603515808c9e7e71cbb828d1d9aea1d11) - `2026-11-25T06:30:51Z` - Adam Short (@ashort96) - PR: [feat: add MacOS support to confcom](https://github.com/Azure/azure-cli-extensions/pull/10380)

### MicrosoftDocs/powerapps-docs (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/powerapp…](https://github.com/MicrosoftDocs/powerapps-docs/commit/4ec882a5398dd3027eb5a527cc039f6e6f7c95b9) - `2026-11-25T01:06:28Z` - Learn Build Service GitHub App
- [Merge pull request #12929 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/powerapps-docs/commit/7e67c2ef839edae17283c48edc77ad345770c097) - `2026-11-25T01:03:58Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update Power Apps code app data and automation guidance (#12926)](https://github.com/MicrosoftDocs/powerapps-docs/commit/df81ce958ad5a9bfac403fed73c95c63baa27569) - `2026-11-24T21:46:32Z` - ergonza93 (@ergonza93)

### MicrosoftDocs/learn (3 commit(s), signal 88)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/2f79da37c81f6a4446414b461ba046c4abaf81b5) - `2026-11-24T23:21:10Z` - Learn Build Service GitHub App
- [Merge pull request #56949 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/learn/commit/316acba4b40ff8bda1dfcd5f445d2f067c73b621) - `2026-11-24T23:10:58Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [First draft of module in my fork of release branch (#56943) (#56948)](https://github.com/MicrosoftDocs/learn/commit/eae82ad2ed9e73e00880fc49e3f1467ed863dca5) - `2026-11-24T21:18:23Z` - Orin Thomas (@Orin-Thomas)

### Azure-Samples/functions-quickstart-typescript-azd-service-bus (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Fix role assignments and preserve local settings in post-provision ho…](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-service-bus/commit/c2094a6f98424261ca5d6003e23541ae81ea9d5d) - `2026-11-25T19:28:48Z` - Manvir Kaur (@manvkaur) - PR: [Fix role assignments and preserve local settings in post-provision hooks](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-service-bus/pull/4)
- [Add post-provision hooks for provision-first workflow (#5)](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-service-bus/commit/eff2966ae154f91945880d940b98e0946fd73d91) - `2026-11-25T05:01:02Z` - Glenn Gailey (@ggailey777) - PR: [Add post-provision hooks for provision-first workflow](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-service-bus/pull/5)

### Azure-Samples/functions-quickstart-javascript-azd-service-bus (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Fix Service Bus provisioning and local settings (#2)](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-service-bus/commit/ed1ba444891abc613802bf5af0713dc44225c486) - `2026-11-25T19:28:08Z` - Manvir Kaur (@manvkaur) - PR: [Fix Service Bus provisioning and local settings](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-service-bus/pull/2)
- [Add post-provision hooks for provision-first workflow (#1)](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-service-bus/commit/17886aed0362a1af0c4967fbd1b52445bf5e076d) - `2026-11-25T05:00:38Z` - Glenn Gailey (@ggailey777) - PR: [Add post-provision hooks for provision-first workflow](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-service-bus/pull/1)

### Azure-Samples/functions-connectors-net (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Add Learn sample metadata (#24)](https://github.com/Azure-Samples/functions-connectors-net/commit/8ab3a3b4ee8dae122bc2d16ea43e91708dd706fd) - `2026-11-25T18:59:44Z` - Manvir Kaur (@manvkaur) - PR: [Add Learn metadata to connector samples](https://github.com/Azure-Samples/functions-connectors-net/pull/24)
- [Add template descriptor for the .NET Polling Connectors QuickStart (#23)](https://github.com/Azure-Samples/functions-connectors-net/commit/ff26a7ca6c7d3551f7bb489d6150661282d71265) - `2026-11-24T21:49:55Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the .NET Polling Connectors QuickStart](https://github.com/Azure-Samples/functions-connectors-net/pull/23)

### MicrosoftDocs/azure-docs-sdk-python (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/3a90cb3a24c00abd69e9ffd12a94298779128eb8) - `2026-11-25T18:35:07Z` - azure-sdk (@azure-sdk)
- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/fd1801a706535034665d4281ef834c4db80da85c) - `2026-11-24T23:08:54Z` - azure-sdk (@azure-sdk)

### MicrosoftLearning/mslearn-github-labs (2 commit(s), signal 77)

Tags: `human-authored, training, watchlist`

- [updating Getting Started with GH Ent auth guidelines](https://github.com/MicrosoftLearning/mslearn-github-labs/commit/a8345320353773fc8cb6773c2938845bcfcaeea2) - `2026-11-25T18:33:04Z` - Peter De Tender (@petender)
- [update accelerate with button to launch exercise + lab link](https://github.com/MicrosoftLearning/mslearn-github-labs/commit/4866c3040e2ca5eebe8c714ced89c670aab729c8) - `2026-11-25T00:50:19Z` - Peter De Tender (@petender)

### microsoft/kiota-python (2 commit(s), signal 27)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #917 from microsoft/dependabot/github_actions/acti…](https://github.com/microsoft/kiota-python/commit/b9e17135172705d8a0c72ad5401662928c6eb1cf) - `2026-11-25T17:48:44Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(deps): bump actions/create-github-app-token from 3.3.0 to 3.4.0](https://github.com/microsoft/kiota-python/pull/917)
- [chore(deps): bump actions/create-github-app-token from 3.3.0 to 3.4.0](https://github.com/microsoft/kiota-python/commit/ce803ea0540d407784bba3d2e9e32f3284c03507) - `2026-11-25T16:28:06Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump actions/create-github-app-token from 3.3.0 to 3.4.0](https://github.com/microsoft/kiota-python/pull/917)

### dotnet/docs-desktop (2 commit(s), signal 42)

Tags: `docs, human-authored`

- [Remove all file-level invalid author metadata (#2308)](https://github.com/dotnet/docs-desktop/commit/39beab5382244d8c21065d910b5e6c52bf8d3292) - `2026-11-25T14:28:45Z` - Genevieve Warren (@gewarren) - PR: [Remove all file-level invalid author metadata](https://github.com/dotnet/docs-desktop/pull/2308)
- [DocFX-only split of dotnet/docs-desktop#2297 for row sheet_001:939 (#…](https://github.com/dotnet/docs-desktop/commit/9e59f69efb23c2712956727b05fd877a1001f89a) - `2026-11-24T21:49:28Z` - Dina Berry (MSFT) (@diberry) - PR: [2026-11-23T13-13-55 DO NOT MERGE - Knowledge Partnership - DocFX-only split of #2297 \| dotnet-desktop \| dotnet-desktop-guide \| docfx \| billwagner](https://github.com/dotnet/docs-desktop/pull/2307)

### microsoft/kiota-serialization-json-go (2 commit(s), signal 27)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #243 from microsoft/dependabot/go_modules/github.c…](https://github.com/microsoft/kiota-serialization-json-go/commit/1533a288b0046d4b8a0af868e574ad12f99f6218) - `2026-11-25T10:54:15Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.1 to 1.12.2](https://github.com/microsoft/kiota-serialization-json-go/pull/243)
- [build(deps): bump github.com/microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-serialization-json-go/commit/0b52dc116ef5ef29f8264402912f0356e47350fa) - `2026-11-25T06:42:33Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.1 to 1.12.2](https://github.com/microsoft/kiota-serialization-json-go/pull/243)

### microsoft/kiota-http-go (2 commit(s), signal 27)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #319 from microsoft/dependabot/go_modules/github.c…](https://github.com/microsoft/kiota-http-go/commit/b267d667c7a06d0782bc2fbdd0b2171b28c28a82) - `2026-11-25T10:52:32Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.1 to 1.12.2](https://github.com/microsoft/kiota-http-go/pull/319)
- [chore(deps): bump github.com/microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-http-go/commit/c9a79a4bf468a020d1a368f3a6b11722ba984f87) - `2026-11-25T09:12:36Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.1 to 1.12.2](https://github.com/microsoft/kiota-http-go/pull/319)

### microsoft/fabric-toolbox (2 commit(s), signal 77)

Tags: `human-authored, product:PowerShell, samples, watchlist`

- [Merge pull request #742 from SrdjanMatin/refine-scalar-udf-lab10](https://github.com/microsoft/fabric-toolbox/commit/5ff1166b7bf4c7930a338fdd859f04c68996366a) - `2026-11-25T10:23:09Z` - Mark Pryce-Maher (@MarkPryceMaherMSFT) - PR: [Clarify Scalar UDF Lab 10 reply-generation guidance](https://github.com/microsoft/fabric-toolbox/pull/742)
- [Docs: Clarify Lab 10 reply-generation guidance](https://github.com/microsoft/fabric-toolbox/commit/1b8ff836dbfa649ab4cbe486ee9a12a316ba9c03) - `2026-11-25T09:05:56Z` - Srdjan Matin (@SrdjanMatin) - PR: [Clarify Scalar UDF Lab 10 reply-generation guidance](https://github.com/microsoft/fabric-toolbox/pull/742)

### Azure-Samples/modernize-bootcamp (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Merge pull request #106 from Azure-Samples/sumit/modify-sql-hyperscale](https://github.com/Azure-Samples/modernize-bootcamp/commit/40ff077770d6c04b78aaa9677cd4aac1a3b93174) - `2026-11-25T03:06:04Z` - Sumit Sengupta (@sumitsengupta) - PR: [Take out MI, add Hyperscale, incomplete still.. need to finish DMS mi…](https://github.com/Azure-Samples/modernize-bootcamp/pull/106)
- [Take out MI, add Hyperscale, incomplete still.. need to finish DMS mi…](https://github.com/Azure-Samples/modernize-bootcamp/commit/47fd68919f698cb57043d4905ce3db5edf5b0155) - `2026-11-24T22:58:21Z` - sumitdatabase (@sumitdatabase) - PR: [Take out MI, add Hyperscale, incomplete still.. need to finish DMS mi…](https://github.com/Azure-Samples/modernize-bootcamp/pull/106)

### Azure/azure-functions-openai-extension (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Add OpenAI extension deprecation notices (#237)](https://github.com/Azure/azure-functions-openai-extension/commit/7a7ffa1d8193966d3bf8340f102e24d6337b2e85) - `2026-11-25T02:19:08Z` - Manvir Kaur (@manvkaur) - PR: [Add OpenAI extension deprecation notices](https://github.com/Azure/azure-functions-openai-extension/pull/237)
- [Maintenance updates (#236)](https://github.com/Azure/azure-functions-openai-extension/commit/4530b99a88f5860afcec2160a9dedb3e6677f1cd) - `2026-11-24T23:05:17Z` - Manvir Kaur (@manvkaur) - PR: [Maintenance updates](https://github.com/Azure/azure-functions-openai-extension/pull/236)

### MicrosoftDocs/azure-docs-sdk-dotnet (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [CI Update](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/93516ed8ba21f98ce9ee1436f2fde7966903c445) - `2026-11-25T02:18:38Z` - docsreference@microsoft.com
- [Update docs CI configuration](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/cc245b62a470693ee0ecf145635e182efccf2d6c) - `2026-11-24T23:53:31Z` - azure-sdk (@azure-sdk)

### microsoft/kiota-ruby (2 commit(s), signal 27)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #228 from microsoft/dependabot/github_actions/ruby…](https://github.com/microsoft/kiota-ruby/commit/d61b4a4ee16c4a735ee0e4fa34d37251721fcf6b) - `2026-11-25T01:47:21Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump ruby/setup-ruby from 1.338.0 to 1.339.0](https://github.com/microsoft/kiota-ruby/pull/228)
- [build(deps): bump ruby/setup-ruby from 1.338.0 to 1.339.0](https://github.com/microsoft/kiota-ruby/commit/2a7d74014980412ed887eac317c923ed0755eecb) - `2026-11-25T00:03:32Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump ruby/setup-ruby from 1.338.0 to 1.339.0](https://github.com/microsoft/kiota-ruby/pull/228)

### Azure-Samples/Spec2Cloud (2 commit(s), signal 0)

Tags: `bot-only, samples`

- [Update templates.json [automated]](https://github.com/Azure-Samples/Spec2Cloud/commit/9f94f9c5043224480ac0832e0b9c13125a2156ed) - `2026-11-25T01:05:19Z` - github-actions[bot] (@github-actions[bot])
- [Update templates.json [automated]](https://github.com/Azure-Samples/Spec2Cloud/commit/e4700ba2fc797969b50ff61a93be751e6a4892e5) - `2026-11-25T00:14:14Z` - github-actions[bot] (@github-actions[bot])

### dotnet/eShop (2 commit(s), signal 42)

Tags: `docs, human-authored`

- [Gate pull requests on a single verify check (#1124)](https://github.com/dotnet/eShop/commit/3c6e531a6063676ece317644f72172fb42a935b3) - `2026-11-24T23:49:20Z` - Damian Edwards (@DamianEdwards) - PR: [Gate pull requests on a single verify check](https://github.com/dotnet/eShop/pull/1124)
- [Update EF Core and Npgsql to 11.0.0 and consolidate Dependabot groups…](https://github.com/dotnet/eShop/commit/31105c937eba91e4850b5a6059c38d51152fa22c) - `2026-11-24T23:16:18Z` - dependabot[bot] (@dependabot[bot]) - PR: [Update EF Core and Npgsql to 11.0.0 and consolidate Dependabot groups](https://github.com/dotnet/eShop/pull/1115)

### microsoft/amplifier-module-loop-streaming (2 commit(s), signal 42)

Tags: `docs, human-authored`

- [Allow an ordinary reply while a compatible paid checkpoint finishes (…](https://github.com/microsoft/amplifier-module-loop-streaming/commit/594d63eb38cf9dadc7bee1930d25178db4199250) - `2026-11-24T21:42:45Z` - Brian Krabach (@bkrabach) - PR: [Allow an ordinary reply while a compatible paid checkpoint finishes](https://github.com/microsoft/amplifier-module-loop-streaming/pull/82)
- [Schedule bounded context maintenance after a confirmed ordinary reply…](https://github.com/microsoft/amplifier-module-loop-streaming/commit/b484f1b89b393625eca6bdd57a1c812697b6a627) - `2026-11-24T21:15:26Z` - Brian Krabach (@bkrabach) - PR: [Schedule bounded context maintenance after a confirmed ordinary reply](https://github.com/microsoft/amplifier-module-loop-streaming/pull/81)

### Azure/setup-azd (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, samples, watchlist`

- [Bump the "all-dependencies" group with 1 update across multiple ecosy…](https://github.com/Azure/setup-azd/commit/de4e2ea05dcd7632c6c576f3738eab4a4a1800c5) - `2026-11-25T21:57:25Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the "all-dependencies" group with 1 update across multiple ecosystems](https://github.com/Azure/setup-azd/pull/655)

### Azure/awesome-azd (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure AI, product:Microsoft Graph, watchlist`

- [Align LangChain agent catalog metadata (#1131)](https://github.com/Azure/awesome-azd/commit/3d4b64197da5475791da39e0fac81630399d3a31) - `2026-11-25T21:43:07Z` - Junjie Li (@MuyangAmigo) - PR: [Align LangChain/LangGraph agent catalog metadata](https://github.com/Azure/awesome-azd/pull/1131)

### microsoft/AzureTRE (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Fix the Health workspace service and add a private Health test (#5296)](https://github.com/microsoft/AzureTRE/commit/ac7d1f483bd401608ffdd1acdbab6007587e90e4) - `2026-11-25T21:08:03Z` - Jay W (@JayDoubleu) - PR: [Fix the Health workspace service and add a private Health test](https://github.com/microsoft/AzureTRE/pull/5296)

### OfficeDev/microsoft-teams-library-js (1 commit(s), signal 86)

Tags: `docs, human-authored, release-language, watchlist`

- [Run the ESRP npm publish on Node 20 with EsrpRelease@13 (#3225)](https://github.com/OfficeDev/microsoft-teams-library-js/commit/1b31d64afc2845c50fe7aa0e32043fdbe0f2a2d9) - `2026-11-25T21:07:06Z` - Patrick Latter (@palatter) - PR: [Run the ESRP npm publish on Node 20 with EsrpRelease@13](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3225)

### microsoft/WindowsAppSDK (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Use template-time ARM64 CodeQL gating (#7000)](https://github.com/microsoft/WindowsAppSDK/commit/8ef9764c0c0d154e10482e4bca3f1a66abec011c) - `2026-11-25T19:33:42Z` - Kyaw Thant (@kythant) - PR: [Use template-time ARM64 CodeQL gating](https://github.com/microsoft/WindowsAppSDK/pull/7000)

### Azure-Samples/functions-quickstart-java-azd-service-bus (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add post-provision hooks for provision-first workflow (#2)](https://github.com/Azure-Samples/functions-quickstart-java-azd-service-bus/commit/08159b4021ac31535d0b7072f4d4626f07205ea2) - `2026-11-25T19:14:45Z` - Glenn Gailey (@ggailey777) - PR: [Add post-provision hooks for provision-first workflow](https://github.com/Azure-Samples/functions-quickstart-java-azd-service-bus/pull/2)

### Azure-Samples/functions-quickstart-python-azd-eventhub (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Fix VNet integration for Python Event Hubs sample (#3)](https://github.com/Azure-Samples/functions-quickstart-python-azd-eventhub/commit/34116eb854ba42a70d3e10b9dca1ceaaaf75a4a2) - `2026-11-25T19:00:30Z` - Manvir Kaur (@manvkaur) - PR: [Fix VNet integration for Python Event Hubs sample](https://github.com/Azure-Samples/functions-quickstart-python-azd-eventhub/pull/3)

### Azure/azure-sdk-for-go (1 commit(s), signal 26)

Tags: `bot-only, docs, product:Azure SDK, watchlist`

- [Sync eng/common for Tools PR 17635 (#28130)](https://github.com/Azure/azure-sdk-for-go/commit/4686f33f63ff0a65b0c454f2f7d3360ab069da2f) - `2026-11-25T18:08:36Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17635](https://github.com/Azure/azure-sdk-for-go/pull/28130)

### Azure/azure-sdk-for-cpp (1 commit(s), signal 26)

Tags: `bot-only, docs, product:Azure SDK, watchlist`

- [Sync eng/common for Tools PR 17635 (#7576)](https://github.com/Azure/azure-sdk-for-cpp/commit/d7a1be1c4a8708bca6cdb3bc3368e11b1f9b9a51) - `2026-11-25T18:08:24Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17635](https://github.com/Azure/azure-sdk-for-cpp/pull/7576)

### Azure/data-api-builder (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [feat: add UTC timestamps to all console log entries (#3709)](https://github.com/Azure/data-api-builder/commit/9a89b29b2b556c71a3fac15c553590d642b334fd) - `2026-11-25T17:28:39Z` - Copilot (@Copilot) - PR: [feat: add UTC timestamps to all console log entries](https://github.com/Azure/data-api-builder/pull/3709)

### microsoft/kiota-typescript (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [auto dependabot: bump the vitest group with 4 updates (#2241)](https://github.com/microsoft/kiota-typescript/commit/b18bad5be3d726f62c9cc081eaf695c6545a961c) - `2026-11-25T14:36:50Z` - dependabot[bot] (@dependabot[bot]) - PR: [auto dependabot: bump the vitest group with 4 updates](https://github.com/microsoft/kiota-typescript/pull/2241)

### Azure-Samples/ms-identity-ciam-native-javascript-samples (1 commit(s), signal 76)

Tags: `human-authored, product:Azure SDK, samples, watchlist`

- [Align Native Auth existing-account sign-up, social callbacks, and HAL…](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/commit/a3a4b87c38ea51a3902ab8d9133efc1652846fd3) - `2026-11-25T14:17:06Z` - Yongdi Wang (@yongdiw) - PR: [Align Native Auth existing-account sign-up, social callbacks, and HAL proxies](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/pull/72)

### dotnet/blazor-samples (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Validate return URLs in Blazor samples (#693)](https://github.com/dotnet/blazor-samples/commit/5840dd8c03b7eb5ef6a0ab00933524fda3402fa1) - `2026-11-25T14:11:56Z` - Ondřej Roztočil (@oroztocil) - PR: [Validate return URLs in Blazor samples](https://github.com/dotnet/blazor-samples/pull/693)

### microsoft/voice-agent (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Add membership, delivery, and pharmacy single-agent samples (examples…](https://github.com/microsoft/voice-agent/commit/12ea92547a9bfaafe82aac3c5927532ff4fe7a58) - `2026-11-25T13:22:11Z` - uchihaqyf-bot (@uchihaqyf-bot) - PR: [Add membership, delivery, and pharmacy single-agent samples (examples 46-48)](https://github.com/microsoft/voice-agent/pull/155)

### Azure/terraform-azurerm-avm-ptn-commercial-marketplace (1 commit(s), signal 26)

Tags: `bot-only, samples, watchlist`

- [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-ptn-commercial-marketplace/commit/0b356013d26c32c447b0ca2d73a442e411656df4) - `2026-11-25T13:11:29Z` - azure-verified-modules[bot] (@azure-verified-modules[bot]) - PR: [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-ptn-commercial-marketplace/pull/76)

### Azure/terraform-azurerm-avm-ptn-aca-lza-hosting-environment (1 commit(s), signal 26)

Tags: `bot-only, samples, watchlist`

- [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-ptn-aca-lza-hosting-environment/commit/314a2a3e3b6b27b09f9f9803f4e749d573e31b5d) - `2026-11-25T12:53:31Z` - azure-verified-modules[bot] (@azure-verified-modules[bot]) - PR: [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-ptn-aca-lza-hosting-environment/pull/118)

### MicrosoftDocs/azure-docs-cli (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [CI Update](https://github.com/MicrosoftDocs/azure-docs-cli/commit/9e8e728b44905a0f38dc852dacc2eca9a7fed9dd) - `2026-11-25T12:49:54Z` - docsreference@microsoft.com

### microsoft/amplifier-module-provider-openai (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Discover the OpenAI Decisions catalog without importing the provider …](https://github.com/microsoft/amplifier-module-provider-openai/commit/903b37c05d0ac1214dc801ba02d9af07986e06d2) - `2026-11-25T12:46:55Z` - Brian Krabach (@bkrabach) - PR: [Discover the OpenAI Decisions catalog without importing the provider runtime](https://github.com/microsoft/amplifier-module-provider-openai/pull/164)

### microsoft/finops-toolkit (1 commit(s), signal 76)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [docs(powershell): Generate PowerShell docs from code (#935)](https://github.com/microsoft/finops-toolkit/commit/64aace063a7fe1befbd4b6a245068f0e6efa6f5f) - `2026-11-25T12:04:50Z` - Michael Flanakin (@flanakin) - PR: [docs(powershell): Generate PowerShell docs from code](https://github.com/microsoft/finops-toolkit/pull/935)

### microsoft/Multi-Agent-Custom-Automation-Engine-Solution-Accelerator (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merge pull request #1190 from microsoft/dev](https://github.com/microsoft/Multi-Agent-Custom-Automation-Engine-Solution-Accelerator/commit/d5d6cc834b5e7de7dc175a53c93d627c6875c04d) - `2026-11-25T12:01:59Z` - Prajwal-Microsoft (@Prajwal-Microsoft) - PR: [feat: merging the changes from dev to main](https://github.com/microsoft/Multi-Agent-Custom-Automation-Engine-Solution-Accelerator/pull/1190)

### Azure-Samples/copilot-openai-todo (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [chore: refresh workspace dependencies and Node runtime (#2)](https://github.com/Azure-Samples/copilot-openai-todo/commit/ddd1bf49ab94d348fc84d1d63daa6b924117070f) - `2026-11-25T11:51:04Z` - Yohan Lasorsa (@sinedied) - PR: [Refresh Todo app dependencies and move to Node.js 24 LTS](https://github.com/Azure-Samples/copilot-openai-todo/pull/2)

### Azure/terraform-azurerm-avm-res-devtestlab-lab (1 commit(s), signal 26)

Tags: `bot-only, training, watchlist`

- [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-res-devtestlab-lab/commit/86c81cb69dced494f8a9fe8274378503224133e3) - `2026-11-25T09:41:50Z` - azure-verified-modules[bot] (@azure-verified-modules[bot]) - PR: [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-res-devtestlab-lab/pull/92)

### dotnet/EntityFramework.Docs (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Updated some extensions to add support for EF Core 11 (#5545)](https://github.com/dotnet/EntityFramework.Docs/commit/2e943ce2b1e5ac26e24adde04827d22f2fe7885d) - `2026-11-25T07:59:41Z` - Jonathan Magnan (@JonathanMagnan) - PR: [Update index.md](https://github.com/dotnet/EntityFramework.Docs/pull/5545)

### Azure/azure-devops-cli-extension (1 commit(s), signal 86)

Tags: `docs, human-authored, release-language, watchlist`

- [Post-Release-1.0.12 (#1546)](https://github.com/Azure/azure-devops-cli-extension/commit/1c71d5a0985da33437c033527631a956f1a58f4c) - `2026-11-25T06:56:31Z` - mishrarish (@mishrarish) - PR: [Post-Release-1.0.12](https://github.com/Azure/azure-devops-cli-extension/pull/1546)

### aspnet/AzureSignalR-samples (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Update Azure Functions samples dependencies, runtimes, and READMEs (#…](https://github.com/aspnet/AzureSignalR-samples/commit/7ed635b7322ec1b8728fea8f3442df51a3e1a736) - `2026-11-25T04:57:47Z` - yzt (@Y-Sindo) - PR: [Update Azure Functions samples dependencies, runtimes, and READMEs](https://github.com/aspnet/AzureSignalR-samples/pull/387)

### OfficeDev/office-js-docs-pr (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [[Outlook] Resolve known issues (#5934)](https://github.com/OfficeDev/office-js-docs-pr/commit/36410dfecdcd33f6a5c654ca32f45e2b3545aed1) - `2026-11-25T00:39:14Z` - Sam Ramon (@samantharamon) - PR: [[Outlook] Resolve known issues](https://github.com/OfficeDev/office-js-docs-pr/pull/5934)

### microsoft/mcp-dotnet-samples (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Update metadata.json](https://github.com/microsoft/mcp-dotnet-samples/commit/c87e649bce212adc7ebb30b6db60e2e858c1e7cd) - `2026-11-25T00:25:34Z` - GitHub Actions (@actions-user)

### dotnet/dotnet-api-docs (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Include warning about write-only spans (#13380)](https://github.com/dotnet/dotnet-api-docs/commit/3bf2effe9fd862fa426d6edcc5e98533956e99be) - `2026-11-24T23:47:36Z` - Levi Broderick (@GrabYourPitchforks) - PR: [Include warning about write-only spans](https://github.com/dotnet/dotnet-api-docs/pull/13380)

### MicrosoftDocs/azure-docs-sdk-cpp (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-cpp/commit/44ee4463ca476727105e515510fa5acb092f29ee) - `2026-11-24T23:21:44Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/azure-compute-docs (1 commit(s), signal 26)

Tags: `bot-only, docs, watchlist`

- [Merge pull request #4442 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-compute-docs/commit/eaee6dbdfc7a50d0918d45fc52e9d1ec0c5510fb) - `2026-11-24T23:02:32Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### MicrosoftDocs/office-docs-powershell (1 commit(s), signal 76)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Fix parameter name in Set-EventsFromEmailConfiguration example (#13839)](https://github.com/MicrosoftDocs/office-docs-powershell/commit/da3e1791c795db8048ad002c11701db7f825372c) - `2026-11-24T22:57:14Z` - 𝙰𝚕𝚎𝚓𝚊𝚗𝚍𝚛𝚘 𝙰𝚗𝚍𝚛𝚎𝚞 (@4leX-42) - PR: [Set-EventsFromEmailConfiguration: fix -InvoiceProgressingLevel typo in example](https://github.com/MicrosoftDocs/office-docs-powershell/pull/13839)

### Azure-Samples/functions-quickstart-go-azd-eventhub (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the Go Event Hubs Trigger (#4)](https://github.com/Azure-Samples/functions-quickstart-go-azd-eventhub/commit/ff1357db3da45f8e1c868a2fa8ae02813b32a120) - `2026-11-24T22:52:37Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Go Event Hubs Trigger](https://github.com/Azure-Samples/functions-quickstart-go-azd-eventhub/pull/4)

### Azure-Samples/functions-quickstart-go-azd-sql (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the Go SQL Trigger (#4)](https://github.com/Azure-Samples/functions-quickstart-go-azd-sql/commit/db3186527471bddfc1859c44a94dfc3ae7c58a27) - `2026-11-24T22:52:36Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Go SQL Trigger](https://github.com/Azure-Samples/functions-quickstart-go-azd-sql/pull/4)

### Azure-Samples/functions-quickstart-go-azd-service-bus (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the Go Service Bus Trigger (#4)](https://github.com/Azure-Samples/functions-quickstart-go-azd-service-bus/commit/90324b330958361e414aacea659062a5c8157436) - `2026-11-24T22:52:36Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Go Service Bus Trigger](https://github.com/Azure-Samples/functions-quickstart-go-azd-service-bus/pull/4)

### Azure-Samples/functions-quickstart-go-azd-eventgrid-blob (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the Go Event Grid Blob Trigger (#5)](https://github.com/Azure-Samples/functions-quickstart-go-azd-eventgrid-blob/commit/efab3087139d1a6053e7cbc511650587fd1e9bf2) - `2026-11-24T22:52:36Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Go Event Grid Blob Trigger](https://github.com/Azure-Samples/functions-quickstart-go-azd-eventgrid-blob/pull/5)

### Azure-Samples/functions-quickstart-go-azd-timer (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the Go Timer Trigger (#8)](https://github.com/Azure-Samples/functions-quickstart-go-azd-timer/commit/7a805d4fa89372d9b6fe65313ec70b2e60d77166) - `2026-11-24T22:52:36Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Go Timer Trigger](https://github.com/Azure-Samples/functions-quickstart-go-azd-timer/pull/8)

### Azure-Samples/durable-functions-order-processing-go (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the Go Durable Functions Order Processing…](https://github.com/Azure-Samples/durable-functions-order-processing-go/commit/83877e6c1fe3dd3fa35f30da9f33084e576c6005) - `2026-11-24T22:52:36Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Go Durable Functions Order Processing](https://github.com/Azure-Samples/durable-functions-order-processing-go/pull/4)

### Azure-Samples/durable-functions-quickstart-typescript-azd (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the TypeScript Durable Functions Fan-Out/…](https://github.com/Azure-Samples/durable-functions-quickstart-typescript-azd/commit/1171a96db47b86f7320cffbeded3ad2fada009cb) - `2026-11-24T22:36:05Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the TypeScript Durable Functions Fan-Out/Fan-In](https://github.com/Azure-Samples/durable-functions-quickstart-typescript-azd/pull/12)

### Azure-Samples/durable-functions-order-processing-python (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the Python Durable Functions Order Proces…](https://github.com/Azure-Samples/durable-functions-order-processing-python/commit/c8a923a3810e0e1381f647b09f2e32500a3c9767) - `2026-11-24T22:35:53Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Python Durable Functions Order Processing](https://github.com/Azure-Samples/durable-functions-order-processing-python/pull/9)

### Azure-Samples/durable-functions-quickstart-python-azd (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the Python Durable Functions Fan-Out/Fan-…](https://github.com/Azure-Samples/durable-functions-quickstart-python-azd/commit/f6e866c2e32a8aa59183eb1587aecfbfcfa0ffed) - `2026-11-24T22:35:43Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Python Durable Functions Fan-Out/Fan-In](https://github.com/Azure-Samples/durable-functions-quickstart-python-azd/pull/9)

### Azure-Samples/functions-quickstart-msft-agent-framework-go-azd (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Add template descriptor for the Go Agent Framework Multi-Agent (#12)](https://github.com/Azure-Samples/functions-quickstart-msft-agent-framework-go-azd/commit/46062b6ec3f35f0aae1cafb8a285968dabc2d095) - `2026-11-24T22:11:06Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Go Agent Framework Multi-Agent](https://github.com/Azure-Samples/functions-quickstart-msft-agent-framework-go-azd/pull/12)

### microsoft/ebpf-for-windows-sample-program (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, product:PowerShell, samples, watchlist`

- [Bump microsoft/setup-msbuild from 1.0.2 to 3.0.0 in the actions group…](https://github.com/microsoft/ebpf-for-windows-sample-program/commit/9e3ddd8d25c825e8217bac776f7f72a2c765d0e4) - `2026-11-24T22:09:49Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump microsoft/setup-msbuild from 1.0.2 to 3.0.0 in the actions group](https://github.com/microsoft/ebpf-for-windows-sample-program/pull/15)

### microsoft/kiota-serialization-form-go (1 commit(s), signal 26)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #177 from microsoft/dependabot/github_actions/acti…](https://github.com/microsoft/kiota-serialization-form-go/commit/eec7a6951ab42c3872e95b349e427f03fbde7142) - `2026-11-24T21:48:50Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump actions/setup-go from 7.0.0 to 7.1.0](https://github.com/microsoft/kiota-serialization-form-go/pull/177)

### Azure-Samples/functions-quickstart-javascript-azd-cosmosdb (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the JavaScript Cosmos DB Trigger (#3)](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-cosmosdb/commit/4768eacf69717afcf780182490c9d1bdab38fecd) - `2026-11-24T21:32:07Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the JavaScript Cosmos DB Trigger](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-cosmosdb/pull/3)

### Azure-Samples/functions-quickstart-javascript-azd-eventgrid-blob (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the JavaScript Event Grid Blob Trigger (#17)](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-eventgrid-blob/commit/40a970df5a6534b32d05ca3f9c20b20a5a062e25) - `2026-11-24T21:32:04Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the JavaScript Event Grid Blob Trigger](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-eventgrid-blob/pull/17)

### Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the TypeScript Event Grid Blob Trigger (#29)](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob/commit/7ea81b7390c345d3108e1e482b73bc2f842fc981) - `2026-11-24T21:32:00Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the TypeScript Event Grid Blob Trigger](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-eventgrid-blob/pull/29)

### Azure-Samples/functions-quickstart-javascript-azd-timer (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the JavaScript Timer Trigger (#5)](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-timer/commit/db9af57874f9d31df51c39c76737c8a40221db93) - `2026-11-24T21:31:56Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the JavaScript Timer Trigger](https://github.com/Azure-Samples/functions-quickstart-javascript-azd-timer/pull/5)

### Azure-Samples/functions-quickstart-typescript-azd-timer (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the TypeScript Timer Trigger (#6)](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-timer/commit/4aad44226847a0b121f8db0f62bf741ec972b9bb) - `2026-11-24T21:31:52Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the TypeScript Timer Trigger](https://github.com/Azure-Samples/functions-quickstart-typescript-azd-timer/pull/6)

### Azure-Samples/functions-quickstart-typescript-azd (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the TypeScript HTTP Trigger (#26)](https://github.com/Azure-Samples/functions-quickstart-typescript-azd/commit/9b3bb1d4f1637a9468c96a427dfd5c1449c3c099) - `2026-11-24T21:31:48Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the TypeScript HTTP Trigger](https://github.com/Azure-Samples/functions-quickstart-typescript-azd/pull/26)

### Azure-Samples/functions-quickstart-go-azd (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the Go HTTP Trigger (#8)](https://github.com/Azure-Samples/functions-quickstart-go-azd/commit/43af0f5f08fd6301ced84fc70970b5d7c3c9d875) - `2026-11-24T21:31:20Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Go HTTP Trigger](https://github.com/Azure-Samples/functions-quickstart-go-azd/pull/8)

### Azure-Samples/functions-quickstart-java-azd-eventgrid-blob (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the Java Event Grid Blob Trigger QuickSta…](https://github.com/Azure-Samples/functions-quickstart-java-azd-eventgrid-blob/commit/087db5a3431f35348fbcf785c65b66f3cc89a3ad) - `2026-11-24T21:31:15Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Java Event Grid Blob Trigger QuickStart](https://github.com/Azure-Samples/functions-quickstart-java-azd-eventgrid-blob/pull/4)

### Azure-Samples/functions-quickstart-java-azd-timer (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the Java Timer Trigger QuickStart (#4)](https://github.com/Azure-Samples/functions-quickstart-java-azd-timer/commit/04541e5d776a4f0131d2acc754dafa43e820208c) - `2026-11-24T21:31:11Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Java Timer Trigger QuickStart](https://github.com/Azure-Samples/functions-quickstart-java-azd-timer/pull/4)

### Azure-Samples/azure-functions-java-flex-consumption-azd (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the Java HTTP Trigger QuickStart (#18)](https://github.com/Azure-Samples/azure-functions-java-flex-consumption-azd/commit/2867b3d05a351bc637dadab70de490d077255ee6) - `2026-11-24T21:31:08Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Java HTTP Trigger QuickStart](https://github.com/Azure-Samples/azure-functions-java-flex-consumption-azd/pull/18)

### Azure-Samples/functions-daily-blog-hosted-skills-azd (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the Python Daily Blog Summarizer Hosted S…](https://github.com/Azure-Samples/functions-daily-blog-hosted-skills-azd/commit/41bedd54ceb9bee0391653dc9ae6076c7e9e17e5) - `2026-11-24T21:31:01Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Python Daily Blog Summarizer Hosted Skill](https://github.com/Azure-Samples/functions-daily-blog-hosted-skills-azd/pull/3)

### Azure-Samples/remote-mcp-apim-functions-python (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Merge pull request #30 from pdthummar/add-cli-template-descriptor](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/commit/8af2a9714d3ff8aecaa21947faca089e2d87b1a4) - `2026-11-24T21:30:56Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Python Remote MCP Server with API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/pull/30)

### Azure-Samples/functions-quickstart-python-azd-cosmosdb (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add template descriptor for the Python Cosmos DB Trigger (#9)](https://github.com/Azure-Samples/functions-quickstart-python-azd-cosmosdb/commit/62df4f3c9e53b1366d079d4f9a1f08ffbdde459c) - `2026-11-24T21:30:48Z` - pdthummar (@pdthummar) - PR: [Add template descriptor for the Python Cosmos DB Trigger](https://github.com/Azure-Samples/functions-quickstart-python-azd-cosmosdb/pull/9)

</details>
