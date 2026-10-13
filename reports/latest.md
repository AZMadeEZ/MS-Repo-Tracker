# Microsoft Ecosystem Daily Brief - 2026-10-13

> Status: Fresh at generation. Current freshness is tracked in `reports/status.json`.
> Generated: 2026-10-13 19:54 UTC - Window: 24.1h from 2026-10-12 19:47 UTC to 2026-10-13 19:54 UTC.
> 115 repo(s) moved - 755 commit(s) - 27 release item(s) - 25 high-signal repo(s).

## Plain-English Summary

- Azure, .NET led the visible product-area activity in this window.
- 27 release item(s) were detected during the window.
- Security-related changes appeared in dotnet/android-api-docs, MicrosoftDocs/azure-aks-docs, MicrosoftDocs/learn.
- Start with human-authored changes in dotnet/android-api-docs, MicrosoftDocs/azure-aks-docs, MicrosoftDocs/learn, Azure/dacs.
- 130 event(s) look automated, bot-heavy, dependency, or generated; review the curated sections before raw volume.

## Headline Metrics

| Metric | Value |
| --- | ---: |
| Inventory repositories | 16680 |
| Repositories after filters | 2627 |
| `pushed_at` candidates | 210 |
| Enrichment candidates | 210 |
| Repositories with movement | 115 |
| Default-branch commits | 755 |

## What Changed That Matters

| Repository | Score | Change | Actor | Noise | Headline | Time |
| --- | ---: | --- | --- | --- | --- | --- |
| [dotnet/android-api-docs](https://github.com/dotnet/android-api-docs) | 100 | security_fix | human | low | [Add Android.Security.Net.Config API 37 documentation](https://github.com/dotnet/android-api-docs/pull/841) | `2026-10-13T17:08:00Z` |
| [MicrosoftDocs/azure-aks-docs](https://github.com/MicrosoftDocs/azure-aks-docs) | 100 | security_fix | human | low | [security: Document external node CSR role permission breaking change …](https://github.com/MicrosoftDocs/azure-aks-docs/commit/5b20bb37906d55958b5d66d9ed36c5e3d6555ef2) | `2026-10-13T16:59:57Z` |
| [MicrosoftDocs/learn](https://github.com/MicrosoftDocs/learn) | 100 | security_fix | human | low | [Security Operations and Remediation Workflows with GitHub Advanced Se…](https://github.com/MicrosoftDocs/learn/commit/607e605e31b0b128c2ed81a70bb0f72fe644c693) | `2026-10-13T15:51:06Z` |
| [MicrosoftDocs/learn](https://github.com/MicrosoftDocs/learn) | 100 | security_fix | human | low | [Security Campaigns & Prevention-First Strategy (#56436) (#56499)](https://github.com/MicrosoftDocs/learn/commit/49c369d2f2c43ea20d3a444cf9fd6be5d3c9695d) | `2026-10-13T15:51:03Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 100 | release | unknown | low | [azure-ai-agentserver-activity_1.0.0b4](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-activity_1.0.0b4) | `2026-10-13T18:46:49Z` |
| [Azure/dacs](https://github.com/Azure/dacs) | 100 | release | unknown | low | [v0.1.0-alpha.2](https://github.com/Azure/dacs/releases/tag/v0.1.0-alpha.2) | `2026-10-13T17:00:57Z` |
| [Azure/dacs](https://github.com/Azure/dacs) | 100 | release | human | low | [ci: run build on tag and generate docker image artifacts](https://github.com/Azure/dacs/pull/84) | `2026-10-13T16:45:09Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 100 | release | human | low | [[azure-ai-evaluation] Release 1.18.9](https://github.com/Azure/azure-sdk-for-python/pull/49504) | `2026-10-13T16:06:18Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 100 | release | unknown | low | [Azure.ResourceManager.Compute.BulkActions_1.2.0-beta.4](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.Compute.BulkActions_1.2.0-beta.4) | `2026-10-13T15:37:47Z` |
| [microsoft/kiota-python](https://github.com/microsoft/kiota-python) | 100 | release | unknown | low | [microsoft-kiota-serialization-multipart: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-serialization-multipart-v1.14.3) | `2026-10-13T13:47:33Z` |
| [microsoft/kiota-python](https://github.com/microsoft/kiota-python) | 100 | release | unknown | low | [microsoft-kiota-serialization-text: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-serialization-text-v1.14.3) | `2026-10-13T13:47:32Z` |
| [microsoft/kiota-dotnet](https://github.com/microsoft/kiota-dotnet) | 100 | release | unknown | low | [v2.1.5](https://github.com/microsoft/kiota-dotnet/releases/tag/v2.1.5) | `2026-10-13T13:20:05Z` |
| [microsoft/vscode-docs](https://github.com/microsoft/vscode-docs) | 100 | release | human | low | [Recovery release 1.141.1](https://github.com/microsoft/vscode-docs/pull/10467) | `2026-10-13T12:54:47Z` |
| [MicrosoftDocs/dynamics-365-customer-engagement](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement) | 100 | release | human | low | [Field Service ur9.3 8.8.150.60 release notes (#17173)](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement/commit/df5f85bec60a6aeb59931908447ab313777d986f) | `2026-10-13T12:26:22Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 100 | release | unknown | low | [Azure.ResourceManager.Compute_1.18.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.Compute_1.18.0) | `2026-10-13T10:40:48Z` |

## Product Areas

| Product area | Signal | Repos | Events | Releases | Security | Top links |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Azure | 163 | 51 | 199 | 21 | 1 | [security: Document external node CSR role permission breaking change …](https://github.com/MicrosoftDocs/azure-aks-docs/commit/5b20bb37906d55958b5d66d9ed36c5e3d6555ef2); [azure-ai-agentserver-activity_1.0.0b4](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-activity_1.0.0b4); [v0.1.0-alpha.2](https://github.com/Azure/dacs/releases/tag/v0.1.0-alpha.2) |
| Unmapped Activity | 64 | 31 | 88 | 0 | 2 | [Security Operations and Remediation Workflows with GitHub Advanced Se…](https://github.com/MicrosoftDocs/learn/commit/607e605e31b0b128c2ed81a70bb0f72fe644c693); [Security Campaigns & Prevention-First Strategy (#56436) (#56499)](https://github.com/MicrosoftDocs/learn/commit/49c369d2f2c43ea20d3a444cf9fd6be5d3c9695d); [Field Service ur9.3 8.8.150.60 release notes (#17173)](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement/commit/df5f85bec60a6aeb59931908447ab313777d986f) |
| .NET | 28 | 12 | 38 | 0 | 1 | [Add Android.Security.Net.Config API 37 documentation](https://github.com/dotnet/android-api-docs/pull/841); [Add Android HID device documentation](https://github.com/dotnet/android-api-docs/pull/838); [Add InputMethodManager animation documentation](https://github.com/dotnet/android-api-docs/pull/832) |
| Microsoft Graph | 23 | 9 | 39 | 6 | 0 | [microsoft-kiota-serialization-multipart: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-serialization-multipart-v1.14.3); [microsoft-kiota-serialization-text: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-serialization-text-v1.14.3); [microsoft-kiota-serialization-form: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-serialization-form-v1.14.3) |
| Identity | 8 | 2 | 8 | 0 | 0 | [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/5b4de6fbf5ed769f456035cf8cefb202de2ab015); [Update cross-tenant-access-overview.md](https://github.com/MicrosoftDocs/entra-docs/commit/d232317b9764e7f6fd301001850cd7a7ab3abaa7); [Update cross-tenant-access-overview.md](https://github.com/MicrosoftDocs/entra-docs/commit/96112b88b3fc5a0c3e5f145e23651392e4013b5d) |
| Microsoft 365 | 6 | 6 | 9 | 0 | 0 | [Updates to preview-feature article](https://github.com/MicrosoftDocs/msteams-docs/pull/14644); [Auto Publish – main to live - 2026-10-13 15:00 UTC](https://github.com/MicrosoftDocs/msteams-docs/pull/14657); [Clarify border indexes for Excel conditional formatting](https://github.com/MicrosoftDocs/VBA-Docs/pull/1970) |
| PowerShell | 6 | 2 | 6 | 0 | 0 | [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/19f1c024e35badc1ffa6f78936fde596c91e32dd); [Make the WinUI app per-monitor DPI aware](https://github.com/microsoft/Aion-Instruct-Preview-Sample/pull/13); [Update geographical-availability-copilot.md (#12028)](https://github.com/MicrosoftDocs/power-platform/commit/e601fd6673c7d13351dcb1559362ac15b39f808b) |
| Windows | 5 | 1 | 5 | 0 | 0 | [Update WindowsServerDocs/manage/windows-admin-center/azure/extension-…](https://github.com/MicrosoftDocs/windowsserverdocs/commit/f0b090426599f586bc237eb60675b5a3105d4a5b); [Update WindowsServerDocs/manage/windows-admin-center/azure/extension-…](https://github.com/MicrosoftDocs/windowsserverdocs/commit/9364fd987567e8769f5a25074e8c9296137ed8be); [Update WindowsServerDocs/manage/windows-admin-center/azure/manage-arc…](https://github.com/MicrosoftDocs/windowsserverdocs/commit/44deab5fe7abf77a0e2c4a1d651ca66288ee1317) |

## Today's Top Links

| Priority | Repository | Why read it |
| ---: | --- | --- |
| 1 | [dotnet/android-api-docs](https://github.com/dotnet/android-api-docs) | [Security-related change: Add Android.Security.Net.Config API 37 documentation](https://github.com/dotnet/android-api-docs/pull/841) |
| 2 | [MicrosoftDocs/azure-aks-docs](https://github.com/MicrosoftDocs/azure-aks-docs) | [Security-related change: security: Document external node CSR role permission breaking change …](https://github.com/MicrosoftDocs/azure-aks-docs/commit/5b20bb37906d55958b5d66d9ed36c5e3d6555ef2) |
| 3 | [MicrosoftDocs/learn](https://github.com/MicrosoftDocs/learn) | [Security-related change: Security Operations and Remediation Workflows with GitHub Advanced Se…](https://github.com/MicrosoftDocs/learn/commit/607e605e31b0b128c2ed81a70bb0f72fe644c693) |
| 4 | [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [Release activity: azure-ai-agentserver-activity_1.0.0b4](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-activity_1.0.0b4) |
| 5 | [Azure/dacs](https://github.com/Azure/dacs) | [Release activity: v0.1.0-alpha.2](https://github.com/Azure/dacs/releases/tag/v0.1.0-alpha.2) |
| 6 | [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Release activity: Azure.ResourceManager.Compute.BulkActions_1.2.0-beta.4](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.Compute.BulkActions_1.2.0-beta.4) |
| 7 | [microsoft/kiota-python](https://github.com/microsoft/kiota-python) | [Release activity: microsoft-kiota-serialization-multipart: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-serialization-multipart-v1.14.3) |
| 8 | [microsoft/kiota-dotnet](https://github.com/microsoft/kiota-dotnet) | [Release activity: v2.1.5](https://github.com/microsoft/kiota-dotnet/releases/tag/v2.1.5) |

## Noise and Automation

- 130 event(s) look automated, bot-heavy, dependency, generated, or medium/high noise.
- Top noisy repositories: microsoft/kiota-samples, microsoft/kiota-ruby, Azure-Samples/Durable-Task-Scheduler, Azure/azure-sdk-for-net, microsoft/kiota-python.
- Noise mix: Docs: 52, Dependency: 36, SDK: 15, CI/Infra: 10, Sample: 8, Release: 5, Fix: 3, Automation: 1.

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
| Repos counted | 210 |
| Repos enriched | 115 |

</details>

<details>
<summary>Show supporting signal, release, and lifecycle tables</summary>

## High-Signal Items

| Repository | Score | Tags |
| --- | ---: | --- |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 150 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 137 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [microsoft/kiota-python](https://github.com/microsoft/kiota-python) | 134 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 133 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 130 | docs, human-authored, product:Azure AI, product:Azure SDK, release, release-language, watchlist |
| [microsoft/kiota-dotnet](https://github.com/microsoft/kiota-dotnet) | 128 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [Azure/dacs](https://github.com/Azure/dacs) | 128 | human-authored, release, release-language, samples, watchlist |
| [MicrosoftDocs/learn](https://github.com/MicrosoftDocs/learn) | 125 | docs, human-authored, security, watchlist |
| [Azure-Samples/app-service-builder-vite](https://github.com/Azure-Samples/app-service-builder-vite) | 124 | human-authored, release-language, samples, security, watchlist |
| [dotnet/android-api-docs](https://github.com/dotnet/android-api-docs) | 109 | docs, human-authored, security, watchlist |
| [MicrosoftDocs/azure-aks-docs](https://github.com/MicrosoftDocs/azure-aks-docs) | 108 | docs, human-authored, security, watchlist |
| [MicrosoftDocs/fabric-docs](https://github.com/MicrosoftDocs/fabric-docs) | 100 | docs, human-authored, watchlist |
| [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs) | 100 | docs, human-authored, watchlist |
| [microsoft/kiota-samples](https://github.com/microsoft/kiota-samples) | 99 | docs, human-authored, product:Microsoft Graph, release-language, watchlist |
| [MicrosoftDocs/dynamics-365-customer-engagement](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement) | 94 | docs, human-authored, release-language, watchlist |

## Watchlist Hits

| Repository | Score | Matches |
| --- | ---: | --- |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 150 | products: Azure SDK; repos: Azure/azure-sdk-for-net; orgs: Azure; keywords: migration, release, sdk |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 137 | products: Azure SDK; repos: Azure/azure-sdk-for-java; orgs: Azure; keywords: release, sdk |
| [microsoft/kiota-python](https://github.com/microsoft/kiota-python) | 134 | products: Microsoft Graph, Azure SDK; keywords: graph, kiota, release, sdk |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 133 | products: Azure SDK; repos: Azure/azure-sdk-for-js; orgs: Azure; keywords: sdk |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 130 | products: Azure AI, Azure SDK; repos: Azure/azure-sdk-for-python; orgs: Azure; keywords: agent, copilot, release, sdk |
| [microsoft/kiota-dotnet](https://github.com/microsoft/kiota-dotnet) | 128 | products: Microsoft Graph, Azure SDK; keywords: graph, kiota, release, sdk |
| [Azure/dacs](https://github.com/Azure/dacs) | 128 | orgs: Azure; keywords: release |
| [MicrosoftDocs/learn](https://github.com/MicrosoftDocs/learn) | 125 | orgs: MicrosoftDocs; keywords: security |
| [Azure-Samples/app-service-builder-vite](https://github.com/Azure-Samples/app-service-builder-vite) | 124 | keywords: migration |
| [dotnet/android-api-docs](https://github.com/dotnet/android-api-docs) | 109 | keywords: security |
| [MicrosoftDocs/azure-aks-docs](https://github.com/MicrosoftDocs/azure-aks-docs) | 108 | orgs: MicrosoftDocs; keywords: breaking change, security |
| [MicrosoftDocs/fabric-docs](https://github.com/MicrosoftDocs/fabric-docs) | 100 | orgs: MicrosoftDocs |
| [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs) | 100 | repos: MicrosoftDocs/azure-docs; orgs: MicrosoftDocs |
| [microsoft/kiota-samples](https://github.com/microsoft/kiota-samples) | 99 | products: Microsoft Graph; repos: microsoft/kiota-samples; keywords: graph, kiota, msgraph |
| [MicrosoftDocs/dynamics-365-customer-engagement](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement) | 94 | orgs: MicrosoftDocs; keywords: copilot, release |

## Releases

| Repository | Release | Published |
| --- | --- | --- |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-ai-agentserver-activity_1.0.0b4](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-activity_1.0.0b4) | `2026-10-13T18:46:49Z` |
| [Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample) | [EPP Function ZIPs 128.1](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/releases/tag/epp-packages-128-1) | `2026-10-13T17:37:00Z` |
| [Azure/dacs](https://github.com/Azure/dacs) | [v0.1.0-alpha.2](https://github.com/Azure/dacs/releases/tag/v0.1.0-alpha.2) | `2026-10-13T17:00:57Z` |
| [Azure/dacs](https://github.com/Azure/dacs) | [v0.1.0-alpha.1](https://github.com/Azure/dacs/releases/tag/v0.1.0-alpha.1) | `2026-10-13T15:48:53Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.ResourceManager.Compute.BulkActions_1.2.0-beta.4](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.Compute.BulkActions_1.2.0-beta.4) | `2026-10-13T15:37:47Z` |
| [microsoft/kiota-python](https://github.com/microsoft/kiota-python) | [microsoft-kiota-serialization-multipart: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-serialization-multipart-v1.14.3) | `2026-10-13T13:47:33Z` |
| [microsoft/kiota-python](https://github.com/microsoft/kiota-python) | [microsoft-kiota-serialization-text: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-serialization-text-v1.14.3) | `2026-10-13T13:47:32Z` |
| [microsoft/kiota-python](https://github.com/microsoft/kiota-python) | [microsoft-kiota-serialization-form: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-serialization-form-v1.14.3) | `2026-10-13T13:47:31Z` |
| [microsoft/kiota-python](https://github.com/microsoft/kiota-python) | [microsoft-kiota-serialization-json: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-serialization-json-v1.14.3) | `2026-10-13T13:47:28Z` |
| [microsoft/kiota-python](https://github.com/microsoft/kiota-python) | [microsoft-kiota-http: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-http-v1.14.3) | `2026-10-13T13:47:27Z` |
| [microsoft/kiota-dotnet](https://github.com/microsoft/kiota-dotnet) | [v2.1.5](https://github.com/microsoft/kiota-dotnet/releases/tag/v2.1.5) | `2026-10-13T13:20:05Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.ResourceManager.Compute_1.18.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.Compute_1.18.0) | `2026-10-13T10:40:48Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.ResourceManager.ResilienceManagement_1.0.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.ResilienceManagement_1.0.0) | `2026-10-13T10:40:24Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.ResourceManager.PlatformValidation_1.0.0-beta.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.PlatformValidation_1.0.0-beta.1) | `2026-10-13T08:32:38Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/resourcemanager/network/armnetwork/v12.1.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/network/armnetwork/v12.1.0) | `2026-10-13T07:18:39Z` |
| [Azure-Samples/iot-edge-opc-plc](https://github.com/Azure-Samples/iot-edge-opc-plc) | [2.15.11](https://github.com/Azure-Samples/iot-edge-opc-plc/releases/tag/2.15.11) | `2026-10-13T06:48:41Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Microsoft.Azure.WebPubSub.AspNetCore_1.6.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Microsoft.Azure.WebPubSub.AspNetCore_1.6.0) | `2026-10-13T06:17:53Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-mgmt-commvaultcontentstore_1.0.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-commvaultcontentstore_1.0.0) | `2026-10-13T03:57:46Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-mgmt-cognitiveservices_15.0.0b6](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-cognitiveservices_15.0.0b6) | `2026-10-13T03:52:20Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure.resourcemanager+azure-resourcemanager-dataprotection_1.7.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-dataprotection_1.7.0-beta.1) | `2026-10-13T03:15:19Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure.resourcemanager+azure-resourcemanager-weightsandbiases_1.0.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-weightsandbiases_1.0.1) | `2026-10-13T03:14:03Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure+azure-sdk-bom_1.3.9](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-sdk-bom_1.3.9) | `2026-10-12T22:30:25Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-commvaultcontentstore_1.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-commvaultcontentstore_1.0.0) | `2026-10-12T21:33:25Z` |
| [Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample) | [EPP Function ZIPs 124.1](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/releases/tag/epp-packages-124-1) | `2026-10-12T21:17:54Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/resourcemanager/commvaultcontentstore/armcommvaultcontentstore/v1.0.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/commvaultcontentstore/armcommvaultcontentstore/v1.0.0) | `2026-10-12T21:09:01Z` |

## Repository Lifecycle

| Change | Count |
| --- | ---: |
| archived_changed | 0 |
| category_changed | 0 |
| default_branch_changed | 0 |
| fork_changed | 0 |
| new_repos | 7 |
| removed_repos | 0 |

## Recently Created Repositories

| Repository | Category | Created |
| --- | --- | --- |
| [Azure-Samples/app-service-builder-php](https://github.com/Azure-Samples/app-service-builder-php) | samples | `2026-10-13T13:03:30Z` |
| [Azure-Samples/app-service-builder-ai-agent](https://github.com/Azure-Samples/app-service-builder-ai-agent) | samples | `2026-10-12T20:29:08Z` |
| [Azure-Samples/app-service-builder-mcp-server](https://github.com/Azure-Samples/app-service-builder-mcp-server) | samples | `2026-10-12T20:27:52Z` |
| [Azure-Samples/app-service-builder-vite](https://github.com/Azure-Samples/app-service-builder-vite) | samples | `2026-10-12T20:26:46Z` |
| [Azure-Samples/app-service-builder-dotnet](https://github.com/Azure-Samples/app-service-builder-dotnet) | samples | `2026-10-12T20:25:31Z` |
| [Azure-Samples/app-service-builder-python](https://github.com/Azure-Samples/app-service-builder-python) | samples | `2026-10-12T20:24:11Z` |
| [Azure-Samples/app-service-builder-nodejs](https://github.com/Azure-Samples/app-service-builder-nodejs) | samples | `2026-10-12T20:22:54Z` |
| [Azure-Samples/app-service-builder-static-html](https://github.com/Azure-Samples/app-service-builder-static-html) | samples | `2026-10-12T19:52:31Z` |

## Category Summary

| Category | Repositories |
| --- | ---: |
| docs | 77 |
| samples | 34 |
| training | 4 |

## Organization Summary

| Org | Repositories |
| --- | ---: |
| MicrosoftDocs | 36 |
| microsoft | 28 |
| Azure-Samples | 18 |
| Azure | 16 |
| dotnet | 11 |
| OfficeDev | 3 |
| microsoftgraph | 2 |
| MicrosoftLearning | 1 |

</details>

<details>
<summary>Show raw repository activity</summary>

## Busiest Repositories

| Repository | Signal | Category | Commits | Releases | Newest commit |
| --- | ---: | --- | ---: | ---: | --- |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 150 | docs | 26 | 5 | `2026-10-13T19:41:38Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 137 | docs | 12 | 4 | `2026-10-13T19:46:59Z` |
| [microsoft/kiota-python](https://github.com/microsoft/kiota-python) | 134 | docs | 9 | 5 | `2026-10-13T18:56:45Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 133 | docs | 8 | 1 | `2026-10-13T19:46:44Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 130 | docs | 5 | 3 | `2026-10-13T16:06:18Z` |
| [microsoft/kiota-dotnet](https://github.com/microsoft/kiota-dotnet) | 128 | docs | 3 | 1 | `2026-10-13T17:45:44Z` |
| [Azure/dacs](https://github.com/Azure/dacs) | 128 | samples | 3 | 2 | `2026-10-13T16:45:09Z` |
| [MicrosoftDocs/learn](https://github.com/MicrosoftDocs/learn) | 125 | docs | 54 | 0 | `2026-10-13T17:21:43Z` |
| [Azure-Samples/app-service-builder-vite](https://github.com/Azure-Samples/app-service-builder-vite) | 124 | samples | 14 | 0 | `2026-10-13T12:58:43Z` |
| [dotnet/android-api-docs](https://github.com/dotnet/android-api-docs) | 109 | docs | 9 | 0 | `2026-10-13T17:27:30Z` |
| [MicrosoftDocs/azure-aks-docs](https://github.com/MicrosoftDocs/azure-aks-docs) | 108 | docs | 8 | 0 | `2026-10-13T17:08:39Z` |
| [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs) | 100 | docs | 66 | 0 | `2026-10-13T17:17:47Z` |
| [MicrosoftDocs/fabric-docs](https://github.com/MicrosoftDocs/fabric-docs) | 100 | docs | 28 | 0 | `2026-10-13T17:08:23Z` |
| [microsoft/kiota-samples](https://github.com/microsoft/kiota-samples) | 99 | docs | 14 | 0 | `2026-10-13T19:03:58Z` |
| [MicrosoftDocs/dynamics-365-customer-engagement](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement) | 94 | docs | 9 | 0 | `2026-10-13T13:08:12Z` |
| [Azure-Samples/fabric-cicd-generic-git](https://github.com/Azure-Samples/fabric-cicd-generic-git) | 91 | samples | 6 | 0 | `2026-10-13T19:52:45Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 91 | docs | 6 | 0 | `2026-10-13T00:32:31Z` |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 90 | samples | 15 | 0 | `2026-10-13T18:42:05Z` |
| [MicrosoftDocs/azure-compute-docs](https://github.com/MicrosoftDocs/azure-compute-docs) | 90 | docs | 15 | 0 | `2026-10-13T17:04:57Z` |
| [MicrosoftDocs/msteams-docs](https://github.com/MicrosoftDocs/msteams-docs) | 88 | docs | 3 | 0 | `2026-10-13T03:26:25Z` |

## Repository Details

### MicrosoftDocs/azure-docs (66 commit(s), signal 100)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #321419 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-docs/commit/777b18e1cadf4836ca6f1e801f7a01a6f8ceaa0d) - `2026-10-13T17:17:47Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #321418 from taylorrees1/patch-2](https://github.com/MicrosoftDocs/azure-docs/commit/aec7a926b9f6a2aed3522903ffa71a569202b4ee) - `2026-10-13T17:06:07Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Update Oracle AI Database@Azure service descriptions](https://github.com/MicrosoftDocs/azure-docs/commit/18a892e98f11fc6ee8011a6ebdfb4add0b861fde) - `2026-10-13T16:46:13Z` - taylorrees1 (@taylorrees1)
- [Merge pull request #321391 from EXPEkesheth/expekesheth-restore-guidance](https://github.com/MicrosoftDocs/azure-docs/commit/e08459a0fee89956ef660718ab538d309df54833) - `2026-10-13T15:56:08Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #321412 from henikaraa/tpe-ra-announcement-faq-202…](https://github.com/MicrosoftDocs/azure-docs/commit/8ce14258bb93f049c8e5e17acb59ff374cea5f46) - `2026-10-13T14:27:59Z` - prmerger-automator[bot] (@prmerger-automator[bot])

### MicrosoftDocs/learn (54 commit(s), signal 125)

Tags: `docs, human-authored, security, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/e23e2bdcfdac9ddd3fa158c9cc47c975634b8c8f) - `2026-10-13T17:21:43Z` - Learn Build Service GitHub App
- [Merge pull request #56500 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/learn/commit/94948f4d084d145e466fea8c6d5866fc84cd8266) - `2026-10-13T17:14:50Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Security Operations and Remediation Workflows with GitHub Advanced Se…](https://github.com/MicrosoftDocs/learn/commit/607e605e31b0b128c2ed81a70bb0f72fe644c693) - `2026-10-13T15:51:06Z` - Bowen Yang (@Albertyang0)
- [Security Campaigns & Prevention-First Strategy (#56436) (#56499)](https://github.com/MicrosoftDocs/learn/commit/49c369d2f2c43ea20d3a444cf9fd6be5d3c9695d) - `2026-10-13T15:51:03Z` - Bowen Yang (@Albertyang0)
- [refresh-wedebols-learn.wwl.explore-fundamentals-of-stream-processing …](https://github.com/MicrosoftDocs/learn/commit/03199566ce977fe6a0ab690c91a07730ea7f10d0) - `2026-10-13T11:39:32Z` - Wesley De Bolster (@weslbo)

### dotnet/runtime (29 commit(s), signal 65)

Tags: `docs, human-authored`

- [Add support for specifying load context in custom hosting APIs (#135460)](https://github.com/dotnet/runtime/commit/109674e8cdca9219a82d49fa7deee0467357dec1) - `2026-10-13T19:25:32Z` - Elinor Fung (@elinor-fung) - PR: [Add support for specifying load context in custom hosting APIs](https://github.com/dotnet/runtime/pull/135460)
- [Read metadata stream count as unsigned in MetadataReader (#135644)](https://github.com/dotnet/runtime/commit/d8ad3875aa545bb70067fbdeafdf1f9892a3d818) - `2026-10-13T18:47:31Z` - Oleg Dubovoi (@Empiree) - PR: [Read metadata stream count as unsigned in MetadataReader](https://github.com/dotnet/runtime/pull/135644)
- [Fix ILVerify entry stacks for nested exception filters (#134749)](https://github.com/dotnet/runtime/commit/1e0326fe5126a037a7a3d4483d38d4a9ba2cca21) - `2026-10-13T18:45:21Z` - Pkuyo (@pkuyo) - PR: [Fix ILVerify entry stacks for nested exception filters](https://github.com/dotnet/runtime/pull/134749)
- [Disable Runtime_133581 on Mono (#135677)](https://github.com/dotnet/runtime/commit/c74f437d417ae87dd3b09158877e9892a636fa62) - `2026-10-13T17:41:57Z` - Jan Kotas (@jkotas) - PR: [Disable Runtime_133581 on Mono](https://github.com/dotnet/runtime/pull/135677)
- [Fix QuicStream send buffer leak (#135591)](https://github.com/dotnet/runtime/commit/cba3c1d6e77baeb1dc6f8b25f2775ac4b606cce4) - `2026-10-13T17:30:26Z` - Muhammad Asad Majeed (@asad24-dev) - PR: [Fix QuicStream send buffer leak](https://github.com/dotnet/runtime/pull/135591)

### MicrosoftDocs/fabric-docs (28 commit(s), signal 100)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #3419 from MicrosoftDocs/main639275080849887820syn…](https://github.com/MicrosoftDocs/fabric-docs/commit/0da677d09dacedbc8f30b15510b15abb503aa367) - `2026-10-13T17:08:23Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3419)
- [Merging changes synced from https://github.com/MicrosoftDocs/fabric-d…](https://github.com/MicrosoftDocs/fabric-docs/commit/e5235f1c1b8821ff3588daa59d01a4832d9add91) - `2026-10-13T17:08:02Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3419)
- [Merge pull request #16936 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/fabric-docs/commit/2b5f387eefbba3e2e5cc5822aa46bf12b2d972f9) - `2026-10-13T17:05:03Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3419)
- [Merge pull request #16934 from eranbenayun1/eranbenayun/gen1-migratio…](https://github.com/MicrosoftDocs/fabric-docs/commit/5d53f7d8c439279cbdd2eddda02299c226675844) - `2026-10-13T16:01:35Z` - prmerger-automator[bot] (@prmerger-automator[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3419)
- [Apply batched suggestions from code review](https://github.com/MicrosoftDocs/fabric-docs/commit/130a780820daa2475210172a7feb4b9e4a6c3d66) - `2026-10-13T15:57:08Z` - eranbenayun1 (@eranbenayun1) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3419)

### Azure/azure-sdk-for-net (26 commit(s), signal 150)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [Azure.ResourceManager.Compute.BulkActions_1.2.0-beta.4](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.Compute.BulkActions_1.2.0-beta.4) - `2026-10-13T15:37:47Z`
- Release: [Azure.ResourceManager.Compute_1.18.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.Compute_1.18.0) - `2026-10-13T10:40:48Z`
- Release: [Azure.ResourceManager.ResilienceManagement_1.0.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.ResilienceManagement_1.0.0) - `2026-10-13T10:40:24Z`
- Release: [Azure.ResourceManager.PlatformValidation_1.0.0-beta.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.PlatformValidation_1.0.0-beta.1) - `2026-10-13T08:32:38Z`
- Release: [Microsoft.Azure.WebPubSub.AspNetCore_1.6.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Microsoft.Azure.WebPubSub.AspNetCore_1.6.0) - `2026-10-13T06:17:53Z`
- [Update UnbrandedGeneratorVersion to 1.0.0-alpha.20261013.2 (#63807)](https://github.com/Azure/azure-sdk-for-net/commit/4bcff5ffc3478e0252d0cce92bdf082b4cef7ec1) - `2026-10-13T19:41:38Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Update UnbrandedGeneratorVersion to 1.0.0-alpha.20261013.2](https://github.com/Azure/azure-sdk-for-net/pull/63807)
- [Increment package version after release of Azure.ResourceManager.Comp…](https://github.com/Azure/azure-sdk-for-net/commit/79097a5d25e8a3493cf0b7d37601c20e4224cb90) - `2026-10-13T19:37:51Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment version for compute releases](https://github.com/Azure/azure-sdk-for-net/pull/63800)
- [docs: update Service Bus migration guides after SDK retirement (#63629)](https://github.com/Azure/azure-sdk-for-net/commit/16c8f7dfec99c75d1b784d74dd1eda35d501ccc7) - `2026-10-13T18:48:58Z` - Eldert Grootenboer (@EldertGrootenboer) - PR: [docs: update Service Bus migration guides after SDK retirement](https://github.com/Azure/azure-sdk-for-net/pull/63629)
- [Increment package version after release of Azure.ResourceManager.Plat…](https://github.com/Azure/azure-sdk-for-net/commit/f8afd5b31d94017aa9b4ce6fb322b87349e012f8) - `2026-10-13T15:42:03Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment version for platformvalidation releases](https://github.com/Azure/azure-sdk-for-net/pull/63793)
- [Increment package version after release of Azure.ResourceManager.Resi…](https://github.com/Azure/azure-sdk-for-net/commit/38108b4714ffdb42f7bbe60e0edc0a5300340c31) - `2026-10-13T15:39:54Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment version for azureresiliencemanagement releases](https://github.com/Azure/azure-sdk-for-net/pull/63795)

### dotnet/docs (20 commit(s), signal 60)

Tags: `docs, human-authored`

- [use workflow instead of policy to merge dependabot prs (#56349)](https://github.com/dotnet/docs/commit/ca59700e5e58f09e0b21868ba2e983b1162b4cdd) - `2026-10-13T19:14:48Z` - Genevieve Warren (@gewarren) - PR: [Use workflow instead of policy to merge Dependabot PRs](https://github.com/dotnet/docs/pull/56349)
- [Clarify browser WebAssembly random number generation (#56360)](https://github.com/dotnet/docs/commit/c49a5b9586cb3bf0911717929620368a80d6f38f) - `2026-10-13T19:13:35Z` - Krzysztof Wicher (@krwq) - PR: [Clarify browser WebAssembly random number generation](https://github.com/dotnet/docs/pull/56360)
- [Add safety warnings to stackalloc examples (#56358)](https://github.com/dotnet/docs/commit/b028664e7011212d00dec837b7b4eab3c950b857) - `2026-10-13T19:11:25Z` - Levi Broderick (@GrabYourPitchforks) - PR: [Add safety warnings to stackalloc examples](https://github.com/dotnet/docs/pull/56358)
- [Tara o 26 10 b (#56355)](https://github.com/dotnet/docs/commit/85d59dcb6b5af1dce6e860b5d927cf6e178a056b) - `2026-10-13T17:09:51Z` - Tara Overfield (@TaraOverfield) - PR: [Tara o 26 10 b](https://github.com/dotnet/docs/pull/56355)
- [Bump Azure.Storage.Blobs across 2 directories (#56382)](https://github.com/dotnet/docs/commit/3ad903a790ef39f8b58ca5fc59f5228454fc6e50) - `2026-10-13T11:13:40Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Azure.Storage.Blobs across 2 directories](https://github.com/dotnet/docs/pull/56382)

### Azure-Samples/Durable-Task-Scheduler (16 commit(s), signal 31)

Tags: `bot-only, dependency-noise, product:Azure AI, product:Azure SDK, samples, watchlist`

- [Bump the npm_and_yarn group across 4 directories with 2 updates (#406)](https://github.com/Azure-Samples/Durable-Task-Scheduler/commit/27ea6a443ef99e9ca8de963d577fee0abad3f0b7) - `2026-10-13T02:01:13Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the npm_and_yarn group across 4 directories with 2 updates](https://github.com/Azure-Samples/Durable-Task-Scheduler/pull/406)
- [Update openai requirement (#402)](https://github.com/Azure-Samples/Durable-Task-Scheduler/commit/0b8ea16828bc4d4fa47f6302aca2fed68efda80a) - `2026-10-13T02:01:04Z` - dependabot[bot] (@dependabot[bot]) - PR: [Update openai requirement from >=3.20.0 to >=3.28.0 in /samples/durable-task-sdks/python/agent-directed-workflows](https://github.com/Azure-Samples/Durable-Task-Scheduler/pull/402)
- [Bump source-map-js (#405)](https://github.com/Azure-Samples/Durable-Task-Scheduler/commit/60aa19d55ec7ab50709704f7599ce47d533753f3) - `2026-10-13T01:55:54Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump source-map-js from 1.2.1 to 1.2.2 in /samples/durable-functions/dotnet/AiAgentTravelPlanOrchestrator/Frontend](https://github.com/Azure-Samples/Durable-Task-Scheduler/pull/405)
- [Update openai requirement (#396)](https://github.com/Azure-Samples/Durable-Task-Scheduler/commit/cac2dbd85c3d9de1dd1ca88484884af34ce75e4d) - `2026-10-13T01:55:48Z` - dependabot[bot] (@dependabot[bot]) - PR: [Update openai requirement from >=3.20.0 to >=3.28.0 in /samples/durable-functions/python/agent-directed-workflows](https://github.com/Azure-Samples/Durable-Task-Scheduler/pull/396)
- [Update redis requirement in /samples/durable-task-sdks/python (#399)](https://github.com/Azure-Samples/Durable-Task-Scheduler/commit/9e49f5f418ed18b87435e4a2b93c85250ee25bc3) - `2026-10-13T01:55:41Z` - dependabot[bot] (@dependabot[bot]) - PR: [Update redis requirement from >=8.0.1 to >=8.1.0 in /samples/durable-task-sdks/python](https://github.com/Azure-Samples/Durable-Task-Scheduler/pull/399)

### Azure/azure-dev (15 commit(s), signal 90)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [fix(extensions): recover interrupted extension upgrades (#10315)](https://github.com/Azure/azure-dev/commit/2f9ac040e92b810d9c8d25cde08fb50e52fc234f) - `2026-10-13T18:42:05Z` - Mohamed Hessien (@m7md7sien) - PR: [fix(extensions): recover interrupted extension upgrades](https://github.com/Azure/azure-dev/pull/10315)
- [fix(ai eval): reconcile evaluation runtime and authoring contracts (#…](https://github.com/Azure/azure-dev/commit/e51b7a777887eb2b1c7190ed8cfd9f95baa9e2a0) - `2026-10-13T18:40:40Z` - Mohamed Hessien (@m7md7sien) - PR: [fix(ai eval): reconcile evaluation runtime and authoring contracts](https://github.com/Azure/azure-dev/pull/10311)
- [fix(foundry): grant developer access during agent predeploy (#10395)](https://github.com/Azure/azure-dev/commit/1d8f52c88c774456a07d29e849a30ddab3ac7940) - `2026-10-13T18:06:15Z` - Zhijie Huang (@hund030) - PR: [fix(foundry): grant developer access during agent predeploy](https://github.com/Azure/azure-dev/pull/10395)
- [feat: plan agent dependencies from definition files (#10410)](https://github.com/Azure/azure-dev/commit/2141977bdbe543a266048788a04e92578b48281c) - `2026-10-13T17:34:29Z` - Hui Miao (@huimiu) - PR: [feat: plan agent dependencies from definition files](https://github.com/Azure/azure-dev/pull/10410)
- [Use stable API contract for Voice Agent reads (#10441)](https://github.com/Azure/azure-dev/commit/11b93efa872db6aac44294e5cdd11bbf5032239d) - `2026-10-13T17:33:34Z` - JianW (@v1212) - PR: [Use stable API contract for Voice Agent reads](https://github.com/Azure/azure-dev/pull/10441)

### MicrosoftDocs/azure-compute-docs (15 commit(s), signal 90)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-co…](https://github.com/MicrosoftDocs/azure-compute-docs/commit/38164b4abefebfaac6966d71eec8c36c781b7bf9) - `2026-10-13T17:04:57Z` - Learn Build Service GitHub App
- [Merge pull request #4222 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-compute-docs/commit/e83244d24f968c3abfd017f368e8cc35e9fe4bb3) - `2026-10-13T17:04:00Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #4185 from elieliteli/pv2-migration-status-docs](https://github.com/MicrosoftDocs/azure-compute-docs/commit/15dedf4b00943873d9b2e50b1dca175405bf0008) - `2026-10-13T15:05:57Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #4221 from sandeepraichura/soft-delete-location-li…](https://github.com/MicrosoftDocs/azure-compute-docs/commit/a00dbde6bf02031efa36caf72676349c0c597590) - `2026-10-13T15:03:35Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Clarify Soft Delete billing duration](https://github.com/MicrosoftDocs/azure-compute-docs/commit/1986cfb55f7e81798a7e6f2d244e2046e7388e69) - `2026-10-13T07:34:13Z` - Sandeep Raichura (@sandeepraichura)

### Azure-Samples/modernize-bootcamp (14 commit(s), signal 54)

Tags: `human-authored, samples`

- [Merge pull request #51 from Azure-Samples/sojorgensen/rewordinglabs](https://github.com/Azure-Samples/modernize-bootcamp/commit/0f30d79d11dfda8385c449d1fbfbc01dcf5b6fcd) - `2026-10-13T19:47:44Z` - Sophie Jorgensen (@sophiejorgensen) - PR: [Update modernization bootcamp lab guidance](https://github.com/Azure-Samples/modernize-bootcamp/pull/51)
- [Update modernization bootcamp lab guidance](https://github.com/Azure-Samples/modernize-bootcamp/commit/8a33c2e487a5460c2c37868b826e0e77967cc492) - `2026-10-13T19:38:07Z` - Sophie Jorgensen - PR: [Update modernization bootcamp lab guidance](https://github.com/Azure-Samples/modernize-bootcamp/pull/51)
- [Merge pull request #50 from Azure-Samples/sumit/modify-day2-data](https://github.com/Azure-Samples/modernize-bootcamp/commit/f08419d1ad077a374ebd0e9cfe2bda6524350472) - `2026-10-13T18:27:47Z` - Sumit Sengupta (@sumitsengupta) - PR: [minor clarifications on challenge 1](https://github.com/Azure-Samples/modernize-bootcamp/pull/50)
- [minor clarifications on challenge 1](https://github.com/Azure-Samples/modernize-bootcamp/commit/1a36d5f10a3f6d7018db2af3c9b7577d351908f3) - `2026-10-13T18:26:01Z` - sumitdatabase (@sumitdatabase) - PR: [minor clarifications on challenge 1](https://github.com/Azure-Samples/modernize-bootcamp/pull/50)
- [Merge pull request #49 from Azure-Samples/sojorgensen/rewordinglabs](https://github.com/Azure-Samples/modernize-bootcamp/commit/afdddd474f730623d1e4bf599ddc8293bc43e36b) - `2026-10-13T01:48:23Z` - Sophie Jorgensen (@sophiejorgensen) - PR: [Refine pacing explanation, git prompt note, and app run options](https://github.com/Azure-Samples/modernize-bootcamp/pull/49)

### microsoft/kiota-samples (14 commit(s), signal 99)

Tags: `docs, human-authored, product:Microsoft Graph, release-language, watchlist`

- [Merge pull request #9148 from microsoft/dependabot/pip/get-started/az…](https://github.com/microsoft/kiota-samples/commit/f47a9ce77f1eb5c29db9a1f3052a72d8fc1bff23) - `2026-10-13T19:03:58Z` - Vincent Biret (@baywet) - PR: [build(deps): bump cryptography from 48.0.1 to 50.0.0 in /get-started/azure-auth/python](https://github.com/microsoft/kiota-samples/pull/9148)
- [Merge pull request #9149 from microsoft/dependabot/go_modules/msgraph…](https://github.com/microsoft/kiota-samples/commit/a6ccec06adf3ab33471b6ac630c9d2d54ca8033b) - `2026-10-13T19:03:51Z` - Vincent Biret (@baywet) - PR: [build(deps): bump github.com/microsoft/kiota-http-go from 1.5.6 to 1.5.7 in /msgraph-mail/go in the kiota-dependencies group](https://github.com/microsoft/kiota-samples/pull/9149)
- [Merge pull request #9150 from microsoft/dependabot/npm_and_yarn/msgra…](https://github.com/microsoft/kiota-samples/commit/5d428b794f7697f8049b8a606f61337c3e26dfcc) - `2026-10-13T19:03:44Z` - Vincent Biret (@baywet) - PR: [build(deps): bump the kiota-dependencies group in /msgraph-mail/typescript with 2 updates](https://github.com/microsoft/kiota-samples/pull/9150)
- [Merge pull request #9151 from microsoft/dependabot/go_modules/petstor…](https://github.com/microsoft/kiota-samples/commit/2aa94fa4eafb115412cf2a9818095404cfe54bb3) - `2026-10-13T19:03:37Z` - Vincent Biret (@baywet) - PR: [build(deps): bump github.com/microsoft/kiota-http-go from 1.5.6 to 1.5.7 in /petstore/go in the kiota-dependencies group](https://github.com/microsoft/kiota-samples/pull/9151)
- [Merge pull request #9152 from microsoft/dependabot/npm_and_yarn/get-s…](https://github.com/microsoft/kiota-samples/commit/73fab31076957dd41627f221d75071e973050b78) - `2026-10-13T19:03:19Z` - Vincent Biret (@baywet) - PR: [build(deps): bump @microsoft/kiota-bundle from 1.0.0-preview.108 to 1.0.0-preview.110 in /get-started/quickstart/typescript in the kiota-dependencies group](https://github.com/microsoft/kiota-samples/pull/9152)

### Azure-Samples/app-service-builder-vite (14 commit(s), signal 124)

Tags: `human-authored, release-language, samples, security, watchlist`

- [Merge pull request #2 from seligj95/seligj95-vite-sample-defaults](https://github.com/Azure-Samples/app-service-builder-vite/commit/fe55edd99fb558ca490f8aaff70ba5bf2eaaaa98) - `2026-10-13T12:58:43Z` - Jordan Selig (@seligj95) - PR: [Simplify the Vite sample's single-component root path](https://github.com/Azure-Samples/app-service-builder-vite/pull/2)
- [Use the implicit root path for the Vite sample](https://github.com/Azure-Samples/app-service-builder-vite/commit/2cdf737518ddd4f6d6d08ca187e2bedcdbb5a941) - `2026-10-12T21:54:24Z` - Jordan Selig (@seligj95) - PR: [Simplify the Vite sample's single-component root path](https://github.com/Azure-Samples/app-service-builder-vite/pull/2)
- [Merge pull request #1 from seligj95/seligj95-vite-sample-migration](https://github.com/Azure-Samples/app-service-builder-vite/commit/77eb01f5aeeaf91b78283026249e195594c09818) - `2026-10-12T20:52:13Z` - Jordan Selig (@seligj95) - PR: [Add standalone Vite TypeScript static sample](https://github.com/Azure-Samples/app-service-builder-vite/pull/1)
- [Handle colored Vite preview output in CI smoke test](https://github.com/Azure-Samples/app-service-builder-vite/commit/a7b626d5ee53097007f8ad5a971c3ef67e98e6b6) - `2026-10-12T20:48:36Z` - Jordan Selig (@seligj95) - PR: [Add standalone Vite TypeScript static sample](https://github.com/Azure-Samples/app-service-builder-vite/pull/1)
- [Patch vulnerable source-map-js build dependency](https://github.com/Azure-Samples/app-service-builder-vite/commit/5aa97ca0e9c7a2c65da3b7106667909e79321428) - `2026-10-12T20:44:11Z` - Jordan Selig (@seligj95) - PR: [Add standalone Vite TypeScript static sample](https://github.com/Azure-Samples/app-service-builder-vite/pull/1)

### Azure-Samples/app-service-builder-static-html (13 commit(s), signal 53)

Tags: `human-authored, samples`

- [Merge pull request #2 from seligj95/seligj95-static-manifest-defaults](https://github.com/Azure-Samples/app-service-builder-static-html/commit/37efdfc6b22f6f58729e4ed6dedc79e3ba88b2fb) - `2026-10-13T12:58:26Z` - Jordan Selig (@seligj95) - PR: [Simplify static Builder manifest root default](https://github.com/Azure-Samples/app-service-builder-static-html/pull/2)
- [Clarify default public URL mount terminology](https://github.com/Azure-Samples/app-service-builder-static-html/commit/4aca038a2e4365faac5d4157bcdc82ee163a4c18) - `2026-10-12T21:55:13Z` - Jordan Selig (@seligj95) - PR: [Simplify static Builder manifest root default](https://github.com/Azure-Samples/app-service-builder-static-html/pull/2)
- [Simplify static Builder manifest root default](https://github.com/Azure-Samples/app-service-builder-static-html/commit/a5bf22d9e28986604b20bd8a39c7ee62bae248aa) - `2026-10-12T21:53:21Z` - Jordan Selig (@seligj95) - PR: [Simplify static Builder manifest root default](https://github.com/Azure-Samples/app-service-builder-static-html/pull/2)
- [Merge pull request #1 from seligj95/seligj95-static-html-sample-migra…](https://github.com/Azure-Samples/app-service-builder-static-html/commit/ad1f8c78d933117a41c4d26dfabaa99a44bdcd39) - `2026-10-12T20:45:46Z` - Jordan Selig (@seligj95) - PR: [Add standalone static HTML App Service Builder sample](https://github.com/Azure-Samples/app-service-builder-static-html/pull/1)
- [Add standalone static HTML Builder sample](https://github.com/Azure-Samples/app-service-builder-static-html/commit/6a0839530d4aa18a4fa0c694e11589a526d24133) - `2026-10-12T20:39:44Z` - Jordan Selig (@seligj95) - PR: [Add standalone static HTML App Service Builder sample](https://github.com/Azure-Samples/app-service-builder-static-html/pull/1)

### Azure/azure-sdk-for-java (12 commit(s), signal 137)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [com.azure.resourcemanager+azure-resourcemanager-dataprotection_1.7.0-beta.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-dataprotection_1.7.0-beta.1) - `2026-10-13T03:15:19Z`
- Release: [com.azure.resourcemanager+azure-resourcemanager-weightsandbiases_1.0.1](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-weightsandbiases_1.0.1) - `2026-10-13T03:14:03Z`
- Release: [com.azure+azure-sdk-bom_1.3.9](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure%2Bazure-sdk-bom_1.3.9) - `2026-10-12T22:30:25Z`
- Release: [com.azure.resourcemanager+azure-resourcemanager-commvaultcontentstore_1.0.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-commvaultcontentstore_1.0.0) - `2026-10-12T20:30:21Z`
- [Configurations:  'specification/cloudhealth/resource-manager/Microsof…](https://github.com/Azure/azure-sdk-for-java/commit/19d7d147dd301db2ed584fd73bf6dfea71a73c3c) - `2026-10-13T19:46:59Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-resourcemanager-cloudhealth]-generated-from-SDK Generation - Java-6884314](https://github.com/Azure/azure-sdk-for-java/pull/50584)
- [[AutoPR azure-resourcemanager-storagecache]-generated-from-SDK Genera…](https://github.com/Azure/azure-sdk-for-java/commit/be253fe7bdbb527d88b8a6e898683b6bbd4e8eaa) - `2026-10-13T14:11:59Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-resourcemanager-storagecache]-generated-from-SDK Generation - Java-6777361](https://github.com/Azure/azure-sdk-for-java/pull/50166)
- [[skip ci] Increment versions for appcontainers releases (#50770)](https://github.com/Azure/azure-sdk-for-java/commit/9142530c1c9d62e3d9d604dfe286ff13c95d9eb3) - `2026-10-13T08:06:13Z` - Weidong Xu (@weidongxu-microsoft) - PR: [[skip ci] Increment versions for appcontainers releases](https://github.com/Azure/azure-sdk-for-java/pull/50770)
- [Relax Network API version regression test (#50771)](https://github.com/Azure/azure-sdk-for-java/commit/cd2e42b5f35add7d9e644471381d6a8a718484dc) - `2026-10-13T07:29:05Z` - Weidong Xu (@weidongxu-microsoft) - PR: [Relax Network API version regression test](https://github.com/Azure/azure-sdk-for-java/pull/50771)
- [Include implementation sources in TypeSpec regeneration checks (#50772)](https://github.com/Azure/azure-sdk-for-java/commit/596ca4a6cc0ab93c76919e5ba7a3a6ddc841a9d8) - `2026-10-13T07:22:59Z` - Weidong Xu (@weidongxu-microsoft) - PR: [Include implementation sources in TypeSpec regeneration checks](https://github.com/Azure/azure-sdk-for-java/pull/50772)

### MicrosoftDocs/architecture-center (12 commit(s), signal 87)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #16940 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/architecture-center/commit/067102457bce26ae9f4b6866ff782ef45629abd6) - `2026-10-13T17:32:24Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Modernize Busy Front End Service Bus samples (#16939)](https://github.com/MicrosoftDocs/architecture-center/commit/60e4fa7c56abfc2dd9d33c645a47ab1eec7c6019) - `2026-10-13T16:55:31Z` - Copilot (@Copilot)
- [Initial workflow (#16932)](https://github.com/MicrosoftDocs/architecture-center/commit/c779853cd43ad5f85909d6fa1ed2c8b0f8ae5b49) - `2026-10-13T15:44:00Z` - Chad Kittel (@ckittel)
- [PnP edit: Choose a Kubernetes at the edge compute option (#16923)](https://github.com/MicrosoftDocs/architecture-center/commit/475053c7034e1b0c5ad669e780a83fbd209b693f) - `2026-10-13T15:35:45Z` - Mick Alberts (@v-albemi)
- [Merge pull request #16935 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/architecture-center/commit/b5625a64d8cd80ab584b86dfcf9fd6423a9eef82) - `2026-10-13T15:22:10Z` - Chad Kittel (@ckittel)

### Azure-Samples/app-service-builder-dotnet (12 commit(s), signal 87)

Tags: `human-authored, samples, watchlist`

- [Merge pull request #2 from seligj95/seligj95-dotnet-sample-yaml-defaults](https://github.com/Azure-Samples/app-service-builder-dotnet/commit/f2dddd107acff2e915a157f62a50b4e5ec96fd0a) - `2026-10-13T14:24:11Z` - Jordan Selig (@seligj95) - PR: [Simplify .NET sample builder.yaml defaults](https://github.com/Azure-Samples/app-service-builder-dotnet/pull/2)
- [Simplify single-component builder manifest defaults](https://github.com/Azure-Samples/app-service-builder-dotnet/commit/a8732f9710e99f19e865cb9fa14deec59f2f8bbf) - `2026-10-12T21:53:25Z` - Jordan Selig (@seligj95) - PR: [Simplify .NET sample builder.yaml defaults](https://github.com/Azure-Samples/app-service-builder-dotnet/pull/2)
- [Merge pull request #1 from seligj95/seligj95-aspnet-sample-migration](https://github.com/Azure-Samples/app-service-builder-dotnet/commit/efaac7525151ef40f7cffc5e6a640575a1252ed2) - `2026-10-12T20:47:50Z` - Jordan Selig (@seligj95) - PR: [Add standalone ASP.NET App Service Builder sample](https://github.com/Azure-Samples/app-service-builder-dotnet/pull/1)
- [Add standalone ASP.NET App Service Builder sample](https://github.com/Azure-Samples/app-service-builder-dotnet/commit/3661d8b00f0458f5dd4951f62b2faf7d0fbe89c8) - `2026-10-12T20:42:02Z` - Jordan Selig (@seligj95) - PR: [Add standalone ASP.NET App Service Builder sample](https://github.com/Azure-Samples/app-service-builder-dotnet/pull/1)
- [.github/PULL_REQUEST_TEMPLATE.md committed](https://github.com/Azure-Samples/app-service-builder-dotnet/commit/854c75906548bc4dfb305c2dd4c76cdafb3855f9) - `2026-10-12T20:25:46Z` - microsoft-github-operations[bot] (@microsoft-github-operations[bot])

### Azure-Samples/app-service-builder-nodejs (12 commit(s), signal 87)

Tags: `human-authored, samples, watchlist`

- [Merge pull request #2 from seligj95/seligj95-node-sample-yaml-defaults](https://github.com/Azure-Samples/app-service-builder-nodejs/commit/ac1fafc6a0f32efce9bbf46b056ceddb30b3e195) - `2026-10-13T12:58:41Z` - Jordan Selig (@seligj95) - PR: [Simplify Node.js sample Builder defaults](https://github.com/Azure-Samples/app-service-builder-nodejs/pull/2)
- [Simplify Node.js sample Builder defaults](https://github.com/Azure-Samples/app-service-builder-nodejs/commit/2f42df470f8f739af51668e5c653a63999296b14) - `2026-10-12T21:54:13Z` - Jordan Selig (@seligj95) - PR: [Simplify Node.js sample Builder defaults](https://github.com/Azure-Samples/app-service-builder-nodejs/pull/2)
- [Merge pull request #1 from seligj95/seligj95-nodejs-sample-migration](https://github.com/Azure-Samples/app-service-builder-nodejs/commit/5f83eb732f92778b663db6eb4e0ba3f1418071a2) - `2026-10-12T20:51:09Z` - Jordan Selig (@seligj95) - PR: [Add standalone Node.js App Service Builder sample](https://github.com/Azure-Samples/app-service-builder-nodejs/pull/1)
- [Add standalone Node.js App Service Builder sample](https://github.com/Azure-Samples/app-service-builder-nodejs/commit/af7d6bb6de110b9818ad80d3aadc6927e69dd4b6) - `2026-10-12T20:41:47Z` - Jordan Selig (@seligj95) - PR: [Add standalone Node.js App Service Builder sample](https://github.com/Azure-Samples/app-service-builder-nodejs/pull/1)
- [.github/PULL_REQUEST_TEMPLATE.md committed](https://github.com/Azure-Samples/app-service-builder-nodejs/commit/5486ed46a5b7de1e3b32b48f51724912f9bdcd56) - `2026-10-12T20:23:08Z` - microsoft-github-operations[bot] (@microsoft-github-operations[bot])

### Azure-Samples/app-service-builder-python (12 commit(s), signal 87)

Tags: `human-authored, samples, watchlist`

- [Merge pull request #2 from seligj95/seligj95-python-sample-yaml-defaults](https://github.com/Azure-Samples/app-service-builder-python/commit/cd22831c5da84e24e17edfe7b84b061a32ed0603) - `2026-10-13T12:58:38Z` - Jordan Selig (@seligj95) - PR: [Simplify Python sample builder defaults](https://github.com/Azure-Samples/app-service-builder-python/pull/2)
- [Simplify Python sample builder defaults](https://github.com/Azure-Samples/app-service-builder-python/commit/3fed0345d05a76f6ad3205ef3e558655fcf819d9) - `2026-10-12T21:53:53Z` - Jordan Selig (@seligj95) - PR: [Simplify Python sample builder defaults](https://github.com/Azure-Samples/app-service-builder-python/pull/2)
- [Merge pull request #1 from seligj95/seligj95-python-sample-migration](https://github.com/Azure-Samples/app-service-builder-python/commit/b14cd5aa2ae3b27e45f90019da6d0e375aab2d1c) - `2026-10-12T20:50:10Z` - Jordan Selig (@seligj95) - PR: [Add standalone Python sample for App Service Builder](https://github.com/Azure-Samples/app-service-builder-python/pull/1)
- [Populate standalone App Service Builder Python sample](https://github.com/Azure-Samples/app-service-builder-python/commit/2e1b97a83a539de02dc8b89238ef7ab2875b6b43) - `2026-10-12T20:42:40Z` - Jordan Selig (@seligj95) - PR: [Add standalone Python sample for App Service Builder](https://github.com/Azure-Samples/app-service-builder-python/pull/1)
- [.github/PULL_REQUEST_TEMPLATE.md committed](https://github.com/Azure-Samples/app-service-builder-python/commit/430edf92a6c72b1fd741dc0697ec5c2d0cad3907) - `2026-10-12T20:24:25Z` - microsoft-github-operations[bot] (@microsoft-github-operations[bot])

### Azure-Samples/app-service-builder-mcp-server (12 commit(s), signal 87)

Tags: `human-authored, samples, watchlist`

- [Merge pull request #2 from seligj95/seligj95-mcp-sample-yaml-defaults](https://github.com/Azure-Samples/app-service-builder-mcp-server/commit/a6ab9b2b91049525870dac5522a94b8a82229691) - `2026-10-13T12:58:34Z` - Jordan Selig (@seligj95) - PR: [Simplify redundant MCP sample builder.yaml defaults](https://github.com/Azure-Samples/app-service-builder-mcp-server/pull/2)
- [Simplify redundant MCP sample builder defaults](https://github.com/Azure-Samples/app-service-builder-mcp-server/commit/a641e3ce2c10c2ad39bc3989d8c2b98886360b2b) - `2026-10-12T21:53:29Z` - Jordan Selig (@seligj95) - PR: [Simplify redundant MCP sample builder.yaml defaults](https://github.com/Azure-Samples/app-service-builder-mcp-server/pull/2)
- [Merge pull request #1 from seligj95/seligj95-mcp-sample-migration](https://github.com/Azure-Samples/app-service-builder-mcp-server/commit/139ae7aa722f3384933c510b701934265be1b318) - `2026-10-12T20:48:32Z` - Jordan Selig (@seligj95) - PR: [Add standalone App Service Builder HTTP MCP sample](https://github.com/Azure-Samples/app-service-builder-mcp-server/pull/1)
- [Add standalone App Service Builder HTTP MCP sample](https://github.com/Azure-Samples/app-service-builder-mcp-server/commit/1e9c991e5dd91689df72b741d93eaa72d25f68ec) - `2026-10-12T20:43:22Z` - Jordan Selig (@seligj95) - PR: [Add standalone App Service Builder HTTP MCP sample](https://github.com/Azure-Samples/app-service-builder-mcp-server/pull/1)
- [.github/ISSUE_TEMPLATE.md committed](https://github.com/Azure-Samples/app-service-builder-mcp-server/commit/0acc111cfcf79393025b630606a8a5ceaaa2aafb) - `2026-10-12T20:28:08Z` - microsoft-github-operations[bot] (@microsoft-github-operations[bot])

### Azure-Samples/app-service-builder-ai-agent (12 commit(s), signal 87)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Merge pull request #2 from seligj95/seligj95-ai-sample-yaml-defaults](https://github.com/Azure-Samples/app-service-builder-ai-agent/commit/1c24a5e371deea3703d63244a4f46d21bd360f2d) - `2026-10-13T12:58:30Z` - Jordan Selig (@seligj95) - PR: [Simplify AI sample Builder YAML defaults](https://github.com/Azure-Samples/app-service-builder-ai-agent/pull/2)
- [Simplify AI sample Builder YAML defaults](https://github.com/Azure-Samples/app-service-builder-ai-agent/commit/e079d9efe5c1c8ad201a7db2427443a2982571fd) - `2026-10-12T21:53:21Z` - Jordan Selig (@seligj95) - PR: [Simplify AI sample Builder YAML defaults](https://github.com/Azure-Samples/app-service-builder-ai-agent/pull/2)
- [Merge pull request #1 from seligj95/seligj95-ai-assistant-sample-migr…](https://github.com/Azure-Samples/app-service-builder-ai-agent/commit/6d8f7db97ab8242061bd4d54b3008ebe6b112bf7) - `2026-10-12T20:49:29Z` - Jordan Selig (@seligj95) - PR: [Add standalone AI assistant HTTP API sample](https://github.com/Azure-Samples/app-service-builder-ai-agent/pull/1)
- [Populate standalone AI assistant HTTP sample](https://github.com/Azure-Samples/app-service-builder-ai-agent/commit/19142ec45c4c16f7fa86ea64de5cf4947d3918ad) - `2026-10-12T20:42:32Z` - Jordan Selig (@seligj95) - PR: [Add standalone AI assistant HTTP API sample](https://github.com/Azure-Samples/app-service-builder-ai-agent/pull/1)
- [.github/PULL_REQUEST_TEMPLATE.md committed](https://github.com/Azure-Samples/app-service-builder-ai-agent/commit/15e513389f400d75d9f582852319ad7c601a57f5) - `2026-10-12T20:29:23Z` - microsoft-github-operations[bot] (@microsoft-github-operations[bot])

### MicrosoftDocs/power-platform (11 commit(s), signal 86)

Tags: `docs, human-authored, product:Microsoft Graph, product:PowerShell, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/19f1c024e35badc1ffa6f78936fde596c91e32dd) - `2026-10-13T19:05:19Z` - Learn Build Service GitHub App
- [Merge pull request #12029 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-platform/commit/edc3325c76ae9240ae1e087bf7c6828ee33b06bf) - `2026-10-13T19:04:08Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update geographical-availability-copilot.md (#12028)](https://github.com/MicrosoftDocs/power-platform/commit/e601fd6673c7d13351dcb1559362ac15b39f808b) - `2026-10-13T17:08:52Z` - Alex Ferguson (@alfergus)
- [Document Dataverse.Unmask in the Power Fx reference (#12016)](https://github.com/MicrosoftDocs/power-platform/commit/37c4680786adc343f5c67ea858b14751aff7af9c) - `2026-10-13T16:58:31Z` - Yogesh Gupta (@yogeshgupta698)
- [Updating maintenance settings documentation to remove older screensho…](https://github.com/MicrosoftDocs/power-platform/commit/e96df50e89d66d4ac14ba0f9039c3454e52e9c08) - `2026-10-13T14:42:20Z` - Aarsh Sharma (@aarsh-msft)

### MicrosoftDocs/SupportArticles-docs (11 commit(s), signal 86)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/513c719e1f56ecc2c2191395c8d8a875f78b00c2) - `2026-10-13T18:06:23Z` - Learn Build Service GitHub App
- [Merge pull request #12587 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/083a6aeef25ccf2c051ef280e8b5cfd6b1374f7b) - `2026-10-13T18:04:41Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/a4e2d9f214f012a0cf422dca9178df18ab4735e6) - `2026-10-13T17:42:43Z` - Learn Build Service GitHub App
- [Out-Of-Band publish (#12585)](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/b78e8be434a0ed4ffb14c14f57cd4c02503878c7) - `2026-10-13T17:40:35Z` - Teresa Appelgate (@v-tappelgate)
- [[OOB publish 10/13 @ 10:00 AM PT] New QMR Group Policy (#12575)](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/77df18d040bc234f6e9e6522073b76bbf88eb0d7) - `2026-10-13T17:24:42Z` - Valentyna Filimonova (@v-fvalentyna)

### Azure-Samples/app-service-builder-php (11 commit(s), signal 51)

Tags: `human-authored, samples`

- [Merge pull request #1 from seligj95/seligj95-standalone-php-sample](https://github.com/Azure-Samples/app-service-builder-php/commit/b3e796d51be0576db14247cbf2efa2dc182da4e1) - `2026-10-13T15:24:00Z` - Jordan Selig (@seligj95) - PR: [Add standalone PHP 8.5 App Service Builder sample](https://github.com/Azure-Samples/app-service-builder-php/pull/1)
- [Keep endpoint checks compatible with Composer-generated metadata](https://github.com/Azure-Samples/app-service-builder-php/commit/8597958915fee0babaf2caf21ea4779ec22a88e1) - `2026-10-13T13:25:15Z` - Jordan Selig (@seligj95) - PR: [Add standalone PHP 8.5 App Service Builder sample](https://github.com/Azure-Samples/app-service-builder-php/pull/1)
- [Add standalone PHP 8.5 App Service Builder sample](https://github.com/Azure-Samples/app-service-builder-php/commit/c7469bc89ba11a974379dde1ec1a1bb5ee8a3942) - `2026-10-13T13:22:51Z` - Jordan Selig (@seligj95) - PR: [Add standalone PHP 8.5 App Service Builder sample](https://github.com/Azure-Samples/app-service-builder-php/pull/1)
- [.github/ISSUE_TEMPLATE.md committed](https://github.com/Azure-Samples/app-service-builder-php/commit/a9b8d53598ea0471754483e66acc375b15dd2e9a) - `2026-10-13T13:03:49Z` - microsoft-github-operations[bot] (@microsoft-github-operations[bot])
- [.github/PULL_REQUEST_TEMPLATE.md committed](https://github.com/Azure-Samples/app-service-builder-php/commit/155409ea62eec460f0fca67bc5ff4f78aa54e9f5) - `2026-10-13T13:03:47Z` - microsoft-github-operations[bot] (@microsoft-github-operations[bot])

### MicrosoftDocs/azure-docs-sdk-dotnet (10 commit(s), signal 85)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/6e9e1f5856bab1a916f8ce09a51715cf0168fbd4) - `2026-10-13T15:57:46Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/9bf7025ff897d70dbc76e01599a82f06faf29b0f) - `2026-10-13T10:52:52Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/72150db5a3f031ea44da64b100e174e030ac82e1) - `2026-10-13T10:52:43Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/a768109a215b3f5b74f34bd2fd414d4a700f6e8a) - `2026-10-13T08:49:13Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/822b37f1bea4b27e93bbac6a592ea547f1e6ec9a) - `2026-10-13T06:29:22Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/azure-devops-docs (10 commit(s), signal 85)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-de…](https://github.com/MicrosoftDocs/azure-devops-docs/commit/66e57d7a9d0221359be79ea8806826f93f25ce16) - `2026-10-13T15:05:35Z` - Learn Build Service GitHub App
- [Merge pull request #9805 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-devops-docs/commit/0d8b85c7a73cfaea33a78484b28391038d15832e) - `2026-10-13T15:04:10Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Announce Ubuntu 22.04 hosted image deprecation (#9785)](https://github.com/MicrosoftDocs/azure-devops-docs/commit/3fc18de83c91dbccff78dbc06c3844be8115472d) - `2026-10-13T14:10:52Z` - Shubham Agarwal (@agarshubh)
- [Merging changes synced from https://github.com/MicrosoftDocs/azure-de…](https://github.com/MicrosoftDocs/azure-devops-docs/commit/2fc31eedfc8e9b115898baf7d29cab34a5d8228d) - `2026-10-13T13:05:26Z` - Learn Build Service GitHub App
- [Merge pull request #9804 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-devops-docs/commit/6184763bfc9136c71b524843e8bf5527dd4578e2) - `2026-10-13T13:03:51Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### microsoft/kiota-python (9 commit(s), signal 134)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [microsoft-kiota-serialization-multipart: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-serialization-multipart-v1.14.3) - `2026-10-13T13:47:33Z`
- Release: [microsoft-kiota-serialization-text: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-serialization-text-v1.14.3) - `2026-10-13T13:47:32Z`
- Release: [microsoft-kiota-serialization-form: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-serialization-form-v1.14.3) - `2026-10-13T13:47:31Z`
- Release: [microsoft-kiota-serialization-json: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-serialization-json-v1.14.3) - `2026-10-13T13:47:28Z`
- Release: [microsoft-kiota-http: v1.14.3](https://github.com/microsoft/kiota-python/releases/tag/microsoft-kiota-http-v1.14.3) - `2026-10-13T13:47:27Z`
- [Merge pull request #792 from microsoft/dependabot/pip/packages/abstra…](https://github.com/microsoft/kiota-python/commit/d07bcce46394477b691ff96dddd4469d92d6ddd9) - `2026-10-13T18:56:45Z` - github-actions[bot] (@github-actions[bot]) - PR: [chore(deps-dev): bump the pylint group across 7 directories with 1 update](https://github.com/microsoft/kiota-python/pull/792)
- [chore(deps-dev): bump the pylint group across 7 directories with 1 up…](https://github.com/microsoft/kiota-python/commit/c1db03446973e8b499c399c83d467ba0aa302863) - `2026-10-13T18:53:20Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps-dev): bump the pylint group across 7 directories with 1 update](https://github.com/microsoft/kiota-python/pull/792)
- [Merge pull request #767 from microsoft/release-please--branches--main](https://github.com/microsoft/kiota-python/commit/3485b61cd99fdc6cfb6863ed6b1a594dc3fa171e) - `2026-10-13T13:46:57Z` - Vincent Biret (@baywet) - PR: [chore: release main](https://github.com/microsoft/kiota-python/pull/767)
- [chore: release main](https://github.com/microsoft/kiota-python/commit/7f870b61dcaea778726023b57c539f4f7c53ad9f) - `2026-10-13T13:43:24Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore: release main](https://github.com/microsoft/kiota-python/pull/767)
- [Merge pull request #791 from rksharma-owg/codex/fix-form-string-white…](https://github.com/microsoft/kiota-python/commit/06e70261aadfea43d5e5e96c5640c9345f8ff3be) - `2026-10-13T13:42:20Z` - Vincent Biret (@baywet) - PR: [fix(serialization-form): preserve whitespace in string values](https://github.com/microsoft/kiota-python/pull/791)

### dotnet/AspNetCore.Docs (9 commit(s), signal 84)

Tags: `docs, human-authored, watchlist`

- [Doc: mention .NET Aspire dashboard in metrics overview (#36397) (#37794)](https://github.com/dotnet/AspNetCore.Docs/commit/8f4c5e2db373a7574d7496f9a845d4fb6e803fbf) - `2026-10-13T18:53:59Z` - surya pratap singh (@SkyDevLab) - PR: [Doc: mention .NET Aspire dashboard in metrics overview (#36397)](https://github.com/dotnet/AspNetCore.Docs/pull/37794)
- [Add docs verifier workflow (#37829)](https://github.com/dotnet/AspNetCore.Docs/commit/04d4bb6aa7b8584ccd8ccddd7b222d51e1a05760) - `2026-10-13T18:43:09Z` - Genevieve Warren (@gewarren) - PR: [Add docs verifier workflow](https://github.com/dotnet/AspNetCore.Docs/pull/37829)
- [Doc: fix premature RedirectToAction on DbUpdateException in Edit acti…](https://github.com/dotnet/AspNetCore.Docs/commit/5c7628b5e56187b3e6d46b7498be221795629345) - `2026-10-13T18:41:56Z` - surya pratap singh (@SkyDevLab) - PR: [Doc: fix premature RedirectToAction on DbUpdateException in Edit actions (#33725)](https://github.com/dotnet/AspNetCore.Docs/pull/37795)
- [Document `--file` option for `dotnet user-jwts` with file-based apps …](https://github.com/dotnet/AspNetCore.Docs/commit/c3cd1014c7219366084b88b7a92455c9541c61a2) - `2026-10-13T18:32:22Z` - Copilot (@Copilot) - PR: [Document `--file` option for `dotnet user-jwts` with file-based apps (.NET 11)](https://github.com/dotnet/AspNetCore.Docs/pull/37838)
- [Fix typos in several articles (#37834)](https://github.com/dotnet/AspNetCore.Docs/commit/e1e34a404ad56585f7129f1bab321502d57da8cd) - `2026-10-13T11:57:50Z` - Caitlin Leonard (@caitlin-leonard) - PR: [Fix typos in several articles](https://github.com/dotnet/AspNetCore.Docs/pull/37834)

### MicrosoftDocs/sql-docs (9 commit(s), signal 84)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/sql-docs…](https://github.com/MicrosoftDocs/sql-docs/commit/717df0060aa24c083448b0f90755ac68b27e0efd) - `2026-10-13T17:39:19Z` - Learn Build Service GitHub App
- [Merge pull request #38334 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/sql-docs/commit/b0f4e0ae5da698ad355339b0180a19323f43ba41) - `2026-10-13T17:37:34Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Move primary key requirement in vector index to old index (#10412)](https://github.com/MicrosoftDocs/sql-docs/commit/e514ba3a371104d8ebdccee6f41c81cac69b10b0) - `2026-10-13T17:32:10Z` - Cláudio Silva (@ClaudioESSilva) - PR: [Move primary key requirement in vector index to old index](https://github.com/MicrosoftDocs/sql-docs/pull/10412)
- [Merge pull request #38333 from rwestMSFT/rw-1013-wwi-link](https://github.com/MicrosoftDocs/sql-docs/commit/30a3be97897ab1044040597498486ecc49c36a6b) - `2026-10-13T17:27:28Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Update create-linked-servers-sql-server-database-engine.md (#38322)](https://github.com/MicrosoftDocs/sql-docs/commit/26bbd58721230c438c5b20227adb219be9d9ad02) - `2026-10-13T17:23:43Z` - Hugo Queiroz (@HugoMSFT)

### dotnet/android-api-docs (9 commit(s), signal 109)

Tags: `docs, human-authored, security, watchlist`

- [Import AppFunctions API 37 documentation (#844)](https://github.com/dotnet/android-api-docs/commit/dbaf73f73435c7c62e3fb0b752d177a76b28d6cb) - `2026-10-13T17:27:30Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Import AppFunctions API 37 documentation](https://github.com/dotnet/android-api-docs/pull/844)
- [Add HID device documentation (#838)](https://github.com/dotnet/android-api-docs/commit/78db572167778abe7bc374e49662d131cea458d8) - `2026-10-13T17:15:23Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Add Android HID device documentation](https://github.com/dotnet/android-api-docs/pull/838)
- [Add InputMethodManager animation docs (#832)](https://github.com/dotnet/android-api-docs/commit/da56f9c4d1b897577a2fd40d089a033022136b80) - `2026-10-13T17:08:37Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Add InputMethodManager animation documentation](https://github.com/dotnet/android-api-docs/pull/832)
- [Add Android.Security.Net.Config documentation (#841)](https://github.com/dotnet/android-api-docs/commit/594920fd10c3041588bc441d568556eae5a5cf83) - `2026-10-13T17:08:00Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Add Android.Security.Net.Config API 37 documentation](https://github.com/dotnet/android-api-docs/pull/841)
- [Add VibrationEffect Builder documentation (#833)](https://github.com/dotnet/android-api-docs/commit/f9f22e9a9891b9a2ad2ee039800f1588aaa260f0) - `2026-10-13T17:05:00Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Add VibrationEffect Builder documentation](https://github.com/dotnet/android-api-docs/pull/833)

### MicrosoftDocs/azure-management-docs (9 commit(s), signal 84)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #2941 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-management-docs/commit/36d8fca4a044d090fcd535c5ecf1390faf0efbea) - `2026-10-13T17:10:01Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #2935 from yhussein896/docs-editor/prerequisites-1…](https://github.com/MicrosoftDocs/azure-management-docs/commit/3fda26f7e318ab399348e35384e7b2299dd8d7f4) - `2026-10-13T13:59:48Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #2939 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-management-docs/commit/2dda974ca8f8ca713d9af1ccf00a0dc48824af79) - `2026-10-13T06:03:07Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #2938 from MasonTorres/ESU-SPLA-updates](https://github.com/MicrosoftDocs/azure-management-docs/commit/bcca6f57afbf861b1e3667e4f8d458d36428db3c) - `2026-10-13T00:09:58Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Update licensing information for Windows Server 2016 ESUs to clarify …](https://github.com/MicrosoftDocs/azure-management-docs/commit/3962cbcda4e9edecad37f536f03631263d6a4945) - `2026-10-12T23:47:01Z` - Mason Torres (@MasonTorres)

### dotnet/docs-maui (9 commit(s), signal 84)

Tags: `docs, human-authored, watchlist`

- [Theming: preserve merged app resources (#3470)](https://github.com/dotnet/docs-maui/commit/4945ee84e71af27e1a2202f0429dcbabb68b835a) - `2026-10-13T15:18:19Z` - Gerald Versluis (@jfversluis) - PR: [Fix runtime theme resource replacement](https://github.com/dotnet/docs-maui/pull/3470)
- [Update remote iOS Simulator log paths and troubleshooting guidance (#…](https://github.com/dotnet/docs-maui/commit/a082181360b1c6eea237848f22b12c5fcfe314cd) - `2026-10-13T15:17:38Z` - Copilot (@Copilot) - PR: [Update remote iOS Simulator log paths and troubleshooting guidance](https://github.com/dotnet/docs-maui/pull/3555)
- [Document automatic DevFlow startup for GTK/Linux (#3541)](https://github.com/dotnet/docs-maui/commit/60558e3f29caf303cd23102ec69c6f60eb0a6725) - `2026-10-13T15:17:27Z` - Copilot (@Copilot) - PR: [Document automatic DevFlow startup for GTK/Linux](https://github.com/dotnet/docs-maui/pull/3541)
- [docs(templates): add .NET 11 RC2 command-line options (#3572)](https://github.com/dotnet/docs-maui/commit/eed538aeebc12d8b463e090e19d32c36552741ec) - `2026-10-13T14:58:14Z` - David Ortinau (@davidortinau) - PR: [.NET 11 RC2 docs: document C# UI and Avalonia template options](https://github.com/dotnet/docs-maui/pull/3572)
- [docs(deployment): cover .NET 11 RC2 runtime and publishing changes (#…](https://github.com/dotnet/docs-maui/commit/6e6657d45e3c17ac7a1d53a24a71aa8b57aba94f) - `2026-10-13T14:57:30Z` - David Ortinau (@davidortinau) - PR: [.NET 11 RC2 docs: runtime and publishing defaults](https://github.com/dotnet/docs-maui/pull/3567)

### MicrosoftDocs/dynamics-365-customer-engagement (9 commit(s), signal 94)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement/commit/6cddd9514cbebc235537374ba1fa74b55a41f05d) - `2026-10-13T13:08:12Z` - Learn Build Service GitHub App
- [Merge pull request #17205 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement/commit/4790706c53f49f1344cf14a183966d1bb6a45966) - `2026-10-13T13:05:20Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [New UI screen to enable conversation diagnostics + Diagnose button fo…](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement/commit/a1470bf49777e9799e49b94e6119fa96f5690167) - `2026-10-13T12:58:11Z` - gandhamm (@gandhamm)
- [Field Service ur9.3 8.8.150.60 release notes (#17173)](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement/commit/df5f85bec60a6aeb59931908447ab313777d986f) - `2026-10-13T12:26:22Z` - HY (@Hongyan2014)
- [Freshness updates for SRA and Copilot Overview (#17203)](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement/commit/074af242095ed6302575b821649f852655e7b730) - `2026-10-13T12:01:33Z` - lavanyakr01 (@lavanyakr01)

### Azure/azure-sdk-for-js (8 commit(s), signal 133)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [@azure/arm-commvaultcontentstore_1.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-commvaultcontentstore_1.0.0) - `2026-10-12T21:33:25Z`
- [[AutoPR @azure-arm-cloudhealth]-generated-from-SDK Generation - JS-68…](https://github.com/Azure/azure-sdk-for-js/commit/23d290aa2bddef1e4647ab60ecb54d856a2e7e74) - `2026-10-13T19:46:44Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR @azure-arm-cloudhealth]-generated-from-SDK Generation - JS-6884316](https://github.com/Azure/azure-sdk-for-js/pull/40093)
- [Add OneSettings control for Azure Monitor Live Metrics (#40282)](https://github.com/Azure/azure-sdk-for-js/commit/d0edf04a9e13f9a4f0a588d1fc4226e1b52fd51e) - `2026-10-13T19:21:38Z` - Jackson Weber (@JacksonWeber) - PR: [Add OneSettings control for Azure Monitor Live Metrics](https://github.com/Azure/azure-sdk-for-js/pull/40282)
- [[docs] Fix inconsistent pnpm turbo build command in migrating-to-type…](https://github.com/Azure/azure-sdk-for-js/commit/beafb1fde8bc0d8178330c2e19981426c06698f3) - `2026-10-13T19:13:33Z` - Jeremy Meng (@jeremymeng) - PR: [[docs] Fix inconsistent pnpm turbo build command in migrating-to-typespec.md](https://github.com/Azure/azure-sdk-for-js/pull/40312)
- [Upgrade magic-string to 1.4.3 in @azure/ai-form-recognizer (#40299)](https://github.com/Azure/azure-sdk-for-js/commit/ef2a29238eed3348a7d0688f430d405abdbcaab9) - `2026-10-13T17:23:02Z` - Jeremy Meng (@jeremymeng) - PR: [Upgrade magic-string to 1.4.3 in @azure/ai-form-recognizer](https://github.com/Azure/azure-sdk-for-js/pull/40299)
- [[Identity] GA Identity Binding Feature (#40297)](https://github.com/Azure/azure-sdk-for-js/commit/4fb292a6faa5f6efdcb9063cf517ab06a117cdd1) - `2026-10-13T16:53:02Z` - Minh-Anh Phan (@minhanh-phan) - PR: [[Identity] GA Identity Binding Feature](https://github.com/Azure/azure-sdk-for-js/pull/40297)

### MicrosoftDocs/azure-aks-docs (8 commit(s), signal 108)

Tags: `docs, human-authored, security, watchlist`

- [Merge pull request #3984 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-aks-docs/commit/5f0ef478ac5f298fe0a81ec5694d4a5695e1934d) - `2026-10-13T17:08:39Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [security: Document external node CSR role permission breaking change …](https://github.com/MicrosoftDocs/azure-aks-docs/commit/5b20bb37906d55958b5d66d9ed36c5e3d6555ef2) - `2026-10-13T16:59:57Z` - Wei Weng (@weng271190436)
- [Document Fleet hub protected-resource access restrictions (#3956)](https://github.com/MicrosoftDocs/azure-aks-docs/commit/8c58fc5370acdd6d4969af52c75bc9237d7997ca) - `2026-10-13T16:15:32Z` - Wei Weng (@weng271190436)
- [Merge pull request #3981 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-aks-docs/commit/b3d2acfee62b021eda3a197815176c69f5ed157f) - `2026-10-13T11:02:25Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #3931 from rahulrai-in/docs/ipv6-only-node-public-…](https://github.com/MicrosoftDocs/azure-aks-docs/commit/49e129dcf5eab6b8f01a056d03eb97cdb7c43932) - `2026-10-13T06:58:16Z` - prmerger-automator[bot] (@prmerger-automator[bot])

### microsoft/onnxruntime (8 commit(s), signal 58)

Tags: `human-authored, release-language, samples`

- [Fix Windows float16 model-path conversion (#33193)](https://github.com/microsoft/onnxruntime/commit/c9f4bb5655609ce406b3032fb3784eaf77b927b2) - `2026-10-13T15:43:08Z` - A Aswanth Raj (@aswanth-07) - PR: [Fix Windows float16 model-path conversion](https://github.com/microsoft/onnxruntime/pull/33193)
- [[MLAS] Skip FP16 unit tests on CPUs without FP16 arithmetic (#33260)](https://github.com/microsoft/onnxruntime/commit/208463adfb92452e9aa8a7266eb5d4497bf97b53) - `2026-10-13T15:42:07Z` - Yair Ben Avraham (@yairbenavraham) - PR: [[MLAS] Skip FP16 unit tests on CPUs without FP16 arithmetic](https://github.com/microsoft/onnxruntime/pull/33260)
- [Validate inline sparse payloads before dense allocation (#32863)](https://github.com/microsoft/onnxruntime/commit/9036f076a2ce4b970f2a2fb0149b0914981d8af4) - `2026-10-13T07:13:00Z` - danielsongmicrosoft (@danielsongmicrosoft) - PR: [Validate inline sparse payloads before dense allocation](https://github.com/microsoft/onnxruntime/pull/32863)
- [[WebGPU] Support fixed subgroup size in im2col_matmul (#33249)](https://github.com/microsoft/onnxruntime/commit/6a78e30eff15fc844f5a4e3bebfd948a3cf6581f) - `2026-10-13T05:17:42Z` - Jiawei Shao (@Jiawei-Shao) - PR: [[WebGPU] Support fixed subgroup size in im2col_matmul](https://github.com/microsoft/onnxruntime/pull/33249)
- [[CUDA] Include SM100 in Linux aarch64 CUDA 13 packages (#33315)](https://github.com/microsoft/onnxruntime/commit/e2e7a0a02df9936c324613791fdfe00bc5972735) - `2026-10-13T01:46:19Z` - Dev Churiwala (@DevChuriwala) - PR: [[CUDA] Include SM100 in Linux aarch64 CUDA 13 packages](https://github.com/microsoft/onnxruntime/pull/33315)

### MicrosoftDocs/windowsserverdocs (7 commit(s), signal 82)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #8486 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/windowsserverdocs/commit/c53c52e82327f4b4ea28af92e2ab8c132cd617f6) - `2026-10-13T17:33:17Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #8484 from davannaw-msft/main](https://github.com/MicrosoftDocs/windowsserverdocs/commit/6f4b3a1621b77ba8638419ee7097cdc60aa37434) - `2026-10-13T16:35:14Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Update WindowsServerDocs/manage/windows-admin-center/azure/extension-…](https://github.com/MicrosoftDocs/windowsserverdocs/commit/f0b090426599f586bc237eb60675b5a3105d4a5b) - `2026-10-13T16:24:32Z` - Davanna White (@davannaw-msft)
- [Update WindowsServerDocs/manage/windows-admin-center/azure/extension-…](https://github.com/MicrosoftDocs/windowsserverdocs/commit/9364fd987567e8769f5a25074e8c9296137ed8be) - `2026-10-13T16:24:16Z` - Davanna White (@davannaw-msft)
- [Update WindowsServerDocs/manage/windows-admin-center/azure/manage-arc…](https://github.com/MicrosoftDocs/windowsserverdocs/commit/44deab5fe7abf77a0e2c4a1d651ca66288ee1317) - `2026-10-13T16:24:04Z` - Davanna White (@davannaw-msft)

### MicrosoftDocs/azure-stack-docs (7 commit(s), signal 82)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #4534 from MicrosoftDocs/main639275078258854142syn…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/376e28fa85487d3ddf4b8c32c5961f459a39384e) - `2026-10-13T17:03:57Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4534)
- [Merging changes synced from https://github.com/MicrosoftDocs/azure-st…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/bffcdf5992efa19ad0e101d9c7e402e98935d961) - `2026-10-13T17:03:41Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4534)
- [Merge pull request #21891 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-stack-docs/commit/be5dfb2850361c0de52f39483325ac6f9e29815d) - `2026-10-13T17:02:23Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4534)
- [Docs runread racadm ipmitool 4.13 (#21802)](https://github.com/MicrosoftDocs/azure-stack-docs/commit/97d9525a772b9c8c8bbabd2a83d9c8f5472399b9) - `2026-10-13T14:20:54Z` - moconnor (@mso128) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4534)
- [Merge pull request #4532 from MicrosoftDocs/main639274394084830218syn…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/715ca3feaee4f3c96d7af2307637921eff4c955d) - `2026-10-12T22:03:45Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4532)

### MicrosoftDocs/azure-dev-docs (7 commit(s), signal 82)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-de…](https://github.com/MicrosoftDocs/azure-dev-docs/commit/6f881918d9e173ee5be03e5ffc63dd4ed012d058) - `2026-10-13T17:03:32Z` - Learn Build Service GitHub App
- [Merge pull request #9912 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-dev-docs/commit/dfc128b273742c9363ecb19889e0794cdc5233a4) - `2026-10-13T17:02:45Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update links to fix broken links (#9910)](https://github.com/MicrosoftDocs/azure-dev-docs/commit/effe6292a3b3f49e5b33bf734070e513531f4118) - `2026-10-13T08:42:33Z` - Saisang Cai (@Saisang)
- [Merge pull request #9911 from MicrosoftDocs/Saisang-patch-2](https://github.com/MicrosoftDocs/azure-dev-docs/commit/dcb9c6c2f31cd9fac744e46b768558a209e0c5e8) - `2026-10-13T08:37:23Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Update tutorial-containerize-simple-web-app-for-app-service.md](https://github.com/MicrosoftDocs/azure-dev-docs/commit/f7e1014f8ab66a6f46753cd5f94d1229a73d2713) - `2026-10-13T08:29:48Z` - Saisang Cai (@Saisang)

### MicrosoftDocs/power-pages-docs (7 commit(s), signal 82)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #1996 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-pages-docs/commit/37506cd6e44ba1adf5a20168a2db4142e8ffdcca) - `2026-10-13T13:02:03Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Transfer ownership update](https://github.com/MicrosoftDocs/power-pages-docs/commit/64072b6883c2f0644118b47d2880cfabd4e39004) - `2026-10-13T10:09:19Z` - Shweta (@shwetamurkute)
- [Merge pull request #1995 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-pages-docs/commit/fdad31c1a2c7504c77883400fb30fa1bc6e0aec4) - `2026-10-13T07:02:03Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Power Pages client API documentation update](https://github.com/MicrosoftDocs/power-pages-docs/commit/acc726faf5485548d37e1b5016dd10de38f94860) - `2026-10-13T06:11:00Z` - Neeraj Nandwana (@neerajnandwana-msft)
- [Power Pages SPA template support for Copilot CLI and Claude Code](https://github.com/MicrosoftDocs/power-pages-docs/commit/f0dacd693a9eb586275b22c54b1a93d22e12cf87) - `2026-10-13T06:04:43Z` - Neeraj Nandwana (@neerajnandwana-msft)

### microsoftgraph/microsoft-graph-docs-contrib (7 commit(s), signal 82)

Tags: `docs, human-authored, product:Microsoft Graph, watchlist`

- [Merge pull request #10064 from microsoftgraph/main639274493133647479s…](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/2ae7381806788f6b3581d85133d0f7df70532fe2) - `2026-10-13T00:48:50Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10064)
- [Merging changes synced from https://github.com/microsoftgraph/microso…](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/7f5b8373687ec2d42362c31081c4aaeb8d4a8f97) - `2026-10-13T00:48:28Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10064)
- [Merge pull request #29736 from microsoftgraph/main](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/b12b836986ceb90cfcf3229a2e501ce31ddce2ec) - `2026-10-13T00:41:42Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10064)
- [Add beta documentation for AuditCore record types 476-510 (#29663)](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/ce6baabc20a5cd1c12ef7bcf16a02299f344b48f) - `2026-10-12T23:28:21Z` - diksha27 (@diksha27) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10064)
- [Update whats-new-overview.md (#29731)](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/e14474410ae18182b6dc30d8dcaf524ef73c58e1) - `2026-10-12T23:28:05Z` - Jarbas Horst (@JarbasHorst) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10064)

### Azure-Samples/fabric-cicd-generic-git (6 commit(s), signal 91)

Tags: `human-authored, product:Azure AI, release-language, samples, watchlist`

- [Merge pull request #3 from Azure-Samples/copilot/fix-broken-link-in-r…](https://github.com/Azure-Samples/fabric-cicd-generic-git/commit/5ec9ded5b8491a963f1956d0845f94b3be2e6708) - `2026-10-13T19:52:45Z` - Yaron Pri-Gal (@yaronpri) - PR: [Update README tutorial link](https://github.com/Azure-Samples/fabric-cicd-generic-git/pull/3)
- [Fix remaining README tutorial link](https://github.com/Azure-Samples/fabric-cicd-generic-git/commit/ea986c89f6744fcf3968a199f97110f32330dd00) - `2026-10-13T17:47:24Z` - copilot-swe-agent[bot] (@Copilot) - PR: [Update README tutorial link](https://github.com/Azure-Samples/fabric-cicd-generic-git/pull/3)
- [Fix broken tutorial link in README](https://github.com/Azure-Samples/fabric-cicd-generic-git/commit/a1c54d4d6ef33174dc93aa4d2acf0dd1ef900b06) - `2026-10-13T17:43:16Z` - copilot-swe-agent[bot] (@Copilot) - PR: [Update README tutorial link](https://github.com/Azure-Samples/fabric-cicd-generic-git/pull/3)
- [Initial plan](https://github.com/Azure-Samples/fabric-cicd-generic-git/commit/c81d95b3fa532d902ff9c14b88dfc63ed656a39c) - `2026-10-13T17:41:49Z` - copilot-swe-agent[bot] (@Copilot) - PR: [Update README tutorial link](https://github.com/Azure-Samples/fabric-cicd-generic-git/pull/3)
- [Merge pull request #1 from yaronpri/bulk-api-ga](https://github.com/Azure-Samples/fabric-cicd-generic-git/commit/2a10c734bfdd8aa2a71dc03ac2937daa2a471f11) - `2026-10-13T17:33:59Z` - Elena Terenzi (@elenaterenzi) - PR: [Remove Preview/beta=true for Bulk Export/Import APIs (now GA)](https://github.com/Azure-Samples/fabric-cicd-generic-git/pull/1)

### MicrosoftDocs/powerapps-docs (6 commit(s), signal 81)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/powerapp…](https://github.com/MicrosoftDocs/powerapps-docs/commit/8e6c84e105229b68509836a9043404302fb607ea) - `2026-10-13T19:05:59Z` - Learn Build Service GitHub App
- [Merge pull request #12725 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/powerapps-docs/commit/6ef939a3ea462e73c94900dd37c5d95e171ac6f4) - `2026-10-13T19:03:32Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Document Dataverse.Unmask for canvas apps (#12713)](https://github.com/MicrosoftDocs/powerapps-docs/commit/55ebd5c4c6bffc96dc094d19ecfd1d11fba08e0d) - `2026-10-13T16:54:52Z` - Yogesh Gupta (@yogeshgupta698)
- [Merging changes synced from https://github.com/MicrosoftDocs/powerapp…](https://github.com/MicrosoftDocs/powerapps-docs/commit/02070ebdd6452279bb620fe113e7a6da439005c0) - `2026-10-13T01:05:23Z` - Learn Build Service GitHub App
- [Merge pull request #12723 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/powerapps-docs/commit/55b4d48d22a316bf159cc1fd59c6720acdb94d14) - `2026-10-13T01:03:22Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### MicrosoftDocs/dynamics-365-project-operations (6 commit(s), signal 81)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/d23830143d9d8d9aa14084e47617f70a121e749f) - `2026-10-13T19:02:34Z` - Learn Build Service GitHub App
- [Merge pull request #2793 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/9a246b975554bbf86de7250eed2aa7edbdd1fc3a) - `2026-10-13T19:02:08Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Default column configuration (#2790)](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/3d0729d90995e0ee61e45b31ec8410bcba79f586) - `2026-10-13T18:26:58Z` - Dishant Popli (@dpopli)
- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/f20186204e1f8be5da7e49aca5c2044007e9216a) - `2026-10-13T01:02:31Z` - Learn Build Service GitHub App
- [Merge pull request #2792 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/5e55bb3d17ed74509a470cad5219879a7fcd0196) - `2026-10-13T01:02:07Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### MicrosoftDocs/azure-docs-sdk-java (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [docs: update retired Service Bus Java reference (#2662)](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/9f08ebf03a40f228d48e9493224783a68d360c69) - `2026-10-13T18:40:08Z` - Eldert Grootenboer (@EldertGrootenboer) - PR: [docs: update retired Service Bus Java reference](https://github.com/MicrosoftDocs/azure-docs-sdk-java/pull/2662)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/f4d713f562c409018ee7410b09ac1710b27937c2) - `2026-10-13T03:40:56Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/911b89ac757b8d852680ff64941ca54c74ecca07) - `2026-10-13T03:40:01Z` - azure-sdk (@azure-sdk)
- [CI Update](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/40a29713dc660aac20aaea02a76038f22e684a66) - `2026-10-13T01:57:40Z` - docsreference@microsoft.com
- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/f1d18e9ce4ddabd6968e38f7390cccbf548dc507) - `2026-10-12T23:48:39Z` - azure-sdk (@azure-sdk)

### microsoft/kiota-ruby (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #178 from andreaTP/feat/serialization-form](https://github.com/microsoft/kiota-ruby/commit/b60fd82ec3e342843fdc07121e7a84c30372c4bd) - `2026-10-13T17:37:46Z` - Vincent Biret (@baywet) - PR: [feat: add form serialization](https://github.com/microsoft/kiota-ruby/pull/178)
- [refactor: read form fields as sent](https://github.com/microsoft/kiota-ruby/commit/ecf4944e29bda5152a74d5d77f0497ac398a74f1) - `2026-10-13T16:22:03Z` - andreatp (@andreaTP) - PR: [feat: add form serialization](https://github.com/microsoft/kiota-ruby/pull/178)
- [refactor: read a form date, time or date time only in its own shape](https://github.com/microsoft/kiota-ruby/commit/ff29bbca0e6081760306d47cdcbe31dd6b49acfa) - `2026-10-13T16:01:19Z` - andreatp (@andreaTP) - PR: [feat: add form serialization](https://github.com/microsoft/kiota-ruby/pull/178)
- [refactor: accept an empty form body](https://github.com/microsoft/kiota-ruby/commit/967129f1d5be51ed49af422a071ec0fb15274411) - `2026-10-13T15:52:32Z` - andreatp (@andreaTP) - PR: [feat: add form serialization](https://github.com/microsoft/kiota-ruby/pull/178)
- [refactor: read an empty form value as an empty string](https://github.com/microsoft/kiota-ruby/commit/de57d85bf0ac21e3aafbc4b95ef9bf4a865907a7) - `2026-10-13T15:04:16Z` - andreatp (@andreaTP) - PR: [feat: add form serialization](https://github.com/microsoft/kiota-ruby/pull/178)

### Azure/azure-cli-extensions (6 commit(s), signal 91)

Tags: `docs, human-authored, release-language, watchlist`

- [{AKS} Add `--enable-upgrade-gate`/`--disable-upgrade-gate` to aks-pre…](https://github.com/Azure/azure-cli-extensions/commit/0877d2279ff0777cc5df218725c984c852c435bc) - `2026-10-13T00:32:31Z` - alice_wang (@Xinyue-Wang) - PR: [{AKS} Add `--enable-upgrade-gate`/`--disable-upgrade-gate` to aks-preview](https://github.com/Azure/azure-cli-extensions/pull/10448)
- [Release 1.0.9 of Azure DevOps CLI Extension (#10451)](https://github.com/Azure/azure-cli-extensions/commit/a56510b65e6cf7f4a554bfcbaca476efee3ce1a2) - `2026-10-12T23:55:25Z` - mishrarish (@mishrarish) - PR: [Release 1.0.9 of Azure DevOps CLI Extension](https://github.com/Azure/azure-cli-extensions/pull/10451)
- [Add stack-hci-vm 1.16.0 to extension index (#10452)](https://github.com/Azure/azure-cli-extensions/commit/4a4cbcb556cd440e6ed14dc7e068c74901aa483f) - `2026-10-12T23:38:40Z` - Altayl (@Altayl) - PR: [Add stack-hci-vm 1.16.0 to extension index](https://github.com/Azure/azure-cli-extensions/pull/10452)
- [Add golden gate tests to credscan suppression (#10460)](https://github.com/Azure/azure-cli-extensions/commit/e1eda3880806b8eb3997d1fd11751ff11720bbb9) - `2026-10-12T23:21:04Z` - JaysonTaiMicrosoft (@JaysonTaiMicrosoft) - PR: [{CI} Supress golden gate oracledatabase cred scan](https://github.com/Azure/azure-cli-extensions/pull/10460)
- [[Release] Update index.json for extension [ aks-preview-22.0.0b13 ]](https://github.com/Azure/azure-cli-extensions/commit/f4f8fbc5811c72b07d28da71bed0461e7373f1af) - `2026-10-12T22:46:51Z` - Azure CLI Team (@azclibot)

### MicrosoftDocs/entra-docs (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #14590 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/entra-docs/commit/927efa819a6f89a40b39b178d702b30f49b63f00) - `2026-10-13T17:34:42Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #14588 from jasonfritts/patch-9](https://github.com/MicrosoftDocs/entra-docs/commit/2bbf81e29fcd467e6d500ecf56f0bdfd14b1ceee) - `2026-10-13T15:33:20Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #14587 from jasonfritts/patch-8](https://github.com/MicrosoftDocs/entra-docs/commit/2d29f4a8d2d49011896b621510f162f07161aff3) - `2026-10-13T15:01:35Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Update cross-tenant-access-overview.md](https://github.com/MicrosoftDocs/entra-docs/commit/d232317b9764e7f6fd301001850cd7a7ab3abaa7) - `2026-10-13T15:00:23Z` - Jason Fritts (@jasonfritts)
- [Update cross-tenant-access-overview.md](https://github.com/MicrosoftDocs/entra-docs/commit/96112b88b3fc5a0c3e5f145e23651392e4013b5d) - `2026-10-13T14:54:53Z` - Jason Fritts (@jasonfritts)

### MicrosoftDocs/azure-monitor-docs (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #5620 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/cf1d58579d8e5884c3f591ea5e4e7b25af8a73ae) - `2026-10-13T17:10:18Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [[Docs] Add Azure Monitor health models to Azure Monitor service limit…](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/e96ea92fcdcd256cc1dfb6b17106bc8c3d2c8578) - `2026-10-13T14:29:01Z` - Megan G (@megan-e-goode)
- [Merge pull request #5618 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/c2c01334c385ca12cfb66dbe435a43a690afc71b) - `2026-10-13T06:04:05Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update Health Models FAQ with SME content (3) (#5616)](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/83e05fb997721ee21c5f08bcb42152ea67d45b5d) - `2026-10-12T23:03:58Z` - Bailey Anderson (@baanders)
- [Merge pull request #5617 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/a06cabf7794163d0668674970eeb62f8aff86401) - `2026-10-12T22:09:41Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### Azure/azure-sdk-for-python (5 commit(s), signal 130)

Tags: `docs, human-authored, product:Azure AI, product:Azure SDK, release, release-language, watchlist`

- Release: [azure-ai-agentserver-activity_1.0.0b4](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-activity_1.0.0b4) - `2026-10-13T18:46:49Z`
- Release: [azure-mgmt-commvaultcontentstore_1.0.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-commvaultcontentstore_1.0.0) - `2026-10-13T03:57:46Z`
- Release: [azure-mgmt-cognitiveservices_15.0.0b6](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-cognitiveservices_15.0.0b6) - `2026-10-13T03:52:20Z`
- [[azure-ai-evaluation] Release 1.18.9 (#49504)](https://github.com/Azure/azure-sdk-for-python/commit/701c4878e38cd365ad007e7b27ffbffeaf8e7dcb) - `2026-10-13T16:06:18Z` - Rabah B (@RabsB) - PR: [[azure-ai-evaluation] Release 1.18.9](https://github.com/Azure/azure-sdk-for-python/pull/49504)
- [Add agent snapshot lifecycle hooks (#49217)](https://github.com/Azure/azure-sdk-for-python/commit/037e8b7867bfcc2285d57c648c2ab5534ec86e06) - `2026-10-13T08:29:23Z` - Pranav Pandit (@vangarp) - PR: [Add agent snapshot lifecycle hooks](https://github.com/Azure/azure-sdk-for-python/pull/49217)
- [Enable AgentServer SSE keep-alives by default (#49378)](https://github.com/Azure/azure-sdk-for-python/commit/385e07bb742d6e8cea4ecad34d6d403d2387fb8b) - `2026-10-13T06:24:25Z` - Copilot (@Copilot) - PR: [Enable AgentServer SSE keep-alives by default](https://github.com/Azure/azure-sdk-for-python/pull/49378)
- [[AutoPR azure-mgmt-cognitiveservices]-generated-from-SDK Generation -…](https://github.com/Azure/azure-sdk-for-python/commit/381b3bdf3258baa7d5386c730b08d73b94ecd60e) - `2026-10-13T02:28:20Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-mgmt-cognitiveservices]-generated-from-SDK Generation - Python-6940910](https://github.com/Azure/azure-sdk-for-python/pull/49463)
- [[EngSys] Add opt-in Rust native wheel build support (#49397)](https://github.com/Azure/azure-sdk-for-python/commit/3ba1c0457c6c1acaeecaed10342676c84df2c3d9) - `2026-10-12T23:19:30Z` - jenny (@JennyPng) - PR: [[EngSys] Add opt-in Rust native wheel build support](https://github.com/Azure/azure-sdk-for-python/pull/49397)

### dotnet/roslyn (5 commit(s), signal 80)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [[main] Update dependencies from dotnet/roslyn (#85916)](https://github.com/dotnet/roslyn/commit/2f6818a02864623e4dcf3d997402519466286bff) - `2026-10-13T15:01:16Z` - dotnet-maestro[bot] (@dotnet-maestro[bot]) - PR: [[main] Update dependencies from dotnet/roslyn](https://github.com/dotnet/roslyn/pull/85916)
- [Fix compiler crash for partial a union declaration (#86025)](https://github.com/dotnet/roslyn/commit/636ab77a25a95adb109ebf7e9a4d73f6d0b94643) - `2026-10-13T13:52:19Z` - AlekseyTs (@AlekseyTs) - PR: [Fix compiler crash for partial a union declaration](https://github.com/dotnet/roslyn/pull/86025)
- [Do not force a newline between } and , in switch expressions (#85992)](https://github.com/dotnet/roslyn/commit/ee4be673ec91d3fbc7431af047a883c6ad00ff9e) - `2026-10-13T11:43:40Z` - Cyrus Najmabadi (@CyrusNajmabadi) - PR: [Do not force a newline between } and , in switch expressions](https://github.com/dotnet/roslyn/pull/85992)
- [Don't include the zero member when formatting a flags enum TypedConst…](https://github.com/dotnet/roslyn/commit/ac2d4c71ad02cc88afa137480b7cc282e6259588) - `2026-10-13T09:16:53Z` - Franco Ceballos Rastello (@xThreeh) - PR: [Don't include the zero member when formatting a flags enum TypedConstant](https://github.com/dotnet/roslyn/pull/85975)
- [Require fail-before/pass-after regression test evidence (#86020)](https://github.com/dotnet/roslyn/commit/47f4f56c7f56dc46a627570540a1a57122708f5b) - `2026-10-12T20:22:24Z` - Ankita Khera (@akhera99) - PR: [Require fail-before/pass-after regression test evidence](https://github.com/dotnet/roslyn/pull/86020)

### MicrosoftDocs/dynamics-365-unified-operations-public (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/Dynamics…](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/7d86a35169692606d303c21e204ae6032d44d44e) - `2026-10-13T13:05:48Z` - Learn Build Service GitHub App
- [Merge pull request #22668 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/c9f3214c71788ddf6d387948388e03a7919fe5d5) - `2026-10-13T13:03:00Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add schedule for 10.0.48 PQU 8 (#22664)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/ee1e57bbe984653fc1ea2fdacc0b38cc38494829) - `2026-10-13T12:53:41Z` - Aarsh Sharma (@aarsh-msft)
- [Confirm merge from repo_sync_working_branch to main to sync with http…](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/7b5b0acf08d3377bc2a40a87476afc441e1e18fe) - `2026-10-13T12:47:48Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Revise documentation for custom pricing attributes (#5214)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/103f4dbced5424b77105271bae0aacad36aeccf8) - `2026-10-13T12:39:11Z` - Chelsie Barrientos (@chelsiemb) - PR: [Revise documentation for custom pricing attributes](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/pull/5214)

### MicrosoftDocs/azure-docs-sdk-python (4 commit(s), signal 79)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/f449c2e5a3d8374cb88e6b1fefd2fd7ab70da77e) - `2026-10-13T19:06:30Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/5665b4c3f42008c80af105096c1c5c09994c0ca6) - `2026-10-13T04:11:53Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/2e6f7f3b6ca2bdcafaa22819e2b51fee9f035156) - `2026-10-13T04:11:19Z` - azure-sdk (@azure-sdk)
- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/d7694e0bd30d5fd7c028aa4b8e8c619ccf14167f) - `2026-10-12T23:06:31Z` - azure-sdk (@azure-sdk)

### microsoft/perfview (4 commit(s), signal 44)

Tags: `human-authored, samples`

- [Run FastSerialization tests in CI (#2490)](https://github.com/microsoft/perfview/commit/089db7a9887642b8f587ae03d21d0a139c30ea0e) - `2026-10-13T18:50:27Z` - Brian Robbins (@brianrob) - PR: [Run FastSerialization Tests In CI](https://github.com/microsoft/perfview/pull/2490)
- [Run FastSerialization tests in CI](https://github.com/microsoft/perfview/commit/f8afdea799239cd2225d6b3b140d887bf27ea5e7) - `2026-10-13T16:47:10Z` - Brian Robbins (@brianrob) - PR: [Run FastSerialization Tests In CI](https://github.com/microsoft/perfview/pull/2490)
- [Fix Linux tracing test architecture mismatch (#2487)](https://github.com/microsoft/perfview/commit/24df4e2c53b9e01c545c92cb1193c75ce69b8a96) - `2026-10-13T02:04:10Z` - Brian Robbins (@brianrob) - PR: [Fix LinuxTracing.Tests Architecture Mismatch](https://github.com/microsoft/perfview/pull/2487)
- [Fix Linux tracing test architecture mismatch](https://github.com/microsoft/perfview/commit/be03ca3f32f2dfeb8ddf75e1b563063fe47644de) - `2026-10-13T01:56:23Z` - Brian Robbins (@brianrob) - PR: [Fix LinuxTracing.Tests Architecture Mismatch](https://github.com/microsoft/perfview/pull/2487)

### microsoft/kiota-abstractions-go (4 commit(s), signal 19)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #284 from microsoft/dependabot/go_modules/go.opent…](https://github.com/microsoft/kiota-abstractions-go/commit/24b0c957626cfe24640d01a4a9224b76b43d49fc) - `2026-10-13T10:58:37Z` - github-actions[bot] (@github-actions[bot]) - PR: [chore(deps): bump go.opentelemetry.io/otel from 1.46.0 to 1.47.0](https://github.com/microsoft/kiota-abstractions-go/pull/284)
- [Merge pull request #285 from microsoft/dependabot/go_modules/go.opent…](https://github.com/microsoft/kiota-abstractions-go/commit/641b7738005bc364fa002b65add003476cd9f921) - `2026-10-13T10:58:29Z` - github-actions[bot] (@github-actions[bot]) - PR: [chore(deps): bump go.opentelemetry.io/otel/trace from 1.46.0 to 1.47.0](https://github.com/microsoft/kiota-abstractions-go/pull/285)
- [chore(deps): bump go.opentelemetry.io/otel/trace from 1.46.0 to 1.47.0](https://github.com/microsoft/kiota-abstractions-go/commit/e41b1857124561ce057eaf605b17c96ee0e47526) - `2026-10-12T22:30:47Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump go.opentelemetry.io/otel/trace from 1.46.0 to 1.47.0](https://github.com/microsoft/kiota-abstractions-go/pull/285)
- [chore(deps): bump go.opentelemetry.io/otel from 1.46.0 to 1.47.0](https://github.com/microsoft/kiota-abstractions-go/commit/be9f0608b92c9621f5a22d17c8988e5201574cc8) - `2026-10-12T22:30:43Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump go.opentelemetry.io/otel from 1.46.0 to 1.47.0](https://github.com/microsoft/kiota-abstractions-go/pull/284)

### MicrosoftDocs/dynamics365smb-devitpro-pb (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/5b4de6fbf5ed769f456035cf8cefb202de2ab015) - `2026-10-13T19:03:20Z` - Learn Build Service GitHub App
- [Merge pull request #8120 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/014c71a895c575d5aef620e5b0048eb39a316f25) - `2026-10-13T19:02:36Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update wording for roadmap based on new shared include file (#8113)](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/c5e93f95555fa220bc49eeb6dcddb4123d320ef1) - `2026-10-13T14:34:48Z` - Eva Dupont (@edupont04)

### Azure-Samples/Apim-Samples (3 commit(s), signal 78)

Tags: `human-authored, samples, watchlist`

- [Update slide deck and samples list (#307)](https://github.com/Azure-Samples/Apim-Samples/commit/0d16dcdc9ee8f49411a4d7d00aca13778f128829) - `2026-10-13T18:31:51Z` - Simon Kurtz (@simonkurtz-MSFT) - PR: [Update slide deck and samples list](https://github.com/Azure-Samples/Apim-Samples/pull/307)
- [Fix test (#306)](https://github.com/Azure-Samples/Apim-Samples/commit/11cde52b1e90fb4945df2ca7ee083b0ec4bd9f21) - `2026-10-13T16:40:05Z` - Simon Kurtz (@simonkurtz-MSFT) - PR: [Fix test](https://github.com/Azure-Samples/Apim-Samples/pull/306)
- [Feature/add aoai v1 migration (#305)](https://github.com/Azure-Samples/Apim-Samples/commit/6dda11d817acd37e32fdbd9e2877c26c9ca8930d) - `2026-10-13T15:59:22Z` - Simon Kurtz (@simonkurtz-MSFT) - PR: [Feature/add aoai v1 migration](https://github.com/Azure-Samples/Apim-Samples/pull/305)

### microsoft/kiota-dotnet (3 commit(s), signal 128)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [v2.1.5](https://github.com/microsoft/kiota-dotnet/releases/tag/v2.1.5) - `2026-10-13T13:20:05Z`
- [fix(http): preserve values when decoding query parameter names (#825)](https://github.com/microsoft/kiota-dotnet/commit/52c5654354f4f50f3a1fa27f537e7b47281c7c68) - `2026-10-13T17:45:44Z` - raven (@r4venrudy) - PR: [fix(http): preserve values when decoding query parameter names](https://github.com/microsoft/kiota-dotnet/pull/825)
- [chore(main): release 2.1.5 (#823)](https://github.com/microsoft/kiota-dotnet/commit/eb6e8a76d2cf77b84b31d1659b4914ab3b60a9a8) - `2026-10-13T13:19:39Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(main): release 2.1.5](https://github.com/microsoft/kiota-dotnet/pull/823)
- [fix(http): honor total UTC delay for Retry-After dates (#822)](https://github.com/microsoft/kiota-dotnet/commit/512cddfaf57f24477041bd1a71ea008f3dfb1b8e) - `2026-10-13T13:02:03Z` - raven (@r4venrudy) - PR: [fix(http): honor total UTC delay for Retry-After dates](https://github.com/microsoft/kiota-dotnet/pull/822)

### Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample (3 commit(s), signal 83)

Tags: `human-authored, release, samples`

- Release: [EPP Function ZIPs 128.1](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/releases/tag/epp-packages-128-1) - `2026-10-13T17:37:00Z`
- Release: [EPP Function ZIPs 124.1](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/releases/tag/epp-packages-124-1) - `2026-10-12T21:17:54Z`
- Release: [EPP Function ZIPs 122.1](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/releases/tag/epp-packages-122-1) - `2026-10-12T20:53:07Z`
- [Prevent duplicate CYOT encryption certificates during setup (#45)](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/commit/aa8119a566265fbaf3b3c88aed0db1269dbd35cd) - `2026-10-13T17:33:33Z` - siyixian (@siyixian) - PR: [Prevent duplicate CYOT encryption certificates during setup](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/pull/45)
- [docs: clarify provider-neutral setup and authentication guidance (#44)](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/commit/e43a9a5635830ccfbbc2a8ff7f80ff2820fd37db) - `2026-10-12T21:16:05Z` - Hou (@SciencePotato) - PR: [docs: clarify provider-neutral setup and authentication guidance](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/pull/44)
- [Route SMS and voice using request-selected endpoints (#43)](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/commit/9b3d299148f26cd458f8e14525e0d76ef6719ba6) - `2026-10-12T20:51:16Z` - siyixian (@siyixian) - PR: [Route SMS and voice using request-selected endpoints](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/pull/43)

### Azure/dacs (3 commit(s), signal 128)

Tags: `human-authored, release, release-language, samples, watchlist`

- Release: [v0.1.0-alpha.2](https://github.com/Azure/dacs/releases/tag/v0.1.0-alpha.2) - `2026-10-13T17:00:57Z`
- Release: [v0.1.0-alpha.1](https://github.com/Azure/dacs/releases/tag/v0.1.0-alpha.1) - `2026-10-13T15:48:53Z`
- [fix(ci): preserve configured Minikube home](https://github.com/Azure/dacs/commit/3bea9d11cc77ef71df8f5361be13e53ad9ab9ab6) - `2026-10-13T16:45:09Z` - Joshua Long (@jmclong) - PR: [ci: run build on tag and generate docker image artifacts](https://github.com/Azure/dacs/pull/84)
- [ci: use cache lookup-only for tag builds](https://github.com/Azure/dacs/commit/722ac18924878b1603004a4469f388485d244df9) - `2026-10-13T16:45:09Z` - Joshua Long (@jmclong) - PR: [ci: run build on tag and generate docker image artifacts](https://github.com/Azure/dacs/pull/84)
- [ci(release): support tagged official builds](https://github.com/Azure/dacs/commit/d895ebb1e6baac79a389cc91f8b71849ba2c9a6b) - `2026-10-13T16:45:09Z` - Joshua Long (@jmclong) - PR: [ci: run build on tag and generate docker image artifacts](https://github.com/Azure/dacs/pull/84)

### microsoft/kiota-typescript (3 commit(s), signal 18)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [auto dependabot: bump js-yaml and lerna (#2177)](https://github.com/microsoft/kiota-typescript/commit/b79f8916973b8a48e901c03df66e4f37d9cf6099) - `2026-10-13T16:11:14Z` - dependabot[bot] (@dependabot[bot]) - PR: [auto dependabot: bump js-yaml and lerna](https://github.com/microsoft/kiota-typescript/pull/2177)
- [auto dependabot: bump handlebars and lerna (#2175)](https://github.com/microsoft/kiota-typescript/commit/04055e6d5d236908378ae758192f7d61c800b600) - `2026-10-13T16:10:42Z` - dependabot[bot] (@dependabot[bot]) - PR: [auto dependabot: bump handlebars and lerna](https://github.com/microsoft/kiota-typescript/pull/2175)
- [auto dependabot: bump webdriverio from 9.32.0 to 10.0.0 (#2178)](https://github.com/microsoft/kiota-typescript/commit/e1b7bbdb72769e0720ea886a5a0cc658ebc3b683) - `2026-10-13T16:05:49Z` - dependabot[bot] (@dependabot[bot]) - PR: [auto dependabot: bump webdriverio from 9.32.0 to 10.0.0](https://github.com/microsoft/kiota-typescript/pull/2178)

### microsoft/fabric-samples (3 commit(s), signal 43)

Tags: `human-authored, samples`

- [Merge pull request #256 from jagan0506/add-plan-enterprise-dataset](https://github.com/microsoft/fabric-samples/commit/9379bb140202eb4d256f44e2625c80b24c939131) - `2026-10-13T15:48:36Z` - Bailey Anderson (@baanders) - PR: [Add plan enterprise dataset](https://github.com/microsoft/fabric-samples/pull/256)
- [Update Enterprise Dataset sample](https://github.com/microsoft/fabric-samples/commit/24505210a5e615c36d275538ac64ae86ec8249a7) - `2026-10-13T08:25:00Z` - Jagan Rathinam Subramanian (Lumel Technologies Inc) (@jagan0506) - PR: [Add plan enterprise dataset](https://github.com/microsoft/fabric-samples/pull/256)
- [Delete docs-samples/iq/plan/Enterprise Dataset.pbix](https://github.com/microsoft/fabric-samples/commit/b81938c9a83b94379e9236ec79438c9caf3d4a28) - `2026-10-13T06:51:51Z` - jagan0506 (@jagan0506) - PR: [Add plan enterprise dataset](https://github.com/microsoft/fabric-samples/pull/256)

### MicrosoftDocs/cloud-adoption-framework (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/cloud-ad…](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/23b3e3dfa70625106b64a4f2aaeb6d5a569db0a3) - `2026-10-13T14:58:19Z` - Learn Build Service GitHub App
- [Merge pull request #7400 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/d8ba6767081f6306d1ec1e10116161d80528f80b) - `2026-10-13T14:57:10Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Fix Cloudockit links for AWS and Google Cloud services (#7399)](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/58174166d2edb672bd163ede0fd9d939ed44d3f4) - `2026-10-13T14:25:45Z` - Saisang Cai (@Saisang)

### Azure-Samples/azuresandbox (3 commit(s), signal 78)

Tags: `human-authored, product:PowerShell, samples, watchlist`

- [Register Bash and PowerShell Sandbox deployment workflow](https://github.com/Azure-Samples/azuresandbox/commit/fb9c6aa9cea3ab5e385aaa47b0b10e9e3b73e05b) - `2026-10-13T13:54:39Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Register Bash and PowerShell Sandbox deployment workflow](https://github.com/Azure-Samples/azuresandbox/pull/829)
- [Register simplified new-Sandbox deployment workflow on main](https://github.com/Azure-Samples/azuresandbox/commit/559447d62f4756eb92ba3a720d804e3499db44b6) - `2026-10-13T01:50:33Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Register simplified new-Sandbox deployment workflow on main](https://github.com/Azure-Samples/azuresandbox/pull/827)
- [Register three-stage Sandbox deployment workflow on main](https://github.com/Azure-Samples/azuresandbox/commit/cdbe5517b9cf18c8f0ec9d9f396cc7ff199dbdc9) - `2026-10-12T20:53:49Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Register three-stage Sandbox deployment workflow on main](https://github.com/Azure-Samples/azuresandbox/pull/811)

### MicrosoftDocs/microsoft-salescopilot-docs (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/viva-doc…](https://github.com/MicrosoftDocs/microsoft-salescopilot-docs/commit/064d283ccb51b3bb1cdc3b9c6d185264c6560ea4) - `2026-10-13T07:03:00Z` - Learn Build Service GitHub App
- [Merge pull request #594 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/microsoft-salescopilot-docs/commit/fa24ac9aecd41741b97e2fe15776660f2a4babbb) - `2026-10-13T07:02:37Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update introduction.md (#593)](https://github.com/MicrosoftDocs/microsoft-salescopilot-docs/commit/d5d0857e691ffa133fc6b9e8b7ab451888b90db5) - `2026-10-13T05:56:53Z` - Shubham Jaiswal (@sbmjais)

### MicrosoftDocs/msteams-docs (3 commit(s), signal 88)

Tags: `docs, human-authored, product:Azure SDK, release-language, watchlist`

- [Updates to preview-feature article (#14644)](https://github.com/MicrosoftDocs/msteams-docs/commit/9bf6a3e947f6bbb846bfcbee3edd1316d76596d5) - `2026-10-13T03:26:25Z` - Nick Walker (@nickwalkmsft) - PR: [Updates to preview-feature article](https://github.com/MicrosoftDocs/msteams-docs/pull/14644)
- [TOC fixup](https://github.com/MicrosoftDocs/msteams-docs/commit/0d1cd09039bc8eb8341435c9cf92702395d79604) - `2026-10-12T20:13:00Z` - Nick Walker (@nickwalkmsft) - PR: [Auto Publish – main to live - 2026-10-13 15:00 UTC](https://github.com/MicrosoftDocs/msteams-docs/pull/14657)
- [[Doc Improvement] Teams SDK .NET Updates (#14556)](https://github.com/MicrosoftDocs/msteams-docs/commit/d4b03f357d49c5da7439e437b9bfd097ad5e2cc1) - `2026-10-12T20:08:53Z` - SirajShaik-MSFT (@SirajShaik-MSFT) - PR: [[Doc Improvement] Teams SDK .NET Updates](https://github.com/MicrosoftDocs/msteams-docs/pull/14556)

### microsoft/TypeAgent (3 commit(s), signal 78)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Pin GitHub Actions to full-length commit SHAs (#3159)](https://github.com/microsoft/TypeAgent/commit/e2c819c2b0ab10ec5524c4f644abab22e41e097d) - `2026-10-13T02:26:03Z` - Dan Fiedler (@danfiedler-msft) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/microsoft/TypeAgent/pull/3159)
- [Streamline Copilot macro execution with native host launches (#3170)](https://github.com/microsoft/TypeAgent/commit/f01ebe355addf4901b986ec94b81d3850b0d24f0) - `2026-10-13T02:25:11Z` - Hillary Mutisya (@hillary-mutisya) - PR: [Streamline Copilot macro execution with native host launches](https://github.com/microsoft/TypeAgent/pull/3170)
- [Streamline wiki construction (#3171)](https://github.com/microsoft/TypeAgent/commit/54f7b9c7d12dff25e1579d560bd1b5f0920b32ce) - `2026-10-12T20:02:27Z` - Hillary Mutisya (@hillary-mutisya) - PR: [Streamline wiki construction](https://github.com/microsoft/TypeAgent/pull/3171)

### MicrosoftDocs/azure-docs-sdk-node (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [CI Update](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/637ddb3825912678dbbeb85ae5e4cd622dbe2ebf) - `2026-10-13T01:25:50Z` - docsreference@microsoft.com
- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/74daf8511db4d65ea148dfecd070969074d0af6c) - `2026-10-12T23:04:32Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/de048818e0ae0a42da68747d2a1d30df30622886) - `2026-10-12T21:40:13Z` - azure-sdk (@azure-sdk)

### microsoft/aspire-samples (3 commit(s), signal 0)

Tags: `bot-only, dependency-noise, docs`

- [Bump brace-expansion from 5.0.9 to 5.0.12 in /samples/vite-react-fast…](https://github.com/microsoft/aspire-samples/commit/51b114ab5c18f15224225125a2089c34ed913892) - `2026-10-12T20:59:28Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump brace-expansion from 5.0.9 to 5.0.12 in /samples/vite-react-fastapi](https://github.com/microsoft/aspire-samples/pull/2075)
- [Bump source-map-js in /samples/node-express-redis/frontend (#2076)](https://github.com/microsoft/aspire-samples/commit/3b6b9c0f4bec98922037f0911d5de0081d176d79) - `2026-10-12T20:58:16Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump source-map-js from 1.2.1 to 1.2.2 in /samples/node-express-redis/frontend](https://github.com/microsoft/aspire-samples/pull/2076)
- [Bump the orleans group with 3 updates (#2074)](https://github.com/microsoft/aspire-samples/commit/d595aa408a9a724ff377b202e793dd3c5e87269f) - `2026-10-12T20:36:11Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the orleans group with 3 updates](https://github.com/microsoft/aspire-samples/pull/2074)

### Azure/azure-sdk-for-go (2 commit(s), signal 67)

Tags: `bot-only, docs, product:Azure SDK, release, watchlist`

- Release: [sdk/resourcemanager/network/armnetwork/v12.1.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/network/armnetwork/v12.1.0) - `2026-10-13T07:18:39Z`
- Release: [sdk/resourcemanager/commvaultcontentstore/armcommvaultcontentstore/v1.0.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/commvaultcontentstore/armcommvaultcontentstore/v1.0.0) - `2026-10-12T21:09:01Z`
- [Configurations:  'specification/cloudhealth/resource-manager/Microsof…](https://github.com/Azure/azure-sdk-for-go/commit/8fdac475541196d5e68bbd9c6c4c35cc73854bba) - `2026-10-13T19:47:09Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR sdk-resourcemanager/cloudhealth/armcloudhealth]-generated-from-SDK Generation - Go-6884318](https://github.com/Azure/azure-sdk-for-go/pull/27615)
- [[AutoPR sdk-resourcemanager/network/armnetwork]-generated-from-SDK Ge…](https://github.com/Azure/azure-sdk-for-go/commit/9cc935a4b28e52fca447fe3f9b1c6d21ed4f2043) - `2026-10-13T06:31:03Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR sdk-resourcemanager/network/armnetwork]-generated-from-SDK Generation - Go-6948620](https://github.com/Azure/azure-sdk-for-go/pull/27720)

### dotnet/dotnet-api-docs (2 commit(s), signal 42)

Tags: `docs, human-authored`

- [Auto-merge Dependabot PRs (#13164)](https://github.com/dotnet/dotnet-api-docs/commit/52feeaaf1fc783616db48e7921cb5a4a35321124) - `2026-10-13T19:10:43Z` - Genevieve Warren (@gewarren) - PR: [Auto-merge Dependabot PRs](https://github.com/dotnet/dotnet-api-docs/pull/13164)
- [Clarify the browser WebAssembly random number source (#13170)](https://github.com/dotnet/dotnet-api-docs/commit/b3f744389f83f55a54e9d9e4cad4b1fef80f5757) - `2026-10-12T22:33:38Z` - Krzysztof Wicher (@krwq) - PR: [Clarify the browser WebAssembly random number source](https://github.com/dotnet/dotnet-api-docs/pull/13170)

### MicrosoftDocs/VBA-Docs (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Clarify border indexes for Excel conditional formatting (#1970)](https://github.com/MicrosoftDocs/VBA-Docs/commit/604bdf2064c1eb56d723184fff2681bda5aaa348) - `2026-10-13T18:00:54Z` - Alex Jerabek (@AlexJerabek) - PR: [Clarify border indexes for Excel conditional formatting](https://github.com/MicrosoftDocs/VBA-Docs/pull/1970)
- [Clarify that Validation.Value evaluates only the upper-left cell of a…](https://github.com/MicrosoftDocs/VBA-Docs/commit/13ce4d45678fbfa114b2209fbf3831f78918aa71) - `2026-10-13T17:40:55Z` - takazawa-kanji-itso (@takazawa-kanji-itso) - PR: [Clarify that Validation.Value evaluates only the upper-left cell of a range](https://github.com/MicrosoftDocs/VBA-Docs/pull/1969)

### MicrosoftDocs/minecraft-creator (2 commit(s), signal 87)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/minecraf…](https://github.com/MicrosoftDocs/minecraft-creator/commit/b75ceddc27b5523279cf62bcbc8acc059dc65618) - `2026-10-13T16:01:52Z` - Learn Build Service GitHub App
- [Updating reference documentation for 1.26.70-preview.20](https://github.com/MicrosoftDocs/minecraft-creator/commit/2a2b98f698f4b0a61c9ae5d622ac030a121ababd) - `2026-10-13T16:00:47Z` - mcautoma (@mcbuildmsft)

### dotnet/msbuild (2 commit(s), signal 42)

Tags: `docs, human-authored`

- [Use enum for diagnostic subcategories (#15236)](https://github.com/dotnet/msbuild/commit/c1c99ee05981494f34191590eb8ec2e47dba1958) - `2026-10-13T14:58:27Z` - Dustin Campbell (@DustinCampbell) - PR: [Use enum for diagnostic subcategories](https://github.com/dotnet/msbuild/pull/15236)
- [Restore 128 KiB node pipe buffers on .NET Framework (#15253)](https://github.com/dotnet/msbuild/commit/cf642f9dd6a852fbecfef3bf3de986db32bcfd75) - `2026-10-13T08:56:57Z` - AR-May (@AR-May) - PR: [Restore 128 KiB node pipe buffers on .NET Framework](https://github.com/dotnet/msbuild/pull/15253)

### microsoft/copilot-extensibility (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Improved readme](https://github.com/microsoft/copilot-extensibility/commit/b8130014e523034db2e31085e4fbc4c059692688) - `2026-10-13T14:40:34Z` - Paolo Pialorsi (@PaoloPia)
- [Improved featured content](https://github.com/microsoft/copilot-extensibility/commit/720aa7b84733bfec9a4c2ef9bb7b335538e2bf3b) - `2026-10-13T12:58:16Z` - Paolo Pialorsi (@PaoloPia)

### MicrosoftLearning/AB-400-microsoft-power-platform-developer (2 commit(s), signal 77)

Tags: `human-authored, training, watchlist`

- [Merge pull request #1 from skulthm-ms/ab400-labs-01-09](https://github.com/MicrosoftLearning/AB-400-microsoft-power-platform-developer/commit/11b51090157716b510a8e218d0bdbd3dc8bbd4d5) - `2026-10-13T09:53:15Z` - skulthm-ms (@skulthm-ms) - PR: [Add AB-400 setup and lab exercises 01-09](https://github.com/MicrosoftLearning/AB-400-microsoft-power-platform-developer/pull/1)
- [Add AB-400 setup and lab exercises 01-09](https://github.com/MicrosoftLearning/AB-400-microsoft-power-platform-developer/commit/bde4031c70c26be198046230c990a14d1973ee4b) - `2026-10-13T09:17:30Z` - skulthm-ms (@skulthm-ms) - PR: [Add AB-400 setup and lab exercises 01-09](https://github.com/MicrosoftLearning/AB-400-microsoft-power-platform-developer/pull/1)

### MicrosoftDocs/Advertising (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Update CPC (#789)](https://github.com/MicrosoftDocs/Advertising/commit/b36fbbaf3bbdcac5bc4c1e49f6688670e4aeecff) - `2026-10-13T00:05:39Z` - Rick Garitta (@rgaritta)
- [Revise MSClickId performance report filter description (#788)](https://github.com/MicrosoftDocs/Advertising/commit/6c6dd0fee54aae51e504bcb3006f60f695f9e5b6) - `2026-10-12T23:10:35Z` - Rick Garitta (@rgaritta)

### Azure/homebrew-azd (2 commit(s), signal 87)

Tags: `human-authored, product:Azure SDK, release-language, samples, watchlist`

- [Update for azd release 1.36.0-beta.1-daily.6946974](https://github.com/Azure/homebrew-azd/commit/b87e4d743f62fe0957bfe5296a085781a4bdbeb2) - `2026-10-12T21:58:18Z` - azure-sdk (@azure-sdk)
- [Update for azd release 1.36.0-beta.1-daily.6946788](https://github.com/Azure/homebrew-azd/commit/b88fe22f4bbaf0b5c97049c21f7ceedcb1758ce1) - `2026-10-12T21:29:42Z` - azure-sdk (@azure-sdk)

### microsoftgraph/msgraph-snippets-java (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #212 from microsoftgraph/dependabot/gradle/com.azu…](https://github.com/microsoftgraph/msgraph-snippets-java/commit/ce69cfe7421e8c499a06e65f1a1b3cb8f1892a9e) - `2026-10-12T19:49:55Z` - github-actions[bot] (@github-actions[bot]) - PR: [Bump com.azure:azure-identity from 1.18.6 to 1.18.7](https://github.com/microsoftgraph/msgraph-snippets-java/pull/212)
- [Bump com.azure:azure-identity from 1.18.6 to 1.18.7](https://github.com/microsoftgraph/msgraph-snippets-java/commit/c5022b5fbbef80154d988e32e3804bb33ef46a36) - `2026-10-12T19:48:30Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump com.azure:azure-identity from 1.18.6 to 1.18.7](https://github.com/microsoftgraph/msgraph-snippets-java/pull/212)

### Azure/LogicAppsUX (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [feat(designer): prototype local workflow extraction (#9657)](https://github.com/Azure/LogicAppsUX/commit/328a2543863484f1e41358b649bfdbb24c9ed7f2) - `2026-10-13T19:46:43Z` - Riley Evans (@rllyy97) - PR: [feat(DesignerV2): Child workflow extraction setup](https://github.com/Azure/LogicAppsUX/pull/9657)

### Azure/iot-operations-sdks (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Rework cross-language pipeline to use WoT codegen output (#1523)](https://github.com/Azure/iot-operations-sdks/commit/6b59d8be0feefdb90e3a0c8a1a57ff31f9f9cf76) - `2026-10-13T19:20:38Z` - Tim Taylor (@timtay-microsoft) - PR: [Rework cross-language pipeline to use WoT codegen output](https://github.com/Azure/iot-operations-sdks/pull/1523)

### dotnet/efcore (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Use CreateTempSubdirectory for temporary directories (#39233)](https://github.com/dotnet/efcore/commit/2c982ae264554eb66a1a045b0d91ed55e34e4fa8) - `2026-10-13T18:41:59Z` - Copilot (@Copilot) - PR: [Use CreateTempSubdirectory for temporary directories](https://github.com/dotnet/efcore/pull/39233)

### microsoft/mu_oem_sample (1 commit(s), signal 0)

Tags: `bot-only, samples`

- [Repo File Sync: Change "GCC5" to "GCC" in bug_report.yml (#377)](https://github.com/microsoft/mu_oem_sample/commit/e66765da7723de3f42cab48c3d556d765eb6d3ec) - `2026-10-13T18:34:25Z` - mu-automation[bot] (@mu-automation[bot]) - PR: [Repo File Sync: Change "GCC5" to "GCC" in bug_report.yml](https://github.com/microsoft/mu_oem_sample/pull/377)

### microsoft/Aion-Instruct-Preview-Sample (1 commit(s), signal 86)

Tags: `human-authored, product:PowerShell, release-language, samples, watchlist`

- [Make the WinUI app per-monitor DPI aware (#13)](https://github.com/microsoft/Aion-Instruct-Preview-Sample/commit/e0c736f55199891d801f5fae18f711d42133ce7b) - `2026-10-13T18:24:40Z` - Erin Genovy (@jefgen) - PR: [Make the WinUI app per-monitor DPI aware](https://github.com/microsoft/Aion-Instruct-Preview-Sample/pull/13)

### OfficeDev/office-js-docs-reference (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Remove dictionary-specific manifest reference (#2643)](https://github.com/OfficeDev/office-js-docs-reference/commit/26ceb9d262912f6ba4f6062044e8bcbf84f5b6ec) - `2026-10-13T17:58:41Z` - Alex Jerabek (@AlexJerabek) - PR: [Remove dictionary-specific manifest reference](https://github.com/OfficeDev/office-js-docs-reference/pull/2643)

### microsoft/PowerApps-Samples (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Demonstrate density-aware theme spacing (#820)](https://github.com/microsoft/PowerApps-Samples/commit/8e42f87026f4c93d7e468f28416f5852375d325a) - `2026-10-13T17:49:09Z` - Jason Green (@jasongre) - PR: [Demonstrate density-aware theme spacing](https://github.com/microsoft/PowerApps-Samples/pull/820)

### MicrosoftDocs/m365copilot-docs (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Microsoft Graph, watchlist`

- [Document Work IQ MCP retrieve tool and migration (#126)](https://github.com/MicrosoftDocs/m365copilot-docs/commit/8f8ccb55eae7547c415defdffc5b241af93825ec) - `2026-10-13T17:46:29Z` - MSFTgraph-sorceress (@MSFTgraph-sorceress) - PR: [Document Work IQ MCP retrieve tool and migration](https://github.com/MicrosoftDocs/m365copilot-docs/pull/126)

### Azure-Samples/quote-of-the-day-dotnet (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add OpenTelemetry Sample](https://github.com/Azure-Samples/quote-of-the-day-dotnet/commit/33a47b582b23ee103727ef13c66c2b624252fba8) - `2026-10-13T17:44:00Z` - Yuan Qu (@yuanqu72) - PR: [Add OpenTelemetry Sample](https://github.com/Azure-Samples/quote-of-the-day-dotnet/pull/24)

### Azure/setup-azd (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, samples, watchlist`

- [build(deps-dev): bump the minor-and-patch group with 5 updates (#628)](https://github.com/Azure/setup-azd/commit/2ed4c2d9bf930768275b6568a7ae9b1e4573cc5d) - `2026-10-13T17:41:16Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps-dev): bump the minor-and-patch group with 5 updates](https://github.com/Azure/setup-azd/pull/628)

### OfficeDev/office-js-snippets (1 commit(s), signal 41)

Tags: `human-authored, training`

- [Expand Word tracked change collection sample (#1133)](https://github.com/OfficeDev/office-js-snippets/commit/8913e2a6a7650259d0c35e511aa5d4c38a0fff6b) - `2026-10-13T16:24:08Z` - Alex Jerabek (@AlexJerabek) - PR: [Expand Word.TrackedChangeCollection sample coverage](https://github.com/OfficeDev/office-js-snippets/pull/1133)

### MicrosoftDocs/edge-developer (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Removing the stale flag from the documentation (#3977)](https://github.com/MicrosoftDocs/edge-developer/commit/dc4de8050e17ed1e6d0f07e449fbf01301507711) - `2026-10-13T14:42:24Z` - GarimaSoni142-coder (@GarimaSoni142-coder) - PR: [Remove 'js-flags' from "WebView2 browser flags"](https://github.com/MicrosoftDocs/edge-developer/pull/3977)

### microsoft/dbt-fabricspark (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [fix: poll only the submitted native table (#308)](https://github.com/microsoft/dbt-fabricspark/commit/91a39609821869cb0998b66cfdde404ef1b55fd0) - `2026-10-13T14:18:48Z` - Raki (@mdrakiburrahman) - PR: [fix: poll only the submitted native table](https://github.com/microsoft/dbt-fabricspark/pull/308)

### Azure-Samples/ms-identity-extid-cors-proxy-function (1 commit(s), signal 76)

Tags: `human-authored, product:Azure SDK, samples, watchlist`

- [Merge pull request #13 from Azure-Samples/yongdi/native-auth-v2](https://github.com/Azure-Samples/ms-identity-extid-cors-proxy-function/commit/6847eff5e68f903c20e6814b53ff67882730b583) - `2026-10-13T13:24:50Z` - Yongdi Wang (@yongdiw) - PR: [Support Native Authentication V2 requests](https://github.com/Azure-Samples/ms-identity-extid-cors-proxy-function/pull/13)

### microsoft/vscode-docs (1 commit(s), signal 86)

Tags: `docs, human-authored, release-language, watchlist`

- [Recovery release 1.141.1 (#10467)](https://github.com/microsoft/vscode-docs/commit/78bab45f23b0d863f9545c29f36832da3824f48c) - `2026-10-13T12:54:47Z` - Nick Trogh (@ntrogh) - PR: [Recovery release 1.141.1](https://github.com/microsoft/vscode-docs/pull/10467)

### microsoft/voice-agent (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Add Java live audio voice agent sample (#36)](https://github.com/microsoft/voice-agent/commit/d24db8bb90c6d83b6eddb84e8494b0a087a11e4a) - `2026-10-13T12:54:44Z` - Mike Guo (@guotuofeng) - PR: [Add Java live audio voice agent sample](https://github.com/microsoft/voice-agent/pull/36)

### Azure/AI-Landing-Zones (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [docs: clarify custom hosted foundation preparation (#153)](https://github.com/Azure/AI-Landing-Zones/commit/7a82cda5af2c30ff6d89af7425ff617406896d73) - `2026-10-13T12:42:04Z` - Paulo Lacerda (@placerda) - PR: [docs: clarify custom hosted foundation preparation](https://github.com/Azure/AI-Landing-Zones/pull/153)

### MicrosoftDocs/azure-docs-cli (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [CI Update](https://github.com/MicrosoftDocs/azure-docs-cli/commit/541c74755f7078f784973edafa398af5ef0e2f48) - `2026-10-13T12:41:57Z` - docsreference@microsoft.com

### Azure/terraform-azurerm-avm-res-devtestlab-lab (1 commit(s), signal 76)

Tags: `human-authored, training, watchlist`

- [chore: refresh DevTest Lab starter from Avm.Authoring 0.23.0 (#73)](https://github.com/Azure/terraform-azurerm-avm-res-devtestlab-lab/commit/63ea40b8ab1e82a8b9a56f5aad7538afce459bf3) - `2026-10-13T12:14:10Z` - Jared Holgate (@jaredfholgate) - PR: [chore: refresh DevTest Lab starter from Avm.Authoring 0.23.0](https://github.com/Azure/terraform-azurerm-avm-res-devtestlab-lab/pull/73)

### microsoft/AzureTRE (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Improve operation retrieval and Airlock request handling (#5251)](https://github.com/microsoft/AzureTRE/commit/c8203b84bef541ad24ad40b6a843761097ffde64) - `2026-10-13T11:17:53Z` - Jay W (@JayDoubleu) - PR: [Improve operation retrieval and Airlock request handling](https://github.com/microsoft/AzureTRE/pull/5251)

### dotnet/docs-mobile (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Merge pull request #142 from vitek-karas/vitkaras-microsoft-sync-maci…](https://github.com/dotnet/docs-mobile/commit/f5db3c217bf3b3b70fc0edf5f8a470fa20afc1fa) - `2026-10-13T08:59:46Z` - Gerald Versluis (@jfversluis) - PR: [Clarify .NET 11 runtime-specific build properties for iOS, tvOS, Mac Catalyst, and macOS](https://github.com/dotnet/docs-mobile/pull/142)

### Azure-Samples/iot-edge-opc-plc (1 commit(s), signal 81)

Tags: `human-authored, release, samples`

- Release: [2.15.11](https://github.com/Azure-Samples/iot-edge-opc-plc/releases/tag/2.15.11) - `2026-10-13T06:48:41Z`
- [Bump OPC UA stack to 1.5.378.182 and PLC to 2.15.11 (#555)](https://github.com/Azure-Samples/iot-edge-opc-plc/commit/d8e1ea6bd2916d96396ef8599ca991809fbacf70) - `2026-10-13T06:36:30Z` - Cristi Pogacean (@cristipogacean) - PR: [Bump OPC UA stack to 1.5.378.182 and PLC to 2.15.11](https://github.com/Azure-Samples/iot-edge-opc-plc/pull/555)

### OfficeDev/Microsoft-Teams-Samples (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Pin GitHub Actions to full-length commit SHAs (#2399)](https://github.com/OfficeDev/Microsoft-Teams-Samples/commit/ea5c649e25fab773c64548b9074b9274728b0557) - `2026-10-13T05:41:41Z` - Dan Fiedler (@danfiedler-msft) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/OfficeDev/Microsoft-Teams-Samples/pull/2399)

### microsoft/mcp-dotnet-samples (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Update metadata.json](https://github.com/microsoft/mcp-dotnet-samples/commit/d56fa1f44767085f24a9a837a364023be753e6fe) - `2026-10-13T05:18:30Z` - GitHub Actions (@actions-user)

### microsoft/amplifier-module-provider-anthropic (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [feat: compile provider-owned neutral computer-use intent (#137)](https://github.com/microsoft/amplifier-module-provider-anthropic/commit/9f9c50c040a2d5f4f24e2f7b9d196d30bf54608b) - `2026-10-13T02:25:53Z` - Brian Krabach (@bkrabach) - PR: [feat: compile provider-owned neutral computer-use intent](https://github.com/microsoft/amplifier-module-provider-anthropic/pull/137)

### microsoft/fabric-terraform-quickstart (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, samples`

- [build(deps): bump the all group across 3 directories with 3 updates (…](https://github.com/microsoft/fabric-terraform-quickstart/commit/380d42af0f27bb6de7ae502571a6b1add9d27cdf) - `2026-10-13T01:16:55Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump the all group across 3 directories with 3 updates](https://github.com/microsoft/fabric-terraform-quickstart/pull/273)

### MicrosoftDocs/azure-docs-sdk-cpp (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-cpp/commit/ac8915ebdab037a32bb9200e5b49d80db807259e) - `2026-10-12T23:17:28Z` - azure-sdk (@azure-sdk)

### dotnet/docs-actions (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Add directory exclusions to docs verifier config (#26)](https://github.com/dotnet/docs-actions/commit/ee93453f8ce383d3fdf0d1028ea57ba88ea2ad24) - `2026-10-12T23:11:20Z` - Genevieve Warren (@gewarren) - PR: [Add directory exclusions to docs verifier config](https://github.com/dotnet/docs-actions/pull/26)

### microsoft/amplifier-module-provider-openai (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [feat: compile provider-neutral computer intent and preserve native im…](https://github.com/microsoft/amplifier-module-provider-openai/commit/38fee172673d196ba54b5e99e434490b86290c5d) - `2026-10-12T22:36:36Z` - Brian Krabach (@bkrabach) - PR: [feat: compile provider-neutral computer intent and preserve native image replay](https://github.com/microsoft/amplifier-module-provider-openai/pull/128)

### microsoft/playwright.dev (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, docs`

- [chore(deps): bump fast-uri from 3.1.7 to 3.1.8 (#2168)](https://github.com/microsoft/playwright.dev/commit/c6b1fb811e88f158de7c84d8800f26a088d25411) - `2026-10-12T22:34:46Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump fast-uri from 3.1.7 to 3.1.8](https://github.com/microsoft/playwright.dev/pull/2168)

### microsoft/amplifier-app-cli (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [feat: add process-local startup update check opt-out (#371)](https://github.com/microsoft/amplifier-app-cli/commit/d408797459a012e064be2330b159bf7b3192b57c) - `2026-10-12T21:30:33Z` - Brian Krabach (@bkrabach) - PR: [feat: add process-local startup update check opt-out](https://github.com/microsoft/amplifier-app-cli/pull/371)

### microsoft/SPARROW (1 commit(s), signal 41)

Tags: `human-authored, training`

- [Merge pull request #81 from microsoft/dependabot/github_actions/githu…](https://github.com/microsoft/SPARROW/commit/27e55a4a200c0e9bb1b9fb30629535097d6c154e) - `2026-10-12T21:16:10Z` - Federico Alves (@urucoder) - PR: [chore(deps): bump the github-actions group with 2 updates](https://github.com/microsoft/SPARROW/pull/81)

### Azure-Samples/azure-search-sample-data (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Add Microsoft earnings-call transcript dataset (#47)](https://github.com/Azure-Samples/azure-search-sample-data/commit/902329750c49e376a164b5f382c85ea01761f2b6) - `2026-10-12T21:02:59Z` - Matt (@mattgotteiner) - PR: [Add Microsoft earnings-call transcript dataset](https://github.com/Azure-Samples/azure-search-sample-data/pull/47)

### microsoft/kiota (1 commit(s), signal 86)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release-language, watchlist`

- [reducing logo size to 1024x1024 (#8393)](https://github.com/microsoft/kiota/commit/893f61af8adcf459a5b67e5705e26a043b711c41) - `2026-10-12T21:02:17Z` - Adrian (@adrian05-ms) - PR: [fix: reducing logo size to 1024x1024 for vscode marketplace release](https://github.com/microsoft/kiota/pull/8393)

### Azure/azure-policy (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, samples, watchlist`

- [Bump brace-expansion (#1613)](https://github.com/Azure/azure-policy/commit/184a951ee59050e19d6e9b5db894383528cb86f3) - `2026-10-12T20:54:41Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump brace-expansion](https://github.com/Azure/azure-policy/pull/1613)

### microsoft/BuildXL (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Merged PR 964337: [MSBuild resolver] Make the dotnet core case honor …](https://github.com/microsoft/BuildXL/commit/62d510c31d5c7ded13857b0313850d100c31fe04) - `2026-10-12T20:41:35Z` - Serge Mera (@smera)

### Azure/awesome-azd (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Remove inaccessible MarketingWriter template (#1026)](https://github.com/Azure/awesome-azd/commit/36849f8fc2825f014ad8d5099cc49005eb5892d3) - `2026-10-12T20:27:35Z` - Copilot (@Copilot) - PR: [Remove inaccessible MarketingWriter template](https://github.com/Azure/awesome-azd/pull/1026)

</details>
