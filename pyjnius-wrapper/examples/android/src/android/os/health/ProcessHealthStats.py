from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProcessHealthStats"]

class ProcessHealthStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/health/ProcessHealthStats"
    MEASUREMENT_ANR_COUNT = JavaStaticField("I")
    MEASUREMENT_CRASHES_COUNT = JavaStaticField("I")
    MEASUREMENT_FOREGROUND_MS = JavaStaticField("I")
    MEASUREMENT_STARTS_COUNT = JavaStaticField("I")
    MEASUREMENT_SYSTEM_TIME_MS = JavaStaticField("I")
    MEASUREMENT_USER_TIME_MS = JavaStaticField("I")