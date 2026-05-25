from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransitionManager"]

class TransitionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/TransitionManager"
    __javaconstructor__ = [("()V", False)]
    setTransition = JavaMultipleMethod([("(Landroid/transition/Scene;Landroid/transition/Transition;)V", False, False), ("(Landroid/transition/Scene;Landroid/transition/Scene;Landroid/transition/Transition;)V", False, False)])
    transitionTo = JavaMethod("(Landroid/transition/Scene;)V")
    go = JavaMultipleMethod([("(Landroid/transition/Scene;)V", True, False), ("(Landroid/transition/Scene;Landroid/transition/Transition;)V", True, False)])
    beginDelayedTransition = JavaMultipleMethod([("(Landroid/view/ViewGroup;)V", True, False), ("(Landroid/view/ViewGroup;Landroid/transition/Transition;)V", True, False)])
    endTransitions = JavaStaticMethod("(Landroid/view/ViewGroup;)V")