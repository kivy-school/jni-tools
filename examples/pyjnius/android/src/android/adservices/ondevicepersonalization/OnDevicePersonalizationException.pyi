from typing import Any, ClassVar, overload

class OnDevicePersonalizationException:
    ERROR_INFERENCE_FAILED: ClassVar[int]
    ERROR_INFERENCE_MODEL_NOT_FOUND: ClassVar[int]
    ERROR_INVALID_TRAINING_MANIFEST: ClassVar[int]
    ERROR_ISOLATED_SERVICE_FAILED: ClassVar[int]
    ERROR_ISOLATED_SERVICE_LOADING_FAILED: ClassVar[int]
    ERROR_ISOLATED_SERVICE_MANIFEST_PARSING_FAILED: ClassVar[int]
    ERROR_ISOLATED_SERVICE_TIMEOUT: ClassVar[int]
    ERROR_PERSONALIZATION_DISABLED: ClassVar[int]
    ERROR_SCHEDULE_TRAINING_FAILED: ClassVar[int]
    def getErrorCode(self) -> int: ...
