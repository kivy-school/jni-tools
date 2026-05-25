from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PidHealthStats"]

class PidHealthStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/health/PidHealthStats"
    MEASUREMENT_WAKE_NESTING_COUNT = JavaStaticField("I")
    MEASUREMENT_WAKE_START_MS = JavaStaticField("I")
    MEASUREMENT_WAKE_SUM_MS = JavaStaticField("I")