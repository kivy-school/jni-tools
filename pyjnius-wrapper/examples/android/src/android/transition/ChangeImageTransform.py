from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChangeImageTransform"]

class ChangeImageTransform(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/ChangeImageTransform"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    captureStartValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    captureEndValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    getTransitionProperties = JavaMethod("()[Ljava/lang/String;")
    createAnimator = JavaMethod("(Landroid/view/ViewGroup;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")