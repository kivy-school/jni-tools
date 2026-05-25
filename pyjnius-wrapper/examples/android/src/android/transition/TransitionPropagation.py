from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransitionPropagation"]

class TransitionPropagation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/TransitionPropagation"
    __javaconstructor__ = [("()V", False)]
    getStartDelay = JavaMethod("(Landroid/view/ViewGroup;Landroid/transition/Transition;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)J")
    captureValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    getPropagationProperties = JavaMethod("()[Ljava/lang/String;")