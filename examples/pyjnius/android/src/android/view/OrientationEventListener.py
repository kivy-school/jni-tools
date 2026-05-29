from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OrientationEventListener"]

class OrientationEventListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/OrientationEventListener"
    __javaconstructor__ = [("(Landroid/content/Context;I)V", False), ("(Landroid/content/Context;)V", False)]
    ORIENTATION_UNKNOWN = JavaStaticField("I")
    canDetectOrientation = JavaMethod("()Z")
    onOrientationChanged = JavaMethod("(I)V")
    disable = JavaMethod("()V")
    enable = JavaMethod("()V")