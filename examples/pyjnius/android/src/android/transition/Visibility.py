from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Visibility"]

class Visibility(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/Visibility"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    MODE_IN = JavaStaticField("I")
    MODE_OUT = JavaStaticField("I")
    MATCH_ID = JavaStaticField("I")
    MATCH_INSTANCE = JavaStaticField("I")
    MATCH_ITEM_ID = JavaStaticField("I")
    MATCH_NAME = JavaStaticField("I")
    onAppear = JavaMultipleMethod([("(Landroid/view/ViewGroup;Landroid/view/View;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;", False, False), ("(Landroid/view/ViewGroup;Landroid/transition/TransitionValues;ILandroid/transition/TransitionValues;I)Landroid/animation/Animator;", False, False)])
    onDisappear = JavaMultipleMethod([("(Landroid/view/ViewGroup;Landroid/transition/TransitionValues;ILandroid/transition/TransitionValues;I)Landroid/animation/Animator;", False, False), ("(Landroid/view/ViewGroup;Landroid/view/View;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;", False, False)])
    getMode = JavaMethod("()I")
    setMode = JavaMethod("(I)V")
    isVisible = JavaMethod("(Landroid/transition/TransitionValues;)Z")
    captureEndValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    captureStartValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    createAnimator = JavaMethod("(Landroid/view/ViewGroup;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")
    getTransitionProperties = JavaMethod("()[Ljava/lang/String;")
    isTransitionRequired = JavaMethod("(Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Z")