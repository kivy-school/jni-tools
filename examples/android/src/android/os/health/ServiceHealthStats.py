from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceHealthStats"]

class ServiceHealthStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/health/ServiceHealthStats"
    MEASUREMENT_LAUNCH_COUNT = JavaStaticField("I")
    MEASUREMENT_START_SERVICE_COUNT = JavaStaticField("I")