from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SensorEventCallback"]

class SensorEventCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/SensorEventCallback"
    __javaconstructor__ = [("()V", False)]
    onFlushCompleted = JavaMethod("(Landroid/hardware/Sensor;)V")
    onSensorAdditionalInfo = JavaMethod("(Landroid/hardware/SensorAdditionalInfo;)V")
    onSensorChanged = JavaMethod("(Landroid/hardware/SensorEvent;)V")
    onAccuracyChanged = JavaMethod("(Landroid/hardware/Sensor;I)V")