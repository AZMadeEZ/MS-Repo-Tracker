# Microsoft Ecosystem Daily Brief - 2026-10-16

> Status: Fresh at generation. Current freshness is tracked in `reports/status.json`.
> Generated: 2026-10-16 17:32 UTC - Window: 25.7h from 2026-10-15 15:49 UTC to 2026-10-16 17:32 UTC.
> 118 repo(s) moved - 721 commit(s) - 36 release item(s) - 25 high-signal repo(s).

## Plain-English Summary

- Azure, Microsoft Graph led the visible product-area activity in this window.
- 36 release item(s) were detected during the window.
- Security-related changes appeared in MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect, Azure/azure-devops-cli-extension, MicrosoftDocs/entra-docs.
- Start with human-authored changes in MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect, Azure/azure-devops-cli-extension, MicrosoftDocs/entra-docs, Azure-Samples/azuresandbox.
- 133 event(s) look automated, bot-heavy, dependency, or generated; review the curated sections before raw volume.

## Headline Metrics

| Metric | Value |
| --- | ---: |
| Inventory repositories | 16712 |
| Repositories after filters | 2630 |
| `pushed_at` candidates | 183 |
| Enrichment candidates | 183 |
| Repositories with movement | 118 |
| Default-branch commits | 721 |

## What Changed That Matters

| Repository | Score | Change | Actor | Noise | Headline | Time |
| --- | ---: | --- | --- | --- | --- | --- |
| [MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect) | 100 | security_fix | human | low | [Update user selection instructions in lab document](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect/pull/92) | `2026-10-16T16:53:00Z` |
| [MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect) | 100 | security_fix | human | low | [Update retention policy settings terminology](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect/pull/93) | `2026-10-16T16:52:29Z` |
| [Azure/azure-devops-cli-extension](https://github.com/Azure/azure-devops-cli-extension) | 100 | security_fix | human | low | [Harden credential store file permissions](https://github.com/Azure/azure-devops-cli-extension/pull/1526) | `2026-10-16T05:14:59Z` |
| [MicrosoftDocs/entra-docs](https://github.com/MicrosoftDocs/entra-docs) | 100 | security_fix | human | low | [Remove section on managing individual Security Defaults (#14618)](https://github.com/MicrosoftDocs/entra-docs/commit/23c29f0c416703762a4953f1cf99d8c0b5fb056b) | `2026-10-16T03:33:15Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 100 | release | unknown | low | [@azure/arm-cognitiveservices_9.0.0-beta.5](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-cognitiveservices_9.0.0-beta.5) | `2026-10-16T17:29:39Z` |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 100 | release | human | low | [Register release static CI gating on main (#854)](https://github.com/Azure-Samples/azuresandbox/pull/857) | `2026-10-16T17:12:17Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 100 | release | unknown | low | [com.azure.resourcemanager+azure-resourcemanager-cloudhealth_1.0.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-cloudhealth_1.0.0) | `2026-10-16T16:48:32Z` |
| [microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-abstractions-go) | 100 | release | unknown | low | [v1.11.2](https://github.com/microsoft/kiota-abstractions-go/releases/tag/v1.11.2) | `2026-10-16T16:27:46Z` |
| [microsoft/kiota-serialization-json-go](https://github.com/microsoft/kiota-serialization-json-go) | 100 | release | unknown | low | [v1.1.5](https://github.com/microsoft/kiota-serialization-json-go/releases/tag/v1.1.5) | `2026-10-16T16:22:47Z` |
| [microsoft/kiota-serialization-json-go](https://github.com/microsoft/kiota-serialization-json-go) | 100 | release | human | low | [chore(main): release 1.1.5](https://github.com/microsoft/kiota-serialization-json-go/pull/223) | `2026-10-16T16:22:20Z` |
| [microsoft/kiota-serialization-text-go](https://github.com/microsoft/kiota-serialization-text-go) | 100 | release | unknown | low | [v1.1.4](https://github.com/microsoft/kiota-serialization-text-go/releases/tag/v1.1.4) | `2026-10-16T16:18:35Z` |
| [microsoft/pylance-release](https://github.com/microsoft/pylance-release) | 100 | release | unknown | low | [2026.4.101](https://github.com/microsoft/pylance-release/releases/tag/2026.4.101) | `2026-10-16T16:18:15Z` |
| [microsoft/kiota-http-go](https://github.com/microsoft/kiota-http-go) | 100 | release | unknown | low | [v1.5.8](https://github.com/microsoft/kiota-http-go/releases/tag/v1.5.8) | `2026-10-16T16:18:12Z` |
| [microsoft/kiota-serialization-text-go](https://github.com/microsoft/kiota-serialization-text-go) | 100 | release | human | low | [chore(main): release 1.1.4](https://github.com/microsoft/kiota-serialization-text-go/pull/168) | `2026-10-16T16:18:11Z` |
| [microsoft/kiota-http-go](https://github.com/microsoft/kiota-http-go) | 100 | release | human | low | [chore(main): release 1.5.8](https://github.com/microsoft/kiota-http-go/pull/280) | `2026-10-16T16:17:43Z` |

## Product Areas

| Product area | Signal | Repos | Events | Releases | Security | Top links |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Azure | 143 | 47 | 182 | 31 | 1 | [Harden credential store file permissions](https://github.com/Azure/azure-devops-cli-extension/pull/1526); [@azure/arm-cognitiveservices_9.0.0-beta.5](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-cognitiveservices_9.0.0-beta.5); [Register release static CI gating on main (#854)](https://github.com/Azure-Samples/azuresandbox/pull/857) |
| Unmapped Activity | 78 | 30 | 94 | 1 | 2 | [Update user selection instructions in lab document](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect/pull/92); [Update retention policy settings terminology](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect/pull/93); [2026.4.101](https://github.com/microsoft/pylance-release/releases/tag/2026.4.101) |
| Microsoft Graph | 28 | 11 | 38 | 4 | 0 | [v1.11.2](https://github.com/microsoft/kiota-abstractions-go/releases/tag/v1.11.2); [v1.1.5](https://github.com/microsoft/kiota-serialization-json-go/releases/tag/v1.1.5); [chore(main): release 1.1.5](https://github.com/microsoft/kiota-serialization-json-go/pull/223) |
| .NET | 23 | 14 | 40 | 0 | 0 | [Update FBA sources. Add --sdk-branch script param.](https://github.com/dotnet/roslyn/pull/86080); [Clarify Linux-only extended support for .NET SDK feature bands](https://github.com/dotnet/docs/pull/56414); [Fix IDE0330 not reported when type contains multi-declarator fields](https://github.com/dotnet/roslyn/pull/86077) |
| PowerShell | 10 | 3 | 10 | 0 | 0 | [feat(agents): add ftk-cos, ftk-release-manager, and ftk-support agents](https://github.com/microsoft/finops-toolkit/pull/2340); [Add Power Platform Admin Cowork setup article (#12031)](https://github.com/MicrosoftDocs/power-platform/commit/70452520e898bb4a4dd33e1e0f33b2aff5ea37ce); [Q1 Governance - Add knowledge sources for agents rule and data policy…](https://github.com/MicrosoftDocs/power-platform/commit/1441cc222fef2a8af2d4b618da57831455284c20) |
| Developer Tools | 8 | 3 | 13 | 0 | 0 | [Restructure MCP content for readability](https://github.com/microsoft/vscode-docs/pull/10497); [Refresh Custom Agents article for correctness and structure](https://github.com/microsoft/vscode-docs/pull/10495); [chore: update netiso policy](https://github.com/microsoft/vscode-docs/pull/10494) |
| Identity | 5 | 1 | 5 | 0 | 1 | [Remove section on managing individual Security Defaults (#14618)](https://github.com/MicrosoftDocs/entra-docs/commit/23c29f0c416703762a4953f1cf99d8c0b5fb056b); [docs: use primary tenant domain in External ID user creation example …](https://github.com/MicrosoftDocs/entra-docs/commit/15df35364c0d4457108f9c1d6917824131eb3f61); [Route invited users to an external identity provider with domain_hint…](https://github.com/MicrosoftDocs/entra-docs/commit/4df42e6f03f5fd9bff11e32579428a97601c47ee) |
| Windows | 5 | 4 | 6 | 0 | 0 | [Add some cleanup actions to the policy bot](https://github.com/microsoft/WindowsAppSDK/pull/6851); [Add Reactor single-file app template (reactor-singlefile)](https://github.com/microsoft/WindowsAppSDK/pull/6844); [Added WSLc settings](https://github.com/MicrosoftDocs/WSL/pull/2641) |

## Today's Top Links

| Priority | Repository | Why read it |
| ---: | --- | --- |
| 1 | [MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect) | [Security-related change: Update user selection instructions in lab document](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect/pull/92) |
| 2 | [Azure/azure-devops-cli-extension](https://github.com/Azure/azure-devops-cli-extension) | [Security-related change: Harden credential store file permissions](https://github.com/Azure/azure-devops-cli-extension/pull/1526) |
| 3 | [MicrosoftDocs/entra-docs](https://github.com/MicrosoftDocs/entra-docs) | [Security-related change: Remove section on managing individual Security Defaults (#14618)](https://github.com/MicrosoftDocs/entra-docs/commit/23c29f0c416703762a4953f1cf99d8c0b5fb056b) |
| 4 | [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [Release activity: @azure/arm-cognitiveservices_9.0.0-beta.5](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-cognitiveservices_9.0.0-beta.5) |
| 5 | [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | [Release activity: Register release static CI gating on main (#854)](https://github.com/Azure-Samples/azuresandbox/pull/857) |
| 6 | [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [Release activity: com.azure.resourcemanager+azure-resourcemanager-cloudhealth_1.0.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-cloudhealth_1.0.0) |
| 7 | [microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-abstractions-go) | [Release activity: v1.11.2](https://github.com/microsoft/kiota-abstractions-go/releases/tag/v1.11.2) |
| 8 | [microsoft/kiota-serialization-json-go](https://github.com/microsoft/kiota-serialization-json-go) | [Release activity: v1.1.5](https://github.com/microsoft/kiota-serialization-json-go/releases/tag/v1.1.5) |

## Noise and Automation

- 133 event(s) look automated, bot-heavy, dependency, generated, or medium/high noise.
- Top noisy repositories: Azure/azure-sdk-for-go, microsoft/kiota-python, MicrosoftDocs/azure-aks-docs, Azure/azure-sdk-for-java, Azure/azure-sdk-for-python.
- Noise mix: Docs: 56, Dependency: 35, SDK: 25, Release: 7, CI/Infra: 6, Automation: 2, Sample: 1, Training: 1.

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
| Repos counted | 183 |
| Repos enriched | 118 |

</details>

<details>
<summary>Show supporting signal, release, and lifecycle tables</summary>

## High-Signal Items

| Repository | Score | Tags |
| --- | ---: | --- |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 150 | docs, human-authored, product:Azure AI, product:Azure SDK, release, release-language, watchlist |
| [Azure/azure-devops-cli-extension](https://github.com/Azure/azure-devops-cli-extension) | 141 | docs, human-authored, release, security, watchlist |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 139 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 137 | docs, human-authored, product:Azure SDK, release, release-language, watchlist |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 135 | docs, human-authored, product:Azure AI, product:Azure SDK, release, release-language, watchlist |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 134 | docs, human-authored, release, release-language, watchlist |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 133 | human-authored, product:Azure AI, product:Azure SDK, release, release-language, samples, watchlist |
| [microsoft/kiota-serialization-text-go](https://github.com/microsoft/kiota-serialization-text-go) | 129 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [microsoft/kiota-serialization-json-go](https://github.com/microsoft/kiota-serialization-json-go) | 129 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [microsoft/kiota-http-go](https://github.com/microsoft/kiota-http-go) | 129 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [microsoft/pylance-release](https://github.com/microsoft/pylance-release) | 127 | docs, human-authored, release, release-language, watchlist |
| [microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-abstractions-go) | 127 | docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 127 | human-authored, release, release-language, samples, watchlist |
| [Azure/azure-sdk-for-cpp](https://github.com/Azure/azure-sdk-for-cpp) | 117 | docs, human-authored, product:Azure SDK, release, watchlist |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 117 | docs, human-authored, release, watchlist |

## Watchlist Hits

| Repository | Score | Matches |
| --- | ---: | --- |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 150 | products: Azure AI, Azure SDK; repos: Azure/azure-sdk-for-net; orgs: Azure; keywords: agent, release, sdk |
| [Azure/azure-devops-cli-extension](https://github.com/Azure/azure-devops-cli-extension) | 141 | orgs: Azure |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 139 | products: Azure SDK; repos: Azure/azure-sdk-for-js; orgs: Azure; keywords: sdk |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 137 | products: Azure SDK; repos: Azure/azure-sdk-for-java; orgs: Azure; keywords: release, sdk |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 135 | products: Azure AI, Azure SDK; repos: Azure/azure-sdk-for-python; orgs: Azure; keywords: agent, release, sdk |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 134 | orgs: Azure; keywords: release |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 133 | products: Azure AI, Azure SDK; orgs: Azure; keywords: azure ai, azure sdk, foundry, release, sdk |
| [microsoft/kiota-serialization-text-go](https://github.com/microsoft/kiota-serialization-text-go) | 129 | products: Microsoft Graph, Azure SDK; keywords: graph, kiota, release, sdk |
| [microsoft/kiota-serialization-json-go](https://github.com/microsoft/kiota-serialization-json-go) | 129 | products: Microsoft Graph, Azure SDK; keywords: graph, kiota, release, sdk |
| [microsoft/kiota-http-go](https://github.com/microsoft/kiota-http-go) | 129 | products: Microsoft Graph, Azure SDK; keywords: graph, kiota, release, sdk |
| [microsoft/pylance-release](https://github.com/microsoft/pylance-release) | 127 | keywords: release |
| [microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-abstractions-go) | 127 | products: Microsoft Graph, Azure SDK; keywords: graph, kiota, release, sdk |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 127 | keywords: release |
| [Azure/azure-sdk-for-cpp](https://github.com/Azure/azure-sdk-for-cpp) | 117 | products: Azure SDK; orgs: Azure; keywords: sdk |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 117 | orgs: Azure |

## Releases

| Repository | Release | Published |
| --- | --- | --- |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-cognitiveservices_9.0.0-beta.5](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-cognitiveservices_9.0.0-beta.5) | `2026-10-16T17:29:39Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure.resourcemanager+azure-resourcemanager-cloudhealth_1.0.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-cloudhealth_1.0.0) | `2026-10-16T16:48:32Z` |
| [microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-abstractions-go) | [v1.11.2](https://github.com/microsoft/kiota-abstractions-go/releases/tag/v1.11.2) | `2026-10-16T16:27:46Z` |
| [microsoft/kiota-serialization-json-go](https://github.com/microsoft/kiota-serialization-json-go) | [v1.1.5](https://github.com/microsoft/kiota-serialization-json-go/releases/tag/v1.1.5) | `2026-10-16T16:22:47Z` |
| [microsoft/kiota-serialization-text-go](https://github.com/microsoft/kiota-serialization-text-go) | [v1.1.4](https://github.com/microsoft/kiota-serialization-text-go/releases/tag/v1.1.4) | `2026-10-16T16:18:35Z` |
| [microsoft/pylance-release](https://github.com/microsoft/pylance-release) | [2026.4.101](https://github.com/microsoft/pylance-release/releases/tag/2026.4.101) | `2026-10-16T16:18:15Z` |
| [microsoft/kiota-http-go](https://github.com/microsoft/kiota-http-go) | [v1.5.8](https://github.com/microsoft/kiota-http-go/releases/tag/v1.5.8) | `2026-10-16T16:18:12Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/resourcemanager/cloudhealth/armcloudhealth/v1.0.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/cloudhealth/armcloudhealth/v1.0.0) | `2026-10-16T16:09:13Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-cloudhealth_1.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-cloudhealth_1.0.0) | `2026-10-16T16:04:41Z` |
| [Azure/azure-sdk-for-cpp](https://github.com/Azure/azure-sdk-for-cpp) | [azure-template_1.1.0-beta.6967811](https://github.com/Azure/azure-sdk-for-cpp/releases/tag/azure-template_1.1.0-beta.6967811) | `2026-10-16T15:54:09Z` |
| [Azure/azure-sdk-for-cpp](https://github.com/Azure/azure-sdk-for-cpp) | [azure-template_1.1.0-beta.6967166](https://github.com/Azure/azure-sdk-for-cpp/releases/tag/azure-template_1.1.0-beta.6967166) | `2026-10-16T13:32:16Z` |
| [Azure/azure-devops-cli-extension](https://github.com/Azure/azure-devops-cli-extension) | [Azure DevOps CLI extension for Azure CLI 1.0.10](https://github.com/Azure/azure-devops-cli-extension/releases/tag/20261015.1) | `2026-10-16T10:35:35Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.Provisioning.Storage_1.2.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Provisioning.Storage_1.2.0) | `2026-10-16T08:49:55Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-mgmt-azurestackhci_8.2.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-azurestackhci_8.2.0) | `2026-10-16T08:30:05Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-azurestackhci_4.2.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-azurestackhci_4.2.0) | `2026-10-16T07:47:50Z` |
| [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go) | [sdk/resourcemanager/azurestackhci/armazurestackhci/v3.2.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/azurestackhci/armazurestackhci/v3.2.0) | `2026-10-16T07:30:47Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-ai-agentserver-responses_2.4.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-responses_2.4.0b1) | `2026-10-16T07:18:15Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.ResourceManager.KeyVault_1.5.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.KeyVault_1.5.0) | `2026-10-16T07:09:50Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.AI.AgentServer.Responses_1.0.0-beta.9](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.AI.AgentServer.Responses_1.0.0-beta.9) | `2026-10-16T06:37:36Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-ai-agentserver-core_2.3.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-core_2.3.0b1) | `2026-10-16T06:31:15Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | [oracle-database 3.0.1](https://github.com/Azure/azure-cli-extensions/releases/tag/oracle-database-3.0.1) | `2026-10-16T06:18:11Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.AI.AgentServer.Core_1.0.0-beta.30](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.AI.AgentServer.Core_1.0.0-beta.30) | `2026-10-16T05:56:13Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | [azure-mgmt-recoveryservicesbackup_11.2.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-recoveryservicesbackup_11.2.0) | `2026-10-16T05:48:55Z` |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.ResourceManager.Compute.WorkloadManager_1.0.0-beta.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.Compute.WorkloadManager_1.0.0-beta.1) | `2026-10-16T05:26:48Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | [@azure/arm-recoveryservicesbackup_15.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-recoveryservicesbackup_15.0.0) | `2026-10-16T04:08:36Z` |

## Repository Lifecycle

| Change | Count |
| --- | ---: |
| archived_changed | 2 |
| category_changed | 0 |
| default_branch_changed | 1 |
| fork_changed | 0 |
| new_repos | 19 |
| removed_repos | 0 |

## Recently Created Repositories

| Repository | Category | Created |
| --- | --- | --- |
| [Azure-Samples/azure-sre-agent-vm-anomaly-detection](https://github.com/Azure-Samples/azure-sre-agent-vm-anomaly-detection) | samples | `2026-10-16T02:02:02Z` |

## Category Summary

| Category | Repositories |
| --- | ---: |
| docs | 87 |
| samples | 23 |
| training | 8 |

## Organization Summary

| Org | Repositories |
| --- | ---: |
| MicrosoftDocs | 38 |
| microsoft | 33 |
| Azure | 18 |
| dotnet | 13 |
| Azure-Samples | 8 |
| MicrosoftLearning | 4 |
| OfficeDev | 3 |
| microsoftgraph | 1 |

</details>

<details>
<summary>Show raw repository activity</summary>

## Busiest Repositories

| Repository | Signal | Category | Commits | Releases | Newest commit |
| --- | ---: | --- | ---: | ---: | --- |
| [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | 150 | docs | 28 | 5 | `2026-10-16T16:57:21Z` |
| [Azure/azure-devops-cli-extension](https://github.com/Azure/azure-devops-cli-extension) | 141 | docs | 1 | 1 | `2026-10-16T05:14:59Z` |
| [Azure/azure-sdk-for-js](https://github.com/Azure/azure-sdk-for-js) | 139 | docs | 14 | 4 | `2026-10-16T16:42:40Z` |
| [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | 137 | docs | 12 | 3 | `2026-10-16T16:47:10Z` |
| [Azure/azure-sdk-for-python](https://github.com/Azure/azure-sdk-for-python) | 135 | docs | 10 | 4 | `2026-10-16T16:46:28Z` |
| [Azure/azure-cli-extensions](https://github.com/Azure/azure-cli-extensions) | 134 | docs | 9 | 3 | `2026-10-16T06:17:07Z` |
| [Azure/azure-dev](https://github.com/Azure/azure-dev) | 133 | samples | 8 | 1 | `2026-10-16T01:23:20Z` |
| [microsoft/kiota-serialization-json-go](https://github.com/microsoft/kiota-serialization-json-go) | 129 | docs | 4 | 1 | `2026-10-16T16:22:20Z` |
| [microsoft/kiota-serialization-text-go](https://github.com/microsoft/kiota-serialization-text-go) | 129 | docs | 4 | 1 | `2026-10-16T16:18:11Z` |
| [microsoft/kiota-http-go](https://github.com/microsoft/kiota-http-go) | 129 | docs | 4 | 1 | `2026-10-16T16:17:43Z` |
| [Azure-Samples/azuresandbox](https://github.com/Azure-Samples/azuresandbox) | 127 | samples | 2 | 1 | `2026-10-16T17:12:17Z` |
| [microsoft/kiota-abstractions-go](https://github.com/microsoft/kiota-abstractions-go) | 127 | docs | 2 | 1 | `2026-10-16T16:27:20Z` |
| [microsoft/pylance-release](https://github.com/microsoft/pylance-release) | 127 | docs | 2 | 1 | `2026-10-16T04:53:51Z` |
| [Azure/LogicAppsUX](https://github.com/Azure/LogicAppsUX) | 117 | docs | 2 | 1 | `2026-10-16T17:24:09Z` |
| [Azure/azure-sdk-for-cpp](https://github.com/Azure/azure-sdk-for-cpp) | 117 | docs | 2 | 2 | `2026-10-15T22:30:53Z` |
| [Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample) | 117 | samples | 2 | 2 | `2026-10-15T22:11:54Z` |
| [MicrosoftDocs/entra-docs](https://github.com/MicrosoftDocs/entra-docs) | 114 | docs | 14 | 0 | `2026-10-16T07:32:42Z` |
| [MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect) | 102 | training | 2 | 0 | `2026-10-16T16:53:00Z` |
| [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs) | 100 | docs | 43 | 0 | `2026-10-16T17:08:31Z` |
| [dotnet/roslyn](https://github.com/dotnet/roslyn) | 95 | docs | 20 | 0 | `2026-10-16T16:11:58Z` |

## Repository Details

### dotnet/android-api-docs (118 commit(s), signal 65)

Tags: `docs, human-authored`

- [Document ApplicationStartInfo source event timestamp (#1070)](https://github.com/dotnet/android-api-docs/commit/1ccdb53adeae4ace968d3abb33af268757215dde) - `2026-10-16T11:52:46Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Document ApplicationStartInfo source event timestamp](https://github.com/dotnet/android-api-docs/pull/1070)
- [Docs: document group display name (#1069)](https://github.com/dotnet/android-api-docs/commit/c6bfb3d8931bc12e8bf0cf1234146c98ca744c74) - `2026-10-16T11:49:20Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Docs: document group display name](https://github.com/dotnet/android-api-docs/pull/1069)
- [Document unwanted auto-missed calls (#1068)](https://github.com/dotnet/android-api-docs/commit/089bfbd97e5af15708562ee2e7bdbe6dfbb3aab2) - `2026-10-16T11:49:11Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Document unwanted auto-missed calls](https://github.com/dotnet/android-api-docs/pull/1068)
- [Docs: document People Provider authority (#1067)](https://github.com/dotnet/android-api-docs/commit/47f5377fbe42f331fc91109f7fefb80ff33618d8) - `2026-10-16T11:48:42Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Docs: document People Provider authority](https://github.com/dotnet/android-api-docs/pull/1067)
- [Document application exit anomaly reason (#1065)](https://github.com/dotnet/android-api-docs/commit/db68d4752855cd82079a1fc2d9c071f14050083a) - `2026-10-16T11:48:14Z` - Jonathan Peppers (@jonathanpeppers) - PR: [Document application exit anomaly reason](https://github.com/dotnet/android-api-docs/pull/1065)

### MicrosoftDocs/azure-docs (43 commit(s), signal 100)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #321517 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-docs/commit/05a3d51b715d30cf95a62033fb7cb79353ce0d32) - `2026-10-16T17:08:31Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Moved cross-region deployment to plan and prepare section (#321512)](https://github.com/MicrosoftDocs/azure-docs/commit/8b936d901747a44e4e21e4827922202ac5ed64d9) - `2026-10-16T16:27:07Z` - Ali Zaman (@anzaman)
- [Add Azure Files change feed documentation (#321126)](https://github.com/MicrosoftDocs/azure-docs/commit/f4b76f3806af3268d2725f18741d71a72757546d) - `2026-10-16T14:30:49Z` - Athreyasubash (@Athreyasubash)
- [Merge pull request #321510 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-docs/commit/b800f512332b8f87be6068a9255d0b5e2fcbdfde) - `2026-10-16T11:39:22Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Updating comments as per PM and TME (#321471)](https://github.com/MicrosoftDocs/azure-docs/commit/8e12a909dd0a33971b6b502dddd18dea00796e59) - `2026-10-16T08:36:50Z` - Manish Chabbria (@netapp-manishc)

### dotnet/runtime (29 commit(s), signal 65)

Tags: `docs, human-authored`

- [[cDAC] Handle GettingReJITParameters state (#135471)](https://github.com/dotnet/runtime/commit/2ec49fefa7c8f8ea911bfcf18360c975ecd5e161) - `2026-10-16T17:15:14Z` - Peter Shrosbree (@pcshrosbree) - PR: [[cDAC] Handle GettingReJITParameters state](https://github.com/dotnet/runtime/pull/135471)
- [cDAC: skip empty assembly-list slots in Loader_1.GetModuleHandles (#1…](https://github.com/dotnet/runtime/commit/70bc56cb3eb3ba5e548466739bb2a039f524c062) - `2026-10-16T17:08:33Z` - Peter Shrosbree (@pcshrosbree) - PR: [cDAC: skip empty assembly-list slots in Loader_1.GetModuleHandles](https://github.com/dotnet/runtime/pull/135519)
- [ILVerify error cleanup (#135798)](https://github.com/dotnet/runtime/commit/22255fbd1dda7c92abdb4f68be53d650da5c4bcd) - `2026-10-16T16:16:28Z` - Jan Kotas (@jkotas) - PR: [ILVerify error cleanup](https://github.com/dotnet/runtime/pull/135798)
- [JIT: Propagate rejectNegativeConst through lcl + cns in monotonicity …](https://github.com/dotnet/runtime/commit/bc110ba9394534d502d4570671adc23fec631345) - `2026-10-16T14:13:19Z` - Egor Bogatov (@EgorBo) - PR: [JIT: Propagate rejectNegativeConst through lcl + cns in monotonicity check](https://github.com/dotnet/runtime/pull/135851)
- [[QUIC] Disable QUIC test on OSX with mono runtime (#135865)](https://github.com/dotnet/runtime/commit/e11eecae536898e055c874b939fb1753221679b4) - `2026-10-16T13:31:23Z` - Marie Píchová (@ManickaP) - PR: [[QUIC] Disable QUIC test on OSX with mono runtime](https://github.com/dotnet/runtime/pull/135865)

### Azure/azure-sdk-for-net (28 commit(s), signal 150)

Tags: `docs, human-authored, product:Azure AI, product:Azure SDK, release, release-language, watchlist`

- Release: [Azure.Provisioning.Storage_1.2.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.Provisioning.Storage_1.2.0) - `2026-10-16T08:49:55Z`
- Release: [Azure.ResourceManager.KeyVault_1.5.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.KeyVault_1.5.0) - `2026-10-16T07:09:50Z`
- Release: [Azure.AI.AgentServer.Responses_1.0.0-beta.9](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.AI.AgentServer.Responses_1.0.0-beta.9) - `2026-10-16T06:37:36Z`
- Release: [Azure.AI.AgentServer.Core_1.0.0-beta.30](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.AI.AgentServer.Core_1.0.0-beta.30) - `2026-10-16T05:56:13Z`
- Release: [Azure.ResourceManager.Compute.WorkloadManager_1.0.0-beta.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.Compute.WorkloadManager_1.0.0-beta.1) - `2026-10-16T05:26:48Z`
- [Bring voice agents to ApiView compliance (#63863)](https://github.com/Azure/azure-sdk-for-net/commit/8e09c928fc766f949345a6fd933e276d2928fc42) - `2026-10-16T16:57:21Z` - Nikolay Rovinskiy (@nick863) - PR: [Bring voice agents to ApiView compliance](https://github.com/Azure/azure-sdk-for-net/pull/63863)
- [Fix GA browser automation sample streaming and cleanup (#63831)](https://github.com/Azure/azure-sdk-for-net/commit/35d6ded29755a7f310b0204c31107f98f6fdd6e4) - `2026-10-16T16:04:00Z` - Mitesh Shah (@mitsha-microsoft) - PR: [Fix GA browser automation sample streaming and cleanup](https://github.com/Azure/azure-sdk-for-net/pull/63831)
- [Increment package version after release of Azure.Provisioning.Storage…](https://github.com/Azure/azure-sdk-for-net/commit/fa674adfb55aefc671da6c1e535d5e2a9a1ef2f0) - `2026-10-16T15:27:02Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment version for storage releases](https://github.com/Azure/azure-sdk-for-net/pull/63925)
- [[Mgmt] Make TypeSpec review guidance more visible (#63917)](https://github.com/Azure/azure-sdk-for-net/commit/aba9cd7d42c9df203fedaf91c31d8c6a2f8867d9) - `2026-10-16T07:58:08Z` - Wei Hu (@live1206) - PR: [[Mgmt] Make TypeSpec review guidance more visible](https://github.com/Azure/azure-sdk-for-net/pull/63917)
- [Increment package version after release of Azure.ResourceManager.KeyV…](https://github.com/Azure/azure-sdk-for-net/commit/5f8876b4af25a83e30265ac3e97301ba0e54890b) - `2026-10-16T07:43:42Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment version for keyvault releases](https://github.com/Azure/azure-sdk-for-net/pull/63918)

### dotnet/roslyn (20 commit(s), signal 95)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update FBA sources. Add --sdk-branch script param. (#86080)](https://github.com/dotnet/roslyn/commit/fe6e2362fac9f83588271b05f78e6ce651fc0502) - `2026-10-16T16:11:58Z` - Rikki Gibson (@RikkiGibson) - PR: [Update FBA sources. Add --sdk-branch script param.](https://github.com/dotnet/roslyn/pull/86080)
- [Fix IDE0330 not reported when type contains multi-declarator fields (…](https://github.com/dotnet/roslyn/commit/b7e2358b2bbd4097b75e4062dcf1311d054dca79) - `2026-10-16T16:00:26Z` - Austin Aviv (@austinaviv) - PR: [Fix IDE0330 not reported when type contains multi-declarator fields](https://github.com/dotnet/roslyn/pull/86077)
- [Set union values state as not-null when constructor invocation uses e…](https://github.com/dotnet/roslyn/commit/7ed110c0f961a5f8800139bc2df914ffb0099aca) - `2026-10-16T02:48:52Z` - AlekseyTs (@AlekseyTs) - PR: [Set union values state as not-null when constructor invocation uses expanded form](https://github.com/dotnet/roslyn/pull/86063)
- [Allow Go To Def from a file path in Razor in more places (#86072)](https://github.com/dotnet/roslyn/commit/96ede607d29ba217dd7a868b8156ba769fb9aa70) - `2026-10-15T21:29:03Z` - David Wengier (@davidwengier) - PR: [Allow Go To Def from a file path in Razor in more places](https://github.com/dotnet/roslyn/pull/86072)
- [Fix symbol-completion publication races (#85972)](https://github.com/dotnet/roslyn/commit/d4e68b6c60f195a000c7b6bb868d9e1b5071187e) - `2026-10-15T20:18:25Z` - Fred Silberberg (@333fred) - PR: [Fix symbol-completion publication races](https://github.com/dotnet/roslyn/pull/85972)

### MicrosoftLearning/mslearn-copilotstudio (14 commit(s), signal 89)

Tags: `human-authored, product:Azure AI, training, watchlist`

- [Add evaluation and publishing instructions for agents](https://github.com/MicrosoftLearning/mslearn-copilotstudio/commit/6364f5fa1b78b5e155cd610e83dd1edd86aa3a00) - `2026-10-16T16:51:38Z` - chandlersyal (@chandlersyal)
- [Add task notification agent and workflow section](https://github.com/MicrosoftLearning/mslearn-copilotstudio/commit/ac6bbb13cca768def0373cebef91664bfb961489) - `2026-10-16T16:51:17Z` - chandlersyal (@chandlersyal)
- [Add equipment recommendation agent section](https://github.com/MicrosoftLearning/mslearn-copilotstudio/commit/da58c769f45170aad7d661d02c4d335177dba652) - `2026-10-16T16:50:59Z` - chandlersyal (@chandlersyal)
- [Update 01-create-benefits-agent.md](https://github.com/MicrosoftLearning/mslearn-copilotstudio/commit/e594eb2d79ca7c5e04a6bedebe1872164c9eec31) - `2026-10-16T16:50:36Z` - chandlersyal (@chandlersyal)
- [Merge pull request #87 from MicrosoftLearning/oct2026update](https://github.com/MicrosoftLearning/mslearn-copilotstudio/commit/dad93d58b9c2707e21462a00279252e88e6fe68a) - `2026-10-16T15:27:48Z` - chandlersyal (@chandlersyal) - PR: [Oct2026update](https://github.com/MicrosoftLearning/mslearn-copilotstudio/pull/87)

### Azure/azure-sdk-for-js (14 commit(s), signal 139)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [@azure/arm-cognitiveservices_9.0.0-beta.5](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-cognitiveservices_9.0.0-beta.5) - `2026-10-16T17:29:39Z`
- Release: [@azure/arm-cloudhealth_1.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-cloudhealth_1.0.0) - `2026-10-16T16:04:41Z`
- Release: [@azure/arm-azurestackhci_4.2.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-azurestackhci_4.2.0) - `2026-10-16T07:47:50Z`
- Release: [@azure/arm-recoveryservicesbackup_15.0.0](https://github.com/Azure/azure-sdk-for-js/releases/tag/%40azure/arm-recoveryservicesbackup_15.0.0) - `2026-10-16T04:08:36Z`
- [[AutoPR @azure-arm-cognitiveservices]-generated-from-SDK Generation -…](https://github.com/Azure/azure-sdk-for-js/commit/416e5db0218744f4f8b46d50375dddc780c67b7b) - `2026-10-16T16:42:40Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR @azure-arm-cognitiveservices]-generated-from-SDK Generation - JS-6940909](https://github.com/Azure/azure-sdk-for-js/pull/40278)
- [[ai-projects] Fix browser automation sample for GA tool (#40309)](https://github.com/Azure/azure-sdk-for-js/commit/1992096c4e1f25150a9d83962e8cd3a96b8ce20f) - `2026-10-16T16:10:35Z` - Mitesh Shah (@mitsha-microsoft) - PR: [[ai-projects] Fix browser automation sample for GA tool](https://github.com/Azure/azure-sdk-for-js/pull/40309)
- [[AutoPR @azure-arm-cloudhealth]-generated-from-SDK Generation - JS-69…](https://github.com/Azure/azure-sdk-for-js/commit/3a17892dbf9d48559cc97e09ba5c8554211d4c69) - `2026-10-16T15:33:25Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR @azure-arm-cloudhealth]-generated-from-SDK Generation - JS-6963068](https://github.com/Azure/azure-sdk-for-js/pull/40361)
- [[AutoPR @azure-arm-azurestackhci]-generated-from-SDK Generation - JS-…](https://github.com/Azure/azure-sdk-for-js/commit/36b1202521fc1797b1baff692a63082d6677a492) - `2026-10-16T06:46:14Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR @azure-arm-azurestackhci]-generated-from-SDK Generation - JS-6961098](https://github.com/Azure/azure-sdk-for-js/pull/40350)
- [improve mgmt review guideline (#40369)](https://github.com/Azure/azure-sdk-for-js/commit/caefcc3ae36614d49e761cee391d8ff7c8f13e1f) - `2026-10-16T05:41:51Z` - ZiWei Chen (@kazrael2119) - PR: [improve mgmt review guideline](https://github.com/Azure/azure-sdk-for-js/pull/40369)

### microsoft/vscode-docs (14 commit(s), signal 89)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merge pull request #10497 from microsoft/docs/mcp-tools-refresh](https://github.com/microsoft/vscode-docs/commit/e6026c88063236095c7801d87c51e5c47aa39be5) - `2026-10-16T15:31:38Z` - Nick Trogh (@ntrogh) - PR: [Restructure MCP content for readability](https://github.com/microsoft/vscode-docs/pull/10497)
- [Restructure MCP content](https://github.com/microsoft/vscode-docs/commit/e1efbf99b32c3ada110039a88921c872579f87ad) - `2026-10-16T14:16:20Z` - Nick Trogh (@ntrogh) - PR: [Restructure MCP content for readability](https://github.com/microsoft/vscode-docs/pull/10497)
- [Merge pull request #10495 from microsoft/docs/custom-agents-accuracy](https://github.com/microsoft/vscode-docs/commit/baa88c2fbfc7b65ea7d0821edd9aba398c6815b7) - `2026-10-16T12:02:55Z` - Nick Trogh (@ntrogh) - PR: [Refresh Custom Agents article for correctness and structure](https://github.com/microsoft/vscode-docs/pull/10495)
- [Refresh Custom Agents article for correctness and structure](https://github.com/microsoft/vscode-docs/commit/8fc5e5375220415fe5618d5d84f3109c878203ae) - `2026-10-16T11:57:28Z` - Nick Trogh (@ntrogh) - PR: [Refresh Custom Agents article for correctness and structure](https://github.com/microsoft/vscode-docs/pull/10495)
- [chore: update netiso policy (#10494)](https://github.com/microsoft/vscode-docs/commit/4d3cd4684e2d752440b1230ae1df9b3de5edd0e0) - `2026-10-15T23:38:26Z` - Raymond Zhao (@rzhao271) - PR: [chore: update netiso policy](https://github.com/microsoft/vscode-docs/pull/10494)

### dotnet/msbuild (14 commit(s), signal 89)

Tags: `docs, human-authored, watchlist`

- [[main] Source code updates from dotnet/dotnet (#15221)](https://github.com/dotnet/msbuild/commit/6348d0c087aeec18c323b01a2c77da089ddafea0) - `2026-10-16T15:18:29Z` - dotnet-maestro[bot] (@dotnet-maestro[bot]) - PR: [[main] Source code updates from dotnet/dotnet](https://github.com/dotnet/msbuild/pull/15221)
- [[main] Update dependencies from nuget/nuget.client and bootstrap with…](https://github.com/dotnet/msbuild/commit/5cb766ca89756c2803857a6a5d6c4ed42c9925e2) - `2026-10-16T15:02:54Z` - dotnet-maestro[bot] (@dotnet-maestro[bot]) - PR: [[main] Update dependencies from nuget/nuget.client and bootstrap with RC2](https://github.com/dotnet/msbuild/pull/15196)
- [Fix skill validation failures from generic syntax in descriptions (#1…](https://github.com/dotnet/msbuild/commit/11d8d142e05b81d831141bd6a5d39a291d681c98) - `2026-10-16T14:12:32Z` - Copilot (@Copilot) - PR: [Fix skill validation failures from generic syntax in descriptions](https://github.com/dotnet/msbuild/pull/15300)
- [Localized file check-in by OneLocBuild Task: Build definition ID 9434…](https://github.com/dotnet/msbuild/commit/75441f006b8c1cca7d7316b116b09096d06c3be0) - `2026-10-16T13:43:21Z` - dotnet-oneloc-localization[bot] (@dotnet-oneloc-localization[bot]) - PR: [Localized file check-in by OneLocBuild Task: Build definition ID 9434: Build ID 15713050](https://github.com/dotnet/msbuild/pull/15298)
- [Grow the logging queue instead of blocking producers when memory allo…](https://github.com/dotnet/msbuild/commit/ff8a5460cedc1490332f283d3d43e4cfedbc9371) - `2026-10-16T13:36:53Z` - Aleš Prokop (@AlesProkop) - PR: [Grow the logging queue instead of blocking producers when memory allows](https://github.com/dotnet/msbuild/pull/15281)

### MicrosoftDocs/entra-docs (14 commit(s), signal 114)

Tags: `docs, human-authored, security, watchlist`

- [Merge pull request #14620 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/entra-docs/commit/943c6575141b721ed0d4ec2bc515f7bc8f61027f) - `2026-10-16T07:32:42Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Remove section on managing individual Security Defaults (#14618)](https://github.com/MicrosoftDocs/entra-docs/commit/23c29f0c416703762a4953f1cf99d8c0b5fb056b) - `2026-10-16T03:33:15Z` - anksridhar (@anksridhar)
- [docs: use primary tenant domain in External ID user creation example …](https://github.com/MicrosoftDocs/entra-docs/commit/15df35364c0d4457108f9c1d6917824131eb3f61) - `2026-10-16T02:13:41Z` - vimrang (@vimrang)
- [Merge pull request #14613 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/entra-docs/commit/49b84e07023770128d83039c07eafb84ff1de1df) - `2026-10-15T22:43:09Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Route invited users to an external identity provider with domain_hint…](https://github.com/MicrosoftDocs/entra-docs/commit/4df42e6f03f5fd9bff11e32579428a97601c47ee) - `2026-10-15T22:33:51Z` - nanguil (@nanguil)

### Azure-Samples/modernize-bootcamp (13 commit(s), signal 53)

Tags: `human-authored, samples`

- [Merge pull request #66 from Azure-Samples/petroula_work_cli](https://github.com/Azure-Samples/modernize-bootcamp/commit/55fe5d8aedb2eaee3c40862656820605b52df53b) - `2026-10-16T16:29:51Z` - mspetroula (@mspetroula) - PR: [Fix spelling errors and improve README clarity](https://github.com/Azure-Samples/modernize-bootcamp/pull/66)
- [Fix spelling errors and improve README clarity](https://github.com/Azure-Samples/modernize-bootcamp/commit/f76e409f8305e655727bc918e637595035ba8a0b) - `2026-10-16T16:28:44Z` - mspetroula (@mspetroula) - PR: [Fix spelling errors and improve README clarity](https://github.com/Azure-Samples/modernize-bootcamp/pull/66)
- [Merge pull request #65 from Azure-Samples/sojorgensen/rewordinglabs](https://github.com/Azure-Samples/modernize-bootcamp/commit/0400601bd87962d0fee6a403ac73e9d7d8dc1312) - `2026-10-16T15:47:23Z` - Sophie Jorgensen (@sophiejorgensen) - PR: [Sojorgensen/rewordinglabs](https://github.com/Azure-Samples/modernize-bootcamp/pull/65)
- [Reference Module 2 for Autopilot and note summary output may vary in …](https://github.com/Azure-Samples/modernize-bootcamp/commit/3e4413daf884a1063fc2234d3f6c953daf270e4c) - `2026-10-16T15:38:30Z` - Sophie Jorgensen - PR: [Sojorgensen/rewordinglabs](https://github.com/Azure-Samples/modernize-bootcamp/pull/65)
- [Clarify Module 3 clone step and add timing notes for the Azure code step](https://github.com/Azure-Samples/modernize-bootcamp/commit/9afad1f054b42f92d394c11b690fddf561adcae9) - `2026-10-16T15:33:05Z` - Sophie Jorgensen - PR: [Sojorgensen/rewordinglabs](https://github.com/Azure-Samples/modernize-bootcamp/pull/65)

### MicrosoftDocs/azure-compute-docs (13 commit(s), signal 88)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-co…](https://github.com/MicrosoftDocs/azure-compute-docs/commit/e15b93076ded34ca8abc8896b8a1810641bca0ad) - `2026-10-16T06:03:14Z` - Learn Build Service GitHub App
- [Merge pull request #4245 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-compute-docs/commit/dd74fd3f2eb86489c72a4563b90d83eca9ebb648) - `2026-10-16T06:02:14Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #4244 from Simon2228/patch-1](https://github.com/MicrosoftDocs/azure-compute-docs/commit/01c782bc51cf72871899461bf11144e4ef5b27a7) - `2026-10-15T23:58:40Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Update articles/virtual-machines/windows/n-series-amd-driver-setup.md](https://github.com/MicrosoftDocs/azure-compute-docs/commit/869bd5c34e1d9fc220a7b8f9cf477c3a88ab39cc) - `2026-10-15T23:39:57Z` - Simon2228 (@Simon2228)
- [Update articles/virtual-machines/windows/n-series-amd-driver-setup.md](https://github.com/MicrosoftDocs/azure-compute-docs/commit/639871d328a14754f1e8d1f027f1a66fefe6321a) - `2026-10-15T23:39:07Z` - Simon2228 (@Simon2228)

### MicrosoftDocs/azure-aks-docs (12 commit(s), signal 87)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #4012 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-aks-docs/commit/94525023eebfbf4ec7dbd6e9a6373ef6ede63eee) - `2026-10-16T17:04:14Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #4011 from ffidelis/expand-disk-over-4tib](https://github.com/MicrosoftDocs/azure-aks-docs/commit/260895fa391ff73438be437086d7159d4dd48e5a) - `2026-10-16T16:07:05Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #4010 from ffidelis/nfs-secure-transfer-note](https://github.com/MicrosoftDocs/azure-aks-docs/commit/a0e5d31cc87ab11c4b19013cb48b820f3f62366a) - `2026-10-16T16:06:26Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Merge pull request #4003 from ffidelis/nfs-mountoptions-note](https://github.com/MicrosoftDocs/azure-aks-docs/commit/6fc0a353cacbaa08aeb566309cfeeee8db4a63ff) - `2026-10-16T16:03:05Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Apply Authoring Assistant suggestion](https://github.com/MicrosoftDocs/azure-aks-docs/commit/2c73b9aaf6efde2482294dcc2eb09b81630d4ece) - `2026-10-16T15:53:36Z` - ffidelis (@ffidelis)

### Azure/azure-sdk-for-java (12 commit(s), signal 137)

Tags: `docs, human-authored, product:Azure SDK, release, release-language, watchlist`

- Release: [com.azure.resourcemanager+azure-resourcemanager-cloudhealth_1.0.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-cloudhealth_1.0.0) - `2026-10-16T16:48:32Z`
- Release: [com.azure.resourcemanager+azure-resourcemanager-terraform_1.0.0-beta.2](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-terraform_1.0.0-beta.2) - `2026-10-16T03:40:12Z`
- Release: [com.azure.resourcemanager+azure-resourcemanager-azurestackhci_1.2.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-azurestackhci_1.2.0) - `2026-10-16T02:13:20Z`
- [[AutoPR azure-resourcemanager-storage]-generated-from-SDK Generation …](https://github.com/Azure/azure-sdk-for-java/commit/26ab19d7e8012f46a66156d72baa527a111dd99b) - `2026-10-16T16:47:10Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-resourcemanager-storage]-generated-from-SDK Generation - Java-6960296](https://github.com/Azure/azure-sdk-for-java/pull/50779)
- [[AutoPR azure-resourcemanager-cloudhealth]-generated-from-SDK Generat…](https://github.com/Azure/azure-sdk-for-java/commit/5d5b647f506dd5a2a2e80976dd15f00440c9b38f) - `2026-10-16T15:29:12Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-resourcemanager-cloudhealth]-generated-from-SDK Generation - Java-6963078](https://github.com/Azure/azure-sdk-for-java/pull/50827)
- [Fix VertxHttpClient streaming request bodies hanging on Vert.x 5.x (#…](https://github.com/Azure/azure-sdk-for-java/commit/6ae911e6cacb3674e8fb4f894ffb7277ec0b4363) - `2026-10-16T12:49:14Z` - James Netherton (@jamesnetherton) - PR: [Fix VertxHttpClient streaming request bodies hanging on Vert.x 5.x](https://github.com/Azure/azure-sdk-for-java/pull/50836)
- [Increment package versions for terraform auto-releases (#50833)](https://github.com/Azure/azure-sdk-for-java/commit/396d9648d9bbfc7b32c970dbb164ea2cabbcb710) - `2026-10-16T05:15:37Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[skip ci] Increment versions for terraform auto-releases](https://github.com/Azure/azure-sdk-for-java/pull/50833)
- [Increment package versions for azurestackhci auto-releases (#50832)](https://github.com/Azure/azure-sdk-for-java/commit/91056ec31129ab44d60ee7814db3f496dc7fc653) - `2026-10-16T02:57:26Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[skip ci] Increment versions for azurestackhci auto-releases](https://github.com/Azure/azure-sdk-for-java/pull/50832)

### microsoft/onnxruntime (11 commit(s), signal 51)

Tags: `human-authored, samples`

- [[CUDA] Optimize packed QSA scoring and multi-token verification (#33328)](https://github.com/microsoft/onnxruntime/commit/b016c164ce9303d3a6c178d947554d4d0e543d9a) - `2026-10-16T17:23:07Z` - kunal-vaishnavi (@kunal-vaishnavi) - PR: [[CUDA] Optimize packed QSA scoring and multi-token verification](https://github.com/microsoft/onnxruntime/pull/33328)
- [Fix d3d12_file_buffer_loader so it can build with no exception and cl…](https://github.com/microsoft/onnxruntime/commit/a8fda2fe6892f9bd0f318d20dd7cb137f44ae6ea) - `2026-10-16T16:37:18Z` - Sushanth Rajasankar (@sushraja-msft) - PR: [Fix d3d12_file_buffer_loader so it can build with no exception and clang](https://github.com/microsoft/onnxruntime/pull/33408)
- [[WebGPU] Optimize subgroup matrix MatMulNBits for AMD wave64 (#32796)](https://github.com/microsoft/onnxruntime/commit/52131d937f84013d1f164dc74e397be7562c5f7f) - `2026-10-16T13:03:38Z` - Yang Gu (@gyagp) - PR: [[WebGPU] Optimize subgroup matrix MatMulNBits for AMD wave64](https://github.com/microsoft/onnxruntime/pull/32796)
- [[CUDA][WebGPU] Add PackedSparseAttentionIndexerMerge for MTP index sh…](https://github.com/microsoft/onnxruntime/commit/f33c1744e1e1064d3618d1d0ce533f0b946aed2d) - `2026-10-16T05:40:29Z` - kunal-vaishnavi (@kunal-vaishnavi) - PR: [[CUDA][WebGPU] Add PackedSparseAttentionIndexerMerge for MTP index sharing](https://github.com/microsoft/onnxruntime/pull/33224)
- [[CUDA] Support offline NVFP4 QMoE weights and fused block-FP8 executi…](https://github.com/microsoft/onnxruntime/commit/2fd0afabe8e6f48c128218d356740b218eec9ca3) - `2026-10-16T04:51:43Z` - kunal-vaishnavi (@kunal-vaishnavi) - PR: [[CUDA] Support offline NVFP4 QMoE weights and fused block-FP8 execution](https://github.com/microsoft/onnxruntime/pull/33094)

### microsoft/kiota-python (11 commit(s), signal 86)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #809 from HardMax71/fix/strict-typing-middleware-o…](https://github.com/microsoft/kiota-python/commit/2d13770937ee6149fb041404665e4189a19bda18) - `2026-10-16T16:22:58Z` - Vincent Biret (@baywet) - PR: [fix(http): pass mypy --strict in middleware options and fix three option bugs](https://github.com/microsoft/kiota-python/pull/809)
- [Merge remote-tracking branch 'origin/main' into fix/strict-typing-mid…](https://github.com/microsoft/kiota-python/commit/2f4f5cf1b05115e32e6f617a1d3299c97b4d495e) - `2026-10-16T16:10:20Z` - HardMax71 (@HardMax71) - PR: [fix(http): pass mypy --strict in middleware options and fix three option bugs](https://github.com/microsoft/kiota-python/pull/809)
- [Merge pull request #807 from HardMax71/fix/json-hooks-for-nested-objects](https://github.com/microsoft/kiota-python/commit/a94454eb5a9deac129c57f15a267198f2ed3e8fa) - `2026-10-15T17:19:53Z` - Vincent Biret (@baywet) - PR: [fix(json): give on_start the object's own writer and pass the hooks to nested parse nodes](https://github.com/microsoft/kiota-python/pull/807)
- [fix(http): pass mypy --strict in middleware options and fix three opt…](https://github.com/microsoft/kiota-python/commit/9b813a65d9e7d33488ac098c39e82161f1ab40c1) - `2026-10-15T17:12:57Z` - HardMax71 (@HardMax71) - PR: [fix(http): pass mypy --strict in middleware options and fix three option bugs](https://github.com/microsoft/kiota-python/pull/809)
- [Merge branch 'main' into fix/json-hooks-for-nested-objects](https://github.com/microsoft/kiota-python/commit/212f4d233040c0a866a15816cdcd67af193bcc16) - `2026-10-15T17:03:31Z` - Max Azatian (@HardMax71) - PR: [fix(json): give on_start the object's own writer and pass the hooks to nested parse nodes](https://github.com/microsoft/kiota-python/pull/807)

### MicrosoftDocs/azure-docs-sdk-dotnet (11 commit(s), signal 86)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/52323624bc4405ab8b2162c0a0d358b60a63925b) - `2026-10-16T09:04:19Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/27166aea26514bb4dfe8f0e274dea073d0b80a5e) - `2026-10-16T07:24:45Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/ad3e0d478db00b1cf9efb05da2850061ffc0a470) - `2026-10-16T06:55:18Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/12fbe5eba000be5797ec96ab9cc8a2dd44bd165f) - `2026-10-16T06:12:23Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/e88d8b085b99c0e5f40e836dbcc29b46cebafe7d) - `2026-10-16T05:42:21Z` - azure-sdk (@azure-sdk)

### Azure/azure-sdk-for-python (10 commit(s), signal 135)

Tags: `docs, human-authored, product:Azure AI, product:Azure SDK, release, release-language, watchlist`

- Release: [azure-mgmt-azurestackhci_8.2.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-azurestackhci_8.2.0) - `2026-10-16T08:30:05Z`
- Release: [azure-ai-agentserver-responses_2.4.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-responses_2.4.0b1) - `2026-10-16T07:18:15Z`
- Release: [azure-ai-agentserver-core_2.3.0b1](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-ai-agentserver-core_2.3.0b1) - `2026-10-16T06:31:15Z`
- Release: [azure-mgmt-recoveryservicesbackup_11.2.0](https://github.com/Azure/azure-sdk-for-python/releases/tag/azure-mgmt-recoveryservicesbackup_11.2.0) - `2026-10-16T05:48:55Z`
- [[AutoPR azure-mgmt-storage]-generated-from-SDK Generation - Python-69…](https://github.com/Azure/azure-sdk-for-python/commit/94ac1e9facc7e96ccdc5f405a78c80083cdadd65) - `2026-10-16T16:46:28Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-mgmt-storage]-generated-from-SDK Generation - Python-6960304](https://github.com/Azure/azure-sdk-for-python/pull/49523)
- [[wip] Trust 1ES proxy certificates for Windows wheel builds (#49458)](https://github.com/Azure/azure-sdk-for-python/commit/dd1392fffc7b82e4da60fcd0c2c12d726c3d4684) - `2026-10-16T15:40:29Z` - Libba Lawrence (@l0lawrence) - PR: [[wip] Trust 1ES proxy certificates for Windows wheel builds](https://github.com/Azure/azure-sdk-for-python/pull/49458)
- [[AutoPR azure-mgmt-cloudhealth]-generated-from-SDK Generation - Pytho…](https://github.com/Azure/azure-sdk-for-python/commit/582e3dfcbdfc5191144bae373cdf2e446135412d) - `2026-10-16T15:28:43Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-mgmt-cloudhealth]-generated-from-SDK Generation - Python-6963115](https://github.com/Azure/azure-sdk-for-python/pull/49558)
- [Increment package version after release of azure-ai-agentserver-core …](https://github.com/Azure/azure-sdk-for-python/commit/56c7f8139e0998e44bc8e70c8b8d1d12052e115b) - `2026-10-16T07:21:47Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Increment version for agentserver releases](https://github.com/Azure/azure-sdk-for-python/pull/49571)
- [[AutoPR azure-mgmt-azurestackhci]-generated-from-SDK Generation - Pyt…](https://github.com/Azure/azure-sdk-for-python/commit/1d19649480ff5a5f119b0e1b81256c5e0376586e) - `2026-10-16T07:08:55Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-mgmt-azurestackhci]-generated-from-SDK Generation - Python-6961099](https://github.com/Azure/azure-sdk-for-python/pull/49551)

### microsoft/TypeAgent (10 commit(s), signal 85)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Add EmbeddingGemma local embeddings (#3188)](https://github.com/microsoft/TypeAgent/commit/00748a4be87704ce871cdf9d86b6d7032b7f7b73) - `2026-10-16T15:37:06Z` - Hillary Mutisya (@hillary-mutisya) - PR: [Add EmbeddingGemma local embeddings](https://github.com/microsoft/TypeAgent/pull/3188)
- [Simplifying copilot macros (#3186)](https://github.com/microsoft/TypeAgent/commit/2f601a5781024ac1b56e1611fb296e3fd2646497) - `2026-10-16T07:44:18Z` - Hillary Mutisya (@hillary-mutisya) - PR: [Simplifying copilot macros](https://github.com/microsoft/TypeAgent/pull/3186)
- [Switch smoke tests to luna models (#3187)](https://github.com/microsoft/TypeAgent/commit/6948989d44959fddfa5bd17536f2bfcd72fab989) - `2026-10-16T05:58:32Z` - Hillary Mutisya (@hillary-mutisya) - PR: [Switch smoke tests to luna models](https://github.com/microsoft/TypeAgent/pull/3187)
- [Render remediation reports from structured data (#3185)](https://github.com/microsoft/TypeAgent/commit/74d5d931cf44cd75d53ad3dd2fed2750c5142282) - `2026-10-16T04:23:10Z` - robgruen (@robgruen) - PR: [Render remediation reports from structured data](https://github.com/microsoft/TypeAgent/pull/3185)
- [Render browser tab labels as text (#3173)](https://github.com/microsoft/TypeAgent/commit/bb38fbcc819dcdb728dd0f1323291a40a25730e6) - `2026-10-15T22:39:22Z` - robgruen (@robgruen) - PR: [Render browser tab labels as text](https://github.com/microsoft/TypeAgent/pull/3173)

### MicrosoftDocs/cloud-adoption-framework (10 commit(s), signal 85)

Tags: `docs, human-authored, watchlist`

- [Add abbreviation for Azure Monitor Private Link Scope (#1436)](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/753a08e5663059b469f82038df82b6cdf14b6928) - `2026-10-16T14:26:46Z` - balazs92117 (@balazs92117) - PR: [Add abbreviation for Azure Monitor Private Link Scope](https://github.com/MicrosoftDocs/cloud-adoption-framework/pull/1436)
- [Merging changes synced from https://github.com/MicrosoftDocs/cloud-ad…](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/52e32393dba4e750030968d7887d819f127c0fc9) - `2026-10-16T13:24:07Z` - Learn Build Service GitHub App
- [Merge pull request #7407 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/1db27877b43798beb0a96ddaa843f8ca0212fb8b) - `2026-10-16T13:23:14Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update index.md (#7406)](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/fa38f25b33dfad161ef243fe2770bd54fe4616a0) - `2026-10-16T13:20:31Z` - Stephen Sumner (@stephen-sumner)
- [Merging changes synced from https://github.com/MicrosoftDocs/cloud-ad…](https://github.com/MicrosoftDocs/cloud-adoption-framework/commit/cd35beb4d454ac8fc861683d0dfac7d34b4a13b7) - `2026-10-15T19:14:25Z` - Learn Build Service GitHub App

### MicrosoftDocs/fabric-docs (10 commit(s), signal 85)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #3428 from MicrosoftDocs/main639276994200936014syn…](https://github.com/MicrosoftDocs/fabric-docs/commit/0cbcc6f71ec43315a94ebc7629d661e885074102) - `2026-10-15T22:17:28Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3428)
- [Merging changes synced from https://github.com/MicrosoftDocs/fabric-d…](https://github.com/MicrosoftDocs/fabric-docs/commit/9c8a0f4f2519f6b1cb3e0c770c67ecef1363a01a) - `2026-10-15T22:16:57Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3428)
- [Merge pull request #16982 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/fabric-docs/commit/2f17bcf02313afb20a362abed05c46820e7f8b9b) - `2026-10-15T22:13:32Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3428)
- [Merge pull request #16981 from baanders/10-15-ontology](https://github.com/MicrosoftDocs/fabric-docs/commit/9277288d95555faac3cc93ab845d16b50324d8a8) - `2026-10-15T20:48:10Z` - prmerger-automator[bot] (@prmerger-automator[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3428)
- [Document trusted resources for Azure event delivery (#16720)](https://github.com/MicrosoftDocs/fabric-docs/commit/4118631219d16472cec761dfbfa6255429575523) - `2026-10-15T20:41:15Z` - George Guirguis (@george-guirguis) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/fabric-docs/pull/3428)

### Azure/azure-cli-extensions (9 commit(s), signal 134)

Tags: `docs, human-authored, release, release-language, watchlist`

- Release: [oracle-database 3.0.1](https://github.com/Azure/azure-cli-extensions/releases/tag/oracle-database-3.0.1) - `2026-10-16T06:18:11Z`
- Release: [storagesync 1.0.2](https://github.com/Azure/azure-cli-extensions/releases/tag/storagesync-1.0.2) - `2026-10-16T02:48:44Z`
- Release: [edgeoperator 1.0.0b2](https://github.com/Azure/azure-cli-extensions/releases/tag/edgeoperator-1.0.0b2) - `2026-10-16T01:36:40Z`
- [[Release] Update index.json for extension [ oracle-database-3.0.1 ]](https://github.com/Azure/azure-cli-extensions/commit/ebea488892f255360e25bc481fc3f01fd5990334) - `2026-10-16T06:17:07Z` - Azure CLI Team (@azclibot)
- [{OracleDatabase} Update listPrivateIps for cloud VM cluster   (#10474)](https://github.com/Azure/azure-cli-extensions/commit/08772c4bd42082e92999ef577a56098f04f70411) - `2026-10-16T06:00:48Z` - Mihret Kidane (@mihretkidane-OCI) - PR: [{OracleDatabase} Update listPrivateIps for cloud VM cluster](https://github.com/Azure/azure-cli-extensions/pull/10474)
- [{aks-preview} Container Insights azure monitor profile onboarding (#1…](https://github.com/Azure/azure-cli-extensions/commit/374be338bbd097a89b7cf933bb4c6e020f542bbd) - `2026-10-16T05:58:00Z` - suyadav1 (@suyadav1) - PR: [{aks-preview} Container Insights azure monitor profile onboarding](https://github.com/Azure/azure-cli-extensions/pull/10337)
- [[Release] Update index.json for extension [ storagesync-1.0.2 ]](https://github.com/Azure/azure-cli-extensions/commit/481f4e0bf308af4a0f1251fd142da8db83ef1d25) - `2026-10-16T02:47:50Z` - Azure CLI Team (@azclibot)
- [[StorageSync] Bump API version to 2025-12-01 (#10442)](https://github.com/Azure/azure-cli-extensions/commit/1c7f521784c4f79066c0841432c9beff978c01cb) - `2026-10-16T02:33:40Z` - JunKai-v (@JunKai-v) - PR: [[StorageSync] Bump API version to 2025-12-01](https://github.com/Azure/azure-cli-extensions/pull/10442)

### microsoftgraph/microsoft-graph-docs-contrib (9 commit(s), signal 84)

Tags: `docs, human-authored, product:Microsoft Graph, watchlist`

- [Merge pull request #10069 from microsoftgraph/main639277084030101522s…](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/616716c6ba69340b9032d571619273fe7fd19609) - `2026-10-16T00:47:11Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10069)
- [Merging changes synced from https://github.com/microsoftgraph/microso…](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/d37db3f3c39d60d888db4f93272a4f88d909023c) - `2026-10-16T00:46:38Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10069)
- [Merge pull request #29752 from microsoftgraph/main](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/e553f1b796b467f412f6d32620daa849c99e1cb4) - `2026-10-16T00:39:21Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10069)
- [Document SharePoint service prioritization report (#29688)](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/6557055722ab8daa63762a515cbac06071478861) - `2026-10-15T19:30:09Z` - abhishekkakhandiki (@abhishekkakhandiki) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10069)
- [Remove outdated August 2026 updates from overview (#29701)](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/commit/08128f3ea0f0f61158acd49f3b43912f5d9cc425) - `2026-10-15T19:29:29Z` - Jarbas Horst (@JarbasHorst) - PR: [Repo sync for protected branch](https://github.com/microsoftgraph/microsoft-graph-docs-contrib/pull/10069)

### MicrosoftDocs/SupportArticles-docs (9 commit(s), signal 84)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/96200d8f820379d90633c5bfd3eda766ef5c7283) - `2026-10-15T22:06:06Z` - Learn Build Service GitHub App
- [Merge pull request #12622 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/8a3b113e3b130d1ac32cc3d50d037986c187d53f) - `2026-10-15T22:03:45Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Fix formatting in troubleshooting documentation (#12618)](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/a68a8ce1cbb85bad97d8eedb73dfaff9d0299efb) - `2026-10-15T21:59:21Z` - guptasonia (@guptasonia)
- [AB#13192: AI Optimization and Freshness review: Remove duplicate rows…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/436494caf15caf0a49ea10246e1f0e1f6dfccbe2) - `2026-10-15T21:39:27Z` - Aarti Goyle (@aartig13)
- [New FAQ article for AI support assistant for commercial products (#12…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/00ec0f48aea2bc19127fdec346979bf89b85acc1) - `2026-10-15T21:03:59Z` - Meera Krishna (@Cloud-Writer)

### MicrosoftDocs/learn (8 commit(s), signal 83)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/4378bc1ee8bbd1c3379e364f8c4d6342104942ca) - `2026-10-16T11:30:06Z` - Learn Build Service GitHub App
- [Merge pull request #56515 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/learn/commit/e712c5d059466642ff1931d7585c482f3445b182) - `2026-10-16T11:17:26Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/f64cc798d5a57d9a6b61064a0acc5c1b5262d87a) - `2026-10-16T07:27:10Z` - Learn Build Service GitHub App
- [Module freshness review & updates (#56513)](https://github.com/MicrosoftDocs/learn/commit/7686eacab3151523891e0f9d7e7613a4a9cd13fa) - `2026-10-16T07:25:52Z` - Orin Thomas (@Orin-Thomas)
- [Merge pull request #56514 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/learn/commit/3aff8dcc50ab23252493ea225ccb87b34044c41d) - `2026-10-16T07:19:20Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### Azure/azure-dev (8 commit(s), signal 133)

Tags: `human-authored, product:Azure AI, product:Azure SDK, release, release-language, samples, watchlist`

- Release: [azd-ext-azure-ai-evaluations_1.0.0-beta.2](https://github.com/Azure/azure-dev/releases/tag/azd-ext-azure-ai-evaluations_1.0.0-beta.2) - `2026-10-15T23:46:33Z`
- [ci: expand azd extension code owners (#10499)](https://github.com/Azure/azure-dev/commit/1bd2ca4699c7b1f371db85dd867f18aa4fbc4730) - `2026-10-16T01:23:20Z` - Hui Miao (@huimiu) - PR: [ci: expand azd extension code owners](https://github.com/Azure/azure-dev/pull/10499)
- [[azure.ai.dataset] Registry update for 1.0.0-beta.2 (#10504)](https://github.com/Azure/azure-dev/commit/fb52e4a6087d8d049c6a603a7acf7689d4326668) - `2026-10-16T00:25:52Z` - Azure SDK Bot (@azure-sdk) - PR: [[azure.ai.dataset] Registry update for 1.0.0-beta.2](https://github.com/Azure/azure-dev/pull/10504)
- [[azure.ai.evaluations] Registry update for 1.0.0-beta.2 (#10507)](https://github.com/Azure/azure-dev/commit/0d6cdf7dfd71ef6a0b3560a9b558c6d7773d4b7b) - `2026-10-16T00:21:30Z` - Azure SDK Bot (@azure-sdk) - PR: [[azure.ai.evaluations] Registry update for 1.0.0-beta.2](https://github.com/Azure/azure-dev/pull/10507)
- [feat: scaffold Azure AI Search extension (#10435)](https://github.com/Azure/azure-dev/commit/7761d181610c06d78cf383657ade7c9e2f668863) - `2026-10-15T23:56:32Z` - hizixin (@hizixin) - PR: [feat: scaffold Azure AI Search extension](https://github.com/Azure/azure-dev/pull/10435)
- [Prepare Foundry evaluations and dataset extension releases (1.0.0-bet…](https://github.com/Azure/azure-dev/commit/c681d5a9e52961914e12e98255680363c52e2a7f) - `2026-10-15T18:44:39Z` - Mohamed Hessien (@m7md7sien) - PR: [Prepare Foundry evaluations and dataset extension releases (1.0.0-beta.2)](https://github.com/Azure/azure-dev/pull/10430)

### MicrosoftDocs/azure-docs-sdk-node (7 commit(s), signal 82)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/7f42dd506807f0307d468e202bbeab6fd7a1e0ea) - `2026-10-16T16:12:09Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/b78d8f30fd4a02347d9a2224b4f72dd359d22299) - `2026-10-16T08:03:38Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/e7206da979816b601bb868f850af07ee30bed56d) - `2026-10-16T04:23:14Z` - azure-sdk (@azure-sdk)
- [CI Update](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/bff6185d6d4603e0c6e0c21e2802e478451fb012) - `2026-10-16T01:17:14Z` - docsreference@microsoft.com
- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/ade1bd67635ea5241318a8faac75f6d356b43ed9) - `2026-10-15T23:05:31Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/dynamics-365-unified-operations-public (7 commit(s), signal 92)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/Dynamics…](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/7dee2e089ec38e2e3fbb1a0bda9269f3d8890347) - `2026-10-16T13:07:06Z` - Learn Build Service GitHub App
- [Merge pull request #22684 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/c34d51b9a530f22802a38b4bc9cbae43dd66c8b0) - `2026-10-16T13:03:30Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [docs: add Planning Optimization October 2026 release notes (#22682)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/dbe374feaa0f750c9ecfb9f6c15a14598e448685) - `2026-10-16T12:51:39Z` - Qi Liu (@liuq-microsoft-service)
- [Merging changes synced from https://github.com/MicrosoftDocs/Dynamics…](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/86ad1c7e8682b247215e5b78c09c3c212ffb7cb7) - `2026-10-15T19:05:36Z` - Learn Build Service GitHub App
- [Merge pull request #22681 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/dc2767b09fd6a42f329cc04b64899f01178fb20c) - `2026-10-15T19:03:20Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### MicrosoftDocs/power-platform (7 commit(s), signal 82)

Tags: `docs, human-authored, product:Azure AI, product:PowerShell, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/41522ae813efd1f3197720f19ce9e2035486d574) - `2026-10-16T01:05:20Z` - Learn Build Service GitHub App
- [Merge pull request #12047 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-platform/commit/91b255bce4af5d77094b0d2de07be97c812367cf) - `2026-10-16T01:03:50Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add Power Platform Admin Cowork setup article (#12031)](https://github.com/MicrosoftDocs/power-platform/commit/70452520e898bb4a4dd33e1e0f33b2aff5ea37ce) - `2026-10-15T20:36:39Z` - Gregg Barker (@Greggbarker-MS)
- [Q1 Governance - Add knowledge sources for agents rule and data policy…](https://github.com/MicrosoftDocs/power-platform/commit/1441cc222fef2a8af2d4b618da57831455284c20) - `2026-10-15T20:29:28Z` - Manjinder (Mints) (@mduelae)
- [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/8c18154ba136654ba625765e6a67361a1af9bb96) - `2026-10-15T19:03:21Z` - Learn Build Service GitHub App

### dotnet/efcore (7 commit(s), signal 47)

Tags: `docs, human-authored`

- [Fix select concat (#39269)](https://github.com/dotnet/efcore/commit/419434f328a9579f335b35dea1f857b7e5f49b04) - `2026-10-16T00:17:36Z` - Aziz-Dhiab (@Aziz-Dhiab) - PR: [Fix select concat](https://github.com/dotnet/efcore/pull/39269)
- [Identify lifted GroupBy groupings by a database-computed rank (#39242)](https://github.com/dotnet/efcore/commit/54be3482356c2072bb3f52ec2ee23216decca8c4) - `2026-10-15T23:50:13Z` - Benedict O'Donovan (@benedict-odonovan) - PR: [Identify lifted GroupBy groupings by a database-computed rank](https://github.com/dotnet/efcore/pull/39242)
- [Differentiate overloaded functions and stored procedures in TableMapp…](https://github.com/dotnet/efcore/commit/dd7fd10750b09d561e67f56ba1799752f9bd3bc3) - `2026-10-15T22:23:39Z` - surya pratap singh (@SkyDevLab) - PR: [Differentiate overloaded functions and stored procedures in TableMappingBaseComparer](https://github.com/dotnet/efcore/pull/39211)
- [Add AggregateFunctionExpression as a relational base for provider agg…](https://github.com/dotnet/efcore/commit/137806dbae6e3923c05b7a7850271ff80a948e09) - `2026-10-15T22:01:14Z` - Abdelrahnam Sayed (@Abde1rahman1) - PR: [Add AggregateFunctionExpression as a relational base for provider aggregate functions](https://github.com/dotnet/efcore/pull/39234)
- [Preserve view comments during scaffolding (#39265)](https://github.com/dotnet/efcore/commit/8ff653707470fffbad8e85a5f734cfc87eae78b3) - `2026-10-15T18:48:43Z` - Shay Rojansky (@roji) - PR: [Preserve view comments during scaffolding](https://github.com/dotnet/efcore/pull/39265)

### MicrosoftDocs/azure-docs-sdk-java (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/2a73a7fe2170053be741cdffd44d219b7100c85d) - `2026-10-16T17:19:41Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/c99a036906d530142e603ab4a326050bba3d7bd2) - `2026-10-16T04:09:18Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/d237f35dbcae38687088a902286f4147856f3bfa) - `2026-10-16T02:35:18Z` - azure-sdk (@azure-sdk)
- [CI Update](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/6dab15726bca8b30ba3c7fceca7ed8cceb040354) - `2026-10-16T01:52:42Z` - docsreference@microsoft.com
- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/7f6980ab8c9f6c8ab27f37035aafba2a00f039a8) - `2026-10-15T23:45:18Z` - azure-sdk (@azure-sdk)

### MicrosoftDocs/azure-monitor-docs (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merge pull request #5641 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/865cd338dd1d8b8d65d418fae5cbda972eb1e4d5) - `2026-10-16T17:05:52Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add health models reliability link to Azure Monitor TOC (#5640)](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/9b7bee7a7e79c67998b82fc8536424424197df49) - `2026-10-16T16:12:47Z` - Kai Nawroth (@kainawroth)
- [Merge pull request #5639 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/4c54223c9030e68ec232fc94b331d40caa8b1f8b) - `2026-10-15T22:12:01Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Apply CBO 1.6 to Dependency Agent policy migration examples (#5559)](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/15c366c9e25674934ef3e03488bb5a72cf5edacc) - `2026-10-15T19:24:25Z` - Kai Nawroth (@kainawroth)
- [Normalize Activity Log query and export examples (#5558)](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/1939dd0814c7b7bb516acd1f5d55fbd63a32ab8b) - `2026-10-15T19:24:08Z` - Kai Nawroth (@kainawroth)

### MicrosoftDocs/azure-management-docs (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Merge pull request #2952 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-management-docs/commit/0b79b52653a18e28dd91c5b5471501076363b590) - `2026-10-16T17:04:21Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Expand Azure Container Registry monitoring metrics guidance (#2951)](https://github.com/MicrosoftDocs/azure-management-docs/commit/d5308cd522a1fe936187eee6a7803c9acb7626fd) - `2026-10-16T16:38:08Z` - Jeanine Burke (@jaysterp)
- [Merge pull request #2950 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-management-docs/commit/f8683f20e8a8e9fa82098c5dc33fd79d9d6d8fec) - `2026-10-15T22:11:58Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #2949 from deankroker/deankroker/deployment-agent-…](https://github.com/MicrosoftDocs/azure-management-docs/commit/feb397197b872cc6ccd48a285db4a9c32bfaac59) - `2026-10-15T20:47:34Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Update Copilot agents and deployment agent docs](https://github.com/MicrosoftDocs/azure-management-docs/commit/66e9b90817f05ff73ddd332e527a327f0f03ab7c) - `2026-10-15T19:31:18Z` - Dean Kroker (@deankroker)

### Azure/azure-sdk-for-go (6 commit(s), signal 71)

Tags: `bot-only, docs, product:Azure SDK, release, watchlist`

- Release: [sdk/resourcemanager/cloudhealth/armcloudhealth/v1.0.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/cloudhealth/armcloudhealth/v1.0.0) - `2026-10-16T16:09:13Z`
- Release: [sdk/resourcemanager/azurestackhci/armazurestackhci/v3.2.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/azurestackhci/armazurestackhci/v3.2.0) - `2026-10-16T07:30:47Z`
- Release: [sdk/resourcemanager/terraform/armterraform/v0.2.0](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/resourcemanager/terraform/armterraform/v0.2.0) - `2026-10-16T02:19:46Z`
- Release: [sdk/security/keyvault/azadmin/v1.6.0-beta.2](https://github.com/Azure/azure-sdk-for-go/releases/tag/sdk/security/keyvault/azadmin/v1.6.0-beta.2) - `2026-10-15T18:58:21Z`
- [[AutoPR sdk-resourcemanager/storage/armstorage]-generated-from-SDK Ge…](https://github.com/Azure/azure-sdk-for-go/commit/c2f2818e158469deb7e74bb953b6295ad7cafd4e) - `2026-10-16T16:47:51Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR sdk-resourcemanager/storage/armstorage]-generated-from-SDK Generation - Go-6960306](https://github.com/Azure/azure-sdk-for-go/pull/27749)
- [[AutoPR sdk-resourcemanager/cloudhealth/armcloudhealth]-generated-fro…](https://github.com/Azure/azure-sdk-for-go/commit/277718db405aaf842f16ecf23a68a51cf3db9d24) - `2026-10-16T15:28:04Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR sdk-resourcemanager/cloudhealth/armcloudhealth]-generated-from-SDK Generation - Go-6963077](https://github.com/Azure/azure-sdk-for-go/pull/27775)
- [[AutoPR sdk-resourcemanager/azurestackhci/armazurestackhci]-generated…](https://github.com/Azure/azure-sdk-for-go/commit/af4b6418bbf242e2a5fa97905a02e3f6e2472a1e) - `2026-10-16T06:45:42Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR sdk-resourcemanager/azurestackhci/armazurestackhci]-generated-from-SDK Generation - Go-6961100](https://github.com/Azure/azure-sdk-for-go/pull/27768)
- [[AutoPR sdk-resourcemanager/terraform/armterraform]-generated-from-SD…](https://github.com/Azure/azure-sdk-for-go/commit/95aefb4c121f878ad97b24710d9e9e4573362474) - `2026-10-16T01:52:11Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR sdk-resourcemanager/terraform/armterraform]-generated-from-SDK Generation - Go-6751159](https://github.com/Azure/azure-sdk-for-go/pull/27465)
- [Configurations:  'specification/cognitiveservices/resource-manager/Mi…](https://github.com/Azure/azure-sdk-for-go/commit/d654c806ca3ce12e4301502b557d43504eb8e369) - `2026-10-15T22:43:48Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR sdk-resourcemanager/cognitiveservices/armcognitiveservices]-generated-from-SDK Generation - Go-6940911](https://github.com/Azure/azure-sdk-for-go/pull/27727)

### Azure/AI-Landing-Zones (6 commit(s), signal 81)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #157 from Azure/feature/customer-docs-final](https://github.com/Azure/AI-Landing-Zones/commit/8a9a55f392d3f73bdf231ad229af53cb4bb28236) - `2026-10-16T15:11:13Z` - Paulo Lacerda (@placerda) - PR: [docs: complete customer deployment and Azure DevOps guidance](https://github.com/Azure/AI-Landing-Zones/pull/157)
- [docs: add customer deployment and gated Azure DevOps guidance](https://github.com/Azure/AI-Landing-Zones/commit/e82986db63fa51b1ea0354f26e0a21c8d5552817) - `2026-10-16T01:11:29Z` - Paulo Lacerda (@placerda) - PR: [docs: complete customer deployment and Azure DevOps guidance](https://github.com/Azure/AI-Landing-Zones/pull/157)
- [Enhance README with details on AI Landing Zones](https://github.com/Azure/AI-Landing-Zones/commit/428ebd8bf4a33d7c2cb03e2354d92465bc32d3ab) - `2026-10-15T18:52:16Z` - Bilal Amjad (@mbilalamjad)
- [Enhance AI Landing Zone documentation with details](https://github.com/Azure/AI-Landing-Zones/commit/bb7cf87096f434f48f6c10bd4953fb561740d428) - `2026-10-15T18:48:25Z` - Bilal Amjad (@mbilalamjad)
- [Update mkdocs.yml](https://github.com/Azure/AI-Landing-Zones/commit/4e5818a62eae68ea1ef51b4a8fb731a4f2850416) - `2026-10-15T18:44:08Z` - Bilal Amjad (@mbilalamjad)

### MicrosoftDocs/architecture-center (6 commit(s), signal 81)

Tags: `docs, human-authored, watchlist`

- [Add guidance on in-flight messages when migrating incrementally with …](https://github.com/MicrosoftDocs/architecture-center/commit/d24d931042d4d28361c339e10d20d913cfc8e207) - `2026-10-16T14:29:32Z` - Bartek Wasielak (@bartekwasielak) - PR: [Add guidance on in-flight messages when migrating incrementally with a Messaging Bridge](https://github.com/MicrosoftDocs/architecture-center/pull/4809)
- [Clarify when Strangler Fig isn't suitable for legacy systems without …](https://github.com/MicrosoftDocs/architecture-center/commit/65641eaec87f99919bdeebdff9b819974107ca55) - `2026-10-16T14:28:14Z` - Bartek Wasielak (@bartekwasielak) - PR: [Clarify when Strangler Fig isn't suitable for legacy systems without source access](https://github.com/MicrosoftDocs/architecture-center/pull/4808)
- [Merge pull request #16969 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/architecture-center/commit/0161a3f3501814726d24113f75e2fc707cb2b8ce) - `2026-10-16T05:03:07Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #16965 from MicrosoftDocs/link-doctor/batch-202610…](https://github.com/MicrosoftDocs/architecture-center/commit/d080564d09e9b35ed70a495b39ddddadbaebb0de) - `2026-10-15T22:19:57Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Improve embedded links in 3 article(s)](https://github.com/MicrosoftDocs/architecture-center/commit/6974910c299c7e5f2b27e37b8f629e255d699475) - `2026-10-15T20:03:18Z` - azure-patterns-practices-assistant[bot] (@azure-patterns-practices-assistant[bot])

### MicrosoftDocs/azure-docs-sdk-python (6 commit(s), signal 81)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/672bcd4bf14028bb0c7310bef70fba50ce35cd01) - `2026-10-16T08:44:15Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/eacd4d9ec4f409c7c1bee841cd78a757b2206722) - `2026-10-16T07:40:32Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/18fb89715b3cfba3697ea423fed03f757d6f6b7d) - `2026-10-16T06:50:18Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/3b6432d3975b9899687cfcd34b0174305ef8569a) - `2026-10-16T06:08:34Z` - azure-sdk (@azure-sdk)
- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/01888310e486d297fb4e2ebc43fa66be0ecb25a2) - `2026-10-16T03:02:56Z` - azure-sdk (@azure-sdk)

### OfficeDev/office-js-docs-reference (6 commit(s), signal 46)

Tags: `docs, human-authored`

- [Bump brace-expansion from 5.0.9 to 5.0.12 in /generate-docs (#2649)](https://github.com/OfficeDev/office-js-docs-reference/commit/6a38c7a75c8de3099cef183d05f7d492bac8407f) - `2026-10-15T20:28:08Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump brace-expansion from 5.0.9 to 5.0.12 in /generate-docs](https://github.com/OfficeDev/office-js-docs-reference/pull/2649)
- [Bump fast-uri from 3.1.7 to 3.1.8 in /generate-docs (#2648)](https://github.com/OfficeDev/office-js-docs-reference/commit/de5255191f3ccd36948c6e734e76037efb18dfc8) - `2026-10-15T20:28:00Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump fast-uri from 3.1.7 to 3.1.8 in /generate-docs](https://github.com/OfficeDev/office-js-docs-reference/pull/2648)
- [Bump brace-expansion from 5.0.7 to 5.0.12 in /generate-docs/scripts (…](https://github.com/OfficeDev/office-js-docs-reference/commit/7a5ed5f9f78aa7f1305fb709723f49584b73b029) - `2026-10-15T20:27:50Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump brace-expansion from 5.0.7 to 5.0.12 in /generate-docs/scripts](https://github.com/OfficeDev/office-js-docs-reference/pull/2647)
- [[Outlook] (modules) Add negative recommendation note (#2644)](https://github.com/OfficeDev/office-js-docs-reference/commit/af984d1ca001934e26fdace5873f21201210d051) - `2026-10-15T17:39:48Z` - Rick Kirkham (@Rick-Kirkham) - PR: [[Outlook] (modules) Add negative recommendation note](https://github.com/OfficeDev/office-js-docs-reference/pull/2644)
- [Bump actions/setup-node from 7.0.0 to 7.1.0 in the github-actions gro…](https://github.com/OfficeDev/office-js-docs-reference/commit/dd2af791ee1d7da43edde048dbb5fe41a29f5fe8) - `2026-10-15T16:57:10Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-node from 7.0.0 to 7.1.0 in the github-actions group](https://github.com/OfficeDev/office-js-docs-reference/pull/2645)

### MicrosoftDocs/azure-devops-docs (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-de…](https://github.com/MicrosoftDocs/azure-devops-docs/commit/15615c428419f39e92d5159dca054975b660737a) - `2026-10-16T13:05:31Z` - Learn Build Service GitHub App
- [Merge pull request #9812 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-devops-docs/commit/ed0097b0487870a2b1efbbffc0b0e766603edccf) - `2026-10-16T13:03:54Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #9810 from ebogatenkov/main](https://github.com/MicrosoftDocs/azure-devops-docs/commit/f074772bd6480879b56bd6d1bf28ab526f672fed) - `2026-10-16T11:56:04Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Fix formatting in service-endpoints.md](https://github.com/MicrosoftDocs/azure-devops-docs/commit/af300fb9a6284c5a3bc6ae48df5a580ecd7e388e) - `2026-10-15T16:52:05Z` - ebogatenkov (@ebogatenkov)
- [Update required scopes for Bitbucket](https://github.com/MicrosoftDocs/azure-devops-docs/commit/45155cd420710cd5243b5bb9f1a5b9fb6afddd63) - `2026-10-15T16:49:35Z` - ebogatenkov (@ebogatenkov)

### microsoft/vscode-edge-devtools (5 commit(s), signal 55)

Tags: `docs, human-authored, release-language`

- [Updating version (#5052)](https://github.com/microsoft/vscode-edge-devtools/commit/d2c50cb82456dc6b62244543541643cf9406a129) - `2026-10-16T05:01:05Z` - Vidal Ortega (@vidorteg) - PR: [Updating to version 2.1.13](https://github.com/microsoft/vscode-edge-devtools/pull/5052)
- [Bump handlebars from 4.7.9 to 4.7.10 (#5048)](https://github.com/microsoft/vscode-edge-devtools/commit/0222721e2e6eccd7e4add5f9ec4f022c32e16a83) - `2026-10-15T18:34:10Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump handlebars from 4.7.9 to 4.7.10](https://github.com/microsoft/vscode-edge-devtools/pull/5048)
- [Bump brace-expansion from 1.1.18 to 1.1.21 (#5047)](https://github.com/microsoft/vscode-edge-devtools/commit/4df415cc24b5dd40aad438c4195d39c5c078b15f) - `2026-10-15T18:29:36Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump brace-expansion from 1.1.18 to 1.1.21](https://github.com/microsoft/vscode-edge-devtools/pull/5047)
- [Restricting setting and launch of browser to trusted workspace (#5049)](https://github.com/microsoft/vscode-edge-devtools/commit/2fc292c74a0be38914fe9eca103adde04ed22fdd) - `2026-10-15T18:15:30Z` - Vidal Ortega (@vidorteg) - PR: [Restricting setting and launch of browser to trusted workspace](https://github.com/microsoft/vscode-edge-devtools/pull/5049)
- [Pinning workflow to a commit and fixing an https validation in utils …](https://github.com/microsoft/vscode-edge-devtools/commit/7e994f0af1fc3ae3f27957cbc8b703512f4ca52c) - `2026-10-15T16:50:41Z` - Vidal Ortega (@vidorteg) - PR: [Pinning workflow to a commit and fixing an https validation in utils](https://github.com/microsoft/vscode-edge-devtools/pull/5046)

### MicrosoftDocs/azure-stack-docs (5 commit(s), signal 80)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #4541 from MicrosoftDocs/main639276986964525991syn…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/aeef9b76e46b319b4bfe312e6d299b2fa65c9fc0) - `2026-10-15T22:05:06Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4541)
- [Merging changes synced from https://github.com/MicrosoftDocs/azure-st…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/66de4a3b7eb0f8b75c9f302f3559a4594fd03d54) - `2026-10-15T22:04:53Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4541)
- [Merge pull request #21899 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-stack-docs/commit/a64a8ab83410c42c4a67dca163faf0289b2808ed) - `2026-10-15T22:03:35Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4541)
- [Merge pull request #21897 from matternst7258/matthewernst/troubleshoo…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/6f95af9bfcfa0ecbf1a906148db959395252e5c7) - `2026-10-15T18:10:24Z` - prmerger-automator[bot] (@prmerger-automator[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4541)
- [Use customer-facing support ticket terminology](https://github.com/MicrosoftDocs/azure-stack-docs/commit/3303e0afdd992708555aaf4a3807e65d5978ed46) - `2026-10-15T18:05:12Z` - Matt Ernst (@matternst7258) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4541)

### MicrosoftDocs/dynamics365-guidance (5 commit(s), signal 90)

Tags: `docs, human-authored, release-language, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365-guidance/commit/23488b4d196ed98f92b5ab89be747265b4ede7da) - `2026-10-15T19:05:59Z` - Learn Build Service GitHub App
- [Merge pull request #1132 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365-guidance/commit/fc84b4b9f534641360b4d0d612b0c00d56ddac61) - `2026-10-15T19:05:24Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Replace release plans with Roadmap (#1129)](https://github.com/MicrosoftDocs/dynamics365-guidance/commit/d28e217cb8bfa3154e50085359d2a94c02e1c023) - `2026-10-15T16:06:06Z` - Eva Dupont (@edupont04)
- [Add deprecation notice for RSAT in testing guide (#1128)](https://github.com/MicrosoftDocs/dynamics365-guidance/commit/5e7178b1b1873ed2d8126d8fb976f1b3f12dc2d4) - `2026-10-15T15:55:07Z` - Eva Dupont (@edupont04)
- [Heer subgrid (#1125)](https://github.com/MicrosoftDocs/dynamics365-guidance/commit/55c6ffb9840ae22ab9d6c19cb93cc2c801ca12a2) - `2026-10-15T15:50:37Z` - Heer Patel (@heerpatelmsft)

### dotnet/docs (4 commit(s), signal 79)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Document the IStartupValidator obsoletion in .NET 11 (#56388)](https://github.com/dotnet/docs/commit/5fe6e4af9a9b21e8e5e84f583097d08cdb1554ea) - `2026-10-16T17:29:51Z` - Copilot (@Copilot) - PR: [Document the IStartupValidator obsoletion in .NET 11](https://github.com/dotnet/docs/pull/56388)
- [Clarify Linux-only extended support for .NET SDK feature bands (#56414)](https://github.com/dotnet/docs/commit/0ca730d84fb650478a2d7dc3910169bc1faba560) - `2026-10-16T14:43:52Z` - Copilot (@Copilot) - PR: [Clarify Linux-only extended support for .NET SDK feature bands](https://github.com/dotnet/docs/pull/56414)
- [Bump Azure.Storage.Blobs across 14 directories (#56377)](https://github.com/dotnet/docs/commit/c078d7fe55030b0e59fb7df35c61133c98bdc24b) - `2026-10-15T21:18:08Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Azure.Storage.Blobs across 14 directories](https://github.com/dotnet/docs/pull/56377)
- [Document dotnetup 0.3.0 self-update, notifications, and uninstall saf…](https://github.com/dotnet/docs/commit/a3fc8c2b42595c84b5b3d98679596d75aa6c9431) - `2026-10-15T15:54:58Z` - Chet Husk (@baronfel) - PR: [Document dotnetup 0.3.0 self-update, notifications, and uninstall safeguards](https://github.com/dotnet/docs/pull/56395)

### microsoft/kiota-serialization-json-go (4 commit(s), signal 129)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [v1.1.5](https://github.com/microsoft/kiota-serialization-json-go/releases/tag/v1.1.5) - `2026-10-16T16:22:47Z`
- [Merge pull request #223 from microsoft/release-please--branches--main…](https://github.com/microsoft/kiota-serialization-json-go/commit/5ecbebd29b78d8290bbb71d2cb98eb602bd3c319) - `2026-10-16T16:22:20Z` - Vincent Biret (@baywet) - PR: [chore(main): release 1.1.5](https://github.com/microsoft/kiota-serialization-json-go/pull/223)
- [chore(main): release 1.1.5](https://github.com/microsoft/kiota-serialization-json-go/commit/86b967c3067a613b0e26edebe5e8dcc90f1e3ea1) - `2026-10-16T16:19:17Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(main): release 1.1.5](https://github.com/microsoft/kiota-serialization-json-go/pull/223)
- [Merge pull request #222 from rksharma-owg/codex/fix-time-read-mutation](https://github.com/microsoft/kiota-serialization-json-go/commit/c0223bd9d2f6f9f2cc1aa4c56666c29608506916) - `2026-10-16T16:18:05Z` - Vincent Biret (@baywet) - PR: [fix: preserve source strings when parsing timestamps](https://github.com/microsoft/kiota-serialization-json-go/pull/222)
- [fix: preserve source strings when parsing timestamps](https://github.com/microsoft/kiota-serialization-json-go/commit/b666c8be53aee6c8b5f9fc616df8aa33edda416a) - `2026-10-16T14:53:43Z` - RKS (@rksharma-owg) - PR: [fix: preserve source strings when parsing timestamps](https://github.com/microsoft/kiota-serialization-json-go/pull/222)

### microsoft/kiota-serialization-text-go (4 commit(s), signal 129)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [v1.1.4](https://github.com/microsoft/kiota-serialization-text-go/releases/tag/v1.1.4) - `2026-10-16T16:18:35Z`
- [Merge pull request #168 from microsoft/release-please--branches--main…](https://github.com/microsoft/kiota-serialization-text-go/commit/aa18a1c65ecf8b8d7f7301e18e11b3979e3f4e0a) - `2026-10-16T16:18:11Z` - Vincent Biret (@baywet) - PR: [chore(main): release 1.1.4](https://github.com/microsoft/kiota-serialization-text-go/pull/168)
- [chore(main): release 1.1.4](https://github.com/microsoft/kiota-serialization-text-go/commit/497a8f9f0a55edf5c992ba3d3c76929331e814e4) - `2026-10-16T16:16:57Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(main): release 1.1.4](https://github.com/microsoft/kiota-serialization-text-go/pull/168)
- [Merge pull request #167 from rksharma-owg/codex/fix-text-timestamp-fo…](https://github.com/microsoft/kiota-serialization-text-go/commit/0287efb8ab5c2a42812b95b803c81ddfc47dc1da) - `2026-10-16T16:15:30Z` - Vincent Biret (@baywet) - PR: [fix: serialize text timestamps in RFC3339 format](https://github.com/microsoft/kiota-serialization-text-go/pull/167)
- [fix: serialize text timestamps in RFC3339 format](https://github.com/microsoft/kiota-serialization-text-go/commit/887e2031da0039d2d1d57b3d7b7ddd5487c30d5f) - `2026-10-16T14:38:22Z` - RKS (@rksharma-owg) - PR: [fix: serialize text timestamps in RFC3339 format](https://github.com/microsoft/kiota-serialization-text-go/pull/167)

### microsoft/kiota-http-go (4 commit(s), signal 129)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [v1.5.8](https://github.com/microsoft/kiota-http-go/releases/tag/v1.5.8) - `2026-10-16T16:18:12Z`
- [Merge pull request #280 from microsoft/release-please--branches--main…](https://github.com/microsoft/kiota-http-go/commit/bf49a6b007902e4570c7e867691c07e11bef15d6) - `2026-10-16T16:17:43Z` - Vincent Biret (@baywet) - PR: [chore(main): release 1.5.8](https://github.com/microsoft/kiota-http-go/pull/280)
- [chore(main): release 1.5.8](https://github.com/microsoft/kiota-http-go/commit/1dd824dc9d2fb640da5582b81a1b9e2bf984dace) - `2026-10-16T16:15:40Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(main): release 1.5.8](https://github.com/microsoft/kiota-http-go/pull/280)
- [Merge pull request #279 from rksharma-owg/codex/fix-content-type-whit…](https://github.com/microsoft/kiota-http-go/commit/32892818f847672a79d3a45e70098281411f6dfb) - `2026-10-16T16:14:58Z` - Vincent Biret (@baywet) - PR: [fix: trim response media types before parser lookup](https://github.com/microsoft/kiota-http-go/pull/279)
- [fix: trim response media types before parser lookup](https://github.com/microsoft/kiota-http-go/commit/3033fb6c57f06ecd1427c7402a8d463c0dccf2cd) - `2026-10-16T16:02:12Z` - RKS (@rksharma-owg) - PR: [fix: trim response media types before parser lookup](https://github.com/microsoft/kiota-http-go/pull/279)

### MicrosoftDocs/powerapps-docs (4 commit(s), signal 89)

Tags: `docs, human-authored, release-language, watchlist`

- [Clarify supported content types for app creation (#5547)](https://github.com/MicrosoftDocs/powerapps-docs/commit/a0ec57c6e9567a285cce39b5f05f2fe425dec1b8) - `2026-10-16T16:00:15Z` - Jessica Lo (@jessicaszelo) - PR: [Clarify supported content types for app creation](https://github.com/MicrosoftDocs/powerapps-docs/pull/5547)
- [Merging changes synced from https://github.com/MicrosoftDocs/powerapp…](https://github.com/MicrosoftDocs/powerapps-docs/commit/4d9cac9516bfe08972330bdfc6b5c2bc05921d45) - `2026-10-15T19:06:35Z` - Learn Build Service GitHub App
- [Merge pull request #12737 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/powerapps-docs/commit/4ecbeeab716b20c0dd8a2d334e7b6ab206851f10) - `2026-10-15T19:03:28Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add standard PP preview disclaimers for BAWIQ content (#12736)](https://github.com/MicrosoftDocs/powerapps-docs/commit/2bca8cabc56ffe3fdd844caebd085812c23ce30e) - `2026-10-15T17:15:39Z` - Erika Doyle Navara (@erikadoyle)

### microsoft/kiota-java (4 commit(s), signal 19)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #2206 from microsoft/dependabot/gradle/com.diffplu…](https://github.com/microsoft/kiota-java/commit/a9fb313931471590b5473c06c08334dd1fe6bd59) - `2026-10-16T10:05:33Z` - github-actions[bot] (@github-actions[bot]) - PR: [chore(deps): bump com.diffplug.spotless from 8.10.3 to 8.10.4](https://github.com/microsoft/kiota-java/pull/2206)
- [Merge pull request #2207 from microsoft/dependabot/github_actions/cod…](https://github.com/microsoft/kiota-java/commit/134d9e0a8100c90f8a0c8a6d70ac881545ef5069) - `2026-10-16T10:05:04Z` - github-actions[bot] (@github-actions[bot]) - PR: [chore(deps): bump the codeql group with 3 updates](https://github.com/microsoft/kiota-java/pull/2207)
- [chore(deps): bump the codeql group with 3 updates](https://github.com/microsoft/kiota-java/commit/8c024eb8eb078da3197f3479f8b3b81fcb54e90c) - `2026-10-15T22:35:39Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump the codeql group with 3 updates](https://github.com/microsoft/kiota-java/pull/2207)
- [chore(deps): bump com.diffplug.spotless from 8.10.3 to 8.10.4](https://github.com/microsoft/kiota-java/commit/3d010de09718a7b0b8a7b362def7d8cc7128643b) - `2026-10-15T22:33:02Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump com.diffplug.spotless from 8.10.3 to 8.10.4](https://github.com/microsoft/kiota-java/pull/2206)

### MicrosoftLearning/trainer-demo-deploy (4 commit(s), signal 79)

Tags: `human-authored, training, watchlist`

- [Merge pull request #131 from massimobonanni/db-vector-search-demo](https://github.com/MicrosoftLearning/trainer-demo-deploy/commit/4e0bf19f729bebd7e9ddf7118b22c1eac0c56dcd) - `2026-10-16T00:02:29Z` - Peter De Tender (@petender) - PR: [Add DB Semantic Search demo with Azure and PostgreSQL](https://github.com/MicrosoftLearning/trainer-demo-deploy/pull/131)
- [Merge branch 'main' into db-vector-search-demo](https://github.com/MicrosoftLearning/trainer-demo-deploy/commit/ffc8ae1f258c5c16e4ceb46f9f59f4e7fb4a178e) - `2026-10-16T00:02:04Z` - Peter De Tender (@petender) - PR: [Add DB Semantic Search demo with Azure and PostgreSQL](https://github.com/MicrosoftLearning/trainer-demo-deploy/pull/131)
- [Merge pull request #161 from koenraadhaedens/main](https://github.com/MicrosoftLearning/trainer-demo-deploy/commit/513024fc2a73d3299e41588073776c2ea1a0c08a) - `2026-10-15T23:55:45Z` - Peter De Tender (@petender) - PR: [Revise title and description for Odoo demo project](https://github.com/MicrosoftLearning/trainer-demo-deploy/pull/161)
- [Merge pull request #162 from MicrosoftLearning/dependabot/github_acti…](https://github.com/MicrosoftLearning/trainer-demo-deploy/commit/68627bb22bbe88f197302fcfcae0879ca04035b6) - `2026-10-15T23:54:57Z` - Peter De Tender (@petender) - PR: [build(deps): bump actions/setup-node from 7.0.0 to 7.1.0 in the github-actions group](https://github.com/MicrosoftLearning/trainer-demo-deploy/pull/162)

### Azure/azure-sdk-for-rust (4 commit(s), signal 79)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update chacha20, quinn-proto (#5461)](https://github.com/Azure/azure-sdk-for-rust/commit/8287ea45ca26459c1e6718bb51b5e277adafcb3b) - `2026-10-15T22:16:32Z` - Heath Stewart (@heaths) - PR: [Update chacha20, quinn-proto](https://github.com/Azure/azure-sdk-for-rust/pull/5461)
- [Avoid no-op Cosmos hedge state updates (#5438)](https://github.com/Azure/azure-sdk-for-rust/commit/714d5624c61934bcb17463b3701ab2fff9ff251a) - `2026-10-15T22:16:08Z` - Tomas Varon (@tvaron3) - PR: [Avoid no-op Cosmos hedge state updates](https://github.com/Azure/azure-sdk-for-rust/pull/5438)
- [Bump the github-actions group with 2 updates (#5460)](https://github.com/Azure/azure-sdk-for-rust/commit/d113d9bffaa1373962811bc0c4574a542e801c7b) - `2026-10-15T21:47:04Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the github-actions group with 2 updates](https://github.com/Azure/azure-sdk-for-rust/pull/5460)
- [Sync eng/common directory with azure-sdk-tools for PR 17240 (#5458)](https://github.com/Azure/azure-sdk-for-rust/commit/f8de7c4256db53feaf5783b3600c388776409814) - `2026-10-15T17:28:55Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17240](https://github.com/Azure/azure-sdk-for-rust/pull/5458)

### microsoft/BuildXL (4 commit(s), signal 89)

Tags: `human-authored, product:Azure AI, release-language, samples, watchlist`

- [Merged PR 965669: Add Agency PR review agent](https://github.com/microsoft/BuildXL/commit/dff214a583408ee9fa9429eb7dc186d1cc7ad186) - `2026-10-15T20:56:00Z` - Semih Okur (@semihokur)
- [Merged PR 964470: Make QTest result publishing best effort for unoffi…](https://github.com/microsoft/BuildXL/commit/2faae45d39f48c06f5abf3542254dfdb7955c9a6) - `2026-10-15T20:47:22Z` - Michael Pysson (@mpysson)
- [Merged PR 965586: Update BuildXL LKG Version to 0.1.0-20261014.5](https://github.com/microsoft/BuildXL/commit/33e1f80e8404e7c4f6715a80c3b23ff958f6d86a) - `2026-10-15T17:50:26Z` - BuildXL-Pipelines
- [Merged PR 965575: Enable Agency pull request reviews](https://github.com/microsoft/BuildXL/commit/8782d1593b3c8fe54f2c7223641b903eadcef599) - `2026-10-15T17:37:27Z` - Semih Okur (@semihokur)

### microsoft/AzureTRE (3 commit(s), signal 43)

Tags: `human-authored, samples`

- [Stabilise certificate provisioning and reuse (#5254)](https://github.com/microsoft/AzureTRE/commit/fbd79d4646570302b42dbc3ab7c5962fda4c977a) - `2026-10-16T17:28:44Z` - Jay W (@JayDoubleu) - PR: [Stabilise certificate provisioning and reuse](https://github.com/microsoft/AzureTRE/pull/5254)
- [Fix bundle execution, VM prerequisites and uninstall status (#5253)](https://github.com/microsoft/AzureTRE/commit/5e585aae81d90305b1d84a970d55a1d279341522) - `2026-10-16T17:16:30Z` - Jay W (@JayDoubleu) - PR: [Fix bundle execution, VM prerequisites and uninstall status](https://github.com/microsoft/AzureTRE/pull/5253)
- [Harden core deployment and preserve Terraform outputs (#5252)](https://github.com/microsoft/AzureTRE/commit/59048f853c88e16bb742e8af72c61c8947b2d57e) - `2026-10-16T17:02:09Z` - Jay W (@JayDoubleu) - PR: [Harden core deployment and preserve Terraform outputs](https://github.com/microsoft/AzureTRE/pull/5252)

### Azure/dacs (3 commit(s), signal 28)

Tags: `bot-only, dependency-noise, release-language, samples, watchlist`

- [build(deps): bump the pip-version-updates group across 2 directories …](https://github.com/Azure/dacs/commit/ca2ec164625cfa111bb5c2cf3630acd8f9681b74) - `2026-10-16T14:18:19Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump the pip-version-updates group across 2 directories with 3 updates](https://github.com/Azure/dacs/pull/113)
- [build(deps): bump the docker group across 2 directories with 2 updates](https://github.com/Azure/dacs/commit/5285753c932b2a080b7af7d84cd9d121980092d1) - `2026-10-15T17:52:45Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump the docker group across 2 directories with 2 updates](https://github.com/Azure/dacs/pull/109)
- [ci(deps): bump the github-actions group across 1 directory with 7 upd…](https://github.com/Azure/dacs/commit/e1dc0e6ab279717a345a972450faec587573cc17) - `2026-10-15T17:44:14Z` - dependabot[bot] (@dependabot[bot]) - PR: [ci(deps): bump the github-actions group across 1 directory with 7 updates](https://github.com/Azure/dacs/pull/114)

### microsoft/power-pages-samples (3 commit(s), signal 53)

Tags: `docs, human-authored, release-language`

- [Fix Starter Layout 2 subpage preview (#209)](https://github.com/microsoft/power-pages-samples/commit/317cc1b03320c046ad5168e1f6104eda3325b0c6) - `2026-10-16T10:00:55Z` - Priyanshu Agrawal (@priyanshu92) - PR: [Fix Starter Layout 2 subpage preview](https://github.com/microsoft/power-pages-samples/pull/209)
- [add starter templates (#207)](https://github.com/microsoft/power-pages-samples/commit/7018a340e31010ee60b1da2b7a315babb72deaf0) - `2026-10-16T08:50:16Z` - Sandeep Satheesh (@sanxsth) - PR: [Add Starter Layout 2–5 templates](https://github.com/microsoft/power-pages-samples/pull/207)
- [docs: add templates to root README (#206)](https://github.com/microsoft/power-pages-samples/commit/db3fe8f3f31062a216ccf744dd4828913e581abe) - `2026-10-16T06:46:08Z` - Priyanshu Agrawal (@priyanshu92) - PR: [docs: add non-SPA and SPA templates to the root README](https://github.com/microsoft/power-pages-samples/pull/206)

### MicrosoftDocs/dynamics-365-customer-engagement (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement/commit/da4c8ecffb3c8fbd4c5c43cb46e6216bdb684698) - `2026-10-16T01:07:48Z` - Learn Build Service GitHub App
- [Merge pull request #17220 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement/commit/a8518857d8f5e733a30511fa404530d1ad2069d3) - `2026-10-16T01:04:03Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update side pane chat topic (#17214)](https://github.com/MicrosoftDocs/dynamics-365-customer-engagement/commit/d915d9eba0ec3765481604d2c9092bb1ddbd02dc) - `2026-10-15T23:15:11Z` - puneet-singh1 (@puneet-singh1)

### MicrosoftDocs/azure-dev-docs (3 commit(s), signal 78)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/azure-de…](https://github.com/MicrosoftDocs/azure-dev-docs/commit/0d5bf019d36951471fd4297cf9af4efe9934875c) - `2026-10-15T23:02:53Z` - Learn Build Service GitHub App
- [Merge pull request #9918 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-dev-docs/commit/1b5e263a0cdbf045ffd6ce1ff1fbc125a72e989a) - `2026-10-15T23:02:04Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add custom model guidance for GitHub Copilot modernization (#9909)](https://github.com/MicrosoftDocs/azure-dev-docs/commit/47397f124970b1fc401af8688c5622449b606c20) - `2026-10-15T22:20:57Z` - puicchan (@puicchan)

### MicrosoftDocs/office-docs-powershell (3 commit(s), signal 88)

Tags: `docs, human-authored, product:PowerShell, release-language, watchlist`

- [FileTypeCustomization changes Set-CsTeamsMessagingConfiguration.md (#…](https://github.com/MicrosoftDocs/office-docs-powershell/commit/c5386f4fae7364d13ae8759abb6bbe1fc1be0dde) - `2026-10-15T21:34:11Z` - vinhvienms (@vinhvienms) - PR: [File Type Customization document added to TeamsMessagingConfiguration](https://github.com/MicrosoftDocs/office-docs-powershell/pull/13834)
- [Clarify recording and transcription audio notification scope and clie…](https://github.com/MicrosoftDocs/office-docs-powershell/commit/b774a4406bc6ad48c99694a10a647f19c511c161) - `2026-10-15T16:09:27Z` - cerise111 (@cerise111) - PR: [Clarify recording and transcription audio notification scope and client support](https://github.com/MicrosoftDocs/office-docs-powershell/pull/13832)
- [Update New-CsTeamsComplianceRecordingPolicy (#13790)](https://github.com/MicrosoftDocs/office-docs-powershell/commit/bbb6f12c4807a52ce6d1d36ce505c095ab7a34bd) - `2026-10-15T15:56:45Z` - Olga (@olsax) - PR: [Update New-CsTeamsComplianceRecordingPolicy](https://github.com/MicrosoftDocs/office-docs-powershell/pull/13790)

### MicrosoftDocs/data-tools (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #942 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/data-tools/commit/8301d71e1921df7450afc7fb559552175ad43bb6) - `2026-10-15T21:01:47Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Merge pull request #941 from MicrosoftDocs/repo_sync_working_branch](https://github.com/MicrosoftDocs/data-tools/commit/3441c2fb1d0f91f8d75717ce20818f928d21219a) - `2026-10-15T19:54:07Z` - prmerger-automator[bot] (@prmerger-automator[bot])
- [Modify certutil commands for certificate installation (#38)](https://github.com/MicrosoftDocs/data-tools/commit/2a2a4c2b51a9a8592748b2451bf84d216dd6abbe) - `2026-10-15T17:52:05Z` - Markus Michalski (@MarkusMichalski) - PR: [Modify certutil commands for certificate installation](https://github.com/MicrosoftDocs/data-tools/pull/38)

### MicrosoftDocs/dynamics-365-project-operations (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/a7f826136cc34561bd4e285ed9d1dc957e9ab6ec) - `2026-10-15T19:02:35Z` - Learn Build Service GitHub App
- [Merge pull request #2798 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/52865143df08e23658697e6846a043f6f6e28bdd) - `2026-10-15T19:02:07Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Add accounting date field description to invoice summary (#2795)](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/aa2e184ef4dc39bb9ee1ea640c139367436a90b9) - `2026-10-15T17:22:30Z` - Namita Shrivastava (@NamitaShri)

### MicrosoftDocs/cpp-docs (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #5978 from MicrosoftDocs/main639276825140184678syn…](https://github.com/MicrosoftDocs/cpp-docs/commit/50c4fa88e98f89ea36aa4b15b9f13bee964ed380) - `2026-10-15T17:35:24Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/cpp-docs/pull/5978)
- [Merging changes synced from https://github.com/MicrosoftDocs/cpp-docs…](https://github.com/MicrosoftDocs/cpp-docs/commit/ddc610baf23b44808586b9e5293a9b8bd419c289) - `2026-10-15T17:35:11Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/cpp-docs/pull/5978)
- [Merge pull request #6853 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/cpp-docs/commit/c77ef42fcb02e24619232f9e574526433ad50235) - `2026-10-15T17:34:07Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/cpp-docs/pull/5978)

### MicrosoftDocs/visualstudio-docs (3 commit(s), signal 78)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #11465 from MicrosoftDocs/main639276770908753134sy…](https://github.com/MicrosoftDocs/visualstudio-docs/commit/019f0e3aa1e59b877b2bb71962c3af12ce60357a) - `2026-10-15T16:05:08Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11465)
- [Merging changes synced from https://github.com/MicrosoftDocs/visualst…](https://github.com/MicrosoftDocs/visualstudio-docs/commit/1cc23b04a168e4e96e612b656dd26253e2193071) - `2026-10-15T16:04:47Z` - Learn Build Service GitHub App - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11465)
- [Merge pull request #15758 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/visualstudio-docs/commit/b4d5d9ad298300cb51827731b5e941d7720b3441) - `2026-10-15T16:02:09Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11465)

### microsoft/XBOX-Godot-Sample (2 commit(s), signal 77)

Tags: `human-authored, samples, watchlist`

- [Add support configuration for GDK 2604.3.7874 (#207)](https://github.com/microsoft/XBOX-Godot-Sample/commit/4720571830983dfc1d2192f81c91b845d317d18a) - `2026-10-16T17:32:00Z` - Copilot (@Copilot) - PR: [Add support configuration for GDK 2604.3.7874](https://github.com/microsoft/XBOX-Godot-Sample/pull/207)
- [Add local PR validation: fresh checkout, live-write engine matrix, PR…](https://github.com/microsoft/XBOX-Godot-Sample/commit/e3f45d6829a04dfeee67db2e9d34a43279df2bf6) - `2026-10-15T21:19:46Z` - James Lenell (@jameslen-atg) - PR: [Add local PR validation: fresh checkout, live-write engine matrix, PR evidence](https://github.com/microsoft/XBOX-Godot-Sample/pull/203)

### Azure/LogicAppsUX (2 commit(s), signal 117)

Tags: `docs, human-authored, release, watchlist`

- Release: [Release v5.1010.0](https://github.com/Azure/LogicAppsUX/releases/tag/v5.1010.0) - `2026-10-15T17:09:02Z`
- [perf(vscode): Move Azurite, C#, and C# dev kit dependencies to extens…](https://github.com/Azure/LogicAppsUX/commit/36868588a5f0d172b05e331be1e06a9dbc072112) - `2026-10-16T17:24:09Z` - Andrew Eldridge (@andrew-eldridge) - PR: [perf(vscode): Move Azurite, C#, and C# dev kit dependencies to extensionPack](https://github.com/Azure/LogicAppsUX/pull/9663)
- [fix(DesignerV2): show workflow note controls on hover (#9661)](https://github.com/Azure/LogicAppsUX/commit/d9de21f7c364c3dee252e81d5cd79cb82e673068) - `2026-10-15T17:12:14Z` - Riley Evans (@rllyy97) - PR: [fix(DesignerV2): show workflow note controls on hover](https://github.com/Azure/LogicAppsUX/pull/9661)

### Azure-Samples/azuresandbox (2 commit(s), signal 127)

Tags: `human-authored, release, release-language, samples, watchlist`

- Release: [Azure Sandbox v5.14.3](https://github.com/Azure-Samples/azuresandbox/releases/tag/v5.14.3) - `2026-10-15T20:15:41Z`
- [Register release static CI gating on main (#857)](https://github.com/Azure-Samples/azuresandbox/commit/8528d93078bf38acff9387dc96f249990f1f0f68) - `2026-10-16T17:12:17Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Register release static CI gating on main (#854)](https://github.com/Azure-Samples/azuresandbox/pull/857)
- [Merge pull request #852 from Azure-Samples/vnext](https://github.com/Azure-Samples/azuresandbox/commit/e2a63ef4dc1697050f2ca78743f081a8d6fa55af) - `2026-10-15T20:14:26Z` - Roger Doherty (MSFT) (@doherty100) - PR: [Release: promote vnext to main](https://github.com/Azure-Samples/azuresandbox/pull/852)

### MicrosoftDocs/sysinternals (2 commit(s), signal 87)

Tags: `docs, human-authored, release-language, watchlist`

- [Update dates and PsKill version (#1017)](https://github.com/MicrosoftDocs/sysinternals/commit/d46b5bfa4b1151a3dbcf568152cb56a4a9f7c032) - `2026-10-16T16:57:35Z` - Alex Mihaiuc (@foxmsft) - PR: [Update dates and PsKill version](https://github.com/MicrosoftDocs/sysinternals/pull/1017)
- [Add code for the October 2026 publish (#1014)](https://github.com/MicrosoftDocs/sysinternals/commit/ddc34ef9963df344b6184a84dc964a976cee07ed) - `2026-10-15T23:53:03Z` - Alex Mihaiuc (@foxmsft) - PR: [Add code for the October 2026 publish](https://github.com/MicrosoftDocs/sysinternals/pull/1014)

### MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect (2 commit(s), signal 102)

Tags: `human-authored, security, training, watchlist`

- [Merge pull request #92 from MicrosoftLearning/v-absamim-patch-1](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect/commit/7264af65f10d7a2c574309f410cfd65d96bee80c) - `2026-10-16T16:53:00Z` - v-absamim (@v-absamim) - PR: [Update user selection instructions in lab document](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect/pull/92)
- [Merge pull request #93 from MicrosoftLearning/v-absamim-patch-2](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect/commit/5f41d10f8d6df0456da15aef6dc7be454a50363d) - `2026-10-16T16:52:29Z` - v-absamim (@v-absamim) - PR: [Update retention policy settings terminology](https://github.com/MicrosoftLearning/SC-100-Microsoft-Cybersecurity-Architect/pull/93)

### MicrosoftDocs/m365copilot-docs (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [Fix unnecesary comma in Scopes in foundry.md (#123)](https://github.com/MicrosoftDocs/m365copilot-docs/commit/63f813279221edd39897ca3d5459f8f8c22e6224) - `2026-10-16T16:49:30Z` - Maciej Kępa (@maciejkepa) - PR: [Fix unnecesary comma in Scopes in foundry.md](https://github.com/MicrosoftDocs/m365copilot-docs/pull/123)
- [Resolve syncing conflicts from repo_sync_working_branch to main (#127)](https://github.com/MicrosoftDocs/m365copilot-docs/commit/6f2b85db416e6f6ed45e1c7a5f980fbe1d920f31) - `2026-10-16T16:44:22Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Resolve syncing conflicts from repo_sync_working_branch to main](https://github.com/MicrosoftDocs/m365copilot-docs/pull/127)

### microsoft/kiota-abstractions-go (2 commit(s), signal 127)

Tags: `docs, human-authored, product:Azure SDK, product:Microsoft Graph, release, release-language, watchlist`

- Release: [v1.11.2](https://github.com/microsoft/kiota-abstractions-go/releases/tag/v1.11.2) - `2026-10-16T16:27:46Z`
- [chore(main): release 1.11.2 (#288)](https://github.com/microsoft/kiota-abstractions-go/commit/685bbbcfa9428be4da85acb6b28a80b09bb87a1f) - `2026-10-16T16:27:20Z` - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(main): release 1.11.2](https://github.com/microsoft/kiota-abstractions-go/pull/288)
- [fix: preserve original serialization start callbacks (#287)](https://github.com/microsoft/kiota-abstractions-go/commit/4c759ff17b8c6e84eff0097ebd23d97b2868603e) - `2026-10-16T16:24:07Z` - RKS (@rksharma-owg) - PR: [fix: preserve original serialization start callbacks](https://github.com/microsoft/kiota-abstractions-go/pull/287)

### MicrosoftDocs/azure-docs-sdk-cpp (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-cpp/commit/25b47d5e5ccc5e46373ebf9014bdba3a0cae2d4c) - `2026-10-16T16:07:47Z` - azure-sdk (@azure-sdk)
- [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-cpp/commit/15982cb608faa25e344832dfd339fe1854c25bc0) - `2026-10-15T23:17:26Z` - azure-sdk (@azure-sdk)

### dotnet/docs-actions (2 commit(s), signal 42)

Tags: `docs, human-authored`

- [Add intro logging (#27)](https://github.com/dotnet/docs-actions/commit/8a59404cc5ed44c3f3f4e5afe513ebfa15286df7) - `2026-10-16T14:26:02Z` - Genevieve Warren (@gewarren) - PR: [Add intro logging](https://github.com/dotnet/docs-actions/pull/27)
- [Bump the github-actions group with 5 updates (#33)](https://github.com/dotnet/docs-actions/commit/0423860a660ff661db5dbfef394d3f6da721d4c0) - `2026-10-15T16:48:21Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the github-actions group with 5 updates](https://github.com/dotnet/docs-actions/pull/33)

### dotnet/AspNetCore.Docs (2 commit(s), signal 42)

Tags: `docs, human-authored`

- [Document client result cancellation tokens (#37908)](https://github.com/dotnet/AspNetCore.Docs/commit/cade1f204d1aba0fb1b88b2fea8acd7906b5df02) - `2026-10-16T12:28:05Z` - Brennan (@BrennanConroy) - PR: [Document cancellation tokens for SignalR client results](https://github.com/dotnet/AspNetCore.Docs/pull/37908)
- [Bump Microsoft.AspNetCore.Identity.EntityFrameworkCore across 19 dire…](https://github.com/dotnet/AspNetCore.Docs/commit/86e7954a0ffed92d8a3c53041a06ec0a9ae7b87e) - `2026-10-16T01:50:38Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.AspNetCore.Identity.EntityFrameworkCore across 19 directories](https://github.com/dotnet/AspNetCore.Docs/pull/37898)

### Azure-Samples/foundry-local-model-catalog (2 commit(s), signal 77)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Merge pull request #95 from Azure-Samples/update-catalog-186068707](https://github.com/Azure-Samples/foundry-local-model-catalog/commit/b5dec2b135e6800c6eb7ed3f00c618a07a27cd51) - `2026-10-16T10:05:38Z` - Schtechel (@Schtechel) - PR: [Update MODEL_CATALOG.md (186068707)](https://github.com/Azure-Samples/foundry-local-model-catalog/pull/95)
- [Update MODEL_CATALOG.md (build 186068707)](https://github.com/Azure-Samples/foundry-local-model-catalog/commit/184ac7a381d74a77f13bab277577e6c4b4c60aa0) - `2026-10-16T03:06:08Z` - ado-pr-bot - PR: [Update MODEL_CATALOG.md (186068707)](https://github.com/Azure-Samples/foundry-local-model-catalog/pull/95)

### microsoft/kiota-ruby (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #182 from microsoft/dependabot/github_actions/ruby…](https://github.com/microsoft/kiota-ruby/commit/5c84e597858f10233803136ce6bcc4c6be1b05b0) - `2026-10-16T10:05:26Z` - github-actions[bot] (@github-actions[bot]) - PR: [build(deps): bump ruby/setup-ruby from 1.327.0 to 1.328.0](https://github.com/microsoft/kiota-ruby/pull/182)
- [build(deps): bump ruby/setup-ruby from 1.327.0 to 1.328.0](https://github.com/microsoft/kiota-ruby/commit/ba211e7852952610754b304201302f3d9efba6da) - `2026-10-16T00:06:21Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump ruby/setup-ruby from 1.327.0 to 1.328.0](https://github.com/microsoft/kiota-ruby/pull/182)

### dotnet/docfx (2 commit(s), signal 42)

Tags: `docs, human-authored`

- [fix: navigate PDF links and bookmarks to page tops (#11196)](https://github.com/dotnet/docfx/commit/a22ecef659497b64eb1be2d36e50f739d41915c7) - `2026-10-16T07:17:24Z` - Liangying.Wei (@vicancy) - PR: [fix: navigate PDF links and bookmarks to page tops](https://github.com/dotnet/docfx/pull/11196)
- [chore: Revert latest `samples\csharp\docfx.json` and update test snap…](https://github.com/dotnet/docfx/commit/a2408f1f7de5e47257d785a15a1617404a29d780) - `2026-10-15T23:33:18Z` - filzrev (@filzrev) - PR: [chore: Revert latest `samples\csharp\docfx.json` and update test snapshots](https://github.com/dotnet/docfx/pull/10968)

### microsoft/pylance-release (2 commit(s), signal 127)

Tags: `docs, human-authored, release, release-language, watchlist`

- Release: [2026.4.101](https://github.com/microsoft/pylance-release/releases/tag/2026.4.101) - `2026-10-16T16:18:15Z`
- [Sync Pylance documentation with 2026.4.1 (#8266)](https://github.com/microsoft/pylance-release/commit/b946877fc1245510cdf55850546fc48cb44129fe) - `2026-10-16T04:53:51Z` - Heejae Chang (@heejaechang) - PR: [Sync Pylance documentation with 2026.4.1](https://github.com/microsoft/pylance-release/pull/8266)
- [Changelog, etc for 2026.4.101 (#8267)](https://github.com/microsoft/pylance-release/commit/0cf10140b2fbb94ceebeab1675d7ca231bf3dcac) - `2026-10-16T04:41:05Z` - Bill Schnurr (@bschnurr) - PR: [Changelog, etc for 2026.4.101](https://github.com/microsoft/pylance-release/pull/8267)

### microsoft/perfview (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Expand Perfcollect CI Coverage (#2492)](https://github.com/microsoft/perfview/commit/65026df998f224dbb30be9a211e82c0ae18225c7) - `2026-10-16T00:18:03Z` - Brian Robbins (@brianrob) - PR: [Expand Perfcollect CI Coverage](https://github.com/microsoft/perfview/pull/2492)
- [Fix Capitalize in GetManifestForRegisteredProvider (#2481)](https://github.com/microsoft/perfview/commit/895882291717a57c0f301f6cadc416b3cb3c4149) - `2026-10-15T23:49:21Z` - John U (@jdu2600) - PR: [Fix Capitalize in GetManifestForRegisteredProvider event names](https://github.com/microsoft/perfview/pull/2481)

### microsoft/WindowsAppSDK (2 commit(s), signal 77)

Tags: `docs, human-authored, product:Azure SDK, watchlist`

- [Add some cleanup actions to the policy bot (#6851)](https://github.com/microsoft/WindowsAppSDK/commit/46f769ce282bb450c80bd9e9168fd2ebe2a089ea) - `2026-10-16T00:17:36Z` - Lauren Ciha (@lauren-ciha) - PR: [Add some cleanup actions to the policy bot](https://github.com/microsoft/WindowsAppSDK/pull/6851)
- [Add Reactor single-file app template (reactor-singlefile) (#6844)](https://github.com/microsoft/WindowsAppSDK/commit/f5d43facd62128fb3b0b22ea933da7ff583f9d36) - `2026-10-15T20:27:13Z` - Alexandre Zollinger Chohfi (@azchohfi) - PR: [Add Reactor single-file app template (reactor-singlefile)](https://github.com/microsoft/WindowsAppSDK/pull/6844)

### Azure/azure-sdk-for-cpp (2 commit(s), signal 117)

Tags: `docs, human-authored, product:Azure SDK, release, watchlist`

- Release: [azure-template_1.1.0-beta.6967811](https://github.com/Azure/azure-sdk-for-cpp/releases/tag/azure-template_1.1.0-beta.6967811) - `2026-10-16T15:54:09Z`
- Release: [azure-template_1.1.0-beta.6967166](https://github.com/Azure/azure-sdk-for-cpp/releases/tag/azure-template_1.1.0-beta.6967166) - `2026-10-16T13:32:16Z`
- [Update C++ APIView parser to 20261009.3 (#7464)](https://github.com/Azure/azure-sdk-for-cpp/commit/15a1f1be77590dd2b00845a4450b949bce2c3617) - `2026-10-15T22:30:53Z` - JinmingHu (@Jinming-Hu) - PR: [Update C++ APIView parser to 20261009.3](https://github.com/Azure/azure-sdk-for-cpp/pull/7464)
- [Sync eng/common directory with azure-sdk-tools for PR 17240 (#7462)](https://github.com/Azure/azure-sdk-for-cpp/commit/533e551ab9e732a5bb5a95200e842c0e81aa1e8f) - `2026-10-15T17:26:44Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17240](https://github.com/Azure/azure-sdk-for-cpp/pull/7462)

### Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample (2 commit(s), signal 117)

Tags: `human-authored, release, samples, watchlist`

- Release: [EPP Function ZIPs 182.1](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/releases/tag/epp-packages-182-1) - `2026-10-15T22:14:07Z`
- Release: [EPP Function ZIPs 165.1](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/releases/tag/epp-packages-165-1) - `2026-10-15T16:55:14Z`
- [docs: simplify documentation structure and troubleshooting (#54)](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/commit/63f10e50a84e99456d8190967b4c82295cc5985e) - `2026-10-15T22:11:54Z` - Hou (@SciencePotato) - PR: [docs: simplify documentation structure and troubleshooting](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/pull/54)
- [docs: clarify customer guidance with public Entra ID terminology (#52)](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/commit/ce68ee2649d8e4ab64e00c4abece33e939cdfa9c) - `2026-10-15T16:52:56Z` - Hou (@SciencePotato) - PR: [docs: clarify customer guidance with public Entra ID terminology](https://github.com/Azure-Samples/ExternalPhoneProvider-AzureFunction-Sample/pull/52)

### MicrosoftDocs/windows-iot-public (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #730 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/windows-iot-public/commit/ca03ffeeb890b53750a12227aa1c446e885cb221) - `2026-10-15T22:05:39Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
- [Update Windows IoT - Quickstart Customize a reference device in Audit…](https://github.com/MicrosoftDocs/windows-iot-public/commit/b27664f09278aaec61be8be50100cbb945cb58ca) - `2026-10-15T21:12:35Z` - Sakshi1691 (@Sakshi1691)

### microsoft/powerbi-desktop-samples (2 commit(s), signal 42)

Tags: `human-authored, samples`

- [Merge pull request #159 from yoon7824/themeSchemaUpdate/2026.10.1](https://github.com/microsoft/powerbi-desktop-samples/commit/64ff6b1476050e07a9011adb0894d25c385dc1f1) - `2026-10-15T21:15:23Z` - YoonK (@yoon7824) - PR: [October 2026 report theme schema update](https://github.com/microsoft/powerbi-desktop-samples/pull/159)
- [October 2026 report theme schema update](https://github.com/microsoft/powerbi-desktop-samples/commit/34f78db38030195329a5ce05323251f778772fe1) - `2026-10-15T20:03:17Z` - Yoon Kim (@yoon7824) - PR: [October 2026 report theme schema update](https://github.com/microsoft/powerbi-desktop-samples/pull/159)

### microsoft/kiota-serialization-form-go (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #142 from microsoft/dependabot/github_actions/code…](https://github.com/microsoft/kiota-serialization-form-go/commit/be764fd95499ccd6e797949156dbfce6ee547caa) - `2026-10-15T20:20:10Z` - github-actions[bot] (@github-actions[bot]) - PR: [build(deps): bump the codeql group with 3 updates](https://github.com/microsoft/kiota-serialization-form-go/pull/142)
- [build(deps): bump the codeql group with 3 updates](https://github.com/microsoft/kiota-serialization-form-go/commit/5797885115530be416fd3c88dbe69cd88d5b76b9) - `2026-10-15T19:54:59Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump the codeql group with 3 updates](https://github.com/microsoft/kiota-serialization-form-go/pull/142)

### MicrosoftLearning/caip (2 commit(s), signal 77)

Tags: `human-authored, training, watchlist`

- [Merge pull request #1 from AngieRudduck/main](https://github.com/MicrosoftLearning/caip/commit/89b1523623327753cc7531106243c0a95e46b477) - `2026-10-15T19:46:01Z` - Ivor Berry (@ivorb) - PR: [New updates for TW L300 lab](https://github.com/MicrosoftLearning/caip/pull/1)
- [update with translytical reference](https://github.com/MicrosoftLearning/caip/commit/888d87165e764612e82223496883dc8efd4d7f79) - `2026-10-15T19:28:10Z` - Angie Rudduck (@AngieRudduck) - PR: [New updates for TW L300 lab](https://github.com/MicrosoftLearning/caip/pull/1)

### microsoft/healthcare-models-and-agents-workshop (2 commit(s), signal 77)

Tags: `human-authored, product:Azure AI, training, watchlist`

- [Lesion-only model catalog, audit-log diagram, and docs cleanup](https://github.com/microsoft/healthcare-models-and-agents-workshop/commit/ad01a6095fc53f533d36d400fbae7ef946e5afa1) - `2026-10-15T18:56:57Z` - Jameson Merkow (@jmerkow)
- [lab: 3D MedImageParse tools, measured reports, patient context](https://github.com/microsoft/healthcare-models-and-agents-workshop/commit/6e9bf822d39b4dc95211703ac1d6e09219867d78) - `2026-10-15T18:56:57Z` - Jameson Merkow (@jmerkow)

### microsoft/healthcare-models-and-agents-workshop (2 commit(s), signal 77)

Tags: `human-authored, product:Azure AI, training, watchlist`

- [Lesion-only model catalog, audit-log diagram, and docs cleanup](https://github.com/microsoft/healthcare-models-and-agents-workshop/commit/ad01a6095fc53f533d36d400fbae7ef946e5afa1) - `2026-10-15T18:56:57Z` - Jameson Merkow (@jmerkow)
- [lab: 3D MedImageParse tools, measured reports, patient context](https://github.com/microsoft/healthcare-models-and-agents-workshop/commit/6e9bf822d39b4dc95211703ac1d6e09219867d78) - `2026-10-15T18:56:57Z` - Jameson Merkow (@jmerkow)

### MicrosoftDocs/azure-docs-powershell (2 commit(s), signal 52)

Tags: `bot-only, docs, product:PowerShell, security, watchlist`

- [status (#4391)](https://github.com/MicrosoftDocs/azure-docs-powershell/commit/cb7b6da682aec9d825f80ccc535aafd4c02312b6) - `2026-10-15T18:05:00Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [[BULK] [Bundle-Security] - Scheduled execution to fix known issues (part 6)](https://github.com/MicrosoftDocs/azure-docs-powershell/pull/4391)
- [status (#4390)](https://github.com/MicrosoftDocs/azure-docs-powershell/commit/0fe99608e2e66e46ee0b1353031ebcf03c47f97f) - `2026-10-15T16:13:26Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [[BULK] [Bundle-Security] - Scheduled execution to fix known issues (part 5)](https://github.com/MicrosoftDocs/azure-docs-powershell/pull/4390)

### microsoft/finops-toolkit (2 commit(s), signal 87)

Tags: `docs, human-authored, product:Azure AI, product:PowerShell, release-language, watchlist`

- [[Power BI] Fix SkuMeterName column error in storage reports for FOCUS…](https://github.com/microsoft/finops-toolkit/commit/f12c29e004725d70c95ec28f4d950c5c80dfeef3) - `2026-10-15T17:57:00Z` - Michael Flanakin (@flanakin) - PR: [[Power BI] Fix SkuMeterName column error in storage reports for FOCUS 1.2 exports](https://github.com/microsoft/finops-toolkit/pull/2333)
- [feat(agents): add ftk-cos, ftk-release-manager, and ftk-support agent…](https://github.com/microsoft/finops-toolkit/commit/22225ce7e1e8ce921bd3a078818ba1e6d82afd75) - `2026-10-15T17:33:58Z` - Michael Flanakin (@flanakin) - PR: [feat(agents): add ftk-cos, ftk-release-manager, and ftk-support agents](https://github.com/microsoft/finops-toolkit/pull/2340)

### microsoft/kiota-authentication-azure-go (2 commit(s), signal 17)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Merge pull request #240 from microsoft/dependabot/github_actions/code…](https://github.com/microsoft/kiota-authentication-azure-go/commit/4b0ffdc6fd5ec2f4306859db92936ca7bd28a38b) - `2026-10-15T17:16:51Z` - github-actions[bot] (@github-actions[bot]) - PR: [build(deps): bump the codeql-github-actions group with 2 updates](https://github.com/microsoft/kiota-authentication-azure-go/pull/240)
- [build(deps): bump the codeql-github-actions group with 2 updates](https://github.com/microsoft/kiota-authentication-azure-go/commit/d12da701fc7a16b46b6d55fcb41d7742ecfce0de) - `2026-10-15T17:15:06Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump the codeql-github-actions group with 2 updates](https://github.com/microsoft/kiota-authentication-azure-go/pull/240)

### MicrosoftDocs/minecraft-creator (2 commit(s), signal 77)

Tags: `docs, human-authored, watchlist`

- [Merging changes synced from https://github.com/MicrosoftDocs/minecraf…](https://github.com/MicrosoftDocs/minecraft-creator/commit/01015e9b7489eb7e86011592f07962e2107226f0) - `2026-10-15T16:29:55Z` - Learn Build Service GitHub App
- [Merge pull request #2333 from MicrosoftDocs/live-merge](https://github.com/MicrosoftDocs/minecraft-creator/commit/146c3bc7ac6a1469231224364300fa4c69108869) - `2026-10-15T16:28:50Z` - jacksonhardaway (@jacksonhardaway)

### Azure/corim (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Merge pull request #89 from mingweishih/feat/strict-signed-validation](https://github.com/Azure/corim/commit/f2b8aee2fe45ec14fd3741012e922e23d3abb4ad) - `2026-10-16T17:27:20Z` - Ming-Wei Shih (@mingweishih) - PR: [Add strict signed CoRIM validation alongside tolerant inspection](https://github.com/Azure/corim/pull/89)

### Azure/terraform-azurerm-avm-ptn-aca-lza-hosting-environment (1 commit(s), signal 26)

Tags: `bot-only, samples, watchlist`

- [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-ptn-aca-lza-hosting-environment/commit/611a66e00a5b3e7ae31c2fe9b1b060fe7ec09694) - `2026-10-16T16:51:36Z` - azure-verified-modules[bot] (@azure-verified-modules[bot]) - PR: [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-ptn-aca-lza-hosting-environment/pull/97)

### microsoft/Windows-IoT-Samples (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Merge EdgeAI-ObjectDetection sample into main branch (#122)](https://github.com/microsoft/Windows-IoT-Samples/commit/6446d2c00c9e859afbf183c0d78708eb5b37b0fe) - `2026-10-16T16:47:04Z` - Anthony Chen (@anch-msft) - PR: [Merge EdgeAI-ObjectDetection sample into main branch](https://github.com/microsoft/Windows-IoT-Samples/pull/122)

### MicrosoftDocs/WSL (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Added WSLc settings (#2641)](https://github.com/MicrosoftDocs/WSL/commit/50342fc53e0f5ab857529ddb567b2ccec1774c9a) - `2026-10-16T16:24:30Z` - Craig Loewen (@craigloewen-msft) - PR: [Added WSLc settings](https://github.com/MicrosoftDocs/WSL/pull/2641)

### microsoft/Agent365-Samples (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [Add front-matter metadata to sample README files (#345)](https://github.com/microsoft/Agent365-Samples/commit/7eef53bf15a4d89ea8528422999bfa370da1c319) - `2026-10-16T16:07:45Z` - Jim Daly (@JimDaly) - PR: [Add front-matter metadata to sample README files](https://github.com/microsoft/Agent365-Samples/pull/345)

### dotnet/dotnet-api-docs (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [CI update - .NET 11 RC 2 Core and Windows Desktop ref (#13185)](https://github.com/dotnet/dotnet-api-docs/commit/b8df334127516edc5110a7100affa1682fc1b5be) - `2026-10-16T14:51:03Z` - Genevieve Warren (@gewarren) - PR: [CI update - .NET 11 RC 2 Core and Windows Desktop ref](https://github.com/dotnet/dotnet-api-docs/pull/13185)

### microsoft/kiota-typescript (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [auto dependabot: bump webdriverio from 10.0.1 to 10.0.2 (#2183)](https://github.com/microsoft/kiota-typescript/commit/bb1a4d4206ae6d4987cde619fd1b9dd694ad6725) - `2026-10-16T14:35:21Z` - dependabot[bot] (@dependabot[bot]) - PR: [auto dependabot: bump webdriverio from 10.0.1 to 10.0.2](https://github.com/microsoft/kiota-typescript/pull/2183)

### Azure/terraform-azurerm-avm-res-devtestlab-lab (1 commit(s), signal 26)

Tags: `bot-only, training, watchlist`

- [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-res-devtestlab-lab/commit/e508be28268141316203c647daf3de70341e7c03) - `2026-10-16T13:48:15Z` - azure-verified-modules[bot] (@azure-verified-modules[bot]) - PR: [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-res-devtestlab-lab/pull/75)

### MicrosoftDocs/azure-docs-cli (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [CI Update](https://github.com/MicrosoftDocs/azure-docs-cli/commit/29d4dc11135ebbc2f00815422582dbe5ba684490) - `2026-10-16T12:52:49Z` - docsreference@microsoft.com

### MicrosoftDocs/azure-cloud-services-files (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Updating the GuestOS xml feed (#51)](https://github.com/MicrosoftDocs/azure-cloud-services-files/commit/9730249b30795eda51c00287fc09763537145214) - `2026-10-16T11:22:27Z` - Srivastcha Sai Tirumalasetti (@srtirumal) - PR: [Updating the GuestOS xml feed](https://github.com/MicrosoftDocs/azure-cloud-services-files/pull/51)

### microsoft/kiota-dotnet (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, docs, product:Azure SDK, product:Microsoft Graph, watchlist`

- [Bump the testing-dependencies group with 4 updates (#830)](https://github.com/microsoft/kiota-dotnet/commit/1b04c284878e3d469d5024042b18af8b8a572dce) - `2026-10-16T10:06:48Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the testing-dependencies group with 4 updates](https://github.com/microsoft/kiota-dotnet/pull/830)

### dotnet/EntityFramework.Docs (1 commit(s), signal 76)

Tags: `docs, human-authored, watchlist`

- [Document EF Core breaking changes and SaveChanges interceptor outcome…](https://github.com/dotnet/EntityFramework.Docs/commit/d74e5b4cd0f1f99fe4ff19d08c138549ffa61b55) - `2026-10-16T10:01:34Z` - Copilot (@Copilot) - PR: [Document EF Core breaking changes and SaveChanges interceptor outcomes](https://github.com/dotnet/EntityFramework.Docs/pull/5485)

### dotnet/msbuild-api-docs (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [CI Update: https://dev.azure.com/msft-skilling/Content/_workitems/edi…](https://github.com/dotnet/msbuild-api-docs/commit/b7f5c8a5e7729ff1e961bb887d6ccdba3821b5c1) - `2026-10-16T08:41:23Z` - Alma Jenks (@v-alje) - PR: [CI Update: https://dev.azure.com/msft-skilling/Content/_workitems/edit/638927](https://github.com/dotnet/msbuild-api-docs/pull/73)

### microsoft/voice-agent (1 commit(s), signal 76)

Tags: `docs, human-authored, product:Azure AI, watchlist`

- [docs: add architecture guide for voice-enabling existing agents (#38)](https://github.com/microsoft/voice-agent/commit/5c81df7cf01d1fef3652da9c410347f127850a6f) - `2026-10-16T08:33:02Z` - szhaomsft (@szhaomsft) - PR: [docs: add architecture guide for voice-enabling existing agents](https://github.com/microsoft/voice-agent/pull/38)

### Azure-Samples/azure-openai-keyless-js (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, product:Azure AI, samples, watchlist`

- [chore(deps): bump the github-actions group with 2 updates (#11)](https://github.com/Azure-Samples/azure-openai-keyless-js/commit/f3bfaceb0c7c0ab3f88a56b57f288d7f50ceb4c6) - `2026-10-16T07:01:43Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump the github-actions group with 2 updates](https://github.com/Azure-Samples/azure-openai-keyless-js/pull/11)

### Azure/azure-devops-cli-extension (1 commit(s), signal 141)

Tags: `docs, human-authored, release, security, watchlist`

- Release: [Azure DevOps CLI extension for Azure CLI 1.0.10](https://github.com/Azure/azure-devops-cli-extension/releases/tag/20261015.1) - `2026-10-16T10:35:35Z`
- [Harden credential store file permissions (#1526)](https://github.com/Azure/azure-devops-cli-extension/commit/429a129a69306ae7377684b00660dd3521a126ea) - `2026-10-16T05:14:59Z` - Bhavesh Bhati (@bhaveshbhati) - PR: [Harden credential store file permissions](https://github.com/Azure/azure-devops-cli-extension/pull/1526)

### microsoft/amplifier-app-cli (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [fix: embedded module update reporting and cached include discovery](https://github.com/microsoft/amplifier-app-cli/commit/f5be404720c5cf9d8859b77dc3145031ec52059d) - `2026-10-16T05:03:02Z` - Brian Krabach (@bkrabach) - PR: [Fix embedded module update reporting and cached include discovery](https://github.com/microsoft/amplifier-app-cli/pull/373)

### microsoft/amplifier-module-tool-bash (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [fix: inspect commands through common execution wrappers (#24)](https://github.com/microsoft/amplifier-module-tool-bash/commit/6d1366c4db30831daa448aaf1fc382006efe0dbb) - `2026-10-16T03:05:31Z` - Brian Krabach (@bkrabach) - PR: [fix: inspect commands through nice, setsid and stdbuf](https://github.com/microsoft/amplifier-module-tool-bash/pull/24)

### Azure-Samples/azure-sre-agent-vm-anomaly-detection (1 commit(s), signal 76)

Tags: `human-authored, product:Azure AI, samples, watchlist`

- [feat: add Azure SRE Agent VM anomaly detection sample](https://github.com/Azure-Samples/azure-sre-agent-vm-anomaly-detection/commit/3596a5c085c438103307957005a0854606ef0647) - `2026-10-16T02:59:40Z` - okada-kai (@okada-kai)

### Azure-Samples/app-templates-springboot-app-on-AKS (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Merge pull request #33 from danfiedler-msft/danfiedler/pin-actions](https://github.com/Azure-Samples/app-templates-springboot-app-on-AKS/commit/b9d1d16882eff844b3a0d0d29b30170486fb4f3d) - `2026-10-16T00:18:08Z` - Paul Yuknewicz (@paulyuk) - PR: [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/app-templates-springboot-app-on-AKS/pull/33)

### microsoft/mcp-dotnet-samples (1 commit(s), signal 41)

Tags: `human-authored, samples`

- [Update metadata.json](https://github.com/microsoft/mcp-dotnet-samples/commit/670c245cc7128acbfc7cef069b02c7bc73fa5c6a) - `2026-10-15T23:11:13Z` - GitHub Actions (@actions-user)

### Azure-Samples/Durable-Task-Scheduler (1 commit(s), signal 76)

Tags: `human-authored, product:Azure SDK, samples, watchlist`

- [Refresh Durable Task Scheduler sample documentation (#407)](https://github.com/Azure-Samples/Durable-Task-Scheduler/commit/bb6bd78eb3acfd0ffbc7ff7f254c3054356e67eb) - `2026-10-15T21:28:16Z` - greenie-msft (@greenie-msft) - PR: [Refresh Durable Task Scheduler sample documentation](https://github.com/Azure-Samples/Durable-Task-Scheduler/pull/407)

### dotnet/eShop (1 commit(s), signal 41)

Tags: `docs, human-authored`

- [Confine catalog picture reads to Pics (#1061)](https://github.com/dotnet/eShop/commit/913acea66708a59595351174cee9b29f37179d29) - `2026-10-15T20:52:28Z` - Stephen Halter (@halter73) - PR: [Confine catalog picture reads to Pics](https://github.com/dotnet/eShop/pull/1061)

### OfficeDev/Office-Add-in-samples (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, samples`

- [chore(deps): Bump the github-actions group with 2 updates (#1581)](https://github.com/OfficeDev/Office-Add-in-samples/commit/2fb9262ce3802c8497d3b148a9bed7129a675da7) - `2026-10-15T20:28:58Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): Bump the github-actions group with 2 updates](https://github.com/OfficeDev/Office-Add-in-samples/pull/1581)

### microsoft/playwright-pytest (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, docs`

- [chore(deps): bump the github-actions group with 2 updates (#336)](https://github.com/microsoft/playwright-pytest/commit/7a0e29803fea6f677b25a574df3739f624c1bbe5) - `2026-10-15T18:08:41Z` - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump the github-actions group with 2 updates](https://github.com/microsoft/playwright-pytest/pull/336)

### MicrosoftDocs/sql-docs (1 commit(s), signal 26)

Tags: `bot-only, docs, watchlist`

- [Merge pull request #38360 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/sql-docs/commit/8c2bed74fd1e1ecfe79c0e568e649c6560d46504) - `2026-10-15T17:36:09Z` - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

### Azure/azure-sdk (1 commit(s), signal 26)

Tags: `bot-only, docs, product:Azure SDK, watchlist`

- [Sync eng/common directory with azure-sdk-tools for PR 17240 (#10348)](https://github.com/Azure/azure-sdk/commit/c1b4076605ce5d304c1505165bcfed9dc116601f) - `2026-10-15T17:26:29Z` - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17240](https://github.com/Azure/azure-sdk/pull/10348)

### Azure/setup-azd (1 commit(s), signal 16)

Tags: `bot-only, dependency-noise, samples, watchlist`

- [build(deps): bump the github-actions group across 1 directory with 5 …](https://github.com/Azure/setup-azd/commit/b40bed18668eb30d701c38a05f6b89b199a6bf71) - `2026-10-15T16:52:42Z` - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump the github-actions group across 1 directory with 5 updates](https://github.com/Azure/setup-azd/pull/630)

### OfficeDev/office-js-snippets (1 commit(s), signal 0)

Tags: `bot-only, dependency-noise, training`

- [Bump the github-actions group with 2 updates (#1134)](https://github.com/OfficeDev/office-js-snippets/commit/896b0a1236576fc78220774b58260cb9c9690373) - `2026-10-15T16:23:39Z` - dependabot[bot] (@dependabot[bot]) - PR: [Bump the github-actions group with 2 updates](https://github.com/OfficeDev/office-js-snippets/pull/1134)

</details>
