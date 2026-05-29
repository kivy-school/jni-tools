from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HealthConnectException"]

class HealthConnectException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/HealthConnectException"
    ERROR_DATA_SYNC_IN_PROGRESS = JavaStaticField("I")
    ERROR_INTERNAL = JavaStaticField("I")
    ERROR_INVALID_ARGUMENT = JavaStaticField("I")
    ERROR_IO = JavaStaticField("I")
    ERROR_RATE_LIMIT_EXCEEDED = JavaStaticField("I")
    ERROR_REMOTE = JavaStaticField("I")
    ERROR_SECURITY = JavaStaticField("I")
    ERROR_UNKNOWN = JavaStaticField("I")
    ERROR_UNSUPPORTED_OPERATION = JavaStaticField("I")
    getErrorCode = JavaMethod("()I")