from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransitionInflater"]

class TransitionInflater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/TransitionInflater"
    from = JavaStaticMethod("(Landroid/content/Context;)Landroid/transition/TransitionInflater;")
    inflateTransitionManager = JavaMethod("(ILandroid/view/ViewGroup;)Landroid/transition/TransitionManager;")
    inflateTransition = JavaMethod("(I)Landroid/transition/Transition;")