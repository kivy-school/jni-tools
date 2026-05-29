from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CircularPropagation"]

class CircularPropagation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/CircularPropagation"
    __javaconstructor__ = [("()V", False)]
    setPropagationSpeed = JavaMethod("(F)V")
    getStartDelay = JavaMethod("(Landroid/view/ViewGroup;Landroid/transition/Transition;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)J")