from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PackageHealthStats"]

class PackageHealthStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/health/PackageHealthStats"
    MEASUREMENTS_WAKEUP_ALARMS_COUNT = JavaStaticField("I")
    STATS_SERVICES = JavaStaticField("I")