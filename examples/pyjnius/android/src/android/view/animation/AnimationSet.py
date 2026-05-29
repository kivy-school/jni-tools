from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimationSet"]

class AnimationSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/AnimationSet"
    __javaconstructor__ = [("(Z)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    ABSOLUTE = JavaStaticField("I")
    INFINITE = JavaStaticField("I")
    RELATIVE_TO_PARENT = JavaStaticField("I")
    RELATIVE_TO_SELF = JavaStaticField("I")
    RESTART = JavaStaticField("I")
    REVERSE = JavaStaticField("I")
    START_ON_FIRST_FRAME = JavaStaticField("I")
    ZORDER_BOTTOM = JavaStaticField("I")
    ZORDER_NORMAL = JavaStaticField("I")
    ZORDER_TOP = JavaStaticField("I")
    addAnimation = JavaMethod("(Landroid/view/animation/Animation;)V")
    getAnimations = JavaMethod("()Ljava/util/List;")
    reset = JavaMethod("()V")
    initialize = JavaMethod("(IIII)V")
    computeDurationHint = JavaMethod("()J")
    getStartTime = JavaMethod("()J")
    getTransformation = JavaMethod("(JLandroid/view/animation/Transformation;)Z")
    restrictDuration = JavaMethod("(J)V")
    scaleCurrentDuration = JavaMethod("(F)V")
    setFillAfter = JavaMethod("(Z)V")
    setFillBefore = JavaMethod("(Z)V")
    setRepeatMode = JavaMethod("(I)V")
    setStartOffset = JavaMethod("(J)V")
    setStartTime = JavaMethod("(J)V")
    willChangeBounds = JavaMethod("()Z")
    willChangeTransformationMatrix = JavaMethod("()Z")
    getDuration = JavaMethod("()J")
    setDuration = JavaMethod("(J)V")