from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransitionListenerAdapter"]

class TransitionListenerAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/TransitionListenerAdapter"
    __javaconstructor__ = [("()V", False)]
    onTransitionPause = JavaMethod("(Landroid/transition/Transition;)V")
    onTransitionEnd = JavaMethod("(Landroid/transition/Transition;)V")
    onTransitionResume = JavaMethod("(Landroid/transition/Transition;)V")
    onTransitionCancel = JavaMethod("(Landroid/transition/Transition;)V")
    onTransitionStart = JavaMethod("(Landroid/transition/Transition;)V")