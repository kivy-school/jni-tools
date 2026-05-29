from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SensorEventListener2"]

class SensorEventListener2(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/SensorEventListener2"
    onFlushCompleted = JavaMethod("(Landroid/hardware/Sensor;)V")