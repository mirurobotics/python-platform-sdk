# Changelog

## 0.10.0 (2026-05-13)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/mirurobotics/python-platform-sdk/compare/v0.9.0...v0.10.0)

### Features

* **api:** upgrade to 2026-05-06.rainier-beta.3 ([2dbcc65](https://github.com/mirurobotics/python-platform-sdk/commit/2dbcc652ba6c201d997a87c6bbf9810cb8c5eabb))
* **internal/types:** support eagerly validating pydantic iterators ([1aadc67](https://github.com/mirurobotics/python-platform-sdk/commit/1aadc67a16bd634bbf368f36c28334365e50c4eb))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([b21baec](https://github.com/mirurobotics/python-platform-sdk/commit/b21baec899aae9a318d65a0acacb76f76f946c07))


### Chores

* **internal:** reformat pyproject.toml ([bd0e40e](https://github.com/mirurobotics/python-platform-sdk/commit/bd0e40e96fecdfa1a46e4cff6260aadcde3aaf0e))

## 0.9.0 (2026-04-28)

Full Changelog: [v0.8.2...v0.9.0](https://github.com/mirurobotics/python-platform-sdk/compare/v0.8.2...v0.9.0)

### Features

* **api:** manual updates ([e15b371](https://github.com/mirurobotics/python-platform-sdk/commit/e15b371d7a9a5687b9fbc60524a818c167cba97a))
* **api:** manual updates ([7c6d61a](https://github.com/mirurobotics/python-platform-sdk/commit/7c6d61aa3d231a787539fbe62138a46de725ee81))
* **api:** manual updates ([80b0c17](https://github.com/mirurobotics/python-platform-sdk/commit/80b0c172dee57b78d5d1f2e17cd1283be0dc6740))
* **api:** manual updates ([187dcb1](https://github.com/mirurobotics/python-platform-sdk/commit/187dcb1e4878640fdf1792f69151714697ae89ed))
* **api:** update to 2026-03-09.tetons ([568d158](https://github.com/mirurobotics/python-platform-sdk/commit/568d158f7af263ec6433e38bbd847643f4b77bf6))
* **api:** update to v2026-03-09.tetons-beta.2 spec ([1a97c7f](https://github.com/mirurobotics/python-platform-sdk/commit/1a97c7f1df22f5cfb6f5e4729af66630a50b3889))
* **internal:** implement indices array format for query and form serialization ([81adbec](https://github.com/mirurobotics/python-platform-sdk/commit/81adbec701adf8e2952ae8211de868dafce42732))
* support setting headers via env ([faef5b5](https://github.com/mirurobotics/python-platform-sdk/commit/faef5b50ecf9d5cdffc11468b845de8a9f3e4427))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([c9d40ca](https://github.com/mirurobotics/python-platform-sdk/commit/c9d40cac501fd18c68af97b2928200a3e99cdd59))
* **deps:** bump minimum typing-extensions version ([63f1814](https://github.com/mirurobotics/python-platform-sdk/commit/63f18147c08d24cae32665f5fd2f77de259a9900))
* ensure file data are only sent as 1 parameter ([1ac879d](https://github.com/mirurobotics/python-platform-sdk/commit/1ac879de2432f0e5ea2abbfe28f4242c4a99f792))
* pydantic model not being parsed on forward references ([5507c1c](https://github.com/mirurobotics/python-platform-sdk/commit/5507c1cc7c05c559a0f62e431005b472a7232796))
* **pydantic:** do not pass `by_alias` unless set ([3a25c23](https://github.com/mirurobotics/python-platform-sdk/commit/3a25c23ed2863ea1b9b4670e53084d4a6e295321))
* sanitize endpoint path params ([1b9b9e4](https://github.com/mirurobotics/python-platform-sdk/commit/1b9b9e4388cd49a78f128ff0c466c42442fb5d5a))
* use correct field name format for multipart file arrays ([a8915f9](https://github.com/mirurobotics/python-platform-sdk/commit/a8915f98210a0f63463467a83257e0f6c2b85381))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([954d6ab](https://github.com/mirurobotics/python-platform-sdk/commit/954d6ab91aea4648ec0f7a2cddf0e0fa4a44a73b))


### Chores

* **ci:** skip lint on metadata-only changes ([0fa2565](https://github.com/mirurobotics/python-platform-sdk/commit/0fa2565e73e4a5ff9a5a97375a541e4c858d00b1))
* **ci:** skip uploading artifacts on stainless-internal branches ([983e18f](https://github.com/mirurobotics/python-platform-sdk/commit/983e18ff19e0214adf95819a74e1fd50a3da7dae))
* **internal:** more robust bootstrap script ([81c815a](https://github.com/mirurobotics/python-platform-sdk/commit/81c815a4143a20ab796bbe18233f921f604d86f8))
* **internal:** tweak CI branches ([14940d2](https://github.com/mirurobotics/python-platform-sdk/commit/14940d2920c3866e32c17169923aafe45e4f3a9a))
* **internal:** update gitignore ([aa19164](https://github.com/mirurobotics/python-platform-sdk/commit/aa19164d96d62b5b345a740ed6260fc091637fe6))
* update example ([615100b](https://github.com/mirurobotics/python-platform-sdk/commit/615100b4fece75e73c1bdddd28d625db7590c509))
* update SDK settings ([b659dc5](https://github.com/mirurobotics/python-platform-sdk/commit/b659dc53534bf310a104987bd2ed3fefe325326e))
* update SDK settings ([5414e23](https://github.com/mirurobotics/python-platform-sdk/commit/5414e23d37776786c9366747cd909bd9851d5231))
* update SDK settings ([71e1217](https://github.com/mirurobotics/python-platform-sdk/commit/71e1217ae174784bda5e3c6052a3cdf70715b750))
* update SDK settings ([8006dd3](https://github.com/mirurobotics/python-platform-sdk/commit/8006dd38b8ce3cdaa2b66d6e8fdebf6f86d95205))
* update SDK settings ([c7d2a67](https://github.com/mirurobotics/python-platform-sdk/commit/c7d2a6715d15e3c535f1b3cc28f3fa9e01244eb4))
* update SDK settings ([60b9e0e](https://github.com/mirurobotics/python-platform-sdk/commit/60b9e0ed6f722e3569145eb5f31d726bf0ca6bc0))


### Refactors

* require miru version header in client initialization ([8e8e267](https://github.com/mirurobotics/python-platform-sdk/commit/8e8e267fe7c72da12c02b04da297bda9161055bb))

## 0.8.2 (2026-04-18)

Full Changelog: [v0.8.1...v0.8.2](https://github.com/mirurobotics/python-platform-sdk/compare/v0.8.1...v0.8.2)

### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([954d6ab](https://github.com/mirurobotics/python-platform-sdk/commit/954d6ab91aea4648ec0f7a2cddf0e0fa4a44a73b))

## 0.8.1 (2026-04-11)

Full Changelog: [v0.8.0...v0.8.1](https://github.com/mirurobotics/python-platform-sdk/compare/v0.8.0...v0.8.1)

### Bug Fixes

* ensure file data are only sent as 1 parameter ([1ac879d](https://github.com/mirurobotics/python-platform-sdk/commit/1ac879de2432f0e5ea2abbfe28f4242c4a99f792))

## 0.8.0 (2026-04-08)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/mirurobotics/python-platform-sdk/compare/v0.7.0...v0.8.0)

### Features

* **internal:** implement indices array format for query and form serialization ([81adbec](https://github.com/mirurobotics/python-platform-sdk/commit/81adbec701adf8e2952ae8211de868dafce42732))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([c9d40ca](https://github.com/mirurobotics/python-platform-sdk/commit/c9d40cac501fd18c68af97b2928200a3e99cdd59))
* **deps:** bump minimum typing-extensions version ([63f1814](https://github.com/mirurobotics/python-platform-sdk/commit/63f18147c08d24cae32665f5fd2f77de259a9900))
* **pydantic:** do not pass `by_alias` unless set ([3a25c23](https://github.com/mirurobotics/python-platform-sdk/commit/3a25c23ed2863ea1b9b4670e53084d4a6e295321))
* sanitize endpoint path params ([1b9b9e4](https://github.com/mirurobotics/python-platform-sdk/commit/1b9b9e4388cd49a78f128ff0c466c42442fb5d5a))


### Chores

* **ci:** skip lint on metadata-only changes ([0fa2565](https://github.com/mirurobotics/python-platform-sdk/commit/0fa2565e73e4a5ff9a5a97375a541e4c858d00b1))
* **internal:** tweak CI branches ([14940d2](https://github.com/mirurobotics/python-platform-sdk/commit/14940d2920c3866e32c17169923aafe45e4f3a9a))
* **internal:** update gitignore ([aa19164](https://github.com/mirurobotics/python-platform-sdk/commit/aa19164d96d62b5b345a740ed6260fc091637fe6))

## 0.7.0 (2026-03-08)

Full Changelog: [v0.7.0-beta.5...v0.7.0](https://github.com/mirurobotics/python-platform-sdk/compare/v0.7.0-beta.5...v0.7.0)

### Features

* **api:** update to 2026-03-09.tetons ([568d158](https://github.com/mirurobotics/python-platform-sdk/commit/568d158f7af263ec6433e38bbd847643f4b77bf6))


### Chores

* **ci:** skip uploading artifacts on stainless-internal branches ([983e18f](https://github.com/mirurobotics/python-platform-sdk/commit/983e18ff19e0214adf95819a74e1fd50a3da7dae))

## 0.7.0-beta.5 (2026-03-06)

Full Changelog: [v0.7.0-beta.4...v0.7.0-beta.5](https://github.com/mirurobotics/python-platform-sdk/compare/v0.7.0-beta.4...v0.7.0-beta.5)

### Features

* **api:** manual updates ([e15b371](https://github.com/mirurobotics/python-platform-sdk/commit/e15b371d7a9a5687b9fbc60524a818c167cba97a))
* **api:** update to v2026-03-09.tetons-beta.2 spec ([1a97c7f](https://github.com/mirurobotics/python-platform-sdk/commit/1a97c7f1df22f5cfb6f5e4729af66630a50b3889))

## 0.7.0-beta.4 (2026-03-05)

Full Changelog: [v0.7.0-beta.3...v0.7.0-beta.4](https://github.com/mirurobotics/python-platform-sdk/compare/v0.7.0-beta.3...v0.7.0-beta.4)

### Bug Fixes

* pydantic model not being parsed on forward references ([5507c1c](https://github.com/mirurobotics/python-platform-sdk/commit/5507c1cc7c05c559a0f62e431005b472a7232796))

## 0.7.0-beta.3 (2026-03-05)

Full Changelog: [v0.7.0-beta.2...v0.7.0-beta.3](https://github.com/mirurobotics/python-platform-sdk/compare/v0.7.0-beta.2...v0.7.0-beta.3)

### Features

* **api:** manual updates ([7c6d61a](https://github.com/mirurobotics/python-platform-sdk/commit/7c6d61aa3d231a787539fbe62138a46de725ee81))

## 0.7.0-beta.2 (2026-03-05)

Full Changelog: [v0.0.2...v0.7.0-beta.2](https://github.com/mirurobotics/python-platform-sdk/compare/v0.0.2...v0.7.0-beta.2)

### Features

* **api:** manual updates ([80b0c17](https://github.com/mirurobotics/python-platform-sdk/commit/80b0c172dee57b78d5d1f2e17cd1283be0dc6740))
* **api:** manual updates ([187dcb1](https://github.com/mirurobotics/python-platform-sdk/commit/187dcb1e4878640fdf1792f69151714697ae89ed))


### Chores

* update example ([615100b](https://github.com/mirurobotics/python-platform-sdk/commit/615100b4fece75e73c1bdddd28d625db7590c509))
* update SDK settings ([b659dc5](https://github.com/mirurobotics/python-platform-sdk/commit/b659dc53534bf310a104987bd2ed3fefe325326e))
* update SDK settings ([5414e23](https://github.com/mirurobotics/python-platform-sdk/commit/5414e23d37776786c9366747cd909bd9851d5231))
* update SDK settings ([71e1217](https://github.com/mirurobotics/python-platform-sdk/commit/71e1217ae174784bda5e3c6052a3cdf70715b750))
* update SDK settings ([8006dd3](https://github.com/mirurobotics/python-platform-sdk/commit/8006dd38b8ce3cdaa2b66d6e8fdebf6f86d95205))
* update SDK settings ([c7d2a67](https://github.com/mirurobotics/python-platform-sdk/commit/c7d2a6715d15e3c535f1b3cc28f3fa9e01244eb4))
* update SDK settings ([60b9e0e](https://github.com/mirurobotics/python-platform-sdk/commit/60b9e0ed6f722e3569145eb5f31d726bf0ca6bc0))


### Refactors

* require miru version header in client initialization ([8e8e267](https://github.com/mirurobotics/python-platform-sdk/commit/8e8e267fe7c72da12c02b04da297bda9161055bb))

## 0.0.2 (2026-03-05)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/mirurobotics/python-platform-sdk/compare/v0.0.1...v0.0.2)

### Chores

* update SDK settings ([60b9e0e](https://github.com/mirurobotics/python-platform-sdk/commit/60b9e0ed6f722e3569145eb5f31d726bf0ca6bc0))
