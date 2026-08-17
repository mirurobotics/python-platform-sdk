# Changelog

## [0.11.1](https://github.com/mirurobotics/python-platform-sdk/compare/v0.11.0...v0.11.1) (2026-08-17)


### Chores

* **stainless:** configure release-please for the platform sdk ([#252](https://github.com/mirurobotics/python-platform-sdk/issues/252)) ([0f8050d](https://github.com/mirurobotics/python-platform-sdk/commit/0f8050dc21d57d819358cb64d1ed73e209ec0f01))

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
