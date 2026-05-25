from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VisibilityPropagation"]

class VisibilityPropagation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/VisibilityPropagation"
    __javaconstructor__ = [("()V", False)]
    captureValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    getPropagationProperties = JavaMethod("()[Ljava/lang/String;")
    getViewVisibility = JavaMethod("(Landroid/transition/TransitionValues;)I")
    getViewX = JavaMethod("(Landroid/transition/TransitionValues;)I")
    getViewY = JavaMethod("(Landroid/transition/TransitionValues;)I")