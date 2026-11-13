# Microsoft Ecosystem Daily Brief - 2026-11-13

> Status: Fresh at generation. Current freshness is tracked in `reports/status.json`.
> Generated: 2026-11-13 20:32 UTC - Window: 25.6h from 2026-11-12 18:57 UTC to 2026-11-13 20:32 UTC.
> 119 repo(s) moved - 641 commit(s) - 28 release item(s) - 25 high-signal repo(s).

## Plain-English Summary

- Azure, Microsoft Graph led the visible product-area activity in this window.
- 28 release item(s) were detected during the window.
- Security-related changes appeared in Azure-Samples/AzureLocal, microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning, MicrosoftDocs/learn.
- Start with human-authored changes in Azure-Samples/AzureLocal, microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning, MicrosoftDocs/learn, microsoftgraph/microsoft-graph-docs-contrib.
- 114 event(s) look automated, bot-heavy, dependency, or generated; review the curated sections before raw volume.

## Headline Metrics

| Metric | Value |
| --- | ---: |
| Inventory repositories | 16787 |
| Repositories after filters | 2571 |
| `pushed_at` candidates | 200 |
| Enrichment candidates | 200 |
| Repositories with movement | 119 |
| Default-branch commits | 641 |

## What Changed That Matters

| Repository | Score | Change | Actor | Noise | Headline | Time |
| --- | ---: | --- | --- | --- | --- | --- |
| [Azure-Samples/AzureLocal](https://github.com/Azure-Samples/AzureLocal) | 100 | security_fix | human | low | [Security baseline 2610: add Validation commands for the Secured-core rows](https://github.com/Azure-Samples/AzureLocal/pull/113) | `2026-11-13T19:42:32Z` |
| [Azure-Samples/AzureLocal](https://github.com/Azure-Samples/AzureLocal) | 100 | security_fix | human | low | [Fix Azure Local 2610 security baseline CSVs](https://github.com/Azure-Samples/AzureLocal/pull/111) | `2026-11-13T17:52:42Z` |
| [microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning](https://github.com/microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning) | 100 | security_fix | human | low | [Harden demand forecasting template identity resolution and relay authentication](https://github.com/microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning/pull/25) | `2026-11-13T17:49:08Z` |
| [MicrosoftDocs/learn](https://github.com/MicrosoftDocs/learn) | 100 | security_fix | human | low | [Add module: Plan integrated security operations with Microsoft Defend…](https://github.com/MicrosoftDocs/learn/commit/e11f34ed69712e5030961860572e3d4d0c3005dc) | `2026-11-13T13:38:17Z` |
| [microsoftgraph/microsoft-graph-docs-contrib](https://github.com/microsoftgraph/microsoft-graph-docs-contrib) | 100 | security_fix | human | low | [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10094) | `2026-11-13T00:01:50Z` |
| [Azure/kars](https://github.com/Azure/kars) | 100 | security_fix | human | low | [Remediate crypto-bigint timing advisory](https://github.com/Azure/kars/pull/620) | `2026-11-12T21:17:21Z` |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 100 | security_fix | human | low | [Add GitHubActionsCredential to azure_identity](https://github.com/Azure/azure-sdk-for-rust/pull/5588) | `2026-11-12T19:06:44Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 100 | release | human | low | [Fix SDK PR handoff in Python release completion](https://github.com/Azure/azure-sdk-for-python/pull/49941) | `2026-11-13T19:56:23Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 100 | release | human | low | [Pass the auto-release SDK PR to release completion](https://github.com/Azure/azure-sdk-for-java/pull/51224) | `2026-11-13T19:48:15Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | 100 | release | human | low | [Pass the auto-release SDK PR to release completion](https://github.com/Azure/azure-sdk-for-go/pull/28020) | `2026-11-13T19:47:53Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 100 | release | human | low | [Pass the auto-release SDK PR to release completion](https://github.com/Azure/azure-sdk-for-js/pull/40770) | `2026-11-13T19:47:41Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 100 | release | human | low | [Pass the auto-release SDK PR to release completion](https://github.com/Azure/azure-sdk-for-net/pull/64863) | `2026-11-13T19:47:35Z` |
| [microsoft/Biodiversity](https://github.com/microsoft/Biodiversity) | 100 | release | human | low | [docs: correct historical release details](https://github.com/microsoft/Biodiversity/pull/672) | `2026-11-13T19:00:01Z` |
| [microsoft/Biodiversity](https://github.com/microsoft/Biodiversity) | 100 | release | human | low | [docs: refresh hub guidance and release history](https://github.com/microsoft/Biodiversity/pull/671) | `2026-11-13T18:55:57Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 100 | release | unknown | low | [com.azure+azure-security-keyvault-keys_4.13.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-security-keyvault-keys_4.13.0) | `2026-11-13T18:53:05Z` |

## Product Areas

| Product area | Signal | Repos | Events | Releases | Security | Top links |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Azure | 151 | 54 | 178 | 24 | 8 | [Security baseline 2610: add Validation commands for the Secured-core rows](https://github.com/Azure-Samples/AzureLocal/pull/113); [Fix Azure Local 2610 security baseline CSVs](https://github.com/Azure-Samples/AzureLocal/pull/111); [Harden demand forecasting template identity resolution and relay authentication](https://github.com/microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning/pull/25) |
| Unmapped Activity | 47 | 20 | 56 | 3 | 1 | [Add module: Plan integrated security operations with Microsoft Defend…](https://github.com/MicrosoftDocs/learn/commit/e11f34ed69712e5030961860572e3d4d0c3005dc); [docs: correct historical release details](https://github.com/microsoft/Biodiversity/pull/672); [docs: refresh hub guidance and release history](https://github.com/microsoft/Biodiversity/pull/671) |
| Microsoft Graph | 35 | 16 | 57 | 1 | 1 | [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10094); [v0.26.0](https://github.com/microsoft/kiota-ruby/releases/tag/v0.26.0); [chore(main): release 0.26.0](https://github.com/microsoft/kiota-ruby/pull/216) |
| .NET | 25 | 11 | 33 | 0 | 0 | [[automated] Merge branch 'release/11.0' => 'main'](https://github.com/dotnet/efcore/pull/39516); [Fix Helix test failures](https://github.com/dotnet/efcore/pull/39635); [Fix MCP client quickstart failing on Linux and macOS](https://github.com/dotnet/docs/pull/56797) |
| Identity | 15 | 4 | 15 | 0 | 0 | [Windows: setup wizard, TPM key lifecycle, and runtime fixes](https://github.com/microsoft/entrabot/pull/149); [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/61c96140b602cd44a3978da72b67766aeacb5590); [Refresh admin center content (#8156)](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/80518d538879211bac90ec42438f1c9d1dd5d779) |
| PowerShell | 11 | 6 | 11 | 0 | 0 | [feat(commands): Add auto mode, pr-loop, and pr-sweep PR commands](https://github.com/microsoft/finops-toolkit/pull/2402); [fix(finops-hub): Paginate Azure Resource Graph queries past 1,000 rows](https://github.com/microsoft/finops-toolkit/pull/2330); [Hydrate samples across .NET toolchains](https://github.com/microsoft/WindowsAppSDK-Samples/pull/686) |
| Windows | 9 | 5 | 11 | 0 | 0 | [.NET Template Localization (Part 1): Add .NET template localization handoffs and status analysis](https://github.com/microsoft/WindowsAppSDK/pull/6964); [Deployment: derive Main/Singleton short tag via canonical v2 helper (experimentalA fix)](https://github.com/microsoft/WindowsAppSDK/pull/6657); [Merging changes synced from https://github.com/MicrosoftDocs/windowss…](https://github.com/MicrosoftDocs/windowsserverdocs/commit/cceb56b597a2c1629e00ab6abf6604659c000974) |
| Developer Tools | 5 | 1 | 5 | 0 | 0 | [Update release note template for highlights video](https://github.com/microsoft/vscode-docs/pull/10647); [Update Insiders release notes](https://github.com/microsoft/vscode-docs/pull/10646) |

## Today's Top Links

| Priority | Repository | Why read it |
| ---: | --- | --- |
| 1 | [Azure-Samples/AzureLocal](https://github.com/Azure-Samples/AzureLocal) | [Security-related change: Security baseline 2610: add Validation commands for the Secured-core rows](https://github.com/Azure-Samples/AzureLocal/pull/113) |
| 2 | [microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning](https://github.com/microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning) | [Security-related change: Harden demand forecasting template identity resolution and relay authentication](https://github.com/microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning/pull/25) |
| 3 | [MicrosoftDocs/learn](https://github.com/MicrosoftDocs/learn) | [Security-related change: Add module: Plan integrated security operations with Microsoft Defend…](https://github.com/MicrosoftDocs/learn/commit/e11f34ed69712e5030961860572e3d4d0c3005dc) |
| 4 | [microsoftgraph/microsoft-graph-docs-contrib](https://github.com/microsoftgraph/microsoft-graph-docs-contrib) | [Security-related change: Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10094) |
| 5 | [Azure/kars](https://github.com/Azure/kars) | [Security-related change: Remediate crypto-bigint timing advisory](https://github.com/Azure/kars/pull/620) |
| 6 | [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | [Security-related change: Add GitHubActionsCredential to azure_identity](https://github.com/Azure/azure-sdk-for-rust/pull/5588) |
| 7 | [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [Release activity: Fix SDK PR handoff in Python release completion](https://github.com/Azure/azure-sdk-for-python/pull/49941) |
| 8 | [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [Release activity: Pass the auto-release SDK PR to release completion](https://github.com/Azure/azure-sdk-for-java/pull/51224) |

## Noise and Automation

- 114 event(s) look automated, bot-heavy, dependency, generated, or medium/high noise.
- Top noisy repositories: microsoft/kiota-http-go, microsoft/kiota-python, microsoft/kiota-java, microsoftgraph/msgraph-snippets-go, microsoft/kiota-samples.
- Noise mix: Dependency: 45, SDK: 31, Docs: 29, CI/Infra: 6, Sample: 2, Release: 1.

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
| Count batches | 6 |
| Detail batches | 4 |
| Repos counted | 200 |
| Repos enriched | 119 |

</details>

<details>
<summary>Show supporting signal, release, and lifecycle tables</summary>

## High-Signal Items

| Repository | Score | Tags |
| --- | ---: | --- |
| [Azure/kars](https://github.com/Azure/kars) | 143 | docs, human-authored, release, security, watchlist |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 139 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 138 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | 138 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime) | 136 | human-authored, product:Microsoft Graph, release, samples, watchlist |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 136 | docs, human-authored, release, release-language, watchlist |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 135 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [microsoft/kiota-ruby](https://github.com/microsoft/kiota-ruby) | 134 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 134 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 127 | human-authored, release, release-language, samples, watchlist |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 125 | human-authored, product:Azure AI, release, samples, watchlist |
| [MicrosoftDocs/learn](https://github.com/MicrosoftDocs/learn) | 115 | docs, human-authored, security, watchlist |
| [Azure-Samples/AzureLocal](https://github.com/Azure-Samples/AzureLocal) | 105 | human-authored, samples, security, watchlist |
| [microsoftgraph/microsoft-graph-docs-contrib](https://github.com/microsoftgraph/microsoft-graph-docs-contrib) | 104 | docs, human-authored, product:Azure AI, product:Microsoft Graph, security, watchlist |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 103 | docs, human-authored, product:Azure SDK, security, watchlist |

## Watchlist Hits

| Repository | Score | Matches |
| --- | ---: | --- |
| [Azure/kars](https://github.com/Azure/kars) | 143 | orgs: Azure; keywords: security |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 139 | products: Azure SDK; repos: Azure/azure-sdk-for-java; orgs: Azure; keywords: release, sdk |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 138 | products: Azure SDK; repos: Azure/azure-sdk-for-js; orgs: Azure; keywords: copilot, release, sdk |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | 138 | products: Azure SDK; orgs: Azure; keywords: copilot, release, sdk |
| [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime) | 136 | products: Microsoft Graph; keywords: graph |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 136 | orgs: Azure; keywords: release |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 135 | products: Azure SDK; repos: Azure/azure-sdk-for-python; orgs: Azure; keywords: release, sdk |
| [microsoft/kiota-ruby](https://github.com/microsoft/kiota-ruby) | 134 | products: Microsoft Graph, Azure SDK; keywords: graph, kiota, release, sdk |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 134 | products: Azure SDK; repos: Azure/azure-sdk-for-net; orgs: Azure; keywords: release, sdk |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 127 | keywords: release |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 125 | products: Azure AI; orgs: Azure; keywords: foundry |
| [MicrosoftDocs/learn](https://github.com/MicrosoftDocs/learn) | 115 | orgs: MicrosoftDocs; keywords: security |
| [Azure-Samples/AzureLocal](https://github.com/Azure-Samples/AzureLocal) | 105 | keywords: security |
| [microsoftgraph/microsoft-graph-docs-contrib](https://github.com/microsoftgraph/microsoft-graph-docs-contrib) | 104 | products: Azure AI, Microsoft Graph; orgs: microsoftgraph; keywords: agent, graph, security |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 103 | products: Azure SDK; orgs: Azure; keywords: copilot, sdk |

## Releases

| Repository | Release | Published |
| --- | --- | --- |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure+azure-security-keyvault-keys_4.13.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-security-keyvault-keys_4.13.0) | `2026-11-13T18:53:05Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure+azure-security-keyvault-administration_4.10.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-security-keyvault-administration_4.10.0) | `2026-11-13T18:52:50Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/storage/azdatalake/v1.8.0-beta.1](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/storage/azdatalake/v1.8.0-beta.1) | `2026-11-13T18:44:17Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-mgmt-cognitiveservices_15.0.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-cognitiveservices_15.0.0) | `2026-11-13T18:12:31Z` |
| [microsoft/dbt-fabricspark](https://github.com/microsoft/dbt-fabricspark) | [v1.13.13](https://github.com/microsoft/dbt-fabricspark/releases/tag/v1.13.13) | `2026-11-13T15:03:53Z` |
| [Azure/kars](https://github.com/Azure/kars) | [v0.2.0-beta.6](https://github.com/Azure/kars/releases/tag/v0.2.0-beta.6) | `2026-11-13T14:10:20Z` |
| [microsoft/kiota-ruby](https://github.com/microsoft/kiota-ruby) | [v0.26.0](https://github.com/microsoft/kiota-ruby/releases/tag/v0.26.0) | `2026-11-13T12:38:27Z` |
| [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime) | [ONNX Runtime v1.32.0](https://github.com/microsoft/onnxruntime/releases/tag/v1.32.0) | `2026-11-13T09:36:22Z` |
| [microsoft/amplifier-persona-workshop](https://github.com/microsoft/amplifier-persona-workshop) | [Persona Workshop 0.7.2](https://github.com/microsoft/amplifier-persona-workshop/releases/tag/v0.7.2) | `2026-11-13T09:29:57Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [migrate 3.0.0b7](https://github.com/Azure/azure-cli-extensions/releases/tag/migrate-3.0.0b7) | `2026-11-13T07:16:39Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/resourcemanager/containerservice/armcontainerservice/v9.8.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/containerservice/armcontainerservice/v9.8.0) | `2026-11-13T04:49:16Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-containerservice_25.8.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-containerservice_25.8.0) | `2026-11-13T04:48:09Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-aiinfraoptimization_1.0.0-beta.2](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-aiinfraoptimization_1.0.0-beta.2) | `2026-11-13T04:32:45Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure.resourcemanager+azure-resourcemanager-cognitiveservices_1.5.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-cognitiveservices_1.5.0) | `2026-11-13T04:30:48Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/resourcemanager/cognitiveservices/armcognitiveservices/v4.0.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/cognitiveservices/armcognitiveservices/v4.0.0) | `2026-11-13T03:56:52Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [fleet 1.12.0](https://github.com/Azure/azure-cli-extensions/releases/tag/fleet-1.12.0) | `2026-11-13T03:54:08Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-cognitiveservices_9.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-cognitiveservices_9.0.0) | `2026-11-13T03:53:38Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure.resourcemanager+azure-resourcemanager-iothub_1.4.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-iothub_1.4.0) | `2026-11-13T03:52:53Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-iothub_7.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-iothub_7.0.0) | `2026-11-13T03:18:50Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/resourcemanager/iothub/armiothub/v2.0.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/iothub/armiothub/v2.0.0) | `2026-11-13T03:16:14Z` |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | [Azure Sandbox v6.0.9](https://github.com/Azure-Samples/azuresandbox/releases/tag/v6.0.9) | `2026-11-13T02:20:22Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure+azure-ai-projects_2.10.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-ai-projects_2.10.0) | `2026-11-13T02:16:20Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.AI.Extensions.OpenAI_3.0.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.AI.Extensions.OpenAI_3.0.0) | `2026-11-13T00:20:39Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [managednetworkfabric 10.0.0b4](https://github.com/Azure/azure-cli-extensions/releases/tag/managednetworkfabric-10.0.0b4) | `2026-11-12T23:25:56Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-keyvault-administration_4.8.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-keyvault-administration_4.8.0) | `2026-11-12T23:13:58Z` |

## Repository Lifecycle

| Change | Count |
| --- | ---: |
| archived_changed | 1 |
| category_changed | 1 |
| default_branch_changed | 0 |
| fork_changed | 0 |
| new_repos | 7 |
| removed_repos | 0 |

## Category Summary

| Category | Repositories |
| --- | ---: |
| docs | 73 |
| samples | 38 |
| training | 8 |

## Organization Summary

| Org | Repositories |
| --- | ---: |
| microsoft | 34 |
| MicrosoftDocs | 23 |
| Azure | 20 |
| Azure-Samples | 20 |
| dotnet | 10 |
| microsoftgraph | 6 |
| MicrosoftLearning | 3 |
| OfficeDev | 3 |

</details>

<details>
<summary>Show raw repository activity</summary>

## Busiest Repositories

| Repository | Signal | Category | Commits | Releases | Newest commit |
| --- | ---: | --- | ---: | ---: | --- |
| [Azure/kars](https://github.com/Azure/kars) | 143 | docs | 3 | 1 | `2026-11-12T22:02:10Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 139 | docs | 14 | 5 | `2026-11-13T20:00:55Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 138 | docs | 13 | 4 | `2026-11-13T20:32:09Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | 138 | docs | 13 | 4 | `2026-11-13T20:20:07Z` |
| [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime) | 136 | samples | 21 | 1 | `2026-11-13T20:16:07Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 136 | docs | 11 | 4 | `2026-11-13T07:15:38Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 135 | docs | 10 | 3 | `2026-11-13T20:15:56Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 134 | docs | 9 | 1 | `2026-11-13T19:47:35Z` |
| [microsoft/kiota-ruby](https://github.com/microsoft/kiota-ruby) | 134 | docs | 9 | 1 | `2026-11-13T19:29:11Z` |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 127 | samples | 2 | 1 | `2026-11-13T00:43:43Z` |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 125 | samples | 10 | 1 | `2026-11-13T10:00:13Z` |
| [MicrosoftDocs/learn](https://github.com/MicrosoftDocs/learn) | 115 | docs | 15 | 0 | `2026-11-13T18:22:22Z` |
| [Azure-Samples/AzureLocal](https://github.com/Azure-Samples/AzureLocal) | 105 | samples | 5 | 0 | `2026-11-13T19:42:32Z` |
| [microsoftgraph/microsoft-graph-docs-contrib](https://github.com/microsoftgraph/microsoft-graph-docs-contrib) | 104 | docs | 4 | 0 | `2026-11-13T00:42:35Z` |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 103 | docs | 3 | 0 | `2026-11-13T02:08:33Z` |
| [microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning](https://github.com/microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning) | 102 | samples | 2 | 0 | `2026-11-13T17:49:08Z` |
| [MicrosoftDocs/architecture-center](https://github.com/MicrosoftDocs/architecture-center) | 100 | docs | 26 | 0 | `2026-11-13T18:31:50Z` |
| [Azure/ResiliencyInAzure](https://github.com/Azure/ResiliencyInAzure) | 100 | docs | 25 | 0 | `2026-11-13T04:43:37Z` |
| [microsoft/Biodiversity](https://github.com/microsoft/Biodiversity) | 100 | docs | 15 | 0 | `2026-11-13T19:00:01Z` |
| [MicrosoftDocs/dynamics-365-unified-operations-public](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public) | 95 | docs | 10 | 0 | `2026-11-13T19:06:50Z` |

## Repository Details

### dotnet/android-api-docs (87 commit(s), signal 65)

Tags: `docs, human-authored`

- [Document supported Android.Media APIs (#1465)](https://github.com/dotnet/android-api-docs/commit/5d7b9f92cfb90ebf8c8bbdc0400e1d74babc7564) - `2026-11-13T18:47:36Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Document supported Android.Media APIs](https://github.com/dotnet/android-api-docs/pull/1465)
- [Document supported Android.Content.PM APIs (#1466)](https://github.com/dotnet/android-api-docs/commit/2052c5a636306762cab2e08b717235bfd9101f85) - `2026-11-13T17:02:15Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Document supported Android.Content.PM APIs](https://github.com/dotnet/android-api-docs/pull/1466)
- [Complete HTTP connection parameter summaries (#1458)](https://github.com/dotnet/android-api-docs/commit/ef326628f1edf8611b65d87f9a6d2979f5ad7e0d) - `2026-11-13T16:23:37Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Complete Org.Apache.Http.Conn.Params documentation](https://github.com/dotnet/android-api-docs/pull/1458)
- [Complete Javax.Xml.Datatype summaries (#1457)](https://github.com/dotnet/android-api-docs/commit/60983786ec10cf0c80d2e308c40b1c9d75a4d496) - `2026-11-13T16:23:19Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Complete Javax.Xml.Datatype documentation summaries](https://github.com/dotnet/android-api-docs/pull/1457)
- [Complete Java.Util.Streams gatherer documentation (#1459)](https://github.com/dotnet/android-api-docs/commit/a4c775842f1f0f7bb23bfe8996510fa47ff57ba8) - `2026-11-13T16:22:52Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Complete Java.Util.Streams gatherer documentation](https://github.com/dotnet/android-api-docs/pull/1459)

### dotnet/runtime (26 commit(s), signal 65)

Tags: `docs, human-authored`

- [JIT: forward byref-exposed stores to same-address loads in value numb…](https://github.com/dotnet/runtime/commit/50a0c6423336dfa9f887e9aac74686070cfe6775) - `2026-11-13T20:30:38Z` - Larry Ewing (@lewing) - PR: [JIT: forward byref-exposed stores to same-address loads in value numbering](https://github.com/dotnet/runtime/pull/136612)
- [Fix BGC allocation context accounting (#134855)](https://github.com/dotnet/runtime/commit/c3bb0a49ba5857defddf2281beda9777a268c98b) - `2026-11-13T19:03:50Z` - Konrad Kokosa (@kkokosa) - PR: [Fix BGC allocation context accounting](https://github.com/dotnet/runtime/pull/134855)
- [[Wasm] Elide singleton virtual IP stores (#137465)](https://github.com/dotnet/runtime/commit/1f6f3c0681e68238f485d2da984c4b2d899443d5) - `2026-11-13T18:47:23Z` - David Wrighton (@davidwrighton) - PR: [[Wasm] Elide singleton virtual IP stores](https://github.com/dotnet/runtime/pull/137465)
- [Improve the performance of Process.HandleCount on Linux (#136630)](https://github.com/dotnet/runtime/commit/a6f96e58c1163961f04d4218c824160ade1cf3f2) - `2026-11-13T17:24:03Z` - Martin Costello (@martincostello) - PR: [Improve the performance of Process.HandleCount on Linux](https://github.com/dotnet/runtime/pull/136630)
- [[wasm] Respect disabled debugger support in CoreCLR layout checks (#1…](https://github.com/dotnet/runtime/commit/00178ee32a0d46acf976f96f1d6fa4a65f8dfc74) - `2026-11-13T16:35:52Z` - Pavel Savara (@pavelsavara) - PR: [[wasm] Respect disabled debugger support in CoreCLR layout checks](https://github.com/dotnet/runtime/pull/137496)

### MicrosoftDocs/architecture-center (26 commit(s), signal 100)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #17387 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/architecture-center/commit/c26c4eb086f6443a8e1e81cc59faa683207e1b70) - `2026-11-13T18:31:50Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #17385 from MicrosoftDocs/prep-for-v1-2-3](https://github.com/MicrosoftDocs/architecture-center/commit/4a5a69daf7f45b93295cc90249a377b9183d5bad) - `2026-11-13T17:41:46Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Remove strict (in aw.json already), update routing.](https://github.com/MicrosoftDocs/architecture-center/commit/d555af3e516cfa7e34f909d54604bb060edb19a7) - `2026-11-13T17:20:17Z` - Chad Kittel (@ckittel)
- [Merge pull request #17384 from MicrosoftDocs/compute-update](https://github.com/MicrosoftDocs/architecture-center/commit/503be694111fb373adaf1d7dbf2fdb790dc1ad8d) - `2026-11-13T16:10:58Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Clarify](https://github.com/MicrosoftDocs/architecture-center/commit/b82ce5bf879f15154bb27060bfe28170ee2aca83) - `2026-11-13T15:58:16Z` - Chad Kittel (@ckittel)

### Azure/ResiliencyInAzure (25 commit(s), signal 100)

Tags: `docs, human-authored, watchlist`

- [Reorder tutorial sections in README](https://github.com/Azure/ResiliencyInAzure/commit/4d564c9ce3b812fc8645a58effe9d8f26062fe61) - `2026-11-13T04:43:37Z` - kalyaninamuduri (@kalyaninamuduri)
- [Update README.md](https://github.com/Azure/ResiliencyInAzure/commit/f03a7b5a4f48667af6f6e0969923c5456913e5f0) - `2026-11-13T04:42:16Z` - kalyaninamuduri (@kalyaninamuduri)
- [Update Create Usage Plan for Service Group.md](https://github.com/Azure/ResiliencyInAzure/commit/906807a8b8c4aba4a21886ed742acf8ca1bfc4e9) - `2026-11-13T04:39:51Z` - kalyaninamuduri (@kalyaninamuduri)
- [Add files via upload](https://github.com/Azure/ResiliencyInAzure/commit/819c2e95c462146897a96295d84f70a1ce8737fb) - `2026-11-13T04:33:17Z` - kalyaninamuduri (@kalyaninamuduri)
- [Create Usage Plan for Service Group document](https://github.com/Azure/ResiliencyInAzure/commit/f6e6d91476ddefebc38f7db3f7b6464985af4115) - `2026-11-13T04:17:01Z` - kalyaninamuduri (@kalyaninamuduri)

### microsoft/onnxruntime (21 commit(s), signal 136)

Tags: `human-authored, product:Microsoft Graph, release, samples, watchlist`

- Release: [ONNX Runtime v1.32.0](https://github.com/microsoft/onnxruntime/releases/tag/v1.32.0) - `2026-11-13T09:36:22Z`
- [Fix FLOAT16 tensor attribute serialization in OrtGraphToProto (#33921)](https://github.com/microsoft/onnxruntime/commit/6f07ceeaddfb00835d10b0fc21db83a359246548) - `2026-11-13T20:16:07Z` - Georgij Tsarin (@crystarm) - PR: [Fix FLOAT16 tensor attribute serialization in OrtGraphToProto](https://github.com/microsoft/onnxruntime/pull/33921)
- [Skip PackedAttention random input generation when CUDA is unavailable…](https://github.com/microsoft/onnxruntime/commit/bdca9e69f0894c720d75967b00f0fd175a1b5a9a) - `2026-11-13T20:15:57Z` - eserscor (@eserscor) - PR: [Skip PackedAttention random input generation when CUDA is unavailable](https://github.com/microsoft/onnxruntime/pull/34199)
- [Split DirectML CI builds from GPU tests (#34080)](https://github.com/microsoft/onnxruntime/commit/c9a334c287cb96170dc32ff79ff5150e67635cd5) - `2026-11-13T17:29:44Z` - eserscor (@eserscor) - PR: [Split DirectML CI builds from GPU tests](https://github.com/microsoft/onnxruntime/pull/34080)
- [Avoid redundant apt installs in Android CI (#34116)](https://github.com/microsoft/onnxruntime/commit/6080d7c7cc598db70335be28c7946c429dfb2671) - `2026-11-13T16:52:22Z` - eserscor (@eserscor) - PR: [Avoid redundant apt installs in Android CI](https://github.com/microsoft/onnxruntime/pull/34116)
- [[CUDA] Optimize MoEPacked GGUF offload 3-stage prefill pipeline and F…](https://github.com/microsoft/onnxruntime/commit/e3a11531634625b0cac4358f93ff12f17d231290) - `2026-11-13T15:08:00Z` - Tianlei Wu (@tianleiwu) - PR: [[CUDA] Optimize MoEPacked GGUF offload 3-stage prefill pipeline and F16C/Batch4/40-core cold decode](https://github.com/microsoft/onnxruntime/pull/34114)

### microsoft/kiota-samples (18 commit(s), signal 93)

Tags: `docs, human-authored, product:Microsoft Graph, watchlist`

- [Merge pull request #9367 from microsoft/dependabot/go_modules/msgraph…](https://github.com/microsoft/kiota-samples/commit/49c2cdb0b70156da7223fc88049f75e162e8a4fb) - `2026-11-13T15:08:55Z` - Vincent Biret (@baywet) - PR: [build(deps): bump the kiota-dependencies group in /msgraph-mail/go with 2 updates](https://github.com/microsoft/kiota-samples/pull/9367)
- [Merge pull request #9368 from microsoft/dependabot/go_modules/get-sta…](https://github.com/microsoft/kiota-samples/commit/fdf646f59f88e7458b42f0ce3c570f561e133c20) - `2026-11-13T15:08:49Z` - Vincent Biret (@baywet) - PR: [build(deps): bump github.com/microsoft/kiota-serialization-form-go from 1.1.6 to 1.1.7 in /get-started/azure-auth/go in the kiota-dependencies group](https://github.com/microsoft/kiota-samples/pull/9368)
- [Merge pull request #9369 from microsoft/dependabot/go_modules/petstor…](https://github.com/microsoft/kiota-samples/commit/dd4714083602d24260928a7c56bd954d8fdcf3f7) - `2026-11-13T15:08:42Z` - Vincent Biret (@baywet) - PR: [build(deps): bump the kiota-dependencies group in /petstore/go with 2 updates](https://github.com/microsoft/kiota-samples/pull/9369)
- [Merge pull request #9370 from microsoft/dependabot/go_modules/get-sta…](https://github.com/microsoft/kiota-samples/commit/30a5dec67b87430c0bd385ed55bfaa1244c0296f) - `2026-11-13T15:08:35Z` - Vincent Biret (@baywet) - PR: [build(deps): bump github.com/microsoft/kiota-serialization-form-go from 1.1.6 to 1.1.7 in /get-started/quickstart/go in the kiota-dependencies group](https://github.com/microsoft/kiota-samples/pull/9370)
- [Merge pull request #9371 from microsoft/dependabot/bundler/get-starte…](https://github.com/microsoft/kiota-samples/commit/94424eae56ff77bb5dde6008e9b6caa874af5eaf) - `2026-11-13T15:08:29Z` - Vincent Biret (@baywet) - PR: [build(deps): bump the kiota-dependencies group in /get-started/azure-auth/ruby with 7 updates](https://github.com/microsoft/kiota-samples/pull/9371)

### microsoft/Biodiversity (15 commit(s), signal 100)

Tags: `docs, human-authored, release-language, watchlist`

- [Merge pull request #672 from microsoft/docs/release-history-corrections](https://github.com/microsoft/Biodiversity/commit/82b20f3e2248e84f6ae10ca85c08e460b8661ae0) - `2026-11-13T19:00:01Z` - Zhongqi Miao (@zhmiao) - PR: [docs: correct historical release details](https://github.com/microsoft/Biodiversity/pull/672)
- [docs: correct historical release details](https://github.com/microsoft/Biodiversity/commit/2ab51de3d329b536383dc0f1a50e7110df16cd82) - `2026-11-13T18:58:55Z` - zhmiao (@zhmiao) - PR: [docs: correct historical release details](https://github.com/microsoft/Biodiversity/pull/672)
- [Merge pull request #671 from microsoft/docs/current-project-information](https://github.com/microsoft/Biodiversity/commit/5d7089d8b5625173b55c2a4c82222aebe9abc5a5) - `2026-11-13T18:55:57Z` - Zhongqi Miao (@zhmiao) - PR: [docs: refresh hub guidance and release history](https://github.com/microsoft/Biodiversity/pull/671)
- [docs: refresh hub guidance and release history](https://github.com/microsoft/Biodiversity/commit/bbca5552c380f5d98c186281c7afb418ad41169b) - `2026-11-13T18:53:38Z` - zhmiao (@zhmiao) - PR: [docs: refresh hub guidance and release history](https://github.com/microsoft/Biodiversity/pull/671)
- [Merge pull request #670 from microsoft/docs/project-catalogue](https://github.com/microsoft/Biodiversity/commit/5bd77c32fac0160c2392b4d130b0c0cf2cfb477c) - `2026-11-13T17:50:18Z` - Zhongqi Miao (@zhmiao) - PR: [docs: add a project catalogue page with model zoo links](https://github.com/microsoft/Biodiversity/pull/670)

### MicrosoftDocs/entra-docs (15 commit(s), signal 90)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merge pull request #14935 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/entra-docs/commit/b21c547f00ee3a7e8f9e68045d1daac28a2adc26) - `2026-11-13T18:33:01Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #14919 from markwahl-msft/mwahl-gov-req-sponsor](https://github.com/MicrosoftDocs/entra-docs/commit/f5361b5a94cdd53486b477cc3fc6a588697f6bc3) - `2026-11-13T16:39:14Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #14923 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/entra-docs/commit/99e0e24425d29715134717cb3f0b856d9a7fb06b) - `2026-11-13T08:36:28Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [clarify requesting for an agent](https://github.com/MicrosoftDocs/entra-docs/commit/859a9a8cfe32ec5ebe68fdae96f6c29c17f61d1e) - `2026-11-13T02:17:06Z` - Mark Wahl (@markwahl-msft)
- [Merge pull request #14912 from markwahl-msft/patch-2](https://github.com/MicrosoftDocs/entra-docs/commit/e14a5be91a384d9b56fde99f42f9a9a3f7b5fb7e) - `2026-11-13T01:39:55Z` - prmerger-automator[bot] (@prmerger-automator[bot])

### MicrosoftDocs/learn (15 commit(s), signal 115)

Tags: `docs, human-authored, security, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/80a5ba29a65b22301cf8c7ae31b071afbc981ce7) - `2026-11-13T18:22:22Z` - Learn Build Service GitHub App
- [Merge pull request #56841 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/learn/commit/a68172d012b0e2a2d6663f53d345e1617164c5e6) - `2026-11-13T18:09:47Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update sqldb mig (#56828)](https://github.com/MicrosoftDocs/learn/commit/0b07d8b951e39e8babd95c8601a4670d80ad7e1c) - `2026-11-13T17:50:49Z` - JulianePadrao (@JulianePadrao)
- [New ignite perception sessions 2026 11 (#56832) (#56838)](https://github.com/MicrosoftDocs/learn/commit/f3540f1527b2b0bcfcf7ec5333c5e6a66fa15fd1) - `2026-11-13T16:12:51Z` - Hassan Rasheed (@hrasheed-msft)
- [Add module: Plan integrated security operations with Microsoft Defend…](https://github.com/MicrosoftDocs/learn/commit/e11f34ed69712e5030961860572e3d4d0c3005dc) - `2026-11-13T13:38:17Z` - Hassan Rasheed (@hrasheed-msft)

### Azure-Samples/portability-patterns-library (15 commit(s), signal 90)

Tags: `human-authored, samples, watchlist`

- [Merge pull request #22 from Azure-Samples/docs/virtual-network-resour…](https://github.com/Azure-Samples/portability-patterns-library/commit/4ffc4fa98980d2dd88813477c2124f3d3010cb35) - `2026-11-13T11:38:15Z` - Sanjeev Hegde (@Sanjeev-Hegde) - PR: [Resource guide: Azure Virtual Network](https://github.com/Azure-Samples/portability-patterns-library/pull/22)
- [Merge pull request #14 from Azure-Samples/docs/resource-guides](https://github.com/Azure-Samples/portability-patterns-library/commit/0da319197dc7bcc6970923b9f805d3f2a2c1ab6e) - `2026-11-13T11:37:54Z` - Sanjeev Hegde (@Sanjeev-Hegde) - PR: [Resource guides: PostgreSQL, Application Insights, Key Vault, Entra Id, Workload Identity, service-bus, storage-account(blob,files)](https://github.com/Azure-Samples/portability-patterns-library/pull/14)
- [Update logical network documentation: clarify private endpoint usage …](https://github.com/Azure-Samples/portability-patterns-library/commit/b1392409b5794b0e1d358e28211e96041800b164) - `2026-11-13T11:31:07Z` - Javeed Ashraf - PR: [Resource guide: Azure Virtual Network](https://github.com/Azure-Samples/portability-patterns-library/pull/22)
- [Merge pull request #43 from Azure-Samples/docs/virtual-network-guide-…](https://github.com/Azure-Samples/portability-patterns-library/commit/b45dddce6d1e68287fe4bc24a773736d22da0f1d) - `2026-11-13T11:19:08Z` - Sanjeev Hegde (@Sanjeev-Hegde) - PR: [Virtual network guide: align with resource guide conventions](https://github.com/Azure-Samples/portability-patterns-library/pull/43)
- [Virtual network guide: align with resource guide conventions](https://github.com/Azure-Samples/portability-patterns-library/commit/b9b74c40ffaf0622e15194bc286724ad173c815c) - `2026-11-13T11:03:48Z` - Sanjeev Hegde - PR: [Virtual network guide: align with resource guide conventions](https://github.com/Azure-Samples/portability-patterns-library/pull/43)

### Azure/azure-sdk-for-java (14 commit(s), signal 139)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [com.azure+azure-security-keyvault-keys_4.13.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-security-keyvault-keys_4.13.0) - `2026-11-13T18:53:05Z`
- Release: [com.azure+azure-security-keyvault-administration_4.10.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-security-keyvault-administration_4.10.0) - `2026-11-13T18:52:50Z`
- Release: [com.azure.resourcemanager+azure-resourcemanager-cognitiveservices_1.5.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-cognitiveservices_1.5.0) - `2026-11-13T04:30:48Z`
- Release: [com.azure.resourcemanager+azure-resourcemanager-iothub_1.4.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-iothub_1.4.0) - `2026-11-13T03:52:53Z`
- Release: [com.azure+azure-ai-projects_2.10.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-ai-projects_2.10.0) - `2026-11-13T02:16:20Z`
- [Increment package versions for keyvault releases (#51258)](https://github.com/Azure/azure-sdk-for-java/commit/cbea30d1f50203ed8be356936cc9bcaccd87d2a6) - `2026-11-13T20:00:55Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[skip ci] Increment versions for keyvault releases](https://github.com/Azure/azure-sdk-for-java/pull/51258)
- [Pass the auto-release SDK PR to release completion (#51224)](https://github.com/Azure/azure-sdk-for-java/commit/93e7415732ed8809844125651981ede599deadc5) - `2026-11-13T19:48:15Z` - Helen Gao (@helen229) - PR: [Pass the auto-release SDK PR to release completion](https://github.com/Azure/azure-sdk-for-java/pull/51224)
- [Create ARCHITECTS file for architecture review mapping (#51236)](https://github.com/Azure/azure-sdk-for-java/commit/2a82a34f9ff3d43b882149f5214bb14b07fb49b2) - `2026-11-13T17:09:04Z` - Travis Prescott (@tjprescott) - PR: [[ARH] Create ARCHITECTS file for architecture review mapping](https://github.com/Azure/azure-sdk-for-java/pull/51236)
- [Regenerate Keys and Administration with latest commit ID (#51235)](https://github.com/Azure/azure-sdk-for-java/commit/13674f3ec30c424269926f1d4e32a24b3059abe8) - `2026-11-13T13:50:35Z` - Hariharan K (@hari9-9) - PR: [Regenerate Keys and Administration with latest commit ID](https://github.com/Azure/azure-sdk-for-java/pull/51235)
- [Increment package versions for cognitiveservices auto-releases (#51245)](https://github.com/Azure/azure-sdk-for-java/commit/948aa700f0b67c93e7c448620f5f4830aaed5565) - `2026-11-13T08:00:50Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[skip ci] Increment versions for cognitiveservices auto-releases](https://github.com/Azure/azure-sdk-for-java/pull/51245)

### Azure/azure-sdk-for-js (13 commit(s), signal 138)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [@azure/arm-containerservice_25.8.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-containerservice_25.8.0) - `2026-11-13T04:48:09Z`
- Release: [@azure/arm-aiinfraoptimization_1.0.0-beta.2](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-aiinfraoptimization_1.0.0-beta.2) - `2026-11-13T04:32:45Z`
- Release: [@azure/arm-cognitiveservices_9.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-cognitiveservices_9.0.0) - `2026-11-13T03:53:38Z`
- Release: [@azure/arm-iothub_7.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-iothub_7.0.0) - `2026-11-13T03:18:50Z`
- [[EngSys] exclude published ARM samples from CodeQL (#40777)](https://github.com/Azure/azure-sdk-for-js/commit/dae41b7495c7d44c76fa89c416cebd0baa9ba6ec) - `2026-11-13T20:32:09Z` - Jeremy Meng (@jeremymeng) - PR: [[EngSys] exclude published ARM samples from CodeQL](https://github.com/Azure/azure-sdk-for-js/pull/40777)
- [Pass the auto-release SDK PR to release completion (#40770)](https://github.com/Azure/azure-sdk-for-js/commit/b18957cfd67d6688c86296fe70bbf5d29bb523e8) - `2026-11-13T19:47:41Z` - Helen Gao (@helen229) - PR: [Pass the auto-release SDK PR to release completion](https://github.com/Azure/azure-sdk-for-js/pull/40770)
- [[EngSys] Replace copyfiles in js-sdk-release-tools (#40778)](https://github.com/Azure/azure-sdk-for-js/commit/a397b7f66a323e5f89b08299eaa7ea4404b4be49) - `2026-11-13T17:44:12Z` - Jeremy Meng (@jeremymeng)
- [Update emitter version (#40784)](https://github.com/Azure/azure-sdk-for-js/commit/bf40b52c521ebb3251cca7c235aac37032303b0e) - `2026-11-13T13:49:37Z` - Jiao Di (MSFT) (@v-jiaodi) - PR: [Update emitter version](https://github.com/Azure/azure-sdk-for-js/pull/40784)
- [Bump TypeSpec emitter dependencies (#40783)](https://github.com/Azure/azure-sdk-for-js/commit/12b5fef79f80963092b1eae620b2625c9a0568aa) - `2026-11-13T05:47:39Z` - Copilot (@Copilot) - PR: [Bump TypeSpec emitter dependencies](https://github.com/Azure/azure-sdk-for-js/pull/40783)

### Azure/azure-sdk-for-go (13 commit(s), signal 138)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [sdk/storage/azdatalake/v1.8.0-beta.1](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/storage/azdatalake/v1.8.0-beta.1) - `2026-11-13T18:44:17Z`
- Release: [sdk/resourcemanager/containerservice/armcontainerservice/v9.8.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/containerservice/armcontainerservice/v9.8.0) - `2026-11-13T04:49:16Z`
- Release: [sdk/resourcemanager/cognitiveservices/armcognitiveservices/v4.0.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/cognitiveservices/armcognitiveservices/v4.0.0) - `2026-11-13T03:56:52Z`
- Release: [sdk/resourcemanager/iothub/armiothub/v2.0.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/iothub/armiothub/v2.0.0) - `2026-11-13T03:16:14Z`
- [Exclude eng/common from Dependabot npm version updates (#28045)](https://github.com/Azure/azure-sdk-for-go/commit/a588a12c14403b23320e4bf37b76b332b04b0261) - `2026-11-13T20:20:07Z` - Heath Stewart (@heaths) - PR: [Exclude eng/common from Dependabot npm version updates](https://github.com/Azure/azure-sdk-for-go/pull/28045)
- [Pass the auto-release SDK PR to release completion (#28020)](https://github.com/Azure/azure-sdk-for-go/commit/460e734958d082e67f041c66a8effc28628f0246) - `2026-11-13T19:47:53Z` - Helen Gao (@helen229) - PR: [Pass the auto-release SDK PR to release completion](https://github.com/Azure/azure-sdk-for-go/pull/28020)
- [Prepare azdatalake 1.8.0-beta.1 for release (#28041)](https://github.com/Azure/azure-sdk-for-go/commit/16274e3bdc8bdf9fed63d92f8d9118d42788b716) - `2026-11-13T12:30:42Z` - gunjansingh-msft (@gunjansingh-msft) - PR: [[Storage] Prepare azdatalake 1.8.0-beta.1 for release](https://github.com/Azure/azure-sdk-for-go/pull/28041)
- [Configurations:  'specification/containerservice/resource-manager/Mic…](https://github.com/Azure/azure-sdk-for-go/commit/8992e6822c028a66d35a87730910ecbaf9ecc61d) - `2026-11-13T04:18:04Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR sdk-resourcemanager/containerservice/armcontainerservice]-generated-from-SDK Generation - Go-7066663](https://github.com/Azure/azure-sdk-for-go/pull/28015)
- [Upgrade Go emitter to 0.19.0 and TypeSpec dependencies (#28039)](https://github.com/Azure/azure-sdk-for-go/commit/08adf1f577fe780a022884afa06993e440a96460) - `2026-11-13T04:13:45Z` - Copilot (@Copilot) - PR: [Upgrade Go emitter to 0.19.0 and TypeSpec dependencies](https://github.com/Azure/azure-sdk-for-go/pull/28039)

### Azure/azure-cli-extensions (11 commit(s), signal 136)

Tags: `docs, human-authored, release, release-language, watchlist`

- Release: [migrate 3.0.0b7](https://github.com/Azure/azure-cli-extensions/releases/tag/migrate-3.0.0b7) - `2026-11-13T07:16:39Z`
- Release: [fleet 1.12.0](https://github.com/Azure/azure-cli-extensions/releases/tag/fleet-1.12.0) - `2026-11-13T03:54:08Z`
- Release: [managednetworkfabric 10.0.0b4](https://github.com/Azure/azure-cli-extensions/releases/tag/managednetworkfabric-10.0.0b4) - `2026-11-12T23:25:56Z`
- Release: [workload-manager 1.0.0b1](https://github.com/Azure/azure-cli-extensions/releases/tag/workload-manager-1.0.0b1) - `2026-11-12T22:46:05Z`
- [[Release] Update index.json for extension [ migrate-3.0.0b7 ]](https://github.com/Azure/azure-cli-extensions/commit/31388ed0605265c105d040a5ffcce367aa2fad24) - `2026-11-13T07:15:38Z` - Azure CLI Team (@azclibot)
- [migrate/runbook: bugbash fixes - resume live view, non editable overr…](https://github.com/Azure/azure-cli-extensions/commit/f072c044bcc4e08e4d66c39ba26c4eacf897b061) - `2026-11-13T07:03:03Z` - krdhruva (@krdhruva) - PR: [migrate/runbook: bugbash fixes - resume live view, non editable override](https://github.com/Azure/azure-cli-extensions/pull/10577)
- [[aks-preview] Add Azure Managed Lustre cluster extension support (#10…](https://github.com/Azure/azure-cli-extensions/commit/ee59f3ea4333afdfd9e973b8ed6fe854d078a495) - `2026-11-13T03:58:05Z` - Wolfgang De Salvador (@wolfgang-desalvador) - PR: [Add AMLFS update preview command](https://github.com/Azure/azure-cli-extensions/pull/10383)
- [[Release] Update index.json for extension [ fleet-1.12.0 ]](https://github.com/Azure/azure-cli-extensions/commit/88f5b3897bbadfcbfaf6119aeaed7afe1db9431a) - `2026-11-13T03:53:09Z` - Azure CLI Team (@azclibot)
- [Fleet 20261102Preview CLI Updates (#10440)](https://github.com/Azure/azure-cli-extensions/commit/8f3ba6d55c9f2d63794b1aa411c9605a32814c42) - `2026-11-13T03:40:21Z` - Yoo Bin Shin (@nibooy) - PR: [Fleet 20261102Preview CLI Updates](https://github.com/Azure/azure-cli-extensions/pull/10440)

### Azure/azure-sdk-for-python (10 commit(s), signal 135)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [azure-mgmt-cognitiveservices_15.0.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-cognitiveservices_15.0.0) - `2026-11-13T18:12:31Z`
- Release: [azure-keyvault-administration_4.8.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-keyvault-administration_4.8.0) - `2026-11-12T23:13:58Z`
- Release: [azure-keyvault-keys_4.12.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-keyvault-keys_4.12.0) - `2026-11-12T23:13:41Z`
- [[Cosmos] Cover vector index type changes without skipping policy test…](https://github.com/Azure/azure-sdk-for-python/commit/7557b2db53e900bd5f167f1bfa4bc0a9c866be1a) - `2026-11-13T20:15:56Z` - Simon Moreno (@simorenoh) - PR: [[Cosmos] Cover vector index type changes without skipping policy tests](https://github.com/Azure/azure-sdk-for-python/pull/49929)
- [Fix SDK PR handoff in Python release completion (#49941)](https://github.com/Azure/azure-sdk-for-python/commit/53f46d97eeadba69608d8099e2808c4dbe5ae38e) - `2026-11-13T19:56:23Z` - Helen Gao (@helen229) - PR: [Fix SDK PR handoff in Python release completion](https://github.com/Azure/azure-sdk-for-python/pull/49941)
- [Increment version for keyvault releases (#49995)](https://github.com/Azure/azure-sdk-for-python/commit/0e68ce029c2709f125b24ba712f65339c636e536) - `2026-11-13T19:19:10Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment version for keyvault releases](https://github.com/Azure/azure-sdk-for-python/pull/49995)
- [[AutoPR azure-mgmt-cognitiveservices]-generated-from-SDK Generation -…](https://github.com/Azure/azure-sdk-for-python/commit/3e59835146b8095e864a236f8ca9c066459f4dda) - `2026-11-13T16:17:32Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-mgmt-cognitiveservices]-generated-from-SDK Generation - Python-7065615](https://github.com/Azure/azure-sdk-for-python/pull/49963)
- [Add PlatformValidation sync/async live and recorded SDK tests (#49303)](https://github.com/Azure/azure-sdk-for-python/commit/137dde6bc2725219aeb4f308a8e536f35a7a4ebc) - `2026-11-13T05:28:32Z` - shivangirana20 (@shivangirana20) - PR: [Add PlatformValidation sync/async live and recorded SDK tests](https://github.com/Azure/azure-sdk-for-python/pull/49303)

### MicrosoftDocs/dynamics-365-unified-operations-public (10 commit(s), signal 95)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/Dynamics…](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/f4cacf7d658561cb727179ceb692171cfdf08600) - `2026-11-13T19:06:50Z` - Learn Build Service GitHub App
- [Merge pull request #22855 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/f510a0dd5f3b3ae94283f4149913ed17df89920f) - `2026-11-13T19:03:20Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Document Management Update (#22784)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/190469d2914a057f36368b4f6a46e0ff0f37a181) - `2026-11-13T17:43:01Z` - Karl Maybach (@kamaybac)
- [Release Notes for IC November 2026 (#22849)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/32059c2ece252aac05edf490893ea887ce32d3b1) - `2026-11-13T16:56:53Z` - Mahesh Prasad Patro Karpana (@MaheshPrasadK)
- [Hr update (#22829)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/2d365d68f4fe75ecc179a63a4aed77e54859a712) - `2026-11-13T15:47:30Z` - twheeloc (@twheeloc)

### dotnet/efcore (10 commit(s), signal 95)

Tags: `docs, human-authored, release-language, watchlist`

- [Keep navigation configuration when a navigation becomes a skip naviga…](https://github.com/dotnet/efcore/commit/c68557018a2845488ad6d0a20b2554edba61b6c0) - `2026-11-13T18:14:23Z` - AsadIqbal-Software Engineer (@AsadIqbal-Dev) - PR: [Keep navigation configuration when a navigation becomes a skip navigation](https://github.com/dotnet/efcore/pull/39502)
- [Flatten nested anonymous types in join key selectors (#39514)](https://github.com/dotnet/efcore/commit/89c632ccf3f4a4bb9852e17776f9efe1e71b3f0c) - `2026-11-13T18:11:04Z` - Hassan Nawaz Khan (@Hassan1305) - PR: [Flatten nested anonymous types in join key selectors](https://github.com/dotnet/efcore/pull/39514)
- [Fix Helix test failures (#39635)](https://github.com/dotnet/efcore/commit/3e1520ccab218e743b7df5a0298d29c974ccebff) - `2026-11-13T17:05:04Z` - Andriy Svyryd (@AndriySvyryd) - PR: [Fix Helix test failures](https://github.com/dotnet/efcore/pull/39635)
- [[automated] Merge branch 'release/11.0' => 'main' (#39516)](https://github.com/dotnet/efcore/commit/3f09c1c66ba76192ff10599df32223be0c9793ac) - `2026-11-13T16:48:21Z` - William Godbe (@wtgodbe) - PR: [[automated] Merge branch 'release/11.0' => 'main'](https://github.com/dotnet/efcore/pull/39516)
- [Filter required table-splitting dependents of a derived TPH type by i…](https://github.com/dotnet/efcore/commit/4fd472aff273cfabfd6cb23f737dff901537df2f) - `2026-11-13T16:25:19Z` - Jeremy Morren (@jeremy-morren) - PR: [Filter required table-splitting dependents of a derived TPH type by its discriminator](https://github.com/dotnet/efcore/pull/39528)

### Azure/azure-dev (10 commit(s), signal 125)

Tags: `human-authored, product:Azure AI, release, samples, watchlist`

- Release: [azd-ext-azure-ai-content-understanding_0.1.2-preview](https://github.com/Azure/azure-dev/releases/tag/azd-ext-azure-ai-content-understanding_0.1.2-preview) - `2026-11-12T23:10:04Z`
- [fix: validate Foundry environment references during discovery (#10878)](https://github.com/Azure/azure-dev/commit/03459efde709d92907b3b788fb20b3ecbbd122cd) - `2026-11-13T10:00:13Z` - Hui Miao (@huimiu) - PR: [fix: validate Foundry environment references during discovery](https://github.com/Azure/azure-dev/pull/10878)
- [refactor(foundry): adopt shared Foundry policy package across extensi…](https://github.com/Azure/azure-dev/commit/9194e6c86a89c92ecdc87c6d624def469fa2c8bc) - `2026-11-13T07:52:25Z` - Zhijie Huang (@hund030) - PR: [refactor(foundry): adopt shared Foundry policy package across extensions](https://github.com/Azure/azure-dev/pull/10953)
- [fix: resolve connection ARM identity from project metadata (#10891)](https://github.com/Azure/azure-dev/commit/f0e10865bda9bf15c23db2ff44382d0983d3c718) - `2026-11-13T06:16:36Z` - Hui Miao (@huimiu) - PR: [fix: resolve connection ARM identity from project metadata](https://github.com/Azure/azure-dev/pull/10891)
- [feat(foundry): add shared Foundry policy package (#10910)](https://github.com/Azure/azure-dev/commit/b4be9e8a706dc3512e9c10c0960bc11777670f33) - `2026-11-13T02:16:00Z` - Zhijie Huang (@hund030) - PR: [feat(foundry): add shared Foundry policy package](https://github.com/Azure/azure-dev/pull/10910)
- [fix(ai): conditionally export AKS Bicep infrastructure (#10915)](https://github.com/Azure/azure-dev/commit/fff782c1c15f0fb2915adcd80e41dedf7249ba9c) - `2026-11-13T01:37:01Z` - Yi Liu (@yiliuTo) - PR: [fix(ai): conditionally export AKS Bicep infrastructure](https://github.com/Azure/azure-dev/pull/10915)

### Azure/azure-sdk-for-net (9 commit(s), signal 134)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [Azure.AI.Extensions.OpenAI_3.0.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.AI.Extensions.OpenAI_3.0.0) - `2026-11-13T00:20:39Z`
- [Pass the auto-release SDK PR to release completion (#64863)](https://github.com/Azure/azure-sdk-for-net/commit/7282d174d231a1f62a0dd2c82e0d17d647931515) - `2026-11-13T19:47:35Z` - Helen Gao (@helen229) - PR: [Pass the auto-release SDK PR to release completion](https://github.com/Azure/azure-sdk-for-net/pull/64863)
- [Diff missing-patch files locally in re-review input (#64838)](https://github.com/Azure/azure-sdk-for-net/commit/fa2a7a994bbeba745c424dd3f601831290e28d6c) - `2026-11-13T19:29:13Z` - m-nash (@m-nash) - PR: [Diff missing-patch files locally in re-review input](https://github.com/Azure/azure-sdk-for-net/pull/64838)
- [Update UnbrandedGeneratorVersion to 1.0.0-alpha.20261112.2 (#64915)](https://github.com/Azure/azure-sdk-for-net/commit/925d9d79745831f66b22ff6a5c8e28f24a3579a3) - `2026-11-13T16:32:50Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Update UnbrandedGeneratorVersion to 1.0.0-alpha.20261112.2](https://github.com/Azure/azure-sdk-for-net/pull/64915)
- [Update Compute TypeSpec commits (#64938)](https://github.com/Azure/azure-sdk-for-net/commit/2fa25228faf71e5436a7586a48d430cef50a9065) - `2026-11-13T05:38:23Z` - Pan Shao (@pshao25) - PR: [Update Compute TypeSpec commits](https://github.com/Azure/azure-sdk-for-net/pull/64938)
- [chore: update CODEOWNERS to add additional owners for various paths (…](https://github.com/Azure/azure-sdk-for-net/commit/219ffcb56a24f53d61860e0486d03da8113268c8) - `2026-11-13T02:59:27Z` - Arthur Ma (@ArthurMa1978) - PR: [chore: update CODEOWNERS to add additional owners for various paths](https://github.com/Azure/azure-sdk-for-net/pull/64867)

### microsoft/kiota-ruby (9 commit(s), signal 134)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [v0.26.0](https://github.com/microsoft/kiota-ruby/releases/tag/v0.26.0) - `2026-11-13T12:38:27Z`
- [Merge pull request #225 from jackson-asmith/fix/retry-unprocessed-mut…](https://github.com/microsoft/kiota-ruby/commit/d50eafd523441b50e318bd0cd6959bee07600280) - `2026-11-13T19:29:11Z` - Vincent Biret (@baywet) - PR: [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-ruby/pull/225)
- [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-ruby/commit/11925e56b32814f6e0360c09ccdac664543b24bb) - `2026-11-13T18:04:31Z` - Jackson Smith (@jackson-asmith) - PR: [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-ruby/pull/225)
- [Merge pull request #216 from microsoft/release-please--branches--main](https://github.com/microsoft/kiota-ruby/commit/32135326b2e74b5b4f0d7be76b19b941a3302a31) - `2026-11-13T12:36:12Z` - Vincent Biret (@baywet) - PR: [chore(main): release 0.26.0](https://github.com/microsoft/kiota-ruby/pull/216)
- [chore(main): release 0.26.0](https://github.com/microsoft/kiota-ruby/commit/094269e31a911e6afd937604191a1bc761cb39eb) - `2026-11-13T12:30:01Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(main): release 0.26.0](https://github.com/microsoft/kiota-ruby/pull/216)
- [Merge pull request #222 from Daiyuanranfeng/feat/retry-handler](https://github.com/microsoft/kiota-ruby/commit/50de2c140f853d0b0325a3707dbf0d469a58eb32) - `2026-11-13T12:27:24Z` - Vincent Biret (@baywet) - PR: [feat(http): add configurable retry middleware](https://github.com/microsoft/kiota-ruby/pull/222)

### MicrosoftDocs/azure-docs-sdk-java (9 commit(s), signal 84)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/c290d11cdfb9243d2eba1182e13e2cd1a2dad8aa) - `2026-11-13T19:16:34Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/fb63977d7c54c919abec141b3cdfda4eb4a46642) - `2026-11-13T05:05:28Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/4604fec5d5ed42bbb8d8e6f88c840a3d790022a5) - `2026-11-13T04:39:38Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/125f9626a56f240a8e120e3f24f7f68c29cb7a84) - `2026-11-13T04:15:27Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/127d2b2af65fd80051e9721fd8d240e6956eab51) - `2026-11-13T02:41:25Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/SupportArticles-docs (9 commit(s), signal 84)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/c58720df1183687268c04e228242246c9413ff20) - `2026-11-13T18:04:33Z` - Learn Build Service GitHub App
- [Merge pull request #12850 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/dfcf0c36717c6ea1f14a528df4a3697a6730575a) - `2026-11-13T18:02:44Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [AB#13424: AI Optimization and Freshness review: Resolve PAGELATCH_EX …](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/3f0c67f8333a8479bc5f6074935c49db6c0f50e1) - `2026-11-13T17:30:30Z` - Aarti Goyle (@aartig13)
- [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/53a6ab748bdc2c4e916e906d7d20696e0fc7eeb4) - `2026-11-13T02:06:10Z` - Learn Build Service GitHub App
- [Merge pull request #12848 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/bc3f7c8f95903d6e10c2655f017d2eeb2a8e8f3c) - `2026-11-13T02:04:09Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### microsoft/entrabot (9 commit(s), signal 84)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merge pull request #149 from microsoft/feat/windows-setup-wizard](https://github.com/microsoft/entrabot/commit/b21f78ec0c5bcdd4d3ca9e2d67b51f26c48fdd3b) - `2026-11-13T17:39:15Z` - Brandon Werner (@brandwe) - PR: [Windows: setup wizard, TPM key lifecycle, and runtime fixes](https://github.com/microsoft/entrabot/pull/149)
- [docs(windows): Work IQ without the Agent 365 CLI; reconcile the chang…](https://github.com/microsoft/entrabot/commit/6c27b7174b7e73292be05f1226a16828f9266ac0) - `2026-11-13T03:34:19Z` - Brandon Werner (@brandwe) - PR: [Windows: setup wizard, TPM key lifecycle, and runtime fixes](https://github.com/microsoft/entrabot/pull/149)
- [feat(windows): switch on Word, Excel and OneDrive files from setup it…](https://github.com/microsoft/entrabot/commit/695aca8d7254d219530c6b54ebf828044731fa2d) - `2026-11-13T03:16:48Z` - Brandon Werner (@brandwe) - PR: [Windows: setup wizard, TPM key lifecycle, and runtime fixes](https://github.com/microsoft/entrabot/pull/149)
- [fix(windows): remove the old sign-in before asking for a new one](https://github.com/microsoft/entrabot/commit/02587b10389e19c2f315375773bd14bb23af2402) - `2026-11-13T00:21:48Z` - Brandon Werner (@brandwe) - PR: [Windows: setup wizard, TPM key lifecycle, and runtime fixes](https://github.com/microsoft/entrabot/pull/149)
- [fix(windows): the browser sign-in setting now reaches az; check a sig…](https://github.com/microsoft/entrabot/commit/f41f9e01ca1a47aa6e159f4c455dae6b2a5be6f8) - `2026-11-13T00:03:39Z` - Brandon Werner (@brandwe) - PR: [Windows: setup wizard, TPM key lifecycle, and runtime fixes](https://github.com/microsoft/entrabot/pull/149)

### microsoft/vscode-docs (8 commit(s), signal 93)

Tags: `docs, human-authored, release-language, watchlist`

- [Merge pull request #10647 from microsoft/ntrogh/template-highlights-v…](https://github.com/microsoft/vscode-docs/commit/b8d9adca67e06a847cc20921ca7a7450ea302dc2) - `2026-11-13T15:30:46Z` - Nick Trogh (@ntrogh) - PR: [Update release note template for highlights video](https://github.com/microsoft/vscode-docs/pull/10647)
- [Update release note template for highlights video](https://github.com/microsoft/vscode-docs/commit/29240996b4dcd336419504576c7e5a6bb75218ee) - `2026-11-13T15:21:50Z` - Nick Trogh (@ntrogh) - PR: [Update release note template for highlights video](https://github.com/microsoft/vscode-docs/pull/10647)
- [Merge pull request #10646 from microsoft/ntrogh/insiders-relnotes](https://github.com/microsoft/vscode-docs/commit/182761fe27a3130bd46a154d8e11d2fe1378f8ec) - `2026-11-13T13:30:49Z` - Nick Trogh (@ntrogh) - PR: [Update Insiders release notes](https://github.com/microsoft/vscode-docs/pull/10646)
- [Update Insiders release notes](https://github.com/microsoft/vscode-docs/commit/aa4241913e3218caff333634f368b91875ee5a10) - `2026-11-13T12:08:24Z` - Nick Trogh (@ntrogh) - PR: [Update Insiders release notes](https://github.com/microsoft/vscode-docs/pull/10646)
- [Fix images for LFS](https://github.com/microsoft/vscode-docs/commit/a086d5cb450890daf838411fdc8d39b61430193b) - `2026-11-13T10:36:59Z` - Nick Trogh (@ntrogh) - PR: [Update Insiders release notes](https://github.com/microsoft/vscode-docs/pull/10646)

### MicrosoftDocs/dynamics-365-contact-center (7 commit(s), signal 92)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/26d999e7dd726453663c7e5a2d6b2822b35b5783) - `2026-11-13T13:03:43Z` - Learn Build Service GitHub App
- [Merge pull request #821 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/2d50cb8c95ff1e20eb7482815bd11fa866b046fd) - `2026-11-13T13:03:19Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Publish Contact Center Admin Workspace content for public preview (#808)](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/f7bbd617a47aad4c5484d75a300a8f9149b05afe) - `2026-11-13T09:10:03Z` - Neeraja Nellimarla (@neeranelli)
- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/63eee7d120dd62abc8603ce62d0ca6e30b5e397b) - `2026-11-13T01:02:29Z` - Learn Build Service GitHub App
- [Merge pull request #819 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/62cc5b658514296eaaa77f1d47bc3bce5a367d3e) - `2026-11-13T01:02:07Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### microsoft/kiota-http-go (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #312 from jackson-asmith/fix/retry-unprocessed-mut…](https://github.com/microsoft/kiota-http-go/commit/3630bdfe720aa0ed680c08fdd76b3cdd8f873d46) - `2026-11-13T18:52:05Z` - Vincent Biret (@baywet) - PR: [feat: add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-http-go/pull/312)
- [refactor: read RetryUnprocessedMutationsOnly through retryHandlerOpti…](https://github.com/microsoft/kiota-http-go/commit/f28583aaba04e196a75d3bd3fe693c7e8d8126ca) - `2026-11-13T18:49:33Z` - Jackson Smith (@jackson-asmith) - PR: [feat: add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-http-go/pull/312)
- [fix: don't resend a POST that a redirect turned into a GET](https://github.com/microsoft/kiota-http-go/commit/0fb24d015b0788c8e18b4f75e5d2ceda323d869f) - `2026-11-13T18:08:12Z` - Jackson Smith (@jackson-asmith) - PR: [feat: add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-http-go/pull/312)
- [feat: add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-http-go/commit/865a020774c75016ff67260a0cb41585d287f8de) - `2026-11-13T16:49:12Z` - Jackson Smith (@jackson-asmith) - PR: [feat: add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-http-go/pull/312)
- [Merge pull request #296 from hardikkaurani/fix/middleware-reliability…](https://github.com/microsoft/kiota-http-go/commit/2a1e879ea8777811482bf9d59f146998f9a2a5cb) - `2026-11-13T14:14:19Z` - Vincent Biret (@baywet) - PR: [fix(http): close intermediate response bodies to prevent socket leaks and honor per-request header scrubber](https://github.com/microsoft/kiota-http-go/pull/296)

### microsoft/kiota-python (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #897 from jackson-asmith/fix/retry-unprocessed-mut…](https://github.com/microsoft/kiota-python/commit/17b952f81ea2a4d46bb44b6fe6b253578a0cf481) - `2026-11-13T18:34:05Z` - Vincent Biret (@baywet) - PR: [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-python/pull/897)
- [test(http): cover redirects with retry_unprocessed_mutations_only](https://github.com/microsoft/kiota-python/commit/e31858f5a1d54f7a6e70125f23343394fd86c49d) - `2026-11-13T17:22:58Z` - Jackson Smith (@jackson-asmith) - PR: [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-python/pull/897)
- [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-python/commit/05e2b75915ed2014e8425d3bb18647c9da66ad00) - `2026-11-13T17:03:11Z` - Jackson Smith (@jackson-asmith) - PR: [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-python/pull/897)
- [Merge pull request #895 from Muneer320/fix/datetime-fold-parameters](https://github.com/microsoft/kiota-python/commit/37ed43879765136059eaa3b85a205c817ef978be) - `2026-11-13T14:04:11Z` - Vincent Biret (@baywet) - PR: [fix(abstractions): preserve datetime fold in request parameters](https://github.com/microsoft/kiota-python/pull/895)
- [Merge pull request #893 from Muneer320/fix/form-field-name-whitespace](https://github.com/microsoft/kiota-python/commit/1cc664f190aa0bac36eaf6902c982cb4f6b122a0) - `2026-11-13T12:35:36Z` - Vincent Biret (@baywet) - PR: [fix(form): preserve whitespace in field names](https://github.com/microsoft/kiota-python/pull/893)

### microsoft/kiota-java (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #2251 from jackson-asmith/fix/retry-unprocessed-mu…](https://github.com/microsoft/kiota-java/commit/3559f2c07c2e96d5f7a88905c07822468444dd3e) - `2026-11-13T18:29:20Z` - Vincent Biret (@baywet) - PR: [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-java/pull/2251)
- [test(http): cover redirects with retryUnprocessedMutationsOnly](https://github.com/microsoft/kiota-java/commit/8e43ee5310d15497bd0e1f860c4492bfd413da2e) - `2026-11-13T17:23:50Z` - Jackson Smith (@jackson-asmith) - PR: [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-java/pull/2251)
- [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-java/commit/e79b4c3212282d0e265f87eab8d2bd973c02c714) - `2026-11-13T17:11:25Z` - Jackson Smith (@jackson-asmith) - PR: [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-java/pull/2251)
- [Merge pull request #2239 from hardikkaurani/fix/form-factory-content-…](https://github.com/microsoft/kiota-java/commit/460d9b990c03090eecc9020ad5dcfbee01ebb200) - `2026-11-13T14:11:18Z` - Vincent Biret (@baywet) - PR: [fix(serialization): support content-type parameters and case-insensitivity in form factories](https://github.com/microsoft/kiota-java/pull/2239)
- [ci: install Java 8 toolchain alongside Java 21](https://github.com/microsoft/kiota-java/commit/bd2dee773b358850d7a2c0ad71983258a99a7f0c) - `2026-11-13T13:09:48Z` - Vincent Biret (@baywet) - PR: [fix(serialization): support content-type parameters and case-insensitivity in form factories](https://github.com/microsoft/kiota-java/pull/2239)

### MicrosoftDocs/azure-docs-sdk-python (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/263285ae1997db4e3af1f9914b8d8c1f5fc00acc) - `2026-11-13T18:26:05Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/33f712ead436e8d3e4bb225a4932789d90b46926) - `2026-11-13T01:47:53Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/f90b993de1d4aac8c577364e3506b48cd582f956) - `2026-11-13T00:21:01Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/42321f5f27d2b1deca82750a897ecb9ffecbac7c) - `2026-11-12T23:34:25Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/ae886c0b82f0b2854170efde2a94b8882b8f2916) - `2026-11-12T23:33:27Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/quantum-docs (6 commit(s), signal 91)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/quantum-…](https://github.com/MicrosoftDocs/quantum-docs/commit/a712d1f6985665581ad95542bd057116185a8f58) - `2026-11-13T17:02:50Z` - Learn Build Service GitHub App
- [Merge pull request #1715 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/quantum-docs/commit/61a113a8e55ba7f0181961f0e46fac2443f954d1) - `2026-11-13T17:02:25Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Updates to QDK/Chemistry articles for release 2.3.0 (#1708)](https://github.com/MicrosoftDocs/quantum-docs/commit/cca43e40a98f049c8ee77286a42ab92a4c17e1b2) - `2026-11-13T16:35:30Z` - Jeremy (@jlehnersd)
- [Merging changes synced from https://github.com/MicrosoftDocs/quantum-…](https://github.com/MicrosoftDocs/quantum-docs/commit/987d683f9cd7e9cfe95baa94aab667bc33b115c3) - `2026-11-12T23:03:11Z` - Learn Build Service GitHub App
- [Merge pull request #1714 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/quantum-docs/commit/ecb7d3317eb5f6ce519e7cc0ab2d6b68b29215c2) - `2026-11-12T23:02:48Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### microsoftgraph/msgraph-snippets-go (6 commit(s), signal 21)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #251 from microsoftgraph/dependabot/go_modules/src…](https://github.com/microsoftgraph/msgraph-snippets-go/commit/9b348698fd9d07566c863380b60170de9b438db5) - `2026-11-13T16:31:16Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump github.com/microsoftgraph/msgraph-sdk-go from 1.105.0 to 1.106.0 in /src](https://github.com/microsoftgraph/msgraph-snippets-go/pull/251)
- [Merge pull request #252 from microsoftgraph/dependabot/go_modules/src…](https://github.com/microsoftgraph/msgraph-snippets-go/commit/0aa7215aabd0242ac592b05fa8547a5fb2159f45) - `2026-11-13T16:30:38Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump github.com/microsoft/kiota-abstractions-go from 1.12.0 to 1.12.1 in /src](https://github.com/microsoftgraph/msgraph-snippets-go/pull/252)
- [Bump github.com/microsoftgraph/msgraph-sdk-go in /src](https://github.com/microsoftgraph/msgraph-snippets-go/commit/9575943e3d888a3feb0db3e057a221e89f4e3eaf) - `2026-11-13T16:28:11Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump github.com/microsoftgraph/msgraph-sdk-go from 1.105.0 to 1.106.0 in /src](https://github.com/microsoftgraph/msgraph-snippets-go/pull/251)
- [Bump github.com/microsoft/kiota-abstractions-go in /src](https://github.com/microsoftgraph/msgraph-snippets-go/commit/b2cd41677f18b1dcc14ec237b90543181c365258) - `2026-11-13T16:27:49Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump github.com/microsoft/kiota-abstractions-go from 1.12.0 to 1.12.1 in /src](https://github.com/microsoftgraph/msgraph-snippets-go/pull/252)
- [Merge pull request #250 from microsoftgraph/dependabot/go_modules/src…](https://github.com/microsoftgraph/msgraph-snippets-go/commit/a2a6e4d8eb0e518187f27d2063de550e0a6f0882) - `2026-11-13T16:25:47Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump github.com/microsoft/kiota-http-go from 1.6.0 to 1.6.1 in /src](https://github.com/microsoftgraph/msgraph-snippets-go/pull/250)

### MicrosoftDocs/windowsserverdocs (6 commit(s), signal 81)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/windowss…](https://github.com/MicrosoftDocs/windowsserverdocs/commit/cceb56b597a2c1629e00ab6abf6604659c000974) - `2026-11-13T16:01:02Z` - Learn Build Service GitHub App
- [Merge pull request #9416 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/windowsserverdocs/commit/9aee47395659305db483a59fd7012f4fa62b5362) - `2026-11-13T15:59:51Z` - Robin Harwood (@robinharwood)
- [Resolve syncing conflicts from repo_sync_working_branch to main (#8738)](https://github.com/MicrosoftDocs/windowsserverdocs/commit/40b930cabdb419d3d02b1bb859d3c1d06e61c695) - `2026-11-13T15:48:01Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merging changes synced from https://github.com/MicrosoftDocs/windowss…](https://github.com/MicrosoftDocs/windowsserverdocs/commit/b0f9a68a9d18d576dcbfe5b0fa7b396fd49b6ed2) - `2026-11-13T15:39:59Z` - Learn Build Service GitHub App
- [Merge pull request #9242 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/windowsserverdocs/commit/8e4d9090fbb2d0f5f495434219c1234f92f00bbc) - `2026-11-13T15:38:42Z` - Robin Harwood (@robinharwood)

### MicrosoftDocs/azure-docs-sdk-node (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/b6ab70b5efd9fcbb8ff05871771a003576104016) - `2026-11-13T04:55:10Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/b2a253ba2b10ee13e4c8a153b7d99ff9833ab66b) - `2026-11-13T04:39:52Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/c923e3f7f934edcaa7d957b2286b5914b08bf387) - `2026-11-13T04:00:13Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/3b95d8996378ea4cb9146f00cf0720ced4f69f54) - `2026-11-13T03:26:47Z` - azure-sdk (@azure-sdk)
- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/732b33bdecdeef2f92c510b7a7f1b3ac44dc90d4) - `2026-11-12T23:09:21Z` - azure-sdk (@azure-sdk)

### Azure-Samples/AzureLocal (5 commit(s), signal 105)

Tags: `human-authored, samples, security, watchlist`

- [Merge pull request #113 from carlosmayol/securedcore-validation-2610](https://github.com/Azure-Samples/AzureLocal/commit/68d4b8b75bff8d1915877f951d081c8dd6911608) - `2026-11-13T19:42:32Z` - Manika Dhiman (@ManikaDhiman) - PR: [Security baseline 2610: add Validation commands for the Secured-core rows](https://github.com/Azure-Samples/AzureLocal/pull/113)
- [Add Validation commands for the three Secured-core rows in the 2610 s…](https://github.com/Azure-Samples/AzureLocal/commit/e49aa4dcf955b9635021db8659bc5b26de598133) - `2026-11-13T19:38:10Z` - Carlos Mayol Berral (@carlosmayol) - PR: [Security baseline 2610: add Validation commands for the Secured-core rows](https://github.com/Azure-Samples/AzureLocal/pull/113)
- [Merge pull request #111 from carlosmayol/security-baseline-2610-fix](https://github.com/Azure-Samples/AzureLocal/commit/e8eca183350c692c5b55229176c9e06f82d5b447) - `2026-11-13T17:52:42Z` - Manika Dhiman (@ManikaDhiman) - PR: [Fix Azure Local 2610 security baseline CSVs](https://github.com/Azure-Samples/AzureLocal/pull/111)
- [Fix SecurityBaseline_2610Adless.csv](https://github.com/Azure-Samples/AzureLocal/commit/865862a055ed4458157156b995412af3ba7a464c) - `2026-11-13T17:49:01Z` - Carlos Mayol (MSFT) (@carlosmayol) - PR: [Fix Azure Local 2610 security baseline CSVs](https://github.com/Azure-Samples/AzureLocal/pull/111)
- [Fix SecurityBaseline_2610domjoin.csv](https://github.com/Azure-Samples/AzureLocal/commit/17ede781a47a077e7b25b555df8228969e3a0dde) - `2026-11-13T17:48:58Z` - Carlos Mayol (MSFT) (@carlosmayol) - PR: [Fix Azure Local 2610 security baseline CSVs](https://github.com/Azure-Samples/AzureLocal/pull/111)

### Azure/data-api-builder (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Add Engine Telemetry - Phase 1 (#3825)](https://github.com/Azure/data-api-builder/commit/594e942a6dfc71d61df272450d8daf7873cfb17c) - `2026-11-13T19:33:27Z` - aaronburtle (@aaronburtle) - PR: [Add Engine Telemetry - Phase 1](https://github.com/Azure/data-api-builder/pull/3825)
- [Add General properties to Application Name Telemetry (#3826)](https://github.com/Azure/data-api-builder/commit/6888332b35ddb11defad967cdce6aab93e0c3c65) - `2026-11-13T12:21:25Z` - aaronburtle (@aaronburtle) - PR: [Add General properties to Application Name Telemetry](https://github.com/Azure/data-api-builder/pull/3826)
- [Populate OpenAPI description from MCP configuration (#3885)](https://github.com/Azure/data-api-builder/commit/a9babf9d23d951030bdd25dff074cda688c9dd5d) - `2026-11-13T06:16:59Z` - Copilot (@Copilot) - PR: [Populate OpenAPI description from MCP configuration](https://github.com/Azure/data-api-builder/pull/3885)
- [Support XML data type for MSSQL (#3006)](https://github.com/Azure/data-api-builder/commit/9aea9c466e3d08d89796cacd676ca9586dbdcaca) - `2026-11-13T01:28:19Z` - Copilot (@Copilot) - PR: [Support XML data type for MSSQL](https://github.com/Azure/data-api-builder/pull/3006)
- [Update aspire packages (#3913)](https://github.com/Azure/data-api-builder/commit/af2f4bc7d8ad239e8f6bded62e75798571fd92d2) - `2026-11-13T00:27:04Z` - RubenCerna2079 (@RubenCerna2079) - PR: [Update aspire packages](https://github.com/Azure/data-api-builder/pull/3913)

### MicrosoftDocs/power-platform (5 commit(s), signal 80)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/0c624798cb8bc7e4e8cb46140f342643b6db0039) - `2026-11-13T19:04:33Z` - Learn Build Service GitHub App
- [Merge pull request #12184 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-platform/commit/84096c3b9f6ebce604ffa7881aeeec35284eb051) - `2026-11-13T19:03:04Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Clarify environment terminology in routing documentation (#12181)](https://github.com/MicrosoftDocs/power-platform/commit/4e9b6a5ed58ce20048373a4fca736647fb5afb7d) - `2026-11-13T17:01:11Z` - Sid Gundavarapu (@sidhartg)
- [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/5e9f6b370edf9a1a56b84d54f1aba5d8b6bf3179) - `2026-11-12T19:04:24Z` - Learn Build Service GitHub App
- [Merge pull request #12180 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-platform/commit/be0c24ffa52e1b6ccc9535f44c0277b2b3ee5b23) - `2026-11-12T19:02:50Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### dotnet/roslyn (5 commit(s), signal 80)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Partial members: avoid missing diagnostics from implementation-only s…](https://github.com/dotnet/roslyn/commit/99f9bfda78f882c6610fb349a75ab57746ab8460) - `2026-11-13T14:39:00Z` - Jan Jones (@jjonescz) - PR: [Partial members: avoid missing diagnostics from implementation-only semantic models](https://github.com/dotnet/roslyn/pull/86324)
- [Discard root compilation events in CompilationWithAnalyzers (#86347)](https://github.com/dotnet/roslyn/commit/6705f17e186664b3ff55ce362d16169a44fa0537) - `2026-11-13T11:14:51Z` - Callum (@callumok2004) - PR: [Discard root compilation events in CompilationWithAnalyzers](https://github.com/dotnet/roslyn/pull/86347)
- [[main] Source code updates from dotnet/dotnet (#86456)](https://github.com/dotnet/roslyn/commit/d31af711e72386db87ddaf2fa73f90812c187099) - `2026-11-13T03:53:46Z` - dotnet-maestro[bot] (@dotnet-maestro[bot]) - PR: [[main] Source code updates from dotnet/dotnet](https://github.com/dotnet/roslyn/pull/86456)
- [Register HotReloadProjectEventSubscriber brokered service (#86418)](https://github.com/dotnet/roslyn/commit/33a84789ae0ceb41e87a8d486504e150b0056c14) - `2026-11-12T22:20:53Z` - Tomáš Matoušek (@tmat) - PR: [Register HotReloadProjectEventSubscriber brokered service](https://github.com/dotnet/roslyn/pull/86418)
- [[main] Update dependencies from dotnet/roslyn (#86358)](https://github.com/dotnet/roslyn/commit/68ef2ac0ca4f1a04b5f79328fc84d4bb8b305e05) - `2026-11-12T19:48:57Z` - dotnet-maestro[bot] (@dotnet-maestro[bot]) - PR: [[main] Update dependencies from dotnet/roslyn](https://github.com/dotnet/roslyn/pull/86358)

### microsoft/amplifier-persona-workshop (5 commit(s), signal 85)

Tags: `human-authored, release, training`

- Release: [Persona Workshop 0.7.2](https://github.com/microsoft/amplifier-persona-workshop/releases/tag/v0.7.2) - `2026-11-13T09:29:57Z`
- [docs: link invited partners to contribution guidance (#17)](https://github.com/microsoft/amplifier-persona-workshop/commit/226b49f0f8b8aedb0ccebcceafba938140d88250) - `2026-11-13T09:49:15Z` - Brian Krabach (@bkrabach)
- [docs: align component boundaries with five primitives (#16)](https://github.com/microsoft/amplifier-persona-workshop/commit/f3dba948fed98dd3245f766a1b5738c13ff7b9f9) - `2026-11-13T05:43:17Z` - Brian Krabach (@bkrabach) - PR: [docs: align Workshop capabilities with five primitives](https://github.com/microsoft/amplifier-persona-workshop/pull/16)
- [docs: describe complete 0.7.2 native update behavior (#15)](https://github.com/microsoft/amplifier-persona-workshop/commit/24c3dd702a6ab9cd9c2c7699db45974c6558d71c) - `2026-11-13T00:14:57Z` - Brian Krabach (@bkrabach) - PR: [Describe the complete 0.7.2 native update behavior](https://github.com/microsoft/amplifier-persona-workshop/pull/15)
- [Keep native updates alive across managed application restarts (#14)](https://github.com/microsoft/amplifier-persona-workshop/commit/a4571d1d886f0af0a208309b820bcbb48b751aef) - `2026-11-12T23:50:22Z` - Brian Krabach (@bkrabach) - PR: [Keep native updates alive across managed application restarts](https://github.com/microsoft/amplifier-persona-workshop/pull/14)
- [Preserve native update journals while status is read (#13)](https://github.com/microsoft/amplifier-persona-workshop/commit/74355ccdbf77aedcbf67b6efdd6d0cc7ff744d52) - `2026-11-12T19:45:47Z` - Brian Krabach (@bkrabach) - PR: [Preserve native update journals while status is read (0.7.2)](https://github.com/microsoft/amplifier-persona-workshop/pull/13)

### MicrosoftDocs/powerapps-docs (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/powerapp…](https://github.com/MicrosoftDocs/powerapps-docs/commit/669d8bf95b53d47069414daf03893dc29f596f1f) - `2026-11-13T01:07:30Z` - Learn Build Service GitHub App
- [Merge pull request #12856 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/powerapps-docs/commit/2411f35d842eeae2db231169ee4fd536f8d14f53) - `2026-11-13T01:05:22Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update billing details for Dataverse MCP tools (#12853)](https://github.com/MicrosoftDocs/powerapps-docs/commit/8a635ff8c2b4cb76570a22629e44f518ed6d80b4) - `2026-11-12T21:52:49Z` - Kent Weare (@kewear)
- [Merging changes synced from https://github.com/MicrosoftDocs/powerapp…](https://github.com/MicrosoftDocs/powerapps-docs/commit/b2b1c76b51484d3d8b3293fc0e2bc95409bb3f90) - `2026-11-12T19:06:28Z` - Learn Build Service GitHub App
- [Merge pull request #12852 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/powerapps-docs/commit/887e65730860519cb84ecef9966d6976369276dd) - `2026-11-12T19:04:19Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### microsoft/kiota-dart (4 commit(s), signal 79)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #179 from jackson-asmith/fix/retry-unprocessed-mut…](https://github.com/microsoft/kiota-dart/commit/54d1f7b2e0bfa1c059ed0281811d9e0a29e8fedd) - `2026-11-13T20:20:15Z` - Vincent Biret (@baywet) - PR: [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-dart/pull/179)
- [docs(http): note the redirect detection limit for retryUnprocessedMut…](https://github.com/microsoft/kiota-dart/commit/49b2bffceeedfa3918bddb7297824e4b76f5906e) - `2026-11-13T18:49:59Z` - Jackson Smith (@jackson-asmith) - PR: [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-dart/pull/179)
- [fix(http): don't resend a POST that a redirect turned into a GET](https://github.com/microsoft/kiota-dart/commit/d7979fa41697b727856fed43d11b6af5ac84f31d) - `2026-11-13T18:09:43Z` - Jackson Smith (@jackson-asmith) - PR: [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-dart/pull/179)
- [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-dart/commit/7e9987ef96c4cd393c3906d14f1901c078374f9c) - `2026-11-13T17:49:04Z` - Jackson Smith (@jackson-asmith) - PR: [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-dart/pull/179)

### Azure/awesome-azd (4 commit(s), signal 89)

Tags: `docs, human-authored, release-language, watchlist`

- [Refactor and clean up the Awesome azd site architecture (#1116)](https://github.com/Azure/awesome-azd/commit/102cecb40dcf1625a5ac819f96f3979ef36d5fbe) - `2026-11-13T18:09:09Z` - hemarina (@hemarina) - PR: [Refactor and clean up the Awesome azd site architecture](https://github.com/Azure/awesome-azd/pull/1116)
- [chore(deps): bump peter-evans/create-pull-request from 8.1.1 to 8.1.2…](https://github.com/Azure/awesome-azd/commit/7f56a4cb6e0a6400eb0e6e36d4523957c9a1cade) - `2026-11-13T07:33:13Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump peter-evans/create-pull-request from 8.1.1 to 8.1.2](https://github.com/Azure/awesome-azd/pull/1114)
- [feat: add template detail pages (#1112)](https://github.com/Azure/awesome-azd/commit/21dd8e96743ae850e00ad6745744237a0595a002) - `2026-11-13T03:32:14Z` - hemarina (@hemarina) - PR: [feat: add template detail pages](https://github.com/Azure/awesome-azd/pull/1112)
- [Validate repository metrics during website release (#1111)](https://github.com/Azure/awesome-azd/commit/a640f50f59e74905a7599eaae03a5fde2210384b) - `2026-11-12T23:52:19Z` - hemarina (@hemarina) - PR: [Validate repository metrics during website release](https://github.com/Azure/awesome-azd/pull/1111)

### dotnet/docs (4 commit(s), signal 89)

Tags: `docs, human-authored, release-language, watchlist`

- [Complete remaining .NET 11 GA documentation updates (#56878)](https://github.com/dotnet/docs/commit/94b7dca39d8dca4374f326176874381661f4dd59) - `2026-11-13T15:43:52Z` - Copilot (@Copilot) - PR: [Complete remaining .NET 11 GA documentation updates](https://github.com/dotnet/docs/pull/56878)
- [Fix MCP client quickstart failing on Linux and macOS (#56797)](https://github.com/dotnet/docs/commit/f7f6fee94d850f9ce925e81d9b9d7013794f5cd5) - `2026-11-13T15:15:12Z` - Henrique Mauri (@hgmauri) - PR: [Fix MCP client quickstart failing on Linux and macOS](https://github.com/dotnet/docs/pull/56797)
- [Clarify TRX report metadata requirements (#56891)](https://github.com/dotnet/docs/commit/dd99230ce7a7e9f1e903546ce34c434766814644) - `2026-11-13T14:09:27Z` - Amaury Levé (@Evangelink) - PR: [Clarify required and optional TRX report metadata](https://github.com/dotnet/docs/pull/56891)
- [docs: fix duplicate word in mstest0017 analyzer rule (#56880)](https://github.com/dotnet/docs/commit/18b836ef5d4cca499abb090d10937161bb3b6a07) - `2026-11-13T08:25:00Z` - Subham Kumar Keshari (@kumar246subham-afk) - PR: [docs: fix duplicate word in mstest0017 analyzer rule](https://github.com/dotnet/docs/pull/56880)

### Azure/AI-Landing-Zones (4 commit(s), signal 79)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [docs(agent-landing-zone): document isolated hub, hosted agent, and ga…](https://github.com/Azure/AI-Landing-Zones/commit/8e72835f11b9c41d3e197dfaa997d2f1ea378575) - `2026-11-13T13:45:57Z` - Paulo Lacerda (@placerda)
- [Merge branch 'feature/optional-app-configuration' of https://github.c…](https://github.com/Azure/AI-Landing-Zones/commit/9cda911b12189f284245720550a49a6f2a34e17e) - `2026-11-13T01:42:08Z` - Paulo Lacerda (@placerda)
- [docs: refresh validated planner prices](https://github.com/Azure/AI-Landing-Zones/commit/f1481fc2389c150cbec7b2644d61547d60bf6e35) - `2026-11-13T00:23:23Z` - github-actions[bot] (@github-actions[bot])
- [Document provider-owned deployment metadata and optional configuration](https://github.com/Azure/AI-Landing-Zones/commit/54458d3bcf40e4b0233d2324c2bbb73ff0b803bd) - `2026-11-12T20:18:00Z` - Paulo Lacerda (@placerda)

### OfficeDev/Microsoft-Teams-Samples (4 commit(s), signal 79)

Tags: `human-authored, product:Azure SDK, samples, watchlist`

- [Merge pull request #2412 from OfficeDev/dependabot/npm_and_yarn/sampl…](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/93cc9c4d3d21fb3f2c4ab40f599ba553fd4705a2) - `2026-11-13T10:56:34Z` - Harikrishnan-MSFT (@Harikrishnan-MSFT) - PR: [Bump node-forge from 1.4.0 to 1.4.3 in /samples/tab-add-in-combined/nodejs/add-in](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2412)
- [Merge pull request #2414 from OfficeDev/dependabot/npm_and_yarn/sampl…](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/f8753f61801a4d8e1bb8094f3b529ecc42c18bf6) - `2026-11-13T10:56:16Z` - Harikrishnan-MSFT (@Harikrishnan-MSFT) - PR: [Bump protobufjs from 7.3.2 to 7.6.6 in /samples/TeamsSDK/Archived/bot-virtual-assistant/echo-skill-bot](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2414)
- [Bump protobufjs](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/176f31e4939b85e68d89c0e67e1360a6e3742037) - `2026-11-13T07:56:02Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump protobufjs from 7.3.2 to 7.6.6 in /samples/TeamsSDK/Archived/bot-virtual-assistant/echo-skill-bot](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2414)
- [Bump node-forge in /samples/tab-add-in-combined/nodejs/add-in](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/f346cdf4d5dd180414d0bc7aca3a3f642e2661eb) - `2026-11-13T07:36:12Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump node-forge from 1.4.0 to 1.4.3 in /samples/tab-add-in-combined/nodejs/add-in](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2412)

### microsoftgraph/microsoft-graph-docs-contrib (4 commit(s), signal 104)

Tags: `docs, human-authored, product:Azure AI, product:Microsoft Graph, security, watchlist`

- [Merge pull request #10094 from microsoftgraph/main639301273377103361s…](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/2329b086341e67d36de55a5743af1a47224046ca) - `2026-11-13T00:42:35Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10094)
- [Merging changes synced from https://github.com/microsoftgraph/microso…](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/67e1e81cc5035d9270ecdac1cb3f5e2f9100b31e) - `2026-11-13T00:42:12Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10094)
- [Merge pull request #29918 from microsoftgraph/main](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/b4b6c1a179c5dc1a7e56f50bfd7880eac87bb7e9) - `2026-11-13T00:35:12Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10094)
- [Fix AgenticSecurity examples and remove beta disclaimers (#29908)](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/658ab118249a8b9fe33e60d3bbeb328f8958e870) - `2026-11-13T00:01:50Z` - berver (@berver) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10094)

### microsoftgraph/msgraph-sample-github-connector-typescript (4 commit(s), signal 19)

Tags: `bot-only, dependency-noise, product:Microsoft Graph, samples, watchlist`

- [Merge pull request #310 from microsoftgraph/dependabot/npm_and_yarn/e…](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/commit/56a959aac31962d02808ab615dd76776c2ec84ee) - `2026-11-13T00:27:35Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump eslint-plugin-prettier from 5.2.6 to 5.5.7](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/pull/310)
- [Bump eslint-plugin-prettier from 5.2.6 to 5.5.7](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/commit/be5aca2236e680871f457b09da03b2bb482e249d) - `2026-11-13T00:26:19Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump eslint-plugin-prettier from 5.2.6 to 5.5.7](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/pull/310)
- [Merge pull request #309 from microsoftgraph/dependabot/npm_and_yarn/m…](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/commit/753e29f648fbc2da1c62ad6ee4c590c1b4a6cb17) - `2026-11-13T00:24:01Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump marked from 18.1.3 to 18.2.0](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/pull/309)
- [Bump marked from 18.1.3 to 18.2.0](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/commit/393946d66b8b3553a4a5a47af80680beb3eecd3e) - `2026-11-13T00:22:56Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump marked from 18.1.3 to 18.2.0](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/pull/309)

### MicrosoftDocs/anyscale-on-azure-docs (4 commit(s), signal 89)

Tags: `docs, human-authored, release-language, watchlist`

- [Repo sync for protected branch (#6)](https://github.com/MicrosoftDocs/anyscale-on-azure-docs/commit/db78f147b4462d2ea11eb26faa2281e456362766) - `2026-11-12T23:34:02Z` - Jason Howell (@JasonWHowell) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/anyscale-on-azure-docs/pull/6)
- [Repo sync for protected branch (#7)](https://github.com/MicrosoftDocs/anyscale-on-azure-docs/commit/7a93ae35957e25c39e1f11599b9a90a76f8c71df) - `2026-11-12T23:33:16Z` - Jason Howell (@JasonWHowell) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/anyscale-on-azure-docs/pull/7)
- [Merge branch 'main' into main639295651279707680sync_temp](https://github.com/MicrosoftDocs/anyscale-on-azure-docs/commit/04741848dc393bd4bbb3ec683e7bbdaf8222f796) - `2026-11-12T23:30:44Z` - Jason Howell (@JasonWHowell) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/anyscale-on-azure-docs/pull/7)
- [Anyscale on Azure docs release-20260923 (#64) (#4)](https://github.com/MicrosoftDocs/anyscale-on-azure-docs/commit/52924ec7a348e2ad031e3ff4ffeda70dc0fa86b1) - `2026-11-12T23:29:44Z` - Jason Howell (@JasonWHowell) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/anyscale-on-azure-docs/pull/4)

### Azure/azure-iot-sdk-node (4 commit(s), signal 79)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Merge pull request #1270 from Azure/maximsemenov/add-credscan-post-an…](https://github.com/Azure/azure-iot-sdk-node/commit/aecebbe5c8cad7b7c5cf810683d9a6c9478456a7) - `2026-11-12T23:00:17Z` - Ewerton Scaboro da Silva (@ewertons) - PR: [ci: run CredScan and break the build on findings](https://github.com/Azure/azure-iot-sdk-node/pull/1270)
- [Merge branch 'main' into maximsemenov/add-credscan-post-analysis](https://github.com/Azure/azure-iot-sdk-node/commit/c9d62f300f707f7d739169ccb3a7ffc6b4d31cf9) - `2026-11-12T21:39:15Z` - Maxim Semenov (@maximsemenov80) - PR: [ci: run CredScan and break the build on findings](https://github.com/Azure/azure-iot-sdk-node/pull/1270)
- [Merge pull request #1271 from Azure/maximsemenov/remove-legacy-codeql…](https://github.com/Azure/azure-iot-sdk-node/commit/e5e3cfacfafb770330f9625c2cb380d3f4e5f5d2) - `2026-11-12T21:33:39Z` - Ewerton Scaboro da Silva (@ewertons) - PR: [ci: remove the legacy CodeQL workflow](https://github.com/Azure/azure-iot-sdk-node/pull/1271)
- [ci: scope Post Analysis to CredScan with the PostAnalysis@2 inputs](https://github.com/Azure/azure-iot-sdk-node/commit/d6716dc653d3c710540d6db7730d6fcbbdb8dca0) - `2026-11-12T19:14:47Z` - maximsemenov (@maximsemenov80) - PR: [ci: run CredScan and break the build on findings](https://github.com/Azure/azure-iot-sdk-node/pull/1270)

### microsoft/kiota-serialization-form-go (3 commit(s), signal 88)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #172 from microsoft/dependabot/go_modules/github.c…](https://github.com/microsoft/kiota-serialization-form-go/commit/bc960c9b64b6e43027686b7c928d1f8ef720590b) - `2026-11-13T19:56:25Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.0 to 1.12.1](https://github.com/microsoft/kiota-serialization-form-go/pull/172)
- [build(deps): bump github.com/microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-serialization-form-go/commit/386224744dfa0fb821513cdb85d4fe670ff3a57f) - `2026-11-13T19:52:39Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.0 to 1.12.1](https://github.com/microsoft/kiota-serialization-form-go/pull/172)
- [Merge pull request #170 from hardikkaurani/fix/union-and-intersection…](https://github.com/microsoft/kiota-serialization-form-go/commit/ec6aaad8307a7d041678011688f2debadb52a448) - `2026-11-12T19:56:31Z` - Vincent Biret (@baywet) - PR: [fix(form): allow root delegation in WriteObjectValue for union and intersection types](https://github.com/microsoft/kiota-serialization-form-go/pull/170)

### MicrosoftDocs/dynamics365smb-devitpro-pb (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/61c96140b602cd44a3978da72b67766aeacb5590) - `2026-11-13T19:03:18Z` - Learn Build Service GitHub App
- [Merge pull request #8157 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/89992246f594fca8fde3a442ddec5d162e50a944) - `2026-11-13T19:02:31Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Refresh admin center content (#8156)](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/80518d538879211bac90ec42438f1c9d1dd5d779) - `2026-11-13T14:44:04Z` - jswymer (@jswymer)

### microsoft/kiota-typescript (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [feat(http): add option to retry only unprocessed mutations (#2230)](https://github.com/microsoft/kiota-typescript/commit/54e0562e71e86d77fa0a35d664c58c76a59778cd) - `2026-11-13T17:40:29Z` - Jackson Smith (@jackson-asmith) - PR: [feat(http): add option to retry only unprocessed mutations](https://github.com/microsoft/kiota-typescript/pull/2230)
- [auto dependabot: bump webdriverio from 10.1.0 to 10.2.0 (#2228)](https://github.com/microsoft/kiota-typescript/commit/4d9ec51f010539240be4ce28631131efe3dd864d) - `2026-11-13T14:36:56Z` - dependabot[bot] (@dependabot[bot]) - PR: [auto dependabot: bump webdriverio from 10.1.0 to 10.2.0](https://github.com/microsoft/kiota-typescript/pull/2228)
- [fix(form): preserve equals delimiters, support empty values, and seri…](https://github.com/microsoft/kiota-typescript/commit/19e5f13af48f75fc56e20fbe5592a96e2a2d2c40) - `2026-11-13T14:12:44Z` - Hardik K (@hardikkaurani) - PR: [fix(form): preserve equals delimiters, support empty values, and serialize zeros](https://github.com/microsoft/kiota-typescript/pull/2218)

### Azure-Samples/AzureMapsCodeSamples (3 commit(s), signal 88)

Tags: `human-authored, release-language, samples, watchlist`

- [Merge pull request #214 from yulinscottkang/overture](https://github.com/Azure-Samples/AzureMapsCodeSamples/commit/9aa66c4e2680a7743d3692e79be7b4166a15eed3) - `2026-11-13T02:43:59Z` - yulinscottkang (@yulinscottkang) - PR: [Always use the latest Overture release version](https://github.com/Azure-Samples/AzureMapsCodeSamples/pull/214)
- [fix filter](https://github.com/Azure-Samples/AzureMapsCodeSamples/commit/f31cd024a41fe2ae60a524261359633ddd5a5691) - `2026-11-13T02:17:50Z` - Scott Kang - PR: [Always use the latest Overture release version](https://github.com/Azure-Samples/AzureMapsCodeSamples/pull/214)
- [use the latest overture release](https://github.com/Azure-Samples/AzureMapsCodeSamples/commit/9941b599666468dbc5ce37fc2dcd964e5b16bcc8) - `2026-11-13T02:03:20Z` - Scott Kang - PR: [Always use the latest Overture release version](https://github.com/Azure-Samples/AzureMapsCodeSamples/pull/214)

### MicrosoftDocs/azure-docs-sdk-dotnet (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [CI Update](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/8c91977e3e5d85a1fb9ce7ed53857585c594f17d) - `2026-11-13T02:11:05Z` - docsreference@microsoft.com
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/6903e3826896eaabe5001fd042bded18ecf1c83f) - `2026-11-13T00:32:55Z` - azure-sdk (@azure-sdk)
- [Update docs CI configuration](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/64b896fa4f80a0367c5ee355b11b29400b5e4087) - `2026-11-12T23:51:09Z` - azure-sdk (@azure-sdk)

### Azure/azure-sdk-for-rust (3 commit(s), signal 103)

Tags: `docs, human-authored, product:Azure SDK, security, watchlist`

- [Add AADSTS700213 error to Identity TSG (#5594)](https://github.com/Azure/azure-sdk-for-rust/commit/b485409baf6e24ce198b028fb6d1c5a54a0e6d4c) - `2026-11-13T02:08:33Z` - Heath Stewart (@heaths) - PR: [Add AADSTS700213 error to Identity TSG](https://github.com/Azure/azure-sdk-for-rust/pull/5594)
- [Bump github/gh-aw-actions/setup-cli from 1.0.1 to 1.2.0 in the github…](https://github.com/Azure/azure-sdk-for-rust/commit/4e0804582bb1e205fdfa3eae129fe03c47bec387) - `2026-11-12T19:31:19Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump github/gh-aw-actions/setup-cli from 1.0.1 to 1.2.0 in the github-actions group](https://github.com/Azure/azure-sdk-for-rust/pull/5592)
- [Add GitHubActionsCredential to azure_identity (#5588)](https://github.com/Azure/azure-sdk-for-rust/commit/403d597280cc140f7bb8020882c9c92482df9655) - `2026-11-12T19:06:44Z` - Copilot (@Copilot) - PR: [Add GitHubActionsCredential to azure_identity](https://github.com/Azure/azure-sdk-for-rust/pull/5588)

### dotnet/AspNetCore.Docs (3 commit(s), signal 53)

Tags: `docs, human-authored, release-language`

- [Remove redundant sample folder versions from main (#38150)](https://github.com/dotnet/AspNetCore.Docs/commit/53d05ee9faf3cfe577c6180a0a4c6966d8396ffd) - `2026-11-13T01:09:50Z` - Genevieve Warren (@gewarren) - PR: [Remove redundant sample folder versions](https://github.com/dotnet/AspNetCore.Docs/pull/38150)
- [Archive in-memory caching docs (#38136)](https://github.com/dotnet/AspNetCore.Docs/commit/9bb8129a2888bf65b8cc84ef838657dcff30ba68) - `2026-11-12T22:21:57Z` - Genevieve Warren (@gewarren) - PR: [Archive in-memory caching docs](https://github.com/dotnet/AspNetCore.Docs/pull/38136)
- [Update workflow for Snippets 5000 (#38148)](https://github.com/dotnet/AspNetCore.Docs/commit/0dcefbc48b7848169ac976b8352bc340351c2081) - `2026-11-12T21:32:39Z` - Genevieve Warren (@gewarren) - PR: [Update workflow for Snippets 5000](https://github.com/dotnet/AspNetCore.Docs/pull/38148)

### Azure/kars (3 commit(s), signal 143)

Tags: `docs, human-authored, release, security, watchlist`

- Release: [v0.2.0-beta.6](https://github.com/Azure/kars/releases/tag/v0.2.0-beta.6) - `2026-11-13T14:10:20Z`
- [Merge pull request #620 from Azure/pallakatos-crypto-bigint-remediation](https://github.com/Azure/kars/commit/f89953b0e477d324291b482d7647f5dfa2413253) - `2026-11-12T22:02:10Z` - Pal Lakatos-Toth (@pallakatos) - PR: [Remediate crypto-bigint timing advisory](https://github.com/Azure/kars/pull/620)
- [Record explicit maintainer security audit sign-off](https://github.com/Azure/kars/commit/50aefe35a654aa90624d0ac8bbf0d9e437e28a6b) - `2026-11-12T21:17:21Z` - pallakatos (@pallakatos) - PR: [Remediate crypto-bigint timing advisory](https://github.com/Azure/kars/pull/620)
- [Simplify overlay readiness check](https://github.com/Azure/kars/commit/2559e384cc66f1499fb990fd2e9b781ea90846b9) - `2026-11-12T19:03:56Z` - pallakatos (@pallakatos) - PR: [Remediate crypto-bigint timing advisory](https://github.com/Azure/kars/pull/620)

### Azure-Samples/semantic-kernel-customer-assistant-demo-java (3 commit(s), signal 43)

Tags: `human-authored, samples`

- [Merge pull request #99 from Azure-Samples/dependabot/npm_and_yarn/src…](https://github.com/Azure-Samples/semantic-kernel-customer-assistant-demo-java/commit/233da5c7b061dd1b88353ae5d9879e935a59e8ad) - `2026-11-12T21:14:16Z` - Martijn Verburg (@karianna) - PR: [Bump node-forge from 1.4.2 to 1.4.3 in /src/main/webapp](https://github.com/Azure-Samples/semantic-kernel-customer-assistant-demo-java/pull/99)
- [Bump node-forge from 1.4.2 to 1.4.3 in /src/main/webapp](https://github.com/Azure-Samples/semantic-kernel-customer-assistant-demo-java/commit/b18118a9126931807ca0ddc43683227db7a3a5ae) - `2026-11-12T20:44:02Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump node-forge from 1.4.2 to 1.4.3 in /src/main/webapp](https://github.com/Azure-Samples/semantic-kernel-customer-assistant-demo-java/pull/99)
- [Merge pull request #98 from Azure-Samples/dependabot/github_actions/g…](https://github.com/Azure-Samples/semantic-kernel-customer-assistant-demo-java/commit/d3817ecf7e3c6258be5ab2cb6e189b1abae68349) - `2026-11-12T20:04:58Z` - Martijn Verburg (@karianna) - PR: [Bump actions/setup-java from 6.1.0 to 6.2.0 in the github-actions group](https://github.com/Azure-Samples/semantic-kernel-customer-assistant-demo-java/pull/98)

### MicrosoftDocs/azure-docs (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-do…](https://github.com/MicrosoftDocs/azure-docs/commit/2acd0be132de9796753b950f5c31f449bc83847e) - `2026-11-12T21:12:22Z` - Learn Build Service GitHub App
- [Merge pull request #322486 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-docs/commit/98e389cae37ee97791d4905411bcdfc65dcdb150) - `2026-11-12T21:11:31Z` - Alma Jenks (@v-alje)
- [Update URL for Azure Data Share deprecation guidance (#322484)](https://github.com/MicrosoftDocs/azure-docs/commit/0a403a6c50d920b29d6f71202fefaf1ef83421a5) - `2026-11-12T20:56:24Z` - Sita Dontharaju (@sidontha)

### Azure-Samples/ms-events-session-guide (3 commit(s), signal 43)

Tags: `human-authored, samples`

- [Add event-specific registration with a persistent event action (#10)](https://github.com/Azure-Samples/ms-events-session-guide/commit/6d169113add4a5ca632f916f93d4ab06f1815eaf) - `2026-11-12T20:54:06Z` - Artem Lovan (@artlovan) - PR: [Add official event registration and a persistent registration action](https://github.com/Azure-Samples/ms-events-session-guide/pull/10)
- [Report browser regression automatically on pull requests (#9)](https://github.com/Azure-Samples/ms-events-session-guide/commit/0cf377f7a965dee01affe2014d881f35aeb38927) - `2026-11-12T19:30:24Z` - Artem Lovan (@artlovan) - PR: [Report browser regression automatically on pull requests](https://github.com/Azure-Samples/ms-events-session-guide/pull/9)
- [Stabilize hosted browser regression and toast interactions (#8)](https://github.com/Azure-Samples/ms-events-session-guide/commit/9afa43648e7466ade1f708b35b377d10c55ef2a1) - `2026-11-12T19:17:47Z` - Artem Lovan (@artlovan) - PR: [Stabilize hosted browser regression and toast interactions](https://github.com/Azure-Samples/ms-events-session-guide/pull/8)

### microsoft/finops-toolkit (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Microsoft Graph, product:PowerShell, watchlist`

- [fix(finops-hub): Paginate Azure Resource Graph queries past 1,000 row…](https://github.com/microsoft/finops-toolkit/commit/f0e73aaba8ec0720f79a1dbdbe0ea7997aa87491) - `2026-11-13T20:31:56Z` - Michael Flanakin (@flanakin) - PR: [fix(finops-hub): Paginate Azure Resource Graph queries past 1,000 rows](https://github.com/microsoft/finops-toolkit/pull/2330)
- [feat(commands): Add auto mode, pr-loop, and pr-sweep PR commands (#2402)](https://github.com/microsoft/finops-toolkit/commit/faefda64c65575b3b5a5d25df71950d810042c72) - `2026-11-13T20:29:20Z` - Michael Flanakin (@flanakin) - PR: [feat(commands): Add auto mode, pr-loop, and pr-sweep PR commands](https://github.com/microsoft/finops-toolkit/pull/2402)

### microsoft/MegaDetector-Acoustic (2 commit(s), signal 42)

Tags: `human-authored, training`

- [Merge pull request #14 from microsoft/docs/fix-retired-framework-links](https://github.com/microsoft/MegaDetector-Acoustic/commit/2739db392f0f2f6fdb9d6c8780aab0a378e41258) - `2026-11-13T18:59:35Z` - Zhongqi Miao (@zhmiao) - PR: [docs: repair retired framework links](https://github.com/microsoft/MegaDetector-Acoustic/pull/14)
- [docs: repair retired framework links](https://github.com/microsoft/MegaDetector-Acoustic/commit/37a299e0c96c570f6655522a84198388376d0682) - `2026-11-13T18:59:15Z` - zhmiao (@zhmiao) - PR: [docs: repair retired framework links](https://github.com/microsoft/MegaDetector-Acoustic/pull/14)

### microsoft/kiota-dotnet (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [fix(abstractions): prevent concurrent double-wrapping in ApiClientBui…](https://github.com/microsoft/kiota-dotnet/commit/efee54c5c88c4eaebf679d4225e17bd331f80028) - `2026-11-13T18:44:40Z` - Hardik K (@hardikkaurani) - PR: [fix(abstractions): prevent concurrent double-wrapping in ApiClientBuilder backing store enablement](https://github.com/microsoft/kiota-dotnet/pull/862)
- [feat(http): add option to skip retrying non-idempotent requests when …](https://github.com/microsoft/kiota-dotnet/commit/446a46b0f27d51a3b47d18244fb8ceea41ff67ea) - `2026-11-13T14:34:01Z` - Jackson Smith (@jackson-asmith) - PR: [feat(http): add option to skip retrying non-idempotent requests when the outcome is unknown](https://github.com/microsoft/kiota-dotnet/pull/864)

### microsoft/foundry-local-on-windowsserver-samples (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, product:Azure AI, samples, watchlist`

- [Bump hono from 4.13.13 to 4.13.18 in /MCP-ToolCalling/mcp-servers/wea…](https://github.com/microsoft/foundry-local-on-windowsserver-samples/commit/16293c97a5b86c16707f668b384752cbf1f135e2) - `2026-11-13T18:19:28Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump hono from 4.13.13 to 4.13.18 in /MCP-ToolCalling/mcp-servers/weather](https://github.com/microsoft/foundry-local-on-windowsserver-samples/pull/52)
- [Bump @hono/node-server from 2.1.5 to 2.1.8 in /MCP-ToolCalling/mcp-se…](https://github.com/microsoft/foundry-local-on-windowsserver-samples/commit/7cc0fbfd0cc7bffabb91f7556b1203bce79134f1) - `2026-11-13T18:18:40Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump @hono/node-server from 2.1.5 to 2.1.8 in /MCP-ToolCalling/mcp-servers/weather](https://github.com/microsoft/foundry-local-on-windowsserver-samples/pull/51)

### microsoft/kiota-authentication-azure-go (2 commit(s), signal 27)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #255 from microsoft/dependabot/go_modules/github.c…](https://github.com/microsoft/kiota-authentication-azure-go/commit/7e6f9c8856ad4be801c1b3b74dddaf3e33ad6d57) - `2026-11-13T18:15:17Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.0 to 1.12.1](https://github.com/microsoft/kiota-authentication-azure-go/pull/255)
- [build(deps): bump github.com/microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-authentication-azure-go/commit/ac42227a9c9d8e18f8e21d003aa988ca040238b8) - `2026-11-13T17:12:30Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.0 to 1.12.1](https://github.com/microsoft/kiota-authentication-azure-go/pull/255)

### microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning (2 commit(s), signal 102)

Tags: `human-authored, samples, security, watchlist`

- [Merge pull request #25 from microsoft/user/datra/securityIssueFix](https://github.com/microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning/commit/3b604cf448139f597e333147528af02897b33fdd) - `2026-11-13T17:49:08Z` - David Tran (@ddavidtran) - PR: [Harden demand forecasting template identity resolution and relay authentication](https://github.com/microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning/pull/25)
- [Pin forecast identities and validate relay caller tokens](https://github.com/microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning/commit/a8e42b86693073d756010d995d119551ace75a5f) - `2026-11-12T22:33:52Z` - David Tran (@ddavidtran) - PR: [Harden demand forecasting template identity resolution and relay authentication](https://github.com/microsoft/Templates-For-Dynamics-365-Supply-Chain-Management-Demand-Forecasting-With-Azure-Machine-Learning/pull/25)

### microsoftgraph/msgraph-sample-github-connector-dotnet (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, product:Microsoft Graph, samples, watchlist`

- [Merge pull request #133 from microsoftgraph/dependabot/github_actions…](https://github.com/microsoftgraph/msgraph-sample-github-connector-dotnet/commit/38f1d03d67db6d6d2aa94e76334883a7ef0094b9) - `2026-11-13T16:56:13Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump actions/setup-dotnet from 6.0.0 to 6.1.0 in the github-actions group](https://github.com/microsoftgraph/msgraph-sample-github-connector-dotnet/pull/133)
- [Bump actions/setup-dotnet](https://github.com/microsoftgraph/msgraph-sample-github-connector-dotnet/commit/a2991d4afc5e6982b1813882db8209a91e2297dc) - `2026-11-13T16:54:54Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-dotnet from 6.0.0 to 6.1.0 in the github-actions group](https://github.com/microsoftgraph/msgraph-sample-github-connector-dotnet/pull/133)

### Azure-Samples/ms-identity-ciam-native-auth-ios-sample (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Merge pull request #52 from Azure-Samples/antrix1989-ciam-v2-sample-i…](https://github.com/Azure-Samples/ms-identity-ciam-native-auth-ios-sample/commit/85ef82afd59572ade876011bad516fd631761dd4) - `2026-11-13T16:27:24Z` - Sergei Demchenko (@antrix1989) - PR: [v2 sample integration](https://github.com/Azure-Samples/ms-identity-ciam-native-auth-ios-sample/pull/52)
- [docs: update README for MSAL 2.18.1](https://github.com/Azure-Samples/ms-identity-ciam-native-auth-ios-sample/commit/a37d6f068266a6220bdbd1d68f2f731ee9e688a2) - `2026-11-12T21:50:32Z` - Sergey Demchenko (@antrix1989) - PR: [v2 sample integration](https://github.com/Azure-Samples/ms-identity-ciam-native-auth-ios-sample/pull/52)

### microsoftgraph/msgraph-search-connector-sample (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, product:Microsoft Graph, samples, watchlist`

- [Merge pull request #121 from microsoftgraph/dependabot/github_actions…](https://github.com/microsoftgraph/msgraph-search-connector-sample/commit/99102290e1e80c65bd360a42a423ed81c01db226) - `2026-11-13T11:43:22Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump actions/setup-dotnet from 6.0.0 to 6.1.0](https://github.com/microsoftgraph/msgraph-search-connector-sample/pull/121)
- [Bump actions/setup-dotnet from 6.0.0 to 6.1.0](https://github.com/microsoftgraph/msgraph-search-connector-sample/commit/06c790b71c856ecd4f1ef25c79356d3cafc4dc40) - `2026-11-13T11:42:39Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-dotnet from 6.0.0 to 6.1.0](https://github.com/microsoftgraph/msgraph-search-connector-sample/pull/121)

### Azure-Samples/Spec2Cloud (2 commit(s), signal 0)

Tags: `bot-only, samples`

- [Update templates.json [automated]](https://github.com/Azure-Samples/Spec2Cloud/commit/6e67847a928519fbb893a65fe518935c792dcd7f) - `2026-11-13T11:04:44Z` - github-actions[bot] (@github-actions[bot])
- [Update templates.json [automated]](https://github.com/Azure-Samples/Spec2Cloud/commit/1db6c96ef3517f63331128ad66d84797d2916453) - `2026-11-13T10:04:58Z` - github-actions[bot] (@github-actions[bot])

### microsoft/amplifier-acp-lab (2 commit(s), signal 42)

Tags: `human-authored, training`

- [docs: link invited partners to contribution guidance (#10)](https://github.com/microsoft/amplifier-acp-lab/commit/a33195ca6ea98d5f24e82ae771e34b728b0abb70) - `2026-11-13T09:36:32Z` - Brian Krabach (@bkrabach) - PR: [docs: guide invited partners to the shared contribution path](https://github.com/microsoft/amplifier-acp-lab/pull/10)
- [docs: align component boundaries with five primitives (#9)](https://github.com/microsoft/amplifier-acp-lab/commit/199d1b37d7520d580d60b35698cf308fe59873f6) - `2026-11-13T05:11:24Z` - Brian Krabach (@bkrabach) - PR: [docs: align Lab evaluation boundaries with five primitives](https://github.com/microsoft/amplifier-acp-lab/pull/9)

### Azure-Samples/iot-edge-opc-plc (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, product:Azure SDK, samples, watchlist`

- [Bump Microsoft.NET.Test.Sdk from 18.11.0 to 18.12.0 (#582)](https://github.com/Azure-Samples/iot-edge-opc-plc/commit/82d2422a0af797faf069757baf665470bbec214d) - `2026-11-13T08:45:33Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.NET.Test.Sdk from 18.11.0 to 18.12.0](https://github.com/Azure-Samples/iot-edge-opc-plc/pull/582)
- [Bump Microsoft.SourceLink.GitHub from 10.0.403 to 11.0.100 (#583)](https://github.com/Azure-Samples/iot-edge-opc-plc/commit/992d37f82625408d081f35caf28690b115be740b) - `2026-11-13T08:44:56Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.SourceLink.GitHub from 10.0.403 to 11.0.100](https://github.com/Azure-Samples/iot-edge-opc-plc/pull/583)

### Azure-Samples/functions-quickstart-dotnet-azd-service-bus (2 commit(s), signal 77)

Tags: `human-authored, product:Azure SDK, samples, watchlist`

- [Improve Service Bus sample deployment and telemetry (#5)](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-service-bus/commit/408e2b5eab339d21f7a7926b917b0d69180829e6) - `2026-11-13T06:26:04Z` - Manvir Kaur (@manvkaur) - PR: [Improve Service Bus sample deployment and telemetry](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-service-bus/pull/5)
- [Update Azure Functions SDK and target .NET 10 (#4)](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-service-bus/commit/2b81e9958fba2da077d4b227a189e086d76a2194) - `2026-11-13T03:13:11Z` - Glenn Gailey (@ggailey777) - PR: [Update Azure Functions SDK and target .NET 10](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-service-bus/pull/4)

### Azure-Samples/functions-quickstart-dotnet-azd-sql (2 commit(s), signal 77)

Tags: `human-authored, product:Azure SDK, samples, watchlist`

- [Fix several issues running on Windows (#12)](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-sql/commit/de313003515d11567c98b57503e50baf04432a3c) - `2026-11-13T04:59:50Z` - Glenn Gailey (@ggailey777) - PR: [Fix several issues running on Windows](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-sql/pull/12)
- [Update Azure Functions SDK and target .NET 10 (#15)](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-sql/commit/32e9a845fcd2cba89eadd73ad8262931cb8fe36c) - `2026-11-13T04:49:22Z` - Glenn Gailey (@ggailey777) - PR: [Update Azure Functions SDK and target .NET 10](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-sql/pull/15)

### Azure-Samples/functions-quickstart-dotnet-azd-eventhub (2 commit(s), signal 77)

Tags: `human-authored, product:Azure SDK, samples, watchlist`

- [Align Event Hub OpenTelemetry and tooling (#4)](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-eventhub/commit/0e41aa28cf2661784f371f806b4c588d93d3676f) - `2026-11-13T03:14:49Z` - Manvir Kaur (@manvkaur) - PR: [Align Event Hub OpenTelemetry and local tooling](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-eventhub/pull/4)
- [Update Azure Functions SDK and target .NET 10 (#3)](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-eventhub/commit/6fd7be8efbf28fe7c59c0fe813a1ac90da6db112) - `2026-11-13T02:06:14Z` - Glenn Gailey (@ggailey777) - PR: [Update Azure Functions SDK and target .NET 10](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-eventhub/pull/3)

### Azure-Samples/functions-quickstart-dotnet-azd-eventgrid-blob (2 commit(s), signal 77)

Tags: `human-authored, product:Azure SDK, samples, watchlist`

- [Migrate Blob sample telemetry to OpenTelemetry (#18)](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-eventgrid-blob/commit/50aad8eb13f46dec67558cb674f668127aa54f42) - `2026-11-13T03:14:32Z` - Manvir Kaur (@manvkaur) - PR: [Migrate Blob sample telemetry to OpenTelemetry](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-eventgrid-blob/pull/18)
- [Update Azure Functions SDK and target .NET 10 (#17)](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-eventgrid-blob/commit/7e03eda016e27f85a0a104ba49a64a1626ce62b9) - `2026-11-13T00:32:04Z` - Glenn Gailey (@ggailey777) - PR: [Update Azure Functions SDK and target .NET 10](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-eventgrid-blob/pull/17)

### microsoft/mcp-dotnet-samples (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Update metadata.json](https://github.com/microsoft/mcp-dotnet-samples/commit/35e3bd177003a61186a18ea86c0a6429bcf9b9ed) - `2026-11-13T03:11:06Z` - GitHub Actions (@actions-user)
- [Update metadata.json](https://github.com/microsoft/mcp-dotnet-samples/commit/40bdd0c3c3505880dc7e45c497ecb937e83116e5) - `2026-11-13T01:09:18Z` - GitHub Actions (@actions-user)

### Azure-Samples/azuresandbox (2 commit(s), signal 127)

Tags: `human-authored, release, release-language, samples, watchlist`

- Release: [Azure Sandbox v6.0.9](https://github.com/Azure-Samples/azuresandbox/releases/tag/v6.0.9) - `2026-11-13T02:20:22Z`
- [Merge pull request #1052 from Azure-Samples/vnext](https://github.com/Azure-Samples/azuresandbox/commit/67595f1d9e1c8c6bcad09723b72e22d5fad468a4) - `2026-11-13T00:43:43Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Release vnext to main](https://github.com/Azure-Samples/azuresandbox/pull/1052)
- [Merge pull request #1050 from Azure-Samples/fix/1048-vnet-app-blob-up…](https://github.com/Azure-Samples/azuresandbox/commit/f075be3918226b35f5abb6f93a20bbc8e1e3ec3e) - `2026-11-12T20:12:40Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Order vnet_app script uploads after blob private endpoint (#1048)](https://github.com/Azure-Samples/azuresandbox/pull/1050)

### microsoft/WindowsAppSDK (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [.NET Template Localization (Part 1): Add .NET template localization h…](https://github.com/microsoft/WindowsAppSDK/commit/ec2fd44f612649d6411a42191f073692ac37ecb7) - `2026-11-12T23:17:31Z` - Lauren Ciha (@lauren-ciha) - PR: [.NET Template Localization (Part 1): Add .NET template localization handoffs and status analysis](https://github.com/microsoft/WindowsAppSDK/pull/6964)
- [Deployment: derive Main/Singleton short tag via canonical v2 helper (…](https://github.com/microsoft/WindowsAppSDK/commit/c2dc593744c3c02dda341c2c37b4f144bbfd5cb4) - `2026-11-12T23:06:35Z` - agniuks (@agniuks) - PR: [Deployment: derive Main/Singleton short tag via canonical v2 helper (experimentalA fix)](https://github.com/microsoft/WindowsAppSDK/pull/6657)

### MicrosoftDocs/dynamics365smb-docs (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/63b153c765c680bc521ba67af7c56ed3f0c61306) - `2026-11-12T19:03:39Z` - Learn Build Service GitHub App
- [Merge pull request #5280 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/aeb78fd01d1d37ecdd53982d0449e7ace289573f) - `2026-11-12T19:02:47Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### microsoft/WindowsAppSDK-Samples (1 commit(s), signal 76)

Tags: `human-authored, product:Azure SDK, product:PowerShell, samples, watchlist`

- [Hydrate samples across .NET toolchains (#686)](https://github.com/microsoft/WindowsAppSDK-Samples/commit/671ddff695f4d45526f7e18362623228595dd5e9) - `2026-11-13T20:14:54Z` - Felipe G (@guimafelipe) - PR: [Hydrate samples across .NET toolchains](https://github.com/microsoft/WindowsAppSDK-Samples/pull/686)

### microsoft/XBOX-Godot-NetRumble (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Explain full lobby join failures (#35)](https://github.com/microsoft/XBOX-Godot-NetRumble/commit/d3842f4b5c0789650465517def8d4a18e3a41f94) - `2026-11-13T20:08:21Z` - James Lenell (@jameslen-atg) - PR: [Report full lobbies when joining matches](https://github.com/microsoft/XBOX-Godot-NetRumble/pull/35)

### Azure-Samples/flex-container-html2pdf-go (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Update README.md](https://github.com/Azure-Samples/flex-container-html2pdf-go/commit/dbc28e42160bffed69b00bc09b976db2892787f6) - `2026-11-13T20:06:57Z` - Madhura Bharadwaj (@MadhuraBharadwaj-MSFT)

### microsoft/web-iq-samples (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Foundry voice agent: use the current Auto mode value (#23)](https://github.com/microsoft/web-iq-samples/commit/89730aeb9fa5c92ca805f8e088195edaa378fd02) - `2026-11-13T19:53:51Z` - Luis Gonzalez (@LuigiDiMaui) - PR: [Foundry voice agent: use the current Auto mode value](https://github.com/microsoft/web-iq-samples/pull/23)

### microsoft/playwright-pytest (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [fix: send launch options to remote browsers with protocol option name…](https://github.com/microsoft/playwright-pytest/commit/d9f2810485e704560efc5ced1731215b7daddb1e) - `2026-11-13T19:17:04Z` - Yury Semikhatsky (@yury-s) - PR: [fix: send launch options to remote browsers with protocol option names](https://github.com/microsoft/playwright-pytest/pull/349)

### Azure-Samples/azure-cosmos-rust-nosql-api-samples (1 commit(s), signal 86)

Tags: `human-authored, product:Azure SDK, release-language, samples, watchlist`

- [Merge pull request #7 from TheovanKraay/sdk/rust-ga](https://github.com/Azure-Samples/azure-cosmos-rust-nosql-api-samples/commit/32d6b78325b5589c69d104a74bde1c5a2cb04f9f) - `2026-11-13T19:13:01Z` - Theo van Kraay (@TheovanKraay) - PR: [Refresh Rust samples for GA SDK 1.0.0](https://github.com/Azure-Samples/azure-cosmos-rust-nosql-api-samples/pull/7)

### dotnet/docs-mobile (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Document generic NSObject subclasses for .NET Apple platforms (#156)](https://github.com/dotnet/docs-mobile/commit/d43fafc4334b9cbc880b8ae206ff1f9dc49e222b) - `2026-11-13T19:12:29Z` - Rolf Bjarne Kvinge (@rolfbjarne) - PR: [Document generic NSObject subclasses for .NET Apple platforms](https://github.com/dotnet/docs-mobile/pull/156)

### Azure/azure-sdk (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Fix unknown names for .NET Azure.Provisioning libraries (#10410)](https://github.com/Azure/azure-sdk/commit/237194b479a4442d559f469eebe5d351f66e1fab) - `2026-11-13T19:03:56Z` - Lori Fraleigh (@lfraleigh) - PR: [Fix unknown names for .NET Azure.Provisioning libraries](https://github.com/Azure/azure-sdk/pull/10410)

### Azure-Samples/ms-identity-ciam-native-javascript-samples (1 commit(s), signal 76)

Tags: `human-authored, product:Azure SDK, samples, watchlist`

- [Add unified Native Auth V1 and V2 samples (#67)](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/commit/49c4e250a1e6eb97e2b813e9fce6670c996a2808) - `2026-11-13T18:49:54Z` - Yongdi Wang (@yongdiw) - PR: [Add unified Native Auth V1 and V2 samples](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/pull/67)

### Azure-Samples/rag-evaluator (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Merge pull request #1 from danfiedler-msft/danfiedler/pin-actions](https://github.com/Azure-Samples/rag-evaluator/commit/6bf128614fefc3e87b2ce67509d885603d2b743b) - `2026-11-13T18:48:24Z` - Asmae Filali (@AsmaeFILALI) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/rag-evaluator/pull/1)

### microsoft/Agent365-Samples (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Update Trademark boilerplate (#349)](https://github.com/microsoft/Agent365-Samples/commit/4e789d45ddb1f87a4fe1af3e4f6122e659b846e0) - `2026-11-13T18:22:59Z` - Jim Daly (@JimDaly) - PR: [Update Trademark boilerplate](https://github.com/microsoft/Agent365-Samples/pull/349)

### microsoft/nonprofit-agent-pack (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Docs: v1.0.7 file-download limitation and chat example outputs](https://github.com/microsoft/nonprofit-agent-pack/commit/154ed5364abe29e4985313b320e1db96e797f6e1) - `2026-11-13T18:15:29Z` - Brett Randby (@brandby915)

### microsoft/cask (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, docs`

- [Bump actions/setup-dotnet from 6.0.0 to 6.1.0 in the github-actions g…](https://github.com/microsoft/cask/commit/d5ef5e330616784a9a16221ba9450370b81156b1) - `2026-11-13T18:00:21Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-dotnet from 6.0.0 to 6.1.0 in the github-actions group](https://github.com/microsoft/cask/pull/83)

### microsoft/XBOX-MonoGame-NetRumble (1 commit(s), signal 86)

Tags: `human-authored, release-language, samples, watchlist`

- [Prepare release and XBOX certification submission (#23)](https://github.com/microsoft/XBOX-MonoGame-NetRumble/commit/203255e785f2ab2671a9d83b724eaa14d5b07414) - `2026-11-13T17:52:07Z` - James Lenell (@jameslen-atg) - PR: [Prepare release and XBOX certification submission](https://github.com/microsoft/XBOX-MonoGame-NetRumble/pull/23)

### microsoft/winget-cli (1 commit(s), signal 76)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Automatic installer log path limits (#6676)](https://github.com/microsoft/winget-cli/commit/1c5fda6a7148c9b83f5cbe70212cea5d96d94dfe) - `2026-11-13T17:45:29Z` - JohnMcPMS (@JohnMcPMS) - PR: [Automatic installer log path limits](https://github.com/microsoft/winget-cli/pull/6676)

### MicrosoftLearning/mslearn-unify-data (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, training, watchlist`

- [Publish L400 Fabric data agents directly to Microsoft 365 Copilot (#2)](https://github.com/MicrosoftLearning/mslearn-unify-data/commit/9d53bd0cf836141b54ecd0ba0fe4600ec070368b) - `2026-11-13T17:10:48Z` - okalb (@okalb) - PR: [Publish L400 Fabric data agents directly to Microsoft 365 Copilot](https://github.com/MicrosoftLearning/mslearn-unify-data/pull/2)

### MicrosoftLearning/mslearn-sec-identity (1 commit(s), signal 76)

Tags: `human-authored, product:PowerShell, training, watchlist`

- [Merge pull request #34 from v-absamim/update/lab-4c-waf-appservice-steps](https://github.com/MicrosoftLearning/mslearn-sec-identity/commit/b82695b07c05b0222978488e9f92571e56aaf915) - `2026-11-13T16:52:36Z` - v-absamim (@v-absamim) - PR: [Update Lab 4C: detailed WAF, App Service auth, and networking steps](https://github.com/MicrosoftLearning/mslearn-sec-identity/pull/34)

### OfficeDev/microsoft-teams-library-js (1 commit(s), signal 86)

Tags: `docs, human-authored, release-language, watchlist`

- [Close fail-open gaps in the release checker's pipeline and CHANGELOG …](https://github.com/OfficeDev/microsoft-teams-library-js/commit/40b3114e6ccea0fe963311f7a41708e35d6efa76) - `2026-11-13T16:28:23Z` - Patrick Latter (@palatter) - PR: [Close fail-open gaps in the release checker's pipeline and CHANGELOG checks](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3216)

### MicrosoftLearning/trainer-demo-deploy (1 commit(s), signal 76)

Tags: `human-authored, training, watchlist`

- [Fix v2 deployment build](https://github.com/MicrosoftLearning/trainer-demo-deploy/commit/a7af532c5bb0a26e1c3ac255966a577f65bc983a) - `2026-11-13T15:29:10Z` - rob foulkrod

### dotnet/EntityFramework.Docs (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Minor wording change in breaking changes documentation for EF Core 10…](https://github.com/dotnet/EntityFramework.Docs/commit/1459c99ecffb85202e1bbcf32504d074c430bfde) - `2026-11-13T15:09:29Z` - CalebBellWebCE (@CalebBellWebCE) - PR: [Minor wording change in breaking changes documentation for EF Core 10.0](https://github.com/dotnet/EntityFramework.Docs/pull/5523)

### Azure/Azure-Landing-Zones (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [fix: remove default assignee for policy template (#4346)](https://github.com/Azure/Azure-Landing-Zones/commit/5ca84c358bb0f2002c83cd22a81b0e8f9e08da48) - `2026-11-13T13:20:15Z` - Qi Zhang (@Zhangqi910) - PR: [fix: remove default assignee for policy template](https://github.com/Azure/Azure-Landing-Zones/pull/4346)

### MicrosoftDocs/azure-docs-cli (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [CI Update](https://github.com/MicrosoftDocs/azure-docs-cli/commit/94aa9f0f8ee202e5364305fb1e2ad757e02b428e) - `2026-11-13T12:47:45Z` - docsreference@microsoft.com

### Azure-Samples/Apim-Samples (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, samples`

- [Bump the python-packages group across 1 directory with 2 updates (#347)](https://github.com/Azure-Samples/Apim-Samples/commit/da5fe40e961ef9c089221e152e0021980448acd4) - `2026-11-13T12:11:14Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the python-packages group across 1 directory with 2 updates](https://github.com/Azure-Samples/Apim-Samples/pull/347)

### MicrosoftDocs/windows-driver-docs (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Clarify secure read restrictions for HID collections (#4061)](https://github.com/MicrosoftDocs/windows-driver-docs/commit/fdd6af157f6f0eef433f087123c8299d989e5ab3) - `2026-11-13T09:29:47Z` - Andrew Yang (@AndrewYangMSFT) - PR: [Clarify secure read restrictions for HID collections](https://github.com/MicrosoftDocs/windows-driver-docs/pull/4061)

### Azure-Samples/azure-openai-keyless-js (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, product:Azure AI, samples, watchlist`

- [chore(deps): bump github/codeql-action/upload-sarif (#15)](https://github.com/Azure-Samples/azure-openai-keyless-js/commit/0c20e2a3431d8080cf3367553e1c646873a87171) - `2026-11-13T08:05:35Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump github/codeql-action/upload-sarif from 4.39.1 to 4.39.3 in the github-actions group](https://github.com/Azure-Samples/azure-openai-keyless-js/pull/15)

### Azure/homebrew-azd (1 commit(s), signal 86)

Tags: `human-authored, product:Azure SDK, release-language, samples, watchlist`

- [Update for azd release 1.38.0-daily.7072838](https://github.com/Azure/homebrew-azd/commit/c822678f8757f134a742ab59a8280741069a5e84) - `2026-11-13T04:03:47Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/office-docs-powershell (1 commit(s), signal 76)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [clarify RecipientAddressType in both New and Set TransportRule cmdlet…](https://github.com/MicrosoftDocs/office-docs-powershell/commit/7cfde21b7f664cdbfd04b1bd6e557fe8b5d23981) - `2026-11-13T03:34:32Z` - Richard Fajardo (@richfaj) - PR: [Clarify RecipientAddressType in both New and Set TransportRule cmdlet](https://github.com/MicrosoftDocs/office-docs-powershell/pull/13835)

### Azure/workload-orchestration (1 commit(s), signal 76)

Tags: `human-authored, samples, watchlist`

- [Merge pull request #29 from rosageorge97/Adding-ARMTemplates-ghes](https://github.com/Azure/workload-orchestration/commit/bcc5b64e1fd9b3802e688cbca3f02595c5082a60) - `2026-11-13T03:06:04Z` - Tanmay Yerunkar (@tanmay-yerunkar-ms) - PR: [Updating ghes arm template](https://github.com/Azure/workload-orchestration/pull/29)

### Azure/LogicAppsUX (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [perf(shared): exclude development fixtures from service bundles (#9703)](https://github.com/Azure/LogicAppsUX/commit/0325d2dcc18d74db66b0915acc1af16c09d906a2) - `2026-11-13T01:22:51Z` - Riley Evans (@rllyy97) - PR: [perf(shared): exclude development fixtures from service bundles](https://github.com/Azure/LogicAppsUX/pull/9703)

### microsoft/voice-agent (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Move output voice below transcription (#132)](https://github.com/microsoft/voice-agent/commit/78c7248851a79c456717fd3348cfe5007036f0c8) - `2026-11-13T00:27:09Z` - szhaomsft (@szhaomsft) - PR: [Move output voice below transcription](https://github.com/microsoft/voice-agent/pull/132)

### OfficeDev/office-js-docs-pr (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [[all hosts] (Yo Office) Update to current prompt options (#5927)](https://github.com/OfficeDev/office-js-docs-pr/commit/0b91867ca90c95653e69fe8d91ffd3474b45acaf) - `2026-11-13T00:16:57Z` - Elizabeth Samuel (@ElizabethSamuel-MSFT) - PR: [[all hosts] (Yo Office) Update to current prompt options](https://github.com/OfficeDev/office-js-docs-pr/pull/5927)

### Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Keep API-key setup applications single-tenant (#100)](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/commit/badd04ece0d904a30809500ad3d570d90097f235) - `2026-11-12T23:39:20Z` - siyixian (@siyixian) - PR: [Keep API-key setup applications single-tenant](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/pull/100)

### MicrosoftDocs/azure-docs-sdk-cpp (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-cpp/commit/df37be399572281a3f3d7774cbc0e7e61804dd25) - `2026-11-12T23:22:42Z` - azure-sdk (@azure-sdk)

### dotnet/docs-tools (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, watchlist`

- [Bump dotnet/sdk from 10.0 to 11.0 in the docker group (#816)](https://github.com/dotnet/docs-tools/commit/1fc4d93b210b9601d266b774aba9422c67ee2854) - `2026-11-12T22:55:13Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump dotnet/sdk from 10.0 to 11.0 in the docker group](https://github.com/dotnet/docs-tools/pull/816)

### dotnet/cli-lab (1 commit(s), signal 76)

Tags: `human-authored, product:Azure SDK, training, watchlist`

- [Protect .NET 10.0.4xx SDKs used by VS 2026 LTSC (#456)](https://github.com/dotnet/cli-lab/commit/cbdd5a7d0742c82a032fa42d8b52b78fffd195c9) - `2026-11-12T22:24:35Z` - Marc Paine (@marcpopMSFT) - PR: [Protect .NET 10.0.4xx SDKs used by VS 2026 LTSC](https://github.com/dotnet/cli-lab/pull/456)

### microsoft/forge-lab (1 commit(s), signal 41)

Tags: `human-authored, training`

- [Add 10 Windows CVEs to the CVE list](https://github.com/microsoft/forge-lab/commit/3a82b17d0d42b36dbd8c01e36dbc7feedd571023) - `2026-11-12T20:27:38Z` - Cen Zhang (@occia)

### Azure/azure-relay-node (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #129 from Azure/fix-hyco-https-accept-crash](https://github.com/Azure/azure-relay-node/commit/ae155284a50c8f9da48c93c3ef763d80a96ceec5) - `2026-11-12T20:18:07Z` - Kala Anantharaman (@kalkeea) - PR: [hyco-https accept crash fix](https://github.com/Azure/azure-relay-node/pull/129)

### microsoft/kiota-abstractions-go (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #324 from hardikkaurani/fix/add-query-parameters-d…](https://github.com/microsoft/kiota-abstractions-go/commit/43b8b508bf00fd97f6280952a357f8cca6c38b8c) - `2026-11-12T19:41:19Z` - Vincent Biret (@baywet) - PR: [fix(abstractions): support direct scalar fields in AddQueryParameters](https://github.com/microsoft/kiota-abstractions-go/pull/324)

### MicrosoftDocs/windows-iot-public (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #732 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/windows-iot-public/commit/1690dfb1bf9ecb2aea1195ffc60705a3b93c6b01) - `2026-11-12T19:04:22Z` - Valentyna Filimonova (@v-fvalentyna)

### microsoftgraph/msgraph-sample-react-native (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, product:Azure SDK, product:Microsoft Graph, samples, watchlist`

- [Merge pull request #191 from microsoftgraph/dependabot/github_actions…](https://github.com/microsoftgraph/msgraph-sample-react-native/commit/82c283851d0216c1c087e7b7d55225af92f68a98) - `2026-11-12T19:02:20Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump actions/setup-java from 6.1.0 to 6.2.0 in the github-actions group](https://github.com/microsoftgraph/msgraph-sample-react-native/pull/191)

</details>
