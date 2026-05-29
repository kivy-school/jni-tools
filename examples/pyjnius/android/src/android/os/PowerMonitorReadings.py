from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PowerMonitorReadings"]

class PowerMonitorReadings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/PowerMonitorReadings"
    ENERGY_UNAVAILABLE = JavaStaticField("I")
    getConsumedEnergy = JavaMethod("(Landroid/os/PowerMonitor;)J")
    toString = JavaMethod("()Ljava/lang/String;")
    getTimestampMillis = JavaMethod("(Landroid/os/PowerMonitor;)J")