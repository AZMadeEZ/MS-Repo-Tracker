# Microsoft Ecosystem Daily Brief - 2026-11-16

> Status: Fresh at generation. Current freshness is tracked in `reports/status.json`.
> Generated: 2026-11-16 22:56 UTC - Window: 29.5h from 2026-11-15 17:24 UTC to 2026-11-16 22:56 UTC.
> 121 repo(s) moved - 610 commit(s) - 28 release item(s) - 25 high-signal repo(s).

## Plain-English Summary

- Azure, Microsoft Graph led the visible product-area activity in this window.
- 28 release item(s) were detected during the window.
- Security-related changes appeared in dotnet/roslyn, microsoft/terraform-provider-power-platform.
- Start with human-authored changes in dotnet/roslyn, microsoft/terraform-provider-power-platform, Azure/azure-cli-extensions, Azure/iotedge-eflow.
- 152 event(s) look automated, bot-heavy, dependency, or generated; review the curated sections before raw volume.

## Headline Metrics

| Metric | Value |
| --- | ---: |
| Inventory repositories | 16800 |
| Repositories after filters | 2552 |
| `pushed_at` candidates | 193 |
| Enrichment candidates | 193 |
| Repositories with movement | 121 |
| Default-branch commits | 610 |

## What Changed That Matters

| Repository | Score | Change | Actor | Noise | Headline | Time |
| --- | ---: | --- | --- | --- | --- | --- |
| [dotnet/roslyn](https://github.com/dotnet/roslyn) | 100 | security_fix | human | low | [Update .NET runtime packages to 10.0.15 to address vulnerability alerts](https://github.com/dotnet/roslyn/pull/86498) | `2026-11-16T22:51:57Z` |
| [microsoft/terraform-provider-power-platform](https://github.com/microsoft/terraform-provider-power-platform) | 100 | security_fix | human | low | [ci: gate acceptance test credentials behind protected environments](https://github.com/microsoft/terraform-provider-power-platform/pull/1305) | `2026-11-16T18:29:26Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 100 | release | unknown | low | [connectedmachine 3.1.0](https://github.com/Azure/azure-cli-extensions/releases/tag/connectedmachine-3.1.0) | `2026-11-16T22:49:02Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 100 | release | human | low | [[Release] Update index.json for extension [ connectedmachine-3.1.0 ]](https://github.com/Azure/azure-cli-extensions/commit/9bf8a60472c40c63c1f70ebb4ad92f213c4bfac2) | `2026-11-16T22:48:02Z` |
| [Azure/iotedge-eflow](https://github.com/Azure/iotedge-eflow) | 100 | release | unknown | low | [1.6.1.11026 LTS](https://github.com/Azure/iotedge-eflow/releases/tag/1.6.1.11026) | `2026-11-16T22:03:23Z` |
| [Azure/iotedge-eflow](https://github.com/Azure/iotedge-eflow) | 100 | release | human | low | [Add EFLOW 1.6.1.11026 LTS release notes](https://github.com/Azure/iotedge-eflow/pull/320) | `2026-11-16T21:51:00Z` |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 100 | release | unknown | low | [Release v5.1019.0](https://github.com/Azure/LogicAppsUX/releases/tag/v5.1019.0) | `2026-11-16T21:09:57Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 100 | release | unknown | low | [@azure/search-documents_13.2.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/search-documents_13.2.0-beta.1) | `2026-11-16T20:31:57Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 100 | release | unknown | low | [azure-search-documents_12.2.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-search-documents_12.2.0b1) | `2026-11-16T19:53:14Z` |
| [microsoft/release-manager-assistant](https://github.com/microsoft/release-manager-assistant) | 100 | release | human | low | [Enable Docker for azd packaging in the dev container](https://github.com/microsoft/release-manager-assistant/pull/68) | `2026-11-16T19:06:46Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 100 | release | unknown | low | [com.azure+azure-search-documents_12.3.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-search-documents_12.3.0-beta.1) | `2026-11-16T19:02:06Z` |
| [Azure/homebrew-azd](https://github.com/Azure/homebrew-azd) | 100 | release | human | low | [Update for azd release 1.38.0](https://github.com/Azure/homebrew-azd/commit/3a30cbe336372a4ed420dbe5c7b911df869526e7) | `2026-11-16T19:01:39Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 100 | release | unknown | low | [azure-mgmt-keyvault_14.2.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-keyvault_14.2.0b1) | `2026-11-16T18:57:51Z` |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 100 | release | unknown | low | [azure-dev-cli_1.38.0](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.38.0) | `2026-11-16T18:57:24Z` |
| [MicrosoftDocs/azure-docs-powershell](https://github.com/MicrosoftDocs/azure-docs-powershell) | 100 | release | human | low | [Stage Azure PowerShell public preview release for Ignite](https://github.com/MicrosoftDocs/azure-docs-powershell/pull/4441) | `2026-11-16T18:54:59Z` |

## Product Areas

| Product area | Signal | Repos | Events | Releases | Security | Top links |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Azure | 121 | 50 | 160 | 26 | 0 | [connectedmachine 3.1.0](https://github.com/Azure/azure-cli-extensions/releases/tag/connectedmachine-3.1.0); [[Release] Update index.json for extension [ connectedmachine-3.1.0 ]](https://github.com/Azure/azure-cli-extensions/commit/9bf8a60472c40c63c1f70ebb4ad92f213c4bfac2); [[connectedmachine] release stable version 2026-09-01](https://github.com/Azure/azure-cli-extensions/pull/10539) |
| Unmapped Activity | 52 | 27 | 78 | 2 | 1 | [ci: gate acceptance test credentials behind protected environments](https://github.com/microsoft/terraform-provider-power-platform/pull/1305); [Enable Docker for azd packaging in the dev container](https://github.com/microsoft/release-manager-assistant/pull/68); [Pin template validation action to compatible SDK revision](https://github.com/microsoft/release-manager-assistant/pull/67) |
| Microsoft Graph | 38 | 15 | 60 | 0 | 0 | [Improve GitHub token handling](https://github.com/microsoft/kiota/pull/8603); [Fix false-positive discriminator warnings for nullable responses](https://github.com/microsoft/kiota/pull/8594); [fix: handle redirects when loading external references](https://github.com/microsoft/kiota/pull/8587) |
| PowerShell | 17 | 6 | 18 | 0 | 0 | [fix(release): Add release steps for blog link, Advisor workbook, and Quickstart metadata](https://github.com/microsoft/finops-toolkit/pull/2421); [Fix Windows CI toolchain selection](https://github.com/microsoft/ebpf-for-windows-sample-program/pull/12); [fix(hubs): Stop dropping reservation details and undated recommendations](https://github.com/microsoft/finops-toolkit/pull/2407) |
| .NET | 15 | 13 | 37 | 0 | 1 | [Update .NET runtime packages to 10.0.15 to address vulnerability alerts](https://github.com/dotnet/roslyn/pull/86498); [Fix Razor component discovery when a base component falls back](https://github.com/dotnet/roslyn/pull/86451); [Fix: Update audit model pinning](https://github.com/dotnet/roslyn/pull/86496) |
| Microsoft 365 | 10 | 3 | 12 | 0 | 0 | [[Doc Feature] Chain of Thought](https://github.com/MicrosoftDocs/msteams-docs/pull/14683); [[Doc feature] [Build html widgets] [5934645]](https://github.com/MicrosoftDocs/msteams-docs/pull/14708); [Merging changes synced from https://github.com/MicrosoftDocs/m365copi…](https://github.com/MicrosoftDocs/m365copilot-docs/commit/ae703ae6bb962efb48f131fb52eed6622f1ec106) |
| Developer Tools | 10 | 3 | 11 | 0 | 0 | [Fix typo in remote SSH documentation](https://github.com/microsoft/vscode-docs/pull/10676); [docs: fix broken internal links and anchor references across documentation](https://github.com/microsoft/vscode-docs/pull/10639); [Document notebookRenderer and notebooks contribution points (fixes #5230, #7811)](https://github.com/microsoft/vscode-docs/pull/10636) |
| Identity | 10 | 2 | 10 | 0 | 0 | [Release 0.3.1: two fixes on top of 0.3.0](https://github.com/microsoft/entrabot/pull/167); [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/ce8ffa8a6c01db31f82a8a4ca53b3f251c28b9cb); [Brent november freshness (#5286)](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/422657dde74512efe2171defde0aaf354568707c) |

## Today's Top Links

| Priority | Repository | Why read it |
| ---: | --- | --- |
| 1 | [dotnet/roslyn](https://github.com/dotnet/roslyn) | [Security-related change: Update .NET runtime packages to 10.0.15 to address vulnerability alerts](https://github.com/dotnet/roslyn/pull/86498) |
| 2 | [microsoft/terraform-provider-power-platform](https://github.com/microsoft/terraform-provider-power-platform) | [Security-related change: ci: gate acceptance test credentials behind protected environments](https://github.com/microsoft/terraform-provider-power-platform/pull/1305) |
| 3 | [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [Release activity: connectedmachine 3.1.0](https://github.com/Azure/azure-cli-extensions/releases/tag/connectedmachine-3.1.0) |
| 4 | [Azure/iotedge-eflow](https://github.com/Azure/iotedge-eflow) | [Release activity: 1.6.1.11026 LTS](https://github.com/Azure/iotedge-eflow/releases/tag/1.6.1.11026) |
| 5 | [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | [Release activity: Release v5.1019.0](https://github.com/Azure/LogicAppsUX/releases/tag/v5.1019.0) |
| 6 | [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [Release activity: @azure/search-documents_13.2.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/search-documents_13.2.0-beta.1) |
| 7 | [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [Release activity: azure-search-documents_12.2.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-search-documents_12.2.0b1) |
| 8 | [microsoft/release-manager-assistant](https://github.com/microsoft/release-manager-assistant) | [Release activity: Enable Docker for azd packaging in the dev container](https://github.com/microsoft/release-manager-assistant/pull/68) |

## Noise and Automation

- 152 event(s) look automated, bot-heavy, dependency, generated, or medium/high noise.
- Top noisy repositories: dotnet/efcore, microsoft/kiota, dotnet/docs, microsoft/kiota-serialization-multipart-go, microsoft/kiota-serialization-text-go.
- Noise mix: Dependency: 60, SDK: 45, Docs: 27, CI/Infra: 17, Fix: 2, Release: 1.

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
| Repos counted | 193 |
| Repos enriched | 121 |

</details>

<details>
<summary>Show supporting signal, release, and lifecycle tables</summary>

## High-Signal Items

| Repository | Score | Tags |
| --- | ---: | --- |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 142 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 137 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 137 | docs, human-authored, release, release-language, watchlist |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 136 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure/iotedge-eflow](https://github.com/Azure/iotedge-eflow) | 129 | docs, human-authored, release, release-language, watchlist |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 128 | docs, human-authored, product:Azure SDK, release, watchlist |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 128 | human-authored, product:Azure AI, product:Azure SDK, release, release-language, samples, watchlist |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | 119 | docs, human-authored, product:Azure SDK, release, watchlist |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 117 | docs, human-authored, release, watchlist |
| [MicrosoftDocs/azure-stack-docs](https://github.com/MicrosoftDocs/azure-stack-docs) | 114 | docs, human-authored, release-language, security, watchlist |
| [microsoft/entrabot](https://github.com/microsoft/entrabot) | 110 | docs, human-authored, release-language, watchlist |
| [dotnet/roslyn](https://github.com/dotnet/roslyn) | 110 | docs, human-authored, product:Azure SDK, security, watchlist |
| [microsoft/terraform-provider-power-platform](https://github.com/microsoft/terraform-provider-power-platform) | 105 | docs, human-authored, security, watchlist |
| [OfficeDev/Microsoft-Teams-Samples](https://github.com/OfficeDev/Microsoft-Teams-Samples) | 102 | human-authored, samples, security, watchlist |
| [MicrosoftDocs/architecture-center](https://github.com/MicrosoftDocs/architecture-center) | 100 | docs, human-authored, watchlist |

## Watchlist Hits

| Repository | Score | Matches |
| --- | ---: | --- |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 142 | products: Azure SDK; repos: Azure/azure-sdk-for-net; orgs: Azure; keywords: release, sdk |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 137 | products: Azure SDK; repos: Azure/azure-sdk-for-java; orgs: Azure; keywords: release, sdk |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 137 | orgs: Azure; keywords: release |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 136 | products: Azure SDK; repos: Azure/azure-sdk-for-js; orgs: Azure; keywords: sdk |
| [Azure/iotedge-eflow](https://github.com/Azure/iotedge-eflow) | 129 | orgs: Azure; keywords: release |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 128 | products: Azure SDK; repos: Azure/azure-sdk-for-python; orgs: Azure; keywords: sdk |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 128 | products: Azure AI, Azure SDK; orgs: Azure; keywords: agent, release, sdk |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | 119 | products: Azure SDK; orgs: Azure; keywords: sdk |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 117 | orgs: Azure |
| [MicrosoftDocs/azure-stack-docs](https://github.com/MicrosoftDocs/azure-stack-docs) | 114 | orgs: MicrosoftDocs; keywords: release, security |
| [microsoft/entrabot](https://github.com/microsoft/entrabot) | 110 | keywords: entra, release |
| [dotnet/roslyn](https://github.com/dotnet/roslyn) | 110 | products: Azure SDK; keywords: sdk |
| [microsoft/terraform-provider-power-platform](https://github.com/microsoft/terraform-provider-power-platform) | 105 | keywords: copilot |
| [OfficeDev/Microsoft-Teams-Samples](https://github.com/OfficeDev/Microsoft-Teams-Samples) | 102 | keywords: security |
| [MicrosoftDocs/architecture-center](https://github.com/MicrosoftDocs/architecture-center) | 100 | orgs: MicrosoftDocs |

## Releases

| Repository | Release | Published |
| --- | --- | --- |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [connectedmachine 3.1.0](https://github.com/Azure/azure-cli-extensions/releases/tag/connectedmachine-3.1.0) | `2026-11-16T22:49:02Z` |
| [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime) | [ONNX Runtime WebGPU Plugin EP v0.6.0](https://github.com/microsoft/onnxruntime/releases/tag/plugin-ep-webgpu/v0.6.0) | `2026-11-16T22:44:35Z` |
| [dotnet/cli-lab](https://github.com/dotnet/cli-lab) | [1.7.756201](https://github.com/dotnet/cli-lab/releases/tag/1.7.756201) | `2026-11-16T22:27:28Z` |
| [Azure/iotedge-eflow](https://github.com/Azure/iotedge-eflow) | [1.6.1.11026 LTS](https://github.com/Azure/iotedge-eflow/releases/tag/1.6.1.11026) | `2026-11-16T22:03:23Z` |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | [Release v5.1019.0](https://github.com/Azure/LogicAppsUX/releases/tag/v5.1019.0) | `2026-11-16T21:09:57Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/search-documents_13.2.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/search-documents_13.2.0-beta.1) | `2026-11-16T20:31:57Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-search-documents_12.2.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-search-documents_12.2.0b1) | `2026-11-16T19:53:14Z` |
| [Azure-Samples/azure-iot-accelerator-workload-for-fabric-rti](https://github.com/Azure-Samples/azure-iot-accelerator-workload-for-fabric-rti) | [v2.0.0](https://github.com/Azure-Samples/azure-iot-accelerator-workload-for-fabric-rti/releases/tag/v2.0.0) | `2026-11-16T19:49:43Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure+azure-search-documents_12.3.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-search-documents_12.3.0-beta.1) | `2026-11-16T19:02:06Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-mgmt-keyvault_14.2.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-keyvault_14.2.0b1) | `2026-11-16T18:57:51Z` |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | [azure-dev-cli_1.38.0](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.38.0) | `2026-11-16T18:57:24Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure.resourcemanager+azure-resourcemanager-keyvault_2.58.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-keyvault_2.58.0-beta.1) | `2026-11-16T18:34:41Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/resourcemanager/keyvault/armkeyvault/v2.2.0-beta.1](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/keyvault/armkeyvault/v2.2.0-beta.1) | `2026-11-16T17:46:13Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-keyvault_6.1.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-keyvault_6.1.0-beta.1) | `2026-11-16T17:45:16Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-ai-agentserver-activity_1.0.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-activity_1.0.0) | `2026-11-16T15:43:01Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-commvaultcontentstore_2.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-commvaultcontentstore_2.0.0) | `2026-11-16T14:26:37Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-eventhub_7.0.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-eventhub_7.0.0-beta.1) | `2026-11-16T10:34:02Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure.resourcemanager+azure-resourcemanager-eventhubs_2.55.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-eventhubs_2.55.0-beta.1) | `2026-11-16T10:22:43Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/resourcemanager/eventhub/armeventhub/v2.0.0-beta.2](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/eventhub/armeventhub/v2.0.0-beta.2) | `2026-11-16T09:42:51Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-messaging-webpubsubchatservice_1.0.0b2](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-messaging-webpubsubchatservice_1.0.0b2) | `2026-11-16T08:52:52Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-mgmt-containerservice_41.10.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-containerservice_41.10.0b1) | `2026-11-16T06:38:49Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [koreai-artemis 1.0.0b1](https://github.com/Azure/azure-cli-extensions/releases/tag/koreai-artemis-1.0.0b1) | `2026-11-16T06:12:47Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/web-pubsub-chat_1.0.0-beta.2](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/web-pubsub-chat_1.0.0-beta.2) | `2026-11-16T06:11:01Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [virtual-network-manager 3.1.0](https://github.com/Azure/azure-cli-extensions/releases/tag/virtual-network-manager-3.1.0) | `2026-11-16T05:54:11Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.ResourceManager.ContainerServiceFleet_1.3.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.ContainerServiceFleet_1.3.0) | `2026-11-16T05:46:48Z` |

## Repository Lifecycle

| Change | Count |
| --- | ---: |
| archived_changed | 3 |
| category_changed | 0 |
| default_branch_changed | 0 |
| fork_changed | 0 |
| new_repos | 27 |
| removed_repos | 0 |

## Recently Created Repositories

| Repository | Category | Created |
| --- | --- | --- |
| [MicrosoftLearning/AB-6010_manage_ai_spend_and_measure_value_in_m365](https://github.com/MicrosoftLearning/AB-6010_manage_ai_spend_and_measure_value_in_m365) | training | `2026-11-16T01:35:16Z` |

## Category Summary

| Category | Repositories |
| --- | ---: |
| docs | 79 |
| reference | 1 |
| samples | 34 |
| training | 7 |

## Organization Summary

| Org | Repositories |
| --- | ---: |
| microsoft | 39 |
| MicrosoftDocs | 26 |
| Azure | 21 |
| Azure-Samples | 16 |
| dotnet | 12 |
| MicrosoftLearning | 3 |
| microsoftgraph | 2 |
| OfficeDev | 1 |
| aspnet | 1 |

</details>

<details>
<summary>Show raw repository activity</summary>

## Busiest Repositories

| Repository | Signal | Category | Commits | Releases | Newest commit |
| --- | ---: | --- | ---: | ---: | --- |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 142 | docs | 17 | 2 | `2026-11-16T22:28:26Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 137 | docs | 12 | 5 | `2026-11-16T22:48:02Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 137 | docs | 12 | 3 | `2026-11-16T20:01:11Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 136 | docs | 11 | 5 | `2026-11-16T21:33:12Z` |
| [Azure/iotedge-eflow](https://github.com/Azure/iotedge-eflow) | 129 | docs | 4 | 1 | `2026-11-16T21:51:00Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 128 | docs | 13 | 5 | `2026-11-16T22:42:16Z` |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 128 | samples | 3 | 1 | `2026-11-16T22:38:36Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | 119 | docs | 4 | 2 | `2026-11-16T17:10:27Z` |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 117 | docs | 2 | 1 | `2026-11-16T21:07:44Z` |
| [MicrosoftDocs/azure-stack-docs](https://github.com/MicrosoftDocs/azure-stack-docs) | 114 | docs | 4 | 0 | `2026-11-16T18:02:02Z` |
| [microsoft/entrabot](https://github.com/microsoft/entrabot) | 110 | docs | 35 | 0 | `2026-11-16T08:00:13Z` |
| [dotnet/roslyn](https://github.com/dotnet/roslyn) | 110 | docs | 10 | 0 | `2026-11-16T22:56:53Z` |
| [microsoft/terraform-provider-power-platform](https://github.com/microsoft/terraform-provider-power-platform) | 105 | docs | 5 | 0 | `2026-11-16T19:16:22Z` |
| [OfficeDev/Microsoft-Teams-Samples](https://github.com/OfficeDev/Microsoft-Teams-Samples) | 102 | samples | 2 | 0 | `2026-11-16T10:45:45Z` |
| [MicrosoftDocs/architecture-center](https://github.com/MicrosoftDocs/architecture-center) | 100 | docs | 28 | 0 | `2026-11-16T18:34:59Z` |
| [microsoft/kiota-dart](https://github.com/microsoft/kiota-dart) | 98 | docs | 23 | 0 | `2026-11-16T18:11:23Z` |
| [MicrosoftDocs/azure-docs-cli](https://github.com/MicrosoftDocs/azure-docs-cli) | 92 | docs | 7 | 0 | `2026-11-16T21:34:25Z` |
| [microsoft/release-manager-assistant](https://github.com/microsoft/release-manager-assistant) | 92 | samples | 7 | 0 | `2026-11-16T19:06:46Z` |
| [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime) | 91 | samples | 11 | 1 | `2026-11-16T22:43:17Z` |
| [MicrosoftDocs/dynamics-365-project-operations](https://github.com/MicrosoftDocs/dynamics-365-project-operations) | 91 | docs | 6 | 0 | `2026-11-16T19:02:51Z` |

## Repository Details

### microsoft/entrabot (35 commit(s), signal 110)

Tags: `docs, human-authored, release-language, watchlist`

- [Merge pull request #167 from microsoft/release/v0.3.1](https://github.com/microsoft/entrabot/commit/7d616c8e27a5716aa22f91d981e142fed5b6e669) - `2026-11-16T08:00:13Z` - Brandon Werner (@brandwe) - PR: [Release 0.3.1: two fixes on top of 0.3.0](https://github.com/microsoft/entrabot/pull/167)
- [Record the release branch's own run on Linux in the verification record](https://github.com/microsoft/entrabot/commit/527f3139d1865fc4c5dcec84da2a64ce84a17d2a) - `2026-11-16T07:44:19Z` - Brandon Werner (@brandwe) - PR: [Release 0.3.1: two fixes on top of 0.3.0](https://github.com/microsoft/entrabot/pull/167)
- [Name 0.3.1 as the current release; record what it rests on](https://github.com/microsoft/entrabot/commit/1000e8543d803a8a1eba871242ee7a9bec3d8874) - `2026-11-16T07:41:46Z` - Brandon Werner (@brandwe) - PR: [Release 0.3.1: two fixes on top of 0.3.0](https://github.com/microsoft/entrabot/pull/167)
- [Release 0.3.1: version, changelog and install commands](https://github.com/microsoft/entrabot/commit/0a408a6704d1a6235e776414b6e99e4c572d7802) - `2026-11-16T07:41:46Z` - Brandon Werner (@brandwe) - PR: [Release 0.3.1: two fixes on top of 0.3.0](https://github.com/microsoft/entrabot/pull/167)
- [Merge pull request #166 from microsoft/docs/readme-video](https://github.com/microsoft/entrabot/commit/6ca45db6e422e510fe201eb0275036197953e7d4) - `2026-11-16T07:22:27Z` - Brandon Werner (@brandwe) - PR: [Link the five-minute video tour from the README](https://github.com/microsoft/entrabot/pull/166)

### MicrosoftDocs/architecture-center (28 commit(s), signal 100)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #17417 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/architecture-center/commit/7adab5a9d0eb14f0737491f845485766aebf7934) - `2026-11-16T18:34:59Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #17416 from MicrosoftDocs/bash-tools](https://github.com/MicrosoftDocs/architecture-center/commit/01ca4937766338a1f299faff9129e957c2d773f1) - `2026-11-16T18:31:08Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Allow common bash tools](https://github.com/MicrosoftDocs/architecture-center/commit/672e90384b9d5f7082aa9806cdbfb0ab2b48c511) - `2026-11-16T18:22:54Z` - Chad Kittel (@ckittel)
- [Merge pull request #17413 from MicrosoftDocs/perms](https://github.com/MicrosoftDocs/architecture-center/commit/19da74d80f40407ee067f57b44fb1de96b8988c8) - `2026-11-16T17:40:09Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #17400 from MicrosoftDocs/quality-signals/storage-…](https://github.com/MicrosoftDocs/architecture-center/commit/dfa5d286b64cbfa51c8eb92a6561e76febf913a8) - `2026-11-16T17:26:12Z` - prmerger-automator[bot] (@prmerger-automator[bot])

### dotnet/docs (26 commit(s), signal 65)

Tags: `bot-only, dependency-noise, docs, security, watchlist`

- [Bump Microsoft.Extensions.Logging.Console across 15 directories (#56920)](https://github.com/dotnet/docs/commit/c845e1f3b74ac42b57d191b1d368a7deda33a31d) - `2026-11-16T21:44:24Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Extensions.Logging.Console across 15 directories](https://github.com/dotnet/docs/pull/56920)
- [Bump Microsoft.Extensions.Diagnostics.ResourceMonitoring.Kubernetes i…](https://github.com/dotnet/docs/commit/db2d1159f800f1f28c06480ecbaab4e21af1335c) - `2026-11-16T21:44:11Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Extensions.Diagnostics.ResourceMonitoring.Kubernetes in /docs/core/diagnostics/snippets/resource-monitoring-kubernetes](https://github.com/dotnet/docs/pull/56921)
- [Bump OpenTelemetry.Exporter.OpenTelemetryProtocol in /docs/fundamenta…](https://github.com/dotnet/docs/commit/4ec9858d1bc80baedb1384ba35ca0b0538c55a63) - `2026-11-16T21:44:01Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump OpenTelemetry.Exporter.OpenTelemetryProtocol in /docs/fundamentals/networking/telemetry/snippets/tracing/ConnectionTracingDemo.ServiceDefaults](https://github.com/dotnet/docs/pull/56899)
- [Bump System.Security.Permissions in /samples/snippets/visualbasic/VS_…](https://github.com/dotnet/docs/commit/af3392162fbcb2c20cc69be37122fe020d92519e) - `2026-11-16T20:33:53Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump System.Security.Permissions in /samples/snippets/visualbasic/VS_Snippets_ADO.NET/DataWorks SqlClient.CAS/VB](https://github.com/dotnet/docs/pull/56909)
- [Bump OpenTelemetry.Instrumentation.AspNetCore in /docs/fundamentals/n…](https://github.com/dotnet/docs/commit/8aee3197fe54848c82856ac87a41d7d99e40652f) - `2026-11-16T19:54:02Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump OpenTelemetry.Instrumentation.AspNetCore in /docs/fundamentals/networking/telemetry/snippets/tracing/ConnectionTracingDemo.ServiceDefaults](https://github.com/dotnet/docs/pull/56901)

### dotnet/runtime (23 commit(s), signal 63)

Tags: `docs, human-authored`

- [Remove unused HW exception support on WASM builds (#137489)](https://github.com/dotnet/runtime/commit/eafb65f7f28fd048fe4910f858ddb375e7da9286) - `2026-11-16T22:31:43Z` - Michal Strehovský (@MichalStrehovsky) - PR: [Remove unused HW exception support on WASM builds](https://github.com/dotnet/runtime/pull/137489)
- [Move environment APIs into shared minipal (#137144)](https://github.com/dotnet/runtime/commit/e58fbf9b8d11293dcc2478a7ef004aa37b748d11) - `2026-11-16T22:29:18Z` - Adeel Mujahid (@am11) - PR: [Move environment APIs into shared minipal](https://github.com/dotnet/runtime/pull/137144)
- [Handle read-only code pages when writing debugger native patches (#13…](https://github.com/dotnet/runtime/commit/9ec6ef1de885b2fe5d2a11d492ac12fd32b2052a) - `2026-11-16T22:21:23Z` - Tom McDonald (@tommcdon) - PR: [Handle read-only code pages when writing debugger native patches](https://github.com/dotnet/runtime/pull/137611)
- [JIT: Guard loop cloning against unsigned decreasing IV wraparound (#1…](https://github.com/dotnet/runtime/commit/05eecbaf90ab8bb8fe9b01e3fe7c17302df2046a) - `2026-11-16T21:59:01Z` - Andy Ayers (@AndyAyersMS) - PR: [JIT: Guard loop cloning against unsigned decreasing IV wraparound](https://github.com/dotnet/runtime/pull/133915)
- [Fix GDB JIT interface exports and ELF output (#137237)](https://github.com/dotnet/runtime/commit/f19a95b83639f33fb629ab204fc930aba62c4e5b) - `2026-11-16T20:01:28Z` - Adeel Mujahid (@am11) - PR: [Fix GDB JIT interface exports and ELF output](https://github.com/dotnet/runtime/pull/137237)

### microsoft/kiota-dart (23 commit(s), signal 98)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #183 from hardikkaurani/fix/form-primitive-collect…](https://github.com/microsoft/kiota-dart/commit/7270a2fee1a6418491a3c4b03f5b4238ae1a015e) - `2026-11-16T18:11:23Z` - Vincent Biret (@baywet) - PR: [fix(serialization-form): support Uint8List serialization, empty byte arrays, and nullable primitive collections](https://github.com/microsoft/kiota-dart/pull/183)
- [refactor(serialization-form): encapsulate decoded value constructor i…](https://github.com/microsoft/kiota-dart/commit/4be0158ec954cc63de965b0fe687f45a0c4e3922) - `2026-11-16T17:07:28Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(serialization-form): support Uint8List serialization, empty byte arrays, and nullable primitive collections](https://github.com/microsoft/kiota-dart/pull/183)
- [fix(serialization-form): allow typed deserialization of null-valued s…](https://github.com/microsoft/kiota-dart/commit/34c10b8a910904ba68ad3f31e07d4f9e8c7ff9d0) - `2026-11-16T16:16:19Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(serialization-form): support Uint8List serialization, empty byte arrays, and nullable primitive collections](https://github.com/microsoft/kiota-dart/pull/183)
- [fix(serialization-form): prevent double decoding and handle base64 nu…](https://github.com/microsoft/kiota-dart/commit/9d2bb42e798479003a27548f75349e69606d33a2) - `2026-11-16T15:34:34Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(serialization-form): support Uint8List serialization, empty byte arrays, and nullable primitive collections](https://github.com/microsoft/kiota-dart/pull/183)
- [docs(serialization-form): document Uint8List and nullable primitive c…](https://github.com/microsoft/kiota-dart/commit/32e25b3f28decaebfcf06fda340d50a71edc1b74) - `2026-11-16T14:59:21Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(serialization-form): support Uint8List serialization, empty byte arrays, and nullable primitive collections](https://github.com/microsoft/kiota-dart/pull/183)

### Azure/azure-sdk-for-net (17 commit(s), signal 142)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [Azure.ResourceManager.ContainerServiceFleet_1.3.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.ContainerServiceFleet_1.3.0) - `2026-11-16T05:46:48Z`
- Release: [Azure.ResourceManager.IotHub_1.2.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.IotHub_1.2.0) - `2026-11-16T05:45:22Z`
- [Load re-review helpers from the base branch tip (#64999)](https://github.com/Azure/azure-sdk-for-net/commit/80b4daa1f194d3875c4e702191595f867d57adb4) - `2026-11-16T22:28:26Z` - m-nash (@m-nash) - PR: [Load re-review helpers from the base branch tip](https://github.com/Azure/azure-sdk-for-net/pull/64999)
- [Update UnbrandedGeneratorVersion to 1.0.0-alpha.20261116.2 (#64994)](https://github.com/Azure/azure-sdk-for-net/commit/b1ce7745c75c2251ee68ec933c4e7c235905442a) - `2026-11-16T21:18:50Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Update UnbrandedGeneratorVersion to 1.0.0-alpha.20261116.2](https://github.com/Azure/azure-sdk-for-net/pull/64994)
- [Regenerate repository SDK with TypeSpec build 20261116.3 [skip ci] (#…](https://github.com/Azure/azure-sdk-for-net/commit/4328b72b5c571d81060880661adddcc32dc3defc) - `2026-11-16T20:41:04Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Update azure-typespec/http-client-csharp version to prerelease 1.0.0-alpha.20261116.3](https://github.com/Azure/azure-sdk-for-net/pull/64995)
- [Describe the missing-patch input accurately in the re-review prompt (…](https://github.com/Azure/azure-sdk-for-net/commit/372edd2d06dd76693f1300d6c3639ade915a676e) - `2026-11-16T19:10:15Z` - m-nash (@m-nash) - PR: [Describe the missing-patch input accurately in the re-review prompt](https://github.com/Azure/azure-sdk-for-net/pull/64965)
- [Update UnbrandedGeneratorVersion to 1.0.0-alpha.20261113.5 (#64967)](https://github.com/Azure/azure-sdk-for-net/commit/9cda36365302724ad5024498a3b3bd1bdf658163) - `2026-11-16T18:58:31Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Update UnbrandedGeneratorVersion to 1.0.0-alpha.20261113.5](https://github.com/Azure/azure-sdk-for-net/pull/64967)

### microsoft/AZD-for-beginners (16 commit(s), signal 56)

Tags: `human-authored, samples`

- [Merge pull request #148 from microsoft/leestott-pin-workflow-actions](https://github.com/microsoft/AZD-for-beginners/commit/37aef730bb3bcf8a7198fbdd4a57382d17f1e2d4) - `2026-11-16T19:26:22Z` - Lee Stott (@leestott) - PR: [Pin workflow actions to immutable commit SHAs](https://github.com/microsoft/AZD-for-beginners/pull/148)
- [Pin workflow actions to immutable commit SHAs](https://github.com/microsoft/AZD-for-beginners/commit/b8674e12d1a1338bab1e96be76882ad00232dde4) - `2026-11-16T19:19:35Z` - Lee Stott (@leestott) - PR: [Pin workflow actions to immutable commit SHAs](https://github.com/microsoft/AZD-for-beginners/pull/148)
- [Merge pull request #147 from hyoshioka0128/patch-36](https://github.com/microsoft/AZD-for-beginners/commit/deb85d266e0deb5ddb383bd96dc84a56f3fe8395) - `2026-11-16T19:00:16Z` - Lee Stott (@leestott) - PR: [Translate retail scenario documentation to Japanese](https://github.com/microsoft/AZD-for-beginners/pull/147)
- [Merge pull request #146 from hyoshioka0128/patch-35](https://github.com/microsoft/AZD-for-beginners/commit/540f45a39e6e071beb14f57149f35f884090f37a) - `2026-11-16T18:59:52Z` - Lee Stott (@leestott) - PR: [Translate README.md content to Japanese](https://github.com/microsoft/AZD-for-beginners/pull/146)
- [Merge pull request #145 from hyoshioka0128/patch-34](https://github.com/microsoft/AZD-for-beginners/commit/e076f38a721cb1dab285852106c1bbf792e17cfa) - `2026-11-16T18:59:30Z` - Lee Stott (@leestott) - PR: [Translate Bicep comments to Japanese](https://github.com/microsoft/AZD-for-beginners/pull/145)

### microsoft/vscode-docs (14 commit(s), signal 89)

Tags: `docs, human-authored, watchlist`

- [Fix typo in remote SSH documentation (#10676)](https://github.com/microsoft/vscode-docs/commit/2e15f50c0c949bb41e6d15447224a2f5389d9bd6) - `2026-11-16T17:30:24Z` - Ultron (@Ultroncn) - PR: [Fix typo in remote SSH documentation](https://github.com/microsoft/vscode-docs/pull/10676)
- [Merge pull request #10675 from microsoft/ntrogh/universe-banner](https://github.com/microsoft/vscode-docs/commit/9dc724b7639dad57bf0c0dc25fc42c2f1c5d7d2f) - `2026-11-16T10:04:59Z` - Nick Trogh (@ntrogh) - PR: [Update website banner for Microsoft Ignite](https://github.com/microsoft/vscode-docs/pull/10675)
- [docs: fix broken internal links and anchor references across document…](https://github.com/microsoft/vscode-docs/commit/b135b9220f8697a65e917e40047bd4273208307a) - `2026-11-16T10:03:08Z` - Alok Pandey (@alok-108) - PR: [docs: fix broken internal links and anchor references across documentation](https://github.com/microsoft/vscode-docs/pull/10639)
- [Update banner for Microsoft Ignite](https://github.com/microsoft/vscode-docs/commit/cb481445d487c99d4716e2fbdc6e88adacc37825) - `2026-11-16T09:59:50Z` - Nick Trogh (@ntrogh) - PR: [Update website banner for Microsoft Ignite](https://github.com/microsoft/vscode-docs/pull/10675)
- [Document notebookRenderer and notebooks contribution points (fixes #5…](https://github.com/microsoft/vscode-docs/commit/fb55ede6ec6fc74fe62af862b17c703552304517) - `2026-11-16T09:56:49Z` - Alok Pandey (@alok-108) - PR: [Document notebookRenderer and notebooks contribution points (fixes #5230, #7811)](https://github.com/microsoft/vscode-docs/pull/10636)

### Azure/azure-sdk-for-python (13 commit(s), signal 128)

Tags: `docs, human-authored, product:Azure SDK, release, watchlist`

- Release: [azure-search-documents_12.2.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-search-documents_12.2.0b1) - `2026-11-16T19:53:14Z`
- Release: [azure-mgmt-keyvault_14.2.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-keyvault_14.2.0b1) - `2026-11-16T18:57:51Z`
- Release: [azure-ai-agentserver-activity_1.0.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-activity_1.0.0) - `2026-11-16T15:43:01Z`
- Release: [azure-messaging-webpubsubchatservice_1.0.0b2](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-messaging-webpubsubchatservice_1.0.0b2) - `2026-11-16T08:52:52Z`
- Release: [azure-mgmt-containerservice_41.10.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-containerservice_41.10.0b1) - `2026-11-16T06:38:49Z`
- [Expand multi-endpoint routing regression coverage (#50036)](https://github.com/Azure/azure-sdk-for-python/commit/efa357c0efa228801e3f43a1c7126e1400b13200) - `2026-11-16T22:42:16Z` - Radhika Gupta (@rads-1996) - PR: [Expand multi-endpoint routing regression coverage](https://github.com/Azure/azure-sdk-for-python/pull/50036)
- [fix(eventhub): surface async receiver invalid-offset errors (#50035)](https://github.com/Azure/azure-sdk-for-python/commit/08cfdd1391d17c27044f468a945d6c18570c1049) - `2026-11-16T22:24:32Z` - Johnathan W (@j7nw4r) - PR: [fix(eventhub): surface async receiver invalid-offset errors](https://github.com/Azure/azure-sdk-for-python/pull/50035)
- [[Core] Re-enable stream error tests without environment proxies (#50032)](https://github.com/Azure/azure-sdk-for-python/commit/2a702ecd0ed47e7a3cb4a4f851370fe5d83869cf) - `2026-11-16T20:50:56Z` - Libba Lawrence (@l0lawrence) - PR: [[Core] Re-enable stream error tests without environment proxies](https://github.com/Azure/azure-sdk-for-python/pull/50032)
- [Update Python TypeSpec emitter dependencies (#50031)](https://github.com/Azure/azure-sdk-for-python/commit/c98eb85b817663b50b8e8f8dc0fb85451303f8c9) - `2026-11-16T18:50:38Z` - Libba Lawrence (@l0lawrence) - PR: [Update Python TypeSpec emitter dependencies](https://github.com/Azure/azure-sdk-for-python/pull/50031)
- [[Storage] mypy 2.1.0 fix (#50013)](https://github.com/Azure/azure-sdk-for-python/commit/e0d24c426958ca4eef13e6ab88b3a3db43ff3cac) - `2026-11-16T18:16:21Z` - anjaliratnam-msft (@anjaliratnam-msft) - PR: [[Storage] mypy 2.1.0 fix](https://github.com/Azure/azure-sdk-for-python/pull/50013)

### Azure/azure-cli-extensions (12 commit(s), signal 137)

Tags: `docs, human-authored, release, release-language, watchlist`

- Release: [connectedmachine 3.1.0](https://github.com/Azure/azure-cli-extensions/releases/tag/connectedmachine-3.1.0) - `2026-11-16T22:49:02Z`
- Release: [koreai-artemis 1.0.0b1](https://github.com/Azure/azure-cli-extensions/releases/tag/koreai-artemis-1.0.0b1) - `2026-11-16T06:12:47Z`
- Release: [virtual-network-manager 3.1.0](https://github.com/Azure/azure-cli-extensions/releases/tag/virtual-network-manager-3.1.0) - `2026-11-16T05:54:11Z`
- Release: [resiliency 1.0.0b1](https://github.com/Azure/azure-cli-extensions/releases/tag/resiliency-1.0.0b1) - `2026-11-16T03:13:43Z`
- Release: [azure-devops 1.0.11](https://github.com/Azure/azure-cli-extensions/releases/tag/azure-devops-1.0.11) - `2026-11-16T00:17:45Z`
- [[Release] Update index.json for extension [ connectedmachine-3.1.0 ]](https://github.com/Azure/azure-cli-extensions/commit/9bf8a60472c40c63c1f70ebb4ad92f213c4bfac2) - `2026-11-16T22:48:02Z` - Azure CLI Team (@azclibot)
- [[connectedmachine] release stable version 2026-09-01 (#10539)](https://github.com/Azure/azure-cli-extensions/commit/63ee2b590a92cc1e0a09cb71a647e71e5205afe5) - `2026-11-16T22:35:10Z` - yaotongms (@yaotongms) - PR: [[connectedmachine] release stable version 2026-09-01](https://github.com/Azure/azure-cli-extensions/pull/10539)
- [[Release] Update index.json for extension [ koreai-artemis-1.0.0b1 ]](https://github.com/Azure/azure-cli-extensions/commit/30f5ada93b3fac0b0d177e0ff8755c2174fb6d80) - `2026-11-16T06:11:42Z` - Azure CLI Team (@azclibot)
- [Add Kore AI Artemis CLI extension (#10544)](https://github.com/Azure/azure-cli-extensions/commit/704dbebd148a62fd65bda5ac368b3ceb8aece90b) - `2026-11-16T06:01:51Z` - Shiwani (@shiwanijain) - PR: [Add Kore AI Artemis CLI extension](https://github.com/Azure/azure-cli-extensions/pull/10544)
- [[Release] Update index.json for extension [ network-manager-3.1.0 ]](https://github.com/Azure/azure-cli-extensions/commit/f5145614f62275cad7f580388cf1e3e905c3cc61) - `2026-11-16T05:53:08Z` - Azure CLI Team (@azclibot)

### Azure/azure-sdk-for-java (12 commit(s), signal 137)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [com.azure+azure-search-documents_12.3.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-search-documents_12.3.0-beta.1) - `2026-11-16T19:02:06Z`
- Release: [com.azure.resourcemanager+azure-resourcemanager-keyvault_2.58.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-keyvault_2.58.0-beta.1) - `2026-11-16T18:34:41Z`
- Release: [com.azure.resourcemanager+azure-resourcemanager-eventhubs_2.55.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-eventhubs_2.55.0-beta.1) - `2026-11-16T10:22:43Z`
- [Increment package versions for search releases (#51279)](https://github.com/Azure/azure-sdk-for-java/commit/1d91947dd2ae2729f072e145841824a90ea7a432) - `2026-11-16T20:01:11Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[skip ci] Increment versions for search releases](https://github.com/Azure/azure-sdk-for-java/pull/51279)
- [Increment package versions for keyvault/azure-resourcemanager-keyvaul…](https://github.com/Azure/azure-sdk-for-java/commit/6e938b998ae3f6ac58af9d708ede9b0c4f110b79) - `2026-11-16T20:00:54Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[skip ci] Increment versions for keyvault/azure-resourcemanager-keyvault auto-releases](https://github.com/Azure/azure-sdk-for-java/pull/51277)
- [Leverage multi release jars further (#51066)](https://github.com/Azure/azure-sdk-for-java/commit/7bde0cf056c6a28d6e2431094df742558a4578cf) - `2026-11-16T18:29:49Z` - Alan Zimmer (@alzimmermsft) - PR: [Leverage multi release jars further](https://github.com/Azure/azure-sdk-for-java/pull/51066)
- [Configurations:  'specification/keyvault/resource-manager/Microsoft.K…](https://github.com/Azure/azure-sdk-for-java/commit/13aebb3ba7197ba74efafe1ddb3e53d715e8de5d) - `2026-11-16T17:10:17Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-resourcemanager-keyvault]-generated-from-SDK Generation - Java-7066461](https://github.com/Azure/azure-sdk-for-java/pull/51219)
- [Set release date for azure-search-documents 12.3.0-beta.1 changelog (…](https://github.com/Azure/azure-sdk-for-java/commit/c52f5629f285610a61dd35d6d96efd09950689ff) - `2026-11-16T17:01:44Z` - Yangyang Lu (@yangylu91) - PR: [Set release date for azure-search-documents 12.3.0-beta.1 changelog](https://github.com/Azure/azure-sdk-for-java/pull/51266)

### microsoft/onnxruntime (11 commit(s), signal 91)

Tags: `human-authored, release, samples`

- Release: [ONNX Runtime WebGPU Plugin EP v0.6.0](https://github.com/microsoft/onnxruntime/releases/tag/plugin-ep-webgpu/v0.6.0) - `2026-11-16T22:44:35Z`
- [Select model package variants in EP priority order (#33508)](https://github.com/microsoft/onnxruntime/commit/01713b72cf4f929ea9c5d7ca4addcfe25e24a313) - `2026-11-16T22:43:17Z` - maxim-davgalev (@maxim-davgalev) - PR: [Select model package variants in EP priority order](https://github.com/microsoft/onnxruntime/pull/33508)
- [KFI-779 Avoid SME2 on GEMV DynamicQuantizeMatMul. (#33739)](https://github.com/microsoft/onnxruntime/commit/7172420c0467ceec0fd5f06f87eb218bf7705e55) - `2026-11-16T18:20:07Z` - Colm Donelan (@Colm-in-Arm) - PR: [KFI-779 Avoid SME2 on GEMV DynamicQuantizeMatMul.](https://github.com/microsoft/onnxruntime/pull/33739)
- [Preserve histogram probability mass in entropy calibration (#34180)](https://github.com/microsoft/onnxruntime/commit/3d51a42f203ee81a3965102b5778a67635a8c865) - `2026-11-16T18:05:45Z` - Afloat (@Afloat16) - PR: [Preserve histogram probability mass in entropy calibration](https://github.com/microsoft/onnxruntime/pull/34180)
- [Handle scalar and empty tensors in integer quantization helpers (#34185)](https://github.com/microsoft/onnxruntime/commit/dd9b78ab823c465bcd37538be3d4b9b2737d6f2a) - `2026-11-16T18:01:56Z` - Afloat (@Afloat16) - PR: [Handle scalar and empty tensors in integer quantization helpers](https://github.com/microsoft/onnxruntime/pull/34185)
- [Honor 16-bit overrides when upgrading FLOAT8 quantization opsets (#34…](https://github.com/microsoft/onnxruntime/commit/a4f51c7b63ba3eb0a9dfc4d61818d262a0825c52) - `2026-11-16T17:57:47Z` - Afloat (@Afloat16) - PR: [Honor 16-bit overrides when upgrading FLOAT8 quantization opsets](https://github.com/microsoft/onnxruntime/pull/34190)

### microsoft/kiota (11 commit(s), signal 86)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Improve GitHub token handling (#8603)](https://github.com/microsoft/kiota/commit/095b38163b04a465693c5f94036a48bf80a3239b) - `2026-11-16T22:04:44Z` - Gavin Barron (@gavinbarron) - PR: [Improve GitHub token handling](https://github.com/microsoft/kiota/pull/8603)
- [Fix false-positive discriminator warnings for nullable responses (#8594)](https://github.com/microsoft/kiota/commit/a77f0e920f5f07ee5de2430eeed31fd7e3f521f7) - `2026-11-16T21:29:02Z` - Gavin Barron (@gavinbarron) - PR: [Fix false-positive discriminator warnings for nullable responses](https://github.com/microsoft/kiota/pull/8594)
- [chore(deps-dev): bump @types/vscode from 1.144.0 to 1.145.0 in /vscod…](https://github.com/microsoft/kiota/commit/9642e58b51bd73a9e2a5cf825e943ded3cb606b4) - `2026-11-16T20:58:43Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps-dev): bump @types/vscode from 1.144.0 to 1.145.0 in /vscode](https://github.com/microsoft/kiota/pull/8590)
- [chore: upgrades go dependencies for integration tests (#8585)](https://github.com/microsoft/kiota/commit/7f58fe2e7d53eeff260fb523dc3cabfd5b838e93) - `2026-11-16T20:11:44Z` - Vincent Biret (@baywet) - PR: [chore: upgrades go dependencies for integration tests](https://github.com/microsoft/kiota/pull/8585)
- [fix: handle redirects when loading external references (#8587)](https://github.com/microsoft/kiota/commit/31a08fa57c173f171e8e19ee182db74450726ee1) - `2026-11-16T19:15:32Z` - Treicy Sanchez (@Treicysg) - PR: [fix: handle redirects when loading external references](https://github.com/microsoft/kiota/pull/8587)

### Azure/azure-sdk-for-js (11 commit(s), signal 136)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [@azure/search-documents_13.2.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/search-documents_13.2.0-beta.1) - `2026-11-16T20:31:57Z`
- Release: [@azure/arm-keyvault_6.1.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-keyvault_6.1.0-beta.1) - `2026-11-16T17:45:16Z`
- Release: [@azure/arm-commvaultcontentstore_2.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-commvaultcontentstore_2.0.0) - `2026-11-16T14:26:37Z`
- Release: [@azure/arm-eventhub_7.0.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-eventhub_7.0.0-beta.1) - `2026-11-16T10:34:02Z`
- Release: [@azure/web-pubsub-chat_1.0.0-beta.2](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/web-pubsub-chat_1.0.0-beta.2) - `2026-11-16T06:11:01Z`
- [[Monitor] Add opt-in multi-endpoint routing (#40586)](https://github.com/Azure/azure-sdk-for-js/commit/33729f44de662a101da37dda9a47857bd5c477ab) - `2026-11-16T21:33:12Z` - Jackson Weber (@JacksonWeber) - PR: [[Monitor] Add opt-in multi-endpoint routing](https://github.com/Azure/azure-sdk-for-js/pull/40586)
- [[engSys] Onboard JavaScript to API Review Hub (#40814)](https://github.com/Azure/azure-sdk-for-js/commit/623cc5cb90c37372e2def0d08fca86d90d7755a3) - `2026-11-16T20:35:22Z` - Maor Leger (@maorleger) - PR: [[engSys] Onboard JavaScript to API Review Hub](https://github.com/Azure/azure-sdk-for-js/pull/40814)
- [[EngSys] upgrade pnpm to version 12.18.0 (#40159)](https://github.com/Azure/azure-sdk-for-js/commit/68eeadd5bbe6e532eb751f4185ce4f04570770c5) - `2026-11-16T19:56:17Z` - Jeremy Meng (@jeremymeng) - PR: [[EngSys] upgrade pnpm to version 12.18.0](https://github.com/Azure/azure-sdk-for-js/pull/40159)
- [Search: add 2026-11-01-preview JS SDK support (#40458)](https://github.com/Azure/azure-sdk-for-js/commit/edbb06cb51328e52e2bca24e2b93d254ab818c6b) - `2026-11-16T19:54:37Z` - Yangyang Lu (@yangylu91) - PR: [Search: add 2026-11-01-preview JS SDK support](https://github.com/Azure/azure-sdk-for-js/pull/40458)
- [[EngSys] automatic pnpm update (#40809)](https://github.com/Azure/azure-sdk-for-js/commit/d94e22d6b7b41b7c378f7b72ca04e203053cdd5c) - `2026-11-16T17:46:28Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[EngSys] automatic pnpm update](https://github.com/Azure/azure-sdk-for-js/pull/40809)

### microsoft/AKS-Lab-GitHubCopilot (11 commit(s), signal 86)

Tags: `human-authored, product:Azure SDK, training, watchlist`

- [Merge pull request #10 from microsoft/dependabot/uv/opentelemetry-api…](https://github.com/microsoft/AKS-Lab-GitHubCopilot/commit/d402a4f00e8125e500fb09f42c719282c5c8c949) - `2026-11-16T18:36:09Z` - Lee Stott (@leestott) - PR: [Bump opentelemetry-api from 1.45.1 to 1.45.2](https://github.com/microsoft/AKS-Lab-GitHubCopilot/pull/10)
- [Bump opentelemetry-api from 1.45.1 to 1.45.2](https://github.com/microsoft/AKS-Lab-GitHubCopilot/commit/dfc03f602541075731bfdf5c633f11e1fe2da36d) - `2026-11-16T18:33:00Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump opentelemetry-api from 1.45.1 to 1.45.2](https://github.com/microsoft/AKS-Lab-GitHubCopilot/pull/10)
- [Merge pull request #9 from microsoft/dependabot/github_actions/github…](https://github.com/microsoft/AKS-Lab-GitHubCopilot/commit/c1ef49106d67e11dec4b3706538f1f9300af0b38) - `2026-11-16T18:32:53Z` - Lee Stott (@leestott) - PR: [Bump the github-actions group with 4 updates](https://github.com/microsoft/AKS-Lab-GitHubCopilot/pull/9)
- [Merge pull request #8 from microsoft/dependabot/uv/opentelemetry-api-…](https://github.com/microsoft/AKS-Lab-GitHubCopilot/commit/9033b49a3718a8bd7e782b31427a86b7e643f1b7) - `2026-11-16T18:32:36Z` - Lee Stott (@leestott) - PR: [Bump opentelemetry-api from 1.43.0 to 1.45.1](https://github.com/microsoft/AKS-Lab-GitHubCopilot/pull/8)
- [Merge pull request #6 from microsoft/dependabot/uv/certifi-2026.10.19](https://github.com/microsoft/AKS-Lab-GitHubCopilot/commit/7526027fc82ed07b94cd00bc47a31a5271fe7f3a) - `2026-11-16T18:31:54Z` - Lee Stott (@leestott) - PR: [Bump certifi from 2026.6.17 to 2026.10.19](https://github.com/microsoft/AKS-Lab-GitHubCopilot/pull/6)

### dotnet/roslyn (10 commit(s), signal 110)

Tags: `docs, human-authored, product:Azure SDK, security, watchlist`

- [Fall back to net472 VBCSCompiler when purging the Roslyn output cache…](https://github.com/dotnet/roslyn/commit/644d0017f81d1d225d4a9b44171b2bcc6bcfb7cc) - `2026-11-16T22:56:53Z` - Fred Silberberg (@333fred) - PR: [Fall back to net472 VBCSCompiler when purging the Roslyn output cache](https://github.com/dotnet/roslyn/pull/86499)
- [Update .NET runtime packages to 10.0.15 to address vulnerability aler…](https://github.com/dotnet/roslyn/commit/7ed489d01341de57d2d9785483f3a7f78ffb93df) - `2026-11-16T22:51:57Z` - Fred Silberberg (@333fred) - PR: [Update .NET runtime packages to 10.0.15 to address vulnerability alerts](https://github.com/dotnet/roslyn/pull/86498)
- [Razor duplicate using cleanup and diagnostic de-dupe (#86424)](https://github.com/dotnet/roslyn/commit/f085217c8cbda0371b0702c9b9ea72f98f3512ed) - `2026-11-16T22:22:10Z` - David Wengier (@davidwengier) - PR: [Razor duplicate using cleanup and diagnostic de-dupe](https://github.com/dotnet/roslyn/pull/86424)
- [Fix Razor component discovery when a base component falls back (#86451)](https://github.com/dotnet/roslyn/commit/a72bcd8fa0d924de8511dee98741aff69952f2d1) - `2026-11-16T20:27:32Z` - David Wengier (@davidwengier) - PR: [Fix Razor component discovery when a base component falls back](https://github.com/dotnet/roslyn/pull/86451)
- [Fix: Update audit model pinning (#86496)](https://github.com/dotnet/roslyn/commit/421c2f89a9182ffc69d13b6a571c924c87bb2b34) - `2026-11-16T19:41:00Z` - Ankita Khera (@akhera99) - PR: [Fix: Update audit model pinning](https://github.com/dotnet/roslyn/pull/86496)

### Azure-Samples/azure-finops-agent (10 commit(s), signal 85)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Take facts only from pages read this turn, and require an assessment'…](https://github.com/Azure-Samples/azure-finops-agent/commit/12f59e55a93803d33bdf4c7bcaf2629982931b19) - `2026-11-16T19:49:03Z` - Ali Reza Farahnak (@alfarahn)
- [Correct the start page's audit rationale](https://github.com/Azure-Samples/azure-finops-agent/commit/d48e9af15bbbc68971d0fd0fdc4fb0fa79c01096) - `2026-11-16T19:00:52Z` - Ali Reza Farahnak (@alfarahn)
- [Keep an answer the model service failed only after it was whole](https://github.com/Azure-Samples/azure-finops-agent/commit/9c7300dbeb5a5d8c9544bf313462a34bd8558ac4) - `2026-11-16T19:00:52Z` - Ali Reza Farahnak (@alfarahn)
- [Fit the start page to what people ask; evaluate the cards they use](https://github.com/Azure-Samples/azure-finops-agent/commit/82aefc4d8e6df0261c29cf2f5700d778653906ef) - `2026-11-16T18:37:55Z` - Ali Reza Farahnak (@alfarahn)
- [Send a read that gets no response once more](https://github.com/Azure-Samples/azure-finops-agent/commit/43d2ee6a7286397cfb06c2171514ee00c20f6434) - `2026-11-16T18:34:28Z` - Ali Reza Farahnak (@alfarahn)

### MicrosoftDocs/learn (10 commit(s), signal 85)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/2dfd44243ca116e3955764caaebdf840ea0aa573) - `2026-11-16T08:25:59Z` - Learn Build Service GitHub App
- [Merge pull request #56852 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/learn/commit/72a61604ee001b3b67fe2a00975dcedf6533e6e1) - `2026-11-16T08:16:49Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #56851 from Orin-Thomas/orthomas-16-NOV-26-X](https://github.com/MicrosoftDocs/learn/commit/195f53e9bb1a4db9fbcbe073dc6a6d50e4ddbff7) - `2026-11-16T07:29:29Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Add Video](https://github.com/MicrosoftDocs/learn/commit/8c7a5dbd88d23cff11839d4ca073732a1e4dbb6f) - `2026-11-16T07:06:25Z` - Orin Thomas (@Orin-Thomas)
- [Merge pull request #56850 from Orin-Thomas/orthomas-16-NOV-26-Y](https://github.com/MicrosoftDocs/learn/commit/8ccb581073ec839fad966cc145cd1fb37f8d1d95) - `2026-11-16T07:04:05Z` - prmerger-automator[bot] (@prmerger-automator[bot])

### MicrosoftDocs/m365copilot-docs (9 commit(s), signal 84)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/m365copi…](https://github.com/MicrosoftDocs/m365copilot-docs/commit/ae703ae6bb962efb48f131fb52eed6622f1ec106) - `2026-11-16T20:56:42Z` - Learn Build Service GitHub App
- [Merge pull request #1839 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/m365copilot-docs/commit/a7928af8dcab373c9308cc5d649181020560dc4f) - `2026-11-16T20:56:11Z` - Jason Johnston (@jasonjoh)
- [Clarified publishing to Marketplace with WIQD (#1838)](https://github.com/MicrosoftDocs/m365copilot-docs/commit/8b71692b0c5b8f09681a48549e9bdb6ee1a521f1) - `2026-11-16T20:46:57Z` - Jason Johnston (@jasonjoh)
- [Document Information Barriers limitation for Chat skills (#1837)](https://github.com/MicrosoftDocs/m365copilot-docs/commit/124c5f0b9afc1ff62442eeea117908daa43015e4) - `2026-11-16T20:18:27Z` - Hanaa Musa (@musa-57)
- [Merging changes synced from https://github.com/MicrosoftDocs/m365copi…](https://github.com/MicrosoftDocs/m365copilot-docs/commit/77df92d00b64b8ebf2066ec8e6065ccda49b31df) - `2026-11-16T19:49:14Z` - Learn Build Service GitHub App

### MicrosoftDocs/dynamics365smb-docs (9 commit(s), signal 84)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/ce8ffa8a6c01db31f82a8a4ca53b3f251c28b9cb) - `2026-11-16T19:04:06Z` - Learn Build Service GitHub App
- [Merge pull request #5290 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/2cf15bc59b2784b61b4fe9df085a3d3c515eeda3) - `2026-11-16T19:03:16Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Brent november freshness (#5286)](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/422657dde74512efe2171defde0aaf354568707c) - `2026-11-16T14:08:19Z` - Brent Holtorf (@brentholtorf)
- [Refresh built-in reports articles andd includes (#5282)](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/9fbef18b4fc8498d8574912111aca30f95e09e27) - `2026-11-16T14:03:34Z` - jswymer (@jswymer)
- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/f6e4e6dbff538cdf9d79d9d98f8db307dedc8e4b) - `2026-11-16T13:03:40Z` - Learn Build Service GitHub App

### microsoft/kiota-samples (9 commit(s), signal 84)

Tags: `docs, human-authored, product:Microsoft Graph, watchlist`

- [Merge pull request #9383 from hardikkaurani/fix/go-samples-test-suite…](https://github.com/microsoft/kiota-samples/commit/1c0bd5026740123e833ccae51726ba09a7fda9de) - `2026-11-16T13:54:42Z` - Vincent Biret (@baywet) - PR: [fix(go): add unit test suites, error handling, and CI workflow for Go samples](https://github.com/microsoft/kiota-samples/pull/9383)
- [Merge pull request #9366 from microsoft/dependabot/npm_and_yarn/sampl…](https://github.com/microsoft/kiota-samples/commit/5bff7b433adf9f38f5d8ba3a3ac407dd2a53e482) - `2026-11-16T13:52:27Z` - Vincent Biret (@baywet) - PR: [build(deps-dev): bump @types/node from 24.19.2 to 26.6.6 in /sample-api/clients/typescript](https://github.com/microsoft/kiota-samples/pull/9366)
- [Merge pull request #9376 from microsoft/dependabot/bundler/get-starte…](https://github.com/microsoft/kiota-samples/commit/0607a48e996442768d17047db6e8a488795439c0) - `2026-11-16T13:45:29Z` - Vincent Biret (@baywet) - PR: [build(deps): bump addressable from 2.9.0 to 2.9.1 in /get-started/azure-auth/ruby](https://github.com/microsoft/kiota-samples/pull/9376)
- [Merge pull request #9377 from microsoft/dependabot/github_actions/act…](https://github.com/microsoft/kiota-samples/commit/1cb34091f35f61c693be7462b570ba92c9bc3ed5) - `2026-11-16T13:45:23Z` - Vincent Biret (@baywet) - PR: [build(deps): bump actions/setup-dotnet from 6.0.0 to 6.1.0](https://github.com/microsoft/kiota-samples/pull/9377)
- [Merge pull request #9378 from microsoft/dependabot/github_actions/act…](https://github.com/microsoft/kiota-samples/commit/42080711154e6f11dafa63f7f8139c19d3e30a4b) - `2026-11-16T13:45:17Z` - Vincent Biret (@baywet) - PR: [build(deps): bump actions/setup-java from 6.1.0 to 6.2.0](https://github.com/microsoft/kiota-samples/pull/9378)

### MicrosoftDocs/visualstudio-docs (8 commit(s), signal 83)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #11494 from MicrosoftDocs/main639304635050243658sy…](https://github.com/MicrosoftDocs/visualstudio-docs/commit/55f03ccb7c47ec059c5a10fbb20407dfd39606df) - `2026-11-16T22:05:22Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11494)
- [Merging changes synced from https://github.com/MicrosoftDocs/visualst…](https://github.com/MicrosoftDocs/visualstudio-docs/commit/efdf3afb02f202cea87e21414587f9d81c6b01cb) - `2026-11-16T22:05:00Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11494)
- [Merge pull request #15823 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/visualstudio-docs/commit/fdb162e87b81bb402817b8e342a3428529bd2f9d) - `2026-11-16T22:02:41Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11494)
- [Document C#/VB Compiler workspace queries (#15811)](https://github.com/MicrosoftDocs/visualstudio-docs/commit/38068a380ae2af1afc964ebf3fd8e381288465f7) - `2026-11-16T17:42:10Z` - Matteo Prosperi (@matteo-prosperi) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11494)
- [Merge pull request #11493 from MicrosoftDocs/main639304420831600974sy…](https://github.com/MicrosoftDocs/visualstudio-docs/commit/8167104ee8c2561a523fd6359b69b8a2f0ab3153) - `2026-11-16T16:08:21Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11493)

### microsoft/kiota-java (8 commit(s), signal 83)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #2255 from microsoft/chore/remove-sonar-20261116](https://github.com/microsoft/kiota-java/commit/15efefe61feb656db3a7df40e496066beee34fef) - `2026-11-16T18:48:21Z` - Vincent Biret (@baywet) - PR: [chore: remove SonarCloud integration](https://github.com/microsoft/kiota-java/pull/2255)
- [Merge pull request #2256 from hardikkaurani/fix/redirect-different-pr…](https://github.com/microsoft/kiota-java/commit/4d35313e45d73bfdc6bcdfaa812a898ea55b075c) - `2026-11-16T18:15:40Z` - Vincent Biret (@baywet) - PR: [fix(http): remove Proxy-Authorization on redirect when the proxy changes](https://github.com/microsoft/kiota-java/pull/2256)
- [test(http): drive intercept through A-B-A redirect loop to verify pro…](https://github.com/microsoft/kiota-java/commit/3176a51510d5dbcf06949f048fb1c2128ddeb05e) - `2026-11-16T16:51:09Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(http): remove Proxy-Authorization on redirect when the proxy changes](https://github.com/microsoft/kiota-java/pull/2256)
- [fix(http): remove Proxy-Authorization on redirect when the proxy changes](https://github.com/microsoft/kiota-java/commit/e1d563fe96eebc71facd7f12742d77dd55453a67) - `2026-11-16T16:18:09Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(http): remove Proxy-Authorization on redirect when the proxy changes](https://github.com/microsoft/kiota-java/pull/2256)
- [test(http): add failing test for Proxy-Authorization stripping when p…](https://github.com/microsoft/kiota-java/commit/c681ebb8925c929b85a3171600244b216de4cbbe) - `2026-11-16T16:16:19Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(http): remove Proxy-Authorization on redirect when the proxy changes](https://github.com/microsoft/kiota-java/pull/2256)

### microsoft/kiota-http-go (8 commit(s), signal 83)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #315 from microsoft/chore/remove-sonar-http-go-202…](https://github.com/microsoft/kiota-http-go/commit/d44af79f4711db0c3a75a7713aecedb4c2acbd76) - `2026-11-16T18:46:07Z` - Vincent Biret (@baywet) - PR: [ci: remove SonarCloud integration](https://github.com/microsoft/kiota-http-go/pull/315)
- [Merge pull request #313 from hardikkaurani/fix/middleware-resilience-…](https://github.com/microsoft/kiota-http-go/commit/3d663a4e07efd7684bef06a56d2bb2454ddb01b1) - `2026-11-16T15:52:19Z` - Vincent Biret (@baywet) - PR: [fix(http): harden middleware against typed nil options, leaks, and unseekable retries](https://github.com/microsoft/kiota-http-go/pull/313)
- [refactor(urlreplace): revert RawPath handling and exercise typed-nil …](https://github.com/microsoft/kiota-http-go/commit/bcd060c8843947fa46f162a03d0a96dbcbbd0821) - `2026-11-16T15:46:27Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(http): harden middleware against typed nil options, leaks, and unseekable retries](https://github.com/microsoft/kiota-http-go/pull/313)
- [fix(urlreplace): guard typed-nil observability options and preserve e…](https://github.com/microsoft/kiota-http-go/commit/3b2e8e376e32ce442c122447ed5286d4dd768dcc) - `2026-11-16T15:08:09Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(http): harden middleware against typed nil options, leaks, and unseekable retries](https://github.com/microsoft/kiota-http-go/pull/313)
- [fix(urlreplace): preserve untouched RawPath escapes and gate span URL…](https://github.com/microsoft/kiota-http-go/commit/46f7a35a3bf9971cad4e21dbe02cf660555a4277) - `2026-11-16T14:32:27Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(http): harden middleware against typed nil options, leaks, and unseekable retries](https://github.com/microsoft/kiota-http-go/pull/313)

### microsoft/voice-agent (8 commit(s), signal 83)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merge pull request #136 from ZhaoChaoqun/zhaochaoqun-smart-appliance-…](https://github.com/microsoft/voice-agent/commit/12564362d37c9ea8aadf0456438330f180142dfa) - `2026-11-16T09:31:33Z` - Yulin Li (@yulin-li) - PR: [Add smart home appliance Voice Agent sample](https://github.com/microsoft/voice-agent/pull/136)
- [Remove WebRTC lab and documentation from smart home sample](https://github.com/microsoft/voice-agent/commit/a4023e3e7a9935ef6580131ea1333221810a4f1d) - `2026-11-16T08:13:44Z` - Chaoqun Zhao (@ZhaoChaoqun) - PR: [Add smart home appliance Voice Agent sample](https://github.com/microsoft/voice-agent/pull/136)
- [Align smart home docs, env example and Modern naming](https://github.com/microsoft/voice-agent/commit/759a83ad8825d453249e9772ed0c63e80b3e4106) - `2026-11-16T08:03:17Z` - Chaoqun Zhao (@ZhaoChaoqun) - PR: [Add smart home appliance Voice Agent sample](https://github.com/microsoft/voice-agent/pull/136)
- [Remove Classic UI and share Modern/Habitat code](https://github.com/microsoft/voice-agent/commit/5f0adbec9fee14a2e4988f83b84168732b512db4) - `2026-11-16T07:29:03Z` - Chaoqun Zhao (@ZhaoChaoqun) - PR: [Add smart home appliance Voice Agent sample](https://github.com/microsoft/voice-agent/pull/136)
- [Replace scripted TV replies with generic completion rules](https://github.com/microsoft/voice-agent/commit/7400298ca1e37db7c7dbff43eee5aa082745bbd5) - `2026-11-16T06:28:34Z` - Chaoqun Zhao (@ZhaoChaoqun) - PR: [Add smart home appliance Voice Agent sample](https://github.com/microsoft/voice-agent/pull/136)

### dotnet/efcore (7 commit(s), signal 0)

Tags: `bot-only, dependency-noise, docs`

- [Update dependencies from build 341531 (#39674)](https://github.com/dotnet/efcore/commit/8cc4e9820a3b2aa1984af29020b294c83c6c21ef) - `2026-11-16T22:22:05Z` - dotnet-maestro[bot] (@dotnet-maestro[bot]) - PR: [[main] Source code updates from dotnet/dotnet](https://github.com/dotnet/efcore/pull/39674)
- [Bump FSharp.Core from 11.0.100 to 11.0.101 (#39677)](https://github.com/dotnet/efcore/commit/2152cb1a88efd340bc4d0b7be6ffec6c6d9545d1) - `2026-11-16T22:21:34Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump FSharp.Core from 11.0.100 to 11.0.101](https://github.com/dotnet/efcore/pull/39677)
- [Bump ICSharpCode.Decompiler from 11.1.0.9782 to 11.2.0.10050 (#39678)](https://github.com/dotnet/efcore/commit/758e8ee709ebcad92c7f18df210ce1dca544c1d5) - `2026-11-16T22:21:16Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump ICSharpCode.Decompiler from 11.1.0.9782 to 11.2.0.10050](https://github.com/dotnet/efcore/pull/39678)
- [Bump Microsoft.AspNetCore.Identity.EntityFrameworkCore from 11.0.0-rc…](https://github.com/dotnet/efcore/commit/c5b7e1167e5604c3a7ca2ce1650452a826f76241) - `2026-11-16T22:21:01Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.AspNetCore.Identity.EntityFrameworkCore from 11.0.0-rc.1.26425.128 to 11.0.0](https://github.com/dotnet/efcore/pull/39679)
- [Bump Microsoft.Azure.Cosmos from 3.63.4 to 3.64.0 (#39680)](https://github.com/dotnet/efcore/commit/ae30389df9d4c01d055d7866232f12ed65e3da07) - `2026-11-16T22:20:28Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Azure.Cosmos from 3.63.4 to 3.64.0](https://github.com/dotnet/efcore/pull/39680)

### MicrosoftDocs/SupportArticles-docs (7 commit(s), signal 82)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/2cd37816a396fb9b3700ea0cc62ffe9213efa841) - `2026-11-16T22:05:03Z` - Learn Build Service GitHub App
- [Merge pull request #12870 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/fca08cb5cc784559cb6f1b59beeba2d88059410b) - `2026-11-16T22:02:44Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add MTR or Laptop Video feed disappears (#12847)](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/640a361225da3b0678d9fb16fd6858d0dca0a12f) - `2026-11-16T21:59:39Z` - Shravya Shashidhar (@shravya-agents)
- [Task 8110143: Explain auto-labeling progress and activity count misma…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/1c1cedb7f6855125465abfb94dc7257d504cf8e5) - `2026-11-16T21:54:07Z` - Nick Robinson (@nickjrobinson)
- [Add TSG - Unable to reserve room from Panel (#12842)](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/b4663f9b2f21dfe82c4ca459b023ea4aad9c907e) - `2026-11-16T21:53:55Z` - Shravya Shashidhar (@shravya-agents)

### MicrosoftDocs/power-platform (7 commit(s), signal 82)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/e1df2ac46ff7ac616dcdf7d29c86ba7ed89939b9) - `2026-11-16T21:47:51Z` - Learn Build Service GitHub App
- [Merge pull request #12195 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-platform/commit/1f6785edfbad2e1de9875ccd03c6381970c2acbf) - `2026-11-16T21:46:14Z` - Tapan Maniar (@tapanm-MSFT)
- [Migrate Power Pages ALM content to Power Platform developer guide (#1…](https://github.com/MicrosoftDocs/power-platform/commit/69cd1c24f3602e9d9558b7c6c6c8ad437dddaaf6) - `2026-11-16T19:28:11Z` - Peter Hecke (@phecke)
- [Update to FAQ (#12191)](https://github.com/MicrosoftDocs/power-platform/commit/580d42e36c0c5e66ebf0ccae8e9886c69a4d78ec) - `2026-11-16T19:08:27Z` - Ellen Wehrle (@EllenWehrle)
- [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/7b5b74c84a25a369d76cb4fdf5f058a5f339340d) - `2026-11-16T19:05:06Z` - Learn Build Service GitHub App

### MicrosoftDocs/azure-docs-cli (7 commit(s), signal 92)

Tags: `docs, human-authored, release-language, watchlist`

- [Replace engineering placeholders in the preview Bicep tutorial (#6343)](https://github.com/MicrosoftDocs/azure-docs-cli/commit/3d03cd8deee79796a3949318ce4bdd5b834673a6) - `2026-11-16T21:34:25Z` - M. Baldwin (@msmbaldwin) - PR: [Replace engineering placeholders in the Azure CLI preview Bicep tutorial](https://github.com/MicrosoftDocs/azure-docs-cli/pull/6343)
- [Align Azure CLI preview article names with Latest-version for version…](https://github.com/MicrosoftDocs/azure-docs-cli/commit/d53b2a8ac51727a0f46dec4c8975424fcb2f1938) - `2026-11-16T21:22:18Z` - M. Baldwin (@msmbaldwin) - PR: [Align Azure CLI preview article names with Latest-version for version switching](https://github.com/MicrosoftDocs/azure-docs-cli/pull/6342)
- [Next-gen Azure CLI public preview release for Ignite (#6269)](https://github.com/MicrosoftDocs/azure-docs-cli/commit/6442e9226d135affbc0a85ba401b65eef44db86f) - `2026-11-16T18:54:37Z` - M. Baldwin (@msmbaldwin) - PR: [Stage Azure CLI public preview release for Ignite](https://github.com/MicrosoftDocs/azure-docs-cli/pull/6269)
- [docs: remove outdated Ignite 2024 and AI Shell highlights (#6331)](https://github.com/MicrosoftDocs/azure-docs-cli/commit/74b44f474caebaa24a64e277f274859d7ba1250b) - `2026-11-16T17:48:41Z` - Alex Wang (@Alex-AZPS) - PR: [docs: remove outdated Ignite 2024 and AI Shell highlights](https://github.com/MicrosoftDocs/azure-docs-cli/pull/6331)
- [CI Update](https://github.com/MicrosoftDocs/azure-docs-cli/commit/8aa8cabaa0ec77ea01ff606d23467b5df71d7fb4) - `2026-11-16T12:55:51Z` - docsreference@microsoft.com - PR: [[main to live] Next-gen Azure CLI public preview Ignite release](https://github.com/MicrosoftDocs/azure-docs-cli/pull/6341)

### MicrosoftDocs/msteams-docs (7 commit(s), signal 82)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [[Doc Feature] Chain of Thought (#14683)](https://github.com/MicrosoftDocs/msteams-docs/commit/b548dfcb2b69875c0b17a8a9b7537ffe256c762b) - `2026-11-16T21:12:11Z` - SirajShaik-MSFT (@SirajShaik-MSFT) - PR: [[Doc Feature] Chain of Thought](https://github.com/MicrosoftDocs/msteams-docs/pull/14683)
- [[Doc Improvement] [Update html widgets] (#14735)](https://github.com/MicrosoftDocs/msteams-docs/commit/4f7e309c30c4eaa537873562f8798e408d13a942) - `2026-11-16T17:28:25Z` - v-shalinirob (@v-shalinirob) - PR: [[Doc Improvement] [Update html widgets]](https://github.com/MicrosoftDocs/msteams-docs/pull/14735)
- [Clarify agent factory provisioning, tenant scope, and identity termin…](https://github.com/MicrosoftDocs/msteams-docs/commit/7acc58c431b20e8ad3bb3c087527ef102c2a4f34) - `2026-11-16T06:46:15Z` - Umang (@umangsehgal) - PR: [Clarify agent factory provisioning, tenant scope, and identity terminology](https://github.com/MicrosoftDocs/msteams-docs/pull/14736)
- [Agent factory docs (#14729)](https://github.com/MicrosoftDocs/msteams-docs/commit/631c2be1f8ceb72554987c590b85497ccfcc3965) - `2026-11-16T06:46:15Z` - Nick Walker (@nickwalkmsft) - PR: [Agent factory docs](https://github.com/MicrosoftDocs/msteams-docs/pull/14729)
- [[Doc feature] [Build html widgets] [5934645] (#14708)](https://github.com/MicrosoftDocs/msteams-docs/commit/82142133c78d51f93d740a99512fef0b5c182e3e) - `2026-11-16T00:54:10Z` - v-shalinirob (@v-shalinirob) - PR: [[Doc feature] [Build html widgets] [5934645]](https://github.com/MicrosoftDocs/msteams-docs/pull/14708)

### microsoft/release-manager-assistant (7 commit(s), signal 92)

Tags: `human-authored, product:Azure SDK, release-language, samples, watchlist`

- [Merge pull request #68 from microsoft/copilot/auto-ai-gallery-standar…](https://github.com/microsoft/release-manager-assistant/commit/06d3db05c3b8e6b80d3f5057951dbeccfdb295aa) - `2026-11-16T19:06:46Z` - Shivam Shrivastava (@shshr) - PR: [Enable Docker for azd packaging in the dev container](https://github.com/microsoft/release-manager-assistant/pull/68)
- [Fix azd packaging and registry validation](https://github.com/microsoft/release-manager-assistant/commit/fc1a18d0ac8c72a1bfa608b005e9b2a6042c1a39) - `2026-11-16T18:49:23Z` - shshr (@shshr) - PR: [Enable Docker for azd packaging in the dev container](https://github.com/microsoft/release-manager-assistant/pull/68)
- [Initial plan](https://github.com/microsoft/release-manager-assistant/commit/c8977e3179efe1bb61e51fa728197f645082937e) - `2026-11-16T18:35:02Z` - shshr (@shshr) - PR: [Enable Docker for azd packaging in the dev container](https://github.com/microsoft/release-manager-assistant/pull/68)
- [Merge pull request #67 from microsoft/copilot/fix-template-validation…](https://github.com/microsoft/release-manager-assistant/commit/1f17b83fe0bdf699f9594ac4375a7de600b1736f) - `2026-11-16T18:29:28Z` - Shivam Shrivastava (@shshr) - PR: [Pin template validation action to compatible SDK revision](https://github.com/microsoft/release-manager-assistant/pull/67)
- [Pin fixed template validation action revision](https://github.com/microsoft/release-manager-assistant/commit/c1eb8b7cfac997da919bb5fe18d891d638254730) - `2026-11-16T18:24:09Z` - shshr (@shshr) - PR: [Pin template validation action to compatible SDK revision](https://github.com/microsoft/release-manager-assistant/pull/67)

### dotnet/AspNetCore.Docs (6 commit(s), signal 81)

Tags: `docs, human-authored, watchlist`

- [Archive authentication docs (#38170)](https://github.com/dotnet/AspNetCore.Docs/commit/3fa2a11a52d02a0094f209ade35bd75a75cef46a) - `2026-11-16T22:35:54Z` - Genevieve Warren (@gewarren) - PR: [Archive authentication docs](https://github.com/dotnet/AspNetCore.Docs/pull/38170)
- [Change workflow triggers to 'pull_request' (#38171)](https://github.com/dotnet/AspNetCore.Docs/commit/b405d8f043498175ff9eb6f445148beb0936f816) - `2026-11-16T22:35:26Z` - Genevieve Warren (@gewarren) - PR: [Change workflow triggers to 'pull_request'](https://github.com/dotnet/AspNetCore.Docs/pull/38171)
- [Archive distributed caching docs (#38156)](https://github.com/dotnet/AspNetCore.Docs/commit/c6fdd8bb4d77baff51b6afd2e92d59dd57de4b18) - `2026-11-16T16:39:56Z` - Genevieve Warren (@gewarren) - PR: [Archive distributed caching docs](https://github.com/dotnet/AspNetCore.Docs/pull/38156)
- [Archive logging docs (#38157)](https://github.com/dotnet/AspNetCore.Docs/commit/c67fa824c3d051804165097a8f9cc5b6a11dac6e) - `2026-11-16T16:39:29Z` - Genevieve Warren (@gewarren) - PR: [Archive logging docs](https://github.com/dotnet/AspNetCore.Docs/pull/38157)
- [Clarify OWIN cookie format compatibility and align shared cookie name…](https://github.com/dotnet/AspNetCore.Docs/commit/1a3255587851dbad2721e9b4cde079cc114747d6) - `2026-11-16T16:38:53Z` - Copilot (@Copilot) - PR: [Clarify OWIN cookie format compatibility and align shared cookie names](https://github.com/dotnet/AspNetCore.Docs/pull/38121)

### MicrosoftDocs/dynamics-365-unified-operations-public (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/Dynamics…](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/588e46f9282cc705d71fac79b1977ab2751ed03f) - `2026-11-16T19:05:50Z` - Learn Build Service GitHub App
- [Merge pull request #22858 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/6f71b3127ff785959f1be3351179535b036ebfaa) - `2026-11-16T19:03:25Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Liza fr cert 2026 (#22820)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/94305960a148ddcfe839a53232234655c995613a) - `2026-11-16T18:48:20Z` - Elizaveta Golub (@liza-golub)
- [Update US GCC deployment documentation to clarify Copilot feature sup…](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/1e2034d7a1b1436a0ccdee8a12e8cab23ca5ecc9) - `2026-11-16T15:34:41Z` - Karl Maybach (@kamaybac)
- [Document custom scenarios for agent-generated emails (#22842)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/6f72a2ec3ef8526713f9ce975be245daa0b0c1e7) - `2026-11-16T15:13:11Z` - Ban Luo (@banluo-ms)

### MicrosoftDocs/dynamics-365-project-operations (6 commit(s), signal 91)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/c273b2730e8144068fabab92261176d7a231c0eb) - `2026-11-16T19:02:51Z` - Learn Build Service GitHub App
- [Merge pull request #2827 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/6905f68e8a53de5d99e8ca348eb3c0752b08919c) - `2026-11-16T19:02:18Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add guide for using import tasks API in Dynamics 365 (#2820)](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/2b520e41f008530deac62c9ffd35c915655dd645) - `2026-11-16T14:27:35Z` - Dishant Popli (@dpopli)
- [Updating UR73 Release Notes page with 1 feature's details (#2823)](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/5d3f35f4f7b7289eb74d021b2cbdedddd7d077f9) - `2026-11-16T14:19:49Z` - Mohit Menon (@mohitmenon)
- [Update UR72 hotfix and UR73 release calendar (#2824)](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/5f01b73b92b66f060f62694a4c3e16b79d034093) - `2026-11-16T14:17:52Z` - Pulkit Walia (@pulkitwalia)

### microsoft/kiota-serialization-text-go (6 commit(s), signal 91)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #198 from microsoft/chore/remove-sonar-text-go-a2e…](https://github.com/microsoft/kiota-serialization-text-go/commit/1018f99eb5663a72b50467af7ecca3a17b61ad96) - `2026-11-16T18:48:26Z` - Vincent Biret (@baywet) - PR: [ci: remove SonarCloud analysis](https://github.com/microsoft/kiota-serialization-text-go/pull/198)
- [Merge pull request #196 from hardikkaurani/fix/whitespace-and-nil-safety](https://github.com/microsoft/kiota-serialization-text-go/commit/8967f16c40f95656975009b562157972229a78ed) - `2026-11-16T14:32:53Z` - Vincent Biret (@baywet) - PR: [fix(text): enhance whitespace tolerance and nil receiver safety across parser and writer](https://github.com/microsoft/kiota-serialization-text-go/pull/196)
- [fix(text): remove inaccurate doc claims and expand WriteObjectValue t…](https://github.com/microsoft/kiota-serialization-text-go/commit/b293766bf485aedd369e0d2712a2861ba88556fd) - `2026-11-16T14:22:53Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(text): enhance whitespace tolerance and nil receiver safety across parser and writer](https://github.com/microsoft/kiota-serialization-text-go/pull/196)
- [ci: remove SonarCloud analysis](https://github.com/microsoft/kiota-serialization-text-go/commit/989de6fecbac97c828f69b23e1b64464e7b13d53) - `2026-11-16T14:20:06Z` - Vincent Biret (@baywet) - PR: [ci: remove SonarCloud analysis](https://github.com/microsoft/kiota-serialization-text-go/pull/198)
- [Merge pull request #197 from microsoft/dependabot/go_modules/github.c…](https://github.com/microsoft/kiota-serialization-text-go/commit/1c35b9080afb9ae9dfebaf8b11207e4f6e122cc3) - `2026-11-16T11:32:37Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.0 to 1.12.1](https://github.com/microsoft/kiota-serialization-text-go/pull/197)

### microsoftgraph/github-issue-manager (6 commit(s), signal 21)

Tags: `bot-only, dependency-noise, product:Microsoft Graph, samples, watchlist`

- [Merge pull request #99 from microsoftgraph/dependabot/nuget/src/Style…](https://github.com/microsoftgraph/github-issue-manager/commit/d18bea74bb36fb682983f83cfb450a60aa466aa1) - `2026-11-16T02:16:02Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump StyleCop.Analyzers from 1.2.0-beta.556 to 1.3.180](https://github.com/microsoftgraph/github-issue-manager/pull/99)
- [Bump StyleCop.Analyzers from 1.2.0-beta.556 to 1.3.180](https://github.com/microsoftgraph/github-issue-manager/commit/d974dffbf1cefdcf9c155ebdf1e86c1f550c12c6) - `2026-11-16T02:15:00Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump StyleCop.Analyzers from 1.2.0-beta.556 to 1.3.180](https://github.com/microsoftgraph/github-issue-manager/pull/99)
- [Merge pull request #96 from microsoftgraph/dependabot/nuget/src/Markd…](https://github.com/microsoftgraph/github-issue-manager/commit/46584709ff1800e42e0ab65619ef59ee49749766) - `2026-11-16T02:12:12Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump Markdig from 1.5.1 to 1.6.0](https://github.com/microsoftgraph/github-issue-manager/pull/96)
- [Bump Markdig from 1.5.1 to 1.6.0](https://github.com/microsoftgraph/github-issue-manager/commit/b6e37af2768e419167a2fbcda520b54c0eb90b15) - `2026-11-16T02:11:21Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Markdig from 1.5.1 to 1.6.0](https://github.com/microsoftgraph/github-issue-manager/pull/96)
- [Merge pull request #98 from microsoftgraph/dependabot/nuget/src/Micro…](https://github.com/microsoftgraph/github-issue-manager/commit/a252ccea70cde3e1f8695c57a632a0755bc3a3c8) - `2026-11-16T02:08:22Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump Microsoft.Azure.Functions.Worker.Extensions.DurableTask from 1.21.0 to 1.22.0](https://github.com/microsoftgraph/github-issue-manager/pull/98)

### microsoft/bobsql (6 commit(s), signal 56)

Tags: `human-authored, release-language, samples`

- [Merge pull request #13 from microsoft/bw](https://github.com/microsoft/bobsql/commit/5f428284897570f225a37d95610eeb0a0d46d0da) - `2026-11-15T23:28:54Z` - Bob Ward (@rgward) - PR: [Bw](https://github.com/microsoft/bobsql/pull/13)
- [Merge remote-tracking branch 'origin/main' into bw](https://github.com/microsoft/bobsql/commit/583126d48bc97ba0651c496770fdde0ba62f3a76) - `2026-11-15T23:27:55Z` - rgward (@rgward) - PR: [Bw](https://github.com/microsoft/bobsql/pull/13)
- [Merge pull request #12 from microsoft/sqlversioning-demo-refinements](https://github.com/microsoft/bobsql/commit/0b416e73bb2061de5af0f91ffc0d4d149852dfd7) - `2026-11-15T23:24:06Z` - Bob Ward (@rgward) - PR: [revisions for versioning](https://github.com/microsoft/bobsql/pull/12)
- [revisions for versioning](https://github.com/microsoft/bobsql/commit/c3273d66aecce2542baf7cf6115cc68d5d1d588c) - `2026-11-15T23:23:12Z` - Bob Ward (@rgward) - PR: [revisions for versioning](https://github.com/microsoft/bobsql/pull/12)
- [Merge pull request #11 from microsoft/add-sqllocal-public-demo](https://github.com/microsoft/bobsql/commit/60e7a266daf3dab605e29f64dcc95a0b924540fd) - `2026-11-15T19:06:08Z` - Bob Ward (@rgward) - PR: [Add sanitized SQL Local demo and folder documentation](https://github.com/microsoft/bobsql/pull/11)

### Azure-Samples/azure-functions-hosted-skills-samples (5 commit(s), signal 45)

Tags: `human-authored, samples`

- [Merge pull request #8 from Azure-Samples/hallvictoria/hosted-skill-bi…](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/commit/be06879a0eb29d02f7d3c1b94a92fa70c15d3a64) - `2026-11-16T21:17:53Z` - hallvictoria (@hallvictoria) - PR: [Add Hosted Skill binding starter and supplier review samples](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/pull/8)
- [docs: add Learn metadata to hosted skill binding samples](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/commit/5da2f8b1e9948067b9c424f4d8fc86ebbf7eba4d) - `2026-11-16T21:06:16Z` - Victoria Hall (@hallvictoria) - PR: [Add Hosted Skill binding starter and supplier review samples](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/pull/8)
- [Merge pull request #9 from Azure-Samples/tsuyoshiushio-add-sample-rea…](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/commit/bc4fc749a083db27a26cf060455d48fd3c26c9d6) - `2026-11-16T20:56:24Z` - Tsuyoshi Ushio (@TsuyoshiUshio) - PR: [Add Learn samples browser metadata to sample READMEs](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/pull/9)
- [Add Learn samples browser metadata to sample READMEs](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/commit/cba44c381548977bd358941e34383c9f682e36f5) - `2026-11-16T20:20:05Z` - Tsuyoshi Ushio (@TsuyoshiUshio) - PR: [Add Learn samples browser metadata to sample READMEs](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/pull/9)
- [Add Hosted Skill binding starter and supplier review samples](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/commit/53926590a11bec70feec0802f011389745d7b620) - `2026-11-16T19:05:54Z` - Victoria Hall (@hallvictoria) - PR: [Add Hosted Skill binding starter and supplier review samples](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/pull/8)

### MicrosoftDocs/azure-docs-sdk-node (5 commit(s), signal 80)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/00999d5fa917af95d45e7b933fb1287709d18171) - `2026-11-16T20:37:45Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/9da18397fa4aaea20239bc6a33adb5aea1892576) - `2026-11-16T18:00:04Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/4d10e4285446b2f599616b5bdd2cbe9b7ad820b6) - `2026-11-16T14:36:44Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/b6706dbd80f1de84849ad0e11135acc7a8c7439f) - `2026-11-16T10:46:41Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/088ebb2cdd1df3e044dfa04f318917cef72b8781) - `2026-11-16T06:16:05Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/azure-docs-sdk-python (5 commit(s), signal 80)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/c840d6f11525b7c624918004148d910ed355ad31) - `2026-11-16T20:13:56Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/2a382cecc52ef2b28f3362acdced14e3c47c6d4f) - `2026-11-16T19:10:01Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/b2ffc6fdc0cfe3a4d10bfa65bdaf2b5e7be49199) - `2026-11-16T15:58:25Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/14c5a9a7bfeabcd57edf0f9560f665cfa42919ce) - `2026-11-16T09:05:28Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/22581472f3956c342e5784c87c9b7badab9f15bf) - `2026-11-16T06:56:31Z` - azure-sdk (@azure-sdk)

### microsoft/terraform-provider-power-platform (5 commit(s), signal 105)

Tags: `docs, human-authored, security, watchlist`

- [fix: populate environment_id, connection id and principal from import…](https://github.com/microsoft/terraform-provider-power-platform/commit/daf4472591bc158cfbb88fb6ba1f8e78ae8a2019) - `2026-11-16T19:16:22Z` - Mateusz Wasilewski (@mawasile) - PR: [fix: populate environment_id, connection id and principal from import ID for connection_share](https://github.com/microsoft/terraform-provider-power-platform/pull/1332)
- [ci: gate acceptance test credentials behind protected environments (#…](https://github.com/microsoft/terraform-provider-power-platform/commit/14849fee50dd01fb434c935557dfeca61a3570da) - `2026-11-16T18:29:26Z` - Mateusz Wasilewski (@mawasile) - PR: [ci: gate acceptance test credentials behind protected environments](https://github.com/microsoft/terraform-provider-power-platform/pull/1305)
- [fix(data_record): remove resource from state when the row was deleted…](https://github.com/microsoft/terraform-provider-power-platform/commit/ded7a11dad5502b0c7f8b59988e5c05009f55433) - `2026-11-16T14:13:53Z` - Alex Sweet (@sweetgiorni) - PR: [fix(data_record): remove resource from state when the row was deleted outside Terraform](https://github.com/microsoft/terraform-provider-power-platform/pull/1330)
- [fix: populate environment_id from import ID for connection and soluti…](https://github.com/microsoft/terraform-provider-power-platform/commit/2a107af77909cd49bfd6fd166578696bdd0a4672) - `2026-11-16T12:10:02Z` - Alex Sweet (@sweetgiorni) - PR: [fix: populate environment_id from import ID for connection and solution](https://github.com/microsoft/terraform-provider-power-platform/pull/1329)
- [ci: use golangci-lint v2.9.0 in Copilot setup steps (#1331)](https://github.com/microsoft/terraform-provider-power-platform/commit/0b797f7ad467f42f4e37fd341bcda2b8e89cb968) - `2026-11-16T08:01:08Z` - Alex Sweet (@sweetgiorni) - PR: [ci: use golangci-lint v2.9.0 in Copilot setup steps](https://github.com/microsoft/terraform-provider-power-platform/pull/1331)

### microsoft/kiota-serialization-multipart-go (5 commit(s), signal 90)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #154 from microsoft/chore/remove-sonar-multipart-g…](https://github.com/microsoft/kiota-serialization-multipart-go/commit/2dd5b4543eef5566a2cae91cf1849458a65803e9) - `2026-11-16T18:48:37Z` - Vincent Biret (@baywet) - PR: [ci: remove SonarCloud integration](https://github.com/microsoft/kiota-serialization-multipart-go/pull/154)
- [ci: remove SonarCloud integration](https://github.com/microsoft/kiota-serialization-multipart-go/commit/04b99bdf60b7c12250e16baaca0fb388427d6e34) - `2026-11-16T14:20:07Z` - Vincent Biret (@baywet) - PR: [ci: remove SonarCloud integration](https://github.com/microsoft/kiota-serialization-multipart-go/pull/154)
- [Merge pull request #147 from hardikkaurani/fix/header-validation-and-…](https://github.com/microsoft/kiota-serialization-multipart-go/commit/cc858b4987a7170490a2da2c11df607685028db1) - `2026-11-16T14:12:48Z` - Vincent Biret (@baywet) - PR: [fix(multipart): validate header keys and reject colons, whitespace, and null characters in WriteStringValue](https://github.com/microsoft/kiota-serialization-multipart-go/pull/147)
- [Merge pull request #152 from microsoft/dependabot/go_modules/github.c…](https://github.com/microsoft/kiota-serialization-multipart-go/commit/b6edaf6e9a4f8bfa89197ccf06b4d237de3091f5) - `2026-11-16T11:34:10Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.0 to 1.12.1](https://github.com/microsoft/kiota-serialization-multipart-go/pull/152)
- [build(deps): bump github.com/microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-serialization-multipart-go/commit/d78140a491671e9d928285c185bab4ed302c9993) - `2026-11-16T00:42:52Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.0 to 1.12.1](https://github.com/microsoft/kiota-serialization-multipart-go/pull/152)

### MicrosoftDocs/windowsserverdocs (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/windowss…](https://github.com/MicrosoftDocs/windowsserverdocs/commit/1b24b91e309bdcacbf20431cfbbd0a597a68a8bc) - `2026-11-16T18:34:00Z` - Learn Build Service GitHub App
- [Merge pull request #9900 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/windowsserverdocs/commit/88e6dda8664fad64b61e6c228bbee03a8d0ad3fd) - `2026-11-16T18:32:22Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Windows Admin Center Virtualization Mode Ignite 2026 (#9897)](https://github.com/MicrosoftDocs/windowsserverdocs/commit/42a75a5c860e30354a5ac70d4d4a7873b1e32470) - `2026-11-16T18:28:04Z` - Robin Harwood (@robinharwood)
- [Refine token factory metadata and accessibility (#9898)](https://github.com/MicrosoftDocs/windowsserverdocs/commit/a75e39344944a90a83c113c89f520fa2838ad08f) - `2026-11-16T18:18:44Z` - Robin Harwood (@robinharwood)
- [Add local AI token factory guidance for Windows Server (#8626)](https://github.com/MicrosoftDocs/windowsserverdocs/commit/2869ae9a5e988f327d2d6c2a1ca34993bffb8d40) - `2026-11-16T17:49:25Z` - Robin Harwood (@robinharwood)

### microsoft/finops-toolkit (5 commit(s), signal 90)

Tags: `docs, human-authored, product:Azure AI, product:PowerShell, release-language, watchlist`

- [docs(hubs): Warn that exports of the same dataset and scope replace e…](https://github.com/microsoft/finops-toolkit/commit/2975555dae5c9ab637659e22e38375792a6f20b3) - `2026-11-16T13:25:05Z` - Roland Krummenacher (@RolandKrummenacher) - PR: [docs(hubs): Warn that exports of the same dataset and scope replace each other](https://github.com/microsoft/finops-toolkit/pull/2412)
- [fix(release): Add release steps for blog link, Advisor workbook, and …](https://github.com/microsoft/finops-toolkit/commit/a05029baf468ec8c3a05e581a08f0354870f823b) - `2026-11-16T13:23:02Z` - Roland Krummenacher (@RolandKrummenacher) - PR: [fix(release): Add release steps for blog link, Advisor workbook, and Quickstart metadata](https://github.com/microsoft/finops-toolkit/pull/2421)
- [fix(hubs): Stop dropping reservation details and undated recommendati…](https://github.com/microsoft/finops-toolkit/commit/6f69badea9c81557cfd547509d3144e4bba3b15a) - `2026-11-16T07:50:48Z` - Roland Krummenacher (@RolandKrummenacher) - PR: [fix(hubs): Stop dropping reservation details and undated recommendations](https://github.com/microsoft/finops-toolkit/pull/2407)
- [fix(agents): Fix support report query limit and stale contributor doc…](https://github.com/microsoft/finops-toolkit/commit/95cbbfcc6f4623be23a1ee8401ce18c94693edf2) - `2026-11-16T07:50:29Z` - Roland Krummenacher (@RolandKrummenacher) - PR: [fix(agents): Fix support report query limit and stale contributor docs](https://github.com/microsoft/finops-toolkit/pull/2411)
- [feat(hubs): Load instance size flexibility open data (#2413)](https://github.com/microsoft/finops-toolkit/commit/5f241ea3c3ed9b52f12e70a0060042d55fe8489b) - `2026-11-16T07:50:07Z` - Roland Krummenacher (@RolandKrummenacher) - PR: [feat(hubs): Load instance size flexibility open data](https://github.com/microsoft/finops-toolkit/pull/2413)

### dotnet/eShop (4 commit(s), signal 0)

Tags: `bot-only, dependency-noise, docs`

- [Bump Grpc.Net.Client and Grpc.Tools (#1044)](https://github.com/dotnet/eShop/commit/07e46f6998ab6194e1c278fe87f93e75c8b14efc) - `2026-11-16T22:48:18Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Grpc.Net.Client and Grpc.Tools](https://github.com/dotnet/eShop/pull/1044)
- [Bump Google.Protobuf from 3.29.3 to 3.36.2 (#1049)](https://github.com/dotnet/eShop/commit/53669198be66a54f75a0caf8a0a5a38e54dcbdd7) - `2026-11-16T22:35:47Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Google.Protobuf from 3.29.3 to 3.36.2](https://github.com/dotnet/eShop/pull/1049)
- [Bump the opentelemetry group with 5 updates (#1084)](https://github.com/dotnet/eShop/commit/6817251273c6c3a3cc2fdd1703af4d5bc40b31fd) - `2026-11-16T22:35:39Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the opentelemetry group with 5 updates](https://github.com/dotnet/eShop/pull/1084)
- [Bump Scalar.AspNetCore from 2.17.10 to 2.21.0 (#1088)](https://github.com/dotnet/eShop/commit/85a5c7bfb9ed733279a27ad3eda3f3dded0cd316) - `2026-11-16T22:35:32Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Scalar.AspNetCore from 2.17.10 to 2.21.0](https://github.com/dotnet/eShop/pull/1088)

### Azure/iotedge-eflow (4 commit(s), signal 129)

Tags: `docs, human-authored, release, release-language, watchlist`

- Release: [1.6.1.11026 LTS](https://github.com/Azure/iotedge-eflow/releases/tag/1.6.1.11026) - `2026-11-16T22:03:23Z`
- [Merge pull request #320 from nnamuhcs/docs/eflow-1.6.1.11026-release-…](https://github.com/Azure/iotedge-eflow/commit/0136dd266ca4a5d7cf47ece97811ee1dc3be4f94) - `2026-11-16T21:51:00Z` - Joseph Knierman (@josephknierman) - PR: [Add EFLOW 1.6.1.11026 LTS release notes](https://github.com/Azure/iotedge-eflow/pull/320)
- [Merge pull request #321 from nnamuhcs/docs/eflow-1.6-readme](https://github.com/Azure/iotedge-eflow/commit/c64d5197f0b50a7e001a367a4d22a5a5c52249f8) - `2026-11-16T21:44:33Z` - Joseph Knierman (@josephknierman) - PR: [Update README for EFLOW 1.6 LTS](https://github.com/Azure/iotedge-eflow/pull/321)
- [Update README for EFLOW 1.6 LTS](https://github.com/Azure/iotedge-eflow/commit/cdfce3893b36bc119407ec12876c898fcb502f61) - `2026-11-16T19:32:31Z` - Schumann - PR: [Update README for EFLOW 1.6 LTS](https://github.com/Azure/iotedge-eflow/pull/321)
- [Clarify EFLOW runtime container image upgrades](https://github.com/Azure/iotedge-eflow/commit/63ca57f2609a3a4530eb07641728e9180ad40dc8) - `2026-11-16T18:51:43Z` - Schumann - PR: [Add EFLOW 1.6.1.11026 LTS release notes](https://github.com/Azure/iotedge-eflow/pull/320)

### microsoft/playwright.dev (4 commit(s), signal 0)

Tags: `bot-only, dependency-noise, docs`

- [chore(deps): bump joi from 17.13.8 to 17.13.9 (#2191)](https://github.com/microsoft/playwright.dev/commit/0d957c77eb1259634d265c0b1c79260c0a7d4825) - `2026-11-16T21:33:10Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump joi from 17.13.8 to 17.13.9](https://github.com/microsoft/playwright.dev/pull/2191)
- [chore(deps): bump qs from 6.15.2 to 6.15.4 (#2190)](https://github.com/microsoft/playwright.dev/commit/ac1fb9fc360fe4cfedc2473b5a8f3de84a3839da) - `2026-11-16T21:32:54Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump qs from 6.15.2 to 6.15.4](https://github.com/microsoft/playwright.dev/pull/2190)
- [chore(deps): bump follow-redirects from 1.16.1 to 1.16.3 (#2189)](https://github.com/microsoft/playwright.dev/commit/4269fd16b8029b5d4c12077ab13060c3f8cce9c7) - `2026-11-16T21:31:13Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump follow-redirects from 1.16.1 to 1.16.3](https://github.com/microsoft/playwright.dev/pull/2189)
- [chore(deps): bump katex and mermaid (#2188)](https://github.com/microsoft/playwright.dev/commit/d6b767011c92910b96460e8192bc2f14fe3ef5f4) - `2026-11-16T21:30:46Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump katex and mermaid](https://github.com/microsoft/playwright.dev/pull/2188)

### MicrosoftDocs/powerapps-docs (4 commit(s), signal 79)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/powerapp…](https://github.com/MicrosoftDocs/powerapps-docs/commit/53af4f410e14e85190916f1c2f882a8f06a61ce2) - `2026-11-16T19:09:43Z` - Learn Build Service GitHub App
- [Merge pull request #12861 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/powerapps-docs/commit/dc759a2426af7032518ddbe85aacaf1976efba1e) - `2026-11-16T19:07:37Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Monitoring Dashboard documentation DON'T PUBLISH BEFORE 11/16 (#12845)](https://github.com/MicrosoftDocs/powerapps-docs/commit/7b316ba9356f152aec57ff4422f502cfdc607c93) - `2026-11-16T16:46:21Z` - Anirudha Bakore (@anibakore-msft)
- [Add environment lifecycle guidance for Fabric links and retention - 1…](https://github.com/MicrosoftDocs/powerapps-docs/commit/c79db97b3755b0f7121502284cec697dd21cf80a) - `2026-11-16T16:35:34Z` - Anirudha Bakore (@anibakore-msft)

### microsoft/kiota-serialization-form-go (4 commit(s), signal 79)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #174 from microsoft/chore/remove-sonar-serializati…](https://github.com/microsoft/kiota-serialization-form-go/commit/706294876254a3f9044dfa6a5b3944fa4c0a0b8b) - `2026-11-16T18:48:36Z` - Vincent Biret (@baywet) - PR: [ci: remove SonarCloud analysis](https://github.com/microsoft/kiota-serialization-form-go/pull/174)
- [Merge pull request #173 from hardikkaurani/fix/writer-buffer-lifecycl…](https://github.com/microsoft/kiota-serialization-form-go/commit/84179b4c3d7bc89188a0907a8818d21e3ea39185) - `2026-11-16T14:32:25Z` - Vincent Biret (@baywet) - PR: [fix(form): prevent sequential buffer corruption and improve direct key lookup safety](https://github.com/microsoft/kiota-serialization-form-go/pull/173)
- [fix(form): remove unused trimLastPropertySeparator method](https://github.com/microsoft/kiota-serialization-form-go/commit/d51c848bb20e6879a7493e970e02fe1185312111) - `2026-11-16T14:25:56Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(form): prevent sequential buffer corruption and improve direct key lookup safety](https://github.com/microsoft/kiota-serialization-form-go/pull/173)
- [ci: remove SonarCloud analysis](https://github.com/microsoft/kiota-serialization-form-go/commit/1d12ff10fcf312aa79c4f9fddbaf5795e7dddafa) - `2026-11-16T14:19:47Z` - Vincent Biret (@baywet) - PR: [ci: remove SonarCloud analysis](https://github.com/microsoft/kiota-serialization-form-go/pull/174)

### microsoft/kiota-serialization-json-go (4 commit(s), signal 89)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #238 from microsoft/chore/remove-sonar-20261116](https://github.com/microsoft/kiota-serialization-json-go/commit/ba90acfd9773b4546c24cc60b3ca69f2177ac12b) - `2026-11-16T18:46:23Z` - Vincent Biret (@baywet) - PR: [ci: remove obsolete SonarCloud integration](https://github.com/microsoft/kiota-serialization-json-go/pull/238)
- [ci: remove obsolete SonarCloud integration](https://github.com/microsoft/kiota-serialization-json-go/commit/ea37f5c1b3c6f92f9b16081aec89e8cc60fe334b) - `2026-11-16T14:20:06Z` - Vincent Biret (@baywet) - PR: [ci: remove obsolete SonarCloud integration](https://github.com/microsoft/kiota-serialization-json-go/pull/238)
- [Merge pull request #237 from microsoft/dependabot/go_modules/github.c…](https://github.com/microsoft/kiota-serialization-json-go/commit/473d28544270ab33fe82f40ffabcec979620f410) - `2026-11-16T11:27:51Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.0 to 1.12.1](https://github.com/microsoft/kiota-serialization-json-go/pull/237)
- [build(deps): bump github.com/microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-serialization-json-go/commit/17d8989396f3695ac4a449c23466effc570b726d) - `2026-11-16T06:59:04Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump github.com/microsoft/kiota-abstractions-go from 1.12.0 to 1.12.1](https://github.com/microsoft/kiota-serialization-json-go/pull/237)

### MicrosoftDocs/azure-stack-docs (4 commit(s), signal 114)

Tags: `docs, human-authored, release-language, security, watchlist`

- [Merge pull request #4599 from MicrosoftDocs/main639304489049337484syn…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/cc1ff1ea7060f59d2278de9b63ea19346a4a1c04) - `2026-11-16T18:02:02Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4599)
- [Merging changes synced from https://github.com/MicrosoftDocs/azure-st…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/8d420b47c0a5ea188d692b6e23be7194e50a560d) - `2026-11-16T18:01:41Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4599)
- [<Publish on Nov 16, 2026@10AM> 2610 November security update release-…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/d60c3fdf45f4c9a3925580308c6bd32fa1c2455b) - `2026-11-16T18:00:23Z` - Bowen Yang (@Albertyang0) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4599)
- [<Publish on Nov 16, 2026@10AM> 2610 November security update release-…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/8ccc2718c2375d69ea348da6dfda5b99e6e66322) - `2026-11-16T16:53:11Z` - Manika Dhiman (@ManikaDhiman) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4599)

### Azure/azure-sdk-for-go (4 commit(s), signal 119)

Tags: `docs, human-authored, product:Azure SDK, release, watchlist`

- Release: [sdk/resourcemanager/keyvault/armkeyvault/v2.2.0-beta.1](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/keyvault/armkeyvault/v2.2.0-beta.1) - `2026-11-16T17:46:13Z`
- Release: [sdk/resourcemanager/eventhub/armeventhub/v2.0.0-beta.2](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/eventhub/armeventhub/v2.0.0-beta.2) - `2026-11-16T09:42:51Z`
- [Configurations:  'specification/keyvault/resource-manager/Microsoft.K…](https://github.com/Azure/azure-sdk-for-go/commit/f13e3dbeabff9d1c39972eed38425d97a80c0554) - `2026-11-16T17:10:27Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR sdk-resourcemanager/keyvault/armkeyvault]-generated-from-SDK Generation - Go-7066458](https://github.com/Azure/azure-sdk-for-go/pull/28013)
- [[AutoPR sdk-resourcemanager/eventhub/armeventhub]-generated-from-SDK …](https://github.com/Azure/azure-sdk-for-go/commit/ae5c42634d6efd0384d6107e71912bbb1893cdfd) - `2026-11-16T09:01:56Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR sdk-resourcemanager/eventhub/armeventhub]-generated-from-SDK Generation - Go-7063599](https://github.com/Azure/azure-sdk-for-go/pull/27234)
- [[skip ci] [Automation] Regenerate SDK based on typespec-go (main) (#2…](https://github.com/Azure/azure-sdk-for-go/commit/bcb5619d083434831f81125c9a98ff07039509f6) - `2026-11-16T04:39:56Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[skip ci] [Automation] Regenerate SDK based on typespec-go (main)](https://github.com/Azure/azure-sdk-for-go/pull/28053)
- [Set min-integrity to none for mgmt-review (#28040)](https://github.com/Azure/azure-sdk-for-go/commit/a40106ca7b0da8f4f7e5fd3caddf4fbc15962032) - `2026-11-16T02:47:31Z` - Chenjie Shi (@tadelesh) - PR: [Set min-integrity to none for mgmt-review](https://github.com/Azure/azure-sdk-for-go/pull/28040)

### microsoftgraph/msgraph-sample-copilot-plugin (4 commit(s), signal 19)

Tags: `bot-only, dependency-noise, product:Microsoft Graph, samples, watchlist`

- [Merge pull request #162 from microsoftgraph/dependabot/nuget/api/Styl…](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/commit/a4a9ecf612f7a444cba144de99bb58d81154cd92) - `2026-11-16T08:23:35Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump StyleCop.Analyzers from 1.2.0-beta.556 to 1.3.180](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/pull/162)
- [Merge pull request #160 from microsoftgraph/dependabot/nuget/api/Micr…](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/commit/b9377ca52d1d0f7b13124541a34a5f843f15d91e) - `2026-11-16T08:23:29Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump Microsoft.AspNetCore.OpenApi from 10.0.14 to 10.0.15](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/pull/160)
- [Bump StyleCop.Analyzers from 1.2.0-beta.556 to 1.3.180](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/commit/95f7e58c78da61b1b4d8c13ae2275e446cabe981) - `2026-11-16T08:22:39Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump StyleCop.Analyzers from 1.2.0-beta.556 to 1.3.180](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/pull/162)
- [Bump Microsoft.AspNetCore.OpenApi from 10.0.14 to 10.0.15](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/commit/942cdcd1c1d253ac799cc2dda4fe3bf3e005f321) - `2026-11-16T08:22:21Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.AspNetCore.OpenApi from 10.0.14 to 10.0.15](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/pull/160)

### Azure/azure-dev (3 commit(s), signal 128)

Tags: `human-authored, product:Azure AI, product:Azure SDK, release, release-language, samples, watchlist`

- Release: [azure-dev-cli_1.38.0](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.38.0) - `2026-11-16T18:57:24Z`
- [Increment CLI version after release (#10966)](https://github.com/Azure/azure-dev/commit/71234bd693a61b6f8ad9c5e6518539e932588702) - `2026-11-16T22:38:36Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment CLI version after release](https://github.com/Azure/azure-dev/pull/10966)
- [Ue GitHub app baed login instead of PAT for azd release (#10955)](https://github.com/Azure/azure-dev/commit/bb7f49a33ca8814612da888b3af3b928d470a091) - `2026-11-16T16:38:00Z` - Praveen Kuttappan (@praveenkuttappan) - PR: [Use GitHub app based login instead of PAT for azd release](https://github.com/Azure/azure-dev/pull/10955)
- [fix(agents): check prompt agent existence before create to avoid 409s…](https://github.com/Azure/azure-dev/commit/64bb3caead3b1377d2425e9c05c945450bc0e93f) - `2026-11-16T06:21:05Z` - Zhijie Huang (@hund030) - PR: [fix(agents): check prompt agent existence before create to avoid 409s](https://github.com/Azure/azure-dev/pull/10954)

### MicrosoftDocs/azure-docs-powershell (3 commit(s), signal 88)

Tags: `docs, human-authored, product:PowerShell, release-language, watchlist`

- [Replace engineering placeholders in Azure PowerShell preview Bicep an…](https://github.com/MicrosoftDocs/azure-docs-powershell/commit/605b6f3619003bf9c4c358a43602aed3d0d5822c) - `2026-11-16T22:30:44Z` - M. Baldwin (@msmbaldwin) - PR: [Replace engineering placeholders in Azure PowerShell preview Bicep and VM tutorials](https://github.com/MicrosoftDocs/azure-docs-powershell/pull/4504)
- [Align Azure PowerShell preview article names with azps-16.5.0 for ver…](https://github.com/MicrosoftDocs/azure-docs-powershell/commit/e07091f85162dcaf36e1a2610a0f5fe6af314de7) - `2026-11-16T21:31:01Z` - M. Baldwin (@msmbaldwin) - PR: [Align Azure PowerShell preview article names with azps-16.5.0 for version switching](https://github.com/MicrosoftDocs/azure-docs-powershell/pull/4503)
- [Next-gen Azure PowerShell public preview release for Ignite (#4441)](https://github.com/MicrosoftDocs/azure-docs-powershell/commit/321a34b1351bfef2f878361c89531df2cfbd08f2) - `2026-11-16T18:54:59Z` - M. Baldwin (@msmbaldwin) - PR: [Stage Azure PowerShell public preview release for Ignite](https://github.com/MicrosoftDocs/azure-docs-powershell/pull/4441)

### Azure/dacs (3 commit(s), signal 43)

Tags: `bot-only, dependency-noise, samples, security, watchlist`

- [build(deps): bump the docker group across 2 directories with 1 update](https://github.com/Azure/dacs/commit/e530dc8bd487970187823b1eb3c3aefd938f57e4) - `2026-11-16T20:37:00Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump the docker group across 2 directories with 1 update](https://github.com/Azure/dacs/pull/190)
- [ci(deps): bump step-security/harden-runner](https://github.com/Azure/dacs/commit/751360399cf89ca94b6631a69f8567ae296043b6) - `2026-11-16T15:11:19Z` - dependabot[bot] (@dependabot[bot]) - PR: [ci(deps): bump step-security/harden-runner from 2.22.3 to 2.22.4 in the github-actions group](https://github.com/Azure/dacs/pull/185)
- [ci(deps): bump go.opentelemetry.io/otel/trace](https://github.com/Azure/dacs/commit/19e0f7203d76b4748f2cb44a89586026daf5c4e6) - `2026-11-16T14:18:35Z` - dependabot[bot] (@dependabot[bot]) - PR: [ci(deps): bump go.opentelemetry.io/otel/trace from 1.45.0 to 1.47.0 in /src/subsystems/cache-controller](https://github.com/Azure/dacs/pull/187)

### Azure-Samples/azure-iot-accelerator-workload-for-fabric-rti (3 commit(s), signal 83)

Tags: `human-authored, release, samples`

- Release: [v2.0.0](https://github.com/Azure-Samples/azure-iot-accelerator-workload-for-fabric-rti/releases/tag/v2.0.0) - `2026-11-16T19:49:43Z`
- [Merge pull request #7 from Azure-Samples/peolivei/e2e](https://github.com/Azure-Samples/azure-iot-accelerator-workload-for-fabric-rti/commit/38479f4352d601d5bbde81e24b2f2960f2199d18) - `2026-11-16T19:51:09Z` - peolivei2 (@peolivei2) - PR: [Automated E2E tests](https://github.com/Azure-Samples/azure-iot-accelerator-workload-for-fabric-rti/pull/7)
- [Merge pull request #6 from Azure-Samples/peolivei/workload-v2](https://github.com/Azure-Samples/azure-iot-accelerator-workload-for-fabric-rti/commit/262ad2b6b46b4397921548cdd933abf042bca2e7) - `2026-11-16T19:46:24Z` - peolivei2 (@peolivei2) - PR: [Workload v2](https://github.com/Azure-Samples/azure-iot-accelerator-workload-for-fabric-rti/pull/6)
- [E2E fixes](https://github.com/Azure-Samples/azure-iot-accelerator-workload-for-fabric-rti/commit/875614a7e16d68f45ce91d5eb9965354695bcbc7) - `2026-11-16T19:20:19Z` - Peri Alves (@peolivei2) - PR: [Automated E2E tests](https://github.com/Azure-Samples/azure-iot-accelerator-workload-for-fabric-rti/pull/7)

### MicrosoftDocs/azure-docs-sdk-java (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/55bf95fd1f8158f47277fc9d1892a3504eb3be2b) - `2026-11-16T19:32:10Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/587b8d9b6b2c40f6a479aa867bddc1878e0f6dc2) - `2026-11-16T18:58:40Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/5ce0ef8f36bac83a1751b4167893d2de0e8f3743) - `2026-11-16T10:52:01Z` - azure-sdk (@azure-sdk)

### microsoft/kiota-python (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #899 from microsoft/chore/remove-sonar-20261116](https://github.com/microsoft/kiota-python/commit/4e6f5c2cf626bbf9c4ed6ca8761b95263d1cd259) - `2026-11-16T18:46:48Z` - Vincent Biret (@baywet) - PR: [chore: remove remaining Sonar suppressions](https://github.com/microsoft/kiota-python/pull/899)
- [Merge pull request #891 from microsoft/dependabot/pip/packages/serial…](https://github.com/microsoft/kiota-python/commit/525b9e012944e62868913a0a466d77c240dcc07d) - `2026-11-16T14:23:48Z` - Vincent Biret (@baywet) - PR: [chore(deps-dev): update types-python-dateutil requirement from <3.0.0,>=2.9.0.20261029 to >=2.9.0.20261104,<3.0.0 in /packages/serialization/form](https://github.com/microsoft/kiota-python/pull/891)
- [chore: remove remaining Sonar suppressions](https://github.com/microsoft/kiota-python/commit/bb6ef73f658937f7350d428c3bf2b0b21b7d738a) - `2026-11-16T14:20:50Z` - Vincent Biret (@baywet) - PR: [chore: remove remaining Sonar suppressions](https://github.com/microsoft/kiota-python/pull/899)

### microsoft/TypeAgent (3 commit(s), signal 78)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [memory: make incremental view maintenance evidence-grounded (#3289)](https://github.com/microsoft/TypeAgent/commit/79205019103b2f18e9b7388ad7b57d699ae4a9f1) - `2026-11-16T18:28:26Z` - Hillary Mutisya (@hillary-mutisya) - PR: [memory: make incremental view maintenance evidence-grounded](https://github.com/microsoft/TypeAgent/pull/3289)
- [memory: use restricted Luna for topic reconciliation (#3288)](https://github.com/microsoft/TypeAgent/commit/ef2da48c0de9098a2f433793959cd7ea8fe8265b) - `2026-11-15T23:12:03Z` - Hillary Mutisya (@hillary-mutisya) - PR: [memory: use restricted Luna for topic reconciliation](https://github.com/microsoft/TypeAgent/pull/3288)
- [memory: use choice-only Luna verdicts for bounded Wiki decisions (#3287)](https://github.com/microsoft/TypeAgent/commit/6e8257c217c1da9bc0a6f5086d82fc8b981973a7) - `2026-11-15T23:11:41Z` - Hillary Mutisya (@hillary-mutisya) - PR: [memory: use choice-only Luna verdicts for bounded Wiki decisions](https://github.com/microsoft/TypeAgent/pull/3287)

### MicrosoftDocs/dynamics-365-contact-center (3 commit(s), signal 88)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/c6832f443097d3ac25a60fddf192f827159a8a01) - `2026-11-16T07:03:30Z` - Learn Build Service GitHub App
- [Merge pull request #824 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/290cc7b6cfc3e20c7e4d6c36e6b82f8b8c2f8c6f) - `2026-11-16T07:03:07Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Publish preview docs for Human Assist feature. (#822)](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/e632b8eb17a1a8d8001f4bc3d20e77f894482522) - `2026-11-16T06:06:18Z` - Neeraja Nellimarla (@neeranelli)

### Azure/template-reference-generator (3 commit(s), signal 18)

Tags: `bot-only, dependency-noise, reference, watchlist`

- [Bump System.IO.Abstractions from 22.3.0 to 23.0.0 (#232)](https://github.com/Azure/template-reference-generator/commit/d846557866e06e5c18628f297fbf620c13ecda43) - `2026-11-15T23:56:24Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump System.IO.Abstractions from 22.3.0 to 23.0.0](https://github.com/Azure/template-reference-generator/pull/232)
- [Bump Microsoft.SourceLink.GitHub from 10.0.403 to 11.0.100 (#230)](https://github.com/Azure/template-reference-generator/commit/06187290e8b40de37cc8cbbc823e33e290df42f9) - `2026-11-15T23:55:41Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.SourceLink.GitHub from 10.0.403 to 11.0.100](https://github.com/Azure/template-reference-generator/pull/230)
- [Bump actions/setup-dotnet from 6.0.0 to 6.1.0 (#229)](https://github.com/Azure/template-reference-generator/commit/3b156261f7d3e0512dc1ca8de1292620502a2839) - `2026-11-15T23:53:16Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-dotnet from 6.0.0 to 6.1.0](https://github.com/Azure/template-reference-generator/pull/229)

### MicrosoftDocs/cloud-adoption-framework (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/cloud-ad…](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/4268f897a465b1065e009cfcd2a7c1da35c63335) - `2026-11-15T19:10:21Z` - Learn Build Service GitHub App
- [Merge pull request #7445 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/bcb8e5fbe08bb336a120600f6fb6b5d269f2c8c1) - `2026-11-15T19:09:13Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [updates (#7444)](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/6ad34a54190fa1f0266ebb8503e94c18035211d3) - `2026-11-15T19:05:45Z` - Stephen Sumner (@stephen-sumner)

### microsoft/winget-cli (2 commit(s), signal 77)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Uninstall previous handling improvements (#6683)](https://github.com/microsoft/winget-cli/commit/88e3ec32a52a7e61275bbee1921cbab4491d7375) - `2026-11-16T22:35:57Z` - JohnMcPMS (@JohnMcPMS) - PR: [Uninstall previous handling improvements](https://github.com/microsoft/winget-cli/pull/6683)
- [Delta baseline optimizer scripts (#6682)](https://github.com/microsoft/winget-cli/commit/c1d7c23cc2e60f23002bd1edb41bab476d558df3) - `2026-11-16T18:30:15Z` - JohnMcPMS (@JohnMcPMS) - PR: [Delta baseline optimizer scripts](https://github.com/microsoft/winget-cli/pull/6682)

### aspnet/AzureSignalR-samples (2 commit(s), signal 0)

Tags: `bot-only, dependency-noise, samples`

- [Bump fast-xml-parser in /samples/EventGridIntegration/javascript (#384)](https://github.com/aspnet/AzureSignalR-samples/commit/a1c4ccbf3638b8f38ecb7af8203804b6a2819366) - `2026-11-16T22:25:43Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump fast-xml-parser from 5.9.0 to 5.12.0 in /samples/EventGridIntegration/javascript](https://github.com/aspnet/AzureSignalR-samples/pull/384)
- [Bump actions/setup-dotnet (#385)](https://github.com/aspnet/AzureSignalR-samples/commit/9b6918d0b32df1f6277669c05f88d0039e30b7bc) - `2026-11-16T22:24:02Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-dotnet from 6.0.0 to 6.1.0 in the github-actions group](https://github.com/aspnet/AzureSignalR-samples/pull/385)

### microsoft/dragon-copilot-extension-samples (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, samples, watchlist`

- [deps: Bump Microsoft.AspNetCore.Authentication.JwtBearer from 9.0.20 …](https://github.com/microsoft/dragon-copilot-extension-samples/commit/35693ebc6406e347e36e652dd2e59289ef0ab178) - `2026-11-16T22:02:12Z` - dependabot[bot] (@dependabot[bot]) - PR: [deps: Bump Microsoft.AspNetCore.Authentication.JwtBearer from 9.0.20 to 9.0.23](https://github.com/microsoft/dragon-copilot-extension-samples/pull/369)
- [deps(deps-dev): Bump rimraf in /tools/dragon-copilot-cli (#363)](https://github.com/microsoft/dragon-copilot-extension-samples/commit/2e7629aebcab440116e48c474e74e0b825e47821) - `2026-11-16T21:44:34Z` - dependabot[bot] (@dependabot[bot]) - PR: [deps(deps-dev): Bump rimraf from 6.1.3 to 6.1.4 in /tools/dragon-copilot-cli](https://github.com/microsoft/dragon-copilot-extension-samples/pull/363)

### Azure/LogicAppsUX (2 commit(s), signal 117)

Tags: `docs, human-authored, release, watchlist`

- Release: [Release v5.1019.0](https://github.com/Azure/LogicAppsUX/releases/tag/v5.1019.0) - `2026-11-16T21:09:57Z`
- [feat(designer-ui-v2): Otto node parity, shared branch axis fix and St…](https://github.com/Azure/LogicAppsUX/commit/832f686595da5599e897e6c23902dc30be55a639) - `2026-11-16T21:07:44Z` - Krrish Mittal (@takyyon) - PR: [feat(designer-ui-v2): Otto node parity, shared branch axis fix and Standard wiring behind useSharedNodeUi](https://github.com/Azure/LogicAppsUX/pull/9710)
- [fix: refresh connection validation when designer services change (#9705)](https://github.com/Azure/LogicAppsUX/commit/e9010b5ce6458fc7ae954d7ebfef7ccb98cba5a3) - `2026-11-16T15:58:52Z` - Krrish Mittal (@takyyon) - PR: [fix: refresh connection validation when designer services change](https://github.com/Azure/LogicAppsUX/pull/9705)

### microsoft/XBOX-Godot-NetRumble (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Match publisher display name to Partner Center seller (#37)](https://github.com/microsoft/XBOX-Godot-NetRumble/commit/bd506b6041723f2f61a68a86499e3e04c30fceee) - `2026-11-16T20:41:06Z` - James Lenell (@jameslen-atg) - PR: [Match publisher display name to Partner Center seller](https://github.com/microsoft/XBOX-Godot-NetRumble/pull/37)
- [Recover clients when hosted lobby authority departs (#36)](https://github.com/microsoft/XBOX-Godot-NetRumble/commit/feef0d1cceb3945c0a93c2647f300eef61aa1f13) - `2026-11-16T19:11:17Z` - James Lenell (@jameslen-atg) - PR: [Recover clients when hosted lobby authority departs](https://github.com/microsoft/XBOX-Godot-NetRumble/pull/36)

### microsoft/amplifier-module-provider-anthropic (2 commit(s), signal 42)

Tags: `docs, human-authored`

- [Fix explicit adaptive type for automatic thinking binding and token c…](https://github.com/microsoft/amplifier-module-provider-anthropic/commit/fa1adae32eea495b0b9214cd03baa9d63f43517b) - `2026-11-16T20:21:37Z` - Brian Krabach (@bkrabach) - PR: [Fix explicit adaptive type for automatic thinking binding and token counting](https://github.com/microsoft/amplifier-module-provider-anthropic/pull/147)
- [Preserve bounded count validation diagnostics without exporting API t…](https://github.com/microsoft/amplifier-module-provider-anthropic/commit/11ee7dc0a704267f69f12914bd2ad9ff27c24e12) - `2026-11-16T20:14:32Z` - Brian Krabach (@bkrabach) - PR: [Preserve bounded count validation diagnostics without exporting API text](https://github.com/microsoft/amplifier-module-provider-anthropic/pull/146)

### microsoft/ebpf-for-windows-sample-program (2 commit(s), signal 77)

Tags: `human-authored, product:PowerShell, samples, watchlist`

- [Bump the actions group across 1 directory with 3 updates (#11)](https://github.com/microsoft/ebpf-for-windows-sample-program/commit/9bfcd9bdf561dad1eccbb7d1736544d166aede84) - `2026-11-16T20:11:40Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the actions group across 1 directory with 3 updates](https://github.com/microsoft/ebpf-for-windows-sample-program/pull/11)
- [Fix Windows CI toolchain selection (#12)](https://github.com/microsoft/ebpf-for-windows-sample-program/commit/ef011cafdc1d855fbe87b6593443f240bf9de6b9) - `2026-11-16T19:41:26Z` - D. Michael Agun (@mikeagun) - PR: [Fix Windows CI toolchain selection](https://github.com/microsoft/ebpf-for-windows-sample-program/pull/12)

### MicrosoftDocs/office-docs-powershell (2 commit(s), signal 77)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Update 3 files in office-docs-powershell (#13883)](https://github.com/MicrosoftDocs/office-docs-powershell/commit/ca8e0b757ec00a345646bd74e6e0aa4ba132b884) - `2026-11-16T19:27:06Z` - paulkwo-msft2 (@paulkwo-msft2) - PR: [Update office-docs-powershell](https://github.com/MicrosoftDocs/office-docs-powershell/pull/13883)
- [Update office-docs-powershell (#13876)](https://github.com/MicrosoftDocs/office-docs-powershell/commit/386a5d3f8060c828287b330a79b0d3fd297cab40) - `2026-11-16T18:06:17Z` - paulkwo-msft2 (@paulkwo-msft2) - PR: [Update office-docs-powershell](https://github.com/MicrosoftDocs/office-docs-powershell/pull/13876)

### Azure/azure-sdk-for-rust (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [feat(eventhubs): add OpenTelemetry observability (#5600)](https://github.com/Azure/azure-sdk-for-rust/commit/8b3996d7cb3849efb6bba2066a39c85a0f0ba290) - `2026-11-16T18:48:11Z` - Johnathan W (@j7nw4r) - PR: [feat(eventhubs): add OpenTelemetry observability](https://github.com/Azure/azure-sdk-for-rust/pull/5600)
- [Sync eng/common directory with azure-sdk-tools for PR 17536 (#5584)](https://github.com/Azure/azure-sdk-for-rust/commit/6978956bdc191bc1a05e3913323181dd2d9e801a) - `2026-11-16T03:52:31Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17536](https://github.com/Azure/azure-sdk-for-rust/pull/5584)

### microsoft/kiota-dotnet (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [ci: remove obsolete SonarCloud workflow (#870)](https://github.com/microsoft/kiota-dotnet/commit/4cbebb2897ea5debf2c60edc8a41f0858295dd3a) - `2026-11-16T18:46:18Z` - Vincent Biret (@baywet) - PR: [ci: remove obsolete SonarCloud workflow](https://github.com/microsoft/kiota-dotnet/pull/870)
- [Bump the testing-dependencies group with 1 update (#869)](https://github.com/microsoft/kiota-dotnet/commit/9d0e792c161618e8a03b8e11cb449c8132b64943) - `2026-11-16T11:32:50Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the testing-dependencies group with 1 update](https://github.com/microsoft/kiota-dotnet/pull/869)

### microsoft/kiota-abstractions-go (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #326 from microsoft/chore/remove-sonar-20261116-1420](https://github.com/microsoft/kiota-abstractions-go/commit/2607157303468438551660d99b4ac12e3299d762) - `2026-11-16T18:46:09Z` - Vincent Biret (@baywet) - PR: [ci: remove obsolete SonarCloud integration](https://github.com/microsoft/kiota-abstractions-go/pull/326)
- [ci: remove obsolete SonarCloud integration](https://github.com/microsoft/kiota-abstractions-go/commit/0bf9836d752865667e5daa358006d3a2727b45bf) - `2026-11-16T14:19:55Z` - Vincent Biret (@baywet) - PR: [ci: remove obsolete SonarCloud integration](https://github.com/microsoft/kiota-abstractions-go/pull/326)

### microsoft/kiota-authentication-azure-go (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #256 from microsoft/chore/remove-sonar-20261116-a2…](https://github.com/microsoft/kiota-authentication-azure-go/commit/204916181aec7a7f559161d9a48f0e57e6312591) - `2026-11-16T18:45:50Z` - Vincent Biret (@baywet) - PR: [ci: remove SonarCloud integration](https://github.com/microsoft/kiota-authentication-azure-go/pull/256)
- [ci: remove SonarCloud integration](https://github.com/microsoft/kiota-authentication-azure-go/commit/11121bb805e2b776fd18bf2cd142c6995f034a39) - `2026-11-16T14:20:44Z` - Vincent Biret (@baywet) - PR: [ci: remove SonarCloud integration](https://github.com/microsoft/kiota-authentication-azure-go/pull/256)

### Azure-Samples/DevOpsEngineerPersona (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Merge pull request #136 from danfiedler-msft/danfiedler/pin-actions](https://github.com/Azure-Samples/DevOpsEngineerPersona/commit/47ae310a4add853a0757b51d51828bf6d3ae27ba) - `2026-11-16T17:50:33Z` - David Sanchez (@dsanchezcr) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/DevOpsEngineerPersona/pull/136)
- [Merge branch 'main' into danfiedler/pin-actions](https://github.com/Azure-Samples/DevOpsEngineerPersona/commit/2fefc57ce34384820abbfe76f7a09c23682083b5) - `2026-11-16T17:17:34Z` - David Sanchez (@dsanchezcr) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/DevOpsEngineerPersona/pull/136)

### dotnet/dotnet-api-docs (2 commit(s), signal 42)

Tags: `docs, human-authored`

- [docs: clarify named pipe impersonation permissions (#13318)](https://github.com/dotnet/dotnet-api-docs/commit/fde3f8081bfb5c0a0bbce28d37997d07d5928973) - `2026-11-16T17:46:48Z` - Jeff Handley (@jeffhandley) - PR: [Clarify named pipe impersonation permissions](https://github.com/dotnet/dotnet-api-docs/pull/13318)
- [Clarify System.Speech grammar safety guidance (#13317)](https://github.com/dotnet/dotnet-api-docs/commit/946953980404a975120a9b52dc38d61145734039) - `2026-11-15T17:46:31Z` - Jeff Handley (@jeffhandley) - PR: [Clarify System.Speech grammar safety guidance](https://github.com/dotnet/dotnet-api-docs/pull/13317)

### MicrosoftLearning/AZ-802-Windows-Server-Administrator-Associate (2 commit(s), signal 77)

Tags: `human-authored, product:PowerShell, training, watchlist`

- [Merge pull request #26 from Rob-Barefoot/WindowsServer2025-updates](https://github.com/MicrosoftLearning/AZ-802-Windows-Server-Administrator-Associate/commit/723a672367109cf265919d9a67d264766467630a) - `2026-11-16T15:39:37Z` - Rob-Barefoot (@Rob-Barefoot) - PR: [Windows server2025 updates](https://github.com/MicrosoftLearning/AZ-802-Windows-Server-Administrator-Associate/pull/26)
- [Merge branch 'MicrosoftLearning:main' into WindowsServer2025-updates](https://github.com/MicrosoftLearning/AZ-802-Windows-Server-Administrator-Associate/commit/f9b5c0d2d4db9cd32730c27209463a23074a1823) - `2026-11-16T15:26:23Z` - Rob-Barefoot (@Rob-Barefoot) - PR: [Windows server2025 updates](https://github.com/MicrosoftLearning/AZ-802-Windows-Server-Administrator-Associate/pull/26)

### Azure-Samples/foundry-local-model-catalog (2 commit(s), signal 77)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Merge pull request #128 from Azure-Samples/update-catalog-191487664](https://github.com/Azure-Samples/foundry-local-model-catalog/commit/52c5846a84e2a5b434cab2c3879a34fd23b6b0fe) - `2026-11-16T14:46:21Z` - Schtechel (@Schtechel) - PR: [Update MODEL_CATALOG.md (191487664)](https://github.com/Azure-Samples/foundry-local-model-catalog/pull/128)
- [Update MODEL_CATALOG.md (build 191487664)](https://github.com/Azure-Samples/foundry-local-model-catalog/commit/a7801f1c1bfc502621f47f821f19411f9eed426b) - `2026-11-16T14:42:09Z` - ado-pr-bot - PR: [Update MODEL_CATALOG.md (191487664)](https://github.com/Azure-Samples/foundry-local-model-catalog/pull/128)

### OfficeDev/Microsoft-Teams-Samples (2 commit(s), signal 102)

Tags: `human-authored, samples, security, watchlist`

- [Merge pull request #2415 from OfficeDev/v-hrajandira/Enable-npm-secur…](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/d39fbc7bf9df39338986cf20d8a161173d5ff9e1) - `2026-11-16T10:45:45Z` - Harikrishnan-MSFT (@Harikrishnan-MSFT) - PR: [Configure Dependabot security updates for all npm samples](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2415)
- [Configure Dependabot security updates for all npm samples](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/d7683d13d9ff3d9d1d7edce58265d593708637d8) - `2026-11-16T02:05:03Z` - Harikrishnan Rajandiran (Tata Consultancy Services Limi) (@Harikrishnan-MSFT) - PR: [Configure Dependabot security updates for all npm samples](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2415)

### Azure/data-api-builder (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Skip unsupported column data types during schema discovery (#3802)](https://github.com/Azure/data-api-builder/commit/befcc5561a6305f473d086380f3f8277f9bcf1e6) - `2026-11-16T09:16:27Z` - Joymax (@joymaxnascimento) - PR: [Skip unsupported column data types during schema discovery](https://github.com/Azure/data-api-builder/pull/3802)
- [Preserve inner exception when a mutation transaction fails (#3906)](https://github.com/Azure/data-api-builder/commit/5637dd8cc0749a4ce7081f1b37fc6ea9257c565a) - `2026-11-16T05:31:42Z` - amritesh1234 (@amritesh1234) - PR: [Preserve inner exception when a mutation transaction fails](https://github.com/Azure/data-api-builder/pull/3906)

### MicrosoftDocs/azure-docs-sdk-dotnet (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/cbe5db57c50ca56082d47fa51f06f3a23a41d350) - `2026-11-16T05:58:05Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/23967aeddc51e86a99fb11bce45a146922873e39) - `2026-11-16T05:55:27Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/msix-docs (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/msix-pr …](https://github.com/MicrosoftDocs/msix-docs/commit/db012603c0cc2821daa30725810978764dcc8f25) - `2026-11-16T05:02:05Z` - Learn Build Service GitHub App
- [Merge pull request #1109 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/msix-docs/commit/a3b6bfd45a56ea190ff8dd5d484d284b5426b86d) - `2026-11-16T05:01:40Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### Azure/azure-sdk (2 commit(s), signal 87)

Tags: `docs, human-authored, product:Azure SDK, release-language, watchlist`

- [Update release catalog package names (#10411)](https://github.com/Azure/azure-sdk/commit/86e9d88142931350134e913c9f1efcac84a3cb53) - `2026-11-16T04:24:01Z` - Lori Fraleigh (@lfraleigh) - PR: [Update release catalog package names](https://github.com/Azure/azure-sdk/pull/10411)
- [Fix test-proxy installation with blocked inherited NuGet sources (#10…](https://github.com/Azure/azure-sdk/commit/a305984e842be51f03ec641bdabca6ea3cdeee79) - `2026-11-16T03:53:16Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17536](https://github.com/Azure/azure-sdk/pull/10407)

### microsoft/amplifier-module-loop-streaming (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Expose the active registered tool call for host approval scopes (#78)](https://github.com/microsoft/amplifier-module-loop-streaming/commit/fd4d8947a4ae06e183ca3a466d5d31b4ea958a70) - `2026-11-16T22:42:44Z` - Brian Krabach (@bkrabach) - PR: [Expose the active registered tool call for host approval scopes](https://github.com/microsoft/amplifier-module-loop-streaming/pull/78)

### microsoft/vscode-docs-authoring (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Merge pull request #970 from danfiedler-msft/danfiedler/pin-actions](https://github.com/microsoft/vscode-docs-authoring/commit/479bfed093624757a554b141f33051d2fde82b6d) - `2026-11-16T22:11:21Z` - Jamar Warren (@jamarw) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/microsoft/vscode-docs-authoring/pull/970)

### Azure/PSDocs.Azure-quickstart (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Pin GitHub Actions to full-length commit SHAs (#288)](https://github.com/Azure/PSDocs.Azure-quickstart/commit/5eda3a668883abda22ee408a093b31db1fa84ff3) - `2026-11-16T21:03:31Z` - Dan Fiedler (@danfiedler-msft) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure/PSDocs.Azure-quickstart/pull/288)

### dotnet/docs-mobile (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Fix typos and technical errors `user-notifications.md` article (#157)](https://github.com/dotnet/docs-mobile/commit/c428272ea65e5171b103ebd1090d1c8301430e19) - `2026-11-16T20:48:31Z` - Nick (@Danghor) - PR: [Fix typos and technical errors `user-notifications.md` article](https://github.com/dotnet/docs-mobile/pull/157)

### Azure-Samples/cognitive-services-speech-sdk (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, product:Azure SDK, samples, watchlist`

- [Bump actions/setup-dotnet (#3108)](https://github.com/Azure-Samples/cognitive-services-speech-sdk/commit/6d33cffe9eb0c469bb01e32cb14e6e6fb43ab7b0) - `2026-11-16T20:04:52Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-dotnet from 6.0.0 to 6.1.0 in the github-actions group](https://github.com/Azure-Samples/cognitive-services-speech-sdk/pull/3108)

### Azure/azureml-examples (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [docs: refresh ai-platform-docs CODEOWNERS entries (#4154)](https://github.com/Azure/azureml-examples/commit/689609b9bcde82958d0d533dc68e5ca1050479a3) - `2026-11-16T19:50:53Z` - Sheri Gilley (@sdgilley) - PR: [Update ai-platform-docs CODEOWNERS entries](https://github.com/Azure/azureml-examples/pull/4154)

### microsoft/AziHSM-Guest (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [update README file](https://github.com/microsoft/AziHSM-Guest/commit/66acd0b362d04337d8793a63fbae1b1494b56852) - `2026-11-16T19:23:58Z` - Dmitry Makarov (@DmitryMA) - PR: [update README file](https://github.com/microsoft/AziHSM-Guest/pull/31)

### dotnet/docs-tools (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Add README.md for Snippets5000 tool (#817)](https://github.com/dotnet/docs-tools/commit/76e4548c1fd9586fd125bed25f172a0a38884360) - `2026-11-16T19:09:27Z` - Genevieve Warren (@gewarren) - PR: [Add README.md for Snippets5000 tool](https://github.com/dotnet/docs-tools/pull/817)

### microsoft/WindowsAppSDK (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Fix Windows SDK package feature naming conflict and DevCheck VS 2026 …](https://github.com/microsoft/WindowsAppSDK/commit/ecb1c60964f7b860031ae0a07e235f9078d3104b) - `2026-11-16T19:04:57Z` - Scott Jones (@Scottj1s) - PR: [Fix Windows SDK package feature naming conflict and DevCheck VS 2026 support](https://github.com/microsoft/WindowsAppSDK/pull/6951)

### Azure/AKS-DevSecOps-Workshop (1 commit(s), signal 76)

Tags: `human-authored, training, watchlist`

- [Merge pull request #120 from danfiedler-msft/danfiedler/pin-actions](https://github.com/Azure/AKS-DevSecOps-Workshop/commit/a45707012dc85199678a06427aab0f21609b1a5c) - `2026-11-16T19:04:57Z` - Ahmed Bham (@ahmedbham) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure/AKS-DevSecOps-Workshop/pull/120)

### Azure/homebrew-azd (1 commit(s), signal 86)

Tags: `human-authored, product:Azure SDK, release-language, samples, watchlist`

- [Update for azd release 1.38.0](https://github.com/Azure/homebrew-azd/commit/3a30cbe336372a4ed420dbe5c7b911df869526e7) - `2026-11-16T19:01:39Z` - azure-sdk (@azure-sdk)

### Azure-Samples/Spec2Cloud (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Pin GitHub Actions to full-length commit SHAs (#15)](https://github.com/Azure-Samples/Spec2Cloud/commit/b9914f797d1394723df67ef261d0c2703ab62982) - `2026-11-16T18:48:00Z` - Dan Fiedler (@danfiedler-msft) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/Spec2Cloud/pull/15)

### Azure-Samples/ms-events-session-guide (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add source code link to shared footer (#11)](https://github.com/Azure-Samples/ms-events-session-guide/commit/72553e828419439c318a80696c3bc06c05ffe8d6) - `2026-11-16T18:28:31Z` - Artem Lovan (@artlovan) - PR: [Add GitHub source code link to the footer](https://github.com/Azure-Samples/ms-events-session-guide/pull/11)

### Azure-Samples/ai-language-samples (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Merge pull request #7 from danfiedler-msft/danfiedler/pin-actions](https://github.com/Azure-Samples/ai-language-samples/commit/d205ef154691f4a642511e3a451838c6df89d198) - `2026-11-16T18:18:19Z` - Ahmed Ashour (@ahmedaashour) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/ai-language-samples/pull/7)

### Azure-Samples/azure-ai-learning-paths (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Pin GitHub Actions to full-length commit SHAs (#1)](https://github.com/Azure-Samples/azure-ai-learning-paths/commit/837cbeca9332a7402c7fc1bcf00b8096082b03e7) - `2026-11-16T17:59:21Z` - saitejapudi (@saiteja-pudi) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/azure-ai-learning-paths/pull/1)

### dotnet/android-api-docs (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Document intended PackageManager activity-options query (#1517)](https://github.com/dotnet/android-api-docs/commit/ef3794ca41cf592ed7bae51127ceb926809df05f) - `2026-11-16T17:50:25Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Document intended PackageManager activity-options query](https://github.com/dotnet/android-api-docs/pull/1517)

### MicrosoftLearning/mslearn-ai-multi-agents (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, training, watchlist`

- [Add debug prints for agent response output](https://github.com/MicrosoftLearning/mslearn-ai-multi-agents/commit/b868846f405c9d852814f0703fd56f5331d2461c) - `2026-11-16T17:27:25Z` - Peter De Tender (@petender)

### Azure-Samples/cosmos-db-design-patterns (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Merge pull request #104 from danfiedler-msft/danfiedler/pin-actions](https://github.com/Azure-Samples/cosmos-db-design-patterns/commit/8e264a1f2ddaeb7cbbe9853928f37862a74f2ecd) - `2026-11-16T17:27:01Z` - Mark Brown (@markjbrown) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/cosmos-db-design-patterns/pull/104)

### Azure-Samples/dapr-store (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Pin GitHub Actions to full-length commit SHAs (#36)](https://github.com/Azure-Samples/dapr-store/commit/ad0081409856e3f5076557adb3973973060e64b8) - `2026-11-16T17:24:38Z` - Dan Fiedler (@danfiedler-msft) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/dapr-store/pull/36)

### Azure-Samples/snippy (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Pin GitHub Actions to full-length commit SHAs (#83)](https://github.com/Azure-Samples/snippy/commit/b54cdaa439f83f03cd177cd4531c0b55ab5aa036) - `2026-11-16T17:20:05Z` - Dan Fiedler (@danfiedler-msft) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/snippy/pull/83)

### Azure/azure-kusto-samples-dotnet (1 commit(s), signal 76)

Tags: `human-authored, samples, watchlist`

- [Merge pull request #32 from danfiedler-msft/danfiedler/pin-actions](https://github.com/Azure/azure-kusto-samples-dotnet/commit/ef21761b760f80fe258cf803b37c6f9d4963bb8c) - `2026-11-16T17:03:50Z` - Ziv Caspi (@zivcaspi) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure/azure-kusto-samples-dotnet/pull/32)

### microsoft/kiota-typescript (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [fix(abstractions): parse TimeOnly fractional seconds as decimal fract…](https://github.com/microsoft/kiota-typescript/commit/153c0144fe902e874fe8180d61f590ad33f9f847) - `2026-11-16T15:55:48Z` - Hardik K (@hardikkaurani) - PR: [fix(abstractions): parse TimeOnly fractional seconds as decimal fraction](https://github.com/microsoft/kiota-typescript/pull/2232)

### dotnet/msbuild (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Cache oversized string references in the binary logger (#15524)](https://github.com/dotnet/msbuild/commit/65b0e0adafe9213b3cb63d438c3ded2322dcb608) - `2026-11-16T15:35:28Z` - Aleš Prokop (@AlesProkop) - PR: [Cache oversized string references in the binary logger](https://github.com/dotnet/msbuild/pull/15524)

### MicrosoftDocs/edge-developer (1 commit(s), signal 86)

Tags: `docs, human-authored, release-language, watchlist`

- [Update Playwright to version 1.65.1 and change workflow to use Ubuntu…](https://github.com/MicrosoftDocs/edge-developer/commit/7172e3c95cce3230c4e3d52ee188abba5159deab) - `2026-11-16T14:32:15Z` - Patrick Brosset (@captainbrosset) - PR: [Update Playwright to version 1.65.1 and change workflow to use Ubuntu 24.04](https://github.com/MicrosoftDocs/edge-developer/pull/4016)

### MicrosoftLearning/mslearn-fabric (1 commit(s), signal 76)

Tags: `human-authored, training, watchlist`

- [Update activator instructions and added note on lab02 (#477)](https://github.com/MicrosoftLearning/mslearn-fabric/commit/8f6ec9ffb16b863f2083e34fe30e3a4ef36e078c) - `2026-11-16T13:55:38Z` - v-vfarias (@v-vfarias) - PR: [Update activator instructions and added note on lab02](https://github.com/MicrosoftLearning/mslearn-fabric/pull/477)

### Azure-Samples/Cognitive-Speech-TTS (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add Ignite 2026 TTS audio samples (#468)](https://github.com/Azure-Samples/Cognitive-Speech-TTS/commit/2072d4cd86f8b3af6675a524d2051e85b5565c15) - `2026-11-16T13:24:51Z` - msftbding (@msftbding) - PR: [Add Ignite 2026 TTS audio samples](https://github.com/Azure-Samples/Cognitive-Speech-TTS/pull/468)

### Azure-Samples/azure-files-samples (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add Azure Files change feed incremental copy sample (#327)](https://github.com/Azure-Samples/azure-files-samples/commit/deec7558651291fcd47d744e5dbe537de1546bcf) - `2026-11-16T12:43:07Z` - Athreyasubash (@Athreyasubash) - PR: [Add Azure Files change feed incremental copy sample](https://github.com/Azure-Samples/azure-files-samples/pull/327)

### MicrosoftDocs/webview2-winrt-reference (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [WebView2: Update documentation for 159.0.4392.0 (#148)](https://github.com/MicrosoftDocs/webview2-winrt-reference/commit/79e35f64dafa488a76817b2c7c6ec44429e0de5f) - `2026-11-16T11:24:04Z` - GarimaSoni142-coder (@GarimaSoni142-coder) - PR: [WebView2: Update documentation for 159.0.4392.0](https://github.com/MicrosoftDocs/webview2-winrt-reference/pull/148)

### MicrosoftDocs/webview2-win32-reference (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [WebView2: Update documentation for 159.0.4392.0 (#169)](https://github.com/MicrosoftDocs/webview2-win32-reference/commit/caf879071a4e9ddd7c0e8f6e5bca38074607022c) - `2026-11-16T11:23:52Z` - GarimaSoni142-coder (@GarimaSoni142-coder) - PR: [WebView2: Update documentation for 159.0.4392.0](https://github.com/MicrosoftDocs/webview2-win32-reference/pull/169)

### microsoft/power-pages-samples (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add community Power Pages template skill (#226)](https://github.com/microsoft/power-pages-samples/commit/0db2f1b572af8beb13d22648578f3729cb91fe66) - `2026-11-16T05:55:03Z` - Priyanshu Agrawal (@priyanshu92) - PR: [Add skill to add new template](https://github.com/microsoft/power-pages-samples/pull/226)

### Azure/azure-sdk-for-cpp (1 commit(s), signal 26)

Tags: `bot-only, docs, product:Azure SDK, watchlist`

- [Fix test-proxy installation with blocked inherited NuGet sources (#7541)](https://github.com/Azure/azure-sdk-for-cpp/commit/fb07dcd79bbec049181fc7081008e6d15ee539ff) - `2026-11-16T03:53:43Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17536](https://github.com/Azure/azure-sdk-for-cpp/pull/7541)

### dotnet/docfx (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [chore: Drop net8.0/net9.0 TFMs support (#11213)](https://github.com/dotnet/docfx/commit/2c8f1f308dfc72195e01593d98ff0fa263b8fb88) - `2026-11-16T03:17:12Z` - filzrev (@filzrev) - PR: [chore: Drop net8.0/net9.0 TFMs support](https://github.com/dotnet/docfx/pull/11213)

### Azure-Samples/azuresandbox (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Accept deployment helper scripts in old or new location (#1053) (#1067)](https://github.com/Azure-Samples/azuresandbox/commit/d85935cdaad295b0c2eada40bdc4e1bcb0d2bddc) - `2026-11-16T03:10:02Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Maintenance: accept deployment helper scripts in old or new location (#1053)](https://github.com/Azure-Samples/azuresandbox/pull/1067)

### microsoft/mcp-dotnet-samples (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Update metadata.json](https://github.com/microsoft/mcp-dotnet-samples/commit/844214b44cf09d90e8d38b4fe7fe13d3e6045719) - `2026-11-16T01:11:58Z` - GitHub Actions (@actions-user)

### Azure/AI-Landing-Zones (1 commit(s), signal 26)

Tags: `bot-only, docs, watchlist`

- [docs: refresh validated planner prices](https://github.com/Azure/AI-Landing-Zones/commit/eea8b5b571cc630eda944d7ab5669f9bb931c20c) - `2026-11-16T00:40:35Z` - github-actions[bot] (@github-actions[bot])

### microsoft/amplifier-persona-workshop (1 commit(s), signal 41)

Tags: `human-authored, training`

- [docs: map ecosystem roles and component relationships (#23)](https://github.com/microsoft/amplifier-persona-workshop/commit/952cf8f26fb3bfd99b52e0e2b16b368e9507d962) - `2026-11-15T18:08:10Z` - Brian Krabach (@bkrabach) - PR: [docs: show ecosystem roles and component maps](https://github.com/microsoft/amplifier-persona-workshop/pull/23)

### microsoft/amplifier-acp-lab (1 commit(s), signal 41)

Tags: `human-authored, training`

- [docs: map ecosystem roles and component relationships (#14)](https://github.com/microsoft/amplifier-acp-lab/commit/3c03c484ae69cc634ef215d85b9226b95056ff9f) - `2026-11-15T17:53:08Z` - Brian Krabach (@bkrabach) - PR: [docs: show ecosystem roles and component maps](https://github.com/microsoft/amplifier-acp-lab/pull/14)

</details>
