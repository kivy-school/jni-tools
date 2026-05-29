from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VisibilityPropagation"]

class VisibilityPropagation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/VisibilityPropagation"
    __javaconstructor__ = [("()V", False)]
    captureValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    getPropagationProperties = JavaMethod("()[Ljava/lang/String;")
    getViewY = JavaMethod("(Landroid/transition/TransitionValues;)I")
    getViewX = JavaMethod("(Landroid/transition/TransitionValues;)I")
    getViewVisibility = JavaMethod("(Landroid/transition/TransitionValues;)I")