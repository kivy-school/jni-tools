from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Scroller"]

class Scroller(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Scroller"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/view/animation/Interpolator;Z)V", False), ("(Landroid/content/Context;Landroid/view/animation/Interpolator;)V", False), ("(Landroid/content/Context;)V", False)]
    getCurrX = JavaMethod("()I")
    getCurrY = JavaMethod("()I")
    getFinalX = JavaMethod("()I")
    getFinalY = JavaMethod("()I")
    getStartX = JavaMethod("()I")
    getStartY = JavaMethod("()I")
    isFinished = JavaMethod("()Z")
    computeScrollOffset = JavaMethod("()Z")
    fling = JavaMethod("(IIIIIIII)V")
    timePassed = JavaMethod("()I")
    abortAnimation = JavaMethod("()V")
    setFinalX = JavaMethod("(I)V")
    setFinalY = JavaMethod("(I)V")
    setFriction = JavaMethod("(F)V")
    startScroll = JavaMultipleMethod([("(IIII)V", False, False), ("(IIIII)V", False, False)])
    forceFinished = JavaMethod("(Z)V")
    getCurrVelocity = JavaMethod("()F")
    extendDuration = JavaMethod("(I)V")
    getDuration = JavaMethod("()I")