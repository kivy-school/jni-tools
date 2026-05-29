from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LayoutTransition"]

class LayoutTransition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/LayoutTransition"
    __javaconstructor__ = [("()V", False)]
    APPEARING = JavaStaticField("I")
    CHANGE_APPEARING = JavaStaticField("I")
    CHANGE_DISAPPEARING = JavaStaticField("I")
    CHANGING = JavaStaticField("I")
    DISAPPEARING = JavaStaticField("I")
    getAnimator = JavaMethod("(I)Landroid/animation/Animator;")
    getStagger = JavaMethod("(I)J")
    addTransitionListener = JavaMethod("(Landroid/animation/LayoutTransition$TransitionListener;)V")
    disableTransitionType = JavaMethod("(I)V")
    enableTransitionType = JavaMethod("(I)V")
    getTransitionListeners = JavaMethod("()Ljava/util/List;")
    hideChild = JavaMultipleMethod([("(Landroid/view/ViewGroup;Landroid/view/View;I)V", False, False), ("(Landroid/view/ViewGroup;Landroid/view/View;)V", False, False)])
    isChangingLayout = JavaMethod("()Z")
    isTransitionTypeEnabled = JavaMethod("(I)Z")
    removeTransitionListener = JavaMethod("(Landroid/animation/LayoutTransition$TransitionListener;)V")
    setAnimateParentHierarchy = JavaMethod("(Z)V")
    setAnimator = JavaMethod("(ILandroid/animation/Animator;)V")
    setStagger = JavaMethod("(IJ)V")
    showChild = JavaMultipleMethod([("(Landroid/view/ViewGroup;Landroid/view/View;)V", False, False), ("(Landroid/view/ViewGroup;Landroid/view/View;I)V", False, False)])
    addChild = JavaMethod("(Landroid/view/ViewGroup;Landroid/view/View;)V")
    removeChild = JavaMethod("(Landroid/view/ViewGroup;Landroid/view/View;)V")
    getDuration = JavaMethod("(I)J")
    isRunning = JavaMethod("()Z")
    getInterpolator = JavaMethod("(I)Landroid/animation/TimeInterpolator;")
    getStartDelay = JavaMethod("(I)J")
    setDuration = JavaMultipleMethod([("(J)V", False, False), ("(IJ)V", False, False)])
    setInterpolator = JavaMethod("(ILandroid/animation/TimeInterpolator;)V")
    setStartDelay = JavaMethod("(IJ)V")

    class TransitionListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/LayoutTransition$TransitionListener"
        startTransition = JavaMethod("(Landroid/animation/LayoutTransition;Landroid/view/ViewGroup;Landroid/view/View;I)V")
        endTransition = JavaMethod("(Landroid/animation/LayoutTransition;Landroid/view/ViewGroup;Landroid/view/View;I)V")