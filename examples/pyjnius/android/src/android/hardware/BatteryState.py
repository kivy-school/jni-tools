from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BatteryState"]

class BatteryState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/BatteryState"
    __javaconstructor__ = [("()V", False)]
    STATUS_CHARGING = JavaStaticField("I")
    STATUS_DISCHARGING = JavaStaticField("I")
    STATUS_FULL = JavaStaticField("I")
    STATUS_NOT_CHARGING = JavaStaticField("I")
    STATUS_UNKNOWN = JavaStaticField("I")
    getStatus = JavaMethod("()I")
    getCapacity = JavaMethod("()F")
    isPresent = JavaMethod("()Z")