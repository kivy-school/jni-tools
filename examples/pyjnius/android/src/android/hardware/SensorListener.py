from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SensorListener"]

class SensorListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/SensorListener"
    onSensorChanged = JavaMethod("(I[F)V")
    onAccuracyChanged = JavaMethod("(II)V")