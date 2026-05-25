from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SensorEventCallback"]

class SensorEventCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/SensorEventCallback"
    __javaconstructor__ = [("()V", False)]
    onSensorChanged = JavaMethod("(Landroid/hardware/SensorEvent;)V")
    onAccuracyChanged = JavaMethod("(Landroid/hardware/Sensor;I)V")
    onFlushCompleted = JavaMethod("(Landroid/hardware/Sensor;)V")
    onSensorAdditionalInfo = JavaMethod("(Landroid/hardware/SensorAdditionalInfo;)V")