# Changes on default branch since 2026-11-16T20:56:46.333079Z

Repos with movement: **142**

## docs

### Azure

- **Azure/azure-sdk-for-net** (`main`) - **16** commit(s)
  - [[Storage] Fixed issue where AlreadyExists error on structured message…](https://github.com/Azure/azure-sdk-for-net/commit/47b12e2c0026311b54741161adcec332741cab71) - 2026-11-17T21:22:14Z - Amanda Nguyen (@amnguye) - PR: [[Storage] Fixed issue where AlreadyExists error on structured message will throw incorrect exception #64993](https://github.com/Azure/azure-sdk-for-net/pull/64993)
  - [Fix OnSendingRequest test flakeyness due to timing clock jitter (#65010)](https://github.com/Azure/azure-sdk-for-net/commit/d1eecc5b98fd779e11b27063d2058587139bf626) - 2026-11-17T20:46:33Z - Amanda Nguyen (@amnguye) - PR: [[Storage] Fix OnSendingRequest test flakeyness due to timing clock jitter #65010](https://github.com/Azure/azure-sdk-for-net/pull/65010)
  - [[Health Deidentification] Set Overwrite in cancel/delete job test (#6…](https://github.com/Azure/azure-sdk-for-net/commit/acec3b127e68d893a5187f20dc8a94dee871c788) - 2026-11-17T20:44:12Z - Josiah Vinson (@jovinson-ms) - PR: [[Health Deidentification] Set Overwrite in cancel/delete job test #65024](https://github.com/Azure/azure-sdk-for-net/pull/65024)
  - [Update azure-typespec/http-client-csharp version to prerelease 1.0.0-…](https://github.com/Azure/azure-sdk-for-net/commit/bf7cd6a8ccc924736ced44aeae020be67563b6c4) - 2026-11-17T20:17:24Z - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Update azure-typespec/http-client-csharp version to prerelease 1.0.0-alpha.20261117.2 #65027](https://github.com/Azure/azure-sdk-for-net/pull/65027)
  - [Prepare for release for other packages (#64930)](https://github.com/Azure/azure-sdk-for-net/commit/8f7562d33a7404b95d65bb820616c1a067708df9) - 2026-11-17T18:49:16Z - Nikolay Rovinskiy (@nick863) - PR: [Prepare for release for other packages #64930](https://github.com/Azure/azure-sdk-for-net/pull/64930)

- **Azure/azure-sdk-for-js** (`main`) - **14** commit(s)
  - [[Health Deidentification] Retry list scan in CreateThenList live test…](https://github.com/Azure/azure-sdk-for-js/commit/e07213da18965842bf8edb8d6386472bf208046f) - 2026-11-17T20:58:11Z - Josiah Vinson (@jovinson-ms) - PR: [[Health Deidentification] Retry list scan in CreateThenList live test #40824](https://github.com/Azure/azure-sdk-for-js/pull/40824)
  - [[EngSys] downgrade `http(s)-proxy-agent` dependencies to v7 (#40830)](https://github.com/Azure/azure-sdk-for-js/commit/20e651afefdb2c5d9a7a5ef68962be428abda58c) - 2026-11-17T20:37:21Z - Jeremy Meng (@jeremymeng) - PR: [[EngSys] downgrade `http(s)-proxy-agent` dependencies to v7 #40830](https://github.com/Azure/azure-sdk-for-js/pull/40830)
  - [[AutoPR @azure-arm-containerregistry]-generated-from-SDK Generation -…](https://github.com/Azure/azure-sdk-for-js/commit/fd1468db66f96a6319c0157c3f3878850852bc85) - 2026-11-17T18:47:38Z - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR @azure-arm-containerregistry]-generated-from-SDK Generation - JS-7062791 #40723](https://github.com/Azure/azure-sdk-for-js/pull/40723)
  - [[AutoPR @azure-arm-netapp]-generated-from-SDK Generation - JS-7080421…](https://github.com/Azure/azure-sdk-for-js/commit/ed8d2cb864a23acb6fb77ae9fb80d340484bae2f) - 2026-11-17T18:35:47Z - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR @azure-arm-netapp]-generated-from-SDK Generation - JS-7080421 #40810](https://github.com/Azure/azure-sdk-for-js/pull/40810)
  - [[dev-tool] List names missing from their module as unresolved referen…](https://github.com/Azure/azure-sdk-for-js/commit/acdefde91bc40be1b1266d6d9afd3f156935f200) - 2026-11-17T18:09:21Z - Maor Leger (@maorleger) - PR: [[dev-tool] List names missing from their module as unresolved references #40818](https://github.com/Azure/azure-sdk-for-js/pull/40818)

- **Azure/azure-sdk-for-python** (`main`) - **11** commit(s)
  - [[Health Deidentification] Tolerate fast job completion in cancel/dele…](https://github.com/Azure/azure-sdk-for-python/commit/0936b67439e84860e1fbab10a0d80f7e4fdf9c2b) - 2026-11-17T21:02:31Z - Josiah Vinson (@jovinson-ms) - PR: [[Health Deidentification] Tolerate fast job completion in cancel/delete tests #50044](https://github.com/Azure/azure-sdk-for-python/pull/50044)
  - [[Identity] Skip azure-identity-broker on Python 3.15 in CI (#50051)](https://github.com/Azure/azure-sdk-for-python/commit/c86ca5302e8d26a1aaf717b1db0be9712a739271) - 2026-11-17T20:31:04Z - Libba Lawrence (@l0lawrence) - PR: [[Identity] Skip azure-identity-broker on Python 3.15 in CI #50051](https://github.com/Azure/azure-sdk-for-python/pull/50051)
  - [[Identity] Prepare 1.27.1 bugfix release (#50048)](https://github.com/Azure/azure-sdk-for-python/commit/ca1c50e780ee270fd6be9cfc9c3d0309c58b64a6) - 2026-11-17T19:12:53Z - Libba Lawrence (@l0lawrence) - PR: [[Identity] Prepare 1.27.1 bugfix release #50048](https://github.com/Azure/azure-sdk-for-python/pull/50048)
  - [[Identity] Parse azd expiresOn as UTC in AzureDeveloperCliCredential …](https://github.com/Azure/azure-sdk-for-python/commit/8cbb6c9cd855a8f7e1c3c8c5305b616f3453c147) - 2026-11-17T18:21:03Z - digit50 (@digit50) - PR: [[Identity] Parse azd expiresOn as UTC in AzureDeveloperCliCredential #49590](https://github.com/Azure/azure-sdk-for-python/pull/49590)
  - [[AutoPR azure-mgmt-cognitiveservices]-generated-from-SDK Generation -…](https://github.com/Azure/azure-sdk-for-python/commit/e8a27c5105e8d12510682bc6493cd38061bef1cf) - 2026-11-17T15:21:03Z - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-mgmt-cognitiveservices]-generated-from-SDK Generation - Python-7078676 #50011](https://github.com/Azure/azure-sdk-for-python/pull/50011)

- **Azure/azure-cli-extensions** (`main`) - **10** commit(s)
  - [[Containerapp] BREAKING CHANGE: Change default logs destination to Az…](https://github.com/Azure/azure-cli-extensions/commit/8c6ecc75a166346cbc8ec18004a8094569076250) - 2026-11-17T05:48:22Z - Michael Dai (@michaelkira) - PR: [[Containerapp] BREAKING CHANGE: Change default logs destination to Azure Monitor #10473](https://github.com/Azure/azure-cli-extensions/pull/10473)
  - [[Release] Update index.json for extension [ neuroshield-1.0.0b1 ]](https://github.com/Azure/azure-cli-extensions/commit/50e6a066d7daf7b49429b8f74a3842918f041c7d) - 2026-11-17T03:38:21Z - Azure CLI Team (@azclibot)
  - [[NeuroShield] `az neuroshield`: Add new extension for NeuroShield (#1…](https://github.com/Azure/azure-cli-extensions/commit/57d0d0d788c41ea2f915a37d623eee61695e8970) - 2026-11-17T03:21:41Z - Jian Hui (@huiii99) - PR: [[NeuroShield] `az neuroshield`: Add new extension for NeuroShield #10586](https://github.com/Azure/azure-cli-extensions/pull/10586)
  - [[Release] Update index.json for extension [ aks-preview-22.0.0b17 ]](https://github.com/Azure/azure-cli-extensions/commit/6fce65ef32d2368e15f175729fa5e7b73692591e) - 2026-11-17T02:21:50Z - Azure CLI Team (@azclibot)
  - [[Release] Update index.json for extension [ documentdb-1.1.0b2 ]](https://github.com/Azure/azure-cli-extensions/commit/36a0bbb4fc0a3535b05870c2f7fec10a149e4dcd) - 2026-11-17T02:15:19Z - Azure CLI Team (@azclibot)

- **Azure/azure-sdk-for-java** (`main`) - **9** commit(s)
  - [Increment package versions for cognitiveservices auto-releases (#51313)](https://github.com/Azure/azure-sdk-for-java/commit/815fe4bc369e9832510d2b833d0b43758c81e167) - 2026-11-17T18:00:53Z - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[skip ci] Increment versions for cognitiveservices auto-releases #51313](https://github.com/Azure/azure-sdk-for-java/pull/51313)
  - [Fixing mono refresh bug (#51295)](https://github.com/Azure/azure-sdk-for-java/commit/b54eb65802ac035cc741d1373f74d0bb2225d37b) - 2026-11-17T17:47:53Z - Matthew Metcalf (@mrm9084) - PR: [Fixing mono refresh bug #51295](https://github.com/Azure/azure-sdk-for-java/pull/51295)
  - [Fix blocked Cosmos source task shutdown (#50560)](https://github.com/Azure/azure-sdk-for-java/commit/464b455a14a2a9d68f576884c5f8f6fa3c5f3584) - 2026-11-17T17:20:45Z - nkokitkar (@nkokitkar) - PR: [Fix blocked Cosmos source task shutdown #50560](https://github.com/Azure/azure-sdk-for-java/pull/50560)
  - [[AutoPR azure-resourcemanager-cognitiveservices]-generated-from-SDK G…](https://github.com/Azure/azure-sdk-for-java/commit/4908d4dc523ddcef8c8b1ebf1a873cfc9f1b9421) - 2026-11-17T15:21:15Z - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR azure-resourcemanager-cognitiveservices]-generated-from-SDK Generation - Java-7078674 #51261](https://github.com/Azure/azure-sdk-for-java/pull/51261)
  - [Increment package versions for containerservice auto-releases (#51307)](https://github.com/Azure/azure-sdk-for-java/commit/b46de14ddf7554c10171db1ce4bc0465a3270df7) - 2026-11-17T10:00:48Z - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[skip ci] Increment versions for containerservice auto-releases #51307](https://github.com/Azure/azure-sdk-for-java/pull/51307)

- **Azure/data-api-builder** (`main`) - **4** commit(s)
  - [mcp: merge DB columns with config fields in describe_entities for tab…](https://github.com/Azure/data-api-builder/commit/3243510258d4bd9bf90ceb33ad93ff3b9a7312c6) - 2026-11-17T17:53:25Z - Mohit G (@gmohit21) - PR: [mcp: merge DB columns with config fields in describe_entities for tables/views #3924](https://github.com/Azure/data-api-builder/pull/3924)
  - [Fix DWSQL MCP grouped aggregate ordering scope (#3884)](https://github.com/Azure/data-api-builder/commit/1088b91e25b7d382725bca85f0d6c9d57ca1c809) - 2026-11-17T06:44:42Z - Copilot (@Copilot) - PR: [Fix DWSQL MCP grouped aggregate ordering scope #3884](https://github.com/Azure/data-api-builder/pull/3884)
  - [Use entity datasource for REST mutations (#3882)](https://github.com/Azure/data-api-builder/commit/ec0af8875d1631fa82571f095ad239ef791764f1) - 2026-11-17T05:05:25Z - Copilot (@Copilot) - PR: [Use entity datasource for REST and MCP mutations #3882](https://github.com/Azure/data-api-builder/pull/3882)
  - [Fix Log-Level Test (#3907)](https://github.com/Azure/data-api-builder/commit/fd51a456508e599dd690fa8215460be41f4ebc92) - 2026-11-17T03:55:18Z - RubenCerna2079 (@RubenCerna2079) - PR: [Fix Log-Level Test #3907](https://github.com/Azure/data-api-builder/pull/3907)

- **Azure/azure-sdk-for-go** (`main`) - **4** commit(s)
  - [[keyvault] Update azkeys and azadmin to stable 2026-04-01 (#27858)](https://github.com/Azure/azure-sdk-for-go/commit/6759398479bdeaac5ed522e3f526da7cd7cdbb08) - 2026-11-17T16:46:25Z - ksemenov-gh (@ksemenov-gh) - PR: [[keyvault] Update azkeys and azadmin to stable 2026-04-01 #27858](https://github.com/Azure/azure-sdk-for-go/pull/27858)
  - [[AutoPR sdk-resourcemanager/containerservicefleet/armcontainerservice…](https://github.com/Azure/azure-sdk-for-go/commit/dd36c66b651b351e2eba6193f2643ff08556d5a6) - 2026-11-17T15:23:14Z - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR sdk-resourcemanager/containerservicefleet/armcontainerservicefleet]-generated-from-SDK Generation - Go-7082502 #28043](https://github.com/Azure/azure-sdk-for-go/pull/28043)
  - [Configurations:  'specification/containerservice/resource-manager/Mic…](https://github.com/Azure/azure-sdk-for-go/commit/13378e571208185f5611ed12dad855285d88c203) - 2026-11-17T03:22:37Z - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR sdk-resourcemanager/containerservice/armcontainerservice]-generated-from-SDK Generation - Go-7079811 #28054](https://github.com/Azure/azure-sdk-for-go/pull/28054)
  - [Configurations:  'specification/netapp/resource-manager/Microsoft.Net…](https://github.com/Azure/azure-sdk-for-go/commit/c2f0fcab1625b840510a6bc95ff8593f37deee31) - 2026-11-17T02:15:12Z - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[AutoPR sdk-resourcemanager/netapp/armnetapp]-generated-from-SDK Generation - Go-7080423 #28055](https://github.com/Azure/azure-sdk-for-go/pull/28055)

- **Azure/azure-devops-cli-extension** (`master`) - **4** commit(s)
  - [Post release 1.0.11 (#1545)](https://github.com/Azure/azure-devops-cli-extension/commit/3ea8b2f20761f5433edb469c9d55235db37fa7f2) - 2026-11-17T09:12:59Z - mishrarish (@mishrarish) - PR: [Post release 1.0.11 #1545](https://github.com/Azure/azure-devops-cli-extension/pull/1545)
  - [Pin GitHub Actions to full-length commit SHAs (#1517)](https://github.com/Azure/azure-devops-cli-extension/commit/4cc5f616a122ed4ec83c30e4d946cba59a1a11c7) - 2026-11-17T08:04:43Z - Dan Fiedler (@danfiedler-msft) - PR: [Pin GitHub Actions to full-length commit SHAs #1517](https://github.com/Azure/azure-devops-cli-extension/pull/1517)
  - [Remove Python 3.9 from merge workflow (#1543)](https://github.com/Azure/azure-devops-cli-extension/commit/17d5638e9895cf683127667626f4032a02154d3a) - 2026-11-17T08:03:55Z - triptijain2112 (@triptijain2112) - PR: [Remove Python 3.9 from merge workflow #1543](https://github.com/Azure/azure-devops-cli-extension/pull/1543)
  - [Post-Release-1.0.11 (#1542)](https://github.com/Azure/azure-devops-cli-extension/commit/d08344a0faa5ed9afc26a764e39e2a41f1bd1589) - 2026-11-17T06:47:15Z - mishrarish (@mishrarish) - PR: [Post-Release-1.0.11 #1542](https://github.com/Azure/azure-devops-cli-extension/pull/1542)

- **Azure/azure-iot-sdk-node** (`main`) - **2** commit(s)
  - [Merge pull request #1273 from Azure/maximsemenov/e2e-storage-policy-s…](https://github.com/Azure/azure-iot-sdk-node/commit/73f3444eaeac0a6cf9efcc18604d813d26fc49c5) - 2026-11-17T21:33:53Z - Ewerton Scaboro da Silva (@ewertons) - PR: [ci: opt the e2e resource group out of the storage public access policy #1273](https://github.com/Azure/azure-iot-sdk-node/pull/1273)
  - [e2e: tag the e2e resource group to opt out of the storage public acce…](https://github.com/Azure/azure-iot-sdk-node/commit/9a0c00462edf730221a02b29456aa193c49e4fe2) - 2026-11-17T19:33:19Z - maximsemenov (@maximsemenov80) - PR: [ci: opt the e2e resource group out of the storage public access policy #1273](https://github.com/Azure/azure-iot-sdk-node/pull/1273)

- **Azure/LogicAppsUX** (`main`) - **2** commit(s)
  - [feat: add TypeScript graph layout engine for designer v2 (#9708)](https://github.com/Azure/LogicAppsUX/commit/cb3426747f80a8bcf9be379792ea16d82ab82e5b) - 2026-11-16T23:16:55Z - Riley Evans (@rllyy97) - PR: [feat: add TypeScript graph layout engine for designer v2 #9708](https://github.com/Azure/LogicAppsUX/pull/9708)
  - [feat(designer-ui-v2): Otto node parity, shared branch axis fix and St…](https://github.com/Azure/LogicAppsUX/commit/832f686595da5599e897e6c23902dc30be55a639) - 2026-11-16T21:07:44Z - Krrish Mittal (@takyyon) - PR: [feat(designer-ui-v2): Otto node parity, shared branch axis fix and Standard wiring behind useSharedNodeUi #9710](https://github.com/Azure/LogicAppsUX/pull/9710)

- **Azure/iotedge-eflow** (`main`) - **2** commit(s)
  - [Merge pull request #320 from nnamuhcs/docs/eflow-1.6.1.11026-release-…](https://github.com/Azure/iotedge-eflow/commit/0136dd266ca4a5d7cf47ece97811ee1dc3be4f94) - 2026-11-16T21:51:00Z - Joseph Knierman (@josephknierman) - PR: [Add EFLOW 1.6.1.11026 LTS release notes #320](https://github.com/Azure/iotedge-eflow/pull/320)
  - [Merge pull request #321 from nnamuhcs/docs/eflow-1.6-readme](https://github.com/Azure/iotedge-eflow/commit/c64d5197f0b50a7e001a367a4d22a5a5c52249f8) - 2026-11-16T21:44:33Z - Joseph Knierman (@josephknierman) - PR: [Update README for EFLOW 1.6 LTS #321](https://github.com/Azure/iotedge-eflow/pull/321)

- **Azure/azure-sdk-for-rust** (`main`) - **1** commit(s)
  - [Include unstable Cosmos APIs in docs.rs (#5605)](https://github.com/Azure/azure-sdk-for-rust/commit/93609e532efad72cda3645b9621b31fbdf23654e) - 2026-11-17T20:12:06Z - Ashley Stanton-Nurse (@analogrelay) - PR: [Include unstable Cosmos APIs in docs.rs #5605](https://github.com/Azure/azure-sdk-for-rust/pull/5605)

- **Azure/azure-sdk-for-cpp** (`main`) - **1** commit(s)
  - [Fix strict-mode service package discovery (#7548)](https://github.com/Azure/azure-sdk-for-cpp/commit/0da57ac2a73cf25fd5ff792df14058f4afdff7bf) - 2026-11-17T16:52:07Z - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [Sync eng/common directory with azure-sdk-tools for PR 17550 #7548](https://github.com/Azure/azure-sdk-for-cpp/pull/7548)

- **Azure/awesome-azd** (`main`) - **1** commit(s)
  - [Retire archived template repositories (#1125)](https://github.com/Azure/awesome-azd/commit/fb5d3ad48a8b064fc6231d9608d04ff2f123aa14) - 2026-11-17T03:51:39Z - hemarina (@hemarina) - PR: [Retire archived template repositories #1125](https://github.com/Azure/awesome-azd/pull/1125)

- **Azure/AI-Landing-Zones** (`main`) - **1** commit(s)
  - [docs: refresh validated planner prices](https://github.com/Azure/AI-Landing-Zones/commit/5276e3adf2d06f76f58f94f04a544f8307291981) - 2026-11-17T00:26:16Z - github-actions[bot] (@github-actions[bot])

- **Azure/PSDocs.Azure-quickstart** (`main`) - **1** commit(s)
  - [Pin GitHub Actions to full-length commit SHAs (#288)](https://github.com/Azure/PSDocs.Azure-quickstart/commit/5eda3a668883abda22ee408a093b31db1fa84ff3) - 2026-11-16T21:03:31Z - Dan Fiedler (@danfiedler-msft) - PR: [Pin GitHub Actions to full-length commit SHAs #288](https://github.com/Azure/PSDocs.Azure-quickstart/pull/288)

### MicrosoftDocs

- **MicrosoftDocs/azure-docs** (`main`) - **81** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/azure-do…](https://github.com/MicrosoftDocs/azure-docs/commit/40311f7c11b40b0f0b94ec04e077489c4410bba0) - 2026-11-17T20:54:41Z - Learn Build Service GitHub App
  - [Merge pull request #322593 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/azure-docs/commit/d5956ed58ee0af8d70cb03d993b128a0fc9e4b88) - 2026-11-17T20:53:38Z - Bowen Yang (@Albertyang0)
  - [Document Teams Phone Extensibility call arrival display info (#321373)](https://github.com/MicrosoftDocs/azure-docs/commit/ad12904213a5da739cf9dca2b6dfe10a28b208c2) - 2026-11-17T20:41:56Z - Heni (@henikaraa)
  - [Remove tokyo2 for ntt (#322518)](https://github.com/MicrosoftDocs/azure-docs/commit/8037c5a8dbe52c0defe0cbd6714733f138bf276f) - 2026-11-17T20:39:32Z - jeff-lovette (@jeff-lovette)
  - [Fix location entry for NTT DOCOMO BUSINESS (#322519)](https://github.com/MicrosoftDocs/azure-docs/commit/1be0d408082104fc9972222e19c03d2300ad4a5f) - 2026-11-17T20:39:21Z - jeff-lovette (@jeff-lovette)

- **MicrosoftDocs/entra-docs** (`main`) - **37** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/entra-do…](https://github.com/MicrosoftDocs/entra-docs/commit/fbedfc384b912731476e8bdc53e424def5e1fc6c) - 2026-11-17T18:37:29Z - Learn Build Service GitHub App
  - [Merge pull request #15023 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/entra-docs/commit/d98a58b6917e3579920d4dee0c92845777915556) - 2026-11-17T18:33:33Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
  - [Merge pull request #15022 from idMdev/main](https://github.com/MicrosoftDocs/entra-docs/commit/f6a79c6f6570d2e263975c735b846f1507c119e5) - 2026-11-17T18:16:20Z - prmerger-automator[bot] (@prmerger-automator[bot])
  - [Update link format for M365 targeted releases](https://github.com/MicrosoftDocs/entra-docs/commit/488ac185f77de1a14161ffea957c5ed053afd5c5) - 2026-11-17T18:09:56Z - Alexander Pavlovsky (@idMdev)
  - [Fix link for M365 targeted releases in browser settings](https://github.com/MicrosoftDocs/entra-docs/commit/5d6c401408a70f2be2a595c96e0a324ebd7ed23a) - 2026-11-17T18:03:35Z - Alexander Pavlovsky (@idMdev)

- **MicrosoftDocs/SupportArticles-docs** (`main`) - **22** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/05593c146e8113a515e9074fcaa0b8c5d1c415d7) - 2026-11-17T18:17:57Z - Learn Build Service GitHub App
  - [AB# [OOB Publish | MS IGNITE | 11/17 10:20 AM PST | Blog-Linked] -- W…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/c294ce599a7be26c39f8423939d10b52ef41c9d2) - 2026-11-17T18:16:06Z - Teresa Appelgate (@v-tappelgate)
  - [Merging changes synced from https://github.com/MicrosoftDocs/SupportA…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/13fded7120b6f50851a24c0bdc0f2cf4dbd06449) - 2026-11-17T18:06:02Z - Learn Build Service GitHub App
  - [Merge pull request #12884 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/3d4292aa670eb0e4c5979a9e3657e6d4e9df5769) - 2026-11-17T18:03:46Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
  - [Add troubleshooting article: incorrect CPU core/logical processor cou…](https://github.com/MicrosoftDocs/SupportArticles-docs/commit/2ba513721459cbc67648894521cba8e76646df0b) - 2026-11-17T17:45:06Z - Scott Roberts (Azure) (@ScottAzure)

- **MicrosoftDocs/learn** (`main`) - **16** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/317ba31981297efe47f0a81146817a532f427bef) - 2026-11-17T18:19:54Z - Learn Build Service GitHub App
  - [Merge pull request #56863 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/learn/commit/e62c56523a6d02d598af434a00ccee6f429ce65a) - 2026-11-17T18:09:44Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
  - [New ignite perception rebrand 11 2026 (#56843) (#56862)](https://github.com/MicrosoftDocs/learn/commit/6c20a00acd570ec9fe0d071b721366c8e374cb63) - 2026-11-17T16:26:38Z - Hassan Rasheed (@hrasheed-msft)
  - [Merging changes synced from https://github.com/MicrosoftDocs/learn-pr…](https://github.com/MicrosoftDocs/learn/commit/38a092d83e439c7d9b4a8283e32ad626481a158f) - 2026-11-17T12:23:39Z - Learn Build Service GitHub App
  - [Merge pull request #56861 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/learn/commit/d8c7f0763ab2fd1c08d0401c7a81e451699e5be5) - 2026-11-17T12:09:10Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

- **MicrosoftDocs/dynamics-365-unified-operations-public** (`main`) - **15** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/Dynamics…](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/c22651b9940de291bcea7b7ab0a6cb3c5bd79555) - 2026-11-17T19:07:21Z - Learn Build Service GitHub App
  - [Merge pull request #22869 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/456e986a2baccbb518badd5eec33303cd638f397) - 2026-11-17T19:04:56Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
  - [Row version change tracking for tables and data entities (#22867)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/5bcfa72813ef34d530c5d1e43073ec1a715e0131) - 2026-11-17T18:15:57Z - John Michalak (@johnmichalak)
  - [Restore 'Import the Globalization solution' section (#22863)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/0de2145400cca0a9af22aaf0a73ec226033b7cd9) - 2026-11-17T17:51:18Z - Elizaveta Golub (@liza-golub)
  - [Document required BI entity field names for archive LTR (#22857)](https://github.com/MicrosoftDocs/dynamics-365-unified-operations-public/commit/9ba21023487fd42b79a5af2c99402c19019a9518) - 2026-11-17T17:50:27Z - Nandadev Rajeev Menon (@nandadevrmenon)

- **MicrosoftDocs/sql-docs** (`live`) - **14** commit(s)
  - [State that BACKUP SYMMETRIC KEY needs the key to be open (#10477)](https://github.com/MicrosoftDocs/sql-docs/commit/6c3acb56dc3be462ab139d1afbb6a0f98e50e169) - 2026-11-17T21:35:16Z - Rudi Bruchez (@rudi-bruchez) - PR: [State that BACKUP SYMMETRIC KEY needs the key to be open #10477](https://github.com/MicrosoftDocs/sql-docs/pull/10477)
  - [Expired certificates: clarify behavior with TLS session resumption (#…](https://github.com/MicrosoftDocs/sql-docs/commit/f5bb2138963332b8acc7b2bdac6365eda4674eb3) - 2026-11-17T21:34:15Z - Ltochon (@Ltochon) - PR: [Expired certificates: clarify behavior with TLS session resumption #10411](https://github.com/MicrosoftDocs/sql-docs/pull/10411)
  - [Correct the schema ID described by the user_id plan attribute (#10500)](https://github.com/MicrosoftDocs/sql-docs/commit/42862e34c45d7a1a5e6379f7cc092acbc759c924) - 2026-11-17T20:26:53Z - Rudi Bruchez (@rudi-bruchez) - PR: [Correct the schema ID described by the user_id plan attribute #10500](https://github.com/MicrosoftDocs/sql-docs/pull/10500)
  - [Fix the Adhoc objtype value in sys.dm_exec_cached_plans (#10498)](https://github.com/MicrosoftDocs/sql-docs/commit/012e6898def7e1278babd15aba35cc8f1f8d390b) - 2026-11-17T20:19:59Z - Rudi Bruchez (@rudi-bruchez) - PR: [Fix the Adhoc objtype value in sys.dm_exec_cached_plans #10498](https://github.com/MicrosoftDocs/sql-docs/pull/10498)
  - [Fix the index_id range of a nonclustered columnstore index in sys.int…](https://github.com/MicrosoftDocs/sql-docs/commit/724b9dfe01a5824b95df49f5fd5c807abd23be1f) - 2026-11-17T20:11:56Z - Rudi Bruchez (@rudi-bruchez) - PR: [Fix the index_id range of a nonclustered columnstore index in sys.internal_partitions #10494](https://github.com/MicrosoftDocs/sql-docs/pull/10494)

- **MicrosoftDocs/powerapps-docs** (`main`) - **12** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/powerapp…](https://github.com/MicrosoftDocs/powerapps-docs/commit/8a1264ce7a87710bc51b25fad3b9ea4a9ce39418) - 2026-11-17T19:08:05Z - Learn Build Service GitHub App
  - [Merge pull request #12871 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/powerapps-docs/commit/c2c9d08b8449606455cbddfcb4b53915c469138a) - 2026-11-17T19:05:34Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
  - [Update (#12870)](https://github.com/MicrosoftDocs/powerapps-docs/commit/257cf8a7ad8a41d6442eee621c058d79e65bf4f1) - 2026-11-17T18:42:32Z - Tapan Maniar (@tapanm-MSFT)
  - [BizApps preview include with preview features (#12869)](https://github.com/MicrosoftDocs/powerapps-docs/commit/fcfa29bdc831edbe673ed72b9a0bb1525e4e2daf) - 2026-11-17T18:28:48Z - Tapan Maniar (@tapanm-MSFT)
  - [Final edits for Ignite 2026 (#12867)](https://github.com/MicrosoftDocs/powerapps-docs/commit/46826223cbc37ba3318716db0c0951cd2cbdfe0b) - 2026-11-17T14:43:21Z - Erika Doyle Navara (@erikadoyle)

- **MicrosoftDocs/power-platform** (`main`) - **11** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/2be0811144d8cfae7f8276968496221896dd5eb7) - 2026-11-17T19:05:01Z - Learn Build Service GitHub App
  - [Merge pull request #12199 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-platform/commit/a16f46179f8130644cf21acf0b8df131d4c216ef) - 2026-11-17T19:03:36Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
  - [Add preview features section for Work IQ (#12198)](https://github.com/MicrosoftDocs/power-platform/commit/eef4d8ae7e72a104ff9f6b463de89c6974d1e064) - 2026-11-17T18:43:25Z - Tapan Maniar (@tapanm-MSFT)
  - [Merging changes synced from https://github.com/MicrosoftDocs/power-pl…](https://github.com/MicrosoftDocs/power-platform/commit/fb877948f865dcf42a2923fdd21a4d721c30136a) - 2026-11-17T13:14:04Z - Learn Build Service GitHub App
  - [Merge pull request #12197 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/power-platform/commit/918574988dd4ed34eb6b203a221408c6efaa5389) - 2026-11-17T13:12:30Z - Tapan Maniar (@tapanm-MSFT)

- **MicrosoftDocs/dynamics-365-contact-center** (`main`) - **11** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/a33f708e26776e6db8e61ae0ede901861c4fe315) - 2026-11-17T13:06:16Z - Learn Build Service GitHub App
  - [Merge pull request #832 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/03c08ab8ffe64b5124b1344e0a5955b69c52ad61) - 2026-11-17T13:05:50Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
  - [Enhance Human Assist documentation for administrators (#828)](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/30fd723a80a1d09fcbbc5e5f608f02960adcd20c) - 2026-11-17T08:17:17Z - isabelgreene (@isabelgreene)
  - [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/9f669ae8258b075ddb2df0be4513ad6eb83533d6) - 2026-11-17T07:02:37Z - Learn Build Service GitHub App
  - [Merge pull request #831 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-contact-center/commit/edf46b30c0d8f38f2a937f65e52cf88fa4581ed0) - 2026-11-17T07:02:14Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot])

- **MicrosoftDocs/azure-docs-cli** (`main`) - **9** commit(s)
  - [Revert "Document which errors skip automatic AI recovery (#6351)" (#6…](https://github.com/MicrosoftDocs/azure-docs-cli/commit/431331a0ce123fbb2772e1ba211b1dfea90f2f26) - 2026-11-17T21:11:46Z - Kelly Gremban (@kgremban) - PR: [Revert "Document which errors skip automatic AI recovery" #6353](https://github.com/MicrosoftDocs/azure-docs-cli/pull/6353)
  - [Document which errors skip automatic AI recovery (#6351)](https://github.com/MicrosoftDocs/azure-docs-cli/commit/265564c02bd66e4291efc6d4159b924b11dda348) - 2026-11-17T21:06:19Z - Aakash Basavaraj [MSFT] (@aakashbsrj) - PR: [Document which errors skip automatic AI recovery #6351](https://github.com/MicrosoftDocs/azure-docs-cli/pull/6351)
  - [Update Azure CLI preview docs with PM answers (AI recovery settings, …](https://github.com/MicrosoftDocs/azure-docs-cli/commit/fd4ca095d1a412771ae77a87f1713c6c525e1f53) - 2026-11-17T21:02:48Z - M. Baldwin (@msmbaldwin) - PR: [Update Azure CLI preview docs with PM answers (AI recovery settings, managed identity tutorial) #6345](https://github.com/MicrosoftDocs/azure-docs-cli/pull/6345)
  - [Add demo videos to the Azure CLI preview overview and AI error recove…](https://github.com/MicrosoftDocs/azure-docs-cli/commit/6fb38c7255128fa3cd95f4cd00ba98c8a05591f9) - 2026-11-17T20:33:31Z - Aakash Basavaraj [MSFT] (@aakashbsrj) - PR: [Add demo videos to the Azure CLI preview overview and AI error recovery articles #6349](https://github.com/MicrosoftDocs/azure-docs-cli/pull/6349)
  - [CI Update](https://github.com/MicrosoftDocs/azure-docs-cli/commit/11f329bd8c95e8e440528a8ad0a3698369511fa2) - 2026-11-17T12:52:07Z - docsreference@microsoft.com

- **MicrosoftDocs/m365copilot-docs** (`main`) - **7** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/m365copi…](https://github.com/MicrosoftDocs/m365copilot-docs/commit/4ce0baff32be9db9953a918b77dc7be2ca69f03a) - 2026-11-17T19:47:39Z - Learn Build Service GitHub App
  - [Merge pull request #1849 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/m365copilot-docs/commit/f4aebbba8c4a301ac0e4c68d8f4b223dc44e814b) - 2026-11-17T19:46:59Z - Jason Johnston (@jasonjoh)
  - [Updated Reports API topics to remove v1 (#1848)](https://github.com/MicrosoftDocs/m365copilot-docs/commit/138201a73c98f87d349e6698e65f85f3c556c300) - 2026-11-17T19:24:53Z - Jason Johnston (@jasonjoh)
  - [Clarify validation scope and new-file author metadata (#1847)](https://github.com/MicrosoftDocs/m365copilot-docs/commit/a0037f2888dd213da645eb208fb1b15b44f9d523) - 2026-11-17T15:14:56Z - Jason Johnston (@jasonjoh)
  - [Merging changes synced from https://github.com/MicrosoftDocs/m365copi…](https://github.com/MicrosoftDocs/m365copilot-docs/commit/8c1cf33dcc7995a4a9d3f978564c23009e1e41d4) - 2026-11-16T23:05:01Z - Learn Build Service GitHub App

- **MicrosoftDocs/windowsserverdocs** (`main`) - **7** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/windowss…](https://github.com/MicrosoftDocs/windowsserverdocs/commit/5fbc977f419e1a80f4087452552d2f1b7d21e460) - 2026-11-17T18:34:45Z - Learn Build Service GitHub App
  - [Merge pull request #10091 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/windowsserverdocs/commit/09178ccc2c58bf3d280e63502f7e5a11fc613727) - 2026-11-17T18:33:16Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
  - [Add Windows Server 2028 preview removals (#8499)](https://github.com/MicrosoftDocs/windowsserverdocs/commit/4da025351e1319159a87f8be8ddfe35b36586bfa) - 2026-11-17T18:19:38Z - Robin Harwood (@robinharwood)
  - [Add SMB Policy Controller documentation (#8726)](https://github.com/MicrosoftDocs/windowsserverdocs/commit/3d9ce5d6060bf03e2f25f9c1749af2f851d4f51e) - 2026-11-17T16:56:34Z - Robin Harwood (@robinharwood)
  - [Add What's new in Windows Server 2028 Preview (#8501)](https://github.com/MicrosoftDocs/windowsserverdocs/commit/deb8dad3d5771a59a74717f32b75d7c1d69f3f7e) - 2026-11-17T16:52:58Z - Robin Harwood (@robinharwood)

- **MicrosoftDocs/azure-docs-powershell** (`main`) - **6** commit(s)
  - [Update Azure PowerShell preview docs with PM answers (sign-in methods…](https://github.com/MicrosoftDocs/azure-docs-powershell/commit/947f8bbab8026ed8f0f970810d3b7e89fcd1d853) - 2026-11-17T20:51:41Z - M. Baldwin (@msmbaldwin) - PR: [Update Azure PowerShell preview docs with PM answers (sign-in methods, feedback cmdlet, managed identity tutorial) #4506](https://github.com/MicrosoftDocs/azure-docs-powershell/pull/4506)
  - [Fix preview landing page feedback link (#4508)](https://github.com/MicrosoftDocs/azure-docs-powershell/commit/2537237443a07c84b44f6a0dddf04d2e2573d8d7) - 2026-11-17T20:03:53Z - Alex Wang (@Alex-AZPS) - PR: [Fix Azure PowerShell preview landing page feedback link #4508](https://github.com/MicrosoftDocs/azure-docs-powershell/pull/4508)
  - [Add demo videos to the Azure PowerShell preview getting started, over…](https://github.com/MicrosoftDocs/azure-docs-powershell/commit/bdfc604424b1d9e3dc856e5642593e949b379d48) - 2026-11-17T19:34:32Z - Aakash Basavaraj [MSFT] (@aakashbsrj) - PR: [Add demo videos to the Azure PowerShell preview getting started, overview, and profiles articles #4509](https://github.com/MicrosoftDocs/azure-docs-powershell/pull/4509)
  - [Add Azure PowerShell preview version of the interactive sign-in artic…](https://github.com/MicrosoftDocs/azure-docs-powershell/commit/97f7b71e4b989b86dc46de1ed226dc99fb54a96a) - 2026-11-16T23:11:23Z - M. Baldwin (@msmbaldwin) - PR: [Add Azure PowerShell preview version of the interactive sign-in article #4505](https://github.com/MicrosoftDocs/azure-docs-powershell/pull/4505)
  - [Replace engineering placeholders in Azure PowerShell preview Bicep an…](https://github.com/MicrosoftDocs/azure-docs-powershell/commit/605b6f3619003bf9c4c358a43602aed3d0d5822c) - 2026-11-16T22:30:44Z - M. Baldwin (@msmbaldwin) - PR: [Replace engineering placeholders in Azure PowerShell preview Bicep and VM tutorials #4504](https://github.com/MicrosoftDocs/azure-docs-powershell/pull/4504)

- **MicrosoftDocs/azure-docs-sdk-node** (`main`) - **6** commit(s)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/ee4a7e21f3fe01fe2550dbdcf344f6db1d7a1d85) - 2026-11-17T19:32:30Z - azure-sdk (@azure-sdk)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/f4de81a3e5605e4f72f253527ad2f1e09b990075) - 2026-11-17T19:25:50Z - azure-sdk (@azure-sdk)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/07e045f83aa99a14ba8ebe57a9509a4d42116d96) - 2026-11-17T16:33:12Z - azure-sdk (@azure-sdk)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/549098ce4bc111ffbf33f51c25b2b436f561a0f3) - 2026-11-17T06:49:03Z - azure-sdk (@azure-sdk) - PR: [Manual merge of main -> live #1740](https://github.com/MicrosoftDocs/azure-docs-sdk-node/pull/1740)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-node/commit/6f2a90f2b92813c42641d373543e408f28d20c91) - 2026-11-17T03:48:14Z - azure-sdk (@azure-sdk) - PR: [Manual merge of main -> live #1740](https://github.com/MicrosoftDocs/azure-docs-sdk-node/pull/1740)

- **MicrosoftDocs/azure-docs-sdk-dotnet** (`main`) - **6** commit(s)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/85597f546031f1706afdb49e9b777ed203c0e991) - 2026-11-17T07:32:12Z - azure-sdk (@azure-sdk)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/31115f71ce3c521bfc35082917000f4b2cd13ee7) - 2026-11-17T05:19:20Z - azure-sdk (@azure-sdk)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/832590ae965531d5ed6d57ff283edaf6074497a3) - 2026-11-17T05:18:30Z - azure-sdk (@azure-sdk)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/174e034c994d8059c6357cd35664de38cdd88ea8) - 2026-11-17T04:04:47Z - azure-sdk (@azure-sdk)
  - [CI Update](https://github.com/MicrosoftDocs/azure-docs-sdk-dotnet/commit/a46f6e57c6883c3e16479cad87a4fb37d1c2f89d) - 2026-11-17T02:20:42Z - docsreference@microsoft.com

- **MicrosoftDocs/azure-docs-sdk-python** (`main`) - **5** commit(s)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/98004c1db0c21384a4643f339e158f8814efeb09) - 2026-11-17T17:45:40Z - azure-sdk (@azure-sdk)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/3378b4dd7de8e410696f52166b56336bcc860cf6) - 2026-11-17T11:04:05Z - azure-sdk (@azure-sdk)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/aa5a1471272a6669948092df296663cc367f6a71) - 2026-11-17T10:09:06Z - azure-sdk (@azure-sdk)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/ae89e0dcceab17ed954c2d81b2ca8799a940c007) - 2026-11-17T05:29:03Z - azure-sdk (@azure-sdk)
  - [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-python/commit/43c760cb0b8c5e54e816c7ecfca04e735e000ac6) - 2026-11-16T23:10:52Z - azure-sdk (@azure-sdk)

- **MicrosoftDocs/msteams-docs** (`main`) - **4** commit(s)
  - [Update deprecated page (#14745)](https://github.com/MicrosoftDocs/msteams-docs/commit/7c0a9ca72cd27ac8388373f37334f741f36435c3) - 2026-11-17T21:30:25Z - Nick Walker (@nickwalkmsft) - PR: [Update deprecated page #14745](https://github.com/MicrosoftDocs/msteams-docs/pull/14745)
  - [Refactor threading information (#14743)](https://github.com/MicrosoftDocs/msteams-docs/commit/7e59f19d2c9082ce526080fc47dafab74472a892) - 2026-11-17T18:22:26Z - Corina (@corinagum) - PR: [[Doc Improvement] Clarify reactive and proactive threading methods #14743](https://github.com/MicrosoftDocs/msteams-docs/pull/14743)
  - [[Doc Improvement] Clarify agent threading availability (#14742)](https://github.com/MicrosoftDocs/msteams-docs/commit/cb344b27979bc6b7a69a914951f12f5947f5beb0) - 2026-11-17T00:42:51Z - Adrian Solis (@aosolis) - PR: [[Doc Improvement] Clarify agent threading availability #14742](https://github.com/MicrosoftDocs/msteams-docs/pull/14742)
  - [[Doc Feature] Chain of Thought (#14683)](https://github.com/MicrosoftDocs/msteams-docs/commit/b548dfcb2b69875c0b17a8a9b7537ffe256c762b) - 2026-11-16T21:12:11Z - SirajShaik-MSFT (@SirajShaik-MSFT) - PR: [[Doc Feature] Chain of Thought #14683](https://github.com/MicrosoftDocs/msteams-docs/pull/14683)

- **MicrosoftDocs/azure-docs-sdk-java** (`main`) - **4** commit(s)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/1e84f5ec4cb113cc46ce57248d71cb833677fa5d) - 2026-11-17T17:26:18Z - azure-sdk (@azure-sdk)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/741bbf7f426d518557dd7d087149f66613af124c) - 2026-11-17T08:53:56Z - azure-sdk (@azure-sdk) - PR: [Manual merge of main -> live #2665](https://github.com/MicrosoftDocs/azure-docs-sdk-java/pull/2665)
  - [Update docs metadata](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/aff71238da500f6ae76c006faa4965ce8590291c) - 2026-11-17T05:05:33Z - azure-sdk (@azure-sdk) - PR: [Manual merge of main -> live #2665](https://github.com/MicrosoftDocs/azure-docs-sdk-java/pull/2665)
  - [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-java/commit/5939a789286b27ea5d82c598da2bf55d62049f2d) - 2026-11-16T23:46:54Z - azure-sdk (@azure-sdk) - PR: [Manual merge of main -> live #2665](https://github.com/MicrosoftDocs/azure-docs-sdk-java/pull/2665)

- **MicrosoftDocs/dynamics365smb-devitpro-pb** (`main`) - **4** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/8bdf7490314e037c34629c2de42d389b426ed7f2) - 2026-11-17T13:03:51Z - Learn Build Service GitHub App
  - [Merge pull request #8162 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/1f8e7e277b128e636d19c62b667a546b3263e6c5) - 2026-11-17T13:03:08Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
  - [Enhance Expense Agent billing details and examples (#8145)](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/c3c7cfac83c9b2a98b3c06aefed6ec6d3bd01637) - 2026-11-17T12:04:40Z - Aleksandar Totovic (@altotovi)
  - [Document Expense Management limitation for on-premises (#8155)](https://github.com/MicrosoftDocs/dynamics365smb-devitpro-pb/commit/91abe289fb5ba5ecf4843eb44ad082bb9055cb6a) - 2026-11-17T12:03:28Z - Aleksandar Totovic (@altotovi)

- **MicrosoftDocs/azure-stack-docs** (`main`) - **3** commit(s)
  - [Merge pull request #4601 from MicrosoftDocs/main639305422059814458syn…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/dfd4057b6a94a5e0e459ddba3812ba5e426c2e76) - 2026-11-17T19:57:15Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch #4601](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4601)
  - [Merging changes synced from https://github.com/MicrosoftDocs/azure-st…](https://github.com/MicrosoftDocs/azure-stack-docs/commit/6771fe3922407b874e957777655ca2d377613387) - 2026-11-17T19:56:42Z - Learn Build Service GitHub App - PR: [Repo sync for protected branch #4601](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4601)
  - [Release ignite26 release (#22025) (#22029)](https://github.com/MicrosoftDocs/azure-stack-docs/commit/58f4726da988956d300ab9788fef9d3c98e7b42a) - 2026-11-17T19:55:12Z - Huaping Yu (@huypub) - PR: [Repo sync for protected branch #4601](https://github.com/MicrosoftDocs/azure-stack-docs/pull/4601)

- **MicrosoftDocs/fabric-docs** (`main`) - **3** commit(s)
  - [Merge pull request #3518 from MicrosoftDocs/main639305421011189270syn…](https://github.com/MicrosoftDocs/fabric-docs/commit/585fc575fe2730e88ee0a67d0b7684e9ede883e2) - 2026-11-17T19:55:18Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch #3518](https://github.com/MicrosoftDocs/fabric-docs/pull/3518)
  - [Merging changes synced from https://github.com/MicrosoftDocs/fabric-d…](https://github.com/MicrosoftDocs/fabric-docs/commit/62a0f1e10cbb241d4349965931a2d36ae970f6c0) - 2026-11-17T19:54:57Z - Learn Build Service GitHub App - PR: [Repo sync for protected branch #3518](https://github.com/MicrosoftDocs/fabric-docs/pull/3518)
  - [Release ignite26 release (#17404) (#17415)](https://github.com/MicrosoftDocs/fabric-docs/commit/2fab22d310509d78b3288c0bc50759a071857f2e) - 2026-11-17T19:51:23Z - Huaping Yu (@huypub) - PR: [Repo sync for protected branch #3518](https://github.com/MicrosoftDocs/fabric-docs/pull/3518)

- **MicrosoftDocs/dynamics-365-project-operations** (`main`) - **3** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/64260337ba4b57f558fec6b47a66db6c593b9ad1) - 2026-11-17T19:02:39Z - Learn Build Service GitHub App
  - [Merge pull request #2828 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/5dc210901a71793828553783e73ddd108f184122) - 2026-11-17T19:02:08Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
  - [Field Service integration v3 updates (#2775)](https://github.com/MicrosoftDocs/dynamics-365-project-operations/commit/a7e597d66a3e5ee165d7cadeccb2d915cf000f55) - 2026-11-17T13:51:13Z - Wendy Smith (@v-wendysmith)

- **MicrosoftDocs/dynamics365smb-docs** (`main`) - **3** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/dynamics…](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/b3b7eb0a831cfab9830b478e2a2dce534721b918) - 2026-11-17T13:03:24Z - Learn Build Service GitHub App
  - [Merge pull request #5291 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/2ff0abe00fd034cbc5cbaed607983d88e10079a4) - 2026-11-17T13:02:35Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
  - [refresh by agent (#5289)](https://github.com/MicrosoftDocs/dynamics365smb-docs/commit/4ba87f7ac3d3cac3a648e65516b62f18ffceda94) - 2026-11-17T08:43:45Z - jswymer (@jswymer)

- **MicrosoftDocs/microsoft-salescopilot-docs** (`main`) - **3** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/viva-doc…](https://github.com/MicrosoftDocs/microsoft-salescopilot-docs/commit/117dabca8e83dcbc59c79429371886d95cba6122) - 2026-11-17T07:02:55Z - Learn Build Service GitHub App
  - [Merge pull request #615 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/microsoft-salescopilot-docs/commit/b1e7ebae15792cb9c8c83b9f6279ca1f17195121) - 2026-11-17T07:02:31Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot])
  - [Business skills unsupported on mobile](https://github.com/MicrosoftDocs/microsoft-salescopilot-docs/commit/4c4b5b887178ed8499e555d0fff27ade2e0707ab) - 2026-11-17T06:19:36Z - katielegan (@katielegan)

- **MicrosoftDocs/visualstudio-docs** (`main`) - **3** commit(s)
  - [Merge pull request #11494 from MicrosoftDocs/main639304635050243658sy…](https://github.com/MicrosoftDocs/visualstudio-docs/commit/55f03ccb7c47ec059c5a10fbb20407dfd39606df) - 2026-11-16T22:05:22Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch #11494](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11494)
  - [Merging changes synced from https://github.com/MicrosoftDocs/visualst…](https://github.com/MicrosoftDocs/visualstudio-docs/commit/efdf3afb02f202cea87e21414587f9d81c6b01cb) - 2026-11-16T22:05:00Z - Learn Build Service GitHub App - PR: [Repo sync for protected branch #11494](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11494)
  - [Merge pull request #15823 from MicrosoftDocs/main](https://github.com/MicrosoftDocs/visualstudio-docs/commit/fdb162e87b81bb402817b8e342a3428529bd2f9d) - 2026-11-16T22:02:41Z - learn-build-service-prod[bot] (@learn-build-service-prod[bot]) - PR: [Repo sync for protected branch #11494](https://github.com/MicrosoftDocs/visualstudio-docs/pull/11494)

- **MicrosoftDocs/azure-compute-docs** (`main`) - **2** commit(s)
  - [Update AMD Windows driver download links to version 26.Q4 from MR2 (#…](https://github.com/MicrosoftDocs/azure-compute-docs/commit/1dc022c8143524da8113462da5b7fc8b3137547e) - 2026-11-17T20:19:08Z - Simon2228 (@Simon2228) - PR: [Update AMD Windows driver download links to version 26.Q4 from MR2 #533](https://github.com/MicrosoftDocs/azure-compute-docs/pull/533)
  - [Release ignite26 release (#4382) (#4383)](https://github.com/MicrosoftDocs/azure-compute-docs/commit/bef1b51405ad941cf7a2c0612734a4375ab22894) - 2026-11-17T19:45:05Z - Huaping Yu (@huypub)

- **MicrosoftDocs/azure-dev-docs** (`main`) - **2** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/azure-de…](https://github.com/MicrosoftDocs/azure-dev-docs/commit/4ecfd234bf7bea55a0d2f499c432cb7502f04006) - 2026-11-17T19:52:24Z - Learn Build Service GitHub App
  - [Release ignite26 release (#9990) (#9992)](https://github.com/MicrosoftDocs/azure-dev-docs/commit/cc8e8e30911ece3721543a2d1467fe8e59f37101) - 2026-11-17T19:51:26Z - Huaping Yu (@huypub)

- **MicrosoftDocs/azure-aks-docs** (`main`) - **2** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/azure-ak…](https://github.com/MicrosoftDocs/azure-aks-docs/commit/8e860e2297a8649c3a221fbc420dbbebe9e75b7b) - 2026-11-17T19:52:13Z - Learn Build Service GitHub App
  - [Release ignite26 release (#4236) (#4239)](https://github.com/MicrosoftDocs/azure-aks-docs/commit/05f981f5d3299450da2d000cd9880222a83eafc4) - 2026-11-17T19:51:34Z - Huaping Yu (@huypub)

- **MicrosoftDocs/minecraft-creator** (`main`) - **2** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/minecraf…](https://github.com/MicrosoftDocs/minecraft-creator/commit/80b7b1713df821debb4a8022e32e6b0ad840a273) - 2026-11-17T16:45:07Z - Learn Build Service GitHub App
  - [Updating reference documentation for 1.26.70-preview.26](https://github.com/MicrosoftDocs/minecraft-creator/commit/c92631126a34b5752c8010bded76495368b2f96d) - 2026-11-17T16:43:05Z - mcautoma (@mcbuildmsft)

- **MicrosoftDocs/Advertising** (`main`) - **2** commit(s)
  - [Merging changes synced from https://github.com/MicrosoftDocs/Advertis…](https://github.com/MicrosoftDocs/Advertising/commit/39173818e002ef90476e6470144ca9037d0c5065) - 2026-11-17T00:13:18Z - Learn Build Service GitHub App
  - [Update MMC for AI labels (#830)](https://github.com/MicrosoftDocs/Advertising/commit/09af7be1b7d89f38a81a011c25e8e1098c1cac8e) - 2026-11-17T00:12:29Z - Rick Garitta (@rgaritta)

- **MicrosoftDocs/PowerShell-Docs** (`main`) - **1** commit(s)
  - [(GHA) Correct `checklist` workflow target (#13392)](https://github.com/MicrosoftDocs/PowerShell-Docs/commit/aedd8efe1fece22f04e478c2521c3fccc17ab03d) - 2026-11-17T21:44:25Z - Mikey Lombardi (He/Him) (@michaeltlombardi) - PR: [(GHA) Correct `checklist` workflow target #13392](https://github.com/MicrosoftDocs/PowerShell-Docs/pull/13392)

- **MicrosoftDocs/data-tools** (`main`) - **1** commit(s)
  - [Release ignite26 release (#969) (#971)](https://github.com/MicrosoftDocs/data-tools/commit/cc14abc4aadcb71dab3c5f2237e4881b962cf1e2) - 2026-11-17T19:55:20Z - Huaping Yu (@huypub)

- **MicrosoftDocs/azure-management-docs** (`main`) - **1** commit(s)
  - [Release ignite26 release (#3072) (#3076)](https://github.com/MicrosoftDocs/azure-management-docs/commit/f98f1ab1b30fdd81c5bdc4e9f6dffd03d8ae26c2) - 2026-11-17T19:55:08Z - Huaping Yu (@huypub)

- **MicrosoftDocs/azure-monitor-docs** (`main`) - **1** commit(s)
  - [Release ignite26 release (#5793) (#5797)](https://github.com/MicrosoftDocs/azure-monitor-docs/commit/f7722c76aa61318c9997e3aa98e019efc1b3aa7c) - 2026-11-17T19:51:29Z - Huaping Yu (@huypub)

- **MicrosoftDocs/windows-driver-docs** (`staging`) - **1** commit(s)
  - [Update WDK documentation for the November 2026 release (#3334)](https://github.com/MicrosoftDocs/windows-driver-docs/commit/3c2f95cb99487cf26a154803a4ffca8b30537e89) - 2026-11-17T10:09:16Z - 5an7y-Microsoft (@5an7y-Microsoft)

- **MicrosoftDocs/OfficeDocs-SharePoint-PowerShell** (`main`) - **1** commit(s)
  - [Document file last access date reporting cmdlets (#1256)](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint-PowerShell/commit/8bc07bfbcf00fff7846acccefdfc8229fcdb9fde) - 2026-11-17T01:56:54Z - Trent Green (@trent-green) - PR: [Document file last access date reporting cmdlets #1256](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint-PowerShell/pull/1256)

- **MicrosoftDocs/office-docs-powershell** (`main`) - **1** commit(s)
  - [Update New-CsUserServicesPolicy.md (#13885)](https://github.com/MicrosoftDocs/office-docs-powershell/commit/8a5961e5af2366fd7c2fdc6f84463450dce3102f) - 2026-11-17T01:01:00Z - paulkwo-msft2 (@paulkwo-msft2) - PR: [Update New-CsUserServicesPolicy.md #13885](https://github.com/MicrosoftDocs/office-docs-powershell/pull/13885)

- **MicrosoftDocs/azure-docs-sdk-cpp** (`main`) - **1** commit(s)
  - [Update docs CI configuration Build: https://dev.azure.com/azure-sdk/i…](https://github.com/MicrosoftDocs/azure-docs-sdk-cpp/commit/2359413e3fe2af10c7a5450c9b7045634da31a90) - 2026-11-16T23:21:34Z - azure-sdk (@azure-sdk)

### OfficeDev

- **OfficeDev/office-js-docs-reference** (`main`) - **1** commit(s)
  - [Automatically generated docs (#2667)](https://github.com/OfficeDev/office-js-docs-reference/commit/f237b8c3c03c94a602f91c976eb99f0899b5daf3) - 2026-11-17T17:27:55Z - Elizabeth Samuel (@ElizabethSamuel-MSFT) - PR: [Automatically generated docs #2667](https://github.com/OfficeDev/office-js-docs-reference/pull/2667)

### dotnet

- **dotnet/dotnet-api-docs** (`main`) - **26** commit(s)
  - [Bump System.CodeDom across 61 directories (#13356)](https://github.com/dotnet/dotnet-api-docs/commit/fc12a94db4a07d21e1a0fd98851c35f5bf2b9a45) - 2026-11-17T16:48:04Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump System.CodeDom across 61 directories #13356](https://github.com/dotnet/dotnet-api-docs/pull/13356)
  - [Bump System.Diagnostics.PerformanceCounter across 19 directories (#13…](https://github.com/dotnet/dotnet-api-docs/commit/b344319f7c41635028ff4fbfa2144ddd5559d531) - 2026-11-17T16:33:12Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump System.Diagnostics.PerformanceCounter across 19 directories #13355](https://github.com/dotnet/dotnet-api-docs/pull/13355)
  - [Bump System.Reflection.MetadataLoadContext in /snippets/csharp/System…](https://github.com/dotnet/dotnet-api-docs/commit/2f0fb4c76fa18b8e84cc1ccaec2cc60c1c02938f) - 2026-11-17T16:32:05Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump System.Reflection.MetadataLoadContext in /snippets/csharp/System.Reflection.Emit/PersistedAssemblyBuilder/Overview #13354](https://github.com/dotnet/dotnet-api-docs/pull/13354)
  - [Bump System.Reflection.Context in /snippets/csharp/System.Reflection.…](https://github.com/dotnet/dotnet-api-docs/commit/b469385105f7ce3adbd1e9462b7e9bb3198f46f6) - 2026-11-17T16:27:37Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump System.Reflection.Context in /snippets/csharp/System.Reflection.Context/CustomReflectionContext #13352](https://github.com/dotnet/dotnet-api-docs/pull/13352)
  - [Bump System.CodeDom in /snippets/csharp/System/Type/Missing (#13351)](https://github.com/dotnet/dotnet-api-docs/commit/afcd8728cba1a3b240d592c52f9b4b4d524cc3ff) - 2026-11-17T16:25:57Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump System.CodeDom in /snippets/csharp/System/Type/Missing #13351](https://github.com/dotnet/dotnet-api-docs/pull/13351)

- **dotnet/runtime** (`main`) - **24** commit(s)
  - [OpenSSL 4.1 compatibility](https://github.com/dotnet/runtime/commit/014646c4ceb68fe5b705f27db6a431c7227a718a) - 2026-11-17T18:33:51Z - Kevin Jones (@vcsjones) - PR: [OpenSSL 4.1 compatibility #137288](https://github.com/dotnet/runtime/pull/137288)
  - [JIT: enregister wasm GC locals with write-through homes (#137473)](https://github.com/dotnet/runtime/commit/acb1fd09c4bf863c390e3bce34851f80bba06119) - 2026-11-17T17:59:06Z - Andy Ayers (@AndyAyersMS) - PR: [JIT: enregister wasm GC locals with write-through homes #137473](https://github.com/dotnet/runtime/pull/137473)
  - [Update container image digests (main) (#137618)](https://github.com/dotnet/runtime/commit/6b2b6e753ec305369d1fe0070a3022ec0fd7884a) - 2026-11-17T17:07:05Z - dotnet-renovate-bot (@dotnet-renovate-bot) - PR: [Update container image digests (main) #137618](https://github.com/dotnet/runtime/pull/137618)
  - [Fix ReadyToRun generic parameter symbol collisions (#136191)](https://github.com/dotnet/runtime/commit/8499fe366fd12ae5d0959db53743560e6df306fb) - 2026-11-17T16:59:39Z - Jackson Schuster (@jtschuster) - PR: [Fix ReadyToRun generic parameter symbol collisions #136191](https://github.com/dotnet/runtime/pull/136191)
  - [JIT: fix profile weights when folding switches with self-edges (#137702)](https://github.com/dotnet/runtime/commit/ad132e1436f16300f6e9addb10f0db0c73f87ec6) - 2026-11-17T16:07:03Z - Andy Ayers (@AndyAyersMS) - PR: [JIT: fix profile weights when folding switches with self-edges #137702](https://github.com/dotnet/runtime/pull/137702)

- **dotnet/eShop** (`main`) - **20** commit(s)
  - [Bump CommunityToolkit.Aspire.OllamaSharp from 13.1.1 to 13.6.1 (#1101)](https://github.com/dotnet/eShop/commit/c7e9c5d1d289992125496543768b2ab1a34039a1) - 2026-11-17T15:27:34Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump CommunityToolkit.Aspire.OllamaSharp from 13.1.1 to 13.6.1 #1101](https://github.com/dotnet/eShop/pull/1101)
  - [Bump CommunityToolkit.Aspire.Hosting.Ollama from 13.1.1 to 13.6.1 (#1…](https://github.com/dotnet/eShop/commit/5e526931f74a61243c314ceb9978bdacb80cb92a) - 2026-11-17T01:50:36Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump CommunityToolkit.Aspire.Hosting.Ollama from 13.1.1 to 13.6.1 #1100](https://github.com/dotnet/eShop/pull/1100)
  - [Bump FluentValidation and FluentValidation.DependencyInjectionExtensi…](https://github.com/dotnet/eShop/commit/844b2fbf0e4ba487e9a31f51a66a73acf0210375) - 2026-11-17T01:50:29Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump FluentValidation and FluentValidation.DependencyInjectionExtensions #1104](https://github.com/dotnet/eShop/pull/1104)
  - [Bump NSubstitute from 5.3.0 to 6.2.0 (#1110)](https://github.com/dotnet/eShop/commit/ddfe83235178b5cd10cdef9001749d838b5eb4f0) - 2026-11-17T01:50:22Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump NSubstitute from 5.3.0 to 6.2.0 #1110](https://github.com/dotnet/eShop/pull/1110)
  - [Bump Microsoft.OpenApi from 3.11.0 to 3.11.1 (#1109)](https://github.com/dotnet/eShop/commit/8b9d6ba87ab39174fbf31fc2f387b5f1f76ff66d) - 2026-11-17T01:50:15Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.OpenApi from 3.11.0 to 3.11.1 #1109](https://github.com/dotnet/eShop/pull/1109)

- **dotnet/efcore** (`main`) - **18** commit(s)
  - [Validate the Cosmos session token management mode (#39658)](https://github.com/dotnet/efcore/commit/35452b56ad565a44f2d9b2441629da87c46be16c) - 2026-11-17T21:31:31Z - İlker amca (@ilkertskn) - PR: [Validate the Cosmos session token management mode #39658](https://github.com/dotnet/efcore/pull/39658)
  - [Throw ObjectDisposedException from SqliteBlob.Write(ReadOnlySpan<byte…](https://github.com/dotnet/efcore/commit/a6d73b6455284203872f8d8b1c00000b7be7ec1b) - 2026-11-17T21:29:37Z - İlker amca (@ilkertskn) - PR: [Throw ObjectDisposedException from SqliteBlob.Write(ReadOnlySpan<byte>) #39656](https://github.com/dotnet/efcore/pull/39656)
  - [Don't turn a sub-second TimeSpan command timeout into no timeout (#39…](https://github.com/dotnet/efcore/commit/928ef741b136e27584e17bdf18ec148a0755c981) - 2026-11-17T21:28:45Z - İlker amca (@ilkertskn) - PR: [Don't turn a sub-second TimeSpan command timeout into no timeout #39655](https://github.com/dotnet/efcore/pull/39655)
  - [Validate enum values parsed from numeric strings in SqliteConnectionS…](https://github.com/dotnet/efcore/commit/5bfb0ba65494a13765b950da9219bd8268dedde1) - 2026-11-17T06:10:39Z - İlker amca (@ilkertskn) - PR: [Validate enum values parsed from numeric strings in SqliteConnectionStringBuilder #39654](https://github.com/dotnet/efcore/pull/39654)
  - [Release completed migration instances (#39520)](https://github.com/dotnet/efcore/commit/32035893d6dece5a20621e99a79294da0f121599) - 2026-11-17T06:09:22Z - abdoalaa2001 (@abdoalaa2001) - PR: [Release completed migration instances #39520](https://github.com/dotnet/efcore/pull/39520)

- **dotnet/roslyn** (`main`) - **6** commit(s)
  - [Fix repository name in formatting documentation (#86508)](https://github.com/dotnet/roslyn/commit/9fada946b343d8f37cc1d46d442347c0be238c90) - 2026-11-17T20:49:25Z - David Wengier (@davidwengier) - PR: [Fix repository name in formatting documentation #86508](https://github.com/dotnet/roslyn/pull/86508)
  - [Report CS4007 for restricted types used across await with runtime asy…](https://github.com/dotnet/roslyn/commit/a18a95a7ddfe5c430a7be6dfb190de81e63f2602) - 2026-11-17T19:11:31Z - Asuka (@akasakariko) - PR: [Report CS4007 for restricted types used across await with runtime async #86486](https://github.com/dotnet/roslyn/pull/86486)
  - [Fix repository name in formatting documentation](https://github.com/dotnet/roslyn/commit/c473c1f52b40af7cb2a195e3339159b6b8c92a62) - 2026-11-17T01:45:21Z - David Wengier (@davidwengier) - PR: [Fix repository name in formatting documentation #86508](https://github.com/dotnet/roslyn/pull/86508)
  - [Fall back to net472 VBCSCompiler when purging the Roslyn output cache…](https://github.com/dotnet/roslyn/commit/644d0017f81d1d225d4a9b44171b2bcc6bcfb7cc) - 2026-11-16T22:56:53Z - Fred Silberberg (@333fred) - PR: [Fall back to net472 VBCSCompiler when purging the Roslyn output cache #86499](https://github.com/dotnet/roslyn/pull/86499)
  - [Update .NET runtime packages to 10.0.15 to address vulnerability aler…](https://github.com/dotnet/roslyn/commit/7ed489d01341de57d2d9785483f3a7f78ffb93df) - 2026-11-16T22:51:57Z - Fred Silberberg (@333fred) - PR: [Update .NET runtime packages to 10.0.15 to address vulnerability alerts #86498](https://github.com/dotnet/roslyn/pull/86498)

- **dotnet/docs** (`main`) - **6** commit(s)
  - [Bump Microsoft.Extensions.Logging across 12 directories (#56916)](https://github.com/dotnet/docs/commit/2c48383647129998298d48974eae1659b2e1af25) - 2026-11-17T15:19:21Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Extensions.Logging across 12 directories #56916](https://github.com/dotnet/docs/pull/56916)
  - [Bump Microsoft.Extensions.Hosting across 78 directories (#56915)](https://github.com/dotnet/docs/commit/f543a623b7a4576ac91d55df91feab2276cff441) - 2026-11-17T15:14:10Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Extensions.Hosting across 78 directories #56915](https://github.com/dotnet/docs/pull/56915)
  - [DNIM updates for preview.2 release (#56929)](https://github.com/dotnet/docs/commit/5359a22c73a9bcdc3873b3b7004609bb2c37b8b4) - 2026-11-17T04:36:31Z - Jacques Eloff (@joeloff) - PR: [Updates for preview.2 release #56929](https://github.com/dotnet/docs/pull/56929)
  - [Bump Microsoft.Extensions.Logging.Console across 15 directories (#56920)](https://github.com/dotnet/docs/commit/c845e1f3b74ac42b57d191b1d368a7deda33a31d) - 2026-11-16T21:44:24Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Extensions.Logging.Console across 15 directories #56920](https://github.com/dotnet/docs/pull/56920)
  - [Bump Microsoft.Extensions.Diagnostics.ResourceMonitoring.Kubernetes i…](https://github.com/dotnet/docs/commit/db2d1159f800f1f28c06480ecbaab4e21af1335c) - 2026-11-16T21:44:11Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump Microsoft.Extensions.Diagnostics.ResourceMonitoring.Kubernetes in /docs/core/diagnostics/snippets/resource-monitoring-kubernetes #56921](https://github.com/dotnet/docs/pull/56921)

- **dotnet/AspNetCore.Docs** (`main`) - **3** commit(s)
  - [Update SignalR OpenTelemetry snippets (#38175)](https://github.com/dotnet/AspNetCore.Docs/commit/33a0a8d8a51f4ac99b1aeb67ffaab69519d784dd) - 2026-11-17T12:48:26Z - Martin Costello (@martincostello) - PR: [Update SignalR OpenTelemetry snippets #38175](https://github.com/dotnet/AspNetCore.Docs/pull/38175)
  - [Archive authentication docs (#38170)](https://github.com/dotnet/AspNetCore.Docs/commit/3fa2a11a52d02a0094f209ade35bd75a75cef46a) - 2026-11-16T22:35:54Z - Genevieve Warren (@gewarren) - PR: [Archive authentication docs #38170](https://github.com/dotnet/AspNetCore.Docs/pull/38170)
  - [Change workflow triggers to 'pull_request' (#38171)](https://github.com/dotnet/AspNetCore.Docs/commit/b405d8f043498175ff9eb6f445148beb0936f816) - 2026-11-16T22:35:26Z - Genevieve Warren (@gewarren) - PR: [Change workflow triggers to 'pull_request' #38171](https://github.com/dotnet/AspNetCore.Docs/pull/38171)

- **dotnet/msbuild** (`main`) - **2** commit(s)
  - [Fix custom BuildCheck registration in multi-project builds (#15555)](https://github.com/dotnet/msbuild/commit/3e68eeebdcaef39261d7d5396fd2aa76ca52edcf) - 2026-11-17T18:58:08Z - Matt Kotsenas (@MattKotsenas) - PR: [Fix custom BuildCheck registration in multi-project builds #15555](https://github.com/dotnet/msbuild/pull/15555)
  - [Fix BuildCheck registration crashes in solution and graph evaluation …](https://github.com/dotnet/msbuild/commit/b21148b779d5e8dc266805ef24e9117586ed102e) - 2026-11-17T15:48:33Z - Matt Kotsenas (@MattKotsenas) - PR: [Fix BuildCheck registration crashes in solution and graph evaluation #15576](https://github.com/dotnet/msbuild/pull/15576)

- **dotnet/docs-maui** (`main`) - **2** commit(s)
  - [AI docs (.NET 10): add Android and Windows chat, consolidate requirem…](https://github.com/dotnet/docs-maui/commit/b863cc25fd3bf7d937e18e6ed5228d6ae003840b) - 2026-11-17T14:17:23Z - Matthew Leibowitz (@mattleibow) - PR: [AI docs (.NET 10): add Android and Windows chat, consolidate requirements, trim clutter #3610](https://github.com/dotnet/docs-maui/pull/3610)
  - [Bump the github-actions group with 2 updates (#3611)](https://github.com/dotnet/docs-maui/commit/f322094e2b77d67e77578371d9a13d3bb5a46a2c) - 2026-11-17T10:07:05Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump the github-actions group with 2 updates #3611](https://github.com/dotnet/docs-maui/pull/3611)

- **dotnet/EntityFramework.Docs** (`main`) - **2** commit(s)
  - [Add ModelHub.MultiTenancy extension documentation (#5527)](https://github.com/dotnet/EntityFramework.Docs/commit/c878d86156b8619a5ca81c3a4dd6d5fc3ca998c3) - 2026-11-17T01:33:43Z - Olosunde Kehinde Ademola (@kenndudez) - PR: [Add ModelHub.MultiTenancy extension documentation #5527](https://github.com/dotnet/EntityFramework.Docs/pull/5527)
  - [Document EF Core 11 breaking change: sharing an owned instance across…](https://github.com/dotnet/EntityFramework.Docs/commit/5ac8d0f39b054bdfb243186ef054884e872e0c16) - 2026-11-17T01:32:27Z - Caner Patır (@CanerPatir) - PR: [Document EF Core 11 breaking change: sharing an owned instance across navigations now throws #5528](https://github.com/dotnet/EntityFramework.Docs/pull/5528)

- **dotnet/docs-tools** (`main`) - **1** commit(s)
  - [Bump the github-actions group with 3 updates (#818)](https://github.com/dotnet/docs-tools/commit/e549b3fb2089ae4d2d42a359d538c4f55434a21d) - 2026-11-17T20:43:20Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump the github-actions group with 3 updates #818](https://github.com/dotnet/docs-tools/pull/818)

### microsoft

- **microsoft/vscode-docs** (`main`) - **13** commit(s)
  - [new-docs: remove stale feature(agent-host-dev-containers) marker ////…](https://github.com/microsoft/vscode-docs/commit/449410e3df07db8a6a017a1a13eea9638aea755c) - 2026-11-17T12:34:36Z - VanshShah37 (@vanshshah37) - PR: [new-docs: remove stale feature(agent-host-dev-containers) marker ////older- build: add feature lifecycle validation script, unit tests, and remove stale #10669](https://github.com/microsoft/vscode-docs/pull/10669)
  - [docs: clarify hook stdout contract across subprocesses (#10679)](https://github.com/microsoft/vscode-docs/commit/25501a82c6f7b0b0b528cdca49925c6f8cdb3265) - 2026-11-17T12:33:12Z - Alok Pandey (@alok-108) - PR: [docs: clarify hook stdout contract across subprocesses #10679](https://github.com/microsoft/vscode-docs/pull/10679)
  - [Add 365 Day & Night to the recommended themes for color vision access…](https://github.com/microsoft/vscode-docs/commit/d050c4528e990ec9c3c566ca5ad7e94d86cf1926) - 2026-11-17T10:03:54Z - Mickaël Lherminez (@mickaellherminez) - PR: [Add 365 Day & Night to the recommended themes for color vision accessibility #10635](https://github.com/microsoft/vscode-docs/pull/10635)
  - [docs: document contributes.localizations contribution point (#10673)](https://github.com/microsoft/vscode-docs/commit/79a72cdc624b5530e3cfa87b37e7b7ac6a08c06a) - 2026-11-17T10:02:23Z - Alok Pandey (@alok-108) - PR: [docs: document contributes.localizations contribution point #10673](https://github.com/microsoft/vscode-docs/pull/10673)
  - [docs: fix two sentences in v1.79 release notes (#10683)](https://github.com/microsoft/vscode-docs/commit/cb6a5ca5b0f82d058396c411c4e818ddbe38dd4a) - 2026-11-17T09:57:40Z - Ultron (@Ultroncn) - PR: [Fix two sentences in v1.79 release notes #10683](https://github.com/microsoft/vscode-docs/pull/10683)

- **microsoft/playwright.dev** (`main`) - **5** commit(s)
  - [chore(deps): bump qs and express (#2192)](https://github.com/microsoft/playwright.dev/commit/450154811efd75a43753df69d92f8e6283613c41) - 2026-11-17T18:38:07Z - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump qs and express #2192](https://github.com/microsoft/playwright.dev/pull/2192)
  - [chore(deps): bump joi from 17.13.8 to 17.13.9 (#2191)](https://github.com/microsoft/playwright.dev/commit/0d957c77eb1259634d265c0b1c79260c0a7d4825) - 2026-11-16T21:33:10Z - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump joi from 17.13.8 to 17.13.9 #2191](https://github.com/microsoft/playwright.dev/pull/2191)
  - [chore(deps): bump qs from 6.15.2 to 6.15.4 (#2190)](https://github.com/microsoft/playwright.dev/commit/ac1fb9fc360fe4cfedc2473b5a8f3de84a3839da) - 2026-11-16T21:32:54Z - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump qs from 6.15.2 to 6.15.4 #2190](https://github.com/microsoft/playwright.dev/pull/2190)
  - [chore(deps): bump follow-redirects from 1.16.1 to 1.16.3 (#2189)](https://github.com/microsoft/playwright.dev/commit/4269fd16b8029b5d4c12077ab13060c3f8cce9c7) - 2026-11-16T21:31:13Z - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump follow-redirects from 1.16.1 to 1.16.3 #2189](https://github.com/microsoft/playwright.dev/pull/2189)
  - [chore(deps): bump katex and mermaid (#2188)](https://github.com/microsoft/playwright.dev/commit/d6b767011c92910b96460e8192bc2f14fe3ef5f4) - 2026-11-16T21:30:46Z - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps): bump katex and mermaid #2188](https://github.com/microsoft/playwright.dev/pull/2188)

- **microsoft/go-sqlcmd** (`main`) - **4** commit(s)
  - [deps: bump go-mssqldb to v1.12.0 (#831)](https://github.com/microsoft/go-sqlcmd/commit/44578951fa2b2ca018a337f37239a45b6d7bd991) - 2026-11-17T21:47:50Z - Saurabh Singh (@saurabh500) - PR: [deps: bump go-mssqldb to v1.12.0 #831](https://github.com/microsoft/go-sqlcmd/pull/831)
  - [deps(deps): bump github.com/klauspost/compress from 1.18.5 to 1.18.7 …](https://github.com/microsoft/go-sqlcmd/commit/0240e5cdbe0acd2baf41afed4694ec8cddb5a604) - 2026-11-17T21:38:09Z - dependabot[bot] (@dependabot[bot]) - PR: [deps(deps): bump github.com/klauspost/compress from 1.18.5 to 1.18.7 #819](https://github.com/microsoft/go-sqlcmd/pull/819)
  - [fix: avoid panic on empty arguments (#826) (#829)](https://github.com/microsoft/go-sqlcmd/commit/4dd2b53e02ea5bbc0af1939423a843ff203f0477) - 2026-11-17T21:02:48Z - Matteo Scaramuccia (@scara) - PR: [fix: avoid panic on empty arguments (#826) #829](https://github.com/microsoft/go-sqlcmd/pull/829)
  - [deps(deps): golang 1.26.11 (#820)](https://github.com/microsoft/go-sqlcmd/commit/5cd5618479557e1409abb75fb49d82e60cb07291) - 2026-11-17T19:43:24Z - Krzysztof Pudłowski (@djkormo) - PR: [deps(deps): golang 1.26.10 #820](https://github.com/microsoft/go-sqlcmd/pull/820)

- **microsoft/winget-cli** (`master`) - **4** commit(s)
  - [MCP test reliability (#6690)](https://github.com/microsoft/winget-cli/commit/c09efb87d20b7b09a692aabfd1d55233733fea5f) - 2026-11-17T19:08:33Z - JohnMcPMS (@JohnMcPMS) - PR: [MCP test reliability #6690](https://github.com/microsoft/winget-cli/pull/6690)
  - [Limit YAML alias expansion to prevent excessive memory use (#6685)](https://github.com/microsoft/winget-cli/commit/b90eaad76fd3f0ea098796fb3e33311220e629df) - 2026-11-17T03:38:23Z - AmirMS (@AmelBawa-msft) - PR: [Limit YAML alias expansion to prevent excessive memory use #6685](https://github.com/microsoft/winget-cli/pull/6685)
  - [Validate COM package objects before accessing native state (#6686)](https://github.com/microsoft/winget-cli/commit/66af7c1d13af67e99c6ab67bd7fe0302b40f85f4) - 2026-11-16T23:55:41Z - AmirMS (@AmelBawa-msft) - PR: [Validate COM package objects before accessing native state #6686](https://github.com/microsoft/winget-cli/pull/6686)
  - [Uninstall previous handling improvements (#6683)](https://github.com/microsoft/winget-cli/commit/88e3ec32a52a7e61275bbee1921cbab4491d7375) - 2026-11-16T22:35:57Z - JohnMcPMS (@JohnMcPMS) - PR: [Uninstall previous handling improvements #6683](https://github.com/microsoft/winget-cli/pull/6683)

- **microsoft/kiota-serialization-multipart-go** (`main`) - **3** commit(s)
  - [Merge pull request #153 from microsoft/release-please--branches--main…](https://github.com/microsoft/kiota-serialization-multipart-go/commit/5281dc8e7941913d3ef0ef589ad9193e147f36b6) - 2026-11-17T21:33:20Z - Gavin Barron (@gavinbarron) - PR: [chore(main): release 1.1.7 #153](https://github.com/microsoft/kiota-serialization-multipart-go/pull/153)
  - [chore(main): release 1.1.7](https://github.com/microsoft/kiota-serialization-multipart-go/commit/8f61a59deef14df429518001b58a98b723579b4b) - 2026-11-17T21:22:01Z - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(main): release 1.1.7 #153](https://github.com/microsoft/kiota-serialization-multipart-go/pull/153)
  - [Merge pull request #136 from hardikkaurani/fix/merging-writer-nil-saf…](https://github.com/microsoft/kiota-serialization-multipart-go/commit/8228900a854f11fedbd001c858ca6484bd08a3fb) - 2026-11-17T21:20:18Z - Gavin Barron (@gavinbarron) - PR: [fix(multipart): improve writer boundary validation, typed nil safety, and factory quote parsing #136](https://github.com/microsoft/kiota-serialization-multipart-go/pull/136)

- **microsoft/simplechat** (`main`) - **3** commit(s)
  - [Merge pull request #1948 from microsoft/paullizer-government-speech-main](https://github.com/microsoft/simplechat/commit/bd085068d103c8c48750235925429519a294f064) - 2026-11-17T17:33:14Z - Paul Lizer (@paullizer) - PR: [Fix Azure Government Speech routing and transcription errors (main hotfix) #1948](https://github.com/microsoft/simplechat/pull/1948)
  - [Fix Government Speech endpoint routing and errors on main](https://github.com/microsoft/simplechat/commit/7cf8fed0bc75f9a7556373e5f99919201d2a1e20) - 2026-11-17T17:26:17Z - Paul Lizer (@paullizer) - PR: [Fix Azure Government Speech routing and transcription errors (main hotfix) #1948](https://github.com/microsoft/simplechat/pull/1948)
  - [Merge pull request #1937 from microsoft/paullizer-yamcs-tls-handling](https://github.com/microsoft/simplechat/commit/273956cd8b9280743c3441654d187201ff677e09) - 2026-11-17T16:37:46Z - Paul Lizer (@paullizer) - PR: [Fix Yamcs TLS verification setting on main #1937](https://github.com/microsoft/simplechat/pull/1937)

- **microsoft/kiota** (`main`) - **3** commit(s)
  - [Improve GitHub token handling (#8603)](https://github.com/microsoft/kiota/commit/095b38163b04a465693c5f94036a48bf80a3239b) - 2026-11-16T22:04:44Z - Gavin Barron (@gavinbarron) - PR: [Improve GitHub token handling #8603](https://github.com/microsoft/kiota/pull/8603)
  - [Fix false-positive discriminator warnings for nullable responses (#8594)](https://github.com/microsoft/kiota/commit/a77f0e920f5f07ee5de2430eeed31fd7e3f521f7) - 2026-11-16T21:29:02Z - Gavin Barron (@gavinbarron) - PR: [Fix false-positive discriminator warnings for nullable responses #8594](https://github.com/microsoft/kiota/pull/8594)
  - [chore(deps-dev): bump @types/vscode from 1.144.0 to 1.145.0 in /vscod…](https://github.com/microsoft/kiota/commit/9642e58b51bd73a9e2a5cf825e943ded3cb606b4) - 2026-11-16T20:58:43Z - dependabot[bot] (@dependabot[bot]) - PR: [chore(deps-dev): bump @types/vscode from 1.144.0 to 1.145.0 in /vscode #8590](https://github.com/microsoft/kiota/pull/8590)

- **microsoft/fabriciq-thirdparty-plugins** (`main`) - **2** commit(s)
  - [Remove SVG icon from powerbi-authoring assets (#9)](https://github.com/microsoft/fabriciq-thirdparty-plugins/commit/fe98a205ed772f7ec4e9267502346c5ae13170fd) - 2026-11-17T20:57:48Z - KailashC (@KailashChoudhury) - PR: [Remove SVG icon from powerbi-authoring for directory validation #9](https://github.com/microsoft/fabriciq-thirdparty-plugins/pull/9)
  - [Add powerbi-authoring plugin (#8)](https://github.com/microsoft/fabriciq-thirdparty-plugins/commit/51dcf111e086d8133f5ea8dd296fa27caa21b9c2) - 2026-11-17T20:48:04Z - KailashC (@KailashChoudhury) - PR: [Add powerbi-authoring plugin #8](https://github.com/microsoft/fabriciq-thirdparty-plugins/pull/8)

- **microsoft/finops-toolkit** (`dev`) - **2** commit(s)
  - [docs(hubs): Add optional row-level security guide for FinOps hubs (#2…](https://github.com/microsoft/finops-toolkit/commit/606b1371fbc4de8c278698d568910c1d38ed2e27) - 2026-11-17T13:09:25Z - Keerthi Math (@keerthimath) - PR: [docs(hubs): Add optional row-level security guide for FinOps hubs #2374](https://github.com/microsoft/finops-toolkit/pull/2374)
  - [fix(docs): Correct configure-scopes anchor in v15 changelog (#2426)](https://github.com/microsoft/finops-toolkit/commit/6ad89cd25ff873794cf5dd9eb5f6daa8e23201e9) - 2026-11-17T07:03:29Z - Roland Krummenacher (@RolandKrummenacher) - PR: [fix(docs): Correct configure-scopes anchor in v15 changelog #2426](https://github.com/microsoft/finops-toolkit/pull/2426)

- **microsoft/kiota-http-guzzle-php** (`main`) - **2** commit(s)
  - [Merge pull request #153 from microsoft/release/http](https://github.com/microsoft/kiota-http-guzzle-php/commit/2ecbd4843c2d9b3b6902b946b602e76111f0ddcb) - 2026-11-17T12:07:43Z - microsoft-graph-devx-bot[bot] (@microsoft-graph-devx-bot[bot]) - PR: [Mono-repo updates for release #153](https://github.com/microsoft/kiota-http-guzzle-php/pull/153)
  - [Merge pull request #137 from microsoft/release-please--branches--main](https://github.com/microsoft/kiota-http-guzzle-php/commit/2aeaa57073427f51bac83a30dcb1af5924ade3f1) - 2026-11-17T01:44:47Z - Gavin Barron (@gavinbarron) - PR: [Mono-repo updates for release #153](https://github.com/microsoft/kiota-http-guzzle-php/pull/153)

- **microsoft/kiota-serialization-json-php** (`main`) - **2** commit(s)
  - [Merge pull request #107 from microsoft/release/serialization-json](https://github.com/microsoft/kiota-serialization-json-php/commit/4da00fc440454a29ca5917cad5e2d5ad40f2b34f) - 2026-11-17T12:07:10Z - microsoft-graph-devx-bot[bot] (@microsoft-graph-devx-bot[bot]) - PR: [Mono-repo updates for release #107](https://github.com/microsoft/kiota-serialization-json-php/pull/107)
  - [Merge pull request #137 from microsoft/release-please--branches--main](https://github.com/microsoft/kiota-serialization-json-php/commit/17ed4fae1bd9270572e6387b59e4dc24b598c44f) - 2026-11-17T01:44:47Z - Gavin Barron (@gavinbarron) - PR: [Mono-repo updates for release #107](https://github.com/microsoft/kiota-serialization-json-php/pull/107)

- **microsoft/kiota-authentication-phpleague-php** (`main`) - **2** commit(s)
  - [Merge pull request #127 from microsoft/release/authentication](https://github.com/microsoft/kiota-authentication-phpleague-php/commit/738e3288c8bd1a260ded407b9af51f5645cfcf44) - 2026-11-17T12:04:20Z - microsoft-graph-devx-bot[bot] (@microsoft-graph-devx-bot[bot]) - PR: [Mono-repo updates for release #127](https://github.com/microsoft/kiota-authentication-phpleague-php/pull/127)
  - [Merge pull request #137 from microsoft/release-please--branches--main](https://github.com/microsoft/kiota-authentication-phpleague-php/commit/9af7fa72f052e1b57eb82c8d045a7f734a47c9ce) - 2026-11-17T01:44:47Z - Gavin Barron (@gavinbarron) - PR: [Mono-repo updates for release #127](https://github.com/microsoft/kiota-authentication-phpleague-php/pull/127)

- **microsoft/kiota-serialization-form-php** (`main`) - **2** commit(s)
  - [Merge pull request #40 from microsoft/release/serialization-form](https://github.com/microsoft/kiota-serialization-form-php/commit/a477df32cb477306a70487eed546dcae3271e388) - 2026-11-17T12:03:38Z - microsoft-graph-devx-bot[bot] (@microsoft-graph-devx-bot[bot]) - PR: [Mono-repo updates for release #40](https://github.com/microsoft/kiota-serialization-form-php/pull/40)
  - [Merge pull request #137 from microsoft/release-please--branches--main](https://github.com/microsoft/kiota-serialization-form-php/commit/40dc70ad7114548ec275a11091ea51818f33feaa) - 2026-11-17T01:44:47Z - Gavin Barron (@gavinbarron) - PR: [Mono-repo updates for release #40](https://github.com/microsoft/kiota-serialization-form-php/pull/40)

- **microsoft/kiota-serialization-text-php** (`main`) - **2** commit(s)
  - [Merge pull request #86 from microsoft/release/serialization-text](https://github.com/microsoft/kiota-serialization-text-php/commit/8d42fed588574dc7383d7ea485372f5491829309) - 2026-11-17T10:58:11Z - microsoft-graph-devx-bot[bot] (@microsoft-graph-devx-bot[bot]) - PR: [Mono-repo updates for release #86](https://github.com/microsoft/kiota-serialization-text-php/pull/86)
  - [Merge pull request #137 from microsoft/release-please--branches--main](https://github.com/microsoft/kiota-serialization-text-php/commit/10ef4d6e88458bf4cb56ec200b51244df4404ffc) - 2026-11-17T01:44:47Z - Gavin Barron (@gavinbarron) - PR: [Mono-repo updates for release #86](https://github.com/microsoft/kiota-serialization-text-php/pull/86)

- **microsoft/kiota-abstractions-php** (`main`) - **2** commit(s)
  - [Merge pull request #197 from microsoft/release/abstractions](https://github.com/microsoft/kiota-abstractions-php/commit/d04e981c4fd7d1545d222a90b716985a8a630e21) - 2026-11-17T10:41:15Z - microsoft-graph-devx-bot[bot] (@microsoft-graph-devx-bot[bot]) - PR: [Mono-repo updates for release #197](https://github.com/microsoft/kiota-abstractions-php/pull/197)
  - [Merge pull request #137 from microsoft/release-please--branches--main](https://github.com/microsoft/kiota-abstractions-php/commit/bb05dd1b6eeb5299c3f7e51dd95d61392508680d) - 2026-11-17T01:44:47Z - Gavin Barron (@gavinbarron) - PR: [Mono-repo updates for release #197](https://github.com/microsoft/kiota-abstractions-php/pull/197)

- **microsoft/kiota-dotnet** (`main`) - **2** commit(s)
  - [build(deps): bump dotnet-sdk from 10.0.403 to 10.0.404 (#871)](https://github.com/microsoft/kiota-dotnet/commit/b9a5c36800b2a60442011b74a5eb9d55bf8e0f20) - 2026-11-17T10:40:28Z - dependabot[bot] (@dependabot[bot]) - PR: [build(deps): bump dotnet-sdk from 10.0.403 to 10.0.404 #871](https://github.com/microsoft/kiota-dotnet/pull/871)
  - [chore(main): release 2.2.0 (#854)](https://github.com/microsoft/kiota-dotnet/commit/a5b687bcaeb71905d864bdcee75c1e24eae206b7) - 2026-11-16T23:59:40Z - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore(main): release 2.2.0 #854](https://github.com/microsoft/kiota-dotnet/pull/854)

- **microsoft/kiota-serialization-form-go** (`main`) - **1** commit(s)
  - [Merge pull request #166 from microsoft/release-please--branches--main…](https://github.com/microsoft/kiota-serialization-form-go/commit/fc54c761f289c6d62015044cda11b2f38b1e58a9) - 2026-11-17T21:34:04Z - Gavin Barron (@gavinbarron) - PR: [chore(main): release 1.1.8 #166](https://github.com/microsoft/kiota-serialization-form-go/pull/166)

- **microsoft/kiota-abstractions-go** (`main`) - **1** commit(s)
  - [Merge pull request #316 from microsoft/release-please--branches--main…](https://github.com/microsoft/kiota-abstractions-go/commit/5f0f09d6d39629b0165c57fa5e07eb4bb8da5f85) - 2026-11-17T21:22:41Z - Gavin Barron (@gavinbarron) - PR: [chore(main): release 1.12.2 #316](https://github.com/microsoft/kiota-abstractions-go/pull/316)

- **microsoft/kiota-http-go** (`main`) - **1** commit(s)
  - [Merge pull request #310 from microsoft/release-please--branches--main…](https://github.com/microsoft/kiota-http-go/commit/26b0092e2e65efffe1a6bf6813257fdff3badd30) - 2026-11-17T21:21:44Z - Gavin Barron (@gavinbarron) - PR: [chore(main): release 1.7.0 #310](https://github.com/microsoft/kiota-http-go/pull/310)

- **microsoft/kiota-serialization-text-go** (`main`) - **1** commit(s)
  - [Merge pull request #192 from microsoft/release-please--branches--main…](https://github.com/microsoft/kiota-serialization-text-go/commit/511d76ac2e1b574785b289f7a89f9f3a6ce5b390) - 2026-11-17T21:17:30Z - Gavin Barron (@gavinbarron) - PR: [chore(main): release 1.1.8 #192](https://github.com/microsoft/kiota-serialization-text-go/pull/192)

- **microsoft/kiota-dart** (`main`) - **1** commit(s)
  - [Merge pull request #174 from microsoft/release-please--branches--main](https://github.com/microsoft/kiota-dart/commit/32fdaf411c732cdd3d28198502e4bc74d23b22d7) - 2026-11-17T12:20:27Z - Vincent Biret (@baywet) - PR: [chore: release main #174](https://github.com/microsoft/kiota-dart/pull/174)

- **microsoft/voice-agent** (`main`) - **1** commit(s)
  - [Add optional Azure Container Apps deployment for the portal (#138)](https://github.com/microsoft/voice-agent/commit/dad3d8f4c7f619825b56fef05cb651b084ac53e7) - 2026-11-17T05:22:32Z - mengyou03042 (@mengyou03042) - PR: [Add optional Azure Container Apps deployment for the portal #138](https://github.com/microsoft/voice-agent/pull/138)

- **microsoft/kiota-python** (`main`) - **1** commit(s)
  - [Merge pull request #873 from microsoft/release-please--branches--main](https://github.com/microsoft/kiota-python/commit/37b270459f391768df698142c741945365cd3191) - 2026-11-17T01:47:30Z - Gavin Barron (@gavinbarron) - PR: [chore: release main #873](https://github.com/microsoft/kiota-python/pull/873)

- **microsoft/kiota-typescript** (`main`) - **1** commit(s)
  - [chore: release main (#2226)](https://github.com/microsoft/kiota-typescript/commit/a7d13051d1f62b790deefb2ab5b94888b1c21442) - 2026-11-17T01:44:16Z - release-please-token-provider[bot] (@release-please-token-provider[bot]) - PR: [chore: release main #2226](https://github.com/microsoft/kiota-typescript/pull/2226)

- **microsoft/amplifier-module-loop-streaming** (`main`) - **1** commit(s)
  - [Expose the active registered tool call for host approval scopes (#78)](https://github.com/microsoft/amplifier-module-loop-streaming/commit/fd4d8947a4ae06e183ca3a466d5d31b4ea958a70) - 2026-11-16T22:42:44Z - Brian Krabach (@bkrabach) - PR: [Expose the active registered tool call for host approval scopes #78](https://github.com/microsoft/amplifier-module-loop-streaming/pull/78)

- **microsoft/vscode-docs-authoring** (`main`) - **1** commit(s)
  - [Merge pull request #970 from danfiedler-msft/danfiedler/pin-actions](https://github.com/microsoft/vscode-docs-authoring/commit/479bfed093624757a554b141f33051d2fde82b6d) - 2026-11-16T22:11:21Z - Jamar Warren (@jamarw) - PR: [Pin GitHub Actions to full-length commit SHAs #970](https://github.com/microsoft/vscode-docs-authoring/pull/970)

### microsoftgraph

- **microsoftgraph/msgraph-snippets-dotnet** (`main`) - **2** commit(s)
  - [Merge pull request #247 from microsoftgraph/dependabot/nuget/src/SdkC…](https://github.com/microsoftgraph/msgraph-snippets-dotnet/commit/7eb5682cfb97011448524916182a7887d4721f6f) - 2026-11-17T19:15:31Z - github-actions[bot] (@github-actions[bot]) - PR: [Bump StyleCop.Analyzers from 1.2.0-beta.556 to 1.3.180 #247](https://github.com/microsoftgraph/msgraph-snippets-dotnet/pull/247)
  - [Bump StyleCop.Analyzers from 1.2.0-beta.556 to 1.3.180](https://github.com/microsoftgraph/msgraph-snippets-dotnet/commit/c76b37882a7e3e820b6e93b129e2e9d2a9245627) - 2026-11-17T19:14:39Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump StyleCop.Analyzers from 1.2.0-beta.556 to 1.3.180 #247](https://github.com/microsoftgraph/msgraph-snippets-dotnet/pull/247)

## samples

### Azure

- **Azure/azure-dev** (`main`) - **9** commit(s)
  - [fix(provision): differentiate Azure AI Studio resources (#10803)](https://github.com/Azure/azure-dev/commit/65e89ab6096704e6b311ed1d0e201a8cae31b4b1) - 2026-11-17T21:01:25Z - Slai.life (@huong8373tt-beep) - PR: [fix(provision): differentiate Azure AI Studio resources #10803](https://github.com/Azure/azure-dev/pull/10803)
  - [Update register Microsoft Foundry 1.2.0 (#10978)](https://github.com/Azure/azure-dev/commit/7fb3ab73d3e9f931e792f70579438579e4697f89) - 2026-11-17T10:19:20Z - Hui Miao (@huimiu) - PR: [Update register Microsoft Foundry 1.2.0 #10978](https://github.com/Azure/azure-dev/pull/10978)
  - [[azure.ai.agents] Registry update for 1.2.0 (#10981)](https://github.com/Azure/azure-dev/commit/376de2c91792633e98be61fbd3e75f0167299725) - 2026-11-17T10:18:15Z - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[azure.ai.agents] Registry update for 1.2.0 #10981](https://github.com/Azure/azure-dev/pull/10981)
  - [[azure.ai.projects] Registry update for 1.1.1 (#10980)](https://github.com/Azure/azure-dev/commit/50a4d196cfc79e7a074cdc6a1bb82076068960a9) - 2026-11-17T09:52:45Z - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[azure.ai.projects] Registry update for 1.1.1 #10980](https://github.com/Azure/azure-dev/pull/10980)
  - [[azure.ai.connections] Registry update for 1.0.1 (#10979)](https://github.com/Azure/azure-dev/commit/272b82780f8ea7660b47a1df212b5df6bd14c5e9) - 2026-11-17T09:35:53Z - azure-sdk-automation[bot] (@azure-sdk-automation[bot]) - PR: [[azure.ai.connections] Registry update for 1.0.1 #10979](https://github.com/Azure/azure-dev/pull/10979)

- **Azure/terraform-ai-gateway-landing-zone** (`main`) - **3** commit(s)
  - [Merge pull request #17 from Azure/nadeemis-refactoring](https://github.com/Azure/terraform-ai-gateway-landing-zone/commit/dabecf2d147da2448b32b965e934babdac0f492f) - 2026-11-17T15:24:18Z - nadeemis (@nadeemis) - PR: [Fix APIM spec imports on StandardV2 and a semantic-cache null-stream error #17](https://github.com/Azure/terraform-ai-gateway-landing-zone/pull/17)
  - [fix(api-spec): update schema type to string for path parameters in Op…](https://github.com/Azure/terraform-ai-gateway-landing-zone/commit/0fb22acea2917dc0f6b10f850397e8ea0e9159cb) - 2026-11-17T14:54:10Z - Nadeem Ishqair (@nadeemis) - PR: [Fix APIM spec imports on StandardV2 and a semantic-cache null-stream error #17](https://github.com/Azure/terraform-ai-gateway-landing-zone/pull/17)
  - [fix(semantic-cache): update condition to handle nullable boolean for …](https://github.com/Azure/terraform-ai-gateway-landing-zone/commit/56922c16cacc6e84e85b15c10dc3e8590c29aed6) - 2026-11-17T10:46:52Z - Nadeem Ishqair (@nadeemis) - PR: [Fix APIM spec imports on StandardV2 and a semantic-cache null-stream error #17](https://github.com/Azure/terraform-ai-gateway-landing-zone/pull/17)

- **Azure/sap-edge-integration-cell-on-azure-accelerator** (`main`) - **2** commit(s)
  - [ignore updated](https://github.com/Azure/sap-edge-integration-cell-on-azure-accelerator/commit/b3dce1273e8d96da6b61a9b45b6e9ae14d77d88d) - 2026-11-17T09:02:05Z - MartinPankraz (@MartinPankraz)
  - [docs: add EIC alerting and PostgreSQL TLS monitoring guidance](https://github.com/Azure/sap-edge-integration-cell-on-azure-accelerator/commit/642f39ce73e5603eaa34ec5277addfc6f21ba0fc) - 2026-11-17T08:58:09Z - MartinPankraz (@MartinPankraz)

- **Azure/setup-azd** (`main`) - **1** commit(s)
  - [build(deps-dev): bump the minor-and-patch group with 3 updates (#645)](https://github.com/Azure/setup-azd/commit/43695fd28acfe0fd2d8aaca9fe84c03b4cea8d90) - 2026-11-17T17:33:23Z - dependabot[bot] (@dependabot[bot]) - PR: [build(deps-dev): bump the minor-and-patch group with 3 updates #645](https://github.com/Azure/setup-azd/pull/645)

- **Azure/logicapps** (`master`) - **1** commit(s)
  - [Add a private workflow bundle installer (#1579)](https://github.com/Azure/logicapps/commit/8755f2529878bbe941177e669f0f59a0be32f61f) - 2026-11-17T01:46:18Z - Rohitha Hewawasam (@rohithah) - PR: [Add a private workflow bundle installer #1579](https://github.com/Azure/logicapps/pull/1579)

- **Azure/terraform-azurerm-avm-ptn-commercial-marketplace** (`main`) - **1** commit(s)
  - [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-ptn-commercial-marketplace/commit/d3ba7c728aaf517694b2e5501f01a9b1b389c11e) - 2026-11-17T01:21:52Z - azure-verified-modules[bot] (@azure-verified-modules[bot]) - PR: [chore: run avm pre-commit [skip ci] #68](https://github.com/Azure/terraform-azurerm-avm-ptn-commercial-marketplace/pull/68)

- **Azure/terraform-azurerm-avm-ptn-aca-lza-hosting-environment** (`main`) - **1** commit(s)
  - [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-ptn-aca-lza-hosting-environment/commit/adc9603fa074a5e9b2cdfa93a6431cbde149c4bd) - 2026-11-17T01:00:17Z - azure-verified-modules[bot] (@azure-verified-modules[bot]) - PR: [chore: run avm pre-commit [skip ci] #111](https://github.com/Azure/terraform-azurerm-avm-ptn-aca-lza-hosting-environment/pull/111)

- **Azure/homebrew-azd** (`main`) - **1** commit(s)
  - [Update for azd release 1.39.0-beta.1-daily.7081913](https://github.com/Azure/homebrew-azd/commit/73b18a8376fa9d3cbb6f45201f0a0dda58f38061) - 2026-11-17T00:22:56Z - azure-sdk (@azure-sdk)

### Azure-Samples

- **Azure-Samples/Legacy-Modernization-Agents** (`main`) - **13** commit(s)
  - [Fix Docker bind setup and REKT staging visibility checks (#215)](https://github.com/Azure-Samples/Legacy-Modernization-Agents/commit/42a12d0555807067aec3d23b2409316af81f21ef) - 2026-11-17T19:43:45Z - aplusdepseudo (@aplusdepseudo) - PR: [Fix Docker bind setup and REKT staging visibility checks #215](https://github.com/Azure-Samples/Legacy-Modernization-Agents/pull/215)
  - [Keep REKT parser logs out of the terminal (#222)](https://github.com/Azure-Samples/Legacy-Modernization-Agents/commit/9b2f4fdf2b160250396cb1467d2deecbfe6d6484) - 2026-11-17T19:06:04Z - Gustav Kaleta (@gkaleta) - PR: [Keep REKT parser logs out of the terminal #222](https://github.com/Azure-Samples/Legacy-Modernization-Agents/pull/222)
  - [Fix REKT Docker bind-mount file permissions (#214)](https://github.com/Azure-Samples/Legacy-Modernization-Agents/commit/14138e7f9b1c1df9004d443ced1bd9a462bdd0ed) - 2026-11-17T19:00:47Z - aplusdepseudo (@aplusdepseudo) - PR: [Fix REKT Docker file permissions on bind mounts #214](https://github.com/Azure-Samples/Legacy-Modernization-Agents/pull/214)
  - [Recompile agentic workflows; README for the .NET tooling (#219)](https://github.com/Azure-Samples/Legacy-Modernization-Agents/commit/bb8c501eb1dbeb8756add869d292b3b24f886fce) - 2026-11-17T18:32:32Z - Gustav Kaleta (@gkaleta) - PR: [Recompile agentic workflows; README for the .NET tooling #219](https://github.com/Azure-Samples/Legacy-Modernization-Agents/pull/219)
  - [Merge pull request #218 from Azure-Samples/feat/py2net-23-evidence](https://github.com/Azure-Samples/Legacy-Modernization-Agents/commit/f4d6cf9853846dd7fcfe21707b67fed6956ecb21) - 2026-11-17T17:44:39Z - Gustav Kaleta (@gkaleta) - PR: [Replace Python tooling with .NET #218](https://github.com/Azure-Samples/Legacy-Modernization-Agents/pull/218)

- **Azure-Samples/foundry-local-model-catalog** (`main`) - **5** commit(s)
  - [Merge pull request #130 from Azure-Samples/dependabot/github_actions/…](https://github.com/Azure-Samples/foundry-local-model-catalog/commit/bde07727ccdf09025eb2b9d3ba03af3b54264568) - 2026-11-17T07:45:43Z - nitzko24 (@nitzko24) - PR: [Bump the github-actions group with 3 updates #130](https://github.com/Azure-Samples/foundry-local-model-catalog/pull/130)
  - [Limit validation job token to read-only contents](https://github.com/Azure-Samples/foundry-local-model-catalog/commit/b56840246914d5dd20b0a64f059210fb46099614) - 2026-11-17T07:43:33Z - nitzko24 (@nitzko24) - PR: [Bump the github-actions group with 3 updates #130](https://github.com/Azure-Samples/foundry-local-model-catalog/pull/130)
  - [Pin validation runner to Ubuntu 22.04 for Python 3.9 support](https://github.com/Azure-Samples/foundry-local-model-catalog/commit/f00727b70e4863635cc5a0a0415173621de4a534) - 2026-11-17T07:42:57Z - nitzko24 (@nitzko24) - PR: [Bump the github-actions group with 3 updates #130](https://github.com/Azure-Samples/foundry-local-model-catalog/pull/130)
  - [Bump the github-actions group with 3 updates](https://github.com/Azure-Samples/foundry-local-model-catalog/commit/52c609a86834f2c491d69d7635297bd99d0bdd1f) - 2026-11-17T07:16:17Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump the github-actions group with 3 updates #130](https://github.com/Azure-Samples/foundry-local-model-catalog/pull/130)
  - [Merge pull request #65 from danfiedler-msft/danfiedler/pin-actions](https://github.com/Azure-Samples/foundry-local-model-catalog/commit/44d3676539e539d62d4d150c7af1199abd6af418) - 2026-11-17T07:15:19Z - nitzko24 (@nitzko24) - PR: [Pin GitHub Actions to full-length commit SHAs #65](https://github.com/Azure-Samples/foundry-local-model-catalog/pull/65)

- **Azure-Samples/modernize-bootcamp** (`main`) - **4** commit(s)
  - [Merge pull request #103 from Azure-Samples/sojorgensen/prereqs](https://github.com/Azure-Samples/modernize-bootcamp/commit/8cd02ba6b43badf32ed839463a42241b50963869) - 2026-11-17T16:32:45Z - Sophie Jorgensen (@sophiejorgensen) - PR: [Link Lab 02 prerequisites to central table #103](https://github.com/Azure-Samples/modernize-bootcamp/pull/103)
  - [Link Lab 02 prerequisites to central table](https://github.com/Azure-Samples/modernize-bootcamp/commit/97ad64aaaefb385b81eab00d3a6968c392f793a0) - 2026-11-17T16:31:05Z - Sophie Jorgensen - PR: [Link Lab 02 prerequisites to central table #103](https://github.com/Azure-Samples/modernize-bootcamp/pull/103)
  - [Merge pull request #102 from Azure-Samples/sojorgensen/prereqs](https://github.com/Azure-Samples/modernize-bootcamp/commit/d4f941497443546267df3bce430cb057ea473266) - 2026-11-17T16:20:02Z - Sophie Jorgensen (@sophiejorgensen) - PR: [Add prerequisites table to labs README #102](https://github.com/Azure-Samples/modernize-bootcamp/pull/102)
  - [Add prerequisites table to labs README](https://github.com/Azure-Samples/modernize-bootcamp/commit/3e5d59c1ec1b57ae217eeb490091ccf8b763feff) - 2026-11-17T16:17:06Z - Sophie Jorgensen - PR: [Add prerequisites table to labs README #102](https://github.com/Azure-Samples/modernize-bootcamp/pull/102)

- **Azure-Samples/ms-identity-ciam-native-auth-android-sample** (`main`) - **3** commit(s)
  - [Merge pull request #65 from Azure-Samples/spetrescu/native-auth-v2-fi…](https://github.com/Azure-Samples/ms-identity-ciam-native-auth-android-sample/commit/e3fd561d168c5fbe3771de5670ac41b96033ecfd) - 2026-11-17T16:49:19Z - Sergei Demchenko (@antrix1989) - PR: [Restore resend for V1 strong-authentication enrollment #65](https://github.com/Azure-Samples/ms-identity-ciam-native-auth-android-sample/pull/65)
  - [fix for v1 resend](https://github.com/Azure-Samples/ms-identity-ciam-native-auth-android-sample/commit/1b4b043d5f39710bb9b02acf7c3002b988214a48) - 2026-11-17T09:11:07Z - Silviu Petrescu (@spetrescu84) - PR: [Restore resend for V1 strong-authentication enrollment #65](https://github.com/Azure-Samples/ms-identity-ciam-native-auth-android-sample/pull/65)
  - [Merge pull request #64 from Azure-Samples/spetrescu/sample-app-v2](https://github.com/Azure-Samples/ms-identity-ciam-native-auth-android-sample/commit/30840cdee74f0529943cb3aed1ea2cbee796b947) - 2026-11-17T01:35:31Z - Sergei Demchenko (@antrix1989) - PR: [Add Native Auth V2 flows and a unified sample experience #64](https://github.com/Azure-Samples/ms-identity-ciam-native-auth-android-sample/pull/64)

- **Azure-Samples/azure-sdk-for-c-swift** (`main`) - **2** commit(s)
  - [Build Linux CI in pinned swift container (#23)](https://github.com/Azure-Samples/azure-sdk-for-c-swift/commit/1f085d9c653d6cc9c42fab6cadac1f9280ecac74) - 2026-11-17T21:50:50Z - Ewerton Scaboro da Silva (@ewertons) - PR: [Build Linux CI in pinned swift container #23](https://github.com/Azure-Samples/azure-sdk-for-c-swift/pull/23)
  - [Pin GitHub Actions to full-length commit SHAs (#20)](https://github.com/Azure-Samples/azure-sdk-for-c-swift/commit/02060815092746ef90ca994f932179e61556c805) - 2026-11-17T01:03:26Z - Dan Fiedler (@danfiedler-msft) - PR: [Pin GitHub Actions to full-length commit SHAs #20](https://github.com/Azure-Samples/azure-sdk-for-c-swift/pull/20)

- **Azure-Samples/hello-azd-python** (`main`) - **2** commit(s)
  - [Merge pull request #1 from alvinashcraft/aashcraft-microsoft-github-a…](https://github.com/Azure-Samples/hello-azd-python/commit/718310f998b8af9b3b973a443443d7af487907ea) - 2026-11-17T20:33:51Z - Alvin Ashcraft (@alvinashcraft) - PR: [Pin GitHub Actions to full-length commit SHAs #1](https://github.com/Azure-Samples/hello-azd-python/pull/1)
  - [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/hello-azd-python/commit/d2abc77d00419cdf435c159511dcb7da13d60c8f) - 2026-11-17T20:20:24Z - Alvin Ashcraft (@alvinashcraft) - PR: [Pin GitHub Actions to full-length commit SHAs #1](https://github.com/Azure-Samples/hello-azd-python/pull/1)

- **Azure-Samples/flex-container-html2pdf-go** (`main`) - **2** commit(s)
  - [Merge pull request #1 from Azure-Samples/add-go-html-to-pdf-sample](https://github.com/Azure-Samples/flex-container-html2pdf-go/commit/c7ac441121be65d143b944d774514bdc66d88cf4) - 2026-11-17T16:35:59Z - Madhura Bharadwaj (@MadhuraBharadwaj-MSFT) - PR: [Add Go Flex container HTML-to-PDF sample #1](https://github.com/Azure-Samples/flex-container-html2pdf-go/pull/1)
  - [Merge main into add-go-html-to-pdf-sample](https://github.com/Azure-Samples/flex-container-html2pdf-go/commit/cdd041d6653791d3821d0e9617567ea6f51ba586) - 2026-11-17T15:49:01Z - MadhuraBharadwaj-MSFT (@MadhuraBharadwaj-MSFT) - PR: [Add Go Flex container HTML-to-PDF sample #1](https://github.com/Azure-Samples/flex-container-html2pdf-go/pull/1)

- **Azure-Samples/flex-container-html2pdf-python** (`main`) - **2** commit(s)
  - [Merge pull request #1 from Azure-Samples/add-python-html-to-pdf-sample](https://github.com/Azure-Samples/flex-container-html2pdf-python/commit/b01d50a63b6ca9eb53e55a42ce0263adf1a44360) - 2026-11-17T16:08:18Z - Madhura Bharadwaj (@MadhuraBharadwaj-MSFT) - PR: [Add Python Flex container HTML-to-PDF sample #1](https://github.com/Azure-Samples/flex-container-html2pdf-python/pull/1)
  - [Merge pull request #2 from gavin-aguiar/gaaguiar/html2pdf-byoc-valida…](https://github.com/Azure-Samples/flex-container-html2pdf-python/commit/178f826eb02328ef7bee52ddfd0b9467acc62ccc) - 2026-11-17T16:07:38Z - Madhura Bharadwaj (@MadhuraBharadwaj-MSFT) - PR: [Verify worker downloads and enable Chromium sandboxing #2](https://github.com/Azure-Samples/flex-container-html2pdf-python/pull/2)

- **Azure-Samples/functions-connectors-typescript** (`main`) - **2** commit(s)
  - [Standardize polling trigger selection and clarify deployment guidance…](https://github.com/Azure-Samples/functions-connectors-typescript/commit/3aa2fc8f1e53d71c82c97a3fc349a2a3da9d7a21) - 2026-11-17T04:51:28Z - Lily Ma (@lilyjma) - PR: [Standardize polling trigger selection and clarify deployment guidance #15](https://github.com/Azure-Samples/functions-connectors-typescript/pull/15)
  - [Make TypeScript connector samples standalone, update to 1.0.0 SDK (#14)](https://github.com/Azure-Samples/functions-connectors-typescript/commit/d84589663e84c23fc81a6c5f624256873a387726) - 2026-11-17T01:08:30Z - Manvir Kaur (@manvkaur) - PR: [Make TypeScript connector samples standalone, update to 1.0.0 SDK #14](https://github.com/Azure-Samples/functions-connectors-typescript/pull/14)

- **Azure-Samples/functions-connectors-python** (`main`) - **2** commit(s)
  - [Add DevOps, Planner, and Salesforce polling and webhook samples (#19)](https://github.com/Azure-Samples/functions-connectors-python/commit/aaa6da053c58ffed1b08eca48db50182bdefb4ef) - 2026-11-17T01:41:53Z - hallvictoria (@hallvictoria) - PR: [Add DevOps, Planner, and Salesforce polling and webhook samples #19](https://github.com/Azure-Samples/functions-connectors-python/pull/19)
  - [Make polling and webhook connector samples independent (#20)](https://github.com/Azure-Samples/functions-connectors-python/commit/0dba20a71781fd3df6c84cc9415929f1769879e7) - 2026-11-17T00:11:54Z - Manvir Kaur (@manvkaur) - PR: [Make polling and webhook connector samples independent #20](https://github.com/Azure-Samples/functions-connectors-python/pull/20)

- **Azure-Samples/azure-functions-hosted-skills-samples** (`main`) - **2** commit(s)
  - [Merge pull request #8 from Azure-Samples/hallvictoria/hosted-skill-bi…](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/commit/be06879a0eb29d02f7d3c1b94a92fa70c15d3a64) - 2026-11-16T21:17:53Z - hallvictoria (@hallvictoria) - PR: [Add Hosted Skill binding starter and supplier review samples #8](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/pull/8)
  - [docs: add Learn metadata to hosted skill binding samples](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/commit/5da2f8b1e9948067b9c424f4d8fc86ebbf7eba4d) - 2026-11-16T21:06:16Z - Victoria Hall (@hallvictoria) - PR: [Add Hosted Skill binding starter and supplier review samples #8](https://github.com/Azure-Samples/azure-functions-hosted-skills-samples/pull/8)

- **Azure-Samples/3DGS-accelerator** (`main`) - **1** commit(s)
  - [Pin GitHub Actions to full-length commit SHAs](https://github.com/Azure-Samples/3DGS-accelerator/commit/20b2288b50432dd76b037044ebd4d4a2a7d5f5ab) - 2026-11-17T21:31:32Z - Dan Fiedler (@danfiedler-msft) - PR: [Pin GitHub Actions to full-length commit SHAs #24](https://github.com/Azure-Samples/3DGS-accelerator/pull/24)

- **Azure-Samples/cognitive-services-speech-sdk** (`master`) - **1** commit(s)
  - [Bump org.json:json in /samples/java/jre/embedded-speech (#3106)](https://github.com/Azure-Samples/cognitive-services-speech-sdk/commit/15bd7453cf2a083f6fcbbcd00b0c1bd18a9dfcc4) - 2026-11-17T21:07:01Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump org.json:json from 20231013 to 20260719 in /samples/java/jre/embedded-speech #3106](https://github.com/Azure-Samples/cognitive-services-speech-sdk/pull/3106)

- **Azure-Samples/functions-connectors-net** (`main`) - **1** commit(s)
  - [Upgrade connector samples to SDK 1.0.0 (#20)](https://github.com/Azure-Samples/functions-connectors-net/commit/8e8b538347442f4723c6921fd00fd6058d2a6fe5) - 2026-11-17T17:36:32Z - Manvir Kaur (@manvkaur) - PR: [Upgrade connector samples to SDK 1.0.0 #20](https://github.com/Azure-Samples/functions-connectors-net/pull/20)

- **Azure-Samples/flex-container-html2pdf-dotnet** (`main`) - **1** commit(s)
  - [Add .NET HTML-to-PDF Flex container sample (#1)](https://github.com/Azure-Samples/flex-container-html2pdf-dotnet/commit/066e142941c40fd352d598fb45eab5fb15ea05e5) - 2026-11-17T16:38:36Z - Madhura Bharadwaj (@MadhuraBharadwaj-MSFT) - PR: [Add .NET HTML-to-PDF Flex container sample #1](https://github.com/Azure-Samples/flex-container-html2pdf-dotnet/pull/1)

- **Azure-Samples/flex-container-html2pdf-node** (`main`) - **1** commit(s)
  - [Add Node.js Flex container HTML-to-PDF sample (#1)](https://github.com/Azure-Samples/flex-container-html2pdf-node/commit/c2183f2a66b3a540fed91df5f413f0df33c184ea) - 2026-11-17T16:27:58Z - Madhura Bharadwaj (@MadhuraBharadwaj-MSFT) - PR: [Add Node.js Flex container HTML-to-PDF sample #1](https://github.com/Azure-Samples/flex-container-html2pdf-node/pull/1)

- **Azure-Samples/functions-quickstart-dotnet-azd-sql** (`main`) - **1** commit(s)
  - [Configure OpenTelemetry and SQL setup for .NET 10 (#16)](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-sql/commit/bafb6ca5c14160e94eab6aaef284b40b58136d84) - 2026-11-17T05:46:35Z - Manvir Kaur (@manvkaur) - PR: [Configure OpenTelemetry and SQL setup for .NET 10 #16](https://github.com/Azure-Samples/functions-quickstart-dotnet-azd-sql/pull/16)

- **Azure-Samples/functions-connectors** (`main`) - **1** commit(s)
  - [Remove public preview note from README (#3)](https://github.com/Azure-Samples/functions-connectors/commit/255b7732eb3dc7bd31ecaf0d0d5806ca58dcb1dc) - 2026-11-17T02:36:21Z - Manvir Kaur (@manvkaur) - PR: [Remove public preview note from README #3](https://github.com/Azure-Samples/functions-connectors/pull/3)

- **Azure-Samples/Durable-Task-Scheduler** (`main`) - **1** commit(s)
  - [Migrate four Durable Functions samples to .NET 10 and harden them (#443)](https://github.com/Azure-Samples/Durable-Task-Scheduler/commit/3dd3d4492cc73e7938df96e3fe0da155b1d5e917) - 2026-11-16T23:51:26Z - Manvir Kaur (@manvkaur) - PR: [Migrate four Durable Functions samples to .NET 10 and harden them #443](https://github.com/Azure-Samples/Durable-Task-Scheduler/pull/443)

- **Azure-Samples/azuresandbox** (`main`) - **1** commit(s)
  - [Merge pull request #1070 from Azure-Samples/vnext](https://github.com/Azure-Samples/azuresandbox/commit/4a6d812c75a4fab49c4b6e84bfb7b54a3628668a) - 2026-11-16T23:30:16Z - Roger Doherty (MSFT) (@doherty100) - PR: [Release vnext to main #1070](https://github.com/Azure-Samples/azuresandbox/pull/1070)

### aspnet

- **aspnet/AzureSignalR-samples** (`main`) - **2** commit(s)
  - [Bump fast-xml-parser in /samples/EventGridIntegration/javascript (#384)](https://github.com/aspnet/AzureSignalR-samples/commit/a1c4ccbf3638b8f38ecb7af8203804b6a2819366) - 2026-11-16T22:25:43Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump fast-xml-parser from 5.9.0 to 5.12.0 in /samples/EventGridIntegration/javascript #384](https://github.com/aspnet/AzureSignalR-samples/pull/384)
  - [Bump actions/setup-dotnet (#385)](https://github.com/aspnet/AzureSignalR-samples/commit/9b6918d0b32df1f6277669c05f88d0039e30b7bc) - 2026-11-16T22:24:02Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-dotnet from 6.0.0 to 6.1.0 in the github-actions group #385](https://github.com/aspnet/AzureSignalR-samples/pull/385)

### dotnet

- **dotnet/macios-samples** (`main`) - **1** commit(s)
  - [Fix notification sample README (#19)](https://github.com/dotnet/macios-samples/commit/7197e2812b88ecf9f12d2266b970adbb6befef91) - 2026-11-17T11:21:06Z - Rolf Bjarne Kvinge (@rolfbjarne) - PR: [Fix notification sample README #19](https://github.com/dotnet/macios-samples/pull/19)

### microsoft

- **microsoft/onnxruntime** (`main`) - **6** commit(s)
  - [Fix 4-bit quantization test with newer ml_dtypes (#34264)](https://github.com/microsoft/onnxruntime/commit/63163cb01727a5ed0c954f970f942848e860e682) - 2026-11-17T19:16:08Z - Edward Chen (@edgchen1) - PR: [Fix 4-bit quantization test with newer ml_dtypes #34264](https://github.com/microsoft/onnxruntime/pull/34264)
  - [avoid softsign unit test failure (#32222)](https://github.com/microsoft/onnxruntime/commit/0730cb518915057dd749cfaf9f44bbdd91e868f0) - 2026-11-17T17:03:24Z - Arne H Juul (@arnej27959) - PR: [avoid softsign unit test failure #32222](https://github.com/microsoft/onnxruntime/pull/32222)
  - [Enable control-flow graph patterns and guarded rewrites (#34118)](https://github.com/microsoft/onnxruntime/commit/d1ff4a4e3b32761dab64722e0da97226427b89ff) - 2026-11-17T16:24:11Z - G. Ramalingam (@gramalingam) - PR: [Enable control-flow graph patterns and guarded rewrites #34118](https://github.com/microsoft/onnxruntime/pull/34118)
  - [Use wide accumulation for FLOAT8 weight statistics (#34186)](https://github.com/microsoft/onnxruntime/commit/f1b4861a41e980c917079f825e26b57f1ae35c81) - 2026-11-17T14:37:27Z - Afloat (@Afloat16) - PR: [Use wide accumulation for FLOAT8 weight statistics #34186](https://github.com/microsoft/onnxruntime/pull/34186)
  - [Allocate Einsum's CUDA intermediates on the stream that uses them (#3…](https://github.com/microsoft/onnxruntime/commit/5e289356eff2c1c66e83696a7b119f388230d5af) - 2026-11-17T04:59:41Z - Arne H Juul (@arnej27959) - PR: [Allocate Einsum's CUDA intermediates on the stream that uses them #32354](https://github.com/microsoft/onnxruntime/pull/32354)

- **microsoft/dragon-copilot-extension-samples** (`main`) - **5** commit(s)
  - [deps(deps): Bump the codeql-action group across 1 directory with 2 up…](https://github.com/microsoft/dragon-copilot-extension-samples/commit/7bfd650b676ba96301ed43b6caf4be6db2c46c1b) - 2026-11-17T15:12:37Z - dependabot[bot] (@dependabot[bot]) - PR: [deps(deps): Bump the codeql-action group across 1 directory with 2 updates #366](https://github.com/microsoft/dragon-copilot-extension-samples/pull/366)
  - [deps(deps): Bump softprops/action-gh-release from 3.0.3 to 3.0.4 (#367)](https://github.com/microsoft/dragon-copilot-extension-samples/commit/4d7ffd62d0ece80a00ba9a3a97ae4a0955eef5cf) - 2026-11-17T14:41:24Z - dependabot[bot] (@dependabot[bot]) - PR: [deps(deps): Bump softprops/action-gh-release from 3.0.3 to 3.0.4 #367](https://github.com/microsoft/dragon-copilot-extension-samples/pull/367)
  - [deps(deps-dev): Bump ts-jest in /tools/dragon-copilot-cli (#364)](https://github.com/microsoft/dragon-copilot-extension-samples/commit/b1e9342ab2ea035f157d8c221edf3e2b19aeae28) - 2026-11-17T14:40:57Z - dependabot[bot] (@dependabot[bot]) - PR: [deps(deps-dev): Bump ts-jest from 29.4.12 to 29.4.15 in /tools/dragon-copilot-cli #364](https://github.com/microsoft/dragon-copilot-extension-samples/pull/364)
  - [deps: Bump Microsoft.AspNetCore.Authentication.JwtBearer from 9.0.20 …](https://github.com/microsoft/dragon-copilot-extension-samples/commit/35693ebc6406e347e36e652dd2e59289ef0ab178) - 2026-11-16T22:02:12Z - dependabot[bot] (@dependabot[bot]) - PR: [deps: Bump Microsoft.AspNetCore.Authentication.JwtBearer from 9.0.20 to 9.0.23 #369](https://github.com/microsoft/dragon-copilot-extension-samples/pull/369)
  - [deps(deps-dev): Bump rimraf in /tools/dragon-copilot-cli (#363)](https://github.com/microsoft/dragon-copilot-extension-samples/commit/2e7629aebcab440116e48c474e74e0b825e47821) - 2026-11-16T21:44:34Z - dependabot[bot] (@dependabot[bot]) - PR: [deps(deps-dev): Bump rimraf from 6.1.3 to 6.1.4 in /tools/dragon-copilot-cli #363](https://github.com/microsoft/dragon-copilot-extension-samples/pull/363)

- **microsoft/web-iq-samples** (`main`) - **3** commit(s)
  - [Bump body-parser from 2.3.0 to 2.4.0 in /samples/typescript/movie-cha…](https://github.com/microsoft/web-iq-samples/commit/6fbec23385d6d460eafa2da3098293152dc71cca) - 2026-11-17T21:22:25Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump body-parser from 2.3.0 to 2.4.0 in /samples/typescript/movie-chat #26](https://github.com/microsoft/web-iq-samples/pull/26)
  - [Bump shell-quote and concurrently in /samples/typescript/movie-chat (…](https://github.com/microsoft/web-iq-samples/commit/c79494f33aebc82ccff7cd73d0b28f5092d0f821) - 2026-11-17T21:21:40Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump shell-quote and concurrently in /samples/typescript/movie-chat #25](https://github.com/microsoft/web-iq-samples/pull/25)
  - [Add Movie Night TypeScript chat sample (#22)](https://github.com/microsoft/web-iq-samples/commit/2b42b032678defb20aead1ee1fa67a3eee7c842b) - 2026-11-17T21:02:33Z - Bart DeBacker (@bartdebacker-ms) - PR: [Add Movie Night TypeScript chat sample #22](https://github.com/microsoft/web-iq-samples/pull/22)

- **microsoft/AZD-for-beginners** (`main`) - **2** commit(s)
  - [Merge pull request #150 from hyoshioka0128/patch-37](https://github.com/microsoft/AZD-for-beginners/commit/2866c4771aa2773a6b2703820f90ba402402de95) - 2026-11-17T21:45:59Z - Lee Stott (@leestott) - PR: [Translate README.md to Japanese #150](https://github.com/microsoft/AZD-for-beginners/pull/150)
  - [Translate README.md to Japanese](https://github.com/microsoft/AZD-for-beginners/commit/0bd1c6f21a2d40e828a52ede00ade4ea9bb2865a) - 2026-11-17T16:03:02Z - Hiroshi Yoshioka (@hyoshioka0128) - PR: [Translate README.md to Japanese #150](https://github.com/microsoft/AZD-for-beginners/pull/150)

- **microsoft/XBOX-Godot-Sample** (`main`) - **2** commit(s)
  - [Replace initialization telemetry with no-op stubs (#218)](https://github.com/microsoft/XBOX-Godot-Sample/commit/ce0b3c7922b6cd031b966c88eff00e9e2bdcd460) - 2026-11-17T20:55:45Z - James Lenell (@jameslen-atg) - PR: [Replace initialization telemetry with no-op stubs #218](https://github.com/microsoft/XBOX-Godot-Sample/pull/218)
  - [Add Compatibility section sourced from the CI version files (#217)](https://github.com/microsoft/XBOX-Godot-Sample/commit/f5eec2ce14ad76a0f11ab7b017af94f2e48c97e9) - 2026-11-17T18:51:21Z - Zach Hooper (XBOX) (@zachhooper) - PR: [Add Compatibility section sourced from the CI version files #217](https://github.com/microsoft/XBOX-Godot-Sample/pull/217)

- **microsoft/CopilotStudioSamples** (`main`) - **2** commit(s)
  - [Pin GitHub Actions to full-length commit SHAs in sharepoint-sidepane …](https://github.com/microsoft/CopilotStudioSamples/commit/b243a7265db85df6ff608f925167edd048b278f9) - 2026-11-17T16:55:53Z - Rajeev Pentyala (@RajeevPentyala) - PR: [Pin GitHub Actions to full-length commit SHAs in sharepoint-sidepane workflow #549](https://github.com/microsoft/CopilotStudioSamples/pull/549)
  - [Pin GitHub Actions to full-length commit SHAs (#541)](https://github.com/microsoft/CopilotStudioSamples/commit/483d64a2a908167cdea60ffba302a1fceb75fdc6) - 2026-11-17T16:55:40Z - Dan Fiedler (@danfiedler-msft) - PR: [Pin GitHub Actions to full-length commit SHAs #541](https://github.com/microsoft/CopilotStudioSamples/pull/541)

- **microsoft/bobsql** (`main`) - **2** commit(s)
  - [Merge pull request #14 from microsoft/bw](https://github.com/microsoft/bobsql/commit/223f25a67bcec22343f11f41f9dbec2f165a3e96) - 2026-11-17T16:53:16Z - Bob Ward (@rgward) - PR: [new hyperscale examples #14](https://github.com/microsoft/bobsql/pull/14)
  - [new hyperscale examples](https://github.com/microsoft/bobsql/commit/122a25b6a5683d80d3f6620169ee0e7812f502a8) - 2026-11-17T16:45:55Z - Bob Ward (@rgward) - PR: [new hyperscale examples #14](https://github.com/microsoft/bobsql/pull/14)

- **microsoft/viva-insights-sample-code** (`main`) - **2** commit(s)
  - [Merge pull request #46 from martinctc/docs/causal-ai-usage-article](https://github.com/microsoft/viva-insights-sample-code/commit/71cb38f1c6ac9b8349300130f53f76088f360022) - 2026-11-17T16:01:27Z - Martin Chan (@martinctc) - PR: [feat(articles): replace causal inference series with AI usage decision guide #46](https://github.com/microsoft/viva-insights-sample-code/pull/46)
  - [docs(articles): shorten causal guide and condition scripts on function](https://github.com/microsoft/viva-insights-sample-code/commit/e129f7170f58b47336898c4ea4b6704da228775f) - 2026-11-17T12:24:40Z - Martin Chan (@martinctc) - PR: [feat(articles): replace causal inference series with AI usage decision guide #46](https://github.com/microsoft/viva-insights-sample-code/pull/46)

- **microsoft/power-pages-samples** (`main`) - **2** commit(s)
  - [Move project skills to .claude (#229)](https://github.com/microsoft/power-pages-samples/commit/2d67ab7fddc859a9255dfc6218aceb33c4a0970f) - 2026-11-17T07:11:09Z - Priyanshu Agrawal (@priyanshu92) - PR: [Move repository skills to .claude for Claude Code discovery #229](https://github.com/microsoft/power-pages-samples/pull/229)
  - [Fix vulnerable dependencies in SPA samples (#228)](https://github.com/microsoft/power-pages-samples/commit/43c4a879fb76affb70b48fb3d34b478886413c55) - 2026-11-17T06:54:06Z - Priyanshu Agrawal (@priyanshu92) - PR: [Fix vulnerable dependencies in SPA samples #228](https://github.com/microsoft/power-pages-samples/pull/228)

- **microsoft/zerotrustassessment** (`main`) - **1** commit(s)
  - [Astaykov/ztw ai updates (#1642)](https://github.com/microsoft/zerotrustassessment/commit/2353ad74c1e720067173a402635143e2a32a0f51) - 2026-11-17T16:23:18Z - Anton Staykov (@astaykov) - PR: [Astaykov/ztw ai updates #1642](https://github.com/microsoft/zerotrustassessment/pull/1642)

- **microsoft/content-processing-solution-accelerator** (`main`) - **1** commit(s)
  - [Merge pull request #732 from microsoft/dev](https://github.com/microsoft/content-processing-solution-accelerator/commit/7215849e8d2e4e3296427afbd48577abd2bb992d) - 2026-11-17T06:12:25Z - Prajwal-Microsoft (@Prajwal-Microsoft) - PR: [chore: Dev to Main #732](https://github.com/microsoft/content-processing-solution-accelerator/pull/732)

- **microsoft/agentic-applications-for-unified-data-foundation-solution-accelerator** (`main`) - **1** commit(s)
  - [Merge pull request #543 from microsoft/dev](https://github.com/microsoft/agentic-applications-for-unified-data-foundation-solution-accelerator/commit/9123ac6718d7a77f206e4f4bda83b8d8cfc73b58) - 2026-11-17T06:11:49Z - Prajwal-Microsoft (@Prajwal-Microsoft) - PR: [chore: dev to main merge #543](https://github.com/microsoft/agentic-applications-for-unified-data-foundation-solution-accelerator/pull/543)

### microsoftgraph

- **microsoftgraph/msgraph-sample-android** (`main`) - **4** commit(s)
  - [Merge pull request #140 from microsoftgraph/dependabot/github_actions…](https://github.com/microsoftgraph/msgraph-sample-android/commit/b2adb91178c3c2eaf7518075bfed53a472cab261) - 2026-11-17T18:59:37Z - github-actions[bot] (@github-actions[bot]) - PR: [Bump actions/setup-java from 6.1.0 to 6.2.0 #140](https://github.com/microsoftgraph/msgraph-sample-android/pull/140)
  - [Merge pull request #139 from microsoftgraph/dependabot/gradle/src/app…](https://github.com/microsoftgraph/msgraph-sample-android/commit/4e861e87a1d65ff3d6e0a3a8cd5ecead774a060c) - 2026-11-17T18:57:59Z - github-actions[bot] (@github-actions[bot]) - PR: [Bump com.microsoft.identity.client:msal from 8.6.0 to 8.7.0 in /src/app #139](https://github.com/microsoftgraph/msgraph-sample-android/pull/139)
  - [Bump actions/setup-java from 6.1.0 to 6.2.0](https://github.com/microsoftgraph/msgraph-sample-android/commit/72a0e89f3a17fabb4854d4309008f0d2a8d95dee) - 2026-11-17T18:52:48Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump actions/setup-java from 6.1.0 to 6.2.0 #140](https://github.com/microsoftgraph/msgraph-sample-android/pull/140)
  - [Bump com.microsoft.identity.client:msal from 8.6.0 to 8.7.0 in /src/app](https://github.com/microsoftgraph/msgraph-sample-android/commit/8e4aac31fa28736eca5eab2c26d2866ee81bb7da) - 2026-11-17T18:52:48Z - dependabot[bot] (@dependabot[bot]) - PR: [Bump com.microsoft.identity.client:msal from 8.6.0 to 8.7.0 in /src/app #139](https://github.com/microsoftgraph/msgraph-sample-android/pull/139)

## training

### Azure

- **Azure/terraform-azurerm-avm-res-devtestlab-lab** (`main`) - **1** commit(s)
  - [chore: run avm pre-commit [skip ci]](https://github.com/Azure/terraform-azurerm-avm-res-devtestlab-lab/commit/2c8814cd0aaafb1b10528a425175c533873ce6d2) - 2026-11-17T02:17:00Z - azure-verified-modules[bot] (@azure-verified-modules[bot]) - PR: [chore: run avm pre-commit [skip ci] #86](https://github.com/Azure/terraform-azurerm-avm-res-devtestlab-lab/pull/86)

### MicrosoftLearning

- **MicrosoftLearning/mslearn-mai-models** (`main`) - **1** commit(s)
  - [Updated screenshots](https://github.com/MicrosoftLearning/mslearn-mai-models/commit/0720dc3943afd1f7b8cf956de83f2f90ff06df1f) - 2026-11-17T04:40:40Z - GraemeMalcolm (@GraemeMalcolm)

### OfficeDev

- **OfficeDev/office-js-snippets** (`main`) - **2** commit(s)
  - [[Excel] (TableColumn) Add snippet showcasing identity and index (#1165)](https://github.com/OfficeDev/office-js-snippets/commit/80ec41b0c8f20263ac425c3b734b7e67bef94044) - 2026-11-17T19:00:51Z - Elizabeth Samuel (@ElizabethSamuel-MSFT) - PR: [[Excel] (TableColumn) Add snippet showcasing identity and index #1165](https://github.com/OfficeDev/office-js-snippets/pull/1165)
  - [[Excel] (Worksheet) Add getUsedRange snippet (#1164)](https://github.com/OfficeDev/office-js-snippets/commit/da270dc37f16455f8f0be39d311b27a4794b0e58) - 2026-11-17T04:39:12Z - Elizabeth Samuel (@ElizabethSamuel-MSFT) - PR: [[Excel] (Worksheet) Add getUsedRange snippet #1164](https://github.com/OfficeDev/office-js-snippets/pull/1164)

### microsoft

- **microsoft/iq-series** (`main`) - **4** commit(s)
  - [Merge pull request #109 from bartdebacker-ms/docs/web-iq-places-auto-ga](https://github.com/microsoft/iq-series/commit/67dd0e27b17d3b2c375082249f9818ba9bc62fff) - 2026-11-17T21:00:25Z - Ayca Bas (@aycabas) - PR: [Update Web IQ cookbook for GA Places and Auto, plus Commerce Private Preview #109](https://github.com/microsoft/iq-series/pull/109)
  - [docs: list Auto first in Web IQ API table](https://github.com/microsoft/iq-series/commit/9fcfcb9fbcc76f9f725560aec69cf78157c3b4d0) - 2026-11-17T20:27:51Z - Bart DeBacker (@bartdebacker-ms) - PR: [Update Web IQ cookbook for GA Places and Auto, plus Commerce Private Preview #109](https://github.com/microsoft/iq-series/pull/109)
  - [docs: add Commerce private preview cookbook examples](https://github.com/microsoft/iq-series/commit/932e1d7a087a45bd53f23ac768b28615785538d4) - 2026-11-17T20:08:45Z - Bart DeBacker (@bartdebacker-ms) - PR: [Update Web IQ cookbook for GA Places and Auto, plus Commerce Private Preview #109](https://github.com/microsoft/iq-series/pull/109)
  - [Update Web IQ cookbook for GA Places and Auto](https://github.com/microsoft/iq-series/commit/0e4343aa529291fd00193dd6e558dbba4ad3ba6f) - 2026-11-17T19:48:19Z - Bart DeBacker (@bartdebacker-ms) - PR: [Update Web IQ cookbook for GA Places and Auto, plus Commerce Private Preview #109](https://github.com/microsoft/iq-series/pull/109)

- **microsoft/forge-lab** (`main`) - **2** commit(s)
  - [Publish cookieless blog pageview analytics](https://github.com/microsoft/forge-lab/commit/82e2f79cf4d933d095e0a8cfa96585f14aa2af37) - 2026-11-17T16:02:04Z - Taesoo Kim (@tsgates)
  - [Add CVE-2026-129488 to the CVE list](https://github.com/microsoft/forge-lab/commit/83015add99efd48470cba3bf3cc531526f0d24f7) - 2026-11-17T14:58:13Z - Cen Zhang (@occia)

- **microsoft/copilot-jetbrains-workshop** (`main`) - **1** commit(s)
  - [Fix lesson steps found by testing a fresh clone end to end](https://github.com/microsoft/copilot-jetbrains-workshop/commit/e96d898c352e2318ec8a5e213abfb398baec4918) - 2026-11-17T13:02:01Z - Rory Preddy (@roryp)

