from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Scroller"]

class Scroller(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Scroller"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/view/animation/Interpolator;)V", False), ("(Landroid/content/Context;Landroid/view/animation/Interpolator;Z)V", False)]
    setFriction = JavaMethod("(F)V")
    isFinished = JavaMethod("()Z")
    forceFinished = JavaMethod("(Z)V")
    getDuration = JavaMethod("()I")
    getCurrX = JavaMethod("()I")
    getCurrY = JavaMethod("()I")
    getCurrVelocity = JavaMethod("()F")
    getStartX = JavaMethod("()I")
    getStartY = JavaMethod("()I")
    getFinalX = JavaMethod("()I")
    getFinalY = JavaMethod("()I")
    computeScrollOffset = JavaMethod("()Z")
    startScroll = JavaMultipleMethod([("(IIII)V", False, False), ("(IIIII)V", False, False)])
    fling = JavaMethod("(IIIIIIII)V")
    abortAnimation = JavaMethod("()V")
    extendDuration = JavaMethod("(I)V")
    timePassed = JavaMethod("()I")
    setFinalX = JavaMethod("(I)V")
    setFinalY = JavaMethod("(I)V")