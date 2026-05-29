from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SensorEvent"]

class SensorEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/SensorEvent"
    accuracy = JavaField("I")
    firstEventAfterDiscontinuity = JavaField("Z")
    sensor = JavaField("Landroid/hardware/Sensor;")
    timestamp = JavaField("J")
    values = JavaField("[F")