from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SensorListener"]

class SensorListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/SensorListener"
    onSensorChanged = JavaMethod("(I[F)V")
    onAccuracyChanged = JavaMethod("(II)V")