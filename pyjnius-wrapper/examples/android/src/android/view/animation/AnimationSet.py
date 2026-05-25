from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimationSet"]

class AnimationSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/AnimationSet"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Z)V", False)]
    clone = JavaMethod("()Landroid/view/animation/AnimationSet;")
    setFillAfter = JavaMethod("(Z)V")
    setFillBefore = JavaMethod("(Z)V")
    setRepeatMode = JavaMethod("(I)V")
    setStartOffset = JavaMethod("(J)V")
    setDuration = JavaMethod("(J)V")
    addAnimation = JavaMethod("(Landroid/view/animation/Animation;)V")
    setStartTime = JavaMethod("(J)V")
    getStartTime = JavaMethod("()J")
    restrictDuration = JavaMethod("(J)V")
    getDuration = JavaMethod("()J")
    computeDurationHint = JavaMethod("()J")
    getTransformation = JavaMethod("(JLandroid/view/animation/Transformation;)Z")
    scaleCurrentDuration = JavaMethod("(F)V")
    initialize = JavaMethod("(IIII)V")
    reset = JavaMethod("()V")
    getAnimations = JavaMethod("()Ljava/util/List;")
    willChangeTransformationMatrix = JavaMethod("()Z")
    willChangeBounds = JavaMethod("()Z")