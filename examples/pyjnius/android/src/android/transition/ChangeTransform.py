from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChangeTransform"]

class ChangeTransform(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/ChangeTransform"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("()V", False)]
    MATCH_ID = JavaStaticField("I")
    MATCH_INSTANCE = JavaStaticField("I")
    MATCH_ITEM_ID = JavaStaticField("I")
    MATCH_NAME = JavaStaticField("I")
    setReparent = JavaMethod("(Z)V")
    getReparent = JavaMethod("()Z")
    getReparentWithOverlay = JavaMethod("()Z")
    setReparentWithOverlay = JavaMethod("(Z)V")
    captureEndValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    captureStartValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    createAnimator = JavaMethod("(Landroid/view/ViewGroup;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")
    getTransitionProperties = JavaMethod("()[Ljava/lang/String;")