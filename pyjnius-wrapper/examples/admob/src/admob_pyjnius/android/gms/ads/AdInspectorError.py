from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdInspectorError"]

class AdInspectorError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/AdInspectorError"
    __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/String;)V", False)]
    ERROR_CODE_INTERNAL_ERROR = JavaStaticField("I")
    ERROR_CODE_FAILED_TO_LOAD = JavaStaticField("I")
    ERROR_CODE_NOT_IN_TEST_MODE = JavaStaticField("I")
    ERROR_CODE_ALREADY_OPEN = JavaStaticField("I")
    getCode = JavaMethod("()I")

    class AdInspectorErrorCode(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/AdInspectorError/AdInspectorErrorCode"