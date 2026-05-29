from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SensorEventListener"]

class SensorEventListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/SensorEventListener"
    onSensorChanged = JavaMethod("(Landroid/hardware/SensorEvent;)V")
    onAccuracyChanged = JavaMethod("(Landroid/hardware/Sensor;I)V")