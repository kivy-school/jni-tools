from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OrientationListener"]

class OrientationListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/OrientationListener"
    __javaconstructor__ = [("(Landroid/content/Context;I)V", False), ("(Landroid/content/Context;)V", False)]
    ORIENTATION_UNKNOWN = JavaStaticField("I")
    onOrientationChanged = JavaMethod("(I)V")
    disable = JavaMethod("()V")
    enable = JavaMethod("()V")
    onSensorChanged = JavaMethod("(I[F)V")
    onAccuracyChanged = JavaMethod("(II)V")