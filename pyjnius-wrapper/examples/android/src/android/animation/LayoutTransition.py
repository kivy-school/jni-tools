from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LayoutTransition"]

class LayoutTransition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/LayoutTransition"
    __javaconstructor__ = [("()V", False)]
    APPEARING = JavaStaticField("I")
    CHANGE_APPEARING = JavaStaticField("I")
    CHANGE_DISAPPEARING = JavaStaticField("I")
    CHANGING = JavaStaticField("I")
    DISAPPEARING = JavaStaticField("I")
    setDuration = JavaMultipleMethod([("(J)V", False, False), ("(IJ)V", False, False)])
    enableTransitionType = JavaMethod("(I)V")
    disableTransitionType = JavaMethod("(I)V")
    isTransitionTypeEnabled = JavaMethod("(I)Z")
    setStartDelay = JavaMethod("(IJ)V")
    getStartDelay = JavaMethod("(I)J")
    getDuration = JavaMethod("(I)J")
    setStagger = JavaMethod("(IJ)V")
    getStagger = JavaMethod("(I)J")
    setInterpolator = JavaMethod("(ILandroid/animation/TimeInterpolator;)V")
    getInterpolator = JavaMethod("(I)Landroid/animation/TimeInterpolator;")
    setAnimator = JavaMethod("(ILandroid/animation/Animator;)V")
    getAnimator = JavaMethod("(I)Landroid/animation/Animator;")
    setAnimateParentHierarchy = JavaMethod("(Z)V")
    isChangingLayout = JavaMethod("()Z")
    isRunning = JavaMethod("()Z")
    addChild = JavaMethod("(Landroid/view/ViewGroup;Landroid/view/View;)V")
    showChild = JavaMultipleMethod([("(Landroid/view/ViewGroup;Landroid/view/View;)V", False, False), ("(Landroid/view/ViewGroup;Landroid/view/View;I)V", False, False)])
    removeChild = JavaMethod("(Landroid/view/ViewGroup;Landroid/view/View;)V")
    hideChild = JavaMultipleMethod([("(Landroid/view/ViewGroup;Landroid/view/View;)V", False, False), ("(Landroid/view/ViewGroup;Landroid/view/View;I)V", False, False)])
    addTransitionListener = JavaMethod("(Landroid/animation/LayoutTransition$TransitionListener;)V")
    removeTransitionListener = JavaMethod("(Landroid/animation/LayoutTransition$TransitionListener;)V")
    getTransitionListeners = JavaMethod("()Ljava/util/List;")

    class TransitionListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/LayoutTransition/TransitionListener"
        startTransition = JavaMethod("(Landroid/animation/LayoutTransition;Landroid/view/ViewGroup;Landroid/view/View;I)V")
        endTransition = JavaMethod("(Landroid/animation/LayoutTransition;Landroid/view/ViewGroup;Landroid/view/View;I)V")