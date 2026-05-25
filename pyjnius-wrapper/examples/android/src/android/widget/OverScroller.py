from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OverScroller"]

class OverScroller(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/OverScroller"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/view/animation/Interpolator;)V", False), ("(Landroid/content/Context;Landroid/view/animation/Interpolator;FF)V", False), ("(Landroid/content/Context;Landroid/view/animation/Interpolator;FFZ)V", False)]
    setFriction = JavaMethod("(F)V")
    isFinished = JavaMethod("()Z")
    forceFinished = JavaMethod("(Z)V")
    getCurrX = JavaMethod("()I")
    getCurrY = JavaMethod("()I")
    getCurrVelocity = JavaMethod("()F")
    getStartX = JavaMethod("()I")
    getStartY = JavaMethod("()I")
    getFinalX = JavaMethod("()I")
    getFinalY = JavaMethod("()I")
    computeScrollOffset = JavaMethod("()Z")
    startScroll = JavaMultipleMethod([("(IIII)V", False, False), ("(IIIII)V", False, False)])
    springBack = JavaMethod("(IIIIII)Z")
    fling = JavaMultipleMethod([("(IIIIIIII)V", False, False), ("(IIIIIIIIII)V", False, False)])
    notifyHorizontalEdgeReached = JavaMethod("(III)V")
    notifyVerticalEdgeReached = JavaMethod("(III)V")
    isOverScrolled = JavaMethod("()Z")
    abortAnimation = JavaMethod("()V")