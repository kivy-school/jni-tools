from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnDevicePersonalizationException"]

class OnDevicePersonalizationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/OnDevicePersonalizationException"
    ERROR_INFERENCE_FAILED = JavaStaticField("I")
    ERROR_INFERENCE_MODEL_NOT_FOUND = JavaStaticField("I")
    ERROR_INVALID_TRAINING_MANIFEST = JavaStaticField("I")
    ERROR_ISOLATED_SERVICE_FAILED = JavaStaticField("I")
    ERROR_ISOLATED_SERVICE_LOADING_FAILED = JavaStaticField("I")
    ERROR_ISOLATED_SERVICE_MANIFEST_PARSING_FAILED = JavaStaticField("I")
    ERROR_ISOLATED_SERVICE_TIMEOUT = JavaStaticField("I")
    ERROR_PERSONALIZATION_DISABLED = JavaStaticField("I")
    ERROR_SCHEDULE_TRAINING_FAILED = JavaStaticField("I")
    getErrorCode = JavaMethod("()I")