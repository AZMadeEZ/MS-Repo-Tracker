# Microsoft Ecosystem Daily Brief - 2026-10-30

> Status: Fresh at generation. Current freshness is tracked in `reports/status.json`.
> Generated: 2026-10-30 18:41 UTC - Window: 25.7h from 2026-10-29 17:01 UTC to 2026-10-30 18:41 UTC.
> 133 repo(s) moved - 837 commit(s) - 36 release item(s) - 25 high-signal repo(s).

## Plain-English Summary

- Azure, .NET led the visible product-area activity in this window.
- 36 release item(s) were detected during the window.
- Security-related changes appeared in Azure/azure-sdk-for-java, MicrosoftDocs/windowsserverdocs, Azure/azure-sdk-for-rust.
- Start with human-authored changes in Azure/azure-sdk-for-java, MicrosoftDocs/windowsserverdocs, Azure/azure-sdk-for-rust, Azure-Samples/ms-identity-ciam-native-javascript-samples.
- 138 event(s) look automated, bot-heavy, dependency, or generated; review the curated sections before raw volume.

## Headline Metrics

| Metric | Value |
| --- | ---: |
| Inventory repositories | 16748 |
| Repositories after filters | 2632 |
| `pushed_at` candidates | 207 |
| Enrichment candidates | 207 |
| Repositories with movement | 133 |
| Default-branch commits | 837 |

## What Changed That Matters

| Repository | Score | Change | Actor | Noise | Headline | Time |
| --- | ---: | --- | --- | --- | --- | --- |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 100 | security_fix | human | low | [Clarify managed identity selection in credential builder documentation](https://github.com/Azure/azure-sdk-for-java/pull/51021) | `2026-10-30T18:10:42Z` |
| [MicrosoftDocs/windowsserverdocs](https://github.com/MicrosoftDocs/windowsserverdocs) | 100 | security_fix | human | low | [Clarify security group descriptions and risks](https://github.com/MicrosoftDocs/windowsserverdocs/pull/8144) | `2026-10-30T10:50:33Z` |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 100 | security_fix | human | low | [Add default credential scope and ARM endpoint support](https://github.com/Azure/azure-sdk-for-rust/pull/5495) | `2026-10-30T00:42:11Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 100 | release | unknown | low | [azure-communication-callautomation_1.6.1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-communication-callautomation_1.6.1) | `2026-10-30T18:18:39Z` |
| [Azure-Samples/ms-identity-ciam-native-javascript-samples](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples) | 100 | release | human | low | [Add passkey naming and broaden authenticator choices](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/pull/69) | `2026-10-30T18:18:01Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 100 | release | unknown | low | [Azure.ResourceManager.DeviceProvisioningServices_1.4.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.DeviceProvisioningServices_1.4.0) | `2026-10-30T18:12:25Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 100 | release | unknown | low | [Azure.Security.Attestation_2.0.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Security.Attestation_2.0.0) | `2026-10-30T17:51:29Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 100 | release | unknown | low | [com.azure+azure-ai-agents_2.9.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-ai-agents_2.9.0) | `2026-10-30T17:16:32Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 100 | release | unknown | low | [com.azure+azure-ai-projects_2.9.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-ai-projects_2.9.0) | `2026-10-30T17:16:18Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 100 | release | unknown | low | [@azure/ai-projects_2.10.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/ai-projects_2.10.0) | `2026-10-30T17:10:46Z` |
| [microsoft/vscode-docs](https://github.com/microsoft/vscode-docs) | 100 | release | human | low | [Fix missing placeholders in VS Code 1.144 release notes](https://github.com/microsoft/vscode-docs/pull/10563) | `2026-10-30T14:41:03Z` |
| [Azure/sap-automation-qa](https://github.com/Azure/sap-automation-qa) | 100 | release | unknown | low | [1.1.5](https://github.com/Azure/sap-automation-qa/releases/tag/1.1.5) | `2026-10-30T14:40:16Z` |
| [Azure/sap-automation-qa](https://github.com/Azure/sap-automation-qa) | 100 | release | human | low | [Release/september 2026](https://github.com/Azure/sap-automation-qa/pull/386) | `2026-10-30T14:28:05Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 100 | release | unknown | low | [azure-mgmt-storagemover_3.2.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-storagemover_3.2.0) | `2026-10-30T09:05:07Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 100 | release | unknown | low | [@azure/arm-netapp_25.1.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-netapp_25.1.0-beta.1) | `2026-10-30T05:01:45Z` |

## Product Areas

| Product area | Signal | Repos | Events | Releases | Security | Top links |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Azure | 168 | 54 | 204 | 32 | 7 | [Clarify managed identity selection in credential builder documentation](https://github.com/Azure/azure-sdk-for-java/pull/51021); [Add default credential scope and ARM endpoint support](https://github.com/Azure/azure-sdk-for-rust/pull/5495); [azure-communication-callautomation_1.6.1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-communication-callautomation_1.6.1) |
| Unmapped Activity | 79 | 40 | 103 | 3 | 0 | [ONNX Runtime v1.30.1](https://github.com/microsoft/onnxruntime/releases/tag/v1.30.1); [ONNX Runtime WebGPU Plugin EP v0.5.0](https://github.com/microsoft/onnxruntime/releases/tag/plugin-ep-webgpu/v0.5.0); [Add Caldova L300 assets and six-hour L400 challenge lab](https://github.com/MicrosoftLearning/mslearn-unify-data/pull/1) |
| .NET | 20 | 9 | 32 | 0 | 0 | [Unsafe evolution: warn for deprecated feature flag](https://github.com/dotnet/roslyn/pull/86224); [Fix JSON complex property projections with identity resolution](https://github.com/dotnet/efcore/pull/39442); [Remove a bunch of ProjectReference Name properties](https://github.com/dotnet/roslyn/pull/86253) |
| Microsoft Graph | 14 | 13 | 47 | 1 | 0 | [v1.37.0](https://github.com/microsoft/kiota/releases/tag/v1.37.0); [- bumps version for release of 1.37.0](https://github.com/microsoft/kiota/pull/8514); [chore: release main](https://github.com/microsoft/kiota-dart/pull/161) |
| PowerShell | 11 | 3 | 11 | 0 | 0 | [Fix syntax formatting in Set-CsUserCallingSettings.md](https://github.com/MicrosoftDocs/office-docs-powershell/pull/13859); [Enhance synopsis for Get-CsUserCallingSettings](https://github.com/MicrosoftDocs/office-docs-powershell/pull/13858); [Respect -WhatIf in PowerShell package commands](https://github.com/microsoft/winget-cli/pull/6588) |
| Developer Tools | 10 | 5 | 14 | 0 | 0 | [Fix missing placeholders in VS Code 1.144 release notes](https://github.com/microsoft/vscode-docs/pull/10563); [Clarify extension access in remote development](https://github.com/microsoft/vscode-docs/pull/10566); [Improve custom instructions docs](https://github.com/microsoft/vscode-docs/pull/10565) |
| Microsoft 365 | 8 | 6 | 12 | 0 | 0 | [Merging changes synced from https://github.com/MicrosoftDocs/m365copi…](https://github.com/MicrosoftDocs/m365copilot-docs/commit/7a9f68194ef55755117362a38a77ce0a82267057); [Merge pull request #1765 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/m365copilot-docs/commit/2991f9e70b59c89f58d32e30793904e4d555a18c); [Update cloud support status (#1764)](https://github.com/MicrosoftDocs/m365copilot-docs/commit/71f17a0bd1b4578a732575cf590e6bf313970141) |
| Identity | 7 | 2 | 7 | 0 | 0 | [Merging changes synced from https://github.com/MicrosoftDocs/entra-do…](https://github.com/MicrosoftDocs/entra-docs/commit/07cb73d6c6380414eecd040ba5e14c1c94d48b66); [Clarify supported objects for synchronization cloud pairs (#14745)](https://github.com/MicrosoftDocs/entra-docs/commit/ddf451b78ba8ce367f1515545b2487dc593d9946); [Publish six CYOT GA articles (#14742)](https://github.com/MicrosoftDocs/entra-docs/commit/19ce39e320688384c4552abc24dfa82b679ef833) |

## Today's Top Links

| Priority | Repository | Why read it |
| ---: | --- | --- |
| 1 | [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [Security-related change: Clarify managed identity selection in credential builder documentation](https://github.com/Azure/azure-sdk-for-java/pull/51021) |
| 2 | [MicrosoftDocs/windowsserverdocs](https://github.com/MicrosoftDocs/windowsserverdocs) | [Security-related change: Clarify security group descriptions and risks](https://github.com/MicrosoftDocs/windowsserverdocs/pull/8144) |
| 3 | [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | [Security-related change: Add default credential scope and ARM endpoint support](https://github.com/Azure/azure-sdk-for-rust/pull/5495) |
| 4 | [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [Release activity: azure-communication-callautomation_1.6.1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-communication-callautomation_1.6.1) |
| 5 | [Azure-Samples/ms-identity-ciam-native-javascript-samples](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples) | [Release activity: Add passkey naming and broaden authenticator choices](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/pull/69) |
| 6 | [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Release activity: Azure.ResourceManager.DeviceProvisioningServices_1.4.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.DeviceProvisioningServices_1.4.0) |
| 7 | [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [Release activity: @azure/ai-projects_2.10.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/ai-projects_2.10.0) |
| 8 | [microsoft/vscode-docs](https://github.com/microsoft/vscode-docs) | [Release activity: Fix missing placeholders in VS Code 1.144 release notes](https://github.com/microsoft/vscode-docs/pull/10563) |

## Noise and Automation

- 138 event(s) look automated, bot-heavy, dependency, generated, or medium/high noise.
- Top noisy repositories: microsoftgraph/msgraph-sample-github-connector-dotnet, microsoft/kiota-java, microsoftgraph/msgraph-sample-github-connector-typescript, microsoftgraph/nodejs-webhooks-sample, microsoftgraph/msgraph-snippets-go.
- Noise mix: Docs: 55, Dependency: 54, CI/Infra: 17, SDK: 11, Release: 1.

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
| Repos counted | 207 |
| Repos enriched | 133 |

</details>

<details>
<summary>Show supporting signal, release, and lifecycle tables</summary>

## High-Signal Items

| Repository | Score | Tags |
| --- | ---: | --- |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 161 | docs, human-authored, product:Azure AI, product:Azure SDK, release, release-language, security, watchlist |
| [Azure/sap-automation-qa](https://github.com/Azure/sap-automation-qa) | 150 | docs, human-authored, product:Azure AI, release, release-language, watchlist |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 150 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [microsoft/kiota](https://github.com/microsoft/kiota) | 131 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 130 | docs, human-authored, release, release-language, watchlist |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 124 | docs, human-authored, product:Azure AI, product:Azure SDK, release, watchlist |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 124 | docs, human-authored, product:Azure AI, product:Azure SDK, release, watchlist |
| [Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample) | 109 | human-authored, release, samples, security |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 104 | docs, human-authored, product:Azure SDK, security, watchlist |
| [MicrosoftDocs/entra-docs](https://github.com/MicrosoftDocs/entra-docs) | 103 | docs, human-authored, release-language, watchlist |
| [microsoft/DataSecurityGuidedAssistant](https://github.com/microsoft/DataSecurityGuidedAssistant) | 102 | docs, human-authored, security, watchlist |
| [microsoft/Agent365-Samples](https://github.com/microsoft/Agent365-Samples) | 101 | human-authored, product:Azure AI, samples, security, watchlist |
| [MicrosoftDocs/windowsserverdocs](https://github.com/MicrosoftDocs/windowsserverdocs) | 101 | docs, human-authored, security, watchlist |
| [microsoftgraph/nodejs-webhooks-sample](https://github.com/microsoftgraph/nodejs-webhooks-sample) | 100 | docs, human-authored, product:Microsoft Graph, watchlist |
| [MicrosoftLearning/mslearn-copilotstudio](https://github.com/MicrosoftLearning/mslearn-copilotstudio) | 100 | human-authored, release-language, training, watchlist |

## Watchlist Hits

| Repository | Score | Matches |
| --- | ---: | --- |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 161 | products: Azure AI, Azure SDK; repos: Azure/azure-sdk-for-java; orgs: Azure; keywords: agent, release, sdk |
| [Azure/sap-automation-qa](https://github.com/Azure/sap-automation-qa) | 150 | products: Azure AI; orgs: Azure; keywords: agent, release |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 150 | products: Azure SDK; repos: Azure/azure-sdk-for-net; orgs: Azure; keywords: copilot, release, sdk |
| [microsoft/kiota](https://github.com/microsoft/kiota) | 131 | products: Microsoft Graph, Azure SDK; repos: microsoft/kiota; keywords: graph, kiota, release, sdk |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 130 | orgs: Azure; keywords: release |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 124 | products: Azure AI, Azure SDK; repos: Azure/azure-sdk-for-python; orgs: Azure; keywords: agent, azure ai, sdk |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 124 | products: Azure AI, Azure SDK; repos: Azure/azure-sdk-for-js; orgs: Azure; keywords: foundry, sdk |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 104 | products: Azure SDK; orgs: Azure; keywords: copilot, sdk |
| [MicrosoftDocs/entra-docs](https://github.com/MicrosoftDocs/entra-docs) | 103 | orgs: MicrosoftDocs; keywords: entra |
| [microsoft/DataSecurityGuidedAssistant](https://github.com/microsoft/DataSecurityGuidedAssistant) | 102 | keywords: security |
| [microsoft/Agent365-Samples](https://github.com/microsoft/Agent365-Samples) | 101 | products: Azure AI; keywords: agent |
| [MicrosoftDocs/windowsserverdocs](https://github.com/MicrosoftDocs/windowsserverdocs) | 101 | orgs: MicrosoftDocs; keywords: security |
| [microsoftgraph/nodejs-webhooks-sample](https://github.com/microsoftgraph/nodejs-webhooks-sample) | 100 | products: Microsoft Graph; orgs: microsoftgraph; keywords: graph |
| [MicrosoftLearning/mslearn-copilotstudio](https://github.com/MicrosoftLearning/mslearn-copilotstudio) | 100 | orgs: MicrosoftLearning; keywords: copilot |
| [MicrosoftDocs/fabric-docs](https://github.com/MicrosoftDocs/fabric-docs) | 100 | products: Azure AI; orgs: MicrosoftDocs; keywords: agent |

## Releases

| Repository | Release | Published |
| --- | --- | --- |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-communication-callautomation_1.6.1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-communication-callautomation_1.6.1) | `2026-10-30T18:18:39Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.ResourceManager.DeviceProvisioningServices_1.4.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.DeviceProvisioningServices_1.4.0) | `2026-10-30T18:12:25Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.Security.Attestation_2.0.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Security.Attestation_2.0.0) | `2026-10-30T17:51:29Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure+azure-ai-agents_2.9.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-ai-agents_2.9.0) | `2026-10-30T17:16:32Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure+azure-ai-projects_2.9.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-ai-projects_2.9.0) | `2026-10-30T17:16:18Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/ai-projects_2.10.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/ai-projects_2.10.0) | `2026-10-30T17:10:46Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure+azure-sdk-template_1.2.1-beta.7021230](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-sdk-template_1.2.1-beta.7021230) | `2026-10-30T16:50:38Z` |
| [Azure/sap-automation-qa](https://github.com/Azure/sap-automation-qa) | [1.1.5](https://github.com/Azure/sap-automation-qa/releases/tag/1.1.5) | `2026-10-30T14:40:16Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.ResourceManager.RedHatOpenShiftHcp_1.0.0-beta.2](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.RedHatOpenShiftHcp_1.0.0-beta.2) | `2026-10-30T11:43:48Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-mgmt-storagemover_3.2.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-storagemover_3.2.0) | `2026-10-30T09:05:07Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.ResourceManager.PrivateTrafficManager_1.0.0-beta.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.PrivateTrafficManager_1.0.0-beta.1) | `2026-10-30T08:15:06Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/resourcemanager/storagemover/armstoragemover/v2.5.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/storagemover/armstoragemover/v2.5.0) | `2026-10-30T07:50:54Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure.resourcemanager+azure-resourcemanager-privatetrafficmanager_1.0.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-privatetrafficmanager_1.0.0-beta.1) | `2026-10-30T07:42:52Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/resourcemanager/privatetrafficmanager/armprivatetrafficmanager/v0.1.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/privatetrafficmanager/armprivatetrafficmanager/v0.1.0) | `2026-10-30T07:41:27Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-ai-agentserver-responses_2.4.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-responses_2.4.0) | `2026-10-30T06:53:10Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-ai-agentserver-invocations_1.3.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-invocations_1.3.0) | `2026-10-30T06:52:25Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.ResourceManager.EdgeActions_1.0.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.EdgeActions_1.0.0) | `2026-10-30T06:03:13Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-mgmt-aiinfraoptimization_1.0.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-aiinfraoptimization_1.0.0b1) | `2026-10-30T05:59:42Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-netapp_25.1.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-netapp_25.1.0-beta.1) | `2026-10-30T05:01:45Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-aiinfraoptimization_1.0.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-aiinfraoptimization_1.0.0-beta.1) | `2026-10-30T04:59:12Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure.resourcemanager+azure-resourcemanager-aiinfraoptimization_1.0.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-aiinfraoptimization_1.0.0-beta.1) | `2026-10-30T02:28:37Z` |
| [microsoft/kiota](https://github.com/microsoft/kiota) | [v1.37.0](https://github.com/microsoft/kiota/releases/tag/v1.37.0) | `2026-10-30T01:16:57Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [edge-action 1.1.0](https://github.com/Azure/azure-cli-extensions/releases/tag/edge-action-1.1.0) | `2026-10-29T23:55:04Z` |
| [Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample) | [EPP javascript Function ZIP 271.1](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/releases/tag/epp-packages-271-1-javascript) | `2026-10-29T23:44:52Z` |
| [Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample) | [EPP python Function ZIP 271.1](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/releases/tag/epp-packages-271-1-python) | `2026-10-29T23:44:50Z` |

## Repository Lifecycle

| Change | Count |
| --- | ---: |
| archived_changed | 1 |
| category_changed | 0 |
| default_branch_changed | 0 |
| fork_changed | 0 |
| new_repos | 7 |
| removed_repos | 0 |

## Category Summary

| Category | Repositories |
| --- | ---: |
| docs | 84 |
| reference | 1 |
| samples | 41 |
| training | 7 |

## Organization Summary

| Org | Repositories |
| --- | ---: |
| MicrosoftDocs | 37 |
| microsoft | 35 |
| Azure | 18 |
| Azure-Samples | 16 |
| dotnet | 9 |
| microsoftgraph | 9 |
| MicrosoftLearning | 6 |
| OfficeDev | 3 |

</details>

<details>
<summary>Show raw repository activity</summary>

## Busiest Repositories

| Repository | Signal | Category | Commits | Releases | Newest commit |
| --- | ---: | --- | ---: | ---: | --- |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 161 | docs | 11 | 5 | `2026-10-30T18:10:42Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 150 | docs | 32 | 5 | `2026-10-30T17:51:57Z` |
| [Azure/sap-automation-qa](https://github.com/Azure/sap-automation-qa) | 150 | docs | 30 | 1 | `2026-10-30T14:28:05Z` |
| [microsoft/kiota](https://github.com/microsoft/kiota) | 131 | docs | 6 | 1 | `2026-10-30T11:16:47Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 130 | docs | 5 | 2 | `2026-10-30T06:47:50Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 124 | docs | 9 | 5 | `2026-10-30T18:38:22Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 124 | docs | 9 | 5 | `2026-10-30T15:58:02Z` |
| [Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample) | 109 | samples | 4 | 5 | `2026-10-29T23:42:08Z` |
| [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) | 104 | docs | 4 | 0 | `2026-10-30T00:42:11Z` |
| [MicrosoftDocs/entra-docs](https://github.com/MicrosoftDocs/entra-docs) | 103 | docs | 18 | 0 | `2026-10-30T17:43:39Z` |
| [microsoft/DataSecurityGuidedAssistant](https://github.com/microsoft/DataSecurityGuidedAssistant) | 102 | docs | 2 | 0 | `2026-10-30T13:45:01Z` |
| [microsoft/Agent365-Samples](https://github.com/microsoft/Agent365-Samples) | 101 | samples | 1 | 0 | `2026-10-30T16:32:39Z` |
| [MicrosoftDocs/windowsserverdocs](https://github.com/MicrosoftDocs/windowsserverdocs) | 101 | docs | 1 | 0 | `2026-10-30T10:50:33Z` |
| [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs) | 100 | docs | 76 | 0 | `2026-10-30T17:17:03Z` |
| [MicrosoftDocs/fabric-docs](https://github.com/MicrosoftDocs/fabric-docs) | 100 | docs | 47 | 0 | `2026-10-30T17:11:56Z` |
| [MicrosoftDocs/azure-compute-docs](https://github.com/MicrosoftDocs/azure-compute-docs) | 100 | docs | 35 | 0 | `2026-10-30T06:07:38Z` |
| [MicrosoftDocs/architecture-center](https://github.com/MicrosoftDocs/architecture-center) | 100 | docs | 27 | 0 | `2026-10-30T17:32:04Z` |
| [microsoftgraph/nodejs-webhooks-sample](https://github.com/microsoftgraph/nodejs-webhooks-sample) | 100 | docs | 25 | 0 | `2026-10-29T20:35:52Z` |
| [MicrosoftLearning/mslearn-copilotstudio](https://github.com/MicrosoftLearning/mslearn-copilotstudio) | 100 | training | 15 | 0 | `2026-10-30T17:52:40Z` |
| [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime) | 98 | samples | 18 | 2 | `2026-10-30T17:28:11Z` |

## Repository Details

### MicrosoftDocs/azure-docs (76 commit(s), signal 100)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-do…](https://github.com/MicrosoftDocs/azure-docs/commit/06482e4e9bb4794f7f1bf803d486d2dae96a4efc) - `2026-10-30T17:17:03Z` - Learn Build Service GitHub App
- [Merge pull request #321884 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-docs/commit/a85f5612cab3587e84a85b1a244bd7445db058f2) - `2026-10-30T17:15:59Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #321832 from jgoldberg1/jmg/sessionTakeoverPrevention](https://github.com/MicrosoftDocs/azure-docs/commit/7c637b0127ca9f764d19d7a606db528f5171707c) - `2026-10-30T17:04:28Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #321881 from NSannala/acz-ga-followup](https://github.com/MicrosoftDocs/azure-docs/commit/62cef2575048d85832ce7b103a828e614960b98f) - `2026-10-30T16:49:20Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merging changes synced from https://github.com/MicrosoftDocs/azure-do…](https://github.com/MicrosoftDocs/azure-docs/commit/e90d383efc956e7f064716250fb25347d5bf0cd5) - `2026-10-30T16:25:15Z` - Learn Build Service GitHub App

### MicrosoftDocs/fabric-docs (47 commit(s), signal 100)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merge pull request #3473 from MicrosoftDocs/main639289770976030020syn…](https://github.com/MicrosoftDocs/fabric-docs/commit/15c09d11be832588b0e4383dccc76b797b9e9165) - `2026-10-30T17:11:56Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3473)
- [Merging changes synced from https://github.com/MicrosoftDocs/fabric-d…](https://github.com/MicrosoftDocs/fabric-docs/commit/a88b4307afe1482f0422328fd57ebc16105d0b8e) - `2026-10-30T17:11:34Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3473)
- [Merge pull request #17167 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/fabric-docs/commit/05335319b8b7e47dbf34bbbf6f730ff90508c48c) - `2026-10-30T17:07:04Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3473)
- [Add Fabric IQ guidance for Agent Builder (#17001)](https://github.com/MicrosoftDocs/fabric-docs/commit/86a5bc8a9c857e4e3b64f4ccaf27d609a19d8514) - `2026-10-30T16:11:21Z` - Fabio Villatoro (@fabiovillatoroPM) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3473)
- [Merge pull request #17164 from conxu-ms/patch-57](https://github.com/MicrosoftDocs/fabric-docs/commit/fc115cc0ae3364d48414071250d6f3e5a3c410fe) - `2026-10-30T15:49:13Z` - prmerger-automator[bot] (@prmerger-automator[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3473)

### MicrosoftDocs/azure-compute-docs (35 commit(s), signal 100)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-co…](https://github.com/MicrosoftDocs/azure-compute-docs/commit/f51840f11d8c719be1178c07f24b60310a391dba) - `2026-10-30T06:07:38Z` - Learn Build Service GitHub App
- [Merge pull request #4298 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-compute-docs/commit/0c0e205d37cd255380b3f12eadc35897b58fc6b1) - `2026-10-30T06:06:20Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #4113 from fitzgeraldsteele/docs/vmss-planned-main…](https://github.com/MicrosoftDocs/azure-compute-docs/commit/8ec33d20e72a37a2dd513f02566f26d1446c5d8d) - `2026-10-30T05:53:01Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merging changes synced from https://github.com/MicrosoftDocs/azure-co…](https://github.com/MicrosoftDocs/azure-compute-docs/commit/c9fda08094915426c71d0a97192d58fe817e91fb) - `2026-10-29T22:03:24Z` - Learn Build Service GitHub App
- [Merge pull request #4293 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-compute-docs/commit/3a769e29d79b989f36faab8dd53b2f45ec8bfc4f) - `2026-10-29T22:02:19Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### Azure/azure-sdk-for-net (32 commit(s), signal 150)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [Azure.ResourceManager.DeviceProvisioningServices_1.4.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.DeviceProvisioningServices_1.4.0) - `2026-10-30T18:12:25Z`
- Release: [Azure.Security.Attestation_2.0.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Security.Attestation_2.0.0) - `2026-10-30T17:51:29Z`
- Release: [Azure.ResourceManager.RedHatOpenShiftHcp_1.0.0-beta.2](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.RedHatOpenShiftHcp_1.0.0-beta.2) - `2026-10-30T11:43:48Z`
- Release: [Azure.ResourceManager.PrivateTrafficManager_1.0.0-beta.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.PrivateTrafficManager_1.0.0-beta.1) - `2026-10-30T08:15:06Z`
- Release: [Azure.ResourceManager.EdgeActions_1.0.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.EdgeActions_1.0.0) - `2026-10-30T06:03:13Z`
- [[Monitor Exporter] Add Attach SDK stats for multi-endpoint routing (#…](https://github.com/Azure/azure-sdk-for-net/commit/f015fd5b950cdaf4c3b80e004313d72f0dab244b) - `2026-10-30T17:51:57Z` - Jackson Weber (@JacksonWeber) - PR: [[Monitor Exporter] Add Attach SDK stats for multi-endpoint routing](https://github.com/Azure/azure-sdk-for-net/pull/63954)
- [Regenerate repository SDK with TypeSpec build 20261030.2 [skip ci] (#…](https://github.com/Azure/azure-sdk-for-net/commit/46c60441441d5e4d6ef965b6ce6560c717cc5307) - `2026-10-30T17:35:03Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Update azure-typespec/http-client-csharp version to prerelease 1.0.0-alpha.20261030.2](https://github.com/Azure/azure-sdk-for-net/pull/64381)
- [Add alzimmermsft to Azure emitter version CODEOWNERS (#64382)](https://github.com/Azure/azure-sdk-for-net/commit/1b746cdb72b4c99be3fc2fa8491fe0a3da5fabef) - `2026-10-30T17:07:58Z` - Copilot (@Copilot) - PR: [Add alzimmermsft to Azure emitter version CODEOWNERS](https://github.com/Azure/azure-sdk-for-net/pull/64382)
- [Bump multer from 2.3.0 to 2.5.0 in /eng/packages/http-client-csharp (…](https://github.com/Azure/azure-sdk-for-net/commit/0a85454290db6ef9f4c2c56cbfa33f393e6318b9) - `2026-10-30T17:00:54Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump multer from 2.3.0 to 2.5.0 in /eng/packages/http-client-csharp](https://github.com/Azure/azure-sdk-for-net/pull/64195)
- [Attestation: set 2.0.0 release date (#64340)](https://github.com/Azure/azure-sdk-for-net/commit/e94aa02884690ef9770c5ab9d3150555a9efd871) - `2026-10-30T16:46:02Z` - Kelvin Sapathy (@ksapathy) - PR: [[Attestation] Set 2.0.0 release date](https://github.com/Azure/azure-sdk-for-net/pull/64340)

### Azure/sap-automation-qa (30 commit(s), signal 150)

Tags: `docs, human-authored, product:Azure AI, release, release-language, watchlist`

- Release: [1.1.5](https://github.com/Azure/sap-automation-qa/releases/tag/1.1.5) - `2026-10-30T14:40:16Z`
- [Change high_availability_agent to use list format](https://github.com/Azure/sap-automation-qa/commit/a9580728e843678d4568057ef7def37c3818f680) - `2026-10-30T14:28:05Z` - Kimmo Forss (@KimForss) - PR: [Release/september 2026](https://github.com/Azure/sap-automation-qa/pull/386)
- [feat: add wait for connection task after indexserver crash (#404)](https://github.com/Azure/sap-automation-qa/commit/b7b772603981c6815da47f94c9507f2f670b541e) - `2026-10-30T14:28:05Z` - Kimmo Forss (@KimForss) - PR: [Release/september 2026](https://github.com/Azure/sap-automation-qa/pull/386)
- [fix: add hashes for azure-common in requirements.txt](https://github.com/Azure/sap-automation-qa/commit/78ffdd5d9d07dded6d670543a52f33c04a6babab) - `2026-10-30T14:28:05Z` - hdamecharla (@hdamecharla) - PR: [Release/september 2026](https://github.com/Azure/sap-automation-qa/pull/386)
- [fix: add hashes for azure-mgmt-network in requirements.txt](https://github.com/Azure/sap-automation-qa/commit/85c99d27f66c0ff5322df3e3d9a68384f650bfad) - `2026-10-30T14:28:05Z` - hdamecharla (@hdamecharla) - PR: [Release/september 2026](https://github.com/Azure/sap-automation-qa/pull/386)
- [Change azure-mgmt-network version to 23.0.0](https://github.com/Azure/sap-automation-qa/commit/9c61bf0702eb2e4c9ee44f1bbdad6c3f04f36679) - `2026-10-30T14:28:05Z` - Kimmo Forss (@KimForss) - PR: [Release/september 2026](https://github.com/Azure/sap-automation-qa/pull/386)

### dotnet/runtime (29 commit(s), signal 65)

Tags: `docs, human-authored`

- [Consolidate PE loading and virtual memory into CoreCLR minipal (#135902)](https://github.com/dotnet/runtime/commit/c4ad2493bbee2da0aee78a74e47edcf441bf0dc9) - `2026-10-30T18:11:06Z` - Jeremy Koritzinsky (@jkoritzinsky) - PR: [Consolidate PE loading and virtual memory into CoreCLR minipal](https://github.com/dotnet/runtime/pull/135902)
- [Avoid quoted cookie attribute allocations (#136704)](https://github.com/dotnet/runtime/commit/0a4458e8e981fd1b4ddbf3cf0752e3a775f42add) - `2026-10-30T15:51:17Z` - Stephen Toub (@stephentoub) - PR: [Avoid quoted cookie attribute allocations](https://github.com/dotnet/runtime/pull/136704)
- [[wasi] Fix WasiHttpHandler request failures, disposal and header hand…](https://github.com/dotnet/runtime/commit/a932cb67bf671398783a89d2c183cb52fda2b546) - `2026-10-30T15:10:52Z` - Larry Ewing (@lewing) - PR: [[wasi] Fix WasiHttpHandler request failures, disposal and header handling](https://github.com/dotnet/runtime/pull/136261)
- [Handle byte swaps in range overflow analysis (#136632)](https://github.com/dotnet/runtime/commit/de42bfa1756cf080b227fc20653db12734d54fae) - `2026-10-30T14:41:33Z` - Nino Floris (@NinoFloris) - PR: [Handle byte swaps in range overflow analysis](https://github.com/dotnet/runtime/pull/136632)
- [Share math helpers between CoreCLR and NativeAOT (#136637)](https://github.com/dotnet/runtime/commit/4ffa73fbc36437953ccae2a50a6282142d49a651) - `2026-10-30T14:10:21Z` - Adeel Mujahid (@am11) - PR: [Share x86 long shift and multiply helpers between CoreCLR and NativeAOT](https://github.com/dotnet/runtime/pull/136637)

### MicrosoftDocs/architecture-center (27 commit(s), signal 100)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #17148 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/architecture-center/commit/81af4b4351f684e7f21d91b18df7ded638a82c54) - `2026-10-30T17:32:04Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #17147 from MicrosoftDocs/router](https://github.com/MicrosoftDocs/architecture-center/commit/10bf3a03078e2666f8f951f908f035252a073dbb) - `2026-10-30T17:16:36Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Remove model routing, it's causing too many problems](https://github.com/MicrosoftDocs/architecture-center/commit/75a3b6bcd63a078099b7494df2b349aa86bd1dd9) - `2026-10-30T17:07:43Z` - Chad Kittel (@ckittel)
- [Merge pull request #17145 from MicrosoftDocs/adjust-routing](https://github.com/MicrosoftDocs/architecture-center/commit/8604166afce00f6def1c492da66b1a2794469908) - `2026-10-30T16:24:45Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Move to balanced](https://github.com/MicrosoftDocs/architecture-center/commit/0dbb29b0df39edc614088a1650cf76b92d30a26d) - `2026-10-30T16:19:43Z` - Chad Kittel (@ckittel)

### microsoftgraph/nodejs-webhooks-sample (25 commit(s), signal 100)

Tags: `docs, human-authored, product:Microsoft Graph, watchlist`

- [Merge pull request #689 from microsoftgraph/dependabot/npm_and_yarn/s…](https://github.com/microsoftgraph/nodejs-webhooks-sample/commit/df72e57baf7e6fcedb4dbce253e0387c231f53ab) - `2026-10-29T20:35:52Z` - github-actions[bot] (@github-actions[bot]) - PR: [chore(deps): Bump serialize-javascript from 7.1.2 to 7.1.4](https://github.com/microsoftgraph/nodejs-webhooks-sample/pull/689)
- [Merge branch 'main' into dependabot/npm_and_yarn/serialize-javascript…](https://github.com/microsoftgraph/nodejs-webhooks-sample/commit/4e2f363b3ab1844b99f8088a9ba46f78d3b0120c) - `2026-10-29T20:34:29Z` - Jason Johnston (@jasonjoh) - PR: [chore(deps): Bump serialize-javascript from 7.1.2 to 7.1.4](https://github.com/microsoftgraph/nodejs-webhooks-sample/pull/689)
- [Merge pull request #688 from microsoftgraph/dependabot/npm_and_yarn/s…](https://github.com/microsoftgraph/nodejs-webhooks-sample/commit/8e1b695ad58716341056b3c3e5f1ddd86cc552e1) - `2026-10-29T20:34:10Z` - github-actions[bot] (@github-actions[bot]) - PR: [chore(deps): Bump socket.io-parser from 4.2.4 to 4.2.7](https://github.com/microsoftgraph/nodejs-webhooks-sample/pull/688)
- [Merge branch 'main' into dependabot/npm_and_yarn/socket.io-parser-4.2.7](https://github.com/microsoftgraph/nodejs-webhooks-sample/commit/4a1fc30f1e2adb8e04cf1eb0d55609731048e7a0) - `2026-10-29T20:33:11Z` - Jason Johnston (@jasonjoh) - PR: [chore(deps): Bump socket.io-parser from 4.2.4 to 4.2.7](https://github.com/microsoftgraph/nodejs-webhooks-sample/pull/688)
- [Merge pull request #687 from microsoftgraph/dependabot/npm_and_yarn/m…](https://github.com/microsoftgraph/nodejs-webhooks-sample/commit/c295ce4ef9c52de209003f89e3afdb1f7a37a9b8) - `2026-10-29T20:32:53Z` - Jason Johnston (@jasonjoh) - PR: [chore(deps): Bump ws, engine.io and socket.io-adapter](https://github.com/microsoftgraph/nodejs-webhooks-sample/pull/687)

### MicrosoftDocs/azure-management-docs (21 commit(s), signal 96)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merge pull request #2998 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-management-docs/commit/e7c3a53341967eaeda4b442bc10531d7f52f0cd2) - `2026-10-30T13:09:26Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #2997 from yhussein896/docs-editor/manage-agent-17…](https://github.com/MicrosoftDocs/azure-management-docs/commit/8100ac5dbf32948030d4ee4afb6f77cd99a51168) - `2026-10-30T12:32:31Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Learn Editor: Update manage-agent.md](https://github.com/MicrosoftDocs/azure-management-docs/commit/55d4f9f1c5c009bc32fad885d125a90e478ce85b) - `2026-10-30T12:27:25Z` - Yunis Hussein (@yhussein896)
- [Learn Editor: Update manage-agent.md](https://github.com/MicrosoftDocs/azure-management-docs/commit/8514d18ab6e84982ed3fb07986831ba1cb1803fe) - `2026-10-30T12:27:16Z` - Yunis Hussein (@yhussein896)
- [Merge pull request #2996 from yhussein896/docs-editor/automatic-agent…](https://github.com/MicrosoftDocs/azure-management-docs/commit/330f3f7d0aa8d49c6f0d328ab3c58327c30ace06) - `2026-10-30T12:23:19Z` - prmerger-automator[bot] (@prmerger-automator[bot])

### MicrosoftDocs/SupportArticles-docs (19 commit(s), signal 94)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/916facb77f9722282eeb153fb06265860ac05e8b) - `2026-10-30T18:06:41Z` - Learn Build Service GitHub App
- [Merge pull request #12751 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/6710a862bd7b9dcd11fac22bf8e116cb59ca7818) - `2026-10-30T18:04:13Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [AB#13257: Azure content clean-up - AKS - Batch 2 (#12728)](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/5158929d0795dab35ab3b87e6df49f0f6493f5cd) - `2026-10-30T17:52:11Z` - Ryan Berg (@ryanberg-aquent)
- [Add MailUser steps to email message format article (#12730)](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/abc440c9f3e8efd956c1f16a0f93d95be753c277) - `2026-10-30T17:18:06Z` - Richard Fajardo (@richfaj)
- [Update in-place-system-upgrade.md (#12750)](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/a8f08be4f2a4fe938ad5f96bc517388a2b91f612) - `2026-10-30T15:36:25Z` - MASA (@m38rtkhs)

### MicrosoftDocs/entra-docs (18 commit(s), signal 103)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/entra-do…](https://github.com/MicrosoftDocs/entra-docs/commit/07cb73d6c6380414eecd040ba5e14c1c94d48b66) - `2026-10-30T17:43:39Z` - Learn Build Service GitHub App
- [Merge pull request #14747 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/entra-docs/commit/40ce4941a26fc21d5c1cab6188a33d1e3e63ffb5) - `2026-10-30T17:40:05Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Clarify supported objects for synchronization cloud pairs (#14745)](https://github.com/MicrosoftDocs/entra-docs/commit/ddf451b78ba8ce367f1515545b2487dc593d9946) - `2026-10-30T14:34:01Z` - ArvindHarinder1 (@ArvindHarinder1)
- [Publish six CYOT GA articles (#14742)](https://github.com/MicrosoftDocs/entra-docs/commit/19ce39e320688384c4552abc24dfa82b679ef833) - `2026-10-30T14:08:47Z` - more-rasika (@more-rasika)
- [Merging changes synced from https://github.com/MicrosoftDocs/entra-do…](https://github.com/MicrosoftDocs/entra-docs/commit/ebd2ad493828db92948c272b97cd4edd8624b368) - `2026-10-30T07:40:04Z` - Learn Build Service GitHub App

### Azure-Samples/enterprise-toolbox (18 commit(s), signal 93)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Merge pull request #18 from Azure-Samples/feaure/seperate_build_deploy](https://github.com/Azure-Samples/enterprise-toolbox/commit/a21393c4d93dd7a7cd7c6df224ca14a7d85b2a0b) - `2026-10-30T17:35:26Z` - David Barkol (@dbarkol) - PR: [Feaure/seperate build deploy](https://github.com/Azure-Samples/enterprise-toolbox/pull/18)
- [Refactor agent deployment workflow and scripts](https://github.com/Azure-Samples/enterprise-toolbox/commit/2a6a2fac0d4223de2b7723d71c11eb12d579bb9e) - `2026-10-30T17:23:33Z` - JFolberth (@JFolberth) - PR: [Feaure/seperate build deploy](https://github.com/Azure-Samples/enterprise-toolbox/pull/18)
- [Normalize environment variable names in deployment workflow and updat…](https://github.com/Azure-Samples/enterprise-toolbox/commit/65ec19b08cf74b5773816bc74b79ce8b9ad8be51) - `2026-10-30T17:15:33Z` - JFolberth (@JFolberth) - PR: [Feaure/seperate build deploy](https://github.com/Azure-Samples/enterprise-toolbox/pull/18)
- [Enhance deployment workflow to include project endpoint outputs and a…](https://github.com/Azure-Samples/enterprise-toolbox/commit/6697ba140a28034e822eecd41e0a1af00f8cf803) - `2026-10-30T17:10:23Z` - JFolberth (@JFolberth) - PR: [Feaure/seperate build deploy](https://github.com/Azure-Samples/enterprise-toolbox/pull/18)
- [Update deployment documentation and Bicep parameters to handle missin…](https://github.com/Azure-Samples/enterprise-toolbox/commit/2fee75929fa907d599bbe012e01814e1a6086ee6) - `2026-10-30T17:05:48Z` - JFolberth (@JFolberth) - PR: [Feaure/seperate build deploy](https://github.com/Azure-Samples/enterprise-toolbox/pull/18)

### microsoft/onnxruntime (18 commit(s), signal 98)

Tags: `human-authored, release, samples`

- Release: [ONNX Runtime v1.30.1](https://github.com/microsoft/onnxruntime/releases/tag/v1.30.1) - `2026-10-29T22:01:54Z`
- Release: [ONNX Runtime WebGPU Plugin EP v0.5.0](https://github.com/microsoft/onnxruntime/releases/tag/plugin-ep-webgpu/v0.5.0) - `2026-10-29T21:30:05Z`
- [Schedule daily CUDA 13 combined wheel builds (#33771)](https://github.com/microsoft/onnxruntime/commit/dd543febefd37da323b11c4c472b4ecb6e81e159) - `2026-10-30T17:28:11Z` - eserscor (@eserscor) - PR: [Schedule daily CUDA 13 combined wheel builds](https://github.com/microsoft/onnxruntime/pull/33771)
- [Make WebGPU CI validation failures blocking (#33715)](https://github.com/microsoft/onnxruntime/commit/9016c6d892dfda99b606ce934b27f135ed625164) - `2026-10-30T16:51:34Z` - Edward Chen (@edgchen1) - PR: [Make WebGPU CI validation failures blocking](https://github.com/microsoft/onnxruntime/pull/33715)
- [Add CUDA BitShift integer kernels (#33647)](https://github.com/microsoft/onnxruntime/commit/103d010b4a3429f92055c4e6206b49408f823e9c) - `2026-10-30T16:46:50Z` - Justin Chu (@justinchuby) - PR: [Add CUDA BitShift integer kernels](https://github.com/microsoft/onnxruntime/pull/33647)
- [Keep a system cuDNN include dir out of the CUDA plugin's include list…](https://github.com/microsoft/onnxruntime/commit/4605d0b437d6d8f42e2a1ca946f139469576c6ab) - `2026-10-30T16:38:16Z` - Arne H Juul (@arnej27959) - PR: [Keep a system cuDNN include dir out of the CUDA plugin's include list](https://github.com/microsoft/onnxruntime/pull/33736)
- [[Pilot] Add region-scoped pattern rewriting through EP capabilities (…](https://github.com/microsoft/onnxruntime/commit/14663eb081b175dca693a0eba20866c6afb6321b) - `2026-10-30T16:33:18Z` - Ti-Tai Wang (@titaiwangms) - PR: [[Pilot] Add region-scoped pattern rewriting through EP capabilities](https://github.com/microsoft/onnxruntime/pull/33652)

### MicrosoftDocs/learn (18 commit(s), signal 93)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/25967204b07a003c72d0dd068b36602380ad112a) - `2026-10-30T17:25:56Z` - Learn Build Service GitHub App
- [Merge pull request #56626 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/learn/commit/b1a078551d133e0408fd9494d1436d04f81bab92) - `2026-10-30T17:16:30Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [update (#56625)](https://github.com/MicrosoftDocs/learn/commit/d1075d6a13135abd0b4f10e2acc615bf22e61fbf) - `2026-10-30T16:11:58Z` - Richelle Swinton (@riswinto)
- [DP-420 add videos to module 02 (#56623)](https://github.com/MicrosoftDocs/learn/commit/8ab776f82f595b6076f218866e1def22bd9b0b32) - `2026-10-30T13:04:23Z` - MScalopez (@MScalopez)
- [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/ba3e37dfeeb813072d81c4a2dfbdfe1d37a260e9) - `2026-10-30T07:24:38Z` - Learn Build Service GitHub App

### Azure/AI-Landing-Zones (16 commit(s), signal 91)

Tags: `docs, human-authored, product:Azure AI, product:Microsoft Graph, watchlist`

- [fix: give documentation navigation room for nested labels](https://github.com/Azure/AI-Landing-Zones/commit/10fe0245f3c4ae6cb315c819cc4e30b9349f1a0c) - `2026-10-30T18:40:31Z` - Paulo Lacerda (@placerda)
- [docs: consolidate Agent Application guides by task](https://github.com/Azure/AI-Landing-Zones/commit/6e3eb0e21b05f446ae21cea87b3706d91b6817d4) - `2026-10-30T18:00:58Z` - Paulo Lacerda (@placerda)
- [docs: clarify homepage architectures and refine typography](https://github.com/Azure/AI-Landing-Zones/commit/b5e14bd4fee86c2211f2a36f0b8011aadb370e1a) - `2026-10-30T17:43:00Z` - Paulo Lacerda (@placerda)
- [docs: publish Agent Landing Zone v5.6.0 guidance](https://github.com/Azure/AI-Landing-Zones/commit/74dff94e5fd475e1eafe7837fa6dbec1ec69178a) - `2026-10-30T15:23:51Z` - Paulo Lacerda (@placerda)
- [docs: refresh validated planner prices](https://github.com/Azure/AI-Landing-Zones/commit/34be4bb81e38f576831a142e654ca75a437f5af8) - `2026-10-30T15:21:36Z` - github-actions[bot] (@github-actions[bot])

### MicrosoftLearning/mslearn-copilotstudio (15 commit(s), signal 100)

Tags: `human-authored, release-language, training, watchlist`

- [Merge pull request #100 from Desiderio25/Update-Copilotstudio-link](https://github.com/MicrosoftLearning/mslearn-copilotstudio/commit/1e34d02e765c34244e829910ca3fb5b413cc7ec0) - `2026-10-30T17:52:40Z` - chandlersyal (@chandlersyal) - PR: [Update Copilot Studio URL](https://github.com/MicrosoftLearning/mslearn-copilotstudio/pull/100)
- [Change Copilot Studio URL in setup instructions](https://github.com/MicrosoftLearning/mslearn-copilotstudio/commit/4798d7a3fec668c4577b9eeffeb8ee62ef26c3a0) - `2026-10-30T16:07:11Z` - André Desidério (@Desiderio25) - PR: [Update Copilot Studio URL](https://github.com/MicrosoftLearning/mslearn-copilotstudio/pull/100)
- [Update Copilot Studio URL from preview to main](https://github.com/MicrosoftLearning/mslearn-copilotstudio/commit/ec10da9735fa07a382481bc7a599bbdd9e63e5ec) - `2026-10-30T16:03:19Z` - André Desidério (@Desiderio25) - PR: [Update Copilot Studio URL](https://github.com/MicrosoftLearning/mslearn-copilotstudio/pull/100)
- [Add files via upload](https://github.com/MicrosoftLearning/mslearn-copilotstudio/commit/7a7c45c12c75ceb4147a5c848fabe64acbb38b1a) - `2026-10-30T15:40:50Z` - André Desidério (@Desiderio25) - PR: [Update Copilot Studio URL](https://github.com/MicrosoftLearning/mslearn-copilotstudio/pull/100)
- [Add files via upload](https://github.com/MicrosoftLearning/mslearn-copilotstudio/commit/0aad76fcd3d2b55c9cda662eaf0f27b7ba0dc617) - `2026-10-30T15:37:53Z` - André Desidério (@Desiderio25) - PR: [Update Copilot Studio URL](https://github.com/MicrosoftLearning/mslearn-copilotstudio/pull/100)

### MicrosoftDocs/sql-docs (14 commit(s), signal 89)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/sql-docs…](https://github.com/MicrosoftDocs/sql-docs/commit/9dc1f4392121b462ceb3dbcfc776a28a9b95dde3) - `2026-10-30T17:39:35Z` - Learn Build Service GitHub App
- [Merge pull request #38534 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/sql-docs/commit/72684c0245176d4c4b3fbf69fe2bf41ff4c2eb87) - `2026-10-30T17:36:49Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add migrate from arc registered agentless sql server instances (#38484)](https://github.com/MicrosoftDocs/sql-docs/commit/8131de3d8cd20e03a555c225ac04b3ab05f2233a) - `2026-10-30T15:55:08Z` - Subhojit Basak (@subhojit-msft)
- [Correct the Express database size limit on Linux for SQL Server 2025 …](https://github.com/MicrosoftDocs/sql-docs/commit/7dbfb28f8b8a08f250fe9750d7865941fc238628) - `2026-10-30T14:57:20Z` - Rudi Bruchez (@rudi-bruchez) - PR: [Correct the Express database size limit in the SQL Server 2025 on Linux editions article](https://github.com/MicrosoftDocs/sql-docs/pull/10453)
- [Merge pull request #38527 from lcwright/lcwright/whats-new-db-hub-rem…](https://github.com/MicrosoftDocs/sql-docs/commit/8e6d6b15ba3398e5878fca8ef56bf9d63a8af036) - `2026-10-29T23:52:44Z` - prmerger-automator[bot] (@prmerger-automator[bot])

### MicrosoftDocs/azure-docs-sdk-python (11 commit(s), signal 86)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/40cb183b9783176b12fb4c5807f321ee28c1914d) - `2026-10-30T18:32:42Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/d6d22a82cc4d69f1764dfa12fcf23ab2aba2d533) - `2026-10-30T09:23:47Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/4adb831aef059fcb0977b3faa425c4459d179351) - `2026-10-30T07:12:37Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/5b4075e47156e21b364ba50d1c92ce0e59c4875d) - `2026-10-30T07:09:10Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/969b0fb157121b51abb7382334f86461fe119d20) - `2026-10-30T06:13:08Z` - azure-sdk (@azure-sdk)

### Azure/azure-sdk-for-java (11 commit(s), signal 161)

Tags: `docs, human-authored, product:Azure AI, product:Azure SDK, release, release-language, security, watchlist`

- Release: [com.azure+azure-ai-agents_2.9.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-ai-agents_2.9.0) - `2026-10-30T17:16:32Z`
- Release: [com.azure+azure-ai-projects_2.9.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-ai-projects_2.9.0) - `2026-10-30T17:16:18Z`
- Release: [com.azure+azure-sdk-template_1.2.1-beta.7021230](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-sdk-template_1.2.1-beta.7021230) - `2026-10-30T16:50:38Z`
- Release: [com.azure.resourcemanager+azure-resourcemanager-privatetrafficmanager_1.0.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-privatetrafficmanager_1.0.0-beta.1) - `2026-10-30T07:42:52Z`
- Release: [com.azure.resourcemanager+azure-resourcemanager-aiinfraoptimization_1.0.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-aiinfraoptimization_1.0.0-beta.1) - `2026-10-30T02:28:37Z`
- [Clarify managed identity selection in credential builder documentatio…](https://github.com/Azure/azure-sdk-for-java/commit/df2d7d416eb47e1be684c02ae1507d1b4a3f5657) - `2026-10-30T18:10:42Z` - hidingmyname (@hidingmyname) - PR: [Clarify managed identity selection in credential builder documentation](https://github.com/Azure/azure-sdk-for-java/pull/51021)
- [Upgrade Java ESRP publishing to v14 and production publisher (#51040)](https://github.com/Azure/azure-sdk-for-java/commit/c650ff1c7a2e1092af0f8847c1996e937637fec1) - `2026-10-30T17:42:20Z` - Ray Chen (@raych1) - PR: [Upgrade Java ESRP publishing to v14 and production publisher](https://github.com/Azure/azure-sdk-for-java/pull/51040)
- [Release azure-ai-agents and azure-ai-projects 2.9.0 (#51031)](https://github.com/Azure/azure-sdk-for-java/commit/e91e643356abd7d170a98d4602275bf8a9c6a242) - `2026-10-30T15:17:09Z` - Kaylie (@kaylieee) - PR: [Release azure-ai-agents and azure-ai-projects 2.9.0](https://github.com/Azure/azure-sdk-for-java/pull/51031)
- [[Automation] Generate SDK based on TypeSpec 0.48.5 (#51036)](https://github.com/Azure/azure-sdk-for-java/commit/ae6ef9f1f78146ad4eebfb627107bc5692b17017) - `2026-10-30T10:39:59Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[skip ci] [Automation] Generate SDK based on TypeSpec 0.48.5](https://github.com/Azure/azure-sdk-for-java/pull/51036)
- [Increase TypeSpec SDK sync timeout to four hours (#51035)](https://github.com/Azure/azure-sdk-for-java/commit/c54907ef15a41421a84362bc0f30ac139183b311) - `2026-10-30T04:47:05Z` - Weidong Xu (@weidongxu-microsoft) - PR: [Increase TypeSpec SDK sync timeout to four hours](https://github.com/Azure/azure-sdk-for-java/pull/51035)

### microsoft/viva-insights-sample-code (10 commit(s), signal 50)

Tags: `human-authored, samples`

- [Merge pull request #37 from microsoft/martinctc/skills-catalogue-dialog](https://github.com/microsoft/viva-insights-sample-code/commit/dc57d74f4b760204d6a179ab4a4d524fe9f400dd) - `2026-10-30T16:46:53Z` - Martin Chan (@martinctc) - PR: [docs(site): add Skills and Prompt Library catalogue dialogs](https://github.com/microsoft/viva-insights-sample-code/pull/37)
- [feat: Enhance quick prompt code block for accessibility](https://github.com/microsoft/viva-insights-sample-code/commit/e219d2f1a91a2fd1a262efbc9f1ef9fe5738f7c6) - `2026-10-30T16:44:08Z` - Martin Chan (@martinctc) - PR: [docs(site): add Skills and Prompt Library catalogue dialogs](https://github.com/microsoft/viva-insights-sample-code/pull/37)
- [fix(site): preserve catalogue fragment history](https://github.com/microsoft/viva-insights-sample-code/commit/5ce0e0b81195bb87b1095b57c7e37cb747db5fcb) - `2026-10-30T15:52:04Z` - Martin Chan (@martinctc) - PR: [docs(site): add Skills and Prompt Library catalogue dialogs](https://github.com/microsoft/viva-insights-sample-code/pull/37)
- [fix(site): harden catalogue prompts and dialogs](https://github.com/microsoft/viva-insights-sample-code/commit/f594db90dac5e6b77fe1b1d0dc8a9c3c8d6a5c56) - `2026-10-30T15:41:41Z` - Martin Chan (@martinctc) - PR: [docs(site): add Skills and Prompt Library catalogue dialogs](https://github.com/microsoft/viva-insights-sample-code/pull/37)
- [chore(site): integrate Skills catalogue branch](https://github.com/microsoft/viva-insights-sample-code/commit/185102c2dbe364a27273b578d107751106141092) - `2026-10-30T14:56:09Z` - Martin Chan (@martinctc) - PR: [docs(site): add Skills and Prompt Library catalogue dialogs](https://github.com/microsoft/viva-insights-sample-code/pull/37)

### microsoftgraph/microsoft-graph-docs-contrib (10 commit(s), signal 85)

Tags: `docs, human-authored, product:Microsoft Graph, watchlist`

- [Merge pull request #10084 from microsoftgraph/main639289177912419612s…](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/a69303123e9701eecbf56568d152ece936a97f1e) - `2026-10-30T00:43:29Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10084)
- [Merging changes synced from https://github.com/microsoftgraph/microso…](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/f9505c7471b69f1be6ed4814490a2da248fdac60) - `2026-10-30T00:43:07Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10084)
- [Merge pull request #29833 from microsoftgraph/main](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/97e53c58373cff6ce3479c31f14d9ea6ddc9a18f) - `2026-10-30T00:36:50Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10084)
- [Update generated permissions tables with build 255361 (#29819)](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/a8040fa92fcefe77dc454cde438289e5b04b0b26) - `2026-10-29T20:43:13Z` - snippet-gen-pull-automation[bot] (@snippet-gen-pull-automation[bot]) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10084)
- [Update generated permissions tables with build 255916 (#29827)](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/ac5e3408b1733b2eed6cd414cf0cc9176d226d90) - `2026-10-29T20:40:40Z` - snippet-gen-pull-automation[bot] (@snippet-gen-pull-automation[bot]) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10084)

### MicrosoftDocs/azure-stack-docs (10 commit(s), signal 85)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #4571 from MicrosoftDocs/main639289082910857316syn…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/746e4286678a2cda0e89d0b7e5764aa2b010d402) - `2026-10-29T22:05:08Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4571)
- [Merging changes synced from https://github.com/MicrosoftDocs/azure-st…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/926e458c7d4fef0a879bac22a64e8dc3f1c032da) - `2026-10-29T22:04:48Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4571)
- [Merge pull request #21963 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-stack-docs/commit/2475799e521085c1337de6a56bbab054c0ea5909) - `2026-10-29T22:03:31Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4571)
- [Merge pull request #21962 from RaghvendraMandawale/patch-20](https://github.com/MicrosoftDocs/azure-stack-docs/commit/e583d33113e432bf6410deaeaa95d3de2de1645a) - `2026-10-29T18:11:03Z` - prmerger-automator[bot] (@prmerger-automator[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4571)
- [Merge pull request #21961 from RaghvendraMandawale/patch-19](https://github.com/MicrosoftDocs/azure-stack-docs/commit/3013b22b12495f1d68ae21f0a67d6195057ef8a9) - `2026-10-29T18:08:26Z` - prmerger-automator[bot] (@prmerger-automator[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4571)

### Azure/azure-sdk-for-python (9 commit(s), signal 124)

Tags: `docs, human-authored, product:Azure AI, product:Azure SDK, release, watchlist`

- Release: [azure-communication-callautomation_1.6.1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-communication-callautomation_1.6.1) - `2026-10-30T18:18:39Z`
- Release: [azure-mgmt-storagemover_3.2.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-storagemover_3.2.0) - `2026-10-30T09:05:07Z`
- Release: [azure-ai-agentserver-responses_2.4.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-responses_2.4.0) - `2026-10-30T06:53:10Z`
- Release: [azure-ai-agentserver-invocations_1.3.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-invocations_1.3.0) - `2026-10-30T06:52:25Z`
- Release: [azure-mgmt-aiinfraoptimization_1.0.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-aiinfraoptimization_1.0.0b1) - `2026-10-30T05:59:42Z`
- [[AgentServer] Add A2A protocol host package (#49649)](https://github.com/Azure/azure-sdk-for-python/commit/45f54ab3362815122a3b946d6f15cc065760dfdb) - `2026-10-30T18:38:22Z` - Hameed Kunkanoor (@Hameedkunkanoor) - PR: [[AgentServer] Add A2A protocol host package](https://github.com/Azure/azure-sdk-for-python/pull/49649)
- [[Bug Fix] Invoke `AzureAppConfigurationProvider` `on_refresh_success`…](https://github.com/Azure/azure-sdk-for-python/commit/7e50a03b2567184d443216c0c800ea55a1bc40c3) - `2026-10-30T18:01:21Z` - Sergei Aleshin (@s-aleshin) - PR: [[Bug Fix] Invoke `AzureAppConfigurationProvider` `on_refresh_success` callback for empty feature flag refresh](https://github.com/Azure/azure-sdk-for-python/pull/49216)
- [Feature/azure ai projects/vnext (#49710)](https://github.com/Azure/azure-sdk-for-python/commit/84a6db9b91535e03d6a2b232d71dda4277a58f02) - `2026-10-30T16:39:01Z` - Howie Leung (@howieleung) - PR: [Feature/azure ai projects/vnext](https://github.com/Azure/azure-sdk-for-python/pull/49710)
- [[AutoPR azure-mgmt-storagemover]-generated-from-SDK Generation - Pyth…](https://github.com/Azure/azure-sdk-for-python/commit/eae424de17dd2fdac648c3dd7eee588db53dec2c) - `2026-10-30T07:16:37Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-mgmt-storagemover]-generated-from-SDK Generation - Python-6798570](https://github.com/Azure/azure-sdk-for-python/pull/48930)
- [[AutoPR azure-mgmt-aiinfraoptimization]-generated-from-SDK Generation…](https://github.com/Azure/azure-sdk-for-python/commit/58678ae3dadfc8a3a729f9aacd2fa30da3bcae03) - `2026-10-30T03:58:12Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-mgmt-aiinfraoptimization]-generated-from-SDK Generation - Python-7018460](https://github.com/Azure/azure-sdk-for-python/pull/49756)

### Azure/azure-dev (9 commit(s), signal 94)

Tags: `human-authored, product:Azure AI, release-language, samples, watchlist`

- [deps: migrate pty to v2.0.1 (#10602)](https://github.com/Azure/azure-dev/commit/d5ed6cd86f45dc7c44da353d6bc4f5a3ef20d873) - `2026-10-30T18:29:28Z` - Victor Vazquez (@vhvb1989) - PR: [deps: migrate pty to v2.0.1](https://github.com/Azure/azure-dev/pull/10602)
- [chore(review): narrow extension contract findings (#10796)](https://github.com/Azure/azure-dev/commit/d18af6b1153ad838f2d262d742d1c95eaa968972) - `2026-10-30T18:13:34Z` - Travis Angevine (@trangevi) - PR: [chore(review): narrow extension contract findings](https://github.com/Azure/azure-dev/pull/10796)
- [fix(agents): validate hosted agent resource configuration (#10559)](https://github.com/Azure/azure-dev/commit/de60993667f7a2982bfc6c5e9247fd633dfec743) - `2026-10-30T09:25:58Z` - Yimin-Jin (@Yimin-Jin) - PR: [fix(agents): validate hosted agent resource configuration](https://github.com/Azure/azure-dev/pull/10559)
- [Support current GA Telephony transfer destination wire format (#10780)](https://github.com/Azure/azure-dev/commit/fd0286f9198fcf0e54438f2ff4249c2d3dde89b2) - `2026-10-30T07:21:24Z` - JianW (@v1212) - PR: [Support current GA Telephony transfer destination wire format](https://github.com/Azure/azure-dev/pull/10780)
- [Fix remote template loading timing in agent Init (#10790)](https://github.com/Azure/azure-dev/commit/1ca7e9865530864ed636851e75708cc87a521f64) - `2026-10-30T02:31:23Z` - JerryYang (@JerryYangKai) - PR: [Fix remote template loading timing in agent Init](https://github.com/Azure/azure-dev/pull/10790)

### MicrosoftDocs/azure-docs-sdk-dotnet (9 commit(s), signal 84)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/57d15d6611df26d60c6f9677ebae29cc3515cbcd) - `2026-10-30T18:25:02Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/55d121a500fcd2023aa6df53743c96e06c5908f7) - `2026-10-30T18:02:02Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/ef2c6f9b793660e3ffc4eb7d6bece3d7cc791c88) - `2026-10-30T12:38:52Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/e3b81dcaf230840e9808bf8c449082984af0b711) - `2026-10-30T11:56:58Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/ffe6db753f7056ad161c81ef1ceea4553fefa552) - `2026-10-30T10:08:46Z` - azure-sdk (@azure-sdk)

### Azure/azure-sdk-for-js (9 commit(s), signal 124)

Tags: `docs, human-authored, product:Azure AI, product:Azure SDK, release, watchlist`

- Release: [@azure/ai-projects_2.10.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/ai-projects_2.10.0) - `2026-10-30T17:10:46Z`
- Release: [@azure/arm-netapp_25.1.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-netapp_25.1.0-beta.1) - `2026-10-30T05:01:45Z`
- Release: [@azure/arm-aiinfraoptimization_1.0.0-beta.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-aiinfraoptimization_1.0.0-beta.1) - `2026-10-30T04:59:12Z`
- Release: [@azure/identity-vscode_2.2.3](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/identity-vscode_2.2.3) - `2026-10-29T23:19:30Z`
- Release: [@azure/identity_4.14.1](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/identity_4.14.1) - `2026-10-29T22:03:50Z`
- [[ai-projects] [Foundry] Foundry SDK v2.10.0 (#40507)](https://github.com/Azure/azure-sdk-for-js/commit/4f0d3e14fde39ef3fb9bce4ffdb8265d9b75fa06) - `2026-10-30T15:58:02Z` - Glenn Harper (@glharper) - PR: [[ai-projects] [Foundry] Foundry SDK v2.10.0](https://github.com/Azure/azure-sdk-for-js/pull/40507)
- [[AutoPR @azure-provisioning-keyvault]-generated-from-SDK Generation -…](https://github.com/Azure/azure-sdk-for-js/commit/fa853efb2d107863e2f774f03c901821f82ab07e) - `2026-10-30T09:33:48Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR @azure-provisioning-keyvault]-generated-from-SDK Generation - JS-7014417](https://github.com/Azure/azure-sdk-for-js/pull/40558)
- [[mgmt]improve mgmt review guideline (#40559)](https://github.com/Azure/azure-sdk-for-js/commit/a6a590842bded6acd90bd57dbcbce732f6738caa) - `2026-10-30T09:10:22Z` - ZiWei Chen (@kazrael2119) - PR: [[mgmt]improve mgmt review guideline](https://github.com/Azure/azure-sdk-for-js/pull/40559)
- [[AutoPR @azure-arm-netapp]-generated-from-SDK Generation - JS-7008836…](https://github.com/Azure/azure-sdk-for-js/commit/cbd286b8c0a7bf50ed7117e5b1bb2b6c65629c71) - `2026-10-30T04:07:20Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR @azure-arm-netapp]-generated-from-SDK Generation - JS-7008836](https://github.com/Azure/azure-sdk-for-js/pull/40537)
- [[AutoPR @azure-arm-aiinfraoptimization]-generated-from-SDK Generation…](https://github.com/Azure/azure-sdk-for-js/commit/67f7528a6bb737e0ba3a71261f7d6827c3e99f44) - `2026-10-30T03:57:33Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR @azure-arm-aiinfraoptimization]-generated-from-SDK Generation - JS-7013434](https://github.com/Azure/azure-sdk-for-js/pull/40555)

### MicrosoftDocs/dynamics-365-contact-center (9 commit(s), signal 84)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/e089627d733ceca7dfb08180378d884c763b1952) - `2026-10-30T14:51:12Z` - Learn Build Service GitHub App
- [Live Publish (#782)](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/5ead239d4e9432d82600d82d7e0f4fcaa2b9c733) - `2026-10-30T14:50:47Z` - Bishal Goswami (@bishalgoswami)
- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/14dd7f2639d7f7c5ccfcc760983a5aa9f3e2da08) - `2026-10-30T13:03:05Z` - Learn Build Service GitHub App
- [Merge pull request #781 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/3ebaccb928d0ebd430b0290f7e03f9c55152295b) - `2026-10-30T13:02:43Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Proactive voice outcomes: SIP 480 is reported as NoAnswer (#748)](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/fa7ca8eaabffdfe2b3608cbf04da5fd41c12be95) - `2026-10-30T08:30:10Z` - ltnsali (@ltnsali)

### MicrosoftDocs/azure-docs-sdk-node (7 commit(s), signal 82)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/c5efa5359182216547e347b4627016bb6a1adde5) - `2026-10-30T17:18:32Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/6cb18e6a9f94d98d0e48d536c8a1face2045f58a) - `2026-10-30T05:11:59Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/787db21e79463b27cba63f2c4d5e57a1fa05039d) - `2026-10-30T05:07:26Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/a2c5423bff328801934d4e46f62a2be48fe2ea35) - `2026-10-29T23:28:35Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/d2a833d676398f2403a476012901b8ff515cd2a9) - `2026-10-29T23:28:20Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/azure-aks-docs (7 commit(s), signal 92)

Tags: `docs, human-authored, release-language, watchlist`

- [Merge pull request #4098 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-aks-docs/commit/069cd91a5bfdd67b1bfde6b71087415ad240de6e) - `2026-10-30T17:04:09Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [initial draft of base to automatic migration guide (#4058)](https://github.com/MicrosoftDocs/azure-aks-docs/commit/3aecd7658cbc396898a24ff8065395977ed0e1f0) - `2026-10-30T15:56:45Z` - Steve Griffith (@swgriffith)
- [Merge pull request #4093 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-aks-docs/commit/8829cab24f8129857b021296a6ac783915da0042) - `2026-10-29T22:10:31Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add KubeRay sample workload validation (#4067)](https://github.com/MicrosoftDocs/azure-aks-docs/commit/b478bd36702ae8055d049145dc6e92480448d19a) - `2026-10-29T21:51:41Z` - Alyssa Vu (@alyssa1303)
- [docs: refresh AppNet supported versions (#4074)](https://github.com/MicrosoftDocs/azure-aks-docs/commit/d0ff0d8a2bf91fb86a5b3d69c86ca8854e6600c8) - `2026-10-29T21:22:05Z` - Jack Ma (@jack4it)

### microsoft/vscode-docs (7 commit(s), signal 92)

Tags: `docs, human-authored, release-language, watchlist`

- [Merge pull request #10563 from yamachu/v144-bracket-escape](https://github.com/microsoft/vscode-docs/commit/af4859a5fb06e699ca687d0bd56367f5ed0f3399) - `2026-10-30T14:41:03Z` - Nick Trogh (@ntrogh) - PR: [Fix missing placeholders in VS Code 1.144 release notes](https://github.com/microsoft/vscode-docs/pull/10563)
- [Merge pull request #10566 from microsoft/ntrogh/remote-access-local](https://github.com/microsoft/vscode-docs/commit/b4065a6180c7859b9a692e4216fe0270a6354455) - `2026-10-30T14:39:25Z` - Nick Trogh (@ntrogh) - PR: [Clarify extension access in remote development](https://github.com/microsoft/vscode-docs/pull/10566)
- [Merge pull request #10565 from microsoft/docs/custom-instructions-get…](https://github.com/microsoft/vscode-docs/commit/8b84eb2f4b6aebd1a11a6239c90f4fc89a5bc699) - `2026-10-30T14:25:14Z` - Nick Trogh (@ntrogh) - PR: [Improve custom instructions docs](https://github.com/microsoft/vscode-docs/pull/10565)
- [Clarify extension access in remote development](https://github.com/microsoft/vscode-docs/commit/551520e103fa1a2aedd9e42a85943fab4af0f305) - `2026-10-30T14:19:05Z` - Nick Trogh (@ntrogh) - PR: [Clarify extension access in remote development](https://github.com/microsoft/vscode-docs/pull/10566)
- [Refactor documentation for Custom Instructions and troubleshooting](https://github.com/microsoft/vscode-docs/commit/c59cab40a63984da32e89d8dd1d8dcd2f829898c) - `2026-10-30T14:12:41Z` - Nick Trogh (@ntrogh) - PR: [Improve custom instructions docs](https://github.com/microsoft/vscode-docs/pull/10565)

### MicrosoftDocs/powerapps-docs (7 commit(s), signal 82)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/powerapp…](https://github.com/MicrosoftDocs/powerapps-docs/commit/cca413dad6b2e8b50dd2fd82c136fd6691077336) - `2026-10-30T13:08:01Z` - Learn Build Service GitHub App
- [Merge pull request #12798 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/powerapps-docs/commit/183a4633f0d941865b05ffbf6b85afb7d182c63b) - `2026-10-30T13:05:47Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Modern personal settings transition](https://github.com/MicrosoftDocs/powerapps-docs/commit/334a45104731de79d13e5e0786235aa3d09fa8ca) - `2026-10-30T12:56:54Z` - Jason Green (@jasongre)
- [Update native app quickstart](https://github.com/MicrosoftDocs/powerapps-docs/commit/99dd3d3b6138585c7ff2b17499ea8bf3530da310) - `2026-10-30T10:04:40Z` - Shweta (@shwetamurkute)
- [Merging changes synced from https://github.com/MicrosoftDocs/powerapp…](https://github.com/MicrosoftDocs/powerapps-docs/commit/ccb381149458b8fec4c565c8ece5786f4a647071) - `2026-10-30T01:05:49Z` - Learn Build Service GitHub App

### MicrosoftDocs/visualstudio-docs (7 commit(s), signal 82)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #11474 from MicrosoftDocs/main639289084346434638sy…](https://github.com/MicrosoftDocs/visualstudio-docs/commit/fedd646924b5e9d7986a4af2be669efa5fe0c29f) - `2026-10-29T22:07:30Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11474)
- [Merging changes synced from https://github.com/MicrosoftDocs/visualst…](https://github.com/MicrosoftDocs/visualstudio-docs/commit/17e9b256e7dff474d86ab54ffbca7dd0db775dd5) - `2026-10-29T22:07:11Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11474)
- [Merge pull request #15781 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/visualstudio-docs/commit/4da9bb2df4e19e86e632e804daf174777d8b5d72) - `2026-10-29T22:04:41Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11474)
- [Update delete-license documentation (#15780)](https://github.com/MicrosoftDocs/visualstudio-docs/commit/4a3334cf2daa3f56be1a1aaa1e70cf7996036922) - `2026-10-29T21:16:07Z` - A-Haage (@A-Haage) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11474)
- [Merge pull request #15779 from A-Haage/A-Haage-patch-256907](https://github.com/MicrosoftDocs/visualstudio-docs/commit/1dc34a44bc6e14e904642670d317f9b3d4cb1432) - `2026-10-29T18:56:04Z` - prmerger-automator[bot] (@prmerger-automator[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11474)

### Azure/azure-managed-grafana (7 commit(s), signal 82)

Tags: `human-authored, samples, watchlist`

- [docs: streamline Azure Monitor MCP guide](https://github.com/Azure/azure-managed-grafana/commit/cf1fa680b96df7c1a9a6008744bd2b6d91c64284) - `2026-10-29T19:51:59Z` - Wuyi Weng (@weng5e)
- [docs: prioritize Azure Monitor query tools in MCP guide](https://github.com/Azure/azure-managed-grafana/commit/ca67a3d18f32f2faacce3880ec31a33c7b4a2526) - `2026-10-29T19:46:07Z` - Wuyi Weng (@weng5e)
- [docs: improve Azure Monitor MCP quick start and log guidance](https://github.com/Azure/azure-managed-grafana/commit/590e2520e9fef3ba3fd35c4a751f01e6bd18a84b) - `2026-10-29T19:43:08Z` - Wuyi Weng (@weng5e)
- [docs: remove cost analysis from Azure Monitor MCP guide](https://github.com/Azure/azure-managed-grafana/commit/8ef9ef9a32d817bb5fe19558d93434a870754f47) - `2026-10-29T19:37:01Z` - Wuyi Weng (@weng5e)
- [docs: add one-click Azure Monitor MCP installation](https://github.com/Azure/azure-managed-grafana/commit/2e2108801e9b0f59d86a0a910f59f92249b9887a) - `2026-10-29T19:00:21Z` - Wuyi Weng (@weng5e)

### Azure-Samples/ms-identity-ciam-native-javascript-samples (6 commit(s), signal 91)

Tags: `human-authored, product:Azure SDK, release-language, samples, watchlist`

- [Merge pull request #69 from Azure-Samples/diegoje/documentation-release](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/commit/91d8d48421c0eb86d09a9d5b2766eeca0f45198c) - `2026-10-30T18:18:01Z` - Diego Jerez (@diegojerezba) - PR: [Add passkey naming and broaden authenticator choices](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/pull/69)
- [Update readme](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/commit/969065ebe5dc3956e29dee34605cb8a1594fc3b1) - `2026-10-30T17:40:05Z` - Diego Jerez (@diegojerezba) - PR: [Add passkey naming and broaden authenticator choices](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/pull/69)
- [Enable local and external authenticators](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/commit/ffe6336450227ff2de374f8bd068e782f25d00b4) - `2026-10-30T17:36:23Z` - Diego Jerez (@diegojerezba) - PR: [Add passkey naming and broaden authenticator choices](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/pull/69)
- [Add name to passkey](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/commit/960071a53b0fe09d1edaaf97868f729fb64ddeec) - `2026-10-30T17:36:23Z` - Diego Jerez (@diegojerezba) - PR: [Add passkey naming and broaden authenticator choices](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/pull/69)
- [Update Readme](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/commit/92cd47d06084e5998dc84cb431191098d36fcd87) - `2026-10-30T17:36:23Z` - Diego Jerez (@diegojerezba) - PR: [Add passkey naming and broaden authenticator choices](https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples/pull/69)

### MicrosoftDocs/m365copilot-docs (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/m365copi…](https://github.com/MicrosoftDocs/m365copilot-docs/commit/7a9f68194ef55755117362a38a77ce0a82267057) - `2026-10-30T17:33:29Z` - Learn Build Service GitHub App
- [Merge pull request #1765 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/m365copilot-docs/commit/2991f9e70b59c89f58d32e30793904e4d555a18c) - `2026-10-30T17:32:58Z` - Jason Johnston (@jasonjoh)
- [Update cloud support status (#1764)](https://github.com/MicrosoftDocs/m365copilot-docs/commit/71f17a0bd1b4578a732575cf590e6bf313970141) - `2026-10-30T17:19:00Z` - Jason Johnston (@jasonjoh)
- [Remove provider qualifier from SharePoint Tools documentation (#1763)](https://github.com/MicrosoftDocs/m365copilot-docs/commit/fbf2ee6ec7c627a13833c67e3aa4ef088e7e5b0e) - `2026-10-30T14:13:36Z` - Patrick Rodgers (@patrick-rodgers)
- [Streamline Copilot and agent pre-commit validation (#1762)](https://github.com/MicrosoftDocs/m365copilot-docs/commit/a5647fee2462a76e3dddd3a4e7d4be7e3e52ab30) - `2026-10-29T19:33:15Z` - Jason Johnston (@jasonjoh)

### dotnet/roslyn (6 commit(s), signal 91)

Tags: `docs, human-authored, product:Azure SDK, release-language, watchlist`

- [Remove a bunch of ProjectReference Name properties (#86253)](https://github.com/dotnet/roslyn/commit/5f643f9ad5dfec1a0f7736dcb8812a831499302d) - `2026-10-30T17:31:06Z` - Jason Malinowski (@jasonmalinowski) - PR: [Remove a bunch of ProjectReference Name properties](https://github.com/dotnet/roslyn/pull/86253)
- [Unsafe evolution: warn for deprecated feature flag (#86224)](https://github.com/dotnet/roslyn/commit/3b229441ea176b34c6ab891eb540f4f52c48c59f) - `2026-10-30T13:38:31Z` - Jan Jones (@jjonescz) - PR: [Unsafe evolution: warn for deprecated feature flag](https://github.com/dotnet/roslyn/pull/86224)
- [Remove a bunch of ProjectReference Name properties](https://github.com/dotnet/roslyn/commit/1272c082c6cda2ac97a3276a0b44c9ac48c7fd4d) - `2026-10-29T23:14:32Z` - Jason Malinowski (@jasonmalinowski) - PR: [Remove a bunch of ProjectReference Name properties](https://github.com/dotnet/roslyn/pull/86253)
- [Keep the margin menu open when toggling inheritance (#86201)](https://github.com/dotnet/roslyn/commit/dcfa99c3da434035cba7aa4c41f33b8b849a0b8c) - `2026-10-29T23:01:15Z` - Jason Malinowski (@jasonmalinowski) - PR: [Keep the margin menu open when toggling inheritance](https://github.com/dotnet/roslyn/pull/86201)
- [Preserve text during conversion operator recovery (#86252)](https://github.com/dotnet/roslyn/commit/6f4fb6dbba6652102f048e0f421c4999d8f12cb0) - `2026-10-29T20:42:12Z` - Fred Silberberg (@333fred) - PR: [Preserve text during conversion operator recovery](https://github.com/dotnet/roslyn/pull/86252)

### microsoftgraph/msgraph-sample-github-connector-dotnet (6 commit(s), signal 46)

Tags: `bot-only, dependency-noise, product:Microsoft Graph, samples, security, watchlist`

- [Merge pull request #124 from microsoftgraph/dependabot/nuget/src/mult…](https://github.com/microsoftgraph/msgraph-sample-github-connector-dotnet/commit/f9113752305000c67d3a659c2ff2ab5ad7f3ec65) - `2026-10-30T17:02:53Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump Microsoft.Extensions.Configuration.Json and Microsoft.Extensions.Configuration.UserSecrets](https://github.com/microsoftgraph/msgraph-sample-github-connector-dotnet/pull/124)
- [Bump Microsoft.Extensions.Configuration.Json and Microsoft.Extensions…](https://github.com/microsoftgraph/msgraph-sample-github-connector-dotnet/commit/3045ae08f0af92610deeebbd3eb460057d895a9d) - `2026-10-30T17:02:14Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Extensions.Configuration.Json and Microsoft.Extensions.Configuration.UserSecrets](https://github.com/microsoftgraph/msgraph-sample-github-connector-dotnet/pull/124)
- [Merge pull request #122 from microsoftgraph/dependabot/nuget/src/Micr…](https://github.com/microsoftgraph/msgraph-sample-github-connector-dotnet/commit/e2c6cd86ec981fcf27aa380c815846db85bdc116) - `2026-10-30T16:58:52Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump Microsoft.Extensions.Configuration.Binder from 10.0.13 to 10.0.14](https://github.com/microsoftgraph/msgraph-sample-github-connector-dotnet/pull/122)
- [Bump Microsoft.Extensions.Configuration.Binder from 10.0.13 to 10.0.14](https://github.com/microsoftgraph/msgraph-sample-github-connector-dotnet/commit/58bb0d42aafe047181b3d04e33742a5b59e9fd7a) - `2026-10-30T16:58:14Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Extensions.Configuration.Binder from 10.0.13 to 10.0.14](https://github.com/microsoftgraph/msgraph-sample-github-connector-dotnet/pull/122)
- [Merge pull request #121 from microsoftgraph/dependabot/nuget/src/Mark…](https://github.com/microsoftgraph/msgraph-sample-github-connector-dotnet/commit/392275b8c10bbe639fa9eb2c3d37e9bb1ea89e47) - `2026-10-30T16:54:51Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump Markdig from 1.4.2 to 1.5.1](https://github.com/microsoftgraph/msgraph-sample-github-connector-dotnet/pull/121)

### dotnet/docs (6 commit(s), signal 91)

Tags: `docs, human-authored, product:Azure SDK, release-language, watchlist`

- [Update package index with latest published versions (#56637)](https://github.com/dotnet/docs/commit/bcbe167f3f4c10a1ad845283784184ec69af4616) - `2026-10-30T15:00:24Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Update package index with latest published versions](https://github.com/dotnet/docs/pull/56637)
- [Document EXTOBS0003: HybridCacheOptions.DisableCompression is obsolet…](https://github.com/dotnet/docs/commit/7dade3318e24a958aa95942290b1bd92dbdcda4c) - `2026-10-30T15:00:00Z` - Petr Onderka (@svick) - PR: [Document EXTOBS0003: HybridCacheOptions.DisableCompression is obsolete](https://github.com/dotnet/docs/pull/56636)
- [Update package index with latest published versions (#56634)](https://github.com/dotnet/docs/commit/faf8e5d14b5ff22f4be9e6a4d182b8bd18103a80) - `2026-10-29T20:37:24Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Update package index with latest published versions](https://github.com/dotnet/docs/pull/56634)
- [Document breaking change: Generated WMI wrappers implement IDisposabl…](https://github.com/dotnet/docs/commit/cf53942c42b6d8e187a5be0205f0bd4e8bbf8879) - `2026-10-29T20:36:16Z` - surya pratap singh (@SkyDevLab) - PR: [Document breaking change: Generated WMI wrappers implement IDisposable](https://github.com/dotnet/docs/pull/56474)
- [Document breaking change: Empty strings in chained configuration over…](https://github.com/dotnet/docs/commit/a653bceef11972f5b799e470b72c5d0e10bc582a) - `2026-10-29T20:31:28Z` - surya pratap singh (@SkyDevLab) - PR: [Document breaking change: Empty strings in chained configuration now override earlier providers](https://github.com/dotnet/docs/pull/56472)

### microsoft/voice-agent (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Add Conference Concierge template (Ignite 2026, official data) and co…](https://github.com/microsoft/voice-agent/commit/0150ee613b914a8ad668a3ee77dafca28376fa85) - `2026-10-30T12:19:24Z` - uchihaqyf-bot (@uchihaqyf-bot) - PR: [Add Conference Concierge template (Ignite 2026, official data) and conference MCP pack](https://github.com/microsoft/voice-agent/pull/91)
- [Add shared SIP system tools and Genesys setup to the sample (#93)](https://github.com/microsoft/voice-agent/commit/3d8e398006154a05a358e408dd062a4b017c8f59) - `2026-10-30T12:16:43Z` - liangxu (@21eutidyt9d67r1) - PR: [Add shared SIP system tools and Genesys setup to the sample](https://github.com/microsoft/voice-agent/pull/93)
- [Add Foundry evaluation tutorial and preliminary Python runner (#94)](https://github.com/microsoft/voice-agent/commit/d29b7bb75230e631491d0eeef048a7fa2de0b02c) - `2026-10-30T12:16:16Z` - yyyufei (@yyyufei) - PR: [Add Foundry evaluation tutorial and preliminary Python runner](https://github.com/microsoft/voice-agent/pull/94)
- [Fix Mermaid parse error in image input sample README (#95)](https://github.com/microsoft/voice-agent/commit/c0c71b48722c1515cdfaba242e6b5813d48bea8c) - `2026-10-30T09:10:51Z` - uchihaqyf-bot (@uchihaqyf-bot) - PR: [Fix Mermaid diagram in image input sample README](https://github.com/microsoft/voice-agent/pull/95)
- [Add Voice Agent image and camera input sample (#90)](https://github.com/microsoft/voice-agent/commit/f9fc83e91408a7b1140828e74339190d569f3281) - `2026-10-30T05:41:43Z` - uchihaqyf-bot (@uchihaqyf-bot) - PR: [Add Voice Agent image and camera input sample](https://github.com/microsoft/voice-agent/pull/90)

### microsoft/kiota (6 commit(s), signal 131)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [v1.37.0](https://github.com/microsoft/kiota/releases/tag/v1.37.0) - `2026-10-30T01:16:57Z`
- [chore(deps-dev): bump org.apache.maven.plugins:maven-surefire-plugin …](https://github.com/microsoft/kiota/commit/81e5baf70e1a4b5f09b61a21811116b13b09e7b0) - `2026-10-30T11:16:47Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps-dev): bump org.apache.maven.plugins:maven-surefire-plugin from 3.6.0 to 3.6.1 in /it/java/basic](https://github.com/microsoft/kiota/pull/8519)
- [chore(deps-dev): bump webpack from 5.112.0 to 5.112.1 in /vscode (#8518)](https://github.com/microsoft/kiota/commit/e0f90e9ae690907a9bd57502c9ee53bfa9bc95b1) - `2026-10-30T10:01:38Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps-dev): bump webpack from 5.112.0 to 5.112.1 in /vscode](https://github.com/microsoft/kiota/pull/8518)
- [chore(deps-dev): bump the eslint group across 1 directory with 2 upda…](https://github.com/microsoft/kiota/commit/a3080633dc5dcc6967f68544f2f1f030e17f072a) - `2026-10-30T08:48:27Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps-dev): bump the eslint group across 1 directory with 2 updates](https://github.com/microsoft/kiota/pull/8401)
- [chore(deps-dev): bump the pytest group across 1 directory with 2 upda…](https://github.com/microsoft/kiota/commit/27f592433ba59d6ce14f2c5303e72fca9479876c) - `2026-10-30T08:44:22Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps-dev): bump the pytest group across 1 directory with 2 updates](https://github.com/microsoft/kiota/pull/8422)
- [- bumps version for release of 1.37.0 (#8514)](https://github.com/microsoft/kiota/commit/f31297c3f2e296eacf1755ca0126df609a4dfc8c) - `2026-10-30T00:10:19Z` - Jingjing Jia (@jingjingjia-ms) - PR: [- bumps version for release of 1.37.0](https://github.com/microsoft/kiota/pull/8514)

### microsoft/winget-cli (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure AI, product:PowerShell, watchlist`

- [Respect -WhatIf in PowerShell package commands (#6588)](https://github.com/microsoft/winget-cli/commit/cf71e38eccd2b9035c03c7408f5328cd0e4fdee8) - `2026-10-30T01:03:03Z` - Slai.life (@huong8373tt-beep) - PR: [Respect -WhatIf in PowerShell package commands](https://github.com/microsoft/winget-cli/pull/6588)
- [Return failure when no MSIX package is found during uninstall (#6587)](https://github.com/microsoft/winget-cli/commit/add0d63ebe937aac099601fff554615773c502e3) - `2026-10-30T01:00:47Z` - Slai.life (@huong8373tt-beep) - PR: [Return failure when no MSIX package is found during uninstall](https://github.com/microsoft/winget-cli/pull/6587)
- [Slai Agent Runtime: Support ARM architectures in package name normali…](https://github.com/microsoft/winget-cli/commit/bac5a5c78efb3130a304efb0fbee4372416a29b3) - `2026-10-29T23:53:21Z` - Slai.life (@huong8373tt-beep) - PR: [Slai Agent Runtime: Support ARM architectures in package name normalization](https://github.com/microsoft/winget-cli/pull/6585)
- [Introduce generic Hash abstraction as foundation for future algorithm…](https://github.com/microsoft/winget-cli/commit/630ec844453b8e16f86ece0e8330816f655e17a5) - `2026-10-29T23:22:02Z` - Kaleb Luedtke (@Trenly) - PR: [Introduce generic Hash abstraction as foundation for future algorithms](https://github.com/microsoft/winget-cli/pull/6561)
- [Skip folded and moved results when folding non-primary matches (#6625)](https://github.com/microsoft/winget-cli/commit/cd2ba39b2df2c95b1390356f5ee1ac55d758a4c2) - `2026-10-29T22:20:25Z` - Tom Plant (@pl4nty) - PR: [Skip folded and moved results when folding non-primary matches](https://github.com/microsoft/winget-cli/pull/6625)

### microsoftgraph/msgraph-sample-github-connector-typescript (6 commit(s), signal 21)

Tags: `bot-only, dependency-noise, product:Microsoft Graph, samples, watchlist`

- [Merge pull request #305 from microsoftgraph/dependabot/npm_and_yarn/a…](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/commit/b839b2471743783705b64cf2c2b2a970ebf6c581) - `2026-10-30T00:29:34Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump @azure/identity from 4.13.1 to 4.14.0](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/pull/305)
- [Bump @azure/identity from 4.13.1 to 4.14.0](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/commit/46c91867e85f35a293610cfb2529ec263e68efde) - `2026-10-30T00:29:05Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump @azure/identity from 4.13.1 to 4.14.0](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/pull/305)
- [Merge pull request #302 from microsoftgraph/dependabot/npm_and_yarn/m…](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/commit/7da35f19ffa4976948c21bd2e266e0f5ba08bc4a) - `2026-10-30T00:26:48Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump marked from 18.1.1 to 18.1.2](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/pull/302)
- [Bump marked from 18.1.1 to 18.1.2](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/commit/52a50942247b58f633ccbf8230372e69bc7914d3) - `2026-10-30T00:26:10Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump marked from 18.1.1 to 18.1.2](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/pull/302)
- [Merge pull request #301 from microsoftgraph/dependabot/npm_and_yarn/t…](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/commit/a33608c34b83ccf17be4e653089318b2901300b5) - `2026-10-30T00:23:51Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump @typescript-eslint/parser from 8.29.0 to 8.72.1](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript/pull/301)

### Azure-Samples/azure-files-samples (5 commit(s), signal 55)

Tags: `human-authored, release-language, samples`

- [Bump RestSetAcls to 0.2.14 (#323)](https://github.com/Azure-Samples/azure-files-samples/commit/af1cdfc571159ed5fb73420fc0f83a0fe0d8a172) - `2026-10-30T18:14:40Z` - Maxime Kjaer (@MaximeKjaer) - PR: [Bump RestSetAcls to 0.2.14](https://github.com/Azure-Samples/azure-files-samples/pull/323)
- [Pin GitHub Actions to full-length commit SHAs (#314)](https://github.com/Azure-Samples/azure-files-samples/commit/5f24d03a49039c1593fb5b8addd4899c98e188dc) - `2026-10-30T18:08:57Z` - Dan Fiedler (@danfiedler-msft) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/azure-files-samples/pull/314)
- [Add minor perf improvement to Update-AzFileAclOnPremToCloudSid (#322)](https://github.com/Azure-Samples/azure-files-samples/commit/636f4a1ef18e48d42ef2bfec22ebfe7804a9460c) - `2026-10-30T16:57:19Z` - Maxime Kjaer (@MaximeKjaer) - PR: [Add minor perf improvement to Update-AzFileAclOnPremToCloudSid](https://github.com/Azure-Samples/azure-files-samples/pull/322)
- [Bump RestSetAcls Version to 0.2.13 (#321)](https://github.com/Azure-Samples/azure-files-samples/commit/51e201866e5213ecf903c7b9e6b7075f4874ba61) - `2026-10-29T18:52:27Z` - MarcosJLR (@MarcosJLR) - PR: [Bump RestSetAcls Version to 0.2.13](https://github.com/Azure-Samples/azure-files-samples/pull/321)
- [Rest set acls Update-AzFileAclOnPremToCloudSid skip missing SIDs and …](https://github.com/Azure-Samples/azure-files-samples/commit/4b2eef418352fde81b2a4dca7541375496d9ef48) - `2026-10-29T18:44:51Z` - MarcosJLR (@MarcosJLR) - PR: [Rest set acls Update-AzFileAclOnPremToCloudSid skip missing SIDs and add SID cache](https://github.com/Azure-Samples/azure-files-samples/pull/320)

### microsoft/TypeAgent (5 commit(s), signal 80)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Enhance Memory Hub performance, UI, and browser compatibility (#3245)](https://github.com/microsoft/TypeAgent/commit/dfbb1dd26cd55181537e3d66daacfa5821e02f18) - `2026-10-30T15:32:07Z` - Hillary Mutisya (@hillary-mutisya) - PR: [Enhance Memory Hub performance, UI, and browser compatibility](https://github.com/microsoft/TypeAgent/pull/3245)
- [Support embedding-3 sizing and index migration (#3242)](https://github.com/microsoft/TypeAgent/commit/714e7999f5946cecaed3758b0a4ba604adf4c060) - `2026-10-30T05:52:36Z` - Hillary Mutisya (@hillary-mutisya) - PR: [Support embedding-3 sizing and index migration](https://github.com/microsoft/TypeAgent/pull/3242)
- [Preserve source temporal provenance in memory MCP results (#3244)](https://github.com/microsoft/TypeAgent/commit/73219c678e34058b39ae053b22586a038cb4c070) - `2026-10-30T02:50:57Z` - Hillary Mutisya (@hillary-mutisya) - PR: [Preserve source temporal provenance in memory MCP results](https://github.com/microsoft/TypeAgent/pull/3244)
- [Enhance memory performance and fix browser response handling (#3243)](https://github.com/microsoft/TypeAgent/commit/d2b522947dfe0c7a23bc4ddc5d6e88e62fad0401) - `2026-10-30T01:08:10Z` - Hillary Mutisya (@hillary-mutisya) - PR: [Enhance memory performance and fix browser response handling](https://github.com/microsoft/TypeAgent/pull/3243)
- [Reduce memory-maintenance latency with checkpoint-aware short-job pri…](https://github.com/microsoft/TypeAgent/commit/375f13ec1af3961a10edc728220a23fb134835fd) - `2026-10-29T22:16:16Z` - Hillary Mutisya (@hillary-mutisya) - PR: [Reduce memory-maintenance latency with checkpoint-aware short-job priority](https://github.com/microsoft/TypeAgent/pull/3241)

### MicrosoftLearning/mslearn-ai-agents (5 commit(s), signal 80)

Tags: `human-authored, product:Azure AI, training, watchlist`

- [Merge pull request #257 from v-vfarias/main](https://github.com/MicrosoftLearning/mslearn-ai-agents/commit/5ab16f692cbd868b7b9b2aa6456abbd7c6a8c904) - `2026-10-30T15:19:11Z` - Graeme Malcolm (@GraemeMalcolm) - PR: [Fix typos and added a tip for webIQ portal UI](https://github.com/MicrosoftLearning/mslearn-ai-agents/pull/257)
- [Fixed typos and suggested tip](https://github.com/MicrosoftLearning/mslearn-ai-agents/commit/72409a7f3ab8e1e59308ba14fedab5768ee1dacc) - `2026-10-30T11:12:36Z` - Victor Barreto (@v-vfarias) - PR: [Fix typos and added a tip for webIQ portal UI](https://github.com/MicrosoftLearning/mslearn-ai-agents/pull/257)
- [Merge pull request #7 from MicrosoftLearning/main](https://github.com/MicrosoftLearning/mslearn-ai-agents/commit/4189ba6afff58549f887961941d3dfb602291abe) - `2026-10-30T11:00:25Z` - v-vfarias (@v-vfarias) - PR: [Fix typos and added a tip for webIQ portal UI](https://github.com/MicrosoftLearning/mslearn-ai-agents/pull/257)
- [Fix typo](https://github.com/MicrosoftLearning/mslearn-ai-agents/commit/11c7d17d789d3aa84f00e5d57af8ca3cf9fa9d93) - `2026-10-29T22:58:35Z` - Graeme Malcolm (@GraemeMalcolm)
- [Added Web IQ lab](https://github.com/MicrosoftLearning/mslearn-ai-agents/commit/b9f1529470a0fc52177786742e352f5b869d9f2f) - `2026-10-29T22:56:57Z` - Graeme Malcolm (@GraemeMalcolm)

### microsoft/kiota-java (5 commit(s), signal 80)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #2227 from microsoft/dependabot/gradle/okhttp-4.12.1](https://github.com/microsoft/kiota-java/commit/7858a903e8fad8dd351bc8b0842777e50a17cf6c) - `2026-10-30T09:57:14Z` - github-actions[bot] (@github-actions[bot]) - PR: [chore(deps): bump okhttp from 4.12.0 to 4.12.1](https://github.com/microsoft/kiota-java/pull/2227)
- [chore(deps): bump okhttp from 4.12.0 to 4.12.1](https://github.com/microsoft/kiota-java/commit/26c21cd65b6906dee5beee9970c4317f769e19c2) - `2026-10-29T22:33:15Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump okhttp from 4.12.0 to 4.12.1](https://github.com/microsoft/kiota-java/pull/2227)
- [Merge pull request #2226 from hardikkaurani/fix/request-information-c…](https://github.com/microsoft/kiota-java/commit/c180e331abbc9ad1ee6f80317583ed2310cd6665) - `2026-10-29T19:00:28Z` - Vincent Biret (@baywet) - PR: [fix(abstractions): support collection sanitization and null safety in RequestInformation](https://github.com/microsoft/kiota-java/pull/2226)
- [test(abstractions): add test coverage for collection sanitization and…](https://github.com/microsoft/kiota-java/commit/9505eef78d6b3ef1fae5d736241a7f31940af7db) - `2026-10-29T18:28:13Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(abstractions): support collection sanitization and null safety in RequestInformation](https://github.com/microsoft/kiota-java/pull/2226)
- [fix(abstractions): support collection sanitization and null safety in…](https://github.com/microsoft/kiota-java/commit/acfe31e3e926ee8f5a03da2264531c07a88b99ba) - `2026-10-29T18:28:13Z` - Hardik Kaurani (@hardikkaurani) - PR: [fix(abstractions): support collection sanitization and null safety in RequestInformation](https://github.com/microsoft/kiota-java/pull/2226)

### dotnet/efcore (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Update Vally packages to 0.20.0 (#39461)](https://github.com/dotnet/efcore/commit/716a0a9517f963afc764b157716f733523f966c3) - `2026-10-30T06:50:52Z` - Copilot (@Copilot) - PR: [Update Vally packages to 0.20.0](https://github.com/dotnet/efcore/pull/39461)
- [Translate grouping aggregates as window functions behind an opt-in (#…](https://github.com/dotnet/efcore/commit/c6291717f38981993a19b8a4dc872680f0a0b0c6) - `2026-10-30T03:43:09Z` - Benedict O'Donovan (@benedict-odonovan) - PR: [Translate grouping aggregates as window functions behind an opt-in](https://github.com/dotnet/efcore/pull/39240)
- [Fix JSON complex property projections with identity resolution (#39442)](https://github.com/dotnet/efcore/commit/f29db88853e3325a8cf3a959392101c3f36eeb23) - `2026-10-30T01:57:54Z` - Thalys Márcio (@thalysmarciobn) - PR: [Fix JSON complex property projections with identity resolution](https://github.com/dotnet/efcore/pull/39442)
- [Report command failures while reading results (#39405)](https://github.com/dotnet/efcore/commit/699022974d62bc43e8820c0f9fd22349c70de22a) - `2026-10-30T01:46:15Z` - Shivansh Gaur (@Shivansh-Gaur2) - PR: [Report command failures while reading results](https://github.com/dotnet/efcore/pull/39405)
- [Visit each IN value once when compensating for nullable values (#39414)](https://github.com/dotnet/efcore/commit/7aa24aa64a64b39a13d04a51a93028b1ae1e6c21) - `2026-10-30T01:43:33Z` - Benedict O'Donovan (@benedict-odonovan) - PR: [Visit each IN value once when compensating for nullable values](https://github.com/dotnet/efcore/pull/39414)

### Azure/azure-cli-extensions (5 commit(s), signal 130)

Tags: `docs, human-authored, release, release-language, watchlist`

- Release: [edge-action 1.1.0](https://github.com/Azure/azure-cli-extensions/releases/tag/edge-action-1.1.0) - `2026-10-29T23:55:04Z`
- Release: [nexusidentity 1.0.0b7](https://github.com/Azure/azure-cli-extensions/releases/tag/nexusidentity-1.0.0b7) - `2026-10-29T22:32:48Z`
- [[Containerapp] `az containerapp env create`: Pre-announce future logs…](https://github.com/Azure/azure-cli-extensions/commit/d79d5bc724e7701a03ad7a74c064d06c260ad417) - `2026-10-30T06:47:50Z` - Michael Dai (@michaelkira) - PR: [[Containerapp] `az containerapp env create`: Pre-announce future logs destination default change](https://github.com/Azure/azure-cli-extensions/pull/10494)
- [[Release] Update index.json for extension [ edge-action-1.1.0 ]](https://github.com/Azure/azure-cli-extensions/commit/e7db878ea7418f4518a8d3eef643babf10bf58ce) - `2026-10-29T23:54:05Z` - Azure CLI Team (@azclibot)
- [[Edge Action] Release 1.1.0 with subscription-scoped listing (#10536)](https://github.com/Azure/azure-cli-extensions/commit/bfd7c1c0932b917831a7cdc43e8d145c75d5343c) - `2026-10-29T23:38:42Z` - Jean Kim (@kestry) - PR: [[Edge Action] Release 1.1.0 with subscription-scoped listing](https://github.com/Azure/azure-cli-extensions/pull/10536)
- [[Release] Update index.json for extension [ nexusidentity-1.0.0b7 ]](https://github.com/Azure/azure-cli-extensions/commit/002e6b50ffd4ee065413d6b9ffdded3e212e508f) - `2026-10-29T22:31:51Z` - Azure CLI Team (@azclibot)
- [[NexusIdentity] CLI update to 1.0.0b7 (#10515)](https://github.com/Azure/azure-cli-extensions/commit/ee9adc7983afe9a3ef070f4e9c101213aa5cc96a) - `2026-10-29T22:14:04Z` - idanielsteven (@idanielsteven) - PR: [[NexusIdentity] CLI update to 1.0.0b7](https://github.com/Azure/azure-cli-extensions/pull/10515)

### MicrosoftDocs/dynamics-365-unified-operations-public (5 commit(s), signal 90)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/Dynamics…](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/09fb97213fa420765c649ff4e9d9547fa9896622) - `2026-10-29T19:05:16Z` - Learn Build Service GitHub App
- [Merge pull request #22783 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/26c78f4278e1ab206cd8dd79833d05abedf1610b) - `2026-10-29T19:03:21Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update general-journal-establishments.md (#22781)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/ea6f6fb94b25db37934e7d94816b34259f28ead5) - `2026-10-29T18:51:22Z` - twheeloc (@twheeloc)
- [Dates new (#22778)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/491368733620f0c00f131e975384a8a616a41b69) - `2026-10-29T17:16:52Z` - twheeloc (@twheeloc)
- [Update platform update version dates (#22777)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/f15489d648b032e0521993fdb9194dc90279c24d) - `2026-10-29T17:15:51Z` - John Michalak (@johnmichalak)

### microsoftgraph/msgraph-snippets-go (4 commit(s), signal 19)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #245 from microsoftgraph/dependabot/go_modules/src…](https://github.com/microsoftgraph/msgraph-snippets-go/commit/25a5206c79edaca9a0f73e3e4eea32c6b01857ac) - `2026-10-30T16:32:45Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump github.com/microsoftgraph/msgraph-sdk-go from 1.104.0 to 1.105.0 in /src](https://github.com/microsoftgraph/msgraph-snippets-go/pull/245)
- [Bump github.com/microsoftgraph/msgraph-sdk-go in /src](https://github.com/microsoftgraph/msgraph-snippets-go/commit/c9f083eba5bd920ffdcee52978ef8b732e4b70c4) - `2026-10-30T16:29:07Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump github.com/microsoftgraph/msgraph-sdk-go from 1.104.0 to 1.105.0 in /src](https://github.com/microsoftgraph/msgraph-snippets-go/pull/245)
- [Merge pull request #246 from microsoftgraph/dependabot/go_modules/src…](https://github.com/microsoftgraph/msgraph-snippets-go/commit/945defcff96aee15e9c52476f514a3a6ff8146c1) - `2026-10-30T16:26:43Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump github.com/microsoft/kiota-abstractions-go from 1.11.3 to 1.11.4 in /src](https://github.com/microsoftgraph/msgraph-snippets-go/pull/246)
- [Bump github.com/microsoft/kiota-abstractions-go in /src](https://github.com/microsoftgraph/msgraph-snippets-go/commit/fe7421d041175ba2ea7efcc8c1d2375ce1be17ba) - `2026-10-30T16:23:03Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump github.com/microsoft/kiota-abstractions-go from 1.11.3 to 1.11.4 in /src](https://github.com/microsoftgraph/msgraph-snippets-go/pull/246)

### dotnet/AspNetCore.Docs (4 commit(s), signal 44)

Tags: `docs, human-authored`

- [Add extra information for UseProxyToSpaDevelopmentServer. (#38062)](https://github.com/dotnet/AspNetCore.Docs/commit/71dcddb428ca888e5767a7bb10681ddd0002a1b8) - `2026-10-30T14:11:54Z` - Jiri Cincura ↹ (@cincuranet) - PR: [Add extra information for UseProxyToSpaDevelopmentServer.](https://github.com/dotnet/AspNetCore.Docs/pull/38062)
- [Remove UID metadata - part two (#38058)](https://github.com/dotnet/AspNetCore.Docs/commit/37d4f7c281362fea72ec6d4aa04e2996abe198d2) - `2026-10-30T12:23:13Z` - Genevieve Warren (@gewarren) - PR: [Remove UID metadata - part two](https://github.com/dotnet/AspNetCore.Docs/pull/38058)
- [Delete .github/policies/pullRequestManagement-labelFiles.yml (#38059)](https://github.com/dotnet/AspNetCore.Docs/commit/13a5c124b721d439fe63ed28195d64a569ee5a0e) - `2026-10-30T01:02:34Z` - Genevieve Warren (@gewarren) - PR: [Delete .github/policies/pullRequestManagement-labelFiles.yml](https://github.com/dotnet/AspNetCore.Docs/pull/38059)
- [Delete orphaned include files (#37980)](https://github.com/dotnet/AspNetCore.Docs/commit/648ccf06cf991634f2a92b60f1d7841793de4dc6) - `2026-10-29T23:18:12Z` - Genevieve Warren (@gewarren) - PR: [Delete orphaned include files](https://github.com/dotnet/AspNetCore.Docs/pull/37980)

### microsoftgraph/msgraph-snippets-java (4 commit(s), signal 19)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #220 from microsoftgraph/dependabot/gradle/com.mic…](https://github.com/microsoftgraph/msgraph-snippets-java/commit/fa99ca53c9c46952957dc2325dd7dc1d508b44ef) - `2026-10-30T06:28:43Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump com.microsoft.kiota:microsoft-kiota-http-okHttp from 1.10.2 to 1.10.3](https://github.com/microsoftgraph/msgraph-snippets-java/pull/220)
- [Bump com.microsoft.kiota:microsoft-kiota-http-okHttp](https://github.com/microsoftgraph/msgraph-snippets-java/commit/3e4b88d28b31fbc7848ae644db6b95f6ddf3bb49) - `2026-10-30T06:26:48Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump com.microsoft.kiota:microsoft-kiota-http-okHttp from 1.10.2 to 1.10.3](https://github.com/microsoftgraph/msgraph-snippets-java/pull/220)
- [Merge pull request #219 from microsoftgraph/dependabot/gradle/com.mic…](https://github.com/microsoftgraph/msgraph-snippets-java/commit/afceca14614de95ee1f44f39ffa7c6ae4eccd6d5) - `2026-10-30T06:24:32Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump com.microsoft.graph:microsoft-graph from 6.71.0 to 6.72.0](https://github.com/microsoftgraph/msgraph-snippets-java/pull/219)
- [Bump com.microsoft.graph:microsoft-graph from 6.71.0 to 6.72.0](https://github.com/microsoftgraph/msgraph-snippets-java/commit/50e560445a526dba9dd9f3a11d85eb7b322dafb5) - `2026-10-30T06:22:51Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump com.microsoft.graph:microsoft-graph from 6.71.0 to 6.72.0](https://github.com/microsoftgraph/msgraph-snippets-java/pull/219)

### Azure/azure-sdk-for-rust (4 commit(s), signal 104)

Tags: `docs, human-authored, product:Azure SDK, security, watchlist`

- [Add default credential scope and ARM endpoint support (#5495)](https://github.com/Azure/azure-sdk-for-rust/commit/7352475fc80a58845d75a0f2d089eb8e9dd09359) - `2026-10-30T00:42:11Z` - Heath Stewart (@heaths) - PR: [Add default credential scope and ARM endpoint support](https://github.com/Azure/azure-sdk-for-rust/pull/5495)
- [Add ARM poller helper under `azure_core::http::poller::resource_manag…](https://github.com/Azure/azure-sdk-for-rust/commit/e8f8c1b6f4acc7e7afdc47e93e461349512540ae) - `2026-10-29T23:01:36Z` - Copilot (@Copilot) - PR: [Add ARM poller helper under `azure_core::http::poller::resource_manager`](https://github.com/Azure/azure-sdk-for-rust/pull/4508)
- [Bump the github-actions group with 3 updates (#5535)](https://github.com/Azure/azure-sdk-for-rust/commit/db7dfa9372969cf81f7e789aa6544235b3bad31f) - `2026-10-29T21:25:02Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the github-actions group with 3 updates](https://github.com/Azure/azure-sdk-for-rust/pull/5535)
- [Bump markdownlint-cli2 from 0.23.3 to 0.24.0 in the npm group (#5536)](https://github.com/Azure/azure-sdk-for-rust/commit/34ee229e20aab56c9646aae00dc06eecae4c3912) - `2026-10-29T21:09:15Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump markdownlint-cli2 from 0.23.3 to 0.24.0 in the npm group](https://github.com/Azure/azure-sdk-for-rust/pull/5536)

### Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample (4 commit(s), signal 109)

Tags: `human-authored, release, samples, security`

- Release: [EPP javascript Function ZIP 271.1](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/releases/tag/epp-packages-271-1-javascript) - `2026-10-29T23:44:52Z`
- Release: [EPP python Function ZIP 271.1](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/releases/tag/epp-packages-271-1-python) - `2026-10-29T23:44:50Z`
- Release: [EPP dotnet Function ZIP 271.1](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/releases/tag/epp-packages-271-1-dotnet) - `2026-10-29T23:44:50Z`
- Release: [EPP python Function ZIP 268.1](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/releases/tag/epp-packages-268-1-python) - `2026-10-29T21:44:07Z`
- Release: [EPP javascript Function ZIP 268.1](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/releases/tag/epp-packages-268-1-javascript) - `2026-10-29T21:44:05Z`
- [Align credential acquisition timeouts to five seconds (#86)](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/commit/f78112112775a846a81e8cb1aa1d25166c642c9c) - `2026-10-29T23:42:08Z` - siyixian (@siyixian) - PR: [Align credential acquisition timeouts to five seconds](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/pull/86)
- [Fix outbound federated credential name collisions (#85)](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/commit/e1e5b87e5c38e48ecd179291824ee2df16bd9de4) - `2026-10-29T21:41:49Z` - siyixian (@siyixian) - PR: [Fix outbound federated credential name collisions](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/pull/85)
- [Remove Sinch and delegate Infobip sender selection (#84)](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/commit/7b47af22e64a3d25828c85d16d65f585e021bfc6) - `2026-10-29T18:16:27Z` - siyixian (@siyixian) - PR: [Remove Sinch and delegate Infobip sender selection](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/pull/84)
- [Upgrade .NET sample and deployment runtime to .NET 10 (#83)](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/commit/2558e84c8c7d784877b617619ea18ac994e5b452) - `2026-10-29T17:06:09Z` - siyixian (@siyixian) - PR: [Upgrade .NET sample and deployment runtime to .NET 10](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/pull/83)

### MicrosoftDocs/data-tools (4 commit(s), signal 79)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #953 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/data-tools/commit/63e047e75c3b2da28ae9784bb4ec237863efb0c5) - `2026-10-29T21:01:45Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #952 from mbarickman/ssms22.11.3relnoteupdates](https://github.com/MicrosoftDocs/data-tools/commit/3a3c4d7cf6577f7e0f35a8e9fc7c229aa6a7a909) - `2026-10-29T19:10:42Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [update VS build number](https://github.com/MicrosoftDocs/data-tools/commit/6c459d2d2b9dbbf45db73feb7496a11ef284ad88) - `2026-10-29T19:06:42Z` - Makena Barickman (@mbarickman)
- [Merge pull request #951 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/data-tools/commit/8de880812648b2eea217125f06a45650fc1b546d) - `2026-10-29T17:05:43Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### MicrosoftLearning/MS-4021-Copilot-Immersion-Experience (4 commit(s), signal 79)

Tags: `human-authored, training, watchlist`

- [Merge pull request #19 from MicrosoftLearning/Ignite_workshop_test](https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/commit/7164f01d75d0d1e89ced5a19fea173be17c35c80) - `2026-10-29T19:45:25Z` - Matt Quinlan (@maquinl) - PR: [Fix](https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/pull/19)
- [Fix](https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/commit/7ca2c80216c9542e0cbb6db68dc293a117c8eb35) - `2026-10-29T19:44:44Z` - Matt Quinlan (@maquinl) - PR: [Fix](https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/pull/19)
- [Merge pull request #18 from MicrosoftLearning/Ignite_workshop_test](https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/commit/587411ad7aaa906cba78bd0928ac1639a2ee9b07) - `2026-10-29T19:38:49Z` - Matt Quinlan (@maquinl) - PR: [Update_skill](https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/pull/18)
- [Update_skill](https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/commit/c85f63ab9daf5c779deda817ad345857e6f4f654) - `2026-10-29T19:38:32Z` - Matt Quinlan (@maquinl) - PR: [Update_skill](https://github.com/MicrosoftLearning/MS-4021-Copilot-Immersion-Experience/pull/18)

### MicrosoftDocs/power-platform (4 commit(s), signal 79)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/2f1a6b702673538a513a2c4a950c7ce0abcb6550) - `2026-10-29T19:03:40Z` - Learn Build Service GitHub App
- [Merge pull request #12111 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-platform/commit/6954a024b2ce8ce82c92b189943f020e84875aac) - `2026-10-29T19:02:33Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Power Automate: Describe it to design it retirement notice (#12104)](https://github.com/MicrosoftDocs/power-platform/commit/5a32b903e3501d71928d73c9414615412373f6b2) - `2026-10-29T17:42:06Z` - Matt Townsend (@radioblazer)
- [Update author information in developer environment and plan documenta…](https://github.com/MicrosoftDocs/power-platform/commit/368f75924cf12cb9a8635aa39e2bc551dba624d7) - `2026-10-29T17:05:57Z` - Jim Daly (@JimDaly)

### MicrosoftLearning/mslearn-azure-ai (4 commit(s), signal 79)

Tags: `human-authored, training, watchlist`

- [Auto-generated zip files [skip ci]](https://github.com/MicrosoftLearning/mslearn-azure-ai/commit/87077d00a31c0391763d4f67a4e101b76d76b28b) - `2026-10-29T18:16:22Z` - GitHub Action (@actions-user)
- [Merge pull request #285 from MicrosoftLearning/azure-web-pubsub](https://github.com/MicrosoftLearning/mslearn-azure-ai/commit/3bc8b39273f80b525404bb44981bc74974ea8b6c) - `2026-10-29T18:16:08Z` - JeffKoMS (@JeffKoMS) - PR: [Azure web pubsub](https://github.com/MicrosoftLearning/mslearn-azure-ai/pull/285)
- [tooling and sync confirmed](https://github.com/MicrosoftLearning/mslearn-azure-ai/commit/9ebc77d5b0d36993a91dba6aaaf1ec0d24eea1a8) - `2026-10-29T18:15:11Z` - jeffkoms (@JeffKoMS) - PR: [Azure web pubsub](https://github.com/MicrosoftLearning/mslearn-azure-ai/pull/285)
- [updated instructions and prepped the sync tools](https://github.com/MicrosoftLearning/mslearn-azure-ai/commit/1ebcd6975aea768932ad9efe58bbf6e95b505f81) - `2026-10-29T18:07:14Z` - jeffkoms (@JeffKoMS) - PR: [Azure web pubsub](https://github.com/MicrosoftLearning/mslearn-azure-ai/pull/285)

### dotnet/msbuild (3 commit(s), signal 43)

Tags: `docs, human-authored`

- [Avoid rewriting unchanged ARM64 manifests behind Wave 18.14 (#15428)](https://github.com/dotnet/msbuild/commit/49b51ed273c0f34dfe8ade13ea98442b96be7112) - `2026-10-30T18:19:51Z` - Jan Provazník (@JanProvaznik) - PR: [Avoid rewriting unchanged ARM64 manifests behind Wave 18.14](https://github.com/dotnet/msbuild/pull/15428)
- [Avoid full link-target resolution for ordinary Windows directories (#…](https://github.com/dotnet/msbuild/commit/eb53291c1a906bbd800ab960ee984a1d642177d4) - `2026-10-30T17:05:00Z` - Aleš Prokop (@AlesProkop) - PR: [Avoid full link-target resolution for ordinary Windows directories](https://github.com/dotnet/msbuild/pull/15282)
- [Replace regex use in globbing with hand-written globber (#15276)](https://github.com/dotnet/msbuild/commit/c4679ee34ec1d53a469c1486ec8e164fcdb0c1c3) - `2026-10-30T12:32:01Z` - Andy Gocke (@agocke) - PR: [Replace regex use in globbing with hand-written globber](https://github.com/dotnet/msbuild/pull/15276)

### dotnet/android-api-docs (3 commit(s), signal 43)

Tags: `docs, human-authored`

- [Complete Android.Database.Sqlite documentation (#1269)](https://github.com/dotnet/android-api-docs/commit/70db95e262c6081ee17287dbf8be35d50aeec41b) - `2026-10-30T17:32:26Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Complete Android.Database.Sqlite documentation](https://github.com/dotnet/android-api-docs/pull/1269)
- [Complete Android.Widget.PhotoPicker documentation (#1215)](https://github.com/dotnet/android-api-docs/commit/21e8c76be786a839e45831e027d2fa54c00ad1e5) - `2026-10-30T17:27:38Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Complete Android.Widget.PhotoPicker documentation](https://github.com/dotnet/android-api-docs/pull/1215)
- [Complete Android.Appwidget documentation (#1256)](https://github.com/dotnet/android-api-docs/commit/a2f8dbc7d4db62e80b898625fe109762a7db8e4e) - `2026-10-30T16:31:23Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Complete Android.Appwidget documentation](https://github.com/dotnet/android-api-docs/pull/1256)

### Azure-Samples/secrets-store-csi-with-aks-akv (3 commit(s), signal 68)

Tags: `human-authored, samples, security`

- [Merge pull request #3 from hyoshioka0128/patch-1](https://github.com/Azure-Samples/secrets-store-csi-with-aks-akv/commit/bea56894baf7fa568df8378a445399090e9201bb) - `2026-10-30T17:00:47Z` - Lila Molyva (@norelina) - PR: [Typo "Github"→"GitHub"](https://github.com/Azure-Samples/secrets-store-csi-with-aks-akv/pull/3)
- [Merge pull request #4 from amarkevich/patch-1](https://github.com/Azure-Samples/secrets-store-csi-with-aks-akv/commit/99668508ccce4cbf4069a515c613da4cf53d45a4) - `2026-10-30T17:00:29Z` - Lila Molyva (@norelina) - PR: [readme: fix installation url](https://github.com/Azure-Samples/secrets-store-csi-with-aks-akv/pull/4)
- [Merge pull request #6 from danfiedler-msft/danfiedler/pin-actions](https://github.com/Azure-Samples/secrets-store-csi-with-aks-akv/commit/cc6b1e444f60a32a134123ee250460e956685add) - `2026-10-30T17:00:11Z` - Lila Molyva (@norelina) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/secrets-store-csi-with-aks-akv/pull/6)

### MicrosoftDocs/azure-monitor-docs (3 commit(s), signal 28)

Tags: `bot-only, docs, watchlist`

- [Merge pull request #5700 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/9f0061dcac998c9d39bba6d9ed0a11ef9b32e1c1) - `2026-10-30T06:03:50Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #5636 from jinmo-yi/jinmo-yi-patch-259824](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/9f9fcc6f8b17fbbfb330234c618aa9c4d30f8b5f) - `2026-10-30T00:08:01Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #5698 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/1419ce53093a722c48591810ab88af4206611560) - `2026-10-29T17:07:45Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### MicrosoftDocs/quantum-docs (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/quantum-…](https://github.com/MicrosoftDocs/quantum-docs/commit/021188f5476959778690c27ad9f6fe3b96f8731b) - `2026-10-30T00:02:21Z` - Learn Build Service GitHub App
- [Merge pull request #1696 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/quantum-docs/commit/6634553ecb8d78adc217d2176804da621f485bef) - `2026-10-30T00:02:00Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Added full-length commit SHA for action pinning (#1695)](https://github.com/MicrosoftDocs/quantum-docs/commit/a89a50dd1cfebd8552cc413928515ef7c763e1cc) - `2026-10-29T22:07:42Z` - Jeremy

### MicrosoftDocs/Advertising (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/Advertis…](https://github.com/MicrosoftDocs/Advertising/commit/cd6e1c76c70e33cb9d529600dbf2bceabbae1e62) - `2026-10-29T19:05:45Z` - Learn Build Service GitHub App
- [Update Tealium link and time range (#814)](https://github.com/MicrosoftDocs/Advertising/commit/e34e4f491f3b779b37e128b2a7954515a4129c1f) - `2026-10-29T19:05:06Z` - Rick Garitta (@rgaritta)
- [Remove unknown and clarify watermark (#813)](https://github.com/MicrosoftDocs/Advertising/commit/03feccc1a71ecacdf2a5caab1b10bb5040414feb) - `2026-10-29T18:58:24Z` - Rick Garitta (@rgaritta)

### Azure/azure-quickstart-templates (3 commit(s), signal 78)

Tags: `human-authored, samples, watchlist`

- [Rename enclave key vault sample folder and update deploy links (#14893)](https://github.com/Azure/azure-quickstart-templates/commit/59eb6101d361d83aeb47423b9d36429fd4a5d36a) - `2026-10-29T18:59:58Z` - Andy Serfass (@aserfass-msft) - PR: [Rename enclave key vault sample folder and update deploy links](https://github.com/Azure/azure-quickstart-templates/pull/14893)
- [Add Azure Enclave storage account quickstart (#14896)](https://github.com/Azure/azure-quickstart-templates/commit/cd236c34cf0d0bfe8e98d2a6b23d624eebef40ff) - `2026-10-29T18:55:35Z` - Andy Serfass (@aserfass-msft) - PR: [Add Azure Enclave storage account quickstart](https://github.com/Azure/azure-quickstart-templates/pull/14896)
- [Update template for SharePoint (#14897)](https://github.com/Azure/azure-quickstart-templates/commit/41c03b167e3536f3bed98890012837e1c960d89a) - `2026-10-29T18:55:27Z` - Yvan Duhamel (@Yvand) - PR: [Update template for SharePoint](https://github.com/Azure/azure-quickstart-templates/pull/14897)

### MicrosoftDocs/VBA-Docs (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Note that WorkbookConnection.Refresh loses the Power Query error mess…](https://github.com/MicrosoftDocs/VBA-Docs/commit/b202c96d9d53896593b73d6fae57f5230601a5e3) - `2026-10-29T17:58:40Z` - takazawa-kanji-itso (@takazawa-kanji-itso) - PR: [Note that WorkbookConnection.Refresh loses the Power Query error message, and point to QueryTable.Refresh](https://github.com/MicrosoftDocs/VBA-Docs/pull/1981)
- [Clarify that ListObject.Refresh also refreshes tables loaded from Pow…](https://github.com/MicrosoftDocs/VBA-Docs/commit/fcf110afc0e0df81e87b9d2761372ab3303e7e50) - `2026-10-29T17:57:48Z` - takazawa-kanji-itso (@takazawa-kanji-itso) - PR: [Clarify that ListObject.Refresh also refreshes tables loaded from Power Query queries](https://github.com/MicrosoftDocs/VBA-Docs/pull/1982)
- [Document how errors and End behave in macros called by Application.Ru…](https://github.com/MicrosoftDocs/VBA-Docs/commit/e17e1bc8c05492ee13ad2ff1959682d40d55b4fe) - `2026-10-29T17:38:49Z` - takazawa-kanji-itso (@takazawa-kanji-itso) - PR: [Document how errors and End behave in macros called by Application.Run](https://github.com/MicrosoftDocs/VBA-Docs/pull/1979)

### microsoft/BuildXL (3 commit(s), signal 78)

Tags: `human-authored, product:Microsoft Graph, samples, watchlist`

- [Merged PR 970198: Fix premature BigBuffer capacity overflow](https://github.com/microsoft/BuildXL/commit/cac66fcefb7cda41903227f4766749b779c333bb) - `2026-10-29T17:54:03Z` - Viv Siless
- [Merged PR 970180: Update ComponentDetection to 2026.10.28.1531](https://github.com/microsoft/BuildXL/commit/8b18308a0d9ecb10ab3431f9142e6848dfb250bc) - `2026-10-29T17:42:36Z` - Michael Pysson (@mpysson)
- [Merged PR 969344: DirectGraph: export artifacts through path-keyed maps](https://github.com/microsoft/BuildXL/commit/d8f24369caa09345f31720472354946efddf66a2) - `2026-10-29T17:41:40Z` - Oleksii Kononenko (@olkononenko)

### MicrosoftDocs/dataexplorer-docs (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #2952 from MicrosoftDocs/main639288901833262008syn…](https://github.com/MicrosoftDocs/dataexplorer-docs/commit/0e7f039fe86860bf705a000f4dea2d0913af6bfe) - `2026-10-29T17:03:13Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/dataexplorer-docs/pull/2952)
- [Merging changes synced from https://github.com/MicrosoftDocs/dataexpl…](https://github.com/MicrosoftDocs/dataexplorer-docs/commit/ec4b7c11a724103e803e96ad7ada377737c8657e) - `2026-10-29T17:03:00Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/dataexplorer-docs/pull/2952)
- [Merge pull request #7629 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dataexplorer-docs/commit/5e771ce3497f5b7a8d8fc247a5238385c738292f) - `2026-10-29T17:02:09Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/dataexplorer-docs/pull/2952)

### microsoft/bbs-node-reference (2 commit(s), signal 42)

Tags: `human-authored, reference`

- [Merge pull request #59 from microsoft/draft14](https://github.com/microsoft/bbs-node-reference/commit/e43cce1d7c3174889dde33df9a1d2a6ba135bb52) - `2026-10-30T17:56:43Z` - Christian Paquin (@christianpaquin) - PR: [Update to draft-irtf-cfrg-bbs-signatures-14](https://github.com/microsoft/bbs-node-reference/pull/59)
- [Update to draft-irtf-cfrg-bbs-signatures-14](https://github.com/microsoft/bbs-node-reference/commit/272fb658e2bdce82a05712c7baa1fae8ef0abc23) - `2026-10-30T15:49:05Z` - Christian Paquin (@christianpaquin) - PR: [Update to draft-irtf-cfrg-bbs-signatures-14](https://github.com/microsoft/bbs-node-reference/pull/59)

### Azure/APICenter-Portal-Starter (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Fix MCP registry review findings (#160)](https://github.com/Azure/APICenter-Portal-Starter/commit/c35d849077a541e1849a33352b126368e2a9548e) - `2026-10-30T15:59:49Z` - Roman Kolesnikov (@rkolesnikovDX) - PR: [Fix MCP registry review findings](https://github.com/Azure/APICenter-Portal-Starter/pull/160)
- [feat(mcp): show registry details and fix setup (#159)](https://github.com/Azure/APICenter-Portal-Starter/commit/7e807d9f6b3a72742e16ec4016368a3e908babed) - `2026-10-30T15:34:07Z` - Roman Kolesnikov (@rkolesnikovDX) - PR: [Show MCP registry details and use registry in setup](https://github.com/Azure/APICenter-Portal-Starter/pull/159)

### microsoft/DataSecurityGuidedAssistant (2 commit(s), signal 102)

Tags: `docs, human-authored, security, watchlist`

- [Merge pull request #17 from microsoft/dependabot/npm_and_yarn/fast-ur…](https://github.com/microsoft/DataSecurityGuidedAssistant/commit/e3b0e7cb1f09575d760ab082f21f58e9124c8ffd) - `2026-10-30T13:45:01Z` - Cj-Scott (@Cj-Scott) - PR: [build(deps-dev): bump fast-uri from 3.1.7 to 3.1.9](https://github.com/microsoft/DataSecurityGuidedAssistant/pull/17)
- [build(deps-dev): bump fast-uri from 3.1.7 to 3.1.9](https://github.com/microsoft/DataSecurityGuidedAssistant/commit/b7635c38e0202de659704dce44cb7063bfe0c0ac) - `2026-10-30T08:08:59Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps-dev): bump fast-uri from 3.1.7 to 3.1.9](https://github.com/microsoft/DataSecurityGuidedAssistant/pull/17)

### MicrosoftDocs/power-pages-docs (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #2031 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-pages-docs/commit/e02cf596c54c354c200ca355ab06672eed185977) - `2026-10-30T13:02:23Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Site visibility updates](https://github.com/MicrosoftDocs/power-pages-docs/commit/74d84dd0deff23dbc6af3e4c77795ed818c27767) - `2026-10-30T09:57:24Z` - Shweta (@shwetamurkute)

### microsoftgraph/msgraph-search-connector-sample (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, product:Microsoft Graph, samples, watchlist`

- [Merge pull request #118 from microsoftgraph/dependabot/nuget/PartsInv…](https://github.com/microsoftgraph/msgraph-search-connector-sample/commit/6a8bd9a3a965560f92e2e3236757c642d391f1c4) - `2026-10-30T11:44:47Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump Azure.Identity from 1.11.4 to 1.21.0](https://github.com/microsoftgraph/msgraph-search-connector-sample/pull/118)
- [Bump Azure.Identity from 1.11.4 to 1.21.0](https://github.com/microsoftgraph/msgraph-search-connector-sample/commit/4b030a50f04d4f18ff241694df7ea5e142feebd2) - `2026-10-30T11:43:59Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Azure.Identity from 1.11.4 to 1.21.0](https://github.com/microsoftgraph/msgraph-search-connector-sample/pull/118)

### Azure-Samples/Apim-Samples (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Bump tornado from 6.5.10 to 6.6 in the python-packages group (#334)](https://github.com/Azure-Samples/Apim-Samples/commit/47792e4423b46b8a060d3bd76f2e53c421e1cfed) - `2026-10-30T10:58:09Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump tornado from 6.5.10 to 6.6 in the python-packages group](https://github.com/Azure-Samples/Apim-Samples/pull/334)
- [Housekeeping (#333)](https://github.com/Azure-Samples/Apim-Samples/commit/3930803979f31db83fe158dfffd2e18bac8fa139) - `2026-10-29T17:01:50Z` - Simon Kurtz (@simonkurtz-MSFT) - PR: [Housekeeping](https://github.com/Azure-Samples/Apim-Samples/pull/333)

### MicrosoftDocs/office-docs-powershell (2 commit(s), signal 77)

Tags: `docs, human-authored, product:PowerShell, watchlist`

- [Fix syntax formatting in Set-CsUserCallingSettings.md (#13859)](https://github.com/MicrosoftDocs/office-docs-powershell/commit/7e922402e7bc7a6054a3062530aa9ba0fc7f65b8) - `2026-10-30T10:50:36Z` - Viktoria Hiiet (@vijurtse) - PR: [Fix syntax formatting in Set-CsUserCallingSettings.md](https://github.com/MicrosoftDocs/office-docs-powershell/pull/13859)
- [Enhance synopsis for Get-CsUserCallingSettings (#13858)](https://github.com/MicrosoftDocs/office-docs-powershell/commit/93a2fba2f13237f88d2c342a29d077a90d175697) - `2026-10-30T10:23:19Z` - Viktoria Hiiet (@vijurtse) - PR: [Enhance synopsis for Get-CsUserCallingSettings](https://github.com/MicrosoftDocs/office-docs-powershell/pull/13858)

### microsoft/web-iq-samples (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Merge pull request #8 from microsoft/users/bartdebacker/apim-public-s…](https://github.com/microsoft/web-iq-samples/commit/41e46eed1fb32b5bea4045c1b8eac8b8ac12a88a) - `2026-10-30T03:05:33Z` - Bart DeBacker (@bartdebacker-ms) - PR: [Add Web IQ APIM managed identity sample](https://github.com/microsoft/web-iq-samples/pull/8)
- [Add additional repository code owners (#9)](https://github.com/microsoft/web-iq-samples/commit/edb79fc5a53869c47524dbf5309d39f2349158f3) - `2026-10-29T17:38:39Z` - Bart DeBacker (@bartdebacker-ms) - PR: [Add alexaleta, teresaqhoang, and sandrohanea-msft as code owners](https://github.com/microsoft/web-iq-samples/pull/9)

### Azure/homebrew-azd (2 commit(s), signal 87)

Tags: `human-authored, product:Azure SDK, release-language, samples, watchlist`

- [Update for azd release 1.38.0-beta.1-daily.7017955](https://github.com/Azure/homebrew-azd/commit/50510f372c200dacad1618bcb5ce3b0c0fbb6629) - `2026-10-30T01:42:10Z` - azure-sdk (@azure-sdk)
- [Update for azd release 1.38.0-beta.1-daily.7016127](https://github.com/Azure/homebrew-azd/commit/f0921bd1f4750c46ed941d9ec537627f1e7a4b0f) - `2026-10-29T18:12:05Z` - azure-sdk (@azure-sdk)

### microsoft/vscode-edge-devtools (2 commit(s), signal 0)

Tags: `bot-only, dependency-noise, docs`

- [Bump qs from 6.16.0 to 6.17.1 (#5079)](https://github.com/microsoft/vscode-edge-devtools/commit/840dba5a69a93737e42fbe0505490f219f509321) - `2026-10-29T23:25:13Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump qs from 6.16.0 to 6.17.1](https://github.com/microsoft/vscode-edge-devtools/pull/5079)
- [Bump undici from 6.28.0 to 6.29.1 (#5074)](https://github.com/microsoft/vscode-edge-devtools/commit/1745540df6134edaa92715926c5fab9ada4c40b5) - `2026-10-29T22:58:19Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump undici from 6.28.0 to 6.29.1](https://github.com/microsoft/vscode-edge-devtools/pull/5074)

### Azure-Samples/explore-iot-operations (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Add reusable data flow pattern samples and published Helm chart (#218)](https://github.com/Azure-Samples/explore-iot-operations/commit/cd86365473de0c67fa711a58743785ed63802885) - `2026-10-29T22:26:15Z` - hugues bouvier (@huguesBouvier) - PR: [Add reusable data flow pattern samples and published Helm chart](https://github.com/Azure-Samples/explore-iot-operations/pull/218)
- [Make quickstart Event Hubs endpoint cloud-agnostic (#221)](https://github.com/Azure-Samples/explore-iot-operations/commit/368a38e48f19e2f9753254d037a84cc53e88b09f) - `2026-10-29T18:09:33Z` - Sri Harsha Kalavala (@shkalavala) - PR: [Make quickstart Event Hubs endpoint cloud-agnostic](https://github.com/Azure-Samples/explore-iot-operations/pull/221)

### MicrosoftLearning/AB-210T00-Accelerate-sales-pipelines-with-AI-in-D365 (2 commit(s), signal 77)

Tags: `human-authored, product:Azure AI, training, watchlist`

- [Merge pull request #6 from MicrosoftLearning/fix/lab06-sales-opportun…](https://github.com/MicrosoftLearning/AB-210T00-Accelerate-sales-pipelines-with-AI-in-D365/commit/4a89a2099af8fc1500f3341b8cdb822f6258e951) - `2026-10-29T21:26:42Z` - Anna Jennings (@anjenni) - PR: [Update Lab 6 for Sales Close Agent retirement](https://github.com/MicrosoftLearning/AB-210T00-Accelerate-sales-pipelines-with-AI-in-D365/pull/6)
- [Update Lab 6 for Sales Close Agent retirement](https://github.com/MicrosoftLearning/AB-210T00-Accelerate-sales-pipelines-with-AI-in-D365/commit/9db9f47099bc7cf89250df2e90ac51c3367a1d8b) - `2026-10-29T21:25:25Z` - Anna Jennings (@anjenni) - PR: [Update Lab 6 for Sales Close Agent retirement](https://github.com/MicrosoftLearning/AB-210T00-Accelerate-sales-pipelines-with-AI-in-D365/pull/6)

### microsoft/CopilotStudioSamples (2 commit(s), signal 77)

Tags: `human-authored, samples, watchlist`

- [Nest Copilot Studio client sample under A2A and MCP (#546)](https://github.com/microsoft/CopilotStudioSamples/commit/762900b7945b1571990c5899740e251148e82738) - `2026-10-29T21:06:55Z` - adilei (@adilei) - PR: [Nest Copilot Studio client sample under A2A and MCP](https://github.com/microsoft/CopilotStudioSamples/pull/546)
- [Add Copilot Studio MCP and A2A client sample (#545)](https://github.com/microsoft/CopilotStudioSamples/commit/e4171aba2da2bfbbd9231f15e3b56b4f8a971df9) - `2026-10-29T21:00:35Z` - adilei (@adilei) - PR: [Add Copilot Studio MCP and A2A client sample](https://github.com/microsoft/CopilotStudioSamples/pull/545)

### MicrosoftDocs/dynamics-365-mixed-reality (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-mixed-reality/commit/bec0a3a1ca3ba2d0bf7733ecbeaa3bb06b84a095) - `2026-10-29T19:05:20Z` - Learn Build Service GitHub App
- [Merge pull request #1321 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-mixed-reality/commit/2ce51351e402b3ab8b71f3e75056d5c203a2460f) - `2026-10-29T19:04:19Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### microsoftgraph/msgraph-sample-react-native (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, product:Azure SDK, product:Microsoft Graph, samples, watchlist`

- [Merge pull request #189 from microsoftgraph/dependabot/npm_and_yarn/G…](https://github.com/microsoftgraph/msgraph-sample-react-native/commit/64063cebbcd6ed340d2d349f97a853f1f5d88ed2) - `2026-10-29T19:03:54Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump @tsconfig/react-native from 3.0.3 to 3.0.9 in /GraphRNSample](https://github.com/microsoftgraph/msgraph-sample-react-native/pull/189)
- [Bump @tsconfig/react-native from 3.0.3 to 3.0.9 in /GraphRNSample](https://github.com/microsoftgraph/msgraph-sample-react-native/commit/c750ce138ecd6229547bb8aba840d39192c551c7) - `2026-10-29T18:53:19Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump @tsconfig/react-native from 3.0.3 to 3.0.9 in /GraphRNSample](https://github.com/microsoftgraph/msgraph-sample-react-native/pull/189)

### MicrosoftDocs/dynamics365smb-docs (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/a5a1ce25426ed7e3efdb9e48a594d2bc858dbe55) - `2026-10-29T19:03:52Z` - Learn Build Service GitHub App
- [Merge pull request #5249 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/1f79d06932de65385ae7edfe584f2bb314b90f9a) - `2026-10-29T19:03:00Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### microsoft/kiota-dart (2 commit(s), signal 87)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [chore: release main (#161)](https://github.com/microsoft/kiota-dart/commit/6d886ea27d7af0fd65f8713c518c0169d317b29f) - `2026-10-29T19:01:29Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore: release main](https://github.com/microsoft/kiota-dart/pull/161)
- [fix(json): support content-type parameters and whitespace in json fac…](https://github.com/microsoft/kiota-dart/commit/0f57078df55e1abd078e063161c83dd9ab519c8d) - `2026-10-29T18:58:11Z` - Hardik K (@hardikkaurani) - PR: [fix(json): support content-type parameters and whitespace in json factories](https://github.com/microsoft/kiota-dart/pull/160)

### microsoft/sql-server-samples (2 commit(s), signal 52)

Tags: `human-authored, release-language, samples`

- [Merge pull request #1535 from microsoft/uc-msft-patch-1](https://github.com/microsoft/sql-server-samples/commit/3c71696a3942879f0481f3bd65fe112a40023f18) - `2026-10-29T18:33:08Z` - Umachandar Jayachandran (@uc-msft) - PR: [Update SQL checks for engine edition and version](https://github.com/microsoft/sql-server-samples/pull/1535)
- [Update SQL checks for engine edition and version](https://github.com/microsoft/sql-server-samples/commit/27cc5b6cbbbbac9577b4c7686dd1bfd05f0c6ec8) - `2026-10-29T18:25:59Z` - Umachandar Jayachandran (@uc-msft) - PR: [Update SQL checks for engine edition and version](https://github.com/microsoft/sql-server-samples/pull/1535)

### Azure-Samples/pghacker-mcp (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Prompt hardening](https://github.com/Azure-Samples/pghacker-mcp/commit/a81837fbb2f86a954cc5c55cea9e8fbb77bac2ea) - `2026-10-29T18:30:15Z` - maxluk (@maxluk)
- [Enforce authenticated and encrypted AKS workload communication](https://github.com/Azure-Samples/pghacker-mcp/commit/51f2a7a848814bf217306fc74de12d9beffa33da) - `2026-10-29T18:30:15Z` - maxluk (@maxluk)

### Azure/Commercial-Marketplace-SaaS-Accelerator (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #908 from danfiedler-msft/danfiedler/pin-actions](https://github.com/Azure/Commercial-Marketplace-SaaS-Accelerator/commit/b59a00a1adfdb5ea84e9d595a141a9f9b6ae1615) - `2026-10-29T17:32:23Z` - Aidan Ryan (@ajryan) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure/Commercial-Marketplace-SaaS-Accelerator/pull/908)
- [Merge pull request #907 from Azure/dependabot/github_actions/github-a…](https://github.com/Azure/Commercial-Marketplace-SaaS-Accelerator/commit/87afb2ae4deab77d198aaf63a27e555cdba5d162) - `2026-10-29T17:31:33Z` - Aidan Ryan (@ajryan) - PR: [Bump the github-actions group with 6 updates](https://github.com/Azure/Commercial-Marketplace-SaaS-Accelerator/pull/907)

### microsoft/XBOX-Godot-Sample (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add local initialization telemetry for GDK and PlayFab (#209)](https://github.com/microsoft/XBOX-Godot-Sample/commit/e260a428f5596eac3899d841a2220b1939129489) - `2026-10-30T18:36:51Z` - James Lenell (@jameslen-atg) - PR: [Add local initialization telemetry for GDK and PlayFab](https://github.com/microsoft/XBOX-Godot-Sample/pull/209)

### microsoftgraph/msgraph-sdk-java-core (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [ci: update android tools setup (#2141)](https://github.com/microsoftgraph/msgraph-sdk-java-core/commit/6d479ddb605017310fd368c6dc16b54b18c1ae27) - `2026-10-30T18:33:34Z` - Gavin Barron (@gavinbarron) - PR: [ci: update android tools setup](https://github.com/microsoftgraph/msgraph-sdk-java-core/pull/2141)

### MicrosoftLearning/mslearn-unify-data (1 commit(s), signal 76)

Tags: `human-authored, training, watchlist`

- [Add Caldova L300 assets and six-hour L400 challenge lab (#1)](https://github.com/MicrosoftLearning/mslearn-unify-data/commit/89652c34f925f8211a82f5a8bba8184bf93a9356) - `2026-10-30T17:51:00Z` - Angie Rudduck (@AngieRudduck) - PR: [Add Caldova L300 assets and six-hour L400 challenge lab](https://github.com/MicrosoftLearning/mslearn-unify-data/pull/1)

### microsoft/AzureTRE (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Fix the Gitea workspace service and limit Key Vault roles (#5284)](https://github.com/microsoft/AzureTRE/commit/fb26638303479e2d09431f5e7880a6ea717c2cde) - `2026-10-30T17:24:30Z` - Jay W (@JayDoubleu) - PR: [Fix the Gitea workspace service and limit Key Vault roles](https://github.com/microsoft/AzureTRE/pull/5284)

### Azure-Samples/dotnetapp-azure-prometheus (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Pin GitHub Actions to full-length commit SHAs (#9)](https://github.com/Azure-Samples/dotnetapp-azure-prometheus/commit/4c2a664c67b3d48194b26bc21ea34b570ae6873a) - `2026-10-30T17:03:28Z` - Dan Fiedler (@danfiedler-msft) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/dotnetapp-azure-prometheus/pull/9)

### microsoft/Agent365-Samples (1 commit(s), signal 101)

Tags: `human-authored, product:Azure AI, samples, security, watchlist`

- [Bump vulnerable npm dependencies in Node.js samples (#355)](https://github.com/microsoft/Agent365-Samples/commit/ec87071f0b945cb7ef939066f80d239823e26cfb) - `2026-10-30T16:32:39Z` - Rick Brighenti (@rbrighenti) - PR: [Bump vulnerable npm dependencies in Node.js samples (Dependabot #36-#43)](https://github.com/microsoft/Agent365-Samples/pull/355)

### OfficeDev/office-scripts-docs-reference (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, docs`

- [Bump fast-uri from 3.1.8 to 3.1.9 in /generate-docs (#470)](https://github.com/OfficeDev/office-scripts-docs-reference/commit/97f8f415842e13e004d7c53c1d24fe45653e50c0) - `2026-10-30T16:23:27Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump fast-uri from 3.1.8 to 3.1.9 in /generate-docs](https://github.com/OfficeDev/office-scripts-docs-reference/pull/470)

### Azure-Samples/hello-azd (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, samples`

- [Bump actions/checkout from 4.4.0 to 7.0.1 in the github-actions group…](https://github.com/Azure-Samples/hello-azd/commit/e9abac294ce22e0a921debf300f0da0fd6d7f655) - `2026-10-30T14:53:03Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/checkout from 4.4.0 to 7.0.1 in the github-actions group](https://github.com/Azure-Samples/hello-azd/pull/12)

### Azure-Samples/decision-point (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Point Play Decision Point at aka.ms/decision-point/play (#2)](https://github.com/Azure-Samples/decision-point/commit/868cff633799bece84553b2205cef73bb0e9dec2) - `2026-10-30T13:52:09Z` - sadiq-emumba (@sadiqali-emumba) - PR: [Point Play Decision Point at aka.ms/decision-point/play](https://github.com/Azure-Samples/decision-point/pull/2)

### dotnet/docs-maui (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Android (.NET 10/11): document Google Play code optimization requirem…](https://github.com/dotnet/docs-maui/commit/6a8412e5801d5d19b3a3809ed26d79fa4b4d584b) - `2026-10-30T13:51:21Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Android docs (.NET 10/11): Google Play code optimization requirements](https://github.com/dotnet/docs-maui/pull/3602)

### microsoft/aspire-samples (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Use the Aspire devcontainer feature instead of the old .NET Aspire on…](https://github.com/microsoft/aspire-samples/commit/bdc638b61bf8afd8b275d54a9ea7259be377ef8c) - `2026-10-30T13:36:29Z` - David Pine (@IEvangelist) - PR: [Use the Aspire devcontainer feature instead of the old .NET Aspire one](https://github.com/microsoft/aspire-samples/pull/2088)

### MicrosoftDocs/semantic-kernel-docs (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update MEVD connectors docs (#460)](https://github.com/MicrosoftDocs/semantic-kernel-docs/commit/7c5c0568a974a6268680d0745ca345d93610baaf) - `2026-10-30T11:17:21Z` - Adam Sitnik (@adamsitnik) - PR: [Update MEVD connectors docs](https://github.com/MicrosoftDocs/semantic-kernel-docs/pull/460)

### MicrosoftDocs/windowsserverdocs (1 commit(s), signal 101)

Tags: `docs, human-authored, security, watchlist`

- [Clarify security group descriptions and risks (#8144)](https://github.com/MicrosoftDocs/windowsserverdocs/commit/2205ce8e55001a9b5e8e0de43981baa8ad782562) - `2026-10-30T10:50:33Z` - Herbert Mauerer (@HerbertMauerer) - PR: [Clarify security group descriptions and risks](https://github.com/MicrosoftDocs/windowsserverdocs/pull/8144)

### Azure-Samples/cognitive-services-speech-sdk (1 commit(s), signal 76)

Tags: `human-authored, product:Azure SDK, samples, watchlist`

- [Clarify TTS skill guidance and installation (#3101)](https://github.com/Azure-Samples/cognitive-services-speech-sdk/commit/dccacc77bce7dd4fc63041a1f4d6f2107b70d055) - `2026-10-30T08:28:26Z` - lixinyu (@lixinyu94) - PR: [Clarify TTS skill guidance and installation](https://github.com/Azure-Samples/cognitive-services-speech-sdk/pull/3101)

### Azure-Samples/azure-openai-keyless-js (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, product:Azure AI, samples, watchlist`

- [chore(deps): bump github/codeql-action/upload-sarif (#13)](https://github.com/Azure-Samples/azure-openai-keyless-js/commit/7561946580277c2da4ec7b656185d3583ff0cbf5) - `2026-10-30T08:02:52Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump github/codeql-action/upload-sarif from 4.39.0 to 4.39.1 in the github-actions group](https://github.com/Azure-Samples/azure-openai-keyless-js/pull/13)

### Azure/azure-sdk-for-go (1 commit(s), signal 66)

Tags: `bot-only, docs, product:Azure SDK, release, watchlist`

- Release: [sdk/resourcemanager/storagemover/armstoragemover/v2.5.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/storagemover/armstoragemover/v2.5.0) - `2026-10-30T07:50:54Z`
- Release: [sdk/resourcemanager/privatetrafficmanager/armprivatetrafficmanager/v0.1.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/privatetrafficmanager/armprivatetrafficmanager/v0.1.0) - `2026-10-30T07:41:27Z`
- Release: [sdk/security/keyvault/azsecrets/v1.5.1](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/security/keyvault/azsecrets/v1.5.1) - `2026-10-29T21:31:58Z`
- [[AutoPR sdk-resourcemanager/storagemover/armstoragemover]-generated-f…](https://github.com/Azure/azure-sdk-for-go/commit/344629ae4fac22d02ce1631074fcca3f75638271) - `2026-10-30T07:16:12Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR sdk-resourcemanager/storagemover/armstoragemover]-generated-from-SDK Generation - Go-6798572](https://github.com/Azure/azure-sdk-for-go/pull/27530)

### MicrosoftDocs/mcp (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Pin GitHub Actions to full-length commit SHAs (#222)](https://github.com/MicrosoftDocs/mcp/commit/f0a9478a954c9b3a7c6525a5183466902ca60731) - `2026-10-30T04:02:36Z` - Xie Yan (@Xieyan) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/MicrosoftDocs/mcp/pull/222)

### Azure/azureml-examples (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Fix NYC taxi prep for pandas 2 (#4136)](https://github.com/Azure/azureml-examples/commit/27f4487a6060b80982ef0793e6ebcea90f509d37) - `2026-10-30T03:17:25Z` - lavakumarrepala (@lavakumarrepala) - PR: [Fix NYC taxi prep for pandas 2](https://github.com/Azure/azureml-examples/pull/4136)

### Azure/azure-sdk-for-cpp (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Migrate Queue private protocol layer to TypeSpec (#7510)](https://github.com/Azure/azure-sdk-for-cpp/commit/4967deb2c0d806ba7b1102cee218f83fe230880a) - `2026-10-30T00:27:49Z` - JinmingHu (@Jinming-Hu) - PR: [Migrate Queue private protocol layer to TypeSpec](https://github.com/Azure/azure-sdk-for-cpp/pull/7510)

### MicrosoftDocs/azure-docs-sdk-java (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/c94f03ae63a291e54b2ade823ae4b24f35632351) - `2026-10-29T23:42:25Z` - azure-sdk (@azure-sdk)

### microsoft/teams-agent-accelerator-templates (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, product:Azure AI, samples, watchlist`

- [Bump undici from 6.29.0 to 6.29.1 in /js/data-analyst-agent (#194)](https://github.com/microsoft/teams-agent-accelerator-templates/commit/66483cfb849d2938427c716a4fe70ceb35624d3c) - `2026-10-29T23:39:59Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump undici from 6.29.0 to 6.29.1 in /js/data-analyst-agent](https://github.com/microsoft/teams-agent-accelerator-templates/pull/194)

### MicrosoftDocs/azure-docs-sdk-cpp (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-cpp/commit/661b65c4060781e55f17be7fbcf7873bd325c074) - `2026-10-29T23:18:27Z` - azure-sdk (@azure-sdk)

### Azure-Samples/functions-connectors-net (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add standalone Office 365 polling and webhook samples (#8)](https://github.com/Azure-Samples/functions-connectors-net/commit/768c4266a1bb0767ef438beaca886cdcffafd92b) - `2026-10-29T22:40:20Z` - Lily Ma (@lilyjma) - PR: [Add standalone Office 365 polling and webhook samples](https://github.com/Azure-Samples/functions-connectors-net/pull/8)

### microsoft/WindowsAppSDK (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Sets the template constraint to .NET 10+, since .NET 10+ is required.…](https://github.com/microsoft/WindowsAppSDK/commit/89d93ef67cfb515b6faf6cc9adb803f935b4352a) - `2026-10-29T21:33:30Z` - Morten Nielsen (@dotMorten) - PR: [Require .NET SDK 10.0+ for .NET 10+ templates](https://github.com/microsoft/WindowsAppSDK/pull/6914)

### MicrosoftDocs/.github (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Fix bot entry in cla.yml (#81)](https://github.com/MicrosoftDocs/.github/commit/a36c68e086cc517210bbc4494fdc21ff3af853ae) - `2026-10-29T19:57:49Z` - John Downs (@johndowns) - PR: [Fix reliability-hub-content-automation bot entry in cla.yml](https://github.com/MicrosoftDocs/.github/pull/81)

### microsoft/vscode-mock-debug (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, samples`

- [Bump actions/setup-node from 7.0.0 to 7.1.0 in the github-actions gro…](https://github.com/microsoft/vscode-mock-debug/commit/0322d057260f85c50e2e2696d6950c203b73b272) - `2026-10-29T19:48:22Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-node from 7.0.0 to 7.1.0 in the github-actions group](https://github.com/microsoft/vscode-mock-debug/pull/149)

### microsoft/vscode-remote-try-java (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, samples`

- [Bump actions/setup-java from 6.0.1 to 6.1.0 in the github-actions gro…](https://github.com/microsoft/vscode-remote-try-java/commit/d475a65f42699fff48d623a517305efca9cece78) - `2026-10-29T19:47:23Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-java from 6.0.1 to 6.1.0 in the github-actions group](https://github.com/microsoft/vscode-remote-try-java/pull/131)

### OfficeDev/Office-Add-in-samples (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [[Outlook] (event-based activation) Add unified manifest support (#1599)](https://github.com/OfficeDev/Office-Add-in-samples/commit/908ec9f714e6c2fefdb1a621b948ca87f981d83e) - `2026-10-29T19:34:05Z` - Sam Ramon (@samantharamon) - PR: [[Outlook] (event-based activation) Add unified manifest support](https://github.com/OfficeDev/Office-Add-in-samples/pull/1599)

### microsoft/kiota-abstractions-go (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [fix(headers): validate addition in RequestHeaders.TryAdd and delegate…](https://github.com/microsoft/kiota-abstractions-go/commit/840be4ef2049766d97c07fab12b1b6b588e6cbc6) - `2026-10-29T19:02:27Z` - Hardik K (@hardikkaurani) - PR: [fix(headers): validate addition in RequestHeaders.TryAdd and delegate AddAll](https://github.com/microsoft/kiota-abstractions-go/pull/303)

### MicrosoftDocs/ai-builder (1 commit(s), signal 26)

Tags: `bot-only, docs, watchlist`

- [Merge pull request #1255 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/ai-builder/commit/ea34cae06bc6ccd89b57ad988d4cfd48384ddadb) - `2026-10-29T19:02:00Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### Azure-Samples/msal-managed-identity (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Merge pull request #39 from danfiedler-msft/danfiedler/pin-actions](https://github.com/Azure-Samples/msal-managed-identity/commit/88235f7836acabdc00889429f3f3b7a935e8b6d4) - `2026-10-29T18:58:43Z` - Gladwin Johnson VR (@gladjohn) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/msal-managed-identity/pull/39)

### microsoft/playwright-pytest (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, docs`

- [chore(deps-dev): bump setuptools in /pytest-playwright-asyncio (#340)](https://github.com/microsoft/playwright-pytest/commit/f71b92ff1e49dda4df03c43be3a33a93bb2c8481) - `2026-10-29T18:52:25Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps-dev): bump setuptools from 83.0.0 to 84.1.0 in /pytest-playwright-asyncio](https://github.com/microsoft/playwright-pytest/pull/340)

### microsoft/azure-devops-skills (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Merge pull request #15 from SchulteDev/upstream-claude-code-plugin](https://github.com/microsoft/azure-devops-skills/commit/b418a6c8fa9fd622274882a1378e664df746f356) - `2026-10-29T18:46:30Z` - Dan Hellem (@danhellem) - PR: [Make the repository installable as a Claude Code plugin](https://github.com/microsoft/azure-devops-skills/pull/15)

### microsoft/LAB730-ignite-2026-healthcare-agents (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, training, watchlist`

- [minor changes for clarity](https://github.com/microsoft/LAB730-ignite-2026-healthcare-agents/commit/30a1709ed305ae7f43775c5cb86f9006a03720f8) - `2026-10-29T18:31:59Z` - Jameson (@jmerkow)

### microsoft/amplifier-app-cli (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [ci: pin GitHub Actions to full-length commit SHAs (#279)](https://github.com/microsoft/amplifier-app-cli/commit/631c4bdbcf3dcd2da20456ad6ccef386e778c101) - `2026-10-29T18:29:37Z` - Dan Fiedler (@danfiedler-msft) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/microsoft/amplifier-app-cli/pull/279)

### microsoft/amplifier-module-tool-web (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [ci: pin GitHub Actions to full-length commit SHAs (#23)](https://github.com/microsoft/amplifier-module-tool-web/commit/2a58cf71f6f941f5b5ef28d59564f5d47af5f294) - `2026-10-29T18:19:57Z` - Salil Das (@sadlilas) - PR: [ci: pin GitHub Actions to full-length commit SHAs](https://github.com/microsoft/amplifier-module-tool-web/pull/23)

### microsoft/amplifier-module-tool-todo (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [ci: pin GitHub Actions to full-length commit SHAs (#6)](https://github.com/microsoft/amplifier-module-tool-todo/commit/b920bfaf28454a3e6c977ef6cc0b54eb17dd4537) - `2026-10-29T18:19:35Z` - Salil Das (@sadlilas) - PR: [ci: pin GitHub Actions to full-length commit SHAs](https://github.com/microsoft/amplifier-module-tool-todo/pull/6)

### microsoft/amplifier-module-tool-filesystem (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [ci: pin GitHub Actions to full-length commit SHAs (#18)](https://github.com/microsoft/amplifier-module-tool-filesystem/commit/c57ee61b744fde399e4d2b6f2a1ea8d7d7ecabd8) - `2026-10-29T18:19:13Z` - Salil Das (@sadlilas) - PR: [ci: pin GitHub Actions to full-length commit SHAs](https://github.com/microsoft/amplifier-module-tool-filesystem/pull/18)

### microsoft/amplifier-module-loop-streaming (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [ci: pin GitHub Actions to full-length commit SHAs (#69)](https://github.com/microsoft/amplifier-module-loop-streaming/commit/a876e6ada2e8a597caaab7b6af9627ccc53ecaa7) - `2026-10-29T18:18:49Z` - Salil Das (@sadlilas) - PR: [ci: pin GitHub Actions to full-length commit SHAs](https://github.com/microsoft/amplifier-module-loop-streaming/pull/69)

### microsoft/amplifier-module-context-simple (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [ci: pin GitHub Actions to full-length commit SHAs (#50)](https://github.com/microsoft/amplifier-module-context-simple/commit/550af35c5b8e7648c73a4c5be7c850affecc96ee) - `2026-10-29T18:18:29Z` - Salil Das (@sadlilas) - PR: [ci: pin GitHub Actions to full-length commit SHAs](https://github.com/microsoft/amplifier-module-context-simple/pull/50)

### OfficeDev/office-js-docs-pr (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [[Outlook] (online meeting) Document changes to the Join button's meet…](https://github.com/OfficeDev/office-js-docs-pr/commit/8d3514d22a2c3d34fb150e2c6c580fe672b26dbf) - `2026-10-29T18:00:23Z` - Sam Ramon (@samantharamon) - PR: [[Outlook] (online meeting) Document changes to the Join button's meeting link](https://github.com/OfficeDev/office-js-docs-pr/pull/5918)

### Azure-Samples/confidential-computing (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add additional scenarios and examples (#41)](https://github.com/Azure-Samples/confidential-computing/commit/772221fca5d96594aecf6c822ef6f4a19be3c86d) - `2026-10-29T17:59:14Z` - Simon Gallagher (@vinfnet) - PR: [Add additional scenarios and examples](https://github.com/Azure-Samples/confidential-computing/pull/41)

### Azure/dacs (1 commit(s), signal 56)

Tags: `bot-only, dependency-noise, release, samples, watchlist`

- Release: [v0.1.0-alpha.3](https://github.com/Azure/dacs/releases/tag/v0.1.0-alpha.3) - `2026-10-29T18:44:17Z`
- [build(deps): bump the docker group across 2 directories with 2 updates](https://github.com/Azure/dacs/commit/ce9722d6f1de6028153b762bafc417bfcd6cddb8) - `2026-10-29T17:54:29Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump the docker group across 2 directories with 2 updates](https://github.com/Azure/dacs/pull/153)

### microsoft/PowerApps-Samples (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Fix link to page results](https://github.com/microsoft/PowerApps-Samples/commit/81d1364ff6ac4d4f94ba2719d308efc31995059e) - `2026-10-29T17:49:54Z` - Jim Daly (@JimDaly)

### dotnet/blazor-samples (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, samples`

- [Bump the nuget group with 3 updates (#685)](https://github.com/dotnet/blazor-samples/commit/667ca0ae3edf683abc5234647cca441a17313f6d) - `2026-10-29T17:46:55Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the nuget group with 3 updates](https://github.com/dotnet/blazor-samples/pull/685)

</details>
