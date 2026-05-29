from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SensorDirectChannel"]

class SensorDirectChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/SensorDirectChannel"
    RATE_FAST = JavaStaticField("I")
    RATE_NORMAL = JavaStaticField("I")
    RATE_STOP = JavaStaticField("I")
    RATE_VERY_FAST = JavaStaticField("I")
    TYPE_HARDWARE_BUFFER = JavaStaticField("I")
    TYPE_MEMORY_FILE = JavaStaticField("I")
    isOpen = JavaMethod("()Z")
    close = JavaMethod("()V")
    configure = JavaMethod("(Landroid/hardware/Sensor;I)I")