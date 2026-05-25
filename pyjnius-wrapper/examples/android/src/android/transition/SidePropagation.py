from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SidePropagation"]

class SidePropagation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/SidePropagation"
    __javaconstructor__ = [("()V", False)]
    setSide = JavaMethod("(I)V")
    setPropagationSpeed = JavaMethod("(F)V")
    getStartDelay = JavaMethod("(Landroid/view/ViewGroup;Landroid/transition/Transition;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)J")