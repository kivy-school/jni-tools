from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Visibility"]

class Visibility(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/Visibility"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    MODE_IN = JavaStaticField("I")
    MODE_OUT = JavaStaticField("I")
    setMode = JavaMethod("(I)V")
    getMode = JavaMethod("()I")
    getTransitionProperties = JavaMethod("()[Ljava/lang/String;")
    captureStartValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    captureEndValues = JavaMethod("(Landroid/transition/TransitionValues;)V")
    isVisible = JavaMethod("(Landroid/transition/TransitionValues;)Z")
    createAnimator = JavaMethod("(Landroid/view/ViewGroup;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;")
    onAppear = JavaMultipleMethod([("(Landroid/view/ViewGroup;Landroid/transition/TransitionValues;ILandroid/transition/TransitionValues;I)Landroid/animation/Animator;", False, False), ("(Landroid/view/ViewGroup;Landroid/view/View;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;", False, False)])
    onDisappear = JavaMultipleMethod([("(Landroid/view/ViewGroup;Landroid/transition/TransitionValues;ILandroid/transition/TransitionValues;I)Landroid/animation/Animator;", False, False), ("(Landroid/view/ViewGroup;Landroid/view/View;Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Landroid/animation/Animator;", False, False)])
    isTransitionRequired = JavaMethod("(Landroid/transition/TransitionValues;Landroid/transition/TransitionValues;)Z")