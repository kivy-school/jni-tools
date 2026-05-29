from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChangeBounds"]

class ChangeBounds(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/ChangeBounds"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    getTransitionProperties = JavaMethod("()[Ljava/lang/String;")
    setResizeClip = JavaMethod("(Z)V")
    getResizeClip = JavaMethod("()Z")
    setReparent = JavaMethod("(Z)V")
    captureStartValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    captureEndValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    createAnimator = JavaMethod("(Landroid/view/ViewGroup;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")