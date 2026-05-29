from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TriggerEvent"]

class TriggerEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/TriggerEvent"
    sensor = JavaField("Landroid/hardware/Sensor;")
    timestamp = JavaField("J")
    values = JavaField("[F")