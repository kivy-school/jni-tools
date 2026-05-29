from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OrientationListener"]

class OrientationListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/OrientationListener"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;I)V", False)]
    ORIENTATION_UNKNOWN = JavaStaticField("I")
    enable = JavaMethod("()V")
    disable = JavaMethod("()V")
    onAccuracyChanged = JavaMethod("(II)V")
    onSensorChanged = JavaMethod("(I[F)V")
    onOrientationChanged = JavaMethod("(I)V")