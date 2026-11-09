# Microsoft Ecosystem Daily Brief - 2026-11-09

> Status: Fresh at generation. Current freshness is tracked in `reports/status.json`.
> Generated: 2026-11-09 23:02 UTC - Window: 30.6h from 2026-11-08 16:24 UTC to 2026-11-09 23:02 UTC.
> 115 repo(s) moved - 587 commit(s) - 30 release item(s) - 25 high-signal repo(s).

## Plain-English Summary

- Azure, Microsoft Graph led the visible product-area activity in this window.
- 30 release item(s) were detected during the window.
- Security-related changes appeared in microsoft/forge-lab, microsoft/MCAPSTechConnect26-LAB483, Azure/data-api-builder.
- Start with human-authored changes in microsoft/forge-lab, microsoft/MCAPSTechConnect26-LAB483, Azure/data-api-builder, Azure/logicapps.
- 134 event(s) look automated, bot-heavy, dependency, or generated; review the curated sections before raw volume.

## Headline Metrics

| Metric | Value |
| --- | ---: |
| Inventory repositories | 16762 |
| Repositories after filters | 2563 |
| `pushed_at` candidates | 178 |
| Enrichment candidates | 178 |
| Repositories with movement | 115 |
| Default-branch commits | 587 |

## What Changed That Matters

| Repository | Score | Change | Actor | Noise | Headline | Time |
| --- | ---: | --- | --- | --- | --- | --- |
| [microsoft/forge-lab](https://github.com/microsoft/forge-lab) | 100 | security_fix | human | low | [Sync Rust article wording with the published Security Blog](https://github.com/microsoft/forge-lab/commit/4438373672e014bead76885633c4e5e8470a1e51) | `2026-11-09T20:38:58Z` |
| [microsoft/MCAPSTechConnect26-LAB483](https://github.com/microsoft/MCAPSTechConnect26-LAB483) | 100 | security_fix | human | low | [Revise security pop-up instructions in build guide](https://github.com/microsoft/MCAPSTechConnect26-LAB483/commit/3e006776e35773d669d87862f1931637c8b11ffe) | `2026-11-09T16:24:48Z` |
| [Azure/data-api-builder](https://github.com/Azure/data-api-builder) | 100 | security_fix | human | low | [Enable secretless OBO authentication in DAB using Workload Identity Federation](https://github.com/Azure/data-api-builder/pull/3880) | `2026-11-09T13:40:40Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 100 | release | unknown | low | [azure-iot-ops 2.11.2](https://github.com/Azure/azure-cli-extensions/releases/tag/azure-iot-ops-2.11.2) | `2026-11-09T22:44:40Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 100 | release | unknown | low | [azure-iot 1.1.0b1](https://github.com/Azure/azure-cli-extensions/releases/tag/azure-iot-1.1.0b1) | `2026-11-09T22:42:33Z` |
| [Azure/logicapps](https://github.com/Azure/logicapps) | 100 | release | human | low | [Update release notes](https://github.com/Azure/logicapps/pull/1578) | `2026-11-09T22:37:06Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 100 | release | human | low | [[Attestation] Prepare 1.0.2 release](https://github.com/Azure/azure-sdk-for-js/pull/40722) | `2026-11-09T22:13:08Z` |
| [Azure/homebrew-azd](https://github.com/Azure/homebrew-azd) | 100 | release | human | low | [Update for azd release 1.38.0-beta.1-daily.7054853](https://github.com/Azure/homebrew-azd/commit/00e99a45985ed5c7071fff4d27cab55a90de41f1) | `2026-11-09T21:59:24Z` |
| [OfficeDev/microsoft-teams-library-js](https://github.com/OfficeDev/microsoft-teams-library-js) | 100 | release | human | low | [Fix release pipelines failing at 'View Published Package URLs' (stale artifact path)](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3187) | `2026-11-09T21:46:28Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 100 | release | human | low | [Prepare Azure Monitor exporter 1.11.0-beta.1 release](https://github.com/Azure/azure-sdk-for-net/pull/64695) | `2026-11-09T21:17:19Z` |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 100 | release | unknown | low | [azure_storage_blob@1.2.0-beta.1](https://github.com/Azure/azure-sdk-for-rust/releases/tag/azure_storage_blob%401.2.0-beta.1) | `2026-11-09T21:03:51Z` |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 100 | release | unknown | low | [azure_storage_sas@1.1.0-beta.1](https://github.com/Azure/azure-sdk-for-rust/releases/tag/azure_storage_sas%401.1.0-beta.1) | `2026-11-09T21:03:41Z` |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 100 | release | unknown | low | [AzureSandbox v6.0.7](https://github.com/Azure-Samples/azuresandbox/releases/tag/v6.0.7) | `2026-11-09T20:44:44Z` |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 100 | release | human | low | [Release: vnext to main (azurerm 5.13)](https://github.com/Azure-Samples/azuresandbox/pull/1020) | `2026-11-09T20:43:38Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 100 | release | unknown | low | [com.azure+azure-data-appconfiguration_1.12.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-data-appconfiguration_1.12.0) | `2026-11-09T20:09:59Z` |

## Product Areas

| Product area | Signal | Repos | Events | Releases | Security | Top links |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Azure | 109 | 49 | 138 | 16 | 1 | [Enable secretless OBO authentication in DAB using Workload Identity Federation](https://github.com/Azure/data-api-builder/pull/3880); [azure-iot-ops 2.11.2](https://github.com/Azure/azure-cli-extensions/releases/tag/azure-iot-ops-2.11.2); [azure-iot 1.1.0b1](https://github.com/Azure/azure-cli-extensions/releases/tag/azure-iot-1.1.0b1) |
| Unmapped Activity | 59 | 25 | 78 | 4 | 1 | [Sync Rust article wording with the published Security Blog](https://github.com/microsoft/forge-lab/commit/4438373672e014bead76885633c4e5e8470a1e51); [release rust-std-memory-safety](https://github.com/microsoft/forge-lab/commit/55b9a3953caf8731d2e1cdda33c31f0487e139ee); [WMA 4.2.3.0 and 4.3.0.0 release schedule and 4.2.3.0 release notes (#…](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/1e863d64e5e846c9a0bab1ee47f278078c937fd5) |
| Microsoft Graph | 55 | 18 | 76 | 10 | 0 | [microsoft_kiota_serialization_multipart: v0.0.5](https://github.com/microsoft/kiota-dart/releases/tag/microsoft_kiota_serialization_multipart-v0.0.5); [microsoft_kiota_serialization_json: v0.0.11](https://github.com/microsoft/kiota-dart/releases/tag/microsoft_kiota_serialization_json-v0.0.11); [microsoft_kiota_serialization_form: v0.0.7](https://github.com/microsoft/kiota-dart/releases/tag/microsoft_kiota_serialization_form-v0.0.7) |
| .NET | 14 | 9 | 31 | 0 | 0 | [Fix nullable annotation warning from nameof emission for a generic component parameter](https://github.com/dotnet/roslyn/pull/86311); [Allow Razor utilities package on non-Windows](https://github.com/dotnet/roslyn/pull/86349); [Remove plan-first requirement from agent instructions](https://github.com/dotnet/roslyn/pull/86353) |
| Identity | 13 | 3 | 13 | 0 | 0 | [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/7a8f426815c5929226ba385fb5524a741fee23f4); [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/6eb04b2fe92a7e9b7d3b94615b2dcc80a2c6bb09); [Merging changes synced from https://github.com/MicrosoftDocs/entra-do…](https://github.com/MicrosoftDocs/entra-docs/commit/523f3dd86df8938363d761064d4465c56977c43e) |
| PowerShell | 12 | 5 | 12 | 0 | 0 | [Add multilingual self service agent reference architecture (#12163)](https://github.com/MicrosoftDocs/power-platform/commit/7fc78075f0015bc13df070b962566af9e7e4ee2f); [Fix Cosmos provisioning, initialization retries, and health checks](https://github.com/MicrosoftLearning/mslearn-devops/pull/51); [fix(demo): Keep 3 months on the demo version being built](https://github.com/microsoft/finops-toolkit/pull/2408) |
| Microsoft 365 | 8 | 4 | 8 | 0 | 1 | [Revise security pop-up instructions in build guide](https://github.com/microsoft/MCAPSTechConnect26-LAB483/commit/3e006776e35773d669d87862f1931637c8b11ffe); [Fix release pipelines failing at 'View Published Package URLs' (stale artifact path)](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3187); [Add read-only release checks to the release-teamsjs skill](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3200) |
| Developer Tools | 8 | 2 | 8 | 0 | 0 | [Update Insiders release notes](https://github.com/microsoft/vscode-docs/pull/10615); [docs(setup): document PATH verification and unrecognized command troubleshooting on Windows](https://github.com/microsoft/vscode-docs/pull/10614); [Correct terminal confirmOnExit description](https://github.com/microsoft/vscode-docs/pull/10611) |

## Today's Top Links

| Priority | Repository | Why read it |
| ---: | --- | --- |
| 1 | [microsoft/forge-lab](https://github.com/microsoft/forge-lab) | [Security-related change: Sync Rust article wording with the published Security Blog](https://github.com/microsoft/forge-lab/commit/4438373672e014bead76885633c4e5e8470a1e51) |
| 2 | [microsoft/MCAPSTechConnect26-LAB483](https://github.com/microsoft/MCAPSTechConnect26-LAB483) | [Security-related change: Revise security pop-up instructions in build guide](https://github.com/microsoft/MCAPSTechConnect26-LAB483/commit/3e006776e35773d669d87862f1931637c8b11ffe) |
| 3 | [Azure/data-api-builder](https://github.com/Azure/data-api-builder) | [Security-related change: Enable secretless OBO authentication in DAB using Workload Identity Federation](https://github.com/Azure/data-api-builder/pull/3880) |
| 4 | [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [Release activity: azure-iot-ops 2.11.2](https://github.com/Azure/azure-cli-extensions/releases/tag/azure-iot-ops-2.11.2) |
| 5 | [Azure/logicapps](https://github.com/Azure/logicapps) | [Release activity: Update release notes](https://github.com/Azure/logicapps/pull/1578) |
| 6 | [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [Release activity: [Attestation] Prepare 1.0.2 release](https://github.com/Azure/azure-sdk-for-js/pull/40722) |
| 7 | [Azure/homebrew-azd](https://github.com/Azure/homebrew-azd) | [Release activity: Update for azd release 1.38.0-beta.1-daily.7054853](https://github.com/Azure/homebrew-azd/commit/00e99a45985ed5c7071fff4d27cab55a90de41f1) |
| 8 | [OfficeDev/microsoft-teams-library-js](https://github.com/OfficeDev/microsoft-teams-library-js) | [Release activity: Fix release pipelines failing at 'View Published Package URLs' (stale artifact path)](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3187) |

## Noise and Automation

- 134 event(s) look automated, bot-heavy, dependency, generated, or medium/high noise.
- Top noisy repositories: microsoft/kiota-abstractions-go, microsoft/kiota-python, microsoft/kiota, dotnet/docs, microsoft/kiota-samples.
- Noise mix: Docs: 43, Dependency: 38, SDK: 38, CI/Infra: 8, Release: 4, Sample: 2, Training: 1.

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
| Repos counted | 178 |
| Repos enriched | 115 |

</details>

<details>
<summary>Show supporting signal, release, and lifecycle tables</summary>

## High-Signal Items

| Repository | Score | Tags |
| --- | ---: | --- |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 140 | human-authored, release, release-language, samples, watchlist |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 137 | docs, human-authored, product:Azure AI, product:Azure SDK, release, release-language, watchlist |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 135 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [microsoft/kiota-ruby](https://github.com/microsoft/kiota-ruby) | 133 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [microsoft/kiota-dart](https://github.com/microsoft/kiota-dart) | 132 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 132 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [microsoft/kiota-serialization-form-go](https://github.com/microsoft/kiota-serialization-form-go) | 131 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 130 | docs, human-authored, release, release-language, watchlist |
| [microsoft/kiota-http-go](https://github.com/microsoft/kiota-http-go) | 129 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 128 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [microsoftgraph/msgraph-sdk-java](https://github.com/microsoftgraph/msgraph-sdk-java) | 126 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [microsoftgraph/msgraph-sdk-go](https://github.com/microsoftgraph/msgraph-sdk-go) | 126 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 121 | docs, human-authored, product:Azure SDK, release, watchlist |
| [Azure/sap-automation](https://github.com/Azure/sap-automation) | 117 | docs, human-authored, release, watchlist |
| [microsoft/forge-lab](https://github.com/microsoft/forge-lab) | 113 | human-authored, release-language, security, training, watchlist |

## Watchlist Hits

| Repository | Score | Matches |
| --- | ---: | --- |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 140 | keywords: release |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 137 | products: Azure AI, Azure SDK; repos: Azure/azure-sdk-for-java; orgs: Azure; keywords: agent, sdk |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 135 | products: Azure SDK; repos: Azure/azure-sdk-for-net; orgs: Azure; keywords: release, sdk |
| [microsoft/kiota-ruby](https://github.com/microsoft/kiota-ruby) | 133 | products: Microsoft Graph, Azure SDK; keywords: copilot, graph, kiota, release, sdk |
| [microsoft/kiota-dart](https://github.com/microsoft/kiota-dart) | 132 | products: Microsoft Graph, Azure SDK; keywords: copilot, graph, kiota, release, sdk |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 132 | products: Azure SDK; repos: Azure/azure-sdk-for-js; orgs: Azure; keywords: release, sdk |
| [microsoft/kiota-serialization-form-go](https://github.com/microsoft/kiota-serialization-form-go) | 131 | products: Microsoft Graph, Azure SDK; keywords: graph, kiota, release, sdk |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 130 | orgs: Azure; keywords: migration |
| [microsoft/kiota-http-go](https://github.com/microsoft/kiota-http-go) | 129 | products: Microsoft Graph, Azure SDK; keywords: graph, kiota, release, sdk |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 128 | products: Azure SDK; orgs: Azure; keywords: release, sdk |
| [microsoftgraph/msgraph-sdk-java](https://github.com/microsoftgraph/msgraph-sdk-java) | 126 | products: Microsoft Graph, Azure SDK; repos: microsoftgraph/msgraph-sdk-java; orgs: microsoftgraph; keywords: graph, msgraph, release, sdk |
| [microsoftgraph/msgraph-sdk-go](https://github.com/microsoftgraph/msgraph-sdk-go) | 126 | products: Microsoft Graph, Azure SDK; orgs: microsoftgraph; keywords: graph, msgraph, release, sdk |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 121 | products: Azure SDK; repos: Azure/azure-sdk-for-python; orgs: Azure; keywords: sdk |
| [Azure/sap-automation](https://github.com/Azure/sap-automation) | 117 | orgs: Azure |
| [microsoft/forge-lab](https://github.com/microsoft/forge-lab) | 113 | keywords: release, security |

## Releases

| Repository | Release | Published |
| --- | --- | --- |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [azure-iot-ops 2.11.2](https://github.com/Azure/azure-cli-extensions/releases/tag/azure-iot-ops-2.11.2) | `2026-11-09T22:44:40Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [azure-iot 1.1.0b1](https://github.com/Azure/azure-cli-extensions/releases/tag/azure-iot-1.1.0b1) | `2026-11-09T22:42:33Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [azure-iot 1.0.0](https://github.com/Azure/azure-cli-extensions/releases/tag/azure-iot-1.0.0) | `2026-11-09T22:42:30Z` |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | [azure_storage_blob@1.2.0-beta.1](https://github.com/Azure/azure-sdk-for-rust/releases/tag/azure_storage_blob%401.2.0-beta.1) | `2026-11-09T21:03:51Z` |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | [azure_storage_sas@1.1.0-beta.1](https://github.com/Azure/azure-sdk-for-rust/releases/tag/azure_storage_sas%401.1.0-beta.1) | `2026-11-09T21:03:41Z` |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | [azure_storage_common@1.1.0-beta.1](https://github.com/Azure/azure-sdk-for-rust/releases/tag/azure_storage_common%401.1.0-beta.1) | `2026-11-09T21:03:32Z` |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | [AzureSandbox v6.0.7](https://github.com/Azure-Samples/azuresandbox/releases/tag/v6.0.7) | `2026-11-09T20:44:44Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure+azure-data-appconfiguration_1.12.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-data-appconfiguration_1.12.0) | `2026-11-09T20:09:59Z` |
| [microsoft/kiota-dart](https://github.com/microsoft/kiota-dart) | [microsoft_kiota_serialization_multipart: v0.0.5](https://github.com/microsoft/kiota-dart/releases/tag/microsoft_kiota_serialization_multipart-v0.0.5) | `2026-11-09T19:59:36Z` |
| [microsoft/kiota-dart](https://github.com/microsoft/kiota-dart) | [microsoft_kiota_serialization_json: v0.0.11](https://github.com/microsoft/kiota-dart/releases/tag/microsoft_kiota_serialization_json-v0.0.11) | `2026-11-09T19:59:34Z` |
| [microsoft/kiota-dart](https://github.com/microsoft/kiota-dart) | [microsoft_kiota_serialization_form: v0.0.7](https://github.com/microsoft/kiota-dart/releases/tag/microsoft_kiota_serialization_form-v0.0.7) | `2026-11-09T19:59:33Z` |
| [microsoft/kiota-dart](https://github.com/microsoft/kiota-dart) | [microsoft_kiota_http: v0.0.8](https://github.com/microsoft/kiota-dart/releases/tag/microsoft_kiota_http-v0.0.8) | `2026-11-09T19:59:31Z` |
| [microsoft/kiota-dart](https://github.com/microsoft/kiota-dart) | [microsoft_kiota_abstractions: v0.3.3](https://github.com/microsoft/kiota-dart/releases/tag/microsoft_kiota_abstractions-v0.3.3) | `2026-11-09T19:59:30Z` |
| [microsoft/kiota-serialization-form-go](https://github.com/microsoft/kiota-serialization-form-go) | [v1.1.7](https://github.com/microsoft/kiota-serialization-form-go/releases/tag/v1.1.7) | `2026-11-09T19:59:22Z` |
| [microsoft/kiota-http-go](https://github.com/microsoft/kiota-http-go) | [v1.6.1](https://github.com/microsoft/kiota-http-go/releases/tag/v1.6.1) | `2026-11-09T19:58:37Z` |
| [microsoft/kiota-ruby](https://github.com/microsoft/kiota-ruby) | [v0.25.3](https://github.com/microsoft/kiota-ruby/releases/tag/v0.25.3) | `2026-11-09T18:53:20Z` |
| [microsoft/fabriciq-thirdparty-plugins](https://github.com/microsoft/fabriciq-thirdparty-plugins) | [v0.1.0-rc3 (ChatGPT package)](https://github.com/microsoft/fabriciq-thirdparty-plugins/releases/tag/v0.1.0-rc3) | `2026-11-09T18:38:01Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-mgmt-chaos_3.0.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-chaos_3.0.0) | `2026-11-09T18:29:51Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure.resourcemanager+azure-resourcemanager-chaos_1.4.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-chaos_1.4.0) | `2026-11-09T18:04:48Z` |
| [Azure/azure-sdk-for-cpp](https://github.com/Azure/azure-sdk-for-cpp) | [azure-messaging-eventhubs-checkpointstore-blob_1.0.0-beta.5](https://github.com/Azure/azure-sdk-for-cpp/releases/tag/azure-messaging-eventhubs-checkpointstore-blob_1.0.0-beta.5) | `2026-11-09T17:52:16Z` |
| [Azure/azure-sdk-for-cpp](https://github.com/Azure/azure-sdk-for-cpp) | [azure-messaging-eventhubs_1.0.0-beta.16](https://github.com/Azure/azure-sdk-for-cpp/releases/tag/azure-messaging-eventhubs_1.0.0-beta.16) | `2026-11-09T17:50:54Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-sovereign_1.0.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-sovereign_1.0.0-beta.1) | `2026-11-09T17:46:42Z` |
| [microsoftgraph/msgraph-sdk-java](https://github.com/microsoftgraph/msgraph-sdk-java) | [v6.73.0](https://github.com/microsoftgraph/msgraph-sdk-java/releases/tag/v6.73.0) | `2026-11-09T15:47:16Z` |
| [microsoftgraph/msgraph-sdk-go](https://github.com/microsoftgraph/msgraph-sdk-go) | [v1.106.0](https://github.com/microsoftgraph/msgraph-sdk-go/releases/tag/v1.106.0) | `2026-11-09T15:46:38Z` |
| [Azure/azure-sdk-for-cpp](https://github.com/Azure/azure-sdk-for-cpp) | [azure-core-amqp_1.0.0-beta.14](https://github.com/Azure/azure-sdk-for-cpp/releases/tag/azure-core-amqp_1.0.0-beta.14) | `2026-11-09T15:31:40Z` |

## Repository Lifecycle

| Change | Count |
| --- | ---: |
| archived_changed | 7 |
| category_changed | 0 |
| default_branch_changed | 0 |
| fork_changed | 0 |
| new_repos | 3 |
| removed_repos | 0 |

## Recently Created Repositories

| Repository | Category | Created |
| --- | --- | --- |
| [Azure-Samples/flex-container-html2pdf-go](https://github.com/Azure-Samples/flex-container-html2pdf-go) | samples | `2026-11-09T07:22:37Z` |

## Category Summary

| Category | Repositories |
| --- | ---: |
| docs | 75 |
| samples | 35 |
| training | 5 |

## Organization Summary

| Org | Repositories |
| --- | ---: |
| microsoft | 36 |
| MicrosoftDocs | 30 |
| Azure | 20 |
| Azure-Samples | 13 |
| dotnet | 8 |
| microsoftgraph | 4 |
| MicrosoftLearning | 2 |
| OfficeDev | 1 |
| aspnet | 1 |

</details>

<details>
<summary>Show raw repository activity</summary>

## Busiest Repositories

| Repository | Signal | Category | Commits | Releases | Newest commit |
| --- | ---: | --- | ---: | ---: | --- |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 140 | samples | 15 | 1 | `2026-11-09T20:43:38Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 137 | docs | 12 | 2 | `2026-11-09T22:09:01Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 135 | docs | 10 | 2 | `2026-11-09T21:40:40Z` |
| [microsoft/kiota-ruby](https://github.com/microsoft/kiota-ruby) | 133 | docs | 8 | 1 | `2026-11-09T18:50:21Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 132 | docs | 7 | 3 | `2026-11-09T22:13:08Z` |
| [microsoft/kiota-dart](https://github.com/microsoft/kiota-dart) | 132 | docs | 7 | 5 | `2026-11-09T20:22:36Z` |
| [microsoft/kiota-serialization-form-go](https://github.com/microsoft/kiota-serialization-form-go) | 131 | docs | 6 | 1 | `2026-11-09T20:10:38Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 130 | docs | 5 | 3 | `2026-11-09T22:51:39Z` |
| [microsoft/kiota-http-go](https://github.com/microsoft/kiota-http-go) | 129 | docs | 4 | 1 | `2026-11-09T19:56:17Z` |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 128 | docs | 3 | 3 | `2026-11-09T22:51:56Z` |
| [microsoftgraph/msgraph-sdk-java](https://github.com/microsoftgraph/msgraph-sdk-java) | 126 | docs | 1 | 1 | `2026-11-09T15:46:50Z` |
| [microsoftgraph/msgraph-sdk-go](https://github.com/microsoftgraph/msgraph-sdk-go) | 126 | docs | 1 | 1 | `2026-11-09T15:46:10Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 121 | docs | 6 | 1 | `2026-11-09T22:35:38Z` |
| [Azure/sap-automation](https://github.com/Azure/sap-automation) | 117 | docs | 2 | 1 | `2026-11-09T02:49:24Z` |
| [microsoft/forge-lab](https://github.com/microsoft/forge-lab) | 113 | training | 3 | 0 | `2026-11-09T20:38:58Z` |
| [microsoft/MCAPSTechConnect26-LAB483](https://github.com/microsoft/MCAPSTechConnect26-LAB483) | 113 | training | 3 | 0 | `2026-11-09T16:28:01Z` |
| [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs) | 110 | docs | 49 | 0 | `2026-11-09T18:07:49Z` |
| [Azure/data-api-builder](https://github.com/Azure/data-api-builder) | 103 | docs | 3 | 0 | `2026-11-09T23:03:19Z` |
| [microsoft/kiota-python](https://github.com/microsoft/kiota-python) | 100 | docs | 25 | 0 | `2026-11-09T20:26:24Z` |
| [MicrosoftDocs/architecture-center](https://github.com/MicrosoftDocs/architecture-center) | 98 | docs | 23 | 0 | `2026-11-09T18:31:57Z` |

## Repository Details

### MicrosoftDocs/azure-docs (49 commit(s), signal 110)

Tags: `docs, human-authored, release-language, watchlist`

- [Merge pull request #322249 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-docs/commit/2bd9faf927c18bc5b12156285cfbbdf20adb56c0) - `2026-11-09T18:07:49Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #322194 from MicrosoftDocs/repo_sync_working_branch](https://github.com/MicrosoftDocs/azure-docs/commit/2ce979dd9766ce5ac7131bddd26f0a4150499dcd) - `2026-11-09T17:55:20Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [chore: clarify MCA billing transfer guidance (#321904)](https://github.com/MicrosoftDocs/azure-docs/commit/8daf11608417c972527cf6cfc34d3b7217b74d93) - `2026-11-09T17:39:43Z` - Chris Lodwig (@CLodwigDocs)
- [Update author in optimize write documentation (#322243)](https://github.com/MicrosoftDocs/azure-docs/commit/ef3064091ea3fa4409040ece01285db35f2c1d08) - `2026-11-09T17:32:10Z` - Genevieve Warren (@gewarren)
- [Document IPv6-only virtual network peering preview (#322004)](https://github.com/MicrosoftDocs/azure-docs/commit/4276d0b22252771563393dbb28c5775f0e150458) - `2026-11-09T17:22:00Z` - Allen Sudbring (@asudbring)

### dotnet/docs (44 commit(s), signal 5)

Tags: `bot-only, dependency-noise, docs`

- [Bump Microsoft.Extensions.Hosting across 6 directories (#56831)](https://github.com/dotnet/docs/commit/615ba82cdc4b4a9806d5184c8ac35911272da120) - `2026-11-09T18:53:08Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Extensions.Hosting across 6 directories](https://github.com/dotnet/docs/pull/56831)
- [Bump System.Threading.Tasks.Dataflow across 2 directories (#56819)](https://github.com/dotnet/docs/commit/96596db4e39203941ae746758666c2b0fad01cb9) - `2026-11-09T18:40:43Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump System.Threading.Tasks.Dataflow across 2 directories](https://github.com/dotnet/docs/pull/56819)
- [Bump System.Configuration.ConfigurationManager across 4 directories (…](https://github.com/dotnet/docs/commit/384dc9499d207561df36bb665cdfc088216b8735) - `2026-11-09T18:40:19Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump System.Configuration.ConfigurationManager across 4 directories](https://github.com/dotnet/docs/pull/56826)
- [Bump System.Drawing.Common in /samples/snippets/visualbasic/VS_Snippe…](https://github.com/dotnet/docs/commit/ec7812807375c7b1c818cdc89e8707bee04636ed) - `2026-11-09T18:40:13Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump System.Drawing.Common in /samples/snippets/visualbasic/VS_Snippets_ADO.NET/DataWorks LargeValueType.Photo/VB](https://github.com/dotnet/docs/pull/56828)
- [Bump Microsoft.AspNetCore.OpenApi across 8 directories (#56818)](https://github.com/dotnet/docs/commit/5a758e93ab852bc8fe4c4acd12a30ef21d9c9ffb) - `2026-11-09T18:40:05Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.AspNetCore.OpenApi across 8 directories](https://github.com/dotnet/docs/pull/56818)

### dotnet/runtime (28 commit(s), signal 75)

Tags: `docs, human-authored, release-language`

- [JIT: omit redundant wasm eqz pairs before conditional branches (#137205)](https://github.com/dotnet/runtime/commit/1889003177d297413cfcff3a57e38091555007cf) - `2026-11-09T23:02:36Z` - Andy Ayers (@AndyAyersMS) - PR: [JIT: omit redundant wasm eqz pairs before conditional branches](https://github.com/dotnet/runtime/pull/137205)
- [Arm64-SVE: Implement Vector<T> HIR with SVE (#133422)](https://github.com/dotnet/runtime/commit/d1452914b9d021137366dfab2cb127d68e13fb34) - `2026-11-09T23:00:00Z` - snickolls-arm (@snickolls-arm) - PR: [Arm64-SVE: Implement Vector<T> HIR with SVE](https://github.com/dotnet/runtime/pull/133422)
- [Check version bubble for R2R comparer and per-instantiation intrinsic…](https://github.com/dotnet/runtime/commit/e43d4b9672de5d11a31da7ef40d78564c1e9d166) - `2026-11-09T22:54:40Z` - David Wrighton (@davidwrighton) - PR: [Check version bubble for R2R comparer and per-instantiation intrinsics](https://github.com/dotnet/runtime/pull/137056)
- [JIT: Preserve unused volatile loads (#137117)](https://github.com/dotnet/runtime/commit/34cf80811c00c244828babe454d0b5404e81d39d) - `2026-11-09T22:49:24Z` - Andy Ayers (@AndyAyersMS) - PR: [JIT: Preserve unused volatile loads](https://github.com/dotnet/runtime/pull/137117)
- [JIT: Preserve indirection flags in field-by-field struct copies (#137…](https://github.com/dotnet/runtime/commit/ee57b51e7f4ea891f7ff8a72150c996585a18692) - `2026-11-09T22:47:06Z` - Andy Ayers (@AndyAyersMS) - PR: [JIT: Preserve indirection flags in field-by-field struct copies](https://github.com/dotnet/runtime/pull/137090)

### microsoft/kiota-python (25 commit(s), signal 100)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #883 from hardikkaurani/fix/parameter-collection-s…](https://github.com/microsoft/kiota-python/commit/80718a12c1147fa5dcb29f10b0d0ee125460488c) - `2026-11-09T20:26:24Z` - Vincent Biret (@baywet) - PR: [fix(abstractions): improve parameter collection sanitization and ISO duration validation](https://github.com/microsoft/kiota-python/pull/883)
- [Merge pull request #867 from hardikkaurani/fix/uri-normalization-and-…](https://github.com/microsoft/kiota-python/commit/b97fdd0486f28db520a6f8ca9d29e90d20877fee) - `2026-11-09T20:20:56Z` - Vincent Biret (@baywet) - PR: [fix(abstractions): validate allowed hosts and access token provider in BaseBearerTokenAuthenticationProvider](https://github.com/microsoft/kiota-python/pull/867)
- [test(abstractions): add unit tests for BaseBearerTokenAuthenticationP…](https://github.com/microsoft/kiota-python/commit/e3675d9454651718d1f0351d932e38da4c601ba7) - `2026-11-09T20:14:44Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(abstractions): validate allowed hosts and access token provider in BaseBearerTokenAuthenticationProvider](https://github.com/microsoft/kiota-python/pull/867)
- [fix(abstractions): validate allowed hosts and access token provider i…](https://github.com/microsoft/kiota-python/commit/a1be7b68ea3a0990c175227b63b4af7f10ba4fd4) - `2026-11-09T20:14:44Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(abstractions): validate allowed hosts and access token provider in BaseBearerTokenAuthenticationProvider](https://github.com/microsoft/kiota-python/pull/867)
- [test(abstractions): add regression tests for enum collections with ni…](https://github.com/microsoft/kiota-python/commit/ad58d7299659bcf33989bbb7f12bef446255f920) - `2026-11-09T20:13:34Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(abstractions): improve parameter collection sanitization and ISO duration validation](https://github.com/microsoft/kiota-python/pull/883)

### MicrosoftDocs/architecture-center (23 commit(s), signal 98)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #17290 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/architecture-center/commit/2ca3725cd5b22cc3e76e94a03a3b94c7f32d9335) - `2026-11-09T18:31:57Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #17288 from MicrosoftDocs/findings](https://github.com/MicrosoftDocs/architecture-center/commit/932f8e20d4a5c8e636f57e2c6893ae69d516f8e0) - `2026-11-09T17:51:28Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Handle null column header](https://github.com/MicrosoftDocs/architecture-center/commit/a189884dfd13c12a5790169260c751fff894c427) - `2026-11-09T17:44:04Z` - Chad Kittel (@ckittel)
- [no-op an empty list](https://github.com/MicrosoftDocs/architecture-center/commit/e35fc2f50ad18ac77a67128e5b9f4459e37e2014) - `2026-11-09T16:51:36Z` - Chad Kittel (@ckittel)
- [Update What's New for November 2026 (#17273)](https://github.com/MicrosoftDocs/architecture-center/commit/f24916dd0dfd1b14865c32422a48c66228666129) - `2026-11-09T16:21:52Z` - azure-patterns-practices-assistant[bot] (@azure-patterns-practices-assistant[bot])

### MicrosoftDocs/fabric-docs (23 commit(s), signal 98)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #3499 from MicrosoftDocs/main639298443686795477syn…](https://github.com/MicrosoftDocs/fabric-docs/commit/aadea08f35c3edaa9c32535c772792f02555c9a4) - `2026-11-09T18:06:37Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3499)
- [Merging changes synced from https://github.com/MicrosoftDocs/fabric-d…](https://github.com/MicrosoftDocs/fabric-docs/commit/a11748ab0afd5535d5a948546217626c55365687) - `2026-11-09T18:06:05Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3499)
- [Merge pull request #17296 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/fabric-docs/commit/7218ec999210063c255a03313c8dbd6cea671092) - `2026-11-09T18:02:41Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3499)
- [Confirm merge from repo_sync_working_branch to main to sync with http…](https://github.com/MicrosoftDocs/fabric-docs/commit/a6ce4894daaa5078fe9b81f958e1b1dcd983a9e8) - `2026-11-09T17:55:24Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3499)
- [Merge pull request #17291 from ukchrist/patch-15](https://github.com/MicrosoftDocs/fabric-docs/commit/83ad369a3e64eb88e38e70258ff128e527f60a36) - `2026-11-09T14:32:12Z` - prmerger-automator[bot] (@prmerger-automator[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3499)

### MicrosoftDocs/azure-aks-docs (16 commit(s), signal 91)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-ak…](https://github.com/MicrosoftDocs/azure-aks-docs/commit/cbc78e0af990aa56a8fdcceee64f8d276a85d54a) - `2026-11-09T07:03:24Z` - Learn Build Service GitHub App
- [Merge pull request #4172 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-aks-docs/commit/d096a85de3e4982a72156077bdf3874b547bcae6) - `2026-11-09T07:02:43Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #4171 from fhryo-msft/main](https://github.com/MicrosoftDocs/azure-aks-docs/commit/679d32fb4d965a2b6eb254a00e25008e44be2f43) - `2026-11-09T01:14:14Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Update articles/aks/operator-best-practices-storage.md](https://github.com/MicrosoftDocs/azure-aks-docs/commit/f701ca2b7aa8ff71a2cf76d8f9fc9e511d9e3fb0) - `2026-11-09T01:02:27Z` - fhryo-msft (@fhryo-msft)
- [Update articles/aks/concepts-storage.md](https://github.com/MicrosoftDocs/azure-aks-docs/commit/f11f8e3f2d2aff8494c851cbd7f679fc376b03e4) - `2026-11-09T01:02:17Z` - fhryo-msft (@fhryo-msft)

### Azure-Samples/azuresandbox (15 commit(s), signal 140)

Tags: `human-authored, release, release-language, samples, watchlist`

- Release: [AzureSandbox v6.0.7](https://github.com/Azure-Samples/azuresandbox/releases/tag/v6.0.7) - `2026-11-09T20:44:44Z`
- [Merge pull request #1020 from Azure-Samples/vnext](https://github.com/Azure-Samples/azuresandbox/commit/3c99e1bc6cc943ef79b4fe1de6d9f4c89856c396) - `2026-11-09T20:43:38Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Release: vnext to main (azurerm 5.13)](https://github.com/Azure-Samples/azuresandbox/pull/1020)
- [Merge pull request #1019 from Azure-Samples/deps/azurerm-5.13](https://github.com/Azure-Samples/azuresandbox/commit/e5598534eb1494f6ba0dcc74565d656d5e1ea19a) - `2026-11-09T17:35:30Z` - Roger Doherty (MSFT) (@doherty100) - PR: [chore(deps): update hashicorp/azurerm requirement to ~> 5.13.0](https://github.com/Azure-Samples/azuresandbox/pull/1019)
- [chore(deps): update hashicorp/azurerm requirement from ~> 5.12.0 to ~…](https://github.com/Azure-Samples/azuresandbox/commit/6025b01312f8153e4b509b1c734a345a6078ffda) - `2026-11-09T16:50:12Z` - Roger Doherty (MSFT) (@doherty100) - PR: [chore(deps): update hashicorp/azurerm requirement to ~> 5.13.0](https://github.com/Azure-Samples/azuresandbox/pull/1019)
- [chore(deps): update hashicorp/azurerm requirement from ~> 5.12.0 to ~…](https://github.com/Azure-Samples/azuresandbox/commit/59df14db0e08d4764d91276db6a10a0a81959727) - `2026-11-09T16:50:11Z` - Roger Doherty (MSFT) (@doherty100) - PR: [chore(deps): update hashicorp/azurerm requirement to ~> 5.13.0](https://github.com/Azure-Samples/azuresandbox/pull/1019)
- [chore(deps): update hashicorp/azurerm requirement from ~> 5.12.0 to ~…](https://github.com/Azure-Samples/azuresandbox/commit/be786c07359bdaa0cce179f5707e9a89a16f66c7) - `2026-11-09T16:50:10Z` - Roger Doherty (MSFT) (@doherty100) - PR: [chore(deps): update hashicorp/azurerm requirement to ~> 5.13.0](https://github.com/Azure-Samples/azuresandbox/pull/1019)

### microsoft/onnxruntime (13 commit(s), signal 98)

Tags: `human-authored, release-language, samples, watchlist`

- [Centralize build tool version specification (#33852)](https://github.com/microsoft/onnxruntime/commit/260bd42748aa4f2bb48e19b4aaac76f35d5462ff) - `2026-11-09T22:25:58Z` - Edward Chen (@edgchen1) - PR: [Centralize build tool version specification](https://github.com/microsoft/onnxruntime/pull/33852)
- [Validate TreeEnsemble category set indices (#33825)](https://github.com/microsoft/onnxruntime/commit/84384280ee830fd1d15614bf479954aaa65ab56d) - `2026-11-09T22:21:29Z` - Akshay Sonawane (@apsonawane) - PR: [Validate TreeEnsemble category set indices](https://github.com/microsoft/onnxruntime/pull/33825)
- [Avoid double initialization when registering plugin EP libraries (#33…](https://github.com/microsoft/onnxruntime/commit/22fe617ba5a99bce80a07c31b6cb53d30d6dd4c4) - `2026-11-09T22:18:12Z` - Copilot (@Copilot) - PR: [Avoid double initialization when registering plugin EP libraries](https://github.com/microsoft/onnxruntime/pull/33701)
- [Fix Windows CUDA builds with contrib operators disabled (#33702)](https://github.com/microsoft/onnxruntime/commit/1849754b9a4d73c3c1b43f694bed28d0368c20e1) - `2026-11-09T22:12:36Z` - Copilot (@Copilot) - PR: [Fix Windows CUDA builds with contrib operators disabled](https://github.com/microsoft/onnxruntime/pull/33702)
- [Parallelize CPU MultiHeadAttention QKV transposes (#33887)](https://github.com/microsoft/onnxruntime/commit/e440187228d03bc16a49efef10aeaac47b34bdd2) - `2026-11-09T22:12:19Z` - Copilot (@Copilot) - PR: [Parallelize CPU MultiHeadAttention QKV transposes](https://github.com/microsoft/onnxruntime/pull/33887)

### microsoft/kiota-samples (13 commit(s), signal 88)

Tags: `docs, human-authored, product:Microsoft Graph, watchlist`

- [Merge pull request #9323 from microsoft/dependabot/go_modules/msgraph…](https://github.com/microsoft/kiota-samples/commit/d98fb617d3d994edab8a1b06fa4d09f08af5c923) - `2026-11-09T14:40:10Z` - Vincent Biret (@baywet) - PR: [build(deps): bump github.com/microsoft/kiota-serialization-multipart-go from 1.1.4 to 1.1.5 in /msgraph-mail/go in the kiota-dependencies group](https://github.com/microsoft/kiota-samples/pull/9323)
- [Merge pull request #9324 from microsoft/dependabot/go_modules/get-sta…](https://github.com/microsoft/kiota-samples/commit/f6ac5359683cec17a1142bf727359254f7acc37f) - `2026-11-09T14:40:04Z` - Vincent Biret (@baywet) - PR: [build(deps): bump github.com/microsoft/kiota-serialization-multipart-go from 1.1.4 to 1.1.5 in /get-started/quickstart/go in the kiota-dependencies group](https://github.com/microsoft/kiota-samples/pull/9324)
- [Merge pull request #9325 from microsoft/dependabot/go_modules/petstor…](https://github.com/microsoft/kiota-samples/commit/0141e68343330f1a873cd905b9a4b5989c862a41) - `2026-11-09T14:39:58Z` - Vincent Biret (@baywet) - PR: [build(deps): bump github.com/microsoft/kiota-serialization-multipart-go from 1.1.4 to 1.1.5 in /petstore/go in the kiota-dependencies group](https://github.com/microsoft/kiota-samples/pull/9325)
- [Merge pull request #9326 from microsoft/dependabot/npm_and_yarn/msgra…](https://github.com/microsoft/kiota-samples/commit/bb6744d9864e29f20241379e95f2331aea153b37) - `2026-11-09T14:39:53Z` - Vincent Biret (@baywet) - PR: [build(deps): bump the kiota-dependencies group in /msgraph-mail/typescript with 2 updates](https://github.com/microsoft/kiota-samples/pull/9326)
- [Merge pull request #9327 from microsoft/dependabot/go_modules/get-sta…](https://github.com/microsoft/kiota-samples/commit/64a84831a99c402c3b540c00d301e19d2a8f452d) - `2026-11-09T14:39:47Z` - Vincent Biret (@baywet) - PR: [build(deps): bump github.com/microsoft/kiota-serialization-multipart-go from 1.1.4 to 1.1.5 in /get-started/azure-auth/go in the kiota-dependencies group](https://github.com/microsoft/kiota-samples/pull/9327)

### Azure/azure-sdk-for-java (12 commit(s), signal 137)

Tags: `docs, human-authored, product:Azure AI, product:Azure SDK, release, release-language, watchlist`

- Release: [com.azure+azure-data-appconfiguration_1.12.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-data-appconfiguration_1.12.0) - `2026-11-09T20:09:59Z`
- Release: [com.azure.resourcemanager+azure-resourcemanager-chaos_1.4.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-chaos_1.4.0) - `2026-11-09T18:04:48Z`
- [[Storage] Make blob User-Agent rewriting independent of the azure-sto…](https://github.com/Azure/azure-sdk-for-java/commit/f393ade68be17a61a7b671de04d4c83caf4f9a8e) - `2026-11-09T22:09:01Z` - browndav-msft (@browndav-msft) - PR: [[Storage] Make blob User-Agent rewriting independent of the azure-storage-blob version format](https://github.com/Azure/azure-sdk-for-java/pull/51180)
- [Sync eng/common directory with azure-sdk-tools for PR 17441 (#51143)](https://github.com/Azure/azure-sdk-for-java/commit/3f4390361ddfaa36b9a4b28c655b62c1e02bfd59) - `2026-11-09T20:33:50Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17441](https://github.com/Azure/azure-sdk-for-java/pull/51143)
- [App Config 1.8.0 (#51172)](https://github.com/Azure/azure-sdk-for-java/commit/8d21722688541d6435cca3f450eebb7c9829a53d) - `2026-11-09T19:27:55Z` - Matthew Metcalf (@mrm9084) - PR: [App Config 1.8.0](https://github.com/Azure/azure-sdk-for-java/pull/51172)
- [App Config 1.8.0 (#51172)](https://github.com/Azure/azure-sdk-for-java/commit/3d0d520fbf4e709ec0eb009581cf045d802599b0) - `2026-11-09T19:10:51Z` - Matthew Metcalf (@mrm9084)
- [App Config 1.8.0 (#51172)](https://github.com/Azure/azure-sdk-for-java/commit/b10d112e5d6b87b264aee3423aafb3e88e16b93e) - `2026-11-09T19:07:01Z` - Matthew Metcalf (@mrm9084)

### dotnet/android-api-docs (12 commit(s), signal 87)

Tags: `docs, human-authored, product:Microsoft Graph, watchlist`

- [Preserve importer metadata bytes and withhold invalid source text (#1…](https://github.com/dotnet/android-api-docs/commit/97d1641d63483fa54269c8cf4906f0b05a107bd7) - `2026-11-09T18:55:37Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Preserve importer metadata bytes and withhold invalid source text](https://github.com/dotnet/android-api-docs/pull/1297)
- [Fill verified Android.Graphics documentation (#1295)](https://github.com/dotnet/android-api-docs/commit/30376b6dbc6c8d7470ea3e6e48178c0a1e24c1a8) - `2026-11-09T17:36:31Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Fill verified Android.Graphics documentation](https://github.com/dotnet/android-api-docs/pull/1295)
- [Fill verified Java.Util API documentation (#1294)](https://github.com/dotnet/android-api-docs/commit/7256eab45415b77ecbd26044a3aa5f03899f1ff3) - `2026-11-09T15:04:39Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Fill verified Java.Util API documentation](https://github.com/dotnet/android-api-docs/pull/1294)
- [Fill verified Android.Net documentation placeholders (#1299)](https://github.com/dotnet/android-api-docs/commit/d7c670be4cb2529e928f7dffb2cb322be4fa4b36) - `2026-11-09T14:42:11Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Fill verified Android.Net documentation placeholders](https://github.com/dotnet/android-api-docs/pull/1299)
- [Fill verified Android.Icu.Text documentation (#1296)](https://github.com/dotnet/android-api-docs/commit/3c4e60fe60b21e0ac8620b2adb1f0295f831bc84) - `2026-11-09T14:13:50Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Fill verified Android.Icu.Text documentation](https://github.com/dotnet/android-api-docs/pull/1296)

### Azure/azure-sdk-for-net (10 commit(s), signal 135)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [Azure.Security.CodeTransparency_1.1.0-beta.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Security.CodeTransparency_1.1.0-beta.1) - `2026-11-09T15:02:20Z`
- Release: [Azure.ResourceManager.RedisEnterprise_1.4.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.RedisEnterprise_1.4.0) - `2026-11-09T09:56:58Z`
- [[Identity] Support Azure Arc user-assigned managed identities (#63126)](https://github.com/Azure/azure-sdk-for-net/commit/3c986f17fa081c03b1c5bf60f96876718286f8a0) - `2026-11-09T21:40:40Z` - Jonathan Cárdenas (@JonathanCrd) - PR: [[Identity] Support Azure Arc user-assigned managed identities](https://github.com/Azure/azure-sdk-for-net/pull/63126)
- [Make re-review coverage reflect what was actually read (#64699)](https://github.com/Azure/azure-sdk-for-net/commit/7af4d79a589ebbd6163298255f7a901d02e06a25) - `2026-11-09T21:31:52Z` - m-nash (@m-nash) - PR: [Make re-review coverage reflect what was actually read](https://github.com/Azure/azure-sdk-for-net/pull/64699)
- [Prepare Azure Monitor exporter 1.11.0-beta.1 release  (#64695)](https://github.com/Azure/azure-sdk-for-net/commit/1cc6badd270e8bb21d036bcd406b8196c01dd70e) - `2026-11-09T21:17:19Z` - Harsimar Kaur (@harsimar) - PR: [Prepare Azure Monitor exporter 1.11.0-beta.1 release](https://github.com/Azure/azure-sdk-for-net/pull/64695)
- [Add configuration/DI parity check to code-review rules (#64698)](https://github.com/Azure/azure-sdk-for-net/commit/df9597343df6cbcaefebb131b917d4ca0c16718e) - `2026-11-09T20:13:26Z` - m-nash (@m-nash) - PR: [Add configuration/DI parity check to code-review rules](https://github.com/Azure/azure-sdk-for-net/pull/64698)
- [Several code fixes for GA (#64512)](https://github.com/Azure/azure-sdk-for-net/commit/0dfafec767acde5db58207c7ff08b1eec48f276e) - `2026-11-09T19:39:08Z` - Nikolay Rovinskiy (@nick863)

### MicrosoftDocs/SupportArticles-docs (9 commit(s), signal 84)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/fb1bcbcbe9cab60db00cd8be363a46dc07e1d477) - `2026-11-09T22:04:44Z` - Learn Build Service GitHub App
- [Merge pull request #12815 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/6d7030c555b49a61f9595c75982726ca602af7c8) - `2026-11-09T22:02:49Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [AB#13223 Teams optimization (#12808)](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/b8560a9c3e34a8e9ad41c096bf1ca48ddcc45452) - `2026-11-09T20:21:34Z` - KC Cross (@KCCross)
- [Update remediation for ECS_E_AZURE_STORAGE_SHARE_SIZE_LIMIT_REACHED (…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/e54a22b3999ef8042fbc4c5fceef3cb90e01fbc6) - `2026-11-09T19:13:53Z` - Grace Kim (@rladbsal)
- [Confirm merge from repo_sync_working_branch to main to sync with http…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/52a03f4e53f4a890071192399a375ca866453eb8) - `2026-11-09T18:07:33Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### microsoft/kiota-abstractions-go (8 commit(s), signal 83)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #312 from hardikkaurani/fix/duration-parsing-and-u…](https://github.com/microsoft/kiota-abstractions-go/commit/3d1c59e9c38da97b5ced693967060fa5236324f1) - `2026-11-09T20:27:52Z` - Vincent Biret (@baywet) - PR: [fix(serialization): handle integer seconds in ISO durations and reject component-free strings](https://github.com/microsoft/kiota-abstractions-go/pull/312)
- [fix(serialization): anchor ISO duration regexes, support integer seco…](https://github.com/microsoft/kiota-abstractions-go/commit/1193d38e62d0951c3debf6161c28c9d4de11a3f5) - `2026-11-09T20:22:03Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(serialization): handle integer seconds in ISO durations and reject component-free strings](https://github.com/microsoft/kiota-abstractions-go/pull/312)
- [Merge pull request #313 from hardikkaurani/fix/duration-composite-nor…](https://github.com/microsoft/kiota-abstractions-go/commit/6102fb171e9e0cb70f8109661b854bc1b7959c1c) - `2026-11-09T20:09:24Z` - Vincent Biret (@baywet) - PR: [fix(serialization): prevent invalid week normalization and preserve millisecond precision in durations](https://github.com/microsoft/kiota-abstractions-go/pull/313)
- [Merge pull request #314 from microsoft/dependabot/go_modules/github.c…](https://github.com/microsoft/kiota-abstractions-go/commit/b959deffdb99a45ace305ca906a3c44e4a3a05f6) - `2026-11-09T19:05:28Z` - Vincent Biret (@baywet) - PR: [chore(deps): bump github.com/std-uritemplate/std-uritemplate/go/v2 from 2.0.12 to 2.0.13](https://github.com/microsoft/kiota-abstractions-go/pull/314)
- [ci: adds missing merge groups trigger for merge queue (#315)](https://github.com/microsoft/kiota-abstractions-go/commit/b1e9a21b0a3c18e4610111bd4f1e8cae8a2b7c0a) - `2026-11-09T18:58:03Z` - Vincent Biret (@baywet) - PR: [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-abstractions-go/pull/315)

### microsoft/kiota-ruby (8 commit(s), signal 133)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [v0.25.3](https://github.com/microsoft/kiota-ruby/releases/tag/v0.25.3) - `2026-11-09T18:53:20Z`
- [Merge pull request #209 from microsoft/release-please--branches--main](https://github.com/microsoft/kiota-ruby/commit/11410b999f27c63caa1d391a97fcf3429218ac18) - `2026-11-09T18:50:21Z` - Vincent Biret (@baywet) - PR: [chore(main): release 0.25.3](https://github.com/microsoft/kiota-ruby/pull/209)
- [chore(main): release 0.25.3](https://github.com/microsoft/kiota-ruby/commit/7244e44f0f03626b920da015285114924f61fe60) - `2026-11-09T18:47:12Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(main): release 0.25.3](https://github.com/microsoft/kiota-ruby/pull/209)
- [Merge pull request #201 from andreaTP/fix/json-any-value](https://github.com/microsoft/kiota-ruby/commit/7015696b07964e6722b70ecbba26caf260c39c06) - `2026-11-09T18:40:53Z` - Vincent Biret (@baywet) - PR: [fix(json): write booleans, guids, symbols and nested objects in additional data](https://github.com/microsoft/kiota-ruby/pull/201)
- [Merge pull request #206 from andreaTP/fix/stduritemplate-commas](https://github.com/microsoft/kiota-ruby/commit/98344ff7efd9ab7b680d59bc22dc4ebf0193c826) - `2026-11-09T18:40:50Z` - Vincent Biret (@baywet) - PR: [fix(abstractions): require std-uritemplate 2.0.13, which keeps commas in paths](https://github.com/microsoft/kiota-ruby/pull/206)
- [Merge pull request #213 from microsoft/copilot/merge-group-ruby-20261109](https://github.com/microsoft/kiota-ruby/commit/7704db72eb5a52121f16919fd3c5d5f5f3e818f9) - `2026-11-09T18:36:46Z` - Gavin Barron (@gavinbarron) - PR: [ci: run required ruby checks for merge groups](https://github.com/microsoft/kiota-ruby/pull/213)

### microsoft/viva-insights-sample-code (8 commit(s), signal 48)

Tags: `human-authored, samples`

- [feat(frontier): add governed business-process analysis skill](https://github.com/microsoft/viva-insights-sample-code/commit/57ab0e5ba0df29c91fb63c4f35bcdea5143d2c58) - `2026-11-09T16:13:42Z` - Martin Chan (@martinctc)
- [docs(frontier): add evidence-led reporting and safe revision guidance](https://github.com/microsoft/viva-insights-sample-code/commit/fc76d3c81c2119d5c68393d622f5ef909ce86728) - `2026-11-09T15:52:46Z` - Martin Chan (@martinctc)
- [fix(frontier): validate meeting flags and clarify comparison rules](https://github.com/microsoft/viva-insights-sample-code/commit/2db0b62f86cd052fbd3a0963c7cc666778ce2237) - `2026-11-09T15:50:08Z` - Martin Chan (@martinctc)
- [fix(site): isolate dashboard render output and remove duplicate anchors](https://github.com/microsoft/viva-insights-sample-code/commit/75dae55c0ddfead231328baa1b9c53d2537d15e3) - `2026-11-09T15:34:56Z` - Martin Chan (@martinctc)
- [feat(frontier): add dashboard guides and refresh analysis skill](https://github.com/microsoft/viva-insights-sample-code/commit/f3fa2e6450375aec03ebacc9812b11116e69920f) - `2026-11-09T15:26:14Z` - Martin Chan (@martinctc)

### MicrosoftDocs/learn (8 commit(s), signal 93)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/ff41a6b21e5fbc642281adaecf83576a708bbc90) - `2026-11-09T12:19:37Z` - Learn Build Service GitHub App
- [Merge pull request #56760 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/learn/commit/0aaf723f2c886cd8cb5ee61ebc585264cc15777d) - `2026-11-09T12:09:11Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [First draft of module in my fork of release branch (#56752) (#56759)](https://github.com/MicrosoftDocs/learn/commit/268373ec287ac122aa5306e40f06b0f057149cf6) - `2026-11-09T07:25:16Z` - Orin Thomas (@Orin-Thomas)
- [Taking ownership of abandoned module (#56757)](https://github.com/MicrosoftDocs/learn/commit/d5901af2888f0ab774a28c33eabdb841c21db928) - `2026-11-09T03:07:53Z` - Orin Thomas (@Orin-Thomas)
- [Taking ownership of abandoned module so that I am now responsible for…](https://github.com/MicrosoftDocs/learn/commit/778cfa2b00838ce65a872cf00216b5ba3fd6b3cd) - `2026-11-09T03:03:44Z` - Orin Thomas (@Orin-Thomas)

### Azure/azure-sdk-for-js (7 commit(s), signal 132)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [@azure/arm-sovereign_1.0.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-sovereign_1.0.0-beta.1) - `2026-11-09T17:46:42Z`
- Release: [@azure/arm-redisenterprisecache_5.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-redisenterprisecache_5.0.0) - `2026-11-09T09:04:47Z`
- Release: [@azure/core-rest-pipeline_1.25.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/core-rest-pipeline_1.25.1) - `2026-11-08T17:24:03Z`
- [[Attestation] Prepare 1.0.2 release (#40722)](https://github.com/Azure/azure-sdk-for-js/commit/2812dd520f3a654824b4aa44651e3824e6963e64) - `2026-11-09T22:13:08Z` - Olga Kroshkina (@olkroshk) - PR: [[Attestation] Prepare 1.0.2 release](https://github.com/Azure/azure-sdk-for-js/pull/40722)
- [[Attestation] Validate service tokens only against trusted signers an…](https://github.com/Azure/azure-sdk-for-js/commit/efd8ddc44f0d8ef985b69c163f1f495ff3d7c915) - `2026-11-09T21:41:40Z` - Olga Kroshkina (@olkroshk) - PR: [[Attestation] Validate service tokens only against trusted signers and stop partial options from skipping validation](https://github.com/Azure/azure-sdk-for-js/pull/40610)
- [[EngSys] pnpm update --recursive --no-save (#40719)](https://github.com/Azure/azure-sdk-for-js/commit/62644018be7226f23e23fd9e5d8d370305f83cec) - `2026-11-09T20:48:50Z` - Jeremy Meng (@jeremymeng) - PR: [[EngSys] pnpm update --recursive --no-save](https://github.com/Azure/azure-sdk-for-js/pull/40719)
- [[Cosmos] Increase ID encoding test timeout (#40604)](https://github.com/Azure/azure-sdk-for-js/commit/e24feb1ce3f9a295cdb92dac99ae7ba119f1f6c2) - `2026-11-09T18:32:59Z` - Simon Moreno (@simorenoh) - PR: [[Cosmos] Increase ID encoding test timeout](https://github.com/Azure/azure-sdk-for-js/pull/40604)
- [Upgrade release tooling to glob 14.0.3 (#40714)](https://github.com/Azure/azure-sdk-for-js/commit/c6df707a3133d50d29c0ecac3047fde00c238dac) - `2026-11-09T17:30:27Z` - Jeremy Meng (@jeremymeng) - PR: [Upgrade release tooling to glob 14.0.3](https://github.com/Azure/azure-sdk-for-js/pull/40714)

### dotnet/roslyn (7 commit(s), signal 82)

Tags: `docs, human-authored, product:Azure AI, product:Azure SDK, watchlist`

- [Fix nullable annotation warning from nameof emission for a generic co…](https://github.com/dotnet/roslyn/commit/64d878021c6b5c42bd518249dee786cb096d3d54) - `2026-11-09T22:00:21Z` - Shanewas Ahmed (@shanewas) - PR: [Fix nullable annotation warning from nameof emission for a generic component parameter](https://github.com/dotnet/roslyn/pull/86311)
- [[main] Update dependencies from dotnet/roslyn (#86108)](https://github.com/dotnet/roslyn/commit/8fe8ca9a276a58bdd7303ff77332ed13b0cd23cf) - `2026-11-09T21:33:52Z` - Ankita Khera (@akhera99) - PR: [[main] Update dependencies from dotnet/roslyn](https://github.com/dotnet/roslyn/pull/86108)
- [Allow Razor utilities package on non-Windows (#86349)](https://github.com/dotnet/roslyn/commit/360a8178f50bc4c085d8fb6b5daa47bd4e9fe9e6) - `2026-11-09T20:49:46Z` - David Wengier (@davidwengier) - PR: [Allow Razor utilities package on non-Windows](https://github.com/dotnet/roslyn/pull/86349)
- [Remove plan-first requirement from agent instructions (#86353)](https://github.com/dotnet/roslyn/commit/23357d6562e8a44f0e7480ee66229a9e268f81f8) - `2026-11-09T19:03:13Z` - Ankita Khera (@akhera99) - PR: [Remove plan-first requirement from agent instructions](https://github.com/dotnet/roslyn/pull/86353)
- [Ensure that Length getter cannot change reference-type receiver befor…](https://github.com/dotnet/roslyn/commit/66dacb3e096abf8db7dd422875397d155976598d) - `2026-11-09T19:02:47Z` - AlekseyTs (@AlekseyTs) - PR: [Ensure that Length getter cannot change reference-type receiver before implicit indexing or slicing completes](https://github.com/dotnet/roslyn/pull/86330)

### microsoft/vscode-docs (7 commit(s), signal 92)

Tags: `docs, human-authored, release-language, watchlist`

- [docs(setup): document PATH verification and unrecognized command trou…](https://github.com/microsoft/vscode-docs/commit/2558307808dfcdac2a566e14079578b18a56249f) - `2026-11-09T20:30:26Z` - Abdul karim mia (@abdul-karim-mia) - PR: [docs(setup): document PATH verification and unrecognized command troubleshooting on Windows](https://github.com/microsoft/vscode-docs/pull/10614)
- [Correct terminal confirmOnExit description (#10611)](https://github.com/microsoft/vscode-docs/commit/b14ee4fc848b732be63a16dc3898a2c635b4475e) - `2026-11-09T20:19:38Z` - Zain Qureshi (@ZainnQureshii) - PR: [Correct terminal confirmOnExit description](https://github.com/microsoft/vscode-docs/pull/10611)
- [Merge pull request #10615 from microsoft/ntrogh/insiders-relnotes](https://github.com/microsoft/vscode-docs/commit/51c583e3d6b28a9afd00741828a58e5a6adae565) - `2026-11-09T17:04:07Z` - Nick Trogh (@ntrogh) - PR: [Update Insiders release notes](https://github.com/microsoft/vscode-docs/pull/10615)
- [Update Insiders release notes](https://github.com/microsoft/vscode-docs/commit/1b705105f252d04499106dfff034e76a6fa643f8) - `2026-11-09T13:05:44Z` - Nick Trogh (@ntrogh) - PR: [Update Insiders release notes](https://github.com/microsoft/vscode-docs/pull/10615)
- [Update Customization concepts and overview (#10598)](https://github.com/microsoft/vscode-docs/commit/b4683a7e3412f178ec0f77a606dc779fd1d5924c) - `2026-11-08T21:18:13Z` - Nick Trogh (@ntrogh) - PR: [Update Customization concepts and overview](https://github.com/microsoft/vscode-docs/pull/10598)

### microsoft/kiota-dart (7 commit(s), signal 132)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [microsoft_kiota_serialization_multipart: v0.0.5](https://github.com/microsoft/kiota-dart/releases/tag/microsoft_kiota_serialization_multipart-v0.0.5) - `2026-11-09T19:59:36Z`
- Release: [microsoft_kiota_serialization_json: v0.0.11](https://github.com/microsoft/kiota-dart/releases/tag/microsoft_kiota_serialization_json-v0.0.11) - `2026-11-09T19:59:34Z`
- Release: [microsoft_kiota_serialization_form: v0.0.7](https://github.com/microsoft/kiota-dart/releases/tag/microsoft_kiota_serialization_form-v0.0.7) - `2026-11-09T19:59:33Z`
- Release: [microsoft_kiota_http: v0.0.8](https://github.com/microsoft/kiota-dart/releases/tag/microsoft_kiota_http-v0.0.8) - `2026-11-09T19:59:31Z`
- Release: [microsoft_kiota_abstractions: v0.3.3](https://github.com/microsoft/kiota-dart/releases/tag/microsoft_kiota_abstractions-v0.3.3) - `2026-11-09T19:59:30Z`
- [Merge pull request #171 from hardikkaurani/fix/json-parse-node-null-o…](https://github.com/microsoft/kiota-dart/commit/a30ee6d2f45651a937d01f17403cfef0538505f4) - `2026-11-09T20:22:36Z` - Vincent Biret (@baywet) - PR: [fix(serialization-json): return null for null JSON nodes and eliminate duplicate hooks in JsonParseNode](https://github.com/microsoft/kiota-dart/pull/171)
- [Merge pull request #164 from microsoft/release-please--branches--main](https://github.com/microsoft/kiota-dart/commit/ad0d98299fe800e3ba39da6cf9f42df2cdf83540) - `2026-11-09T19:56:35Z` - Vincent Biret (@baywet) - PR: [chore: release main](https://github.com/microsoft/kiota-dart/pull/164)
- [fix(serialization-json): guard parsable hook invocation by map shape](https://github.com/microsoft/kiota-dart/commit/360a5fda680183a64c889b2432fa9282d4e472c1) - `2026-11-09T19:19:30Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(serialization-json): return null for null JSON nodes and eliminate duplicate hooks in JsonParseNode](https://github.com/microsoft/kiota-dart/pull/171)
- [chore: release main](https://github.com/microsoft/kiota-dart/commit/57bdb40b775d093846b11214b9097cb62013e2af) - `2026-11-09T18:38:52Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore: release main](https://github.com/microsoft/kiota-dart/pull/164)
- [Merge pull request #173 from microsoft/copilot-mq-dart](https://github.com/microsoft/kiota-dart/commit/da2d0979b5c8ebdf539746bf271a380104ec6de9) - `2026-11-09T18:35:44Z` - Gavin Barron (@gavinbarron) - PR: [ci: run required Dart checks for merge groups](https://github.com/microsoft/kiota-dart/pull/173)

### microsoft/kiota (7 commit(s), signal 82)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [docs: point the Ruby links at the kiota-ruby monorepo (#8501)](https://github.com/microsoft/kiota/commit/1b9a5aa33818523855cf9060919115f0cd2ebbc0) - `2026-11-09T20:05:42Z` - Andrea Peruffo (@andreaTP) - PR: [docs: point the Ruby links at the kiota-ruby monorepo](https://github.com/microsoft/kiota/pull/8501)
- [fix(ruby): rename colliding flattened models and keep function path p…](https://github.com/microsoft/kiota/commit/afa2be459e8c158d2853859303cfb7d2f72141c3) - `2026-11-09T15:28:35Z` - Andrea Peruffo (@andreaTP) - PR: [fix(ruby): rename colliding flattened models and keep function path parameters](https://github.com/microsoft/kiota/pull/8502)
- [chore(deps): bump ruby/setup-ruby from 1.335.0 to 1.336.0 (#8557)](https://github.com/microsoft/kiota/commit/2c9676da38529ff637517ab09aac67e2c82162d3) - `2026-11-09T15:06:25Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump ruby/setup-ruby from 1.335.0 to 1.336.0](https://github.com/microsoft/kiota/pull/8557)
- [chore(deps): bump actions/setup-dotnet from 6.0.0 to 6.1.0 (#8562)](https://github.com/microsoft/kiota/commit/e9fb7f86961a4a1e08195e636d9e301fa43042bd) - `2026-11-09T14:39:47Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump actions/setup-dotnet from 6.0.0 to 6.1.0](https://github.com/microsoft/kiota/pull/8562)
- [chore(deps-dev): bump webpack-cli from 7.2.3 to 7.3.1 in /vscode (#8565)](https://github.com/microsoft/kiota/commit/478787b98389cf9bf6db028257f25fd3f8bf51c2) - `2026-11-09T14:39:45Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps-dev): bump webpack-cli from 7.2.3 to 7.3.1 in /vscode](https://github.com/microsoft/kiota/pull/8565)

### Azure/azure-sdk-for-python (6 commit(s), signal 121)

Tags: `docs, human-authored, product:Azure SDK, release, watchlist`

- Release: [azure-mgmt-chaos_3.0.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-chaos_3.0.0) - `2026-11-09T18:29:51Z`
- [[CI] Remove management plan workarounds (#49659)](https://github.com/Azure/azure-sdk-for-python/commit/235addf15cd7aed4cc8ef400927ea39fb6fc33d1) - `2026-11-09T22:35:38Z` - Travis Prescott (@tjprescott) - PR: [[CI] Remove management plan workarounds](https://github.com/Azure/azure-sdk-for-python/pull/49659)
- [Add Python 3.15 to the shared pipeline matrix (#49896)](https://github.com/Azure/azure-sdk-for-python/commit/6920dd7eb01e68a72a62d7147618ed7b076bd898) - `2026-11-09T19:28:38Z` - Libba Lawrence (@l0lawrence)
- [[AutoPR azure-mgmt-chaos]-generated-from-SDK Generation - Python-7038…](https://github.com/Azure/azure-sdk-for-python/commit/bdcbed4c5868f8c36af60e69104faaa1e9704753) - `2026-11-09T16:54:06Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-mgmt-chaos]-generated-from-SDK Generation - Python-7038298](https://github.com/Azure/azure-sdk-for-python/pull/49828)
- [[Automation] Update emitter package dependencies (#49864)](https://github.com/Azure/azure-sdk-for-python/commit/17a56c7d32b742701dea535e7b424154f6e6cdb1) - `2026-11-09T16:24:37Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[Automation] Update emitter package dependencies](https://github.com/Azure/azure-sdk-for-python/pull/49864)
- [Delete sdk/privatetrafficmanager directory (#49894)](https://github.com/Azure/azure-sdk-for-python/commit/c6ea2b57f3d2caea321a66dc54c94f3de79f529a) - `2026-11-09T09:44:08Z` - Chenxi Jiang (@ChenxiJiang333) - PR: [Delete sdk/privatetrafficmanager directory](https://github.com/Azure/azure-sdk-for-python/pull/49894)

### microsoft/kiota-serialization-form-go (6 commit(s), signal 131)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [v1.1.7](https://github.com/microsoft/kiota-serialization-form-go/releases/tag/v1.1.7) - `2026-11-09T19:59:22Z`
- [Merge pull request #164 from hardikkaurani/fix/form-parse-node-null-p…](https://github.com/microsoft/kiota-serialization-form-go/commit/9cfeef25e5190c22782929d19ab97c588f415d09) - `2026-11-09T20:10:38Z` - Vincent Biret (@baywet) - PR: [fix(form): return nil for null and whitespace object and collection nodes in FormParseNode](https://github.com/microsoft/kiota-serialization-form-go/pull/164)
- [Merge pull request #156 from microsoft/release-please--branches--main…](https://github.com/microsoft/kiota-serialization-form-go/commit/a52899f640c42aa33d9b85a6cee71e5ee261b689) - `2026-11-09T19:56:55Z` - Vincent Biret (@baywet) - PR: [chore(main): release 1.1.7](https://github.com/microsoft/kiota-serialization-form-go/pull/156)
- [fix(form): validate sanitized child node index and optimize null node…](https://github.com/microsoft/kiota-serialization-form-go/commit/3d41d7293c413fbdefaf0e8890d4a9499db8d2d8) - `2026-11-09T19:56:28Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(form): return nil for null and whitespace object and collection nodes in FormParseNode](https://github.com/microsoft/kiota-serialization-form-go/pull/164)
- [chore(main): release 1.1.7](https://github.com/microsoft/kiota-serialization-form-go/commit/387c6606c53c3fffceddcaee5e30390b8debd493) - `2026-11-09T19:34:10Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(main): release 1.1.7](https://github.com/microsoft/kiota-serialization-form-go/pull/156)
- [Merge pull request #165 from microsoft/ci/merge-groups](https://github.com/microsoft/kiota-serialization-form-go/commit/7cb2307f09cab432de3850b8a165772590a31d05) - `2026-11-09T18:29:43Z` - Gavin Barron (@gavinbarron) - PR: [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-serialization-form-go/pull/165)

### MicrosoftDocs/dynamics-365-contact-center (6 commit(s), signal 81)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/404395dd8d4aa040ffb9e2a325d8c93591342611) - `2026-11-09T19:06:42Z` - Learn Build Service GitHub App
- [Merge pull request #810 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/83d80b6a807ec0ad8d05d0cac067841bfbc6659e) - `2026-11-09T19:06:19Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add contact-center-ai-shared repository to dependent repositories (#658)](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/53b2903701172fc7097119a7e8fa8636e962a3b8) - `2026-11-09T17:29:59Z` - puneet-singh1 (@puneet-singh1)
- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/cf7ca3749943587200913c9f8fb11dfc8c45839d) - `2026-11-09T13:03:21Z` - Learn Build Service GitHub App
- [Merge pull request #809 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/935802f4c8d4eebedfa2bd6ea380f55e3e4fbe4a) - `2026-11-09T13:02:56Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### MicrosoftDocs/powerapps-docs (6 commit(s), signal 81)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/powerapp…](https://github.com/MicrosoftDocs/powerapps-docs/commit/26953c0d65d08fcc915137b41b71eb35f3aaf44a) - `2026-11-09T19:06:37Z` - Learn Build Service GitHub App
- [Merge pull request #12837 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/powerapps-docs/commit/f70bfbd2663295a4c150fe2b5d5779a1b2ca2b0e) - `2026-11-09T19:03:38Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Elaborate about migration details for Power Apps Vibe (#12835)](https://github.com/MicrosoftDocs/powerapps-docs/commit/a677df55c05c51ba45bb6be50dd3e5ae26a4f491) - `2026-11-09T18:11:57Z` - Jessica Lo (@jessicaszelo)
- [Clarify cascading relationship effects on sync timestamps (#12831)](https://github.com/MicrosoftDocs/powerapps-docs/commit/8638f16ed35aca9fc53d381d37d8a80d6bf8f630) - `2026-11-09T16:35:39Z` - Anirudha Bakore (@anibakore-msft)
- [Update Synapse data lake connection guidance (#12830)](https://github.com/MicrosoftDocs/powerapps-docs/commit/e1d82e0dcbd5379660b64a7e5d3f37f62c7f1717) - `2026-11-09T16:26:14Z` - Anirudha Bakore (@anibakore-msft)

### MicrosoftDocs/dynamics365smb-docs (6 commit(s), signal 81)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/6eb04b2fe92a7e9b7d3b94615b2dcc80a2c6bb09) - `2026-11-09T19:03:45Z` - Learn Build Service GitHub App
- [Merge pull request #5265 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/50dbf2e3db4460f5aef914c90a43730254278a97) - `2026-11-09T19:03:05Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [PBC checklist article update (#5262)](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/d4e445796b4fad7c1a8adcd8c383ad037af26ea3) - `2026-11-09T13:20:22Z` - Brent Holtorf (@brentholtorf)
- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/b63cd10ebe1684ee63b9bc24e5269884e1f3d529) - `2026-11-09T13:03:17Z` - Learn Build Service GitHub App
- [Merge pull request #5263 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/35471f0f046004802de673519ea9fd7c297fd5be) - `2026-11-09T13:02:38Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### microsoftgraph/msgraph-sample-copilot-plugin (6 commit(s), signal 21)

Tags: `bot-only, dependency-noise, product:Microsoft Graph, samples, watchlist`

- [Merge pull request #159 from microsoftgraph/dependabot/nuget/api/Micr…](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/commit/1b083b859cb083edba0f15f6d1aae9e9ee11b5e0) - `2026-11-09T08:26:06Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump Microsoft.Identity.Web from 4.16.1 to 4.18.0](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/pull/159)
- [Bump Microsoft.Identity.Web from 4.16.1 to 4.18.0](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/commit/654f389a75b8e25d1c5628ac072b15a2eb0f82ab) - `2026-11-09T08:25:14Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Identity.Web from 4.16.1 to 4.18.0](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/pull/159)
- [Merge pull request #158 from microsoftgraph/dependabot/nuget/api/Micr…](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/commit/eb0e703b250c84c4d273aea4d82f2da071548976) - `2026-11-09T08:22:27Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump Microsoft.Identity.Web.GraphServiceClient from 4.16.1 to 4.18.0](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/pull/158)
- [Bump Microsoft.Identity.Web.GraphServiceClient from 4.16.1 to 4.18.0](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/commit/afd1df408b739c911c55f82086ce22564202eb20) - `2026-11-09T08:21:32Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Identity.Web.GraphServiceClient from 4.16.1 to 4.18.0](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/pull/158)
- [Merge pull request #157 from microsoftgraph/dependabot/github_actions…](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/commit/af438bb8d66c6b18fdb144a6a17a759e0d3af8ae) - `2026-11-09T08:21:24Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump actions/setup-dotnet from 6.0.0 to 6.1.0](https://github.com/microsoftgraph/msgraph-sample-copilot-plugin/pull/157)

### Azure/azure-cli-extensions (5 commit(s), signal 130)

Tags: `docs, human-authored, release, release-language, watchlist`

- Release: [azure-iot-ops 2.11.2](https://github.com/Azure/azure-cli-extensions/releases/tag/azure-iot-ops-2.11.2) - `2026-11-09T22:44:40Z`
- Release: [azure-iot 1.1.0b1](https://github.com/Azure/azure-cli-extensions/releases/tag/azure-iot-1.1.0b1) - `2026-11-09T22:42:33Z`
- Release: [azure-iot 1.0.0](https://github.com/Azure/azure-cli-extensions/releases/tag/azure-iot-1.0.0) - `2026-11-09T22:42:30Z`
- [aks-preview: add upgrade readiness insight commands (#10553)](https://github.com/Azure/azure-cli-extensions/commit/0d9287265841875cda1a2849e3ca6aef0b1a1abe) - `2026-11-09T22:51:39Z` - skuchipudi295 (@skuchipudi295) - PR: [aks-preview: add upgrade readiness insight commands](https://github.com/Azure/azure-cli-extensions/pull/10553)
- [Add 2.11.2 support (#10571)](https://github.com/Azure/azure-cli-extensions/commit/bb92a6e0203c2d98834afa187b428f06ec8cd698) - `2026-11-09T22:43:45Z` - Yuelin Zhao (@cheatsheet1999) - PR: [[IoT Ops] Update index.json for extension azure-iot-ops-2.11.2](https://github.com/Azure/azure-cli-extensions/pull/10571)
- [{IoT} Adds IoT extension 1.0.0 and 1.1.0b1 (#10566)](https://github.com/Azure/azure-cli-extensions/commit/510e9b84b3053040433e93ed252e588843bbab2d) - `2026-11-09T22:41:20Z` - Yuelin Zhao (@cheatsheet1999) - PR: [{IoT} Adds IoT extension 1.0.0 and 1.1.0b1](https://github.com/Azure/azure-cli-extensions/pull/10566)
- [[k8s-extension] ChaosStudio built-in role migration and namespace ret…](https://github.com/Azure/azure-cli-extensions/commit/da2acb9c34daa158c774e95a0911458087fde2cf) - `2026-11-09T22:25:00Z` - Frank Li (@franklixuefei) - PR: [[k8s-extension] ChaosStudio built-in role migration and namespace retention (1.9.5)](https://github.com/Azure/azure-cli-extensions/pull/10542)
- [[FileShare] Update to API version 2026-09-01 (#10471)](https://github.com/Azure/azure-cli-extensions/commit/1c11485d529a92fc4088f5c00eb746b854574208) - `2026-11-09T03:00:25Z` - James Lindamood (@jlindamood) - PR: [[FileShare] Update to API version 2026-09-01](https://github.com/Azure/azure-cli-extensions/pull/10471)

### MicrosoftDocs/Advertising (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/Advertis…](https://github.com/MicrosoftDocs/Advertising/commit/9fcda4d704ac49798d0ac2eb19eae2796d7bfca6) - `2026-11-09T19:53:29Z` - Learn Build Service GitHub App
- [Add MessagingRestrictions to Campaign Management docs (#827)](https://github.com/MicrosoftDocs/Advertising/commit/e888e6fc3977194491efc0daab3fa1f565207ba1) - `2026-11-09T19:50:45Z` - Rick Garitta (@rgaritta)
- [General updates  11/9 (#826)](https://github.com/MicrosoftDocs/Advertising/commit/cebb6e0609f1b01b9334a2d7895faba240bc3c10) - `2026-11-09T19:46:34Z` - Rick Garitta (@rgaritta)
- [Merging changes synced from https://github.com/MicrosoftDocs/Advertis…](https://github.com/MicrosoftDocs/Advertising/commit/fba71744f7388fc7450ac46dbaa724d94c953549) - `2026-11-09T16:45:04Z` - Learn Build Service GitHub App
- [Update api-verisoning page (#825)](https://github.com/MicrosoftDocs/Advertising/commit/6e329f2d6ffb87052420a893c09bdcb20a6ee943) - `2026-11-09T16:44:17Z` - Rick Garitta (@rgaritta)

### MicrosoftDocs/dynamics-365-unified-operations-public (5 commit(s), signal 90)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/Dynamics…](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/6736edcbbb46d95074bb60e31288f25cf3a1a422) - `2026-11-09T19:07:00Z` - Learn Build Service GitHub App
- [Merge pull request #22825 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/a2ab00d08ac62a268a34db5c04571b76b50ff3a6) - `2026-11-09T19:04:25Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Hr preboard (#22755)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/93a6882d7049c9aae48f897568e4c0968573c692) - `2026-11-09T13:16:35Z` - twheeloc (@twheeloc)
- [WMA 4.2.3.0 and 4.3.0.0 release schedule and 4.2.3.0 release notes (#…](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/1e863d64e5e846c9a0bab1ee47f278078c937fd5) - `2026-11-09T13:15:54Z` - Pedro Augusto Freitas de Souza (@pedroafsouza)
- [status (#22466)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/1b4cb252c5686e50e4afb5a9ac3a4b6a8eff1579) - `2026-11-09T06:42:15Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### MicrosoftDocs/entra-docs (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/entra-do…](https://github.com/MicrosoftDocs/entra-docs/commit/523f3dd86df8938363d761064d4465c56977c43e) - `2026-11-09T18:39:47Z` - Learn Build Service GitHub App
- [Merge pull request #14842 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/entra-docs/commit/1df024dbac39bf1ef0675c7e7c5cfb9d2d388e42) - `2026-11-09T18:36:18Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #14841 from diegojerezba/diegojerezba-update-main-…](https://github.com/MicrosoftDocs/entra-docs/commit/4f64f286b56305154e22a79a86e04571543bb808) - `2026-11-09T18:25:24Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Remove custom url domain from the prerequisites](https://github.com/MicrosoftDocs/entra-docs/commit/2edbd7758b9b1e344a92e20b10fb8ecbbacfb404) - `2026-11-09T18:06:57Z` - Diego Jerez (@diegojerezba)
- [Update delete info](https://github.com/MicrosoftDocs/entra-docs/commit/c735e4fd4b897577120d0a14a9b59cab9461ab6b) - `2026-11-09T18:00:58Z` - Diego Jerez (@diegojerezba)

### MicrosoftDocs/sql-docs (5 commit(s), signal 90)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/sql-docs…](https://github.com/MicrosoftDocs/sql-docs/commit/c3774345a1c199ac150c8711036a2f4258bd1e9d) - `2026-11-09T18:38:15Z` - Learn Build Service GitHub App
- [Merge pull request #38579 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/sql-docs/commit/b1e7e1d71e3b1c6b8347c254d09ff81c5feee115) - `2026-11-09T18:36:09Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #38578 from dimitri-furman/dfurman/version-read-me…](https://github.com/MicrosoftDocs/sql-docs/commit/90ea4fbacf1d778cf5bb8ce6c3d5f8c6697fc280) - `2026-11-09T17:52:01Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Apply batched suggestions from code review](https://github.com/MicrosoftDocs/sql-docs/commit/85dd1aa9be8e31ac7263f47a9143f9fde1abd960) - `2026-11-09T17:39:13Z` - Dimitri Furman (@dimitri-furman)
- [Update SQL Server transaction locking guide](https://github.com/MicrosoftDocs/sql-docs/commit/3757cf8cef2eecb0d9ac748cf26e863ce92d34a8) - `2026-11-09T17:37:05Z` - Dimitri Furman (@dimitri-furman)

### Azure-Samples/confidential-computing (5 commit(s), signal 45)

Tags: `human-authored, samples`

- [Merge pull request #43 from Azure-Samples:docs-refresh-root-sample-na…](https://github.com/Azure-Samples/confidential-computing/commit/064114cafe9bc8b834211ae8bc72e4b8788264a6) - `2026-11-09T18:34:47Z` - Simon Gallagher (@vinfnet) - PR: [Refresh root README with sample chooser and latest additions](https://github.com/Azure-Samples/confidential-computing/pull/43)
- [Refresh root README with sample chooser and latest additions](https://github.com/Azure-Samples/confidential-computing/commit/a9ce596977db065e79ed972558ad492188870aaf) - `2026-11-09T18:33:05Z` - Simon Gallagher (@sgallagherMS) - PR: [Refresh root README with sample chooser and latest additions](https://github.com/Azure-Samples/confidential-computing/pull/43)
- [Merge pull request #42 from Azure-Samples:azure-container-apps-sample](https://github.com/Azure-Samples/confidential-computing/commit/5a1c4105e782f441b7210bbcaa659875a435f65f) - `2026-11-09T18:24:55Z` - Simon Gallagher (@vinfnet) - PR: [Add confidential Container Apps and native Functions samples](https://github.com/Azure-Samples/confidential-computing/pull/42)
- [Complete confidential Functions deployment and validation guides](https://github.com/Azure-Samples/confidential-computing/commit/3c23da75106bb1c09fd3036a5fc79c732baf8851) - `2026-11-09T18:21:15Z` - Simon Gallagher (@sgallagherMS) - PR: [Add confidential Container Apps and native Functions samples](https://github.com/Azure-Samples/confidential-computing/pull/42)
- [Add confidential Container Apps and native Functions hello-world samples](https://github.com/Azure-Samples/confidential-computing/commit/60bbc83497240be6ea81126d962e5ae5a7869711) - `2026-11-09T15:52:06Z` - Simon Gallagher (@sgallagherMS) - PR: [Add confidential Container Apps and native Functions samples](https://github.com/Azure-Samples/confidential-computing/pull/42)

### MicrosoftDocs/azure-stack-docs (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #4588 from MicrosoftDocs/main639298442687750656syn…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/f076fd893ad7ac84edaa9c52f3b35dda2b282378) - `2026-11-09T18:04:42Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4588)
- [Merging changes synced from https://github.com/MicrosoftDocs/azure-st…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/ebe58fb43e839fc7ebc0f17ea7e3eea353659ad2) - `2026-11-09T18:04:25Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4588)
- [Merge pull request #21994 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-stack-docs/commit/973059eedebab3f0cbf95655249b92c66347518d) - `2026-11-09T18:02:52Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4588)
- [Add .github/copilot-instructions.md (#21984)](https://github.com/MicrosoftDocs/azure-stack-docs/commit/d519ea34c69ffa649b3d106faa7c2b001113cc23) - `2026-11-09T16:56:42Z` - Pavel Shageev (@shageev-msft) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4588)
- [Merge pull request #21977 from kerimhanif/kerimhanif-patch-669931](https://github.com/MicrosoftDocs/azure-stack-docs/commit/538dadef0648aeb238fb83f740815c87391d97a6) - `2026-11-09T07:07:50Z` - prmerger-automator[bot] (@prmerger-automator[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4588)

### microsoft/AZD-for-beginners (5 commit(s), signal 90)

Tags: `human-authored, product:Azure AI, release-language, samples, watchlist`

- [Merge pull request #135 from hyoshioka0128/patch-25](https://github.com/microsoft/AZD-for-beginners/commit/27a133943e1116542df1bc2a954006e01ce24657) - `2026-11-09T16:22:00Z` - Lee Stott (@leestott) - PR: [Update Japanese translation for coordination patterns](https://github.com/microsoft/AZD-for-beginners/pull/135)
- [Merge pull request #136 from hyoshioka0128/patch-26](https://github.com/microsoft/AZD-for-beginners/commit/326f9d323c39600d14b86bb2456c15bf04e2699c) - `2026-11-09T16:21:47Z` - Lee Stott (@leestott) - PR: [Translate pre-deployment checks document to Japanese](https://github.com/microsoft/AZD-for-beginners/pull/136)
- [Merge pull request #137 from hyoshioka0128/patch-27](https://github.com/microsoft/AZD-for-beginners/commit/4f5ad9f76811ba2bc5482f2150f99136b5151f57) - `2026-11-09T16:21:34Z` - Lee Stott (@leestott) - PR: [Update disclaimer for Co-op Translator in Japanese translation](https://github.com/microsoft/AZD-for-beginners/pull/137)
- [Merge pull request #138 from microsoft/leestott-foundry-ga-update](https://github.com/microsoft/AZD-for-beginners/commit/256e94af02dc98df03fa5fa7a1fe0f922b67611c) - `2026-11-09T16:20:52Z` - Lee Stott (@leestott) - PR: [docs: Microsoft Foundry 1.0 GA is now live](https://github.com/microsoft/AZD-for-beginners/pull/138)
- [docs: update course for live Microsoft Foundry GA release](https://github.com/microsoft/AZD-for-beginners/commit/90182e9af8908894e2a53e949b02d18738124da9) - `2026-11-09T16:19:12Z` - Lee Stott (@leestott) - PR: [docs: Microsoft Foundry 1.0 GA is now live](https://github.com/microsoft/AZD-for-beginners/pull/138)

### dotnet/msbuild (5 commit(s), signal 45)

Tags: `docs, human-authored`

- [Localized file check-in by OneLocBuild Task: Build definition ID 9434…](https://github.com/dotnet/msbuild/commit/33c935576266a2a5711480c81b73192e8226988e) - `2026-11-09T13:19:23Z` - dotnet-oneloc-localization[bot] (@dotnet-oneloc-localization[bot]) - PR: [Localized file check-in by OneLocBuild Task: Build definition ID 9434: Build ID 15966680](https://github.com/dotnet/msbuild/pull/15477)
- [[main] Update dependencies from dotnet/arcade (#15443)](https://github.com/dotnet/msbuild/commit/3ccc609d30cd264f2d523f06370da214b115769a) - `2026-11-09T12:59:23Z` - dotnet-maestro[bot] (@dotnet-maestro[bot]) - PR: [[main] Update dependencies from dotnet/arcade](https://github.com/dotnet/msbuild/pull/15443)
- [Update ngenPriority to 3 for Microsoft.VisualStudio.Telemetry.dll (#1…](https://github.com/dotnet/msbuild/commit/000166da7c4003e0c4bca1b3e8856bedee3d98d7) - `2026-11-09T12:22:31Z` - Jan Provazník (@JanProvaznik) - PR: [Update ngenPriority to 3 for Microsoft.VisualStudio.Telemetry.dll](https://github.com/dotnet/msbuild/pull/15499)
- [Fix skipped target hooks in out-of-process builds (#15482)](https://github.com/dotnet/msbuild/commit/82b38802705ffaa4d186c971564ec854b0d5afad) - `2026-11-09T09:58:01Z` - Andrew Arnott (@AArnott) - PR: [Fix skipped target hooks in out-of-process builds](https://github.com/dotnet/msbuild/pull/15482)
- [Align PAT validation with dotnet/core (#15493)](https://github.com/dotnet/msbuild/commit/861dd2e77aae7b27a456d47ac8d32d4366b7546f) - `2026-11-09T09:53:46Z` - Jeff Handley (@jeffhandley) - PR: [Align PAT validation with dotnet/core](https://github.com/dotnet/msbuild/pull/15493)

### microsoft/kiota-dotnet (4 commit(s), signal 79)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [fix(serialization-form): handle non-boolean and invalid primitives sa…](https://github.com/microsoft/kiota-dotnet/commit/6d2e8a072f0f1db8ce632c71c40a802a55b2e809) - `2026-11-09T20:30:44Z` - Hardik K (@hardikkaurani) - PR: [fix(serialization-form): handle non-boolean and invalid primitives safely in FormParseNode](https://github.com/microsoft/kiota-dotnet/pull/850)
- [fix(serialization-text): defensive byte array and timespan parsing in…](https://github.com/microsoft/kiota-dotnet/commit/3833f1b25cb5c943a7f2786432fd543f85477ad2) - `2026-11-09T20:23:46Z` - Hardik K (@hardikkaurani) - PR: [fix(serialization-text): defensive byte array and timespan parsing in TextParseNode](https://github.com/microsoft/kiota-dotnet/pull/855)
- [build(deps): bump actions/setup-dotnet from 6.0.0 to 6.1.0 (#857)](https://github.com/microsoft/kiota-dotnet/commit/c32de0c99917bc1570430c6d56ba9a4dca6653f6) - `2026-11-09T10:21:07Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump actions/setup-dotnet from 6.0.0 to 6.1.0](https://github.com/microsoft/kiota-dotnet/pull/857)
- [Bump Std.UriTemplate from 2.0.12 to 2.0.13 (#858)](https://github.com/microsoft/kiota-dotnet/commit/504861a545378ee229d33194c973d4e0a8308fc5) - `2026-11-09T10:20:31Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Std.UriTemplate from 2.0.12 to 2.0.13](https://github.com/microsoft/kiota-dotnet/pull/858)

### microsoft/kiota-typescript (4 commit(s), signal 79)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [auto dependabot: bump tsc-alias from 1.9.9 to 1.9.10 (#2220)](https://github.com/microsoft/kiota-typescript/commit/2212b23a859e72d989cb1471d2e17b3ea7aff6c5) - `2026-11-09T20:09:16Z` - dependabot[bot] (@dependabot[bot]) - PR: [auto dependabot: bump tsc-alias from 1.9.9 to 1.9.10](https://github.com/microsoft/kiota-typescript/pull/2220)
- [auto dependabot: bump @microsoft/sp-http from 1.24.0 to 1.24.1 (#2221)](https://github.com/microsoft/kiota-typescript/commit/6f0e2192e0f965b186faead3beb04b47d4af7a4c) - `2026-11-09T20:09:13Z` - dependabot[bot] (@dependabot[bot]) - PR: [auto dependabot: bump @microsoft/sp-http from 1.24.0 to 1.24.1](https://github.com/microsoft/kiota-typescript/pull/2221)
- [auto dependabot: bump tslib from 2.8.1 to 2.9.1 (#2222)](https://github.com/microsoft/kiota-typescript/commit/27c0d7cba482ff5790a4f46aebd53ae64cd3b677) - `2026-11-09T20:09:10Z` - dependabot[bot] (@dependabot[bot]) - PR: [auto dependabot: bump tslib from 2.8.1 to 2.9.1](https://github.com/microsoft/kiota-typescript/pull/2222)
- [ci: run required TypeScript checks for merge groups (#2223)](https://github.com/microsoft/kiota-typescript/commit/855599feaa14bfe7d0a8db3da16fbcccab399af5) - `2026-11-09T18:37:13Z` - Vincent Biret (@baywet) - PR: [ci: run required TypeScript checks for merge groups](https://github.com/microsoft/kiota-typescript/pull/2223)

### microsoft/kiota-http-go (4 commit(s), signal 129)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [v1.6.1](https://github.com/microsoft/kiota-http-go/releases/tag/v1.6.1) - `2026-11-09T19:58:37Z`
- [Merge pull request #299 from microsoft/release-please--branches--main…](https://github.com/microsoft/kiota-http-go/commit/40d41a50cdfee2d104e9f9b6eca12af04db797e9) - `2026-11-09T19:56:17Z` - Vincent Biret (@baywet) - PR: [chore(main): release 1.6.1](https://github.com/microsoft/kiota-http-go/pull/299)
- [chore(main): release 1.6.1](https://github.com/microsoft/kiota-http-go/commit/3a4d3006ec86505666a143a32ac5aa955b9e171f) - `2026-11-09T19:26:48Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(main): release 1.6.1](https://github.com/microsoft/kiota-http-go/pull/299)
- [Merge pull request #306 from microsoft/ci/merge-groups](https://github.com/microsoft/kiota-http-go/commit/4e1d42554c4231d025f4dd3f3748aa332e7e608b) - `2026-11-09T18:27:49Z` - Gavin Barron (@gavinbarron) - PR: [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-http-go/pull/306)
- [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-http-go/commit/cdf39ab87fe52e4c42f0294cdeb4457ef4d631eb) - `2026-11-09T13:00:25Z` - Vincent Biret (@baywet) - PR: [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-http-go/pull/306)

### MicrosoftDocs/power-platform (4 commit(s), signal 79)

Tags: `docs, human-authored, product:Azure AI, product:PowerShell, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/7506d9d6cd083ee805ca7e0672e010b91e2d729d) - `2026-11-09T19:04:41Z` - Learn Build Service GitHub App
- [Merge pull request #12165 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-platform/commit/8400fcabbdf67e400319c4edf176958465380597) - `2026-11-09T19:03:12Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add multilingual self service agent reference architecture (#12163)](https://github.com/MicrosoftDocs/power-platform/commit/7fc78075f0015bc13df070b962566af9e7e4ee2f) - `2026-11-09T17:25:28Z` - Jeanne Haskett (@jhaskett-msft)
- [Architecture Center: reference architecture for building a regulatory…](https://github.com/MicrosoftDocs/power-platform/commit/dec3207fa5b2c94f622f8fb88d19bdd98bdd0664) - `2026-11-09T14:40:34Z` - Manuela Pichler (@manuelap-msft)

### Azure/AI-Landing-Zones (4 commit(s), signal 79)

Tags: `docs, human-authored, watchlist`

- [docs: publish inline visuals highlights for v7.3.0](https://github.com/Azure/AI-Landing-Zones/commit/570d29dbb70e323f428d41b31c1cde88ec68a416) - `2026-11-09T00:35:42Z` - Paulo Lacerda (@placerda)
- [Merge pull request #178 from Azure/feature/inline-visual-output-docs](https://github.com/Azure/AI-Landing-Zones/commit/0d1f658e7c435373795212a9bdb9a29270b200b1) - `2026-11-09T00:26:25Z` - Paulo Lacerda (@placerda) - PR: [docs: add inline visuals guide and diagram](https://github.com/Azure/AI-Landing-Zones/pull/178)
- [docs: refresh validated planner prices](https://github.com/Azure/AI-Landing-Zones/commit/979a35da0f28269db74182694c93a959fc2e653a) - `2026-11-09T00:25:20Z` - github-actions[bot] (@github-actions[bot])
- [Fix UI test setup and responsive documentation checks](https://github.com/Azure/AI-Landing-Zones/commit/1bc229ae58d82c857eb8eb574e83365f81a6834d) - `2026-11-08T23:04:37Z` - Paulo Lacerda (@placerda) - PR: [docs: add inline visuals guide and diagram](https://github.com/Azure/AI-Landing-Zones/pull/178)

### MicrosoftLearning/mslearn-devops (4 commit(s), signal 79)

Tags: `human-authored, product:Azure AI, product:PowerShell, training, watchlist`

- [Merge pull request #51 from MicrosoftLearning/fix/49-cosmos-initializ…](https://github.com/MicrosoftLearning/mslearn-devops/commit/2b83944a6e5a3e424b67becd41199db53b0f3ecc) - `2026-11-08T18:58:33Z` - Peter De Tender (@petender) - PR: [Fix Cosmos provisioning, initialization retries, and health checks](https://github.com/MicrosoftLearning/mslearn-devops/pull/51)
- [Fix Cosmos provisioning and initialization for SRE lab](https://github.com/MicrosoftLearning/mslearn-devops/commit/fc631197b7f8ce724d165d68705dd6f1c9b2f932) - `2026-11-08T18:57:30Z` - Peter De Tender (@petender) - PR: [Fix Cosmos provisioning, initialization retries, and health checks](https://github.com/MicrosoftLearning/mslearn-devops/pull/51)
- [Merge pull request #50 from MicrosoftLearning/pdt-ado-copilot-cli](https://github.com/MicrosoftLearning/mslearn-devops/commit/697563c20e5b00736c60b72d7228399750b334c7) - `2026-11-08T18:31:17Z` - Peter De Tender (@petender) - PR: [extract agentic-iac-lab-files to folder as backup for zip not working](https://github.com/MicrosoftLearning/mslearn-devops/pull/50)
- [extract agentic-iac-lab-files to folder as backup for zip not working](https://github.com/MicrosoftLearning/mslearn-devops/commit/9a032a95304f79dc4f1e05408c5f27522ccd4a39) - `2026-11-08T18:30:23Z` - Peter De Tender (@petender) - PR: [extract agentic-iac-lab-files to folder as backup for zip not working](https://github.com/MicrosoftLearning/mslearn-devops/pull/50)

### Azure/data-api-builder (3 commit(s), signal 103)

Tags: `docs, human-authored, security, watchlist`

- [Update HotChocolate packages to 16.7.3 (#3902)](https://github.com/Azure/data-api-builder/commit/9f9b79ee7dbe2ac26bf720a591473e20891fe07b) - `2026-11-09T23:03:19Z` - Tobias Tengler (@tobias-tengler) - PR: [Update HotChocolate packages to 16.7.3](https://github.com/Azure/data-api-builder/pull/3902)
- [Fix protected-field leaks in SQL pagination cursors (#3898)](https://github.com/Azure/data-api-builder/commit/bc4e979f0feb216dc33fcb8012f4d3ac43a4efbe) - `2026-11-09T16:41:23Z` - Souvik Ghosh (@souvikghosh04) - PR: [Fix protected-field leaks in SQL pagination cursors](https://github.com/Azure/data-api-builder/pull/3898)
- [Enable secretless OBO authentication in DAB using Workload Identity F…](https://github.com/Azure/data-api-builder/commit/e92b02ecbc91800fff8d1131cb0ee1ed028cbcd4) - `2026-11-09T13:40:40Z` - Mohit G (@gmohit21) - PR: [Enable secretless OBO authentication in DAB using Workload Identity Federation](https://github.com/Azure/data-api-builder/pull/3880)

### Azure/azure-sdk-for-rust (3 commit(s), signal 128)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [azure_storage_blob@1.2.0-beta.1](https://github.com/Azure/azure-sdk-for-rust/releases/tag/azure_storage_blob%401.2.0-beta.1) - `2026-11-09T21:03:51Z`
- Release: [azure_storage_sas@1.1.0-beta.1](https://github.com/Azure/azure-sdk-for-rust/releases/tag/azure_storage_sas%401.1.0-beta.1) - `2026-11-09T21:03:41Z`
- Release: [azure_storage_common@1.1.0-beta.1](https://github.com/Azure/azure-sdk-for-rust/releases/tag/azure_storage_common%401.1.0-beta.1) - `2026-11-09T21:03:32Z`
- [[Storage] Bump versions after STG105 release (#5581)](https://github.com/Azure/azure-sdk-for-rust/commit/4d6512825ffcc5c2ef1c7d2b89bc0e8369dfef61) - `2026-11-09T22:51:56Z` - vincenttran-msft (@vincenttran-msft) - PR: [[Storage] Bump versions after STG105 release](https://github.com/Azure/azure-sdk-for-rust/pull/5581)
- [[Storage] Prep `main` for STG105 beta release (#5575)](https://github.com/Azure/azure-sdk-for-rust/commit/6292988ccca95760f1383e908aa7c7a50b91781a) - `2026-11-09T20:08:40Z` - vincenttran-msft (@vincenttran-msft) - PR: [[Storage] Prep `main` for STG105 beta release](https://github.com/Azure/azure-sdk-for-rust/pull/5575)
- [Add unified Cosmos read-many operations (#5385)](https://github.com/Azure/azure-sdk-for-rust/commit/abb97735bf84fd27acd0b57b60d260b2e482b806) - `2026-11-09T19:06:32Z` - Tomas Varon (@tvaron3) - PR: [Add unified Cosmos read-many operations](https://github.com/Azure/azure-sdk-for-rust/pull/5385)

### Azure/dacs (3 commit(s), signal 88)

Tags: `human-authored, release-language, samples, watchlist`

- [build(deps): bump the docker group across 2 directories with 3 updates](https://github.com/Azure/dacs/commit/102101d6fbe54bb20116032ba494fb14f2baea91) - `2026-11-09T22:27:26Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump the docker group across 2 directories with 3 updates](https://github.com/Azure/dacs/pull/174)
- [fix(ci): derive safe development versions from release tags](https://github.com/Azure/dacs/commit/6347b745be8cbb2dca1ed7c218bd473430e11dde) - `2026-11-09T20:02:11Z` - Joshua Long (@jmclong) - PR: [fix(ci): distinguish non-tag builds at release commits](https://github.com/Azure/dacs/pull/170)
- [docs: document PyPI client and add stable release badge](https://github.com/Azure/dacs/commit/bfeffa05660d4dce8ca708dbbf2f9b408763fd1c) - `2026-11-09T14:18:14Z` - Joshua Long (@jmclong) - PR: [docs: document PyPI client and add stable release badge](https://github.com/Azure/dacs/pull/173)

### microsoft/BuildXL (3 commit(s), signal 53)

Tags: `human-authored, release-language, samples`

- [Merged PR 973439: Remove unused helpers and file generator](https://github.com/microsoft/BuildXL/commit/d47a95af300f403cdc9eea3d8e8927db38d80549) - `2026-11-09T21:42:48Z` - Michael Pysson (@mpysson)
- [Merged PR 973015: Remove BasicFilesystem from Engine.Cache NuGet package](https://github.com/microsoft/BuildXL/commit/314ae78a5708d293fa67edcf85a91881fb5bae19) - `2026-11-09T20:21:32Z` - Michael Pysson (@mpysson)
- [Merged PR 973361: Update BuildXL LKG Version to 0.1.0-20261108.1](https://github.com/microsoft/BuildXL/commit/29fe489d75b93b6d20076bc1ad57290e10b1b498) - `2026-11-09T18:32:38Z` - BuildXL-Pipelines

### microsoft/TypeAgent (3 commit(s), signal 78)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [ci: upload fork CodeQL results to the verified PR commit (#3274)](https://github.com/microsoft/TypeAgent/commit/dd09a04a29366af2faf3affc6b33fd2b17de7834) - `2026-11-09T20:59:53Z` - Hillary Mutisya (@hillary-mutisya) - PR: [ci: upload fork CodeQL results to the verified PR commit](https://github.com/microsoft/TypeAgent/pull/3274)
- [memory: add source-grounded procedural view examples (#3273)](https://github.com/microsoft/TypeAgent/commit/5b40c973375705d5f7e302131ba99bd0aae5c6a6) - `2026-11-09T19:18:57Z` - Hillary Mutisya (@hillary-mutisya)
- [Enhance validation examples and improve index-retry diagnostics (#3272)](https://github.com/microsoft/TypeAgent/commit/f1bd7da449d30854c649cff067b58ac73bfe6bdb) - `2026-11-09T03:44:36Z` - Hillary Mutisya (@hillary-mutisya) - PR: [Enhance validation examples and improve index-retry diagnostics](https://github.com/microsoft/TypeAgent/pull/3272)

### MicrosoftDocs/cloud-adoption-framework (3 commit(s), signal 88)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/cloud-ad…](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/d9d5da6c8fb0baa3c2447464bfd1eef7f2a0bfda) - `2026-11-09T20:57:57Z` - Learn Build Service GitHub App
- [Merge pull request #7435 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/b0a7302cc75af741db87c25796b5f829c5d7c118) - `2026-11-09T20:56:52Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Remove the preview label from Azure Monitor health models (#7434)](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/c2868ffdc52d9474c9b4ea23a484619e8205eef6) - `2026-11-09T20:54:08Z` - Marie Halloran (@mariehalloran)

### microsoft/forge-lab (3 commit(s), signal 113)

Tags: `human-authored, release-language, security, training, watchlist`

- [Sync Rust article wording with the published Security Blog](https://github.com/microsoft/forge-lab/commit/4438373672e014bead76885633c4e5e8470a1e51) - `2026-11-09T20:38:58Z` - Cen Zhang (@occia)
- [Style Rust open-issues note as a boxed callout](https://github.com/microsoft/forge-lab/commit/f22be6029b11e245ce398c2c680e9172bf6058e4) - `2026-11-09T20:02:45Z` - Taesoo Kim
- [release rust-std-memory-safety](https://github.com/microsoft/forge-lab/commit/55b9a3953caf8731d2e1cdda33c31f0487e139ee) - `2026-11-09T17:59:02Z` - Taesoo Kim

### Azure/azure-sdk-for-go (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Sync eng/common directory with azure-sdk-tools for PR 17441 (#27974)](https://github.com/Azure/azure-sdk-for-go/commit/aaa0d8c739c27600745a9b8f4c11c2651d1da910) - `2026-11-09T20:34:00Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17441](https://github.com/Azure/azure-sdk-for-go/pull/27974)
- [Storage/stg105 all (#27871)](https://github.com/Azure/azure-sdk-for-go/commit/a18c09737e272d0e3f69dcfa272a6cdd76ddfb49) - `2026-11-09T15:13:23Z` - gunjansingh-msft (@gunjansingh-msft) - PR: [Storage/stg105 all](https://github.com/Azure/azure-sdk-for-go/pull/27871)
- [Upgrade Go emitter to 0.18.0 (#27982)](https://github.com/Azure/azure-sdk-for-go/commit/b2450a2f4cd57997faae4d24605f081ad347ac6c) - `2026-11-09T00:12:27Z` - Copilot (@Copilot) - PR: [Upgrade Go emitter to 0.18.0](https://github.com/Azure/azure-sdk-for-go/pull/27982)

### microsoft/kiota-serialization-text-go (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #190 from hardikkaurani/fix/strip-utf8-byte-order-…](https://github.com/microsoft/kiota-serialization-text-go/commit/f8272d4b471adef4182e6c75cbb59081fe71e0fa) - `2026-11-09T20:09:27Z` - Vincent Biret (@baywet) - PR: [fix(text): strip UTF-8 byte order mark during parse node initialization](https://github.com/microsoft/kiota-serialization-text-go/pull/190)
- [Merge pull request #191 from microsoft/ci/merge-groups](https://github.com/microsoft/kiota-serialization-text-go/commit/86a8feadbcc7f1386c9ebc047277a98c718e256b) - `2026-11-09T18:32:07Z` - Gavin Barron (@gavinbarron) - PR: [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-serialization-text-go/pull/191)
- [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-serialization-text-go/commit/2bb805c9de1c34e56f4a74f6d3b2716a8201dafb) - `2026-11-09T12:59:59Z` - Vincent Biret (@baywet) - PR: [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-serialization-text-go/pull/191)

### MicrosoftDocs/dynamics365smb-devitpro-pb (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/7a8f426815c5929226ba385fb5524a741fee23f4) - `2026-11-09T19:04:04Z` - Learn Build Service GitHub App
- [Merge pull request #8146 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/5b07219e60d9de73634c07f0b9e626b4184de063) - `2026-11-09T19:03:08Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Freshness (#8138)](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/d12aeed596144d2eb03c14591b76619c7bb025f9) - `2026-11-09T13:07:22Z` - Susanne Windfeld Pedersen (@SusanneWindfeldPedersen)

### microsoft/kiota-java (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #2240 from microsoft/copilot/merge-group-java-2026…](https://github.com/microsoft/kiota-java/commit/f96d8bc5d29f046f7047e936e78cc1898ae4c3c3) - `2026-11-09T18:36:09Z` - Gavin Barron (@gavinbarron) - PR: [ci: run required workflows for merge groups](https://github.com/microsoft/kiota-java/pull/2240)
- [ci: use plain merge group triggers](https://github.com/microsoft/kiota-java/commit/39513fdf047e8360b4979aaabb8534a9cfb70d3e) - `2026-11-09T14:56:34Z` - Vincent Biret (@baywet) - PR: [ci: run required workflows for merge groups](https://github.com/microsoft/kiota-java/pull/2240)
- [ci: run required workflows for merge groups](https://github.com/microsoft/kiota-java/commit/0f66563d1c1432c1126ea8bfc2bbf882d19b961b) - `2026-11-09T14:43:48Z` - Vincent Biret (@baywet) - PR: [ci: run required workflows for merge groups](https://github.com/microsoft/kiota-java/pull/2240)

### MicrosoftDocs/azure-docs-sdk-cpp (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-cpp/commit/6f1af6765e5c02370394aa2953ebffbe460314cd) - `2026-11-09T18:06:53Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-cpp/commit/b5b42da612d2a5a014064101f248426151a88e55) - `2026-11-09T18:06:24Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-cpp/commit/a4853c554b6881d0d102e1253c3d6a7fa5c01ac8) - `2026-11-09T15:49:14Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/azure-docs-sdk-node (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/04d4b8e2d28c92c57a5a611a219e83b684ce3e0b) - `2026-11-09T17:54:36Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/63104e8e9f0e11ae3cc3d1981692ceba4bfceca3) - `2026-11-09T09:13:26Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/7921a7371b69fa495a85a53e63da3ed73d4617c1) - `2026-11-08T17:38:25Z` - azure-sdk (@azure-sdk)

### microsoft/MCAPSTechConnect26-LAB483 (3 commit(s), signal 113)

Tags: `human-authored, product:Azure SDK, release-language, security, training, watchlist`

- [Fix alert message location in build instructions](https://github.com/microsoft/MCAPSTechConnect26-LAB483/commit/526980b9e7182a71f6a17619807f4caf3e84716a) - `2026-11-09T16:28:01Z` - TristianWilliams-skillable (@TristianWilliams-skillable)
- [Revise security pop-up instructions in build guide](https://github.com/microsoft/MCAPSTechConnect26-LAB483/commit/3e006776e35773d669d87862f1931637c8b11ffe) - `2026-11-09T16:24:48Z` - TristianWilliams-skillable (@TristianWilliams-skillable)
- [Update Teams manifest to version 1.25](https://github.com/microsoft/MCAPSTechConnect26-LAB483/commit/d2f0bfb920c66ee4c7ec330be0e216cb4bdb5ccf) - `2026-11-09T15:28:33Z` - TristianWilliams-skillable (@TristianWilliams-skillable)

### MicrosoftDocs/visualstudio-docs (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #11488 from MicrosoftDocs/main639298372433359022sy…](https://github.com/MicrosoftDocs/visualstudio-docs/commit/c909850af2bb99ced29df945b90659905edf8614) - `2026-11-09T16:07:40Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11488)
- [Merging changes synced from https://github.com/MicrosoftDocs/visualst…](https://github.com/MicrosoftDocs/visualstudio-docs/commit/2a410133d5b438994038f4ff963b534cbc4a2cd9) - `2026-11-09T16:07:20Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11488)
- [Merge pull request #15805 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/visualstudio-docs/commit/5c3ff2bbf22f040834eba2d1798c0aeb1ca12708) - `2026-11-09T16:04:41Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11488)

### MicrosoftDocs/azure-monitor-docs (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #5767 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/80bfe78762e50763672fe95ba50ffd70b3b94a75) - `2026-11-09T13:03:27Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #5766 from moti-ba/docs/table-schema-cdc-links](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/09430a7d34ae488c0a775813b4196be060b50dfa) - `2026-11-09T11:52:05Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [docs: link custom event table references to custom data collection](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/0a83f4216e1a534b892bf7f742e20e71fb5d6f96) - `2026-11-09T11:45:50Z` - Moti Bani (@MotiBani)

### microsoft/voice-agent (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure AI, product:Azure SDK, watchlist`

- [Merge pull request #119 from niuzheng168/main](https://github.com/microsoft/voice-agent/commit/a7dd0da828d1dec8a7ad089dceafa5aedff30ab5) - `2026-11-09T09:02:33Z` - Yulin Li (@yulin-li) - PR: [Update GPT Live samples to Projects SDK 2.11.0 with greetings, structured inputs, and client delegation](https://github.com/microsoft/voice-agent/pull/119)
- [Add typed messages to the GPT Live samples](https://github.com/microsoft/voice-agent/commit/878405e186f6bc57f9d81ab01d5e3224ae861082) - `2026-11-09T06:54:32Z` - Zheng Niu - PR: [Update GPT Live samples to Projects SDK 2.11.0 with greetings, structured inputs, and client delegation](https://github.com/microsoft/voice-agent/pull/119)
- [Update GPT Live samples to Projects SDK 2.11.0 with greetings, struct…](https://github.com/microsoft/voice-agent/commit/546d7f652b49c153af7493ec532bb6a8e793373f) - `2026-11-09T04:56:28Z` - Zheng Niu - PR: [Update GPT Live samples to Projects SDK 2.11.0 with greetings, structured inputs, and client delegation](https://github.com/microsoft/voice-agent/pull/119)

### microsoft/mcp-dotnet-samples (3 commit(s), signal 43)

Tags: `human-authored, samples`

- [Update metadata.json](https://github.com/microsoft/mcp-dotnet-samples/commit/6d56137fba72e93012858be519943fcab63d1b68) - `2026-11-09T03:12:22Z` - GitHub Actions (@actions-user)
- [Update metadata.json](https://github.com/microsoft/mcp-dotnet-samples/commit/9bda9dadc0ce84c16e0293f0dcddd54513a66e77) - `2026-11-09T02:13:35Z` - GitHub Actions (@actions-user)
- [Update metadata.json](https://github.com/microsoft/mcp-dotnet-samples/commit/c6f68793a8e4c95eb6ccedcee09ad6504a44cfa5) - `2026-11-09T00:27:03Z` - GitHub Actions (@actions-user)

### microsoft/bobsql (3 commit(s), signal 53)

Tags: `human-authored, release-language, samples`

- [Merge pull request #8 from microsoft/sqlversioning-presentation-apps](https://github.com/microsoft/bobsql/commit/a8add788269bb02113094f7994fea8ad4f4087bb) - `2026-11-08T17:57:22Z` - Bob Ward (@rgward) - PR: [Add SQL versioning presentation apps and named demo folders](https://github.com/microsoft/bobsql/pull/8)
- [Create bobsql.code-workspace](https://github.com/microsoft/bobsql/commit/182467510d27869fdb1b9c5fa731779db13fe403) - `2026-11-08T17:53:06Z` - Bob Ward (@rgward) - PR: [Add SQL versioning presentation apps and named demo folders](https://github.com/microsoft/bobsql/pull/8)
- [Add SQL versioning presentation apps and named demo folders](https://github.com/microsoft/bobsql/commit/04260d4ec7ecb67393c3ad045291ec4bca44e2a9) - `2026-11-08T17:07:24Z` - Bob Ward (@rgward) - PR: [Add SQL versioning presentation apps and named demo folders](https://github.com/microsoft/bobsql/pull/8)

### microsoft/WindowsAppSDK (2 commit(s), signal 87)

Tags: `docs, human-authored, product:Azure AI, product:Azure SDK, release-language, watchlist`

- [Consume the monobuild binary version (#6881)](https://github.com/microsoft/WindowsAppSDK/commit/587f406d512702b9c1694ff39eae82ce03949eba) - `2026-11-09T22:39:57Z` - Scott Jones (@Scottj1s) - PR: [Consume the monobuild binary version](https://github.com/microsoft/WindowsAppSDK/pull/6881)
- [Add VS Code debug config and AGENTS.md to WinUI 3 app templates (#6866)](https://github.com/microsoft/WindowsAppSDK/commit/02d63449632312c0168a5bc0475a58c714601991) - `2026-11-09T20:10:07Z` - Chiara Mooney (@chiaramooney) - PR: [Add VS Code debug config and AGENTS.md to WinUI 3 app templates](https://github.com/microsoft/WindowsAppSDK/pull/6866)

### microsoft/winget-cli (2 commit(s), signal 77)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Remove old workflows (#6668)](https://github.com/microsoft/winget-cli/commit/7de3b02def71f06e43cda719d52bc379c00e9021) - `2026-11-09T22:24:27Z` - JohnMcPMS (@JohnMcPMS) - PR: [Remove old workflows](https://github.com/microsoft/winget-cli/pull/6668)
- [Move to manual vcpkg install to avoid spurious failures (#6662)](https://github.com/microsoft/winget-cli/commit/ec4a0a698db5d9c986b3a15d032da9b9236b2d7d) - `2026-11-09T22:23:47Z` - JohnMcPMS (@JohnMcPMS) - PR: [Move to manual vcpkg install to avoid spurious failures](https://github.com/microsoft/winget-cli/pull/6662)

### OfficeDev/microsoft-teams-library-js (2 commit(s), signal 87)

Tags: `docs, human-authored, release-language, watchlist`

- [Fix release pipelines failing at 'View Published Package URLs' (stale…](https://github.com/OfficeDev/microsoft-teams-library-js/commit/59d3330606f1c673e5f993763ebf6aa98b34ef52) - `2026-11-09T21:46:28Z` - Patrick Latter (@palatter) - PR: [Fix release pipelines failing at 'View Published Package URLs' (stale artifact path)](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3187)
- [Add read-only release checks to the release-teamsjs skill (#3200)](https://github.com/OfficeDev/microsoft-teams-library-js/commit/92b97acda3c78e2e71c0452c7d7156e6dd7a0d8c) - `2026-11-09T20:06:07Z` - Patrick Latter (@palatter) - PR: [Add read-only release checks to the release-teamsjs skill](https://github.com/OfficeDev/microsoft-teams-library-js/pull/3200)

### MicrosoftDocs/msteams-docs (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure AI, product:Azure SDK, watchlist`

- [Add new page for ABS agent auth config (#14569)](https://github.com/MicrosoftDocs/msteams-docs/commit/37874ab9af5385105d894c729394a516159dc543) - `2026-11-09T20:56:04Z` - Nick Walker (@nickwalkmsft) - PR: [Add new page for ABS agent auth config](https://github.com/MicrosoftDocs/msteams-docs/pull/14569)
- [SDK docs migration (quick) (#14712)](https://github.com/MicrosoftDocs/msteams-docs/commit/3a2e8e1c5c9e67a96d6762ac89bc50d2549d5708) - `2026-11-09T20:29:08Z` - Nick Walker (@nickwalkmsft) - PR: [SDK docs migration (quick)](https://github.com/MicrosoftDocs/msteams-docs/pull/14712)

### MicrosoftDocs/azure-docs-sdk-java (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/24d4eddc708eb03349376adcfa804f31c9f4e549) - `2026-11-09T20:32:32Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/acffad0da612ff89558ab2b8c6d6ac91e43f2622) - `2026-11-09T18:32:43Z` - azure-sdk (@azure-sdk)

### Azure-Samples/modernize-bootcamp (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Merge pull request #99 from Azure-Samples/sojorgensen/rewordinglabs](https://github.com/Azure-Samples/modernize-bootcamp/commit/03ef31fbcd1c1838e450ded66921512c3ac7b1c1) - `2026-11-09T19:53:45Z` - Sophie Jorgensen (@sophiejorgensen) - PR: [Remove obsolete lab instructions and NSG image](https://github.com/Azure-Samples/modernize-bootcamp/pull/99)
- [Remove obsolete lab instructions and NSG image](https://github.com/Azure-Samples/modernize-bootcamp/commit/ff1dcaf0f5d8302a224f8e0baf4e13e9c452fbb7) - `2026-11-09T19:49:22Z` - Sophie Jorgensen - PR: [Remove obsolete lab instructions and NSG image](https://github.com/Azure-Samples/modernize-bootcamp/pull/99)

### microsoft/kiota-serialization-multipart-go (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #148 from microsoft/ci/merge-groups](https://github.com/microsoft/kiota-serialization-multipart-go/commit/4ea989d485f0372485c152e3d354482f7a8ee597) - `2026-11-09T18:31:48Z` - Gavin Barron (@gavinbarron) - PR: [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-serialization-multipart-go/pull/148)
- [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-serialization-multipart-go/commit/c9d88a34bbd912a67ab47338c7aea8b17029e1ba) - `2026-11-09T12:59:59Z` - Vincent Biret (@baywet) - PR: [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-serialization-multipart-go/pull/148)

### microsoft/kiota-serialization-json-go (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #233 from microsoft/ci/merge-groups](https://github.com/microsoft/kiota-serialization-json-go/commit/5b1e9b006ca034b94f3350cda804e1296e4b787c) - `2026-11-09T18:30:35Z` - Gavin Barron (@gavinbarron) - PR: [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-serialization-json-go/pull/233)
- [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-serialization-json-go/commit/10bc9a5f99b0dd95583191937dcbbefa6d722bba) - `2026-11-09T13:00:03Z` - Vincent Biret (@baywet) - PR: [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-serialization-json-go/pull/233)

### microsoft/kiota-authentication-azure-go (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #250 from microsoft/ci/merge-groups](https://github.com/microsoft/kiota-authentication-azure-go/commit/816de2d7c54474d63357e10804cb033062700675) - `2026-11-09T18:28:38Z` - Gavin Barron (@gavinbarron) - PR: [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-authentication-azure-go/pull/250)
- [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-authentication-azure-go/commit/2ab84529e06c36bcf7f7f87eb0a2c4598daaf114) - `2026-11-09T13:00:04Z` - Vincent Biret (@baywet) - PR: [ci: adds missing merge groups trigger for merge queue](https://github.com/microsoft/kiota-authentication-azure-go/pull/250)

### MicrosoftDocs/azure-docs-sdk-dotnet (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/e6e0cc83ba8c62185c4df97674c9d0dc75ee7e8f) - `2026-11-09T15:14:12Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/9500c2fad4740e2af8f3e5d313be41d109030aae) - `2026-11-09T10:14:34Z` - azure-sdk (@azure-sdk)

### aspnet/AzureSignalR-samples (2 commit(s), signal 0)

Tags: `bot-only, dependency-noise, samples`

- [Bump minimatch and rimraf in /samples/ServerlessChatWithAuth/v4-model…](https://github.com/aspnet/AzureSignalR-samples/commit/da8021919b8c38634bd32db0ba33374899f57deb) - `2026-11-09T06:06:27Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump minimatch and rimraf in /samples/ServerlessChatWithAuth/v4-model](https://github.com/aspnet/AzureSignalR-samples/pull/383)
- [Bump zod from 4.4.3 to 4.6.7 in /samples/Whiteboard/MCPServer (#382)](https://github.com/aspnet/AzureSignalR-samples/commit/e84ed43f0cb989d50a60584cbfbedf9f7d0a927d) - `2026-11-09T03:10:03Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump zod from 4.4.3 to 4.6.7 in /samples/Whiteboard/MCPServer](https://github.com/aspnet/AzureSignalR-samples/pull/382)

### MicrosoftDocs/msix-docs (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/msix-pr …](https://github.com/MicrosoftDocs/msix-docs/commit/01b8c552dd73985e5e437e926fc9110df03422c6) - `2026-11-09T05:01:55Z` - Learn Build Service GitHub App
- [Merge pull request #1107 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/msix-docs/commit/ca64a42e9a9ec830dff992e3ed05f4ad8dc8852a) - `2026-11-09T05:01:32Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### Azure/sap-automation (2 commit(s), signal 117)

Tags: `docs, human-authored, release, watchlist`

- Release: [v3.24.0.0](https://github.com/Azure/sap-automation/releases/tag/v3.24.0.0) - `2026-11-09T07:43:04Z`
- [Update usrsap volume size logic in disks_config.yml for improved flex…](https://github.com/Azure/sap-automation/commit/93862673fe8393e6ecafd99d49c1a6256705d373) - `2026-11-09T02:49:24Z` - Kimmo Forss - PR: [Fix usrsap volume size logic in disks_config.yml](https://github.com/Azure/sap-automation/pull/1379)
- [Fix usrsap volume size logic in disks_config.yml](https://github.com/Azure/sap-automation/commit/2ec1c0b075adbe4c29e00a7d02f30d4247d189ce) - `2026-11-09T02:49:24Z` - Kimmo Forss - PR: [Fix usrsap volume size logic in disks_config.yml](https://github.com/Azure/sap-automation/pull/1379)

### microsoftgraph/github-issue-manager (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, product:Microsoft Graph, samples, watchlist`

- [Merge pull request #95 from microsoftgraph/dependabot/github_actions/…](https://github.com/microsoftgraph/github-issue-manager/commit/17311e264aa83876804622652fd40ad46546c390) - `2026-11-09T02:06:48Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump actions/setup-dotnet from 6.0.0 to 6.1.0](https://github.com/microsoftgraph/github-issue-manager/pull/95)
- [Bump actions/setup-dotnet from 6.0.0 to 6.1.0](https://github.com/microsoftgraph/github-issue-manager/commit/816c14a9703d025bbe32da52557072fdb1b0c71d) - `2026-11-09T02:05:52Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-dotnet from 6.0.0 to 6.1.0](https://github.com/microsoftgraph/github-issue-manager/pull/95)

### Azure/logicapps (1 commit(s), signal 86)

Tags: `human-authored, release-language, samples, watchlist`

- [Update changelog from internal release (automated) (#1578)](https://github.com/Azure/logicapps/commit/9d71fc753bff6f07968fa7021755223cc9d0647f) - `2026-11-09T22:37:06Z` - Abdulqader (Abode) Saafan (@AbodeSaafan) - PR: [Update release notes](https://github.com/Azure/logicapps/pull/1578)

### Azure/azure-sdk (1 commit(s), signal 26)

Tags: `bot-only, docs, product:Azure SDK, watchlist`

- [Sync eng/common directory with azure-sdk-tools for PR 17441 (#10406)](https://github.com/Azure/azure-sdk/commit/8cbc8580c6685987d7986be13901564cf9143ddc) - `2026-11-09T22:06:22Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17441](https://github.com/Azure/azure-sdk/pull/10406)

### Azure/homebrew-azd (1 commit(s), signal 86)

Tags: `human-authored, product:Azure SDK, release-language, samples, watchlist`

- [Update for azd release 1.38.0-beta.1-daily.7054853](https://github.com/Azure/homebrew-azd/commit/00e99a45985ed5c7071fff4d27cab55a90de41f1) - `2026-11-09T21:59:24Z` - azure-sdk (@azure-sdk)

### dotnet/efcore (1 commit(s), signal 0)

Tags: `bot-only, docs`

- [[main] Source code updates from dotnet/dotnet (#39572)](https://github.com/dotnet/efcore/commit/1c541c7683dbf33a7b1aa0655200050b04fa8efe) - `2026-11-09T21:31:46Z` - dotnet-maestro[bot] (@dotnet-maestro[bot]) - PR: [[main] Source code updates from dotnet/dotnet](https://github.com/dotnet/efcore/pull/39572)

### Azure-Samples/functions-quickstart-go-azd (1 commit(s), signal 51)

Tags: `human-authored, release-language, samples`

- [Upgrade Go worker to v1.0.0 GA (#7)](https://github.com/Azure-Samples/functions-quickstart-go-azd/commit/487bf01435f7962fbef65c931977c30e6cd14f77) - `2026-11-09T20:43:30Z` - Harshitha Vegaraju (@harshivcodes) - PR: [Upgrade Go worker to v1.0.0 GA](https://github.com/Azure-Samples/functions-quickstart-go-azd/pull/7)

### MicrosoftLearning/MS-4022-Extend-Microsoft-365-Copilot-in-Copilot-Studio (1 commit(s), signal 76)

Tags: `human-authored, training, watchlist`

- [Merge pull request #43 from Desiderio25/MS-4022-improvements](https://github.com/MicrosoftLearning/MS-4022-Extend-Microsoft-365-Copilot-in-Copilot-Studio/commit/69c27a9751ec4b05a8e60855ae07dea09cd4b55c) - `2026-11-09T20:41:08Z` - chandlersyal (@chandlersyal) - PR: [Update lab setup and classic Copilot Studio navigation instructions](https://github.com/MicrosoftLearning/MS-4022-Extend-Microsoft-365-Copilot-in-Copilot-Studio/pull/43)

### Azure-Samples/durable-functions-order-processing-go (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add Go Durable Functions order-processing sample (#2)](https://github.com/Azure-Samples/durable-functions-order-processing-go/commit/0bc35ccd8601c540ef1aae86147d939179f62836) - `2026-11-09T20:30:45Z` - Harshitha Vegaraju (@harshivcodes) - PR: [Add Go Durable Functions order-processing sample](https://github.com/Azure-Samples/durable-functions-order-processing-go/pull/2)

### Azure-Samples/durable-functions-quickstart-go-azd (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add Go Durable Functions fan-out/fan-in quickstart (#2)](https://github.com/Azure-Samples/durable-functions-quickstart-go-azd/commit/57ebf950e61ba72f4c13610c4208b4a978660f50) - `2026-11-09T20:30:31Z` - Harshitha Vegaraju (@harshivcodes) - PR: [Add Go Durable Functions fan-out/fan-in quickstart](https://github.com/Azure-Samples/durable-functions-quickstart-go-azd/pull/2)

### Azure-Samples/functions-quickstart-go-azd-sql (1 commit(s), signal 51)

Tags: `human-authored, release-language, samples`

- [Upgrade Go worker to v1.0.0 GA (#3)](https://github.com/Azure-Samples/functions-quickstart-go-azd-sql/commit/fe5b330def3bc2c50899b9f9a4d6d288bcc3c3a8) - `2026-11-09T20:30:10Z` - Harshitha Vegaraju (@harshivcodes) - PR: [Upgrade Go worker to v1.0.0 GA](https://github.com/Azure-Samples/functions-quickstart-go-azd-sql/pull/3)

### Azure-Samples/functions-quickstart-go-azd-service-bus (1 commit(s), signal 51)

Tags: `human-authored, release-language, samples`

- [Upgrade Go worker to v1.0.0 GA (#3)](https://github.com/Azure-Samples/functions-quickstart-go-azd-service-bus/commit/f82bcdbf06012815039af2a8ba4b5dd8236ec479) - `2026-11-09T20:29:53Z` - Harshitha Vegaraju (@harshivcodes) - PR: [Upgrade Go worker to v1.0.0 GA](https://github.com/Azure-Samples/functions-quickstart-go-azd-service-bus/pull/3)

### Azure-Samples/functions-quickstart-go-azd-eventgrid-blob (1 commit(s), signal 51)

Tags: `human-authored, release-language, samples`

- [Upgrade Go worker to v1.0.0 GA (#4)](https://github.com/Azure-Samples/functions-quickstart-go-azd-eventgrid-blob/commit/044b0e0e45d963711dc0bf1f99f4474b3e688ec7) - `2026-11-09T20:29:40Z` - Harshitha Vegaraju (@harshivcodes) - PR: [Upgrade Go worker to v1.0.0 GA](https://github.com/Azure-Samples/functions-quickstart-go-azd-eventgrid-blob/pull/4)

### Azure-Samples/functions-quickstart-go-azd-timer (1 commit(s), signal 51)

Tags: `human-authored, release-language, samples`

- [Upgrade Go worker to v1.0.0 GA (#7)](https://github.com/Azure-Samples/functions-quickstart-go-azd-timer/commit/83e5c7f5247442b9b317cc4b54e824e587c97a12) - `2026-11-09T20:29:24Z` - Harshitha Vegaraju (@harshivcodes) - PR: [Upgrade Go worker to v1.0.0 GA](https://github.com/Azure-Samples/functions-quickstart-go-azd-timer/pull/7)

### Azure-Samples/functions-quickstart-go-azd-cosmosdb (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add Go Cosmos DB change feed quickstart (#1)](https://github.com/Azure-Samples/functions-quickstart-go-azd-cosmosdb/commit/f9b082c837301df01470acfd00ccdea03450d280) - `2026-11-09T20:28:56Z` - Harshitha Vegaraju (@harshivcodes) - PR: [Add Go Cosmos DB change feed quickstart](https://github.com/Azure-Samples/functions-quickstart-go-azd-cosmosdb/pull/1)

### Azure-Samples/functions-quickstart-go-azd-eventhub (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add Go Event Hubs trigger quickstart (#1)](https://github.com/Azure-Samples/functions-quickstart-go-azd-eventhub/commit/aac583f48a7c55430769a34ac53a16ef3bba8f84) - `2026-11-09T20:28:39Z` - Harshitha Vegaraju (@harshivcodes) - PR: [Add Go Event Hubs trigger quickstart](https://github.com/Azure-Samples/functions-quickstart-go-azd-eventhub/pull/1)

### Azure/azure-dev (1 commit(s), signal 76)

Tags: `human-authored, samples, watchlist`

- [fix: emit extension errors as JSON on stderr in JSON output mode (#10…](https://github.com/Azure/azure-dev/commit/8e1a9ec2ca506e3bccf6b612af56d4408be9751c) - `2026-11-09T20:14:24Z` - Hui Miao (@huimiu) - PR: [fix: emit extension errors as JSON on stderr in JSON output mode](https://github.com/Azure/azure-dev/pull/10861)

### MicrosoftDocs/azure-docs-sdk-python (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/71850bfe0f08801448ab1f8ccb814066fd9c540d) - `2026-11-09T18:44:40Z` - azure-sdk (@azure-sdk)

### Azure/setup-azd (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, samples, watchlist`

- [build(deps-dev): bump eslint (#642)](https://github.com/Azure/setup-azd/commit/a2855ef5c4bf20233e19aa57ca53ef3a1d95b665) - `2026-11-09T18:06:09Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps-dev): bump eslint from 10.13.0 to 10.14.0 in the minor-and-patch group](https://github.com/Azure/setup-azd/pull/642)

### dotnet/AspNetCore.Docs (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, docs`

- [Bump Microsoft.EntityFrameworkCore.InMemory across 44 directories (#3…](https://github.com/dotnet/AspNetCore.Docs/commit/9a64f8789b15998c33e006c14a1d59841b4000e0) - `2026-11-09T18:01:35Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.EntityFrameworkCore.InMemory across 44 directories](https://github.com/dotnet/AspNetCore.Docs/pull/38053)

### MicrosoftDocs/PowerShell-Docs-DSC (1 commit(s), signal 76)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Clarify unsupported status for PSDscResources module (#433)](https://github.com/MicrosoftDocs/PowerShell-Docs-DSC/commit/4838f13553bd17627a3e85a3239ef6a43a20149d) - `2026-11-09T16:39:19Z` - Mikey Lombardi (He/Him) (@michaeltlombardi) - PR: [(MAINT) Clarify unsupported status for PSDscResources module](https://github.com/MicrosoftDocs/PowerShell-Docs-DSC/pull/433)

### Azure/iot-operations-sdks (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, watchlist`

- [Bump the patch-and-minor group with 3 updates (#1540)](https://github.com/Azure/iot-operations-sdks/commit/0a78ca98014a4b096dae969de94e8982d020656b) - `2026-11-09T16:31:52Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the patch-and-minor group with 3 updates](https://github.com/Azure/iot-operations-sdks/pull/1540)

### MicrosoftDocs/data-tools (1 commit(s), signal 26)

Tags: `bot-only, docs, watchlist`

- [Merge pull request #961 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/data-tools/commit/bfee6a4d674df5334318f9b80a578e97d6da9a57) - `2026-11-09T16:31:44Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### microsoftgraph/msgraph-sdk-java (1 commit(s), signal 126)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [v6.73.0](https://github.com/microsoftgraph/msgraph-sdk-java/releases/tag/v6.73.0) - `2026-11-09T15:47:16Z`
- [Merge pull request #2706 from microsoftgraph/release-please--branches…](https://github.com/microsoftgraph/msgraph-sdk-java/commit/bd416f82569403e8362b91dfcfc5d0189fc2b7c5) - `2026-11-09T15:46:50Z` - Treicy Sanchez (@Treicysg) - PR: [chore(main): release 6.73.0](https://github.com/microsoftgraph/msgraph-sdk-java/pull/2706)

### microsoftgraph/msgraph-sdk-go (1 commit(s), signal 126)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [v1.106.0](https://github.com/microsoftgraph/msgraph-sdk-go/releases/tag/v1.106.0) - `2026-11-09T15:46:38Z`
- [Merge pull request #1066 from microsoftgraph/release-please--branches…](https://github.com/microsoftgraph/msgraph-sdk-go/commit/23223e06ede97b9482cbfd5a4445b0650a83749c) - `2026-11-09T15:46:10Z` - Treicy Sanchez (@Treicysg) - PR: [chore(main): release 1.106.0](https://github.com/microsoftgraph/msgraph-sdk-go/pull/1066)

### MicrosoftDocs/winapps-winrt-api (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Clarify Window.Activate foreground behavior (#125)](https://github.com/MicrosoftDocs/winapps-winrt-api/commit/a554305df14f498f34f95b70e78f30c2ed94576e) - `2026-11-09T15:32:40Z` - Jesse Collins (@JesseCol) - PR: [Clarify Window.Activate foreground behavior](https://github.com/MicrosoftDocs/winapps-winrt-api/pull/125)

### Azure/terraform-azurerm-avm-res-devtestlab-lab (1 commit(s), signal 26)

Tags: `bot-only, training, watchlist`

- [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-res-devtestlab-lab/commit/51792edf72ae85e9a7a6dc3217bc894dec19d913) - `2026-11-09T14:11:57Z` - azure-verified-modules[bot] (@azure-verified-modules[bot]) - PR: [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-res-devtestlab-lab/pull/85)

### microsoft/Agent365-Samples (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, product:Azure AI, samples, watchlist`

- [Build(deps): Bump the github-actions group across 1 directory with 6 …](https://github.com/microsoft/Agent365-Samples/commit/8b199c4c0d80d844b280b7fe475ba26cb5921ad9) - `2026-11-09T14:01:55Z` - dependabot[bot] (@dependabot[bot]) - PR: [Build(deps): Bump the github-actions group across 1 directory with 6 updates](https://github.com/microsoft/Agent365-Samples/pull/353)

### microsoft/waf-adoption-strategy-sample (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Merge pull request #2 from danfiedler-msft/danfiedler/pin-actions](https://github.com/microsoft/waf-adoption-strategy-sample/commit/46d43fb11d3edc2a64a1d8fd7907e51ead290f65) - `2026-11-09T13:25:53Z` - Aymen (@aymenfurter) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/microsoft/waf-adoption-strategy-sample/pull/2)

### microsoft/custom-monaco-copilot-demo (1 commit(s), signal 76)

Tags: `human-authored, samples, watchlist`

- [Merge pull request #53 from danfiedler-msft/danfiedler/pin-actions](https://github.com/microsoft/custom-monaco-copilot-demo/commit/b0de06fed8bd4b3e97ba698a1dd2f42b24899099) - `2026-11-09T13:25:29Z` - Aymen (@aymenfurter) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/microsoft/custom-monaco-copilot-demo/pull/53)

### Azure/terraform-azurerm-avm-ptn-commercial-marketplace (1 commit(s), signal 26)

Tags: `bot-only, samples, watchlist`

- [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-ptn-commercial-marketplace/commit/0a4c7e13647c08abf73f7f39064b8c7d06236fe6) - `2026-11-09T13:13:51Z` - azure-verified-modules[bot] (@azure-verified-modules[bot]) - PR: [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-ptn-commercial-marketplace/pull/67)

### Azure/terraform-azurerm-avm-ptn-aca-lza-hosting-environment (1 commit(s), signal 26)

Tags: `bot-only, samples, watchlist`

- [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-ptn-aca-lza-hosting-environment/commit/0067c3c0542c1dfd55ff8f38336ae6809d1783c0) - `2026-11-09T12:49:09Z` - azure-verified-modules[bot] (@azure-verified-modules[bot]) - PR: [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-ptn-aca-lza-hosting-environment/pull/109)

### microsoft/CopilotAnalyticsLabs (1 commit(s), signal 76)

Tags: `human-authored, samples, watchlist`

- [Add Cowork Chargeback Report and align template actions](https://github.com/microsoft/CopilotAnalyticsLabs/commit/574fae6e30d979fdc1320614e9455e9961382ac6) - `2026-11-09T11:32:37Z` - Swastik Das (@swadas1989)

### microsoft/agentic-applications-for-unified-data-foundation-solution-accelerator (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Merge pull request #541 from microsoft/dev](https://github.com/microsoft/agentic-applications-for-unified-data-foundation-solution-accelerator/commit/9ecb6f0df7e97a34fbe927508b94e9d641110f06) - `2026-11-09T09:11:10Z` - Roopan-Microsoft (@Roopan-Microsoft) - PR: [chore: dev to main branch merge](https://github.com/microsoft/agentic-applications-for-unified-data-foundation-solution-accelerator/pull/541)

### Azure-Samples/flex-container-html2pdf-go (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Initial commit](https://github.com/Azure-Samples/flex-container-html2pdf-go/commit/63e4bd9d84ffd723296f0da9bdc96ff97b883d74) - `2026-11-09T07:22:39Z` - Paul Yuknewicz (@paulyuk)

### microsoft/aspire-samples (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, docs`

- [build(deps): Bump actions/setup-dotnet (#2162)](https://github.com/microsoft/aspire-samples/commit/c19d8c1d740bfbd77949c09ab83fea6924407010) - `2026-11-09T07:09:22Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): Bump actions/setup-dotnet from 6.0.0 to 6.1.0 in the github-actions group](https://github.com/microsoft/aspire-samples/pull/2162)

### microsoft/Multi-Agent-Custom-Automation-Engine-Solution-Accelerator (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merge pull request #1185 from microsoft/dev](https://github.com/microsoft/Multi-Agent-Custom-Automation-Engine-Solution-Accelerator/commit/92d476ae2fe3d67e1c394f0af922d65e90155026) - `2026-11-09T06:32:36Z` - Roopan-Microsoft (@Roopan-Microsoft) - PR: [fix: merging the changes from dev to main](https://github.com/microsoft/Multi-Agent-Custom-Automation-Engine-Solution-Accelerator/pull/1185)

### dotnet/docfx (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [test: find the solution folder by docfx.slnx and only rewrite paths f…](https://github.com/dotnet/docfx/commit/b818fc329e3eb89979b6dea64bfd0568aa6c5a13) - `2026-11-09T03:18:09Z` - MaceWindu (@MaceWindu) - PR: [test: find the solution folder by docfx.slnx and only rewrite paths for WSL on Linux](https://github.com/dotnet/docfx/pull/11209)

### MicrosoftDocs/Agent-Skills (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [2026-11-08 02:42 - Generate skills from docs (code: ADO/main, target:…](https://github.com/MicrosoftDocs/Agent-Skills/commit/9b16b5c7c7716949c83fc4bbdc448e0ada7f93a3) - `2026-11-09T00:06:15Z` - Osmond Jiang (@OsmondJiang) - PR: [Sync docs to agent skills - 2026-11-08 02:42](https://github.com/MicrosoftDocs/Agent-Skills/pull/83)

### microsoft/finops-toolkit (1 commit(s), signal 86)

Tags: `docs, human-authored, product:PowerShell, release-language, watchlist`

- [fix(demo): Keep 3 months on the demo version being built (#2408)](https://github.com/microsoft/finops-toolkit/commit/09c73e7bbaa24fffc67729827a843eaee11a51d8) - `2026-11-08T17:38:32Z` - Michael Flanakin (@flanakin) - PR: [fix(demo): Keep 3 months on the demo version being built](https://github.com/microsoft/finops-toolkit/pull/2408)

</details>
