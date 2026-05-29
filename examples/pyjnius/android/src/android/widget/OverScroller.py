from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OverScroller"]

class OverScroller(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/OverScroller"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/view/animation/Interpolator;FFZ)V", False), ("(Landroid/content/Context;Landroid/view/animation/Interpolator;FF)V", False), ("(Landroid/content/Context;Landroid/view/animation/Interpolator;)V", False), ("(Landroid/content/Context;)V", False)]
    getCurrX = JavaMethod("()I")
    getCurrY = JavaMethod("()I")
    getFinalX = JavaMethod("()I")
    getFinalY = JavaMethod("()I")
    getStartX = JavaMethod("()I")
    getStartY = JavaMethod("()I")
    isFinished = JavaMethod("()Z")
    computeScrollOffset = JavaMethod("()Z")
    fling = JavaMultipleMethod([("(IIIIIIIIII)V", False, False), ("(IIIIIIII)V", False, False)])
    abortAnimation = JavaMethod("()V")
    setFriction = JavaMethod("(F)V")
    startScroll = JavaMultipleMethod([("(IIIII)V", False, False), ("(IIII)V", False, False)])
    forceFinished = JavaMethod("(Z)V")
    getCurrVelocity = JavaMethod("()F")
    isOverScrolled = JavaMethod("()Z")
    notifyHorizontalEdgeReached = JavaMethod("(III)V")
    notifyVerticalEdgeReached = JavaMethod("(III)V")
    springBack = JavaMethod("(IIIIII)Z")