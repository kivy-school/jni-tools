from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OrientationEventListener"]

class OrientationEventListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/OrientationEventListener"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;I)V", False)]
    ORIENTATION_UNKNOWN = JavaStaticField("I")
    enable = JavaMethod("()V")
    disable = JavaMethod("()V")
    canDetectOrientation = JavaMethod("()Z")
    onOrientationChanged = JavaMethod("(I)V")