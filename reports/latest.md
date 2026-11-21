# Microsoft Ecosystem Daily Brief - 2026-11-21

> Status: Fresh at generation. Current freshness is tracked in `reports/status.json`.
> Generated: 2026-11-21 20:09 UTC - Window: 24.9h from 2026-11-20 19:18 UTC to 2026-11-21 20:09 UTC.
> 67 repo(s) moved - 347 commit(s) - 11 release item(s) - 25 high-signal repo(s).

## Plain-English Summary

- Azure, PowerShell led the visible product-area activity in this window.
- 11 release item(s) were detected during the window.
- Security-related changes appeared in Azure/azure-sdk-for-rust.
- Start with human-authored changes in Azure/azure-sdk-for-rust, microsoft/vscode-docs, dotnet/runtime, Azure/homebrew-azd.
- 54 event(s) look automated, bot-heavy, dependency, or generated; review the curated sections before raw volume.

## Headline Metrics

| Metric | Value |
| --- | ---: |
| Inventory repositories | 16854 |
| Repositories after filters | 2550 |
| `pushed_at` candidates | 107 |
| Enrichment candidates | 107 |
| Repositories with movement | 67 |
| Default-branch commits | 347 |

## What Changed That Matters

| Repository | Score | Change | Actor | Noise | Headline | Time |
| --- | ---: | --- | --- | --- | --- | --- |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 100 | security_fix | human | low | [Fix CLI credential working directory on Windows](https://github.com/Azure/azure-sdk-for-rust/pull/5647) | `2026-11-20T23:54:58Z` |
| [microsoft/vscode-docs](https://github.com/microsoft/vscode-docs) | 100 | release | human | low | [docs: fix typos and grammar across release notes](https://github.com/microsoft/vscode-docs/pull/10743) | `2026-11-21T18:21:11Z` |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 100 | release | unknown | low | [Azure Sandbox v6.2.0](https://github.com/Azure-Samples/azuresandbox/releases/tag/v6.2.0) | `2026-11-21T14:38:24Z` |
| [dotnet/runtime](https://github.com/dotnet/runtime) | 100 | release | human | low | [Fix swift compilation to use a release build on release](https://github.com/dotnet/runtime/pull/138038) | `2026-11-21T08:26:46Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 100 | release | unknown | low | [Azure.Search.Documents_12.1.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Search.Documents_12.1.0) | `2026-11-21T07:59:09Z` |
| [Azure/homebrew-azd](https://github.com/Azure/homebrew-azd) | 100 | release | human | low | [Update for azd release 1.40.0-beta.1-daily.7100116](https://github.com/Azure/homebrew-azd/commit/b10b593f562658c0bcbaaecfbdbe59852a840530) | `2026-11-21T05:45:37Z` |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 100 | release | human | low | [Release vnext to main](https://github.com/Azure-Samples/azuresandbox/pull/1082) | `2026-11-21T02:57:30Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 100 | release | unknown | low | [Azure.Storage.Files.DataLake_12.28.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Storage.Files.DataLake_12.28.1) | `2026-11-21T01:26:14Z` |
| [MicrosoftDocs/sql-docs](https://github.com/MicrosoftDocs/sql-docs) | 100 | release | human | low | [docs: update PHP 5.14.0 release documentation (#38624)](https://github.com/MicrosoftDocs/sql-docs/commit/1f0979025fbb37d9e24c2b6fe0cb82fc6e9d15e8) | `2026-11-20T22:31:28Z` |
| [microsoft/perfview](https://github.com/microsoft/perfview) | 100 | release | unknown | low | [PerfView and TraceEvent 4.0.2](https://github.com/microsoft/perfview/releases/tag/v4.0.2) | `2026-11-20T22:19:29Z` |
| [microsoftgraph/msgraph-beta-sdk-java](https://github.com/microsoftgraph/msgraph-beta-sdk-java) | 100 | release | unknown | low | [v6.67.1](https://github.com/microsoftgraph/msgraph-beta-sdk-java/releases/tag/v6.67.1) | `2026-11-20T22:09:02Z` |
| [microsoftgraph/msgraph-sdk-java-core](https://github.com/microsoftgraph/msgraph-sdk-java-core) | 100 | release | human | low | [Increase Maven heap for release tasks](https://github.com/microsoftgraph/msgraph-sdk-java-core/pull/2128) | `2026-11-20T20:41:47Z` |
| [microsoftgraph/msgraph-sdk-java-core](https://github.com/microsoftgraph/msgraph-sdk-java-core) | 100 | release | human | low | [fix(ci): upgrade ESRP release task to v14](https://github.com/microsoftgraph/msgraph-sdk-java-core/pull/2166) | `2026-11-20T20:26:43Z` |
| [microsoftgraph/msgraph-beta-sdk-java](https://github.com/microsoftgraph/msgraph-beta-sdk-java) | 100 | release | human | low | [fix(ci): upgrade ESRP release task to v14](https://github.com/microsoftgraph/msgraph-beta-sdk-java/pull/1442) | `2026-11-20T20:26:27Z` |
| [microsoftgraph/msgraph-sdk-go](https://github.com/microsoftgraph/msgraph-sdk-go) | 100 | release | unknown | low | [v1.107.0](https://github.com/microsoftgraph/msgraph-sdk-go/releases/tag/v1.107.0) | `2026-11-20T19:56:36Z` |

## Product Areas

| Product area | Signal | Repos | Events | Releases | Security | Top links |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Azure | 75 | 31 | 91 | 7 | 1 | [Fix CLI credential working directory on Windows](https://github.com/Azure/azure-sdk-for-rust/pull/5647); [Azure Sandbox v6.2.0](https://github.com/Azure-Samples/azuresandbox/releases/tag/v6.2.0); [Azure.Search.Documents_12.1.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Search.Documents_12.1.0) |
| Unmapped Activity | 34 | 18 | 50 | 2 | 0 | [docs: update PHP 5.14.0 release documentation (#38624)](https://github.com/MicrosoftDocs/sql-docs/commit/1f0979025fbb37d9e24c2b6fe0cb82fc6e9d15e8); [PerfView and TraceEvent 4.0.2](https://github.com/microsoft/perfview/releases/tag/v4.0.2); [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/5a943178128ea3434b1df90fd8d842b1bbc08054) |
| PowerShell | 12 | 4 | 12 | 0 | 0 | [feat(open-data): Add meter category to Services to split shared resource types](https://github.com/microsoft/finops-toolkit/pull/2423); [fix(finops-hub): Stop price transform row fan-out and fix eligibility scoping](https://github.com/microsoft/finops-toolkit/pull/2246); [fix(finops-hub): Stop flagging FOCUS 1.2 rows as LegacyFocusVersion](https://github.com/microsoft/finops-toolkit/pull/2432) |
| .NET | 11 | 5 | 17 | 0 | 0 | [Fix swift compilation to use a release build on release](https://github.com/dotnet/runtime/pull/138038); [Add short-form verbosity examples to dotnet command docs](https://github.com/dotnet/docs/pull/56954); [EventPipe: Fix event loss during final session flush](https://github.com/dotnet/runtime/pull/137991) |
| Microsoft Graph | 8 | 3 | 10 | 2 | 0 | [v6.67.1](https://github.com/microsoftgraph/msgraph-beta-sdk-java/releases/tag/v6.67.1); [Increase Maven heap for release tasks](https://github.com/microsoftgraph/msgraph-sdk-java-core/pull/2128); [fix(ci): upgrade ESRP release task to v14](https://github.com/microsoftgraph/msgraph-sdk-java-core/pull/2166) |
| Microsoft 365 | 6 | 3 | 8 | 0 | 0 | [Merging changes synced from https://github.com/MicrosoftDocs/m365copi…](https://github.com/MicrosoftDocs/m365copilot-docs/commit/596a99e5917a8702f1cce517d9a610ba89060ce4); [Merge pull request #1862 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/m365copilot-docs/commit/703d96c260b38efe6a5a833cd9c4ba390603d7b2); [Update Work IQ MCP tool docs with content sanitization info (#1860)](https://github.com/MicrosoftDocs/m365copilot-docs/commit/25bb4049ab8c36eb0cc4c3cd943246894209c7b1) |
| Developer Tools | 1 | 2 | 2 | 0 | 0 | [docs: fix typos and grammar across release notes](https://github.com/microsoft/vscode-docs/pull/10743) |
| Identity | 0 | 1 | 2 | 0 | 0 |  |

## Today's Top Links

| Priority | Repository | Why read it |
| ---: | --- | --- |
| 1 | [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | [Security-related change: Fix CLI credential working directory on Windows](https://github.com/Azure/azure-sdk-for-rust/pull/5647) |
| 2 | [microsoft/vscode-docs](https://github.com/microsoft/vscode-docs) | [Release activity: docs: fix typos and grammar across release notes](https://github.com/microsoft/vscode-docs/pull/10743) |
| 3 | [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | [Release activity: Azure Sandbox v6.2.0](https://github.com/Azure-Samples/azuresandbox/releases/tag/v6.2.0) |
| 4 | [dotnet/runtime](https://github.com/dotnet/runtime) | [Release activity: Fix swift compilation to use a release build on release](https://github.com/dotnet/runtime/pull/138038) |
| 5 | [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Release activity: Azure.Search.Documents_12.1.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Search.Documents_12.1.0) |
| 6 | [Azure/homebrew-azd](https://github.com/Azure/homebrew-azd) | [Release activity: Update for azd release 1.40.0-beta.1-daily.7100116](https://github.com/Azure/homebrew-azd/commit/b10b593f562658c0bcbaaecfbdbe59852a840530) |
| 7 | [MicrosoftDocs/sql-docs](https://github.com/MicrosoftDocs/sql-docs) | [Release activity: docs: update PHP 5.14.0 release documentation (#38624)](https://github.com/MicrosoftDocs/sql-docs/commit/1f0979025fbb37d9e24c2b6fe0cb82fc6e9d15e8) |
| 8 | [microsoft/perfview](https://github.com/microsoft/perfview) | [Release activity: PerfView and TraceEvent 4.0.2](https://github.com/microsoft/perfview/releases/tag/v4.0.2) |

## Noise and Automation

- 54 event(s) look automated, bot-heavy, dependency, generated, or medium/high noise.
- Top noisy repositories: Azure-Samples/Durable-Task-Scheduler, MicrosoftDocs/azure-docs, MicrosoftDocs/fabric-docs, MicrosoftDocs/azure-monitor-docs, microsoft/aspire-samples.
- Noise mix: Docs: 28, Dependency: 15, Fix: 5, Sample: 2, Release: 2, SDK: 1, CI/Infra: 1.

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
| Count batches | 4 |
| Detail batches | 2 |
| Repos counted | 107 |
| Repos enriched | 67 |

</details>

<details>
<summary>Show supporting signal, release, and lifecycle tables</summary>

## High-Signal Items

| Repository | Score | Tags |
| --- | ---: | --- |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 137 | docs, human-authored, product:Azure AI, product:Azure SDK, release, release-language, watchlist |
| [microsoft/perfview](https://github.com/microsoft/perfview) | 136 | human-authored, release, release-language, samples, watchlist |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 130 | human-authored, release, release-language, samples, watchlist |
| [microsoftgraph/msgraph-beta-sdk-java](https://github.com/microsoftgraph/msgraph-beta-sdk-java) | 128 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 118 | docs, human-authored, product:Azure SDK, release-language, security, watchlist |
| [dotnet/runtime](https://github.com/dotnet/runtime) | 110 | docs, human-authored, release-language, watchlist |
| [Azure-Samples/azure-app-platform-templates](https://github.com/Azure-Samples/azure-app-platform-templates) | 102 | human-authored, release-language, samples, watchlist |
| [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs) | 100 | docs, human-authored, watchlist |
| [MicrosoftDocs/azure-compute-docs](https://github.com/MicrosoftDocs/azure-compute-docs) | 100 | docs, human-authored, watchlist |
| [MicrosoftDocs/fabric-docs](https://github.com/MicrosoftDocs/fabric-docs) | 95 | docs, human-authored, watchlist |
| [MicrosoftDocs/azure-docs-sdk-dotnet](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet) | 94 | docs, human-authored, product:Azure SDK, watchlist |
| [microsoft/finops-toolkit](https://github.com/microsoft/finops-toolkit) | 91 | docs, human-authored, product:PowerShell, release-language, watchlist |
| [MicrosoftDocs/azure-monitor-docs](https://github.com/MicrosoftDocs/azure-monitor-docs) | 90 | docs, human-authored, release-language, watchlist |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 90 | docs, human-authored, product:Azure SDK, release-language, watchlist |
| [microsoftgraph/msgraph-sdk-java-core](https://github.com/microsoftgraph/msgraph-sdk-java-core) | 89 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release-language, watchlist |

## Watchlist Hits

| Repository | Score | Matches |
| --- | ---: | --- |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 137 | products: Azure AI, Azure SDK; repos: Azure/azure-sdk-for-net; orgs: Azure; keywords: agent, release, sdk |
| [microsoft/perfview](https://github.com/microsoft/perfview) | 136 | keywords: release |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 130 | keywords: release |
| [microsoftgraph/msgraph-beta-sdk-java](https://github.com/microsoftgraph/msgraph-beta-sdk-java) | 128 | products: Microsoft Graph, Azure SDK; orgs: microsoftgraph; keywords: graph, msgraph, release, sdk |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 118 | products: Azure SDK; orgs: Azure; keywords: sdk |
| [dotnet/runtime](https://github.com/dotnet/runtime) | 110 | keywords: release |
| [Azure-Samples/azure-app-platform-templates](https://github.com/Azure-Samples/azure-app-platform-templates) | 102 | keywords: release |
| [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs) | 100 | repos: MicrosoftDocs/azure-docs; orgs: MicrosoftDocs |
| [MicrosoftDocs/azure-compute-docs](https://github.com/MicrosoftDocs/azure-compute-docs) | 100 | orgs: MicrosoftDocs |
| [MicrosoftDocs/fabric-docs](https://github.com/MicrosoftDocs/fabric-docs) | 95 | orgs: MicrosoftDocs |
| [MicrosoftDocs/azure-docs-sdk-dotnet](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet) | 94 | products: Azure SDK; orgs: MicrosoftDocs; keywords: sdk |
| [microsoft/finops-toolkit](https://github.com/microsoft/finops-toolkit) | 91 | products: PowerShell; keywords: powershell |
| [MicrosoftDocs/azure-monitor-docs](https://github.com/MicrosoftDocs/azure-monitor-docs) | 90 | orgs: MicrosoftDocs |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 90 | products: Azure SDK; repos: Azure/azure-sdk-for-python; orgs: Azure; keywords: azure sdk, sdk |
| [microsoftgraph/msgraph-sdk-java-core](https://github.com/microsoftgraph/msgraph-sdk-java-core) | 89 | products: Microsoft Graph, Azure SDK; orgs: microsoftgraph; keywords: graph, kiota, msgraph, release, sdk |

## Releases

| Repository | Release | Published |
| --- | --- | --- |
| [Azure/azure-sdk-for-cpp](https://github.com/Azure/azure-sdk-for-cpp) | [azure-core-amqp_1.0.0-beta.15](https://github.com/Azure/azure-sdk-for-cpp/releases/tag/azure-core-amqp_1.0.0-beta.15) | `2026-11-21T15:53:36Z` |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | [Azure Sandbox v6.2.0](https://github.com/Azure-Samples/azuresandbox/releases/tag/v6.2.0) | `2026-11-21T14:38:24Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.Search.Documents_12.1.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Search.Documents_12.1.0) | `2026-11-21T07:59:09Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.Storage.Files.DataLake_12.28.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Storage.Files.DataLake_12.28.1) | `2026-11-21T01:26:14Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.Storage.Files.Shares_12.28.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Storage.Files.Shares_12.28.1) | `2026-11-20T23:04:34Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.Storage.Queues_12.28.2](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Storage.Queues_12.28.2) | `2026-11-20T23:03:17Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.Storage.Common_12.29.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Storage.Common_12.29.1) | `2026-11-20T22:52:53Z` |
| [microsoft/perfview](https://github.com/microsoft/perfview) | [PerfView and TraceEvent 4.0.2](https://github.com/microsoft/perfview/releases/tag/v4.0.2) | `2026-11-20T22:19:29Z` |
| [microsoftgraph/msgraph-beta-sdk-java](https://github.com/microsoftgraph/msgraph-beta-sdk-java) | [v6.67.1](https://github.com/microsoftgraph/msgraph-beta-sdk-java/releases/tag/v6.67.1) | `2026-11-20T22:09:02Z` |
| [Azure/data-api-builder](https://github.com/Azure/data-api-builder) | [2.1.7: Data API builder for Azure Databases](https://github.com/Azure/data-api-builder/releases/tag/v2.1.7) | `2026-11-20T20:03:31Z` |
| [microsoftgraph/msgraph-sdk-go](https://github.com/microsoftgraph/msgraph-sdk-go) | [v1.107.0](https://github.com/microsoftgraph/msgraph-sdk-go/releases/tag/v1.107.0) | `2026-11-20T19:56:36Z` |

## Repository Lifecycle

| Change | Count |
| --- | ---: |
| archived_changed | 0 |
| category_changed | 0 |
| default_branch_changed | 0 |
| fork_changed | 0 |
| new_repos | 0 |
| removed_repos | 0 |

## Category Summary

| Category | Repositories |
| --- | ---: |
| docs | 48 |
| samples | 17 |
| training | 2 |

## Organization Summary

| Org | Repositories |
| --- | ---: |
| MicrosoftDocs | 20 |
| microsoft | 16 |
| Azure | 13 |
| Azure-Samples | 6 |
| dotnet | 5 |
| microsoftgraph | 3 |
| MicrosoftLearning | 2 |
| OfficeDev | 1 |
| SharePoint | 1 |

</details>

<details>
<summary>Show raw repository activity</summary>

## Busiest Repositories

| Repository | Signal | Category | Commits | Releases | Newest commit |
| --- | ---: | --- | ---: | ---: | --- |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 137 | docs | 12 | 5 | `2026-11-21T19:32:07Z` |
| [microsoft/perfview](https://github.com/microsoft/perfview) | 136 | samples | 11 | 1 | `2026-11-21T00:17:09Z` |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 130 | samples | 5 | 1 | `2026-11-21T02:57:30Z` |
| [microsoftgraph/msgraph-beta-sdk-java](https://github.com/microsoftgraph/msgraph-beta-sdk-java) | 128 | docs | 3 | 1 | `2026-11-20T22:08:33Z` |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 118 | docs | 8 | 0 | `2026-11-21T00:57:22Z` |
| [dotnet/runtime](https://github.com/dotnet/runtime) | 110 | docs | 27 | 0 | `2026-11-21T15:32:40Z` |
| [Azure-Samples/azure-app-platform-templates](https://github.com/Azure-Samples/azure-app-platform-templates) | 102 | samples | 17 | 0 | `2026-11-21T18:29:24Z` |
| [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs) | 100 | docs | 45 | 0 | `2026-11-21T18:09:54Z` |
| [MicrosoftDocs/azure-compute-docs](https://github.com/MicrosoftDocs/azure-compute-docs) | 100 | docs | 29 | 0 | `2026-11-20T23:03:32Z` |
| [MicrosoftDocs/fabric-docs](https://github.com/MicrosoftDocs/fabric-docs) | 95 | docs | 20 | 0 | `2026-11-21T06:06:52Z` |
| [MicrosoftDocs/azure-docs-sdk-dotnet](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet) | 94 | docs | 19 | 0 | `2026-11-21T08:11:52Z` |
| [microsoft/finops-toolkit](https://github.com/microsoft/finops-toolkit) | 91 | docs | 6 | 0 | `2026-11-21T11:22:24Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 90 | docs | 5 | 0 | `2026-11-20T23:50:43Z` |
| [MicrosoftDocs/azure-monitor-docs](https://github.com/MicrosoftDocs/azure-monitor-docs) | 90 | docs | 5 | 0 | `2026-11-20T23:09:11Z` |
| [microsoftgraph/msgraph-sdk-java-core](https://github.com/microsoftgraph/msgraph-sdk-java-core) | 89 | docs | 4 | 0 | `2026-11-20T20:41:47Z` |
| [MicrosoftDocs/sql-docs](https://github.com/MicrosoftDocs/sql-docs) | 88 | docs | 3 | 0 | `2026-11-20T23:38:38Z` |
| [MicrosoftDocs/azure-docs-sdk-python](https://github.com/MicrosoftDocs/azure-docs-sdk-python) | 87 | docs | 2 | 0 | `2026-11-20T23:06:14Z` |
| [MicrosoftDocs/SupportArticles-docs](https://github.com/MicrosoftDocs/SupportArticles-docs) | 86 | docs | 11 | 0 | `2026-11-21T02:04:32Z` |
| [microsoft/vscode-docs](https://github.com/microsoft/vscode-docs) | 86 | docs | 1 | 0 | `2026-11-21T18:21:11Z` |
| [microsoft/WindowsAppSDK-Samples](https://github.com/microsoft/WindowsAppSDK-Samples) | 86 | samples | 1 | 0 | `2026-11-21T16:42:49Z` |

## Repository Details

### MicrosoftDocs/azure-docs (45 commit(s), signal 100)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-do…](https://github.com/MicrosoftDocs/azure-docs/commit/3ba4b2a3845f15f2136eb6d8af775e77d687cc54) - `2026-11-21T18:09:54Z` - Learn Build Service GitHub App
- [Merge pull request #322738 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-docs/commit/86a2ddb4ca47696bd61cbf84fcf565a10e423962) - `2026-11-21T18:09:20Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #322735 from n-bajaj/patch-22](https://github.com/MicrosoftDocs/azure-docs/commit/bc7385b9b5f1a44cbfc2b89c8b820da5b2b0b66f) - `2026-11-21T17:54:39Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #322732 from n-bajaj/patch-19](https://github.com/MicrosoftDocs/azure-docs/commit/495546a8a31176c870f13f3cad762f327d8d3957) - `2026-11-21T17:52:41Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #322733 from n-bajaj/patch-20](https://github.com/MicrosoftDocs/azure-docs/commit/f249c3ac62f1b81762363d113c287529abc6197f) - `2026-11-21T17:15:27Z` - prmerger-automator[bot] (@prmerger-automator[bot])

### MicrosoftDocs/azure-compute-docs (29 commit(s), signal 100)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #4429 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-compute-docs/commit/d10a4ef845825300e9d837fd287bed44250d59e7) - `2026-11-20T23:03:32Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #4408 from suzuber/virtual-machines-gpu-lifecycle-…](https://github.com/MicrosoftDocs/azure-compute-docs/commit/ec2a082fa5c434f1602dec9995c866b59cc89e43) - `2026-11-20T22:35:03Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Update articles/virtual-machines/sizes/lifecycle/retirement/ncv3-nc24…](https://github.com/MicrosoftDocs/azure-compute-docs/commit/73ab757bdbb1e748dc0f77a2c99a73e9a79bf64a) - `2026-11-20T22:28:56Z` - Suzi Zuber (@suzuber)
- [Merge branch 'main' into virtual-machines-gpu-lifecycle-retirement-no…](https://github.com/MicrosoftDocs/azure-compute-docs/commit/6cbc3082a8e9f3ffc6d85c4037d7ea6eca75fd28) - `2026-11-20T22:17:58Z` - Suzi Zuber (@suzuber)
- [docs: Update NVv4 retirement author metadata](https://github.com/MicrosoftDocs/azure-compute-docs/commit/f8aa4b74a3b6d601eb9a1a0410a5ed1157107e47) - `2026-11-20T22:09:07Z` - suzuber (@suzuber)

### dotnet/runtime (27 commit(s), signal 110)

Tags: `docs, human-authored, release-language, watchlist`

- [JIT: don't make small-typed divisors reg-optional on xarch (#137969)](https://github.com/dotnet/runtime/commit/d7a6547f2a039031d9c29180bb95541a06a86276) - `2026-11-21T15:32:40Z` - Andy Ayers (@AndyAyersMS) - PR: [JIT: don't make small-typed divisors reg-optional on xarch](https://github.com/dotnet/runtime/pull/137969)
- [JIT: preserve wide-vector WithElement source across side effects (#13…](https://github.com/dotnet/runtime/commit/1510510a8f3d3a88476c7a5b88e95ff4f46b7565) - `2026-11-21T15:31:31Z` - Andy Ayers (@AndyAyersMS) - PR: [JIT: preserve wide-vector WithElement source across side effects](https://github.com/dotnet/runtime/pull/138024)
- [Remove metadata token deletion (HAS_DELETE) support (#137789)](https://github.com/dotnet/runtime/commit/36f825506e9b37bca61eaed37b2152feccd0e983) - `2026-11-21T13:10:23Z` - David Wrighton (@davidwrighton) - PR: [Remove metadata token deletion (HAS_DELETE) support](https://github.com/dotnet/runtime/pull/137789)
- [EventPipe: Fix event loss during final session flush (#137991)](https://github.com/dotnet/runtime/commit/c7cc51295d975e557ef97a79370dc0466911f284) - `2026-11-21T10:59:36Z` - Pavel Savara (@pavelsavara) - PR: [EventPipe: Fix event loss during final session flush](https://github.com/dotnet/runtime/pull/137991)
- [Fix swift compilation to use a release build on release (#138038)](https://github.com/dotnet/runtime/commit/257af3fd248eb911e5e904e8e91d1114e98b433d) - `2026-11-21T08:26:46Z` - Kevin Jones (@vcsjones) - PR: [Fix swift compilation to use a release build on release](https://github.com/dotnet/runtime/pull/138038)

### MicrosoftDocs/fabric-docs (20 commit(s), signal 95)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #3533 from MicrosoftDocs/main639308379951141119syn…](https://github.com/MicrosoftDocs/fabric-docs/commit/d17f1d1a3690312c9a2f23172b72d7455348794f) - `2026-11-21T06:06:52Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3533)
- [Merging changes synced from https://github.com/MicrosoftDocs/fabric-d…](https://github.com/MicrosoftDocs/fabric-docs/commit/a05adfd18c21b03b2cf4fd1456cc54ac84f92b09) - `2026-11-21T06:06:29Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3533)
- [Merge pull request #17477 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/fabric-docs/commit/58546bd8572911677cc7dd60af89a66ad50a60b9) - `2026-11-21T06:02:20Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3533)
- [Merge pull request #3532 from MicrosoftDocs/main639308147589126468syn…](https://github.com/MicrosoftDocs/fabric-docs/commit/7cb4f3be8ec5a1c64eca18c568c7ee49c2ebab50) - `2026-11-20T23:39:34Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3532)
- [Merging changes synced from https://github.com/MicrosoftDocs/fabric-d…](https://github.com/MicrosoftDocs/fabric-docs/commit/c94dbb5ff9946792d27623ee01c23cb14f4bd073) - `2026-11-20T23:39:16Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3532)

### MicrosoftDocs/azure-docs-sdk-dotnet (19 commit(s), signal 94)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/df947d3252de9d5c5d8ba4f89a168d3e9e7b3cf6) - `2026-11-21T08:11:52Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/6d0186f47fbf74f2f2442ef6062feb59561fcc7c) - `2026-11-21T02:26:33Z` - azure-sdk (@azure-sdk)
- [CI Update](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/92b467d91d156691a12fbd171f542cfa8334c201) - `2026-11-21T02:18:16Z` - docsreference@microsoft.com
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/e23d73a2e5ec1cefb7229fca0ed4ce2a3e1d9331) - `2026-11-21T01:38:08Z` - azure-sdk (@azure-sdk)
- [Update docs CI configuration](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/30c677e3278621cf60eca593311e07a08ac29d6b) - `2026-11-20T23:51:19Z` - azure-sdk (@azure-sdk)

### Azure-Samples/azure-app-platform-templates (17 commit(s), signal 102)

Tags: `human-authored, release-language, samples, watchlist`

- [Merge pull request #9 from Azure-Samples/fix/zero-simulation-dealersh…](https://github.com/Azure-Samples/azure-app-platform-templates/commit/2a00a00b4e42213f011c01180928b6f816038c5a) - `2026-11-21T18:29:24Z` - Paul Yuknewicz (@paulyuk) - PR: [Remove runtime simulation in sandbox starters and dealership-e2e](https://github.com/Azure-Samples/azure-app-platform-templates/pull/9)
- [Merge pull request #10 from Azure-Samples/feat/mcp-skill-conventions](https://github.com/Azure-Samples/azure-app-platform-templates/commit/0d45c699a7ea083fcb179aa03da16239d65b105e) - `2026-11-21T18:29:16Z` - Paul Yuknewicz (@paulyuk) - PR: [feat: add shared deterministic MCP Hosted Skill block and wire pilot templates](https://github.com/Azure-Samples/azure-app-platform-templates/pull/10)
- [fix: isolate POSIX MCP skills in dedicated process groups and tear do…](https://github.com/Azure-Samples/azure-app-platform-templates/commit/43d0a4f60ec6faff16660d7804b23ea9ebf05625) - `2026-11-21T10:26:29Z` - paulyuk (@paulyuk) - PR: [feat: add shared deterministic MCP Hosted Skill block and wire pilot templates](https://github.com/Azure-Samples/azure-app-platform-templates/pull/10)
- [test(dealership): drop removed skip_parsing kwarg in inventory runtim…](https://github.com/Azure-Samples/azure-app-platform-templates/commit/5e9de7ec6a254b2a67762d4d7ca7c82645d95d99) - `2026-11-21T10:24:45Z` - paulyuk (@paulyuk) - PR: [Remove runtime simulation in sandbox starters and dealership-e2e](https://github.com/Azure-Samples/azure-app-platform-templates/pull/9)
- [fix: add tenacity dependency, uv prerelease setting, and supervisor-f…](https://github.com/Azure-Samples/azure-app-platform-templates/commit/08b156390a337f00e1583a28842018f1970178f7) - `2026-11-21T10:19:12Z` - paulyuk (@paulyuk) - PR: [feat: add shared deterministic MCP Hosted Skill block and wire pilot templates](https://github.com/Azure-Samples/azure-app-platform-templates/pull/10)

### Azure-Samples/Durable-Task-Scheduler (15 commit(s), signal 30)

Tags: `bot-only, dependency-noise, product:Azure AI, product:Azure SDK, samples, watchlist`

- [Update openai requirement (#425)](https://github.com/Azure-Samples/Durable-Task-Scheduler/commit/145056eeb59d2ea1842468e46cd73a3e2f693f28) - `2026-11-21T01:27:38Z` - dependabot[bot] (@dependabot[bot]) - PR: [Update openai requirement from >=3.28.0 to >=3.54.0 in /samples/durable-functions/python/agent-directed-workflows](https://github.com/Azure-Samples/Durable-Task-Scheduler/pull/425)
- [Update azure-identity requirement in /samples/durable-task-sdks/pytho…](https://github.com/Azure-Samples/Durable-Task-Scheduler/commit/dc6a7ae5c77fe8849e9ba76531762467cc00ee41) - `2026-11-21T01:27:30Z` - dependabot[bot] (@dependabot[bot]) - PR: [Update azure-identity requirement from >=1.25.3 to >=1.27.0 in /samples/durable-task-sdks/python](https://github.com/Azure-Samples/Durable-Task-Scheduler/pull/428)
- [Bump the npm_and_yarn group across 2 directories with 1 update (#460)](https://github.com/Azure-Samples/Durable-Task-Scheduler/commit/d8b0390f4aaa25870547e9aecf4222f7b6b21639) - `2026-11-21T01:27:22Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the npm_and_yarn group across 2 directories with 1 update](https://github.com/Azure-Samples/Durable-Task-Scheduler/pull/460)
- [Bump follow-redirects (#439)](https://github.com/Azure-Samples/Durable-Task-Scheduler/commit/c40588a25cc6e78e8c9e86a92e419202d2209af5) - `2026-11-20T23:49:12Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump follow-redirects from 1.16.0 to 1.16.3 in /samples/durable-functions/javascript/HelloCities](https://github.com/Azure-Samples/Durable-Task-Scheduler/pull/439)
- [Bump follow-redirects (#440)](https://github.com/Azure-Samples/Durable-Task-Scheduler/commit/9d03fcd60083c94b590af4ba2622aad3bd7582bb) - `2026-11-20T23:49:05Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump follow-redirects from 1.16.0 to 1.16.3 in /samples/durable-functions/dotnet/AiAgentTravelPlanOrchestrator/Frontend](https://github.com/Azure-Samples/Durable-Task-Scheduler/pull/440)

### Azure/azure-sdk-for-net (12 commit(s), signal 137)

Tags: `docs, human-authored, product:Azure AI, product:Azure SDK, release, release-language, watchlist`

- Release: [Azure.Search.Documents_12.1.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Search.Documents_12.1.0) - `2026-11-21T07:59:09Z`
- Release: [Azure.Storage.Files.DataLake_12.28.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Storage.Files.DataLake_12.28.1) - `2026-11-21T01:26:14Z`
- Release: [Azure.Storage.Files.Shares_12.28.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Storage.Files.Shares_12.28.1) - `2026-11-20T23:04:34Z`
- Release: [Azure.Storage.Queues_12.28.2](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Storage.Queues_12.28.2) - `2026-11-20T23:03:17Z`
- Release: [Azure.Storage.Common_12.29.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Storage.Common_12.29.1) - `2026-11-20T22:52:53Z`
- [[AgentServer] Add experimental original-subject attribution (#65073)](https://github.com/Azure/azure-sdk-for-net/commit/77ac5395e75f506cd1732cb119a702bbf0650027) - `2026-11-21T19:32:07Z` - Shiva S (@Shivakishore14) - PR: [[AgentServer] Add experimental original-subject attribution](https://github.com/Azure/azure-sdk-for-net/pull/65073)
- [Increment version for appconfiguration releases (#65071)](https://github.com/Azure/azure-sdk-for-net/commit/830c9c91604c7a7022a8560aec20c5f354b35c4b) - `2026-11-21T19:03:20Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment version for appconfiguration releases](https://github.com/Azure/azure-sdk-for-net/pull/65071)
- [[Search] .NET SDK for DP 2026-10-01 GA (#63555)](https://github.com/Azure/azure-sdk-for-net/commit/e1f9d2366f338e7d2b297e7b5e9067400970d3f9) - `2026-11-21T00:20:42Z` - efrainretana (@efrainretana) - PR: [[Search] .NET SDK for DP 2026-10-01 GA](https://github.com/Azure/azure-sdk-for-net/pull/63555)
- [Increment version for storage releases (#65101)](https://github.com/Azure/azure-sdk-for-net/commit/3dda46e1a9e1a7effa5233a0de9ba6f543838834) - `2026-11-20T23:11:27Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment version for storage releases](https://github.com/Azure/azure-sdk-for-net/pull/65101)
- [Make code-review rules individually linkable (#65097)](https://github.com/Azure/azure-sdk-for-net/commit/dc916a6d6e1882f9ac7f7c8454df46e97dcee81e) - `2026-11-20T22:25:34Z` - m-nash (@m-nash) - PR: [Make code-review rules individually linkable](https://github.com/Azure/azure-sdk-for-net/pull/65097)

### MicrosoftDocs/SupportArticles-docs (11 commit(s), signal 86)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/bcf139953721fe82879b7f2fab7a384a141d00de) - `2026-11-21T02:04:32Z` - Learn Build Service GitHub App
- [Merge pull request #12930 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/326a63905b569c37d83ff5031cbffa9c742221e2) - `2026-11-21T02:02:38Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Free/busy is unavailable within the same Exchange Online tenant (#12915)](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/20b31952c1d53e1f4c823fd904ed798e05ad1d70) - `2026-11-21T00:17:09Z` - Shane Ferrell (@Shanefe)
- [AB#13521: AI Optimization and Freshness review: SQL Server error 1642…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/259a260dac3773416d5b63e71b80493abb93c782) - `2026-11-20T22:49:40Z` - Aarti Goyle (@aartig13)
- [AB#13519: AI Optimization and Freshness review: Installation of SQL S…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/35cb45bd93e3cb90d0116cbc692d944e54455728) - `2026-11-20T22:36:31Z` - Aarti Goyle (@aartig13)

### microsoft/perfview (11 commit(s), signal 136)

Tags: `human-authored, release, release-language, samples, watchlist`

- Release: [PerfView and TraceEvent 4.0.2](https://github.com/microsoft/perfview/releases/tag/v4.0.2) - `2026-11-20T22:19:29Z`
- [Merge PerfView/TraceEvent 4.0.2 Changes (#2518)](https://github.com/microsoft/perfview/commit/ea4e78e0e363a0838c963338619221f3e211ddb5) - `2026-11-21T00:17:09Z` - Brian Robbins (@brianrob) - PR: [Merge PerfView/TraceEvent 4.0.2 Changes](https://github.com/microsoft/perfview/pull/2518)
- [Test CTF payload limits after string conversion](https://github.com/microsoft/perfview/commit/3ce91243c77a610c2522e95c7126eaee1888b91b) - `2026-11-20T22:07:58Z` - Brian Robbins (@brianrob) - PR: [Merge PerfView/TraceEvent 4.0.2 Changes](https://github.com/microsoft/perfview/pull/2518)
- [Bump release version to 4.0.2](https://github.com/microsoft/perfview/commit/eeebb00e1aafb3eab47125cbb22c8edd8b6a5a68) - `2026-11-20T21:38:54Z` - Brian Robbins (@brianrob) - PR: [Merge PerfView/TraceEvent 4.0.2 Changes](https://github.com/microsoft/perfview/pull/2518)
- [Validate complete event payloads before reads and allocation](https://github.com/microsoft/perfview/commit/2dbabf82079f5f562d48cbab92bdbd38fb7e0861) - `2026-11-20T21:38:34Z` - Jeremy Kuhne (@JeremyKuhne) - PR: [Merge PerfView/TraceEvent 4.0.2 Changes](https://github.com/microsoft/perfview/pull/2518)
- [Decode TCP connection fields by event layout](https://github.com/microsoft/perfview/commit/5bb755726ec5943687c46b3dee2b1d6977083034) - `2026-11-20T21:38:34Z` - Brian Robbins (@brianrob) - PR: [Merge PerfView/TraceEvent 4.0.2 Changes](https://github.com/microsoft/perfview/pull/2518)

### MicrosoftDocs/learn (9 commit(s), signal 84)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/5a943178128ea3434b1df90fd8d842b1bbc08054) - `2026-11-21T08:18:22Z` - Learn Build Service GitHub App
- [Merge pull request #56910 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/learn/commit/724eb37f4fe9447780706206240903c84969b5e1) - `2026-11-21T08:10:13Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Module review and freshness update (#56908)](https://github.com/MicrosoftDocs/learn/commit/31f5da2eb556971c76058257c5ad94c18e21acaa) - `2026-11-21T07:15:42Z` - Orin Thomas (@Orin-Thomas)
- [Post-Ignite UI updates (#56907)](https://github.com/MicrosoftDocs/learn/commit/87ce422e3e52f7de882bb125a43523bc258d15f8) - `2026-11-21T06:23:45Z` - Graeme Malcolm (@GraemeMalcolm)
- [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/279d77af110bac91c3760cc862be7755a55c100c) - `2026-11-20T23:16:18Z` - Learn Build Service GitHub App

### Azure/azure-sdk-for-rust (8 commit(s), signal 118)

Tags: `docs, human-authored, product:Azure SDK, release-language, security, watchlist`

- [Isolate Key Vault test resource names (#5653)](https://github.com/Azure/azure-sdk-for-rust/commit/554dc96b730b4b802883552bc0dc9e6e017241f4) - `2026-11-21T00:57:22Z` - Heath Stewart (@heaths) - PR: [Isolate Key Vault test resource names](https://github.com/Azure/azure-sdk-for-rust/pull/5653)
- [Bump core and identity package versions (#5650)](https://github.com/Azure/azure-sdk-for-rust/commit/48c3790a40c812f76b30684b452decfa43e58f13) - `2026-11-21T00:53:46Z` - Heath Stewart (@heaths) - PR: [Bump core and identity package versions](https://github.com/Azure/azure-sdk-for-rust/pull/5650)
- [Fix driver test build: add missing vector_embedding_policy field (#5652)](https://github.com/Azure/azure-sdk-for-rust/commit/4eda694b24b8f07cb1e66017f73ad1fa38d1e2e3) - `2026-11-20T23:55:34Z` - DmitriMelnikov (@DmitriMelnikov) - PR: [Fix driver test build: add missing vector_embedding_policy field](https://github.com/Azure/azure-sdk-for-rust/pull/5652)
- [Fix CLI credential working directory on Windows (#5647)](https://github.com/Azure/azure-sdk-for-rust/commit/2614e8d6738d6648943b380eba7c2f2950e70d78) - `2026-11-20T23:54:58Z` - Heath Stewart (@heaths) - PR: [Fix CLI credential working directory on Windows](https://github.com/Azure/azure-sdk-for-rust/pull/5647)
- [Sync eng/common directory with azure-sdk-tools for PR 17576 (#5639)](https://github.com/Azure/azure-sdk-for-rust/commit/d7b27354bd43eecab2b13be083f5971eb93a139c) - `2026-11-20T22:28:32Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17576](https://github.com/Azure/azure-sdk-for-rust/pull/5639)

### microsoft/finops-toolkit (6 commit(s), signal 91)

Tags: `docs, human-authored, product:PowerShell, release-language, watchlist`

- [feat(open-data): Add meter category to Services to split shared resou…](https://github.com/microsoft/finops-toolkit/commit/0e46c2afd720bb6218837c76842c2b7dac226ce6) - `2026-11-21T11:22:24Z` - Michael Flanakin (@flanakin) - PR: [feat(open-data): Add meter category to Services to split shared resource types](https://github.com/microsoft/finops-toolkit/pull/2423)
- [fix(finops-hub): Stop price transform row fan-out and fix eligibility…](https://github.com/microsoft/finops-toolkit/commit/9f27f21bf33f94b6bf1a6244d9fa8026cb0ecf7a) - `2026-11-21T11:14:34Z` - Michael Flanakin (@flanakin) - PR: [fix(finops-hub): Stop price transform row fan-out and fix eligibility scoping](https://github.com/microsoft/finops-toolkit/pull/2246)
- [fix(finops-hub): Stop flagging FOCUS 1.2 rows as LegacyFocusVersion (…](https://github.com/microsoft/finops-toolkit/commit/ffd68ed379f752b1114c73ab517599c77939126f) - `2026-11-21T10:51:47Z` - Michael Flanakin (@flanakin) - PR: [fix(finops-hub): Stop flagging FOCUS 1.2 rows as LegacyFocusVersion](https://github.com/microsoft/finops-toolkit/pull/2432)
- [fix(hubs): Start only hub triggers in Init-DataFactory (#2431)](https://github.com/microsoft/finops-toolkit/commit/4ae24d7520805361cc651c49ec02602c8224d3ca) - `2026-11-21T10:42:45Z` - Michael Flanakin (@flanakin) - PR: [fix(hubs): Start only hub triggers in Init-DataFactory](https://github.com/microsoft/finops-toolkit/pull/2431)
- [fix(power-bi): Replace dead aka.ms invoicing and tsg links with Micro…](https://github.com/microsoft/finops-toolkit/commit/ad1160f19f056d9c34fc898483eadad43b44966a) - `2026-11-21T10:34:09Z` - Michael Flanakin (@flanakin) - PR: [fix(power-bi): Replace dead aka.ms invoicing and tsg links with Microsoft Learn URLs](https://github.com/microsoft/finops-toolkit/pull/2429)

### MicrosoftDocs/power-platform (6 commit(s), signal 81)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/cb4d2d3f94e8096c8e7371eaf8dc13249663469b) - `2026-11-21T01:03:28Z` - Learn Build Service GitHub App
- [Merge pull request #12229 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-platform/commit/b1c0fea02d444296a4742e29b824b2362a513a0e) - `2026-11-21T01:02:07Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Unified experience documentation updates (2 changes) (#12219)](https://github.com/MicrosoftDocs/power-platform/commit/5dfc152843249d3976df736889647693a0a88ac2) - `2026-11-20T20:01:32Z` - Lane Swenka (@laneswenka)
- [Unified experience documentation updates (2 changes) (#12227)](https://github.com/MicrosoftDocs/power-platform/commit/e6c8ac71cd7e998f31bf54f5232fc30fdbd47103) - `2026-11-20T19:42:38Z` - Lane Swenka (@laneswenka)
- [Advanced connector policies documentation updates (3 changes) (#12218)](https://github.com/MicrosoftDocs/power-platform/commit/95d2db80a33e41244d8973399ecc77a3fa5e8a45) - `2026-11-20T19:34:17Z` - Lane Swenka (@laneswenka)

### Azure-Samples/azuresandbox (5 commit(s), signal 130)

Tags: `human-authored, release, release-language, samples, watchlist`

- Release: [Azure Sandbox v6.2.0](https://github.com/Azure-Samples/azuresandbox/releases/tag/v6.2.0) - `2026-11-21T14:38:24Z`
- [Merge pull request #1082 from Azure-Samples/vnext](https://github.com/Azure-Samples/azuresandbox/commit/38aa5c4df3459954d2f6b51edd2865d76ee775b3) - `2026-11-21T02:57:30Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Release vnext to main](https://github.com/Azure-Samples/azuresandbox/pull/1082)
- [Merge pull request #1081 from Azure-Samples/docs/1051-admin-contribut…](https://github.com/Azure-Samples/azuresandbox/commit/54a77dfb743f571d7b896fee597bfb1893f46f1b) - `2026-11-21T00:24:59Z` - Roger Doherty (MSFT) (@doherty100) - PR: [docs(rg-devops-iac): personas and consistency sweep (#1051)](https://github.com/Azure-Samples/azuresandbox/pull/1081)
- [docs(rg-devops-iac): personas and consistency sweep (#1051)](https://github.com/Azure-Samples/azuresandbox/commit/1f96010556714086c69c0a33cad0e70df26bf3be) - `2026-11-21T00:23:29Z` - Roger Doherty (MSFT) (@doherty100) - PR: [docs(rg-devops-iac): personas and consistency sweep (#1051)](https://github.com/Azure-Samples/azuresandbox/pull/1081)
- [Merge pull request #1080 from Azure-Samples/feature/1071-standardize-…](https://github.com/Azure-Samples/azuresandbox/commit/a33d11c3f8e1abcc7920e1971f0b28ac299426ce) - `2026-11-20T23:06:24Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Standardize VM and NIC settings on the mssqlwin1 baseline (#1071)](https://github.com/Azure-Samples/azuresandbox/pull/1080)
- [Standardize VM and NIC settings on the mssqlwin1 baseline (#1071)](https://github.com/Azure-Samples/azuresandbox/commit/66bd3570a1b5afba30a13e767804989b455a8794) - `2026-11-20T22:58:57Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Standardize VM and NIC settings on the mssqlwin1 baseline (#1071)](https://github.com/Azure-Samples/azuresandbox/pull/1080)

### Azure/azure-sdk-for-python (5 commit(s), signal 90)

Tags: `docs, human-authored, product:Azure SDK, release-language, watchlist`

- [[AI Projects] Send preview header in custom evaluator samples and lab…](https://github.com/Azure/azure-sdk-for-python/commit/e1c0306c77b27b46c79755f53783474a03fd8c0d) - `2026-11-20T23:50:43Z` - aprilk-ms (@aprilk-ms) - PR: [[AI Projects] Send preview header in custom evaluator samples and label them preview](https://github.com/Azure/azure-sdk-for-python/pull/50099)
- [Use Azure SDK clients for live sample Search provisioning (#50100)](https://github.com/Azure/azure-sdk-for-python/commit/e381ac17bb6bcb0357c06988c4726f889225741d) - `2026-11-20T23:38:37Z` - Howie Leung (@howieleung) - PR: [Use Azure SDK clients for live sample Search provisioning](https://github.com/Azure/azure-sdk-for-python/pull/50100)
- [[Storage] Introduce `azure-storage-extensionstransfer` and integrate …](https://github.com/Azure/azure-sdk-for-python/commit/03af9c094d76bd472960c379cc78b086e0dd4775) - `2026-11-20T23:16:03Z` - Jacob Lauzon (@jalauzon-msft) - PR: [[Storage] Introduce `azure-storage-extensionstransfer` and integrate with Blob](https://github.com/Azure/azure-sdk-for-python/pull/49992)
- [[Storage] create session structured message tests (#50101)](https://github.com/Azure/azure-sdk-for-python/commit/ad0ec934c880bbe3afc2d3ebf21ccf65666c1c39) - `2026-11-20T22:09:40Z` - anjaliratnam-msft (@anjaliratnam-msft) - PR: [[Storage] create session structured message tests](https://github.com/Azure/azure-sdk-for-python/pull/50101)
- [Fix Milestone parameter typo in Update-GitHubIssue (#50098)](https://github.com/Azure/azure-sdk-for-python/commit/422b13f8d5b71fca32535dae1deb4e38f5a43125) - `2026-11-20T21:01:21Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17576](https://github.com/Azure/azure-sdk-for-python/pull/50098)

### MicrosoftDocs/azure-monitor-docs (5 commit(s), signal 90)

Tags: `docs, human-authored, release-language, watchlist`

- [Merge pull request #5828 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/2d30ba8467d2fc4815b0080796e8e219aab7f335) - `2026-11-20T23:09:11Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #5774 from tokaplan/tokaplan/shannon-doc-followups](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/330cdeed83bcea6611e5bb11af080df84ab3af3d) - `2026-11-20T21:04:22Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #5827 from ganga1980/main](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/3cf7443f23d76511d5ee81e75324ac3601989eac) - `2026-11-20T20:52:56Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Update Application Insights telemetry limits](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/501cb0f117f1ee14fe9ad69c82ad9a0ecc07eafc) - `2026-11-20T20:29:50Z` - Ganga Mahesh Siddem (@ganga1980)
- [Document the 256 KB limit for GenAI content attribute values](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/f7acd4edcb3a9691d4de60643248632385f9cf6d) - `2026-11-20T19:45:06Z` - Ganga Mahesh Siddem (@ganga1980)

### MicrosoftDocs/m365copilot-docs (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/m365copi…](https://github.com/MicrosoftDocs/m365copilot-docs/commit/596a99e5917a8702f1cce517d9a610ba89060ce4) - `2026-11-20T22:00:47Z` - Learn Build Service GitHub App
- [Merge pull request #1862 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/m365copilot-docs/commit/703d96c260b38efe6a5a833cd9c4ba390603d7b2) - `2026-11-20T22:00:21Z` - Jason Johnston (@jasonjoh)
- [Update Work IQ MCP tool docs with content sanitization info (#1860)](https://github.com/MicrosoftDocs/m365copilot-docs/commit/25bb4049ab8c36eb0cc4c3cd943246894209c7b1) - `2026-11-20T21:15:03Z` - Camille Birch (@cabirch)
- [Merging changes synced from https://github.com/MicrosoftDocs/m365copi…](https://github.com/MicrosoftDocs/m365copilot-docs/commit/f2269d66e9b8e0ab95a4480092721220550650b6) - `2026-11-20T20:33:46Z` - Learn Build Service GitHub App
- [Merge pull request #1859 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/m365copilot-docs/commit/6e3b26eac508bc7f91bb65a87c8f2db64b30693a) - `2026-11-20T20:33:21Z` - Jason Johnston (@jasonjoh)

### dotnet/AspNetCore.Docs (4 commit(s), signal 54)

Tags: `docs, human-authored, release-language`

- [[11.0] GA tasks and API cross-link work (#38154)](https://github.com/dotnet/AspNetCore.Docs/commit/546bd4242547958c3d12d5e3fc0d484c380aa57d) - `2026-11-21T12:45:30Z` - Luke Latham (@guardrex) - PR: [[11.0] GA tasks and API cross-link work](https://github.com/dotnet/AspNetCore.Docs/pull/38154)
- [Archive legacy EF Core MVC tutorials (#38199)](https://github.com/dotnet/AspNetCore.Docs/commit/85419317b222dd119e76a0c967b89a47de8a4cc5) - `2026-11-21T02:41:57Z` - Genevieve Warren (@gewarren) - PR: [Archive legacy EF Core MVC tutorials](https://github.com/dotnet/AspNetCore.Docs/pull/38199)
- [Remove wait step in build warnings workflow (#38206)](https://github.com/dotnet/AspNetCore.Docs/commit/6f390792b6ac1ba0f192cb2ad9a248a28e2ead29) - `2026-11-21T02:41:08Z` - Genevieve Warren (@gewarren) - PR: [Remove wait step in build warnings workflow](https://github.com/dotnet/AspNetCore.Docs/pull/38206)
- [Bump Microsoft.EntityFrameworkCore.InMemory across 22 directories (#3…](https://github.com/dotnet/AspNetCore.Docs/commit/86b3c7749d99a82508050952f5aa052e65e6c4de) - `2026-11-21T01:13:53Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.EntityFrameworkCore.InMemory across 22 directories](https://github.com/dotnet/AspNetCore.Docs/pull/38193)

### microsoft/amplifier-module-provider-openai (4 commit(s), signal 79)

Tags: `docs, human-authored, product:Azure AI, product:Azure SDK, watchlist`

- [Count the exact native compaction operation input (#161)](https://github.com/microsoft/amplifier-module-provider-openai/commit/5d2b190c3fe2cfa7dc10a8e4d8a611f929760677) - `2026-11-21T04:44:17Z` - Brian Krabach (@bkrabach) - PR: [Count the exact input sent to native compaction](https://github.com/microsoft/amplifier-module-provider-openai/pull/161)
- [Allow Astra and Sol to reuse qualified standalone compaction (#158)](https://github.com/microsoft/amplifier-module-provider-openai/commit/46ef7b656d9ed06fc2ff35a883700d9ed0e2cfa4) - `2026-11-21T04:23:33Z` - Brian Krabach (@bkrabach) - PR: [Allow Astra and Sol to reuse qualified standalone compaction](https://github.com/microsoft/amplifier-module-provider-openai/pull/158)
- [Keep submitted images out of SDK error chains and escaped diagnostics…](https://github.com/microsoft/amplifier-module-provider-openai/commit/d5fbf4f82a7fbf58f4f367e53df8b9b711d09d62) - `2026-11-21T02:37:44Z` - Brian Krabach (@bkrabach) - PR: [Keep submitted images out of SDK error chains and escaped diagnostics](https://github.com/microsoft/amplifier-module-provider-openai/pull/160)
- [Prepare image redaction patterns once per OpenAI request (#159)](https://github.com/microsoft/amplifier-module-provider-openai/commit/69b40dde3b4bdfd98843c3da1d53e975ca6c8c4d) - `2026-11-21T02:01:14Z` - Brian Krabach (@bkrabach) - PR: [Prepare image redaction patterns once per OpenAI request](https://github.com/microsoft/amplifier-module-provider-openai/pull/159)

### MicrosoftDocs/powerapps-docs (4 commit(s), signal 79)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/powerapp…](https://github.com/MicrosoftDocs/powerapps-docs/commit/c348031067700b46faff75dcc197fad1e0e5c59c) - `2026-11-21T01:07:38Z` - Learn Build Service GitHub App
- [Merge pull request #12888 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/powerapps-docs/commit/a1a500b5d07e089fd0dca36ef5daabee1989da6e) - `2026-11-21T01:05:25Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Confirm merge from repo_sync_working_branch to main to sync with http…](https://github.com/MicrosoftDocs/powerapps-docs/commit/b814244fa6d74ce9e368f2810975825494ff3e9d) - `2026-11-21T00:20:38Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Revise settings descriptions for prompt column processing (#5561)](https://github.com/MicrosoftDocs/powerapps-docs/commit/f99763fa6cc46ee81e5f82a3a687c0341c2a16b6) - `2026-11-21T00:12:17Z` - Vaishanavi-gif (@Vaishanavi-gif) - PR: [Revise settings descriptions for prompt column processing](https://github.com/MicrosoftDocs/powerapps-docs/pull/5561)

### MicrosoftDocs/azure-aks-docs (4 commit(s), signal 79)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-ak…](https://github.com/MicrosoftDocs/azure-aks-docs/commit/31fa5fd0ff5eb81c290a1f023da94071f263554f) - `2026-11-20T23:04:03Z` - Learn Build Service GitHub App
- [Merge pull request #4275 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-aks-docs/commit/1eaff4a48a2cb21e5a66bebedea0c7e59ea33006) - `2026-11-20T23:03:25Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #4274 from nshankar13/nshankar/asm-gateway-docs-up…](https://github.com/MicrosoftDocs/azure-aks-docs/commit/1adca81cca426457dca3d717441650dc2fb2fa0a) - `2026-11-20T21:40:46Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Fix outdated Gateway API limitation](https://github.com/MicrosoftDocs/azure-aks-docs/commit/34696618465f5b167135c8ec65a3ff64b49f4263) - `2026-11-20T21:23:51Z` - nshankar13 (@nshankar13)

### microsoft/aspire-samples (4 commit(s), signal 44)

Tags: `docs, human-authored`

- [Bump Microsoft.AspNetCore.Authentication.JwtBearer and 6 others (#2191)](https://github.com/microsoft/aspire-samples/commit/96aceb451094e708d385865a1fdcf14d351c5a28) - `2026-11-20T20:46:18Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.AspNetCore.Authentication.JwtBearer and 6 others](https://github.com/microsoft/aspire-samples/pull/2191)
- [Bump Microsoft.Extensions.Diagnostics.Testing and 4 others (#2207)](https://github.com/microsoft/aspire-samples/commit/4349a056e98990cb45cbf6141c991c91b10c6c60) - `2026-11-20T20:13:53Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Extensions.Diagnostics.Testing and 4 others](https://github.com/microsoft/aspire-samples/pull/2207)
- [Bump Microsoft.EntityFrameworkCore.InMemory and 2 others (#2192)](https://github.com/microsoft/aspire-samples/commit/1d32a52f1baceee5af5b74e618f0afe7fe186491) - `2026-11-20T19:57:49Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.EntityFrameworkCore.InMemory and 2 others](https://github.com/microsoft/aspire-samples/pull/2192)
- [Update all samples to Aspire 17.0 (#2173)](https://github.com/microsoft/aspire-samples/commit/22e2fc974f79650f34f911725bbef3e260a89bbc) - `2026-11-20T19:34:17Z` - David Pine (@IEvangelist) - PR: [Update all samples to Aspire 17.0](https://github.com/microsoft/aspire-samples/pull/2173)

### microsoftgraph/msgraph-sdk-java-core (4 commit(s), signal 89)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [ci: Increase Maven heap for release tasks (#2128)](https://github.com/microsoftgraph/msgraph-sdk-java-core/commit/773e1f8916a5f971102d5973fadabcb3fe329f33) - `2026-11-20T20:41:47Z` - Gavin Barron (@gavinbarron) - PR: [Increase Maven heap for release tasks](https://github.com/microsoftgraph/msgraph-sdk-java-core/pull/2128)
- [fix(ci): upgrade ESRP release task to v14 (#2166)](https://github.com/microsoftgraph/msgraph-sdk-java-core/commit/328c52fedffd9e95b5dbc96a004cf793f59ea339) - `2026-11-20T20:26:43Z` - Gavin Barron (@gavinbarron) - PR: [fix(ci): upgrade ESRP release task to v14](https://github.com/microsoftgraph/msgraph-sdk-java-core/pull/2166)
- [ci: run required conflict check on opened and reopened PRs (#2167)](https://github.com/microsoftgraph/msgraph-sdk-java-core/commit/de74efe3617ef7c032610e89bf2a4541fbd48268) - `2026-11-20T20:22:57Z` - Gavin Barron (@gavinbarron) - PR: [ci: run required conflict check on opened and reopened PRs](https://github.com/microsoftgraph/msgraph-sdk-java-core/pull/2167)
- [fix(deps): bump the kiota-dependencies group in /android with 7 updat…](https://github.com/microsoftgraph/msgraph-sdk-java-core/commit/492ee0e79cb3a3ba4c6182f285e44ea02f1fc729) - `2026-11-20T19:40:05Z` - dependabot[bot] (@dependabot[bot]) - PR: [fix(deps): bump the kiota-dependencies group in /android with 7 updates](https://github.com/microsoftgraph/msgraph-sdk-java-core/pull/2159)

### microsoft/amplifier-module-provider-anthropic (3 commit(s), signal 43)

Tags: `docs, human-authored`

- [Count the exact input and beta used for Claude native compaction (#151)](https://github.com/microsoft/amplifier-module-provider-anthropic/commit/b4762db1ee14c07daad7f20dac6a9534ebaed1b6) - `2026-11-21T04:38:58Z` - Brian Krabach (@bkrabach) - PR: [Count the input used by Claude native compaction](https://github.com/microsoft/amplifier-module-provider-anthropic/pull/151)
- [Support locally qualified native compaction and replay on Claude mode…](https://github.com/microsoft/amplifier-module-provider-anthropic/commit/2d016065ebc83e5930e00616d0b6c2eb82a4b557) - `2026-11-21T04:23:38Z` - Brian Krabach (@bkrabach) - PR: [Support locally qualified native compaction and replay on Claude model switches](https://github.com/microsoft/amplifier-module-provider-anthropic/pull/150)
- [fix: preserve ordinary Anthropic user and tool images (#148)](https://github.com/microsoft/amplifier-module-provider-anthropic/commit/681b67a0b22695285140e61d71ed6cf9ae7d5951) - `2026-11-21T02:31:51Z` - Brian Krabach (@bkrabach) - PR: [fix: preserve ordinary Anthropic user and tool images](https://github.com/microsoft/amplifier-module-provider-anthropic/pull/148)

### Azure/azure-sdk-for-java (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [[AutoPR azure-resourcemanager-containerregistry]-generated-from-SDK G…](https://github.com/Azure/azure-sdk-for-java/commit/835b6f6197d73745e2d520c955174b1b8588ead3) - `2026-11-21T03:13:53Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-resourcemanager-containerregistry]-generated-from-SDK Generation - Java-7097054](https://github.com/Azure/azure-sdk-for-java/pull/51354)
- [remove upfront getBody call and only call as needed (#51350)](https://github.com/Azure/azure-sdk-for-java/commit/865e8099912886c1d52fd7715b7f700b61ccd40c) - `2026-11-20T20:43:50Z` - Isabelle (@ibrandes) - PR: [[Core] Request the response body once in async RestProxy BinaryData streaming](https://github.com/Azure/azure-sdk-for-java/pull/51350)
- [Fix Milestone parameter typo in Update-GitHubIssue (#51358)](https://github.com/Azure/azure-sdk-for-java/commit/a891c9fde603403100e7707ab481737e2164ae3f) - `2026-11-20T19:42:09Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17576](https://github.com/Azure/azure-sdk-for-java/pull/51358)

### MicrosoftDocs/azure-docs-sdk-node (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [CI Update](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/c4772ee0bb02c05a62e2945393c1f955bd0b1c7b) - `2026-11-21T01:39:22Z` - docsreference@microsoft.com
- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/4c59648ff5343d40a71ef6854753dae2ad6f2b85) - `2026-11-20T23:04:49Z` - azure-sdk (@azure-sdk)
- [CI Update](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/52f850530c12441978726aaeef61c5161513f9c4) - `2026-11-20T21:14:39Z` - docsreference@microsoft.com

### dotnet/roslyn (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Deterministically tear down LSP JsonRpc pumps before AppDomain unload…](https://github.com/dotnet/roslyn/commit/da9878a16b492563fdcefc4259f2692fc07ddb24) - `2026-11-21T01:19:52Z` - Copilot (@Copilot) - PR: [Deterministically tear down LSP JsonRpc pumps before AppDomain unload in test hosts](https://github.com/dotnet/roslyn/pull/84266)
- [Write unsupported ProjectData markers during opted-in builds (#86463)](https://github.com/dotnet/roslyn/commit/51f71f06e2a1e59bf481f08edf8a497e166c28ce) - `2026-11-20T22:50:00Z` - Emanuel Fernandez Dell'Oca (@emaf) - PR: [Write unsupported ProjectData markers during opted-in builds](https://github.com/dotnet/roslyn/pull/86463)
- [Do not log missing generated output directory for Venus design-time p…](https://github.com/dotnet/roslyn/commit/3ba333703c4833834cd6669f85ce9cebb8624330) - `2026-11-20T22:02:06Z` - Tomáš Matoušek (@tmat) - PR: [Do not log missing generated output directory for Venus design-time project](https://github.com/dotnet/roslyn/pull/86533)

### MicrosoftDocs/sql-docs (3 commit(s), signal 88)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/sql-docs…](https://github.com/MicrosoftDocs/sql-docs/commit/c19cfab3bec52d6eead896900478f67468f4fe2d) - `2026-11-20T23:38:38Z` - Learn Build Service GitHub App
- [Merge pull request #38651 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/sql-docs/commit/4972eaf943cbff1169c4596bc1ee67c2a66bdf66) - `2026-11-20T23:36:35Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [docs: update PHP 5.14.0 release documentation (#38624)](https://github.com/MicrosoftDocs/sql-docs/commit/1f0979025fbb37d9e24c2b6fe0cb82fc6e9d15e8) - `2026-11-20T22:31:28Z` - David Levy (@dlevy-msft-sql)

### microsoftgraph/msgraph-beta-sdk-java (3 commit(s), signal 128)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [v6.67.1](https://github.com/microsoftgraph/msgraph-beta-sdk-java/releases/tag/v6.67.1) - `2026-11-20T22:09:02Z`
- [chore(main): release 6.67.1 (#1443)](https://github.com/microsoftgraph/msgraph-beta-sdk-java/commit/91cd1094dd9b757e7898d0e399eb6d0c81d8ebec) - `2026-11-20T22:08:33Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(main): release 6.67.1](https://github.com/microsoftgraph/msgraph-beta-sdk-java/pull/1443)
- [chore: Update Microsoft Graph Core dependency to version 3.6.6 (#1322)](https://github.com/microsoftgraph/msgraph-beta-sdk-java/commit/a8b180619a25ba787afae110baf552f3ffb09dfe) - `2026-11-20T21:15:48Z` - Ramses Sanchez-Hernandez (@ramsessanchez) - PR: [chore: Update Microsoft Graph Core dependency to version 3.6.6](https://github.com/microsoftgraph/msgraph-beta-sdk-java/pull/1322)
- [fix(ci): upgrade ESRP release task to v14 (#1442)](https://github.com/microsoftgraph/msgraph-beta-sdk-java/commit/c420c9e6d8970c951d66c0b9992920d19998b255) - `2026-11-20T20:26:27Z` - Gavin Barron (@gavinbarron) - PR: [fix(ci): upgrade ESRP release task to v14](https://github.com/microsoftgraph/msgraph-beta-sdk-java/pull/1442)

### dotnet/docs (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Document Uri parsing and UriBuilder breaking changes in .NET 11 (#56514)](https://github.com/dotnet/docs/commit/c023f59008561b0633204140aaccd803139ac435) - `2026-11-20T19:45:31Z` - surya pratap singh (@SkyDevLab) - PR: [Document Uri parsing and UriBuilder breaking changes in .NET 11](https://github.com/dotnet/docs/pull/56514)
- [🤖Copilot🤖:  Add short-form verbosity examples to dotnet command docs…](https://github.com/dotnet/docs/commit/1bea2d8730b6981d5dcf9fb5add527c95a924b62) - `2026-11-20T19:44:56Z` - Michael Yanni (@MiYanni) - PR: [Add short-form verbosity examples to dotnet command docs](https://github.com/dotnet/docs/pull/56954)
- [Create comprehensive F# 8 What's New documentation from blog post (#5…](https://github.com/dotnet/docs/commit/243250ff6ecff3a61e0f89db5d82628e248fcd98) - `2026-11-20T19:41:09Z` - Copilot (@Copilot) - PR: [Create comprehensive F# 8 What's New documentation from blog post](https://github.com/dotnet/docs/pull/50100)

### MicrosoftDocs/azure-docs-sdk-cpp (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-cpp/commit/9756c11261cfc576a64fde0b8b4b10682f8d8e0e) - `2026-11-21T16:04:29Z` - azure-sdk (@azure-sdk)
- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-cpp/commit/90c5e7800b6d54f7c4c5731b579cbae7a669a0e0) - `2026-11-20T23:21:46Z` - azure-sdk (@azure-sdk)

### Azure-Samples/Spec2Cloud (2 commit(s), signal 0)

Tags: `bot-only, samples`

- [Update templates.json [automated]](https://github.com/Azure-Samples/Spec2Cloud/commit/18a9ed3086d7abcca4f846554bd6da5792fc8635) - `2026-11-21T13:04:28Z` - github-actions[bot] (@github-actions[bot])
- [Update templates.json [automated]](https://github.com/Azure-Samples/Spec2Cloud/commit/3338f2d6ca13a39f062c5327d966b2e48507b90c) - `2026-11-21T12:06:59Z` - github-actions[bot] (@github-actions[bot])

### MicrosoftDocs/entra-docs (2 commit(s), signal 27)

Tags: `bot-only, docs, watchlist`

- [Merge pull request #15057 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/entra-docs/commit/5acb03fbf88f73e4268796fb958f2f847f2a2829) - `2026-11-21T08:37:26Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #15053 from jconley76/jconley76-sponsored-guests-r…](https://github.com/MicrosoftDocs/entra-docs/commit/1e4db57cf7553d37fcf2d3e7d3f3ef137d476ee7) - `2026-11-21T00:23:44Z` - prmerger-automator[bot] (@prmerger-automator[bot])

### dotnet/efcore (2 commit(s), signal 42)

Tags: `docs, human-authored`

- [Lift GroupBy aggregates over navigations next to operator chains (#39…](https://github.com/dotnet/efcore/commit/bfd4aefb66f128974c88ab3404e330a72f092cb8) - `2026-11-21T02:05:54Z` - SERAG AHMED (@seragAhmed) - PR: [Lift GroupBy aggregates over navigations next to operator chains](https://github.com/dotnet/efcore/pull/39648)
- [Support complex properties on owned types (#39522)](https://github.com/dotnet/efcore/commit/177ef9de4776840b69d6073835bf2b789f387500) - `2026-11-21T00:33:27Z` - Jeremy Morren (@jeremy-morren) - PR: [Support complex properties on owned types](https://github.com/dotnet/efcore/pull/39522)

### MicrosoftDocs/Advertising (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/Advertis…](https://github.com/MicrosoftDocs/Advertising/commit/bbcd67345a308825eb8ea63e50aa883a9180a6fa) - `2026-11-21T00:41:37Z` - Learn Build Service GitHub App
- [API updates 11/20 (#832)](https://github.com/MicrosoftDocs/Advertising/commit/6f4ee26d486b2ad994641c1374aa48687ebc805b) - `2026-11-21T00:40:44Z` - Rick Garitta (@rgaritta)

### OfficeDev/Office-Add-in-samples (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [[Word] Migrate and update sample (#1620)](https://github.com/OfficeDev/Office-Add-in-samples/commit/303fa9901c2068b94d10d6d80397f84eb97d8d01) - `2026-11-21T00:37:57Z` - Sam Ramon (@samantharamon) - PR: [[Word] Migrate and update sample](https://github.com/OfficeDev/Office-Add-in-samples/pull/1620)
- [[All hosts] Create skill file and refresh templates (#1621)](https://github.com/OfficeDev/Office-Add-in-samples/commit/5d17457208c3569d4ee92867f4321caa883a8050) - `2026-11-21T00:29:29Z` - Sam Ramon (@samantharamon) - PR: [[All hosts] Create skill file and refresh templates](https://github.com/OfficeDev/Office-Add-in-samples/pull/1621)

### MicrosoftDocs/azure-docs-sdk-python (2 commit(s), signal 87)

Tags: `docs, human-authored, product:Azure SDK, release-language, watchlist`

- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/dd2b2c8279251dd5060b4a9a3a5e639705eacec6) - `2026-11-20T23:06:14Z` - azure-sdk (@azure-sdk)
- [Remove azure-ai-ml package from packages-preview.json (#2084)](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/31d43f8630c8dcffd9f05911cb29919583ed564a) - `2026-11-20T22:25:48Z` - Mark Smith (@markjulmar) - PR: [Remove azure-ai-ml package from packages-preview.json](https://github.com/MicrosoftDocs/azure-docs-sdk-python/pull/2084)

### Azure/azure-sdk-for-go (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [fix condition request change detection (#28101)](https://github.com/Azure/azure-sdk-for-go/commit/80d300a44dfae42c321d49a272fb9363dfa61ad4) - `2026-11-20T22:52:37Z` - linglingye001 (@linglingye001) - PR: [Fix test failures for condition request change detection](https://github.com/Azure/azure-sdk-for-go/pull/28101)
- [Fix Milestone parameter typo in Update-GitHubIssue (#28099)](https://github.com/Azure/azure-sdk-for-go/commit/a8d6f0663daf5fc533536c00fa0ca6fffbe6690d) - `2026-11-20T19:47:02Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17576](https://github.com/Azure/azure-sdk-for-go/pull/28099)

### Azure/azure-sdk-for-js (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [[Monitor] Protect offline retry directories (#40875)](https://github.com/Azure/azure-sdk-for-js/commit/40034d1622b911bafd0d240ac390112fa12d9443) - `2026-11-20T22:14:23Z` - Jackson Weber (@JacksonWeber) - PR: [[Monitor] Protect offline retry directories](https://github.com/Azure/azure-sdk-for-js/pull/40875)
- [Sync eng/common directory with azure-sdk-tools for PR 17576 (#40877)](https://github.com/Azure/azure-sdk-for-js/commit/4a094fbe831cfaeb89ed8517a2ee4a4882ac090f) - `2026-11-20T19:58:07Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17576](https://github.com/Azure/azure-sdk-for-js/pull/40877)

### microsoft/bobsql (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Merge pull request #16 from microsoft/bw](https://github.com/microsoft/bobsql/commit/ff054500f7eab5d75693c7deba38bf0f6e3df238) - `2026-11-20T22:09:08Z` - Bob Ward (@rgward) - PR: [Add Azure SQL container demos and local indexing preparation](https://github.com/microsoft/bobsql/pull/16)
- [Add Azure SQL container demos and local indexing preparation](https://github.com/microsoft/bobsql/commit/130f46aa21be8096758fc4671f9b06c9c148657d) - `2026-11-20T22:06:47Z` - Bob Ward (@rgward) - PR: [Add Azure SQL container demos and local indexing preparation](https://github.com/microsoft/bobsql/pull/16)

### Azure-Samples/azure-functions-hosted-skills-samples (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Merge pull request #11 from pdthummar/add-cli-template-descriptor](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/commit/b0f15524f743c1fe063a4c44fa7f80d91b187818) - `2026-11-20T20:25:27Z` - Tsuyoshi Ushio (@TsuyoshiUshio) - PR: [Add template descriptor for the Python Hosted Skills Samples](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/pull/11)
- [Merge pull request #10 from Azure-Samples/decision-1-1](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/commit/1a37ac731186643387e2c6a7a2556232092a7472) - `2026-11-20T20:02:38Z` - Tsuyoshi Ushio (@TsuyoshiUshio) - PR: [Use Microsoft-Decision-1.1 in alert investigation sample](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/pull/10)

### microsoft/react-native-windows-samples (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, samples`

- [📦 Bump the all-dependencies group across 3 directories with 2 updates…](https://github.com/microsoft/react-native-windows-samples/commit/d4e999c342f35f47fbbc7611ec8d1a7a11dcad73) - `2026-11-21T18:43:17Z` - dependabot[bot] (@dependabot[bot]) - PR: [📦 Bump the all-dependencies group across 3 directories with 2 updates](https://github.com/microsoft/react-native-windows-samples/pull/1369)

### microsoft/vscode-docs (1 commit(s), signal 86)

Tags: `docs, human-authored, release-language, watchlist`

- [docs: fix typos and grammar across release notes (#10743)](https://github.com/microsoft/vscode-docs/commit/284f20ec9cfc6589f9505c1a5895056e728d355d) - `2026-11-21T18:21:11Z` - Nick Trogh (@ntrogh) - PR: [docs: fix typos and grammar across release notes](https://github.com/microsoft/vscode-docs/pull/10743)

### microsoft/WindowsAppSDK-Samples (1 commit(s), signal 86)

Tags: `human-authored, product:Azure SDK, product:PowerShell, release-language, samples, watchlist`

- [Keep hydration branch and version input in the queue form (#687)](https://github.com/microsoft/WindowsAppSDK-Samples/commit/36e10c2e780e5937090e5eb3dea3c720df03a77b) - `2026-11-21T16:42:49Z` - Scott Jones (@Scottj1s) - PR: [Keep hydration branch and version input in the queue form](https://github.com/microsoft/WindowsAppSDK-Samples/pull/687)

### SharePoint/sp-dev-docs (1 commit(s), signal 76)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Document container type limits in the central limits table (#11101)](https://github.com/SharePoint/sp-dev-docs/commit/7964a00d66e000678a328ce67bfe6711b3ec54ba) - `2026-11-21T13:17:53Z` - Reynaldo RZ (@userr2232) - PR: [Document container type limits in the central limits table](https://github.com/SharePoint/sp-dev-docs/pull/11101)

### Azure/homebrew-azd (1 commit(s), signal 86)

Tags: `human-authored, product:Azure SDK, release-language, samples, watchlist`

- [Update for azd release 1.40.0-beta.1-daily.7100116](https://github.com/Azure/homebrew-azd/commit/b10b593f562658c0bcbaaecfbdbe59852a840530) - `2026-11-21T05:45:37Z` - azure-sdk (@azure-sdk)

### microsoft/apm-sample-package (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Merge pull request #7 from microsoft/pin-transitive-drop-mode](https://github.com/microsoft/apm-sample-package/commit/45e69a68a7111bbab36a0457915d41b4b93f9acf) - `2026-11-21T05:35:00Z` - Daniel Meppiel (@danielmeppiel) - PR: [Pin the transitive skill and drop unsupported prompt mode (v1.0.1)](https://github.com/microsoft/apm-sample-package/pull/7)

### Azure/accelerator-bootstrap-modules (1 commit(s), signal 76)

Tags: `human-authored, samples, watchlist`

- [fix: compile Bicep sources in generated CI templates (#152)](https://github.com/Azure/accelerator-bootstrap-modules/commit/c58ce1009505cb0be92eb2af18eea528bd2c41f7) - `2026-11-21T04:19:55Z` - Shaik Naseeruddin (@NaseerDevops-1994) - PR: [fix: compile Bicep sources in generated CI templates](https://github.com/Azure/accelerator-bootstrap-modules/pull/152)

### microsoft/amplifier-module-provider-ollama (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Keep submitted image data out of Ollama diagnostics and public errors…](https://github.com/microsoft/amplifier-module-provider-ollama/commit/7f0e5503fdf4cf5d571f6395443cefba01242907) - `2026-11-21T02:29:44Z` - Brian Krabach (@bkrabach) - PR: [Keep submitted images private in Ollama error diagnostics](https://github.com/microsoft/amplifier-module-provider-ollama/pull/31)

### microsoft/amplifier-module-provider-vllm (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Keep submitted image data out of vLLM diagnostics and public errors (…](https://github.com/microsoft/amplifier-module-provider-vllm/commit/a4ac66f3f18fcefeb6710961ed6d7fab99e498a4) - `2026-11-21T02:29:43Z` - Brian Krabach (@bkrabach) - PR: [Keep submitted images private in vLLM error diagnostics](https://github.com/microsoft/amplifier-module-provider-vllm/pull/53)

### MicrosoftDocs/power-automate-docs (1 commit(s), signal 26)

Tags: `bot-only, docs, watchlist`

- [Resolve syncing conflicts from repo_sync_working_branch to main (#1771)](https://github.com/MicrosoftDocs/power-automate-docs/commit/1101e087427a803d892404f97903ace342dd61b8) - `2026-11-21T02:05:00Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Resolve syncing conflicts from repo_sync_working_branch to main](https://github.com/MicrosoftDocs/power-automate-docs/pull/1771)

### microsoft/voice-agent (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Support managed MAI Realtime in the voice sample (#133)](https://github.com/microsoft/voice-agent/commit/7a94596b9b4d029af5c4eb9fda936ac8a1230d09) - `2026-11-21T00:34:10Z` - szhaomsft (@szhaomsft) - PR: [Support managed MAI Realtime in the voice sample](https://github.com/microsoft/voice-agent/pull/133)

### Azure/AI-Landing-Zones (1 commit(s), signal 26)

Tags: `bot-only, docs, watchlist`

- [docs: refresh validated planner prices](https://github.com/Azure/AI-Landing-Zones/commit/4f9a74fed635eec55ba1225a2efa73e90a38301b) - `2026-11-21T00:23:00Z` - github-actions[bot] (@github-actions[bot])

### microsoft/amplifier-module-provider-azure-openai (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [test: qualify GPT-6.2 deployment aliases and Azure pricing boundaries…](https://github.com/microsoft/amplifier-module-provider-azure-openai/commit/f4b612efc66eb6b7f29672c31ac6ba447cc52f6e) - `2026-11-21T00:01:46Z` - Brian Krabach (@bkrabach) - PR: [test: qualify GPT-6.2 deployment aliases and Azure pricing boundaries](https://github.com/microsoft/amplifier-module-provider-azure-openai/pull/51)

### MicrosoftLearning/mslearn-agent-quickstart (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, training, watchlist`

- [Post-Ignite UI updates](https://github.com/MicrosoftLearning/mslearn-agent-quickstart/commit/ef77f57950ee869f8ed6017b265dfa4daedf3227) - `2026-11-20T23:48:40Z` - GraemeMalcolm (@GraemeMalcolm)

### MicrosoftLearning/mslearn-ai-fundamentals (1 commit(s), signal 86)

Tags: `human-authored, release-language, training, watchlist`

- [Added step to close preview](https://github.com/MicrosoftLearning/mslearn-ai-fundamentals/commit/75722f3b1bb75f81f66b4185265fe2c62a38025d) - `2026-11-20T23:48:28Z` - GraemeMalcolm (@GraemeMalcolm)

### MicrosoftDocs/azure-docs-sdk-java (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/0fae8bf58bd60c47ddeb2d4a966f7bb81384f5fb) - `2026-11-20T23:42:32Z` - azure-sdk (@azure-sdk)

### microsoft/BuildXL (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Merged PR 974538: Overlap BuildXL log upload with the build - xlg sta…](https://github.com/microsoft/BuildXL/commit/1f61f59905bd5b905474b27714c6dfdb17d95aa8) - `2026-11-20T23:40:01Z` - Viv Siless

### Azure/azure-sdk (1 commit(s), signal 26)

Tags: `bot-only, docs, product:Azure SDK, watchlist`

- [Fix Milestone parameter typo in Update-GitHubIssue (#10421)](https://github.com/Azure/azure-sdk/commit/cb164c66ce392a3c560ef2fac56bc28fbc99b9d5) - `2026-11-20T22:27:30Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17576](https://github.com/Azure/azure-sdk/pull/10421)

### microsoft/vscode-extension-samples (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [chore: pin actions (#1320)](https://github.com/microsoft/vscode-extension-samples/commit/b284b915f1afbc8835bccda2ce4e198c23b719f0) - `2026-11-20T22:02:01Z` - Raymond Zhao (@rzhao271) - PR: [chore: pin actions](https://github.com/microsoft/vscode-extension-samples/pull/1320)

### Azure/awesome-azd (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Add SAHAYA relief-claim adjudication template (#1129)](https://github.com/Azure/awesome-azd/commit/64a829146a76527018f2fa2c4620f6219352d7f1) - `2026-11-20T21:29:24Z` - hemarina (@hemarina) - PR: [Add SAHAYA relief-claim adjudication template](https://github.com/Azure/awesome-azd/pull/1129)

### MicrosoftDocs/msteams-docs (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Updates to file upload/download docs for tempAuth deprecation (#14746)](https://github.com/MicrosoftDocs/msteams-docs/commit/0d8db11778699492c87bf4eb1a12c4652050fce3) - `2026-11-20T21:06:17Z` - prrathna-msft (@prrathna-msft) - PR: [Updates to file upload/download docs for tempAuth deprecation](https://github.com/MicrosoftDocs/msteams-docs/pull/14746)

### Azure/azure-sdk-for-cpp (1 commit(s), signal 66)

Tags: `bot-only, docs, product:Azure SDK, release, watchlist`

- Release: [azure-core-amqp_1.0.0-beta.15](https://github.com/Azure/azure-sdk-for-cpp/releases/tag/azure-core-amqp_1.0.0-beta.15) - `2026-11-21T15:53:36Z`
- [Fix Milestone parameter typo in Update-GitHubIssue (#7570)](https://github.com/Azure/azure-sdk-for-cpp/commit/9d32f08547e65270056dc6d7ffd0acd9f732a639) - `2026-11-20T21:01:33Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17576](https://github.com/Azure/azure-sdk-for-cpp/pull/7570)

### Azure/azure-dev (1 commit(s), signal 76)

Tags: `human-authored, samples, watchlist`

- [docs: define naming for new azd environment controls (#10996)](https://github.com/Azure/azure-dev/commit/dc9dd2095f4c6f6c752e9c29ec676f2fbdae9b43) - `2026-11-20T20:50:56Z` - Kristen Womack (@kristenwomack) - PR: [Document naming for new azd environment variables](https://github.com/Azure/azure-dev/pull/10996)

### Azure-Samples/functions-quickstart-dotnet-azd-service-bus (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add synthesis descriptor for the Service Bus QuickStart (#6)](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-service-bus/commit/96d15ff03bffa1ce5fd63ffb23193fe8f8281563) - `2026-11-20T20:05:58Z` - pdthummar (@pdthummar) - PR: [Add synthesis descriptor for the Service Bus QuickStart](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-service-bus/pull/6)

### microsoftgraph/msgraph-sdk-go (1 commit(s), signal 76)

Tags: `bot-only, docs, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [v1.107.0](https://github.com/microsoftgraph/msgraph-sdk-go/releases/tag/v1.107.0) - `2026-11-20T19:56:36Z`
- [chore(main): release 1.107.0 (#1074)](https://github.com/microsoftgraph/msgraph-sdk-go/commit/afc24b90c0218dc852ec075aa1c31c85e9751136) - `2026-11-20T19:56:11Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(main): release 1.107.0](https://github.com/microsoftgraph/msgraph-sdk-go/pull/1074)

</details>
