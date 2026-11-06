# Changelog

## [0.14.1](https://github.com/mirurobotics/python-platform-sdk/compare/v0.14.0...v0.14.1) (2026-11-06)


### Bug Fixes

* **platform:** send 2026-11-04.everglades as the SDK's default Miru-Version ([#453](https://github.com/mirurobotics/python-platform-sdk/issues/453)) ([9d91ff3](https://github.com/mirurobotics/python-platform-sdk/commit/9d91ff3267090b8eae9966eb86bb8bd62c86093e))

## [0.14.0](https://github.com/mirurobotics/python-platform-sdk/compare/v0.13.0...v0.14.0) (2026-11-06)


### Features

* add archived_by_id and archived_by to archived resources ([#423](https://github.com/mirurobotics/python-platform-sdk/issues/423)) ([dac772f](https://github.com/mirurobotics/python-platform-sdk/commit/dac772f59f1d58288124131d6c62033a0ee6abe0))
* **device,agent:** let device apps read their calibrations from Miru via /cloud ([#370](https://github.com/mirurobotics/python-platform-sdk/issues/370)) ([3c8f97b](https://github.com/mirurobotics/python-platform-sdk/commit/3c8f97b5bc5b47309b0a9362db9adfb40b394d59))
* **lint:** cap Device and Platform API operation and body schema descriptions at 120 characters ([#408](https://github.com/mirurobotics/python-platform-sdk/issues/408)) ([9d3a11d](https://github.com/mirurobotics/python-platform-sdk/commit/9d3a11d9dd4f44988b1d90a69a5ee46570bac916))
* **platform:** add archived and deleted list filters, and tidy descriptions ([#446](https://github.com/mirurobotics/python-platform-sdk/issues/446)) ([1efcf64](https://github.com/mirurobotics/python-platform-sdk/commit/1efcf6479582489255272ac2a74b50a797f7a257))
* **platform:** add attribution, users, archived_at and schema git commits ([#374](https://github.com/mirurobotics/python-platform-sdk/issues/374)) ([9ac6d5a](https://github.com/mirurobotics/python-platform-sdk/commit/9ac6d5addc91ae6ec0234471a87a0e34c0c8a036))
* **platform:** add read-only API key endpoints behind api_keys:read ([#428](https://github.com/mirurobotics/python-platform-sdk/issues/428)) ([8ce17e7](https://github.com/mirurobotics/python-platform-sdk/commit/8ce17e7d0b594405c22fcc30bf364932c2de3ce3))
* **platform:** add release archive, unarchive and delete endpoints ([#437](https://github.com/mirurobotics/python-platform-sdk/issues/437)) ([cd190db](https://github.com/mirurobotics/python-platform-sdk/commit/cd190db64ccf961ee2f1dd7ef130936fb539f514))
* **platform:** add type to Principal ([#431](https://github.com/mirurobotics/python-platform-sdk/issues/431)) ([5320fbe](https://github.com/mirurobotics/python-platform-sdk/commit/5320fbe7253dd458cb3e4dcd20abf35f80111227))
* **platform:** expand attribution IDs into principals ([#418](https://github.com/mirurobotics/python-platform-sdk/issues/418)) ([6fd8fd6](https://github.com/mirurobotics/python-platform-sdk/commit/6fd8fd6ea5823f0cf79ea67aaf23b39971a905ff))
* **platform:** shorten list calibrations and add deployment staged_at and staged_by ([#443](https://github.com/mirurobotics/python-platform-sdk/issues/443)) ([a4585a0](https://github.com/mirurobotics/python-platform-sdk/commit/a4585a0d12ddb2787c4eb4ddb70a07c548dda241))


### Bug Fixes

* **platform:** document the users list's name order default ([#421](https://github.com/mirurobotics/python-platform-sdk/issues/421)) ([032c5cb](https://github.com/mirurobotics/python-platform-sdk/commit/032c5cb0eaccd90fe7213aebd919f333c8032f4b))


### Refactors

* **platform:** remove the API key created_by expansion ([#433](https://github.com/mirurobotics/python-platform-sdk/issues/433)) ([2b246c4](https://github.com/mirurobotics/python-platform-sdk/commit/2b246c4a96653b1d83f3e3344ee83bd7c7303b93))
* **platform:** remove updated_by_id and the updated_by expansion ([#426](https://github.com/mirurobotics/python-platform-sdk/issues/426)) ([79d35fc](https://github.com/mirurobotics/python-platform-sdk/commit/79d35fcafe86713aa024e8972186adafaee80bb0))

## [0.13.0](https://github.com/mirurobotics/python-platform-sdk/compare/v0.12.0...v0.13.0) (2026-11-01)


### ⚠ BREAKING CHANGES

* **platform:** name calibration components, roles and aspects by slug ([#387](https://github.com/mirurobotics/python-platform-sdk/issues/387))

### Features

* **platform:** name calibration components, roles and aspects by slug ([#387](https://github.com/mirurobotics/python-platform-sdk/issues/387)) ([3aeeae1](https://github.com/mirurobotics/python-platform-sdk/commit/3aeeae1adfc86d29a685974c48c0f43271049c7e))


### Bug Fixes

* **platform:** send 2026-10-29.everglades as the SDK's default Miru-Version ([#401](https://github.com/mirurobotics/python-platform-sdk/issues/401)) ([e7e536f](https://github.com/mirurobotics/python-platform-sdk/commit/e7e536fda8f3ce2bf643fbe822f31b309ca1cb4e))


### Chores

* **sdkgen:** repin stlc-python to rebuild list models (6a8d16c) ([#389](https://github.com/mirurobotics/python-platform-sdk/issues/389)) ([ce1b249](https://github.com/mirurobotics/python-platform-sdk/commit/ce1b24904a68a8dfb68c79f22ef9faeddc5aa248))
* **sdkgen:** repin stlc-python to ship CVE-fixed SDK lockfiles ([#390](https://github.com/mirurobotics/python-platform-sdk/issues/390)) ([bb09893](https://github.com/mirurobotics/python-platform-sdk/commit/bb09893fac64d0523cfa245bb21de8632c67dc79))


### Refactors

* **external-users:** rename operators to external users ([#386](https://github.com/mirurobotics/python-platform-sdk/issues/386)) ([b70e282](https://github.com/mirurobotics/python-platform-sdk/commit/b70e282aca067f2deb698727df184c89766e5a28))

## [0.12.0](https://github.com/mirurobotics/python-platform-sdk/compare/v0.11.0...v0.12.0) (2026-10-28)


### ⚠ BREAKING CHANGES

* **deployments:** rename deployed_by to queued_by and add derived staged_by ([#316](https://github.com/mirurobotics/python-platform-sdk/issues/316))
* **frontend:** remove release migrate endpoint ([#310](https://github.com/mirurobotics/python-platform-sdk/issues/310))

### Features

* add calibration contracts to the agent, Device and frontend APIs ([#301](https://github.com/mirurobotics/python-platform-sdk/issues/301)) ([1c7cb0e](https://github.com/mirurobotics/python-platform-sdk/commit/1c7cb0e27ecdb460921bc265183c3bf9acedd71a))
* buffered calibrations in the Device API, reported_at in the agent API ([#327](https://github.com/mirurobotics/python-platform-sdk/issues/327)) ([4bae2fe](https://github.com/mirurobotics/python-platform-sdk/commit/4bae2fe1b7a66fc71f0ce100b0ae3271eaf9c11b))
* **cli:** add OAuth Device Flow (RFC 8628) auth endpoints ([#255](https://github.com/mirurobotics/python-platform-sdk/issues/255)) ([488b819](https://github.com/mirurobotics/python-platform-sdk/commit/488b8193b9787f8faa8dd5199f11caaa328f52f2))
* **configs:** add csv to InstanceFormat ([#366](https://github.com/mirurobotics/python-platform-sdk/issues/366)) ([6df3dba](https://github.com/mirurobotics/python-platform-sdk/commit/6df3dbaee5c166333ab51e48e82a457a2abd84f8))
* **configs:** Windows file rule globs and read-only os fields ([#293](https://github.com/mirurobotics/python-platform-sdk/issues/293)) ([ad439ad](https://github.com/mirurobotics/python-platform-sdk/commit/ad439adc53dc791089e8a760618b95186fb3b41c))
* **deployments:** rename deployed_by to queued_by and add derived staged_by ([#316](https://github.com/mirurobotics/python-platform-sdk/issues/316)) ([1a282ee](https://github.com/mirurobotics/python-platform-sdk/commit/1a282eea622c8670754325ff40bd20c4f915df4f))
* **device:** add agent-reported system-metadata fields ([#284](https://github.com/mirurobotics/python-platform-sdk/issues/284)) ([73aba87](https://github.com/mirurobotics/python-platform-sdk/commit/73aba8732f059fcc963c18eeee9bfc6a73f6a5eb))
* **device:** constrain device os/arch to DeviceOS/DeviceArch enums ([#289](https://github.com/mirurobotics/python-platform-sdk/issues/289)) ([f84bf90](https://github.com/mirurobotics/python-platform-sdk/commit/f84bf9041a25bb3483aafd3d0ef16906642f5146))
* **platform:** add calibrations get and list endpoints ([#378](https://github.com/mirurobotics/python-platform-sdk/issues/378)) ([1fcfc16](https://github.com/mirurobotics/python-platform-sdk/commit/1fcfc169f60d58f8ff1c7fb69d4f965a8354ff3a))
* **platform:** add components, component roles and aspects read endpoints ([#379](https://github.com/mirurobotics/python-platform-sdk/issues/379)) ([3d065ba](https://github.com/mirurobotics/python-platform-sdk/commit/3d065baa010b4d6e407f81afaedcd6b6ba0b159c))
* **releases:** add description to releases ([#371](https://github.com/mirurobotics/python-platform-sdk/issues/371)) ([3ca2e9c](https://github.com/mirurobotics/python-platform-sdk/commit/3ca2e9cbdd430fdd0da39a60268562179b48c123))


### Bug Fixes

* **platform:** send 2026-10-28.everglades as the SDK's default Miru-Version ([#384](https://github.com/mirurobotics/python-platform-sdk/issues/384)) ([cf2e771](https://github.com/mirurobotics/python-platform-sdk/commit/cf2e7718b4cf87d340a1c14ec0f60ef8bd48d1cc))


### Chores

* **sdkgen:** repin stlc-python at a7fb576, set python floor &gt;= 3.10 ([#285](https://github.com/mirurobotics/python-platform-sdk/issues/285)) ([893774a](https://github.com/mirurobotics/python-platform-sdk/commit/893774a00b7e0ca74f9e2f8ec292f7cfc80e398c))
* **sdkgen:** repin stlc-python to surgical re-lock (570bf02) ([#287](https://github.com/mirurobotics/python-platform-sdk/issues/287)) ([f0302df](https://github.com/mirurobotics/python-platform-sdk/commit/f0302df50fdf44a1585d47d33c6af212d212a511))


### Refactors

* **frontend:** remove release migrate endpoint ([#310](https://github.com/mirurobotics/python-platform-sdk/issues/310)) ([39466c3](https://github.com/mirurobotics/python-platform-sdk/commit/39466c3558c98c09ff6b58f823ea108d9acfdbd8))

## [0.11.0](https://github.com/mirurobotics/python-platform-sdk/compare/v0.10.0...v0.11.0) (2026-08-17)


### ⚠ BREAKING CHANGES

* **file-rule:** rename upload rules to file rules and split the rule body ([#212](https://github.com/mirurobotics/python-platform-sdk/issues/212))

### Features

* **buckets:** migrate GCS to B1 and add GET /buckets/setup ([#204](https://github.com/mirurobotics/python-platform-sdk/issues/204)) ([7b68f14](https://github.com/mirurobotics/python-platform-sdk/commit/7b68f14af7d62cd70be993143c754b9c2397bf62))
* **cli:** add POST /config_schemas/validate dry-run endpoint ([#242](https://github.com/mirurobotics/python-platform-sdk/issues/242)) ([569985d](https://github.com/mirurobotics/python-platform-sdk/commit/569985d9d16a1554222c0c1f0a5918e686c0676f))
* **configs:** add instance slots to config schemas ([#214](https://github.com/mirurobotics/python-platform-sdk/issues/214)) ([dc4ef82](https://github.com/mirurobotics/python-platform-sdk/commit/dc4ef829ebb12378c380fea610bd72345c4efd21))
* **configs:** add schemaless to SchemaLanguage and SchemaFormat enums ([#211](https://github.com/mirurobotics/python-platform-sdk/issues/211)) ([0fd39b3](https://github.com/mirurobotics/python-platform-sdk/commit/0fd39b324a7243a32af18bce4fc1adce55dbc9fd))
* **file-rule:** rename upload rules to file rules and split the rule body ([#212](https://github.com/mirurobotics/python-platform-sdk/issues/212)) ([4d6003d](https://github.com/mirurobotics/python-platform-sdk/commit/4d6003d3f6f053e09180dcbd37e53dfa404cca92))
* **platform:** add a group write surface ([#249](https://github.com/mirurobotics/python-platform-sdk/issues/249)) ([9f1629a](https://github.com/mirurobotics/python-platform-sdk/commit/9f1629ab613077b04ae9afc37329facefba9718c))
* **platform:** add read-only groups resource ([#245](https://github.com/mirurobotics/python-platform-sdk/issues/245)) ([c9d5e3d](https://github.com/mirurobotics/python-platform-sdk/commit/c9d5e3d9c4fa699367e63dbc2f397d225efb97fa))
* **platform:** connect devices to groups ([#246](https://github.com/mirurobotics/python-platform-sdk/issues/246)) ([ca693a5](https://github.com/mirurobotics/python-platform-sdk/commit/ca693a5fc8fdd77039bf4b75545fac9f1f7b658e))
* **platform:** expose deployment lifecycle timestamps ([#248](https://github.com/mirurobotics/python-platform-sdk/issues/248)) ([6d27dee](https://github.com/mirurobotics/python-platform-sdk/commit/6d27dee0a6a01a582c9872e3a6a39baeb28e8f74))
* **platform:** expose deployment parent, drop file rules and group ancestors ([#247](https://github.com/mirurobotics/python-platform-sdk/issues/247)) ([e48cc60](https://github.com/mirurobotics/python-platform-sdk/commit/e48cc6090178231b5e81261747232c3326c06d2e))


### Bug Fixes

* **config-schemas:** make instance_slots optional on create ([#237](https://github.com/mirurobotics/python-platform-sdk/issues/237)) ([356a9f0](https://github.com/mirurobotics/python-platform-sdk/commit/356a9f08ff845855422dbb125abe34c5ad3789f8))
* **configs:** drop opaque from SchemaFormat enum ([#220](https://github.com/mirurobotics/python-platform-sdk/issues/220)) ([ade48b5](https://github.com/mirurobotics/python-platform-sdk/commit/ade48b5f2500127a0cc2273f0845104d9ef92c53))
* **stlc:** make generate CI install work on Blacksmith (ssh-auth + npm cache) ([#147](https://github.com/mirurobotics/python-platform-sdk/issues/147)) ([c416f66](https://github.com/mirurobotics/python-platform-sdk/commit/c416f66d97fcdc71d3dd6a21cd5b944aa66eba66))


### Chores

* **stainless:** configure release-please for the platform sdk ([#252](https://github.com/mirurobotics/python-platform-sdk/issues/252)) ([0f8050d](https://github.com/mirurobotics/python-platform-sdk/commit/0f8050dc21d57d819358cb64d1ed73e209ec0f01))


### Refactors

* **configs:** rename instance format other value to text ([#217](https://github.com/mirurobotics/python-platform-sdk/issues/217)) ([98e06d4](https://github.com/mirurobotics/python-platform-sdk/commit/98e06d4b69bac1e659f3ccb5c4d0158001a567aa))
* **configs:** rename schemaless schema value to opaque ([#215](https://github.com/mirurobotics/python-platform-sdk/issues/215)) ([0f27f1b](https://github.com/mirurobotics/python-platform-sdk/commit/0f27f1b3af7f9b3f8fe1ad13937f5e57d5ba7780))
* **platform:** fold devices:move back into devices:write ([#250](https://github.com/mirurobotics/python-platform-sdk/issues/250)) ([bc11a9c](https://github.com/mirurobotics/python-platform-sdk/commit/bc11a9c64f5d873c3d0361abb299c23afcfbbcd6))
* **platform:** remove bulk device move ([#251](https://github.com/mirurobotics/python-platform-sdk/issues/251)) ([751d9cb](https://github.com/mirurobotics/python-platform-sdk/commit/751d9cb0cea2c6f3981b21400eca571f1eed8c35))
* **platform:** remove upload collections resource ([#244](https://github.com/mirurobotics/python-platform-sdk/issues/244)) ([5ddf516](https://github.com/mirurobotics/python-platform-sdk/commit/5ddf51620c40d2309fc52b36b8a0a96b7041c6a0))
