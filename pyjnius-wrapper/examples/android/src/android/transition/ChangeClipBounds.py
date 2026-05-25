from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChangeClipBounds"]

class ChangeClipBounds(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/ChangeClipBounds"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    getTransitionProperties = JavaMethod("()[Ljava/lang/String;")
    captureStartValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    captureEndValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    createAnimator = JavaMethod("(Landroid/view/ViewGroup;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")