from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnDevicePersonalizationException"]

class OnDevicePersonalizationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/OnDevicePersonalizationException"
    ERROR_ISOLATED_SERVICE_FAILED = JavaStaticField("I")
    ERROR_PERSONALIZATION_DISABLED = JavaStaticField("I")
    getErrorCode = JavaMethod("()I")