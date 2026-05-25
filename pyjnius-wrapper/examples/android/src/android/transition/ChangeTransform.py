from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChangeTransform"]

class ChangeTransform(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/ChangeTransform"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    getReparentWithOverlay = JavaMethod("()Z")
    setReparentWithOverlay = JavaMethod("(Z)V")
    getReparent = JavaMethod("()Z")
    setReparent = JavaMethod("(Z)V")
    getTransitionProperties = JavaMethod("()[Ljava/lang/String;")
    captureStartValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    captureEndValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    createAnimator = JavaMethod("(Landroid/view/ViewGroup;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")