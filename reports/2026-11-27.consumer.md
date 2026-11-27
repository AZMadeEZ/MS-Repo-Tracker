# Microsoft Ecosystem Brief - 2026-11-27

> Fresh as of 2026-11-27 22:08 UTC. 72 repos moved, 248 commits, 6 releases, 190 tracked events.

## What To Look At First

### 1. [Security-related change: ci: isolate checkout and Marketplace credentials](https://github.com/microsoft/vscode-platform-specific-sample/pull/21)

- Repository: [microsoft/vscode-platform-specific-sample](https://github.com/microsoft/vscode-platform-specific-sample)
- Why it matters: Review for security, admin, or training impact; this may affect guidance consumers rely on.

### 2. [Security-related change: 20261125 secretless obo and caching in multi-source config (#541)](https://github.com/MicrosoftDocs/data-api-builder-docs/commit/7f1c76c05daffd24fa4d864ad626cfab7e09c5f9)

- Repository: [MicrosoftDocs/data-api-builder-docs](https://github.com/MicrosoftDocs/data-api-builder-docs)
- Why it matters: Review for security, admin, or training impact; this may affect guidance consumers rely on.

### 3. [Release activity: 0.30.0](https://github.com/microsoft/AzureTRE/releases/tag/v0.30.0)

- Repository: [microsoft/AzureTRE](https://github.com/microsoft/AzureTRE)
- Why it matters: Check release notes or linked PRs if your team consumes this package, sample, SDK, or tool.

### 4. [Release activity: Azure.ResourceManager.CognitiveServices_1.8.0-beta.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.CognitiveServices_1.8.0-beta.1)

- Repository: [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net)
- Why it matters: Check release notes or linked PRs if your team consumes this package, sample, SDK, or tool.

### 5. [Release activity: Merge from release branch to main (#56991)](https://github.com/MicrosoftDocs/learn/commit/a0acb943a208a34c894dd51b242416c119e810ca)

- Repository: [MicrosoftDocs/learn](https://github.com/MicrosoftDocs/learn)
- Why it matters: Check release notes or linked PRs if your team consumes this package, sample, SDK, or tool.

### 6. [Release activity: com.azure.resourcemanager+azure-resourcemanager-postgresqlflexibleserver_3.1.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-postgresqlflexibleserver_3.1.0)

- Repository: [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java)
- Why it matters: Check release notes or linked PRs if your team consumes this package, sample, SDK, or tool.

### 7. [Security-related change: Fix documentation errors in Android.Credentials (R068, pass 3)](https://github.com/dotnet/android-api-docs/pull/1949)

- Repository: [dotnet/android-api-docs](https://github.com/dotnet/android-api-docs)
- Why it matters: Review for security, admin, or training impact; this may affect guidance consumers rely on.

### 8. [Security-related change: CI: Limit test workflow credentials](https://github.com/microsoft/vscode-mock-debug/pull/152)

- Repository: [microsoft/vscode-mock-debug](https://github.com/microsoft/vscode-mock-debug)
- Why it matters: Review for security, admin, or training impact; this may affect guidance consumers rely on.

## Product Area Briefings

### Azure

30 repos, 74 tracked events, 5 releases, 0 security/admin signals.

- Likely audience: Developers, Learners, General MS consumers.
- Reader takeaway: Start with releases; consumers may need version or sample awareness.
- Most useful links:
  - [0.30.0](https://github.com/microsoft/AzureTRE/releases/tag/v0.30.0) (microsoft/AzureTRE)
  - [Prepare AzureTRE v0.30.0 release](https://github.com/microsoft/AzureTRE/pull/5321) (microsoft/AzureTRE)
  - [Azure.ResourceManager.CognitiveServices_1.8.0-beta.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.CognitiveServices_1.8.0-beta.1) (Azure/azure-sdk-for-net)

### Unmapped Activity

15 repos, 44 tracked events, 1 release, 1 security/admin signal.

- Likely audience: Learners, General MS consumers, Developers.
- Reader takeaway: Start with the security/admin-sensitive links, then scan releases.
- Most useful links:
  - [20261125 secretless obo and caching in multi-source config (#541)](https://github.com/MicrosoftDocs/data-api-builder-docs/commit/7f1c76c05daffd24fa4d864ad626cfab7e09c5f9) (MicrosoftDocs/data-api-builder-docs)
  - [Merge from release branch to main (#56991)](https://github.com/MicrosoftDocs/learn/commit/a0acb943a208a34c894dd51b242416c119e810ca) (MicrosoftDocs/learn)
  - [v1.13.14](https://github.com/microsoft/dbt-fabricspark/releases/tag/v1.13.14) (microsoft/dbt-fabricspark)

### .NET

8 repos, 24 tracked events, 0 releases, 1 security/admin signal.

- Likely audience: Developers, General MS consumers, Learners.
- Reader takeaway: Start with the security/admin-sensitive links, then scan releases.
- Most useful links:
  - [Fix documentation errors in Android.Credentials (R068, pass 3)](https://github.com/dotnet/android-api-docs/pull/1949) (dotnet/android-api-docs)
  - [[Android] Fix SslStream handshake connection info queries on older Android versions](https://github.com/dotnet/runtime/pull/136517) (dotnet/runtime)
  - [Remove obsolete runtime categories from WBT](https://github.com/dotnet/runtime/pull/138425) (dotnet/runtime)

### Developer Tools

5 repos, 14 tracked events, 0 releases, 5 security/admin signals.

- Likely audience: Developers.
- Reader takeaway: Start with the security/admin-sensitive links, then scan releases.
- Most useful links:
  - [ci: isolate checkout and Marketplace credentials](https://github.com/microsoft/vscode-platform-specific-sample/pull/21) (microsoft/vscode-platform-specific-sample)
  - [CI: Limit test workflow credentials](https://github.com/microsoft/vscode-mock-debug/pull/152) (microsoft/vscode-mock-debug)
  - [Improve AI in VS Code documentation IA, structure, and developer guides](https://github.com/microsoft/vscode-docs/pull/10779) (microsoft/vscode-docs)

### Microsoft Graph

11 repos, 29 tracked events, 0 releases, 0 security/admin signals.

- Likely audience: Developers, General MS consumers, Learners.
- Reader takeaway: Use the top links first; some of the movement is likely generated or operational.
- Most useful links:
  - [fix(http): resolve relative redirect locations that contain "://"](https://github.com/microsoft/kiota-typescript/pull/2243) (microsoft/kiota-typescript)
  - [fix(abstractions): serialize timedelta path and query parameters as ISO 8601 durations](https://github.com/microsoft/kiota-python/pull/925) (microsoft/kiota-python)
  - [fix: preserve fractional seconds when serializing date-times](https://github.com/microsoft/kiota-serialization-json-go/pull/247) (microsoft/kiota-serialization-json-go)

### PowerShell

2 repos, 4 tracked events, 0 releases, 0 security/admin signals.

- Likely audience: Admins.
- Reader takeaway: Use the top links first; some of the movement is likely generated or operational.
- Most useful links:
  - [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/57867cf99730255905e07efb509366b729fab4e0) (MicrosoftDocs/power-platform)
  - [disable public contributions (#12274)](https://github.com/MicrosoftDocs/power-platform/commit/c8e17007d24a1b2f2f9feed37076bce7a5e34aa8) (MicrosoftDocs/power-platform)
  - [New Meters](https://github.com/microsoft/fabric-toolbox/pull/741) (microsoft/fabric-toolbox)

### Windows

1 repo, 1 tracked event, 0 releases, 0 security/admin signals.

- Likely audience: General MS consumers.
- Reader takeaway: Use the top links first; some of the movement is likely generated or operational.

## Release Radar

| Product area | Repository | Release | Why it matters |
| --- | --- | --- | --- |
| Azure | [microsoft/AzureTRE](https://github.com/microsoft/AzureTRE) | [0.30.0](https://github.com/microsoft/AzureTRE/releases/tag/v0.30.0) | New release available for consumers of this repo. |
| Azure | [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.ResourceManager.CognitiveServices_1.8.0-beta.1](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.CognitiveServices_1.8.0-beta.1) | Pre-release; inspect before adopting broadly. |
| Azure | [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.ResourceManager.Network_1.18.0](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.Network_1.18.0) | New release available for consumers of this repo. |
| Azure | [Azure/azure-sdk-for-net](https://github.com/Azure/azure-sdk-for-net) | [Azure.ResourceManager.Chaos_1.2.0-beta.4](https://github.com/Azure/azure-sdk-for-net/releases/tag/Azure.ResourceManager.Chaos_1.2.0-beta.4) | Pre-release; inspect before adopting broadly. |
| Azure | [Azure/azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) | [com.azure.resourcemanager+azure-resourcemanager-postgresqlflexibleserver_3.1.0](https://github.com/Azure/azure-sdk-for-java/releases/tag/com.azure.resourcemanager%2Bazure-resourcemanager-postgresqlflexibleserver_3.1.0) | New release available for consumers of this repo. |
| Unknown | [microsoft/dbt-fabricspark](https://github.com/microsoft/dbt-fabricspark) | [v1.13.14](https://github.com/microsoft/dbt-fabricspark/releases/tag/v1.13.14) | New release available for consumers of this repo. |

## Security And Admin Attention

These are not automatically vulnerabilities; they are items with security/admin-sensitive language or taxonomy.

- [microsoft/vscode-platform-specific-sample](https://github.com/microsoft/vscode-platform-specific-sample): [ci: isolate checkout and Marketplace credentials](https://github.com/microsoft/vscode-platform-specific-sample/pull/21)
- [MicrosoftDocs/data-api-builder-docs](https://github.com/MicrosoftDocs/data-api-builder-docs): [20261125 secretless obo and caching in multi-source config (#541)](https://github.com/MicrosoftDocs/data-api-builder-docs/commit/7f1c76c05daffd24fa4d864ad626cfab7e09c5f9)
- [dotnet/android-api-docs](https://github.com/dotnet/android-api-docs): [Fix documentation errors in Android.Credentials (R068, pass 3)](https://github.com/dotnet/android-api-docs/pull/1949)
- [microsoft/vscode-mock-debug](https://github.com/microsoft/vscode-mock-debug): [CI: Limit test workflow credentials](https://github.com/microsoft/vscode-mock-debug/pull/152)

## What Was Mostly Noise

93 events looked automated, bot-heavy, dependency-related, generated, or medium/high-noise.

Top noisy clusters:

- [microsoftgraph/msgraph-snippets-go](https://github.com/microsoftgraph/msgraph-snippets-go) - 5 events
- [Azure-Samples/portability-patterns-library](https://github.com/Azure-Samples/portability-patterns-library) - 5 events
- [microsoftgraph/msgraph-sample-github-connector-typescript](https://github.com/microsoftgraph/msgraph-sample-github-connector-typescript) - 5 events
- [microsoft/kiota-python](https://github.com/microsoft/kiota-python) - 4 events
- [microsoft/vscode-extension-samples](https://github.com/microsoft/vscode-extension-samples) - 4 events

Noise mix: Dependency: 50, Docs: 24, SDK: 7, Sample: 5, CI/Infra: 4, Release: 2, Training: 1.

## Data Confidence

- Source: GitHub scheduled/manual digest artifacts in this repository.
- Window: 25.7 hours from `2026-11-26T20:27:15.864534Z` to `2026-11-27T22:08:05.031289Z`.
- Event stream: 184 commits, 6 releases.
- Freshness: tracked in [`reports/status.json`](status.json).
- Full data: [`latest.summary.json`](latest.summary.json), [`latest.events.ndjson`](latest.events.ndjson), [`latest.json`](latest.json).
