from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ValueAnimator"]

class ValueAnimator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/ValueAnimator"
    __javaconstructor__ = [("()V", False)]
    INFINITE = JavaStaticField("I")
    RESTART = JavaStaticField("I")
    REVERSE = JavaStaticField("I")
    getDurationScale = JavaStaticMethod("()F")
    registerDurationScaleChangeListener = JavaStaticMethod("(Landroid/animation/ValueAnimator$DurationScaleChangeListener;)Z")
    unregisterDurationScaleChangeListener = JavaStaticMethod("(Landroid/animation/ValueAnimator$DurationScaleChangeListener;)Z")
    areAnimatorsEnabled = JavaStaticMethod("()Z")
    ofInt = JavaStaticMethod("([I)Landroid/animation/ValueAnimator;", varargs=True)
    ofArgb = JavaStaticMethod("([I)Landroid/animation/ValueAnimator;", varargs=True)
    ofFloat = JavaStaticMethod("([F)Landroid/animation/ValueAnimator;", varargs=True)
    ofPropertyValuesHolder = JavaStaticMethod("([Landroid/animation/PropertyValuesHolder;)Landroid/animation/ValueAnimator;", varargs=True)
    ofObject = JavaStaticMethod("(Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ValueAnimator;", varargs=True)
    setIntValues = JavaMethod("([I)V", varargs=True)
    setFloatValues = JavaMethod("([F)V", varargs=True)
    setObjectValues = JavaMethod("([Ljava/lang/Object;)V", varargs=True)
    setValues = JavaMethod("([Landroid/animation/PropertyValuesHolder;)V", varargs=True)
    getValues = JavaMethod("()[Landroid/animation/PropertyValuesHolder;")
    setDuration = JavaMethod("(J)Landroid/animation/ValueAnimator;")
    getDuration = JavaMethod("()J")
    getTotalDuration = JavaMethod("()J")
    setCurrentPlayTime = JavaMethod("(J)V")
    setCurrentFraction = JavaMethod("(F)V")
    getCurrentPlayTime = JavaMethod("()J")
    getStartDelay = JavaMethod("()J")
    setStartDelay = JavaMethod("(J)V")
    getFrameDelay = JavaStaticMethod("()J")
    setFrameDelay = JavaStaticMethod("(J)V")
    getAnimatedValue = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(Ljava/lang/String;)Ljava/lang/Object;", False, False)])
    setRepeatCount = JavaMethod("(I)V")
    getRepeatCount = JavaMethod("()I")
    setRepeatMode = JavaMethod("(I)V")
    getRepeatMode = JavaMethod("()I")
    addUpdateListener = JavaMethod("(Landroid/animation/ValueAnimator$AnimatorUpdateListener;)V")
    removeAllUpdateListeners = JavaMethod("()V")
    removeUpdateListener = JavaMethod("(Landroid/animation/ValueAnimator$AnimatorUpdateListener;)V")
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)V")
    getInterpolator = JavaMethod("()Landroid/animation/TimeInterpolator;")
    setEvaluator = JavaMethod("(Landroid/animation/TypeEvaluator;)V")
    start = JavaMethod("()V")
    cancel = JavaMethod("()V")
    end = JavaMethod("()V")
    resume = JavaMethod("()V")
    pause = JavaMethod("()V")
    isRunning = JavaMethod("()Z")
    isStarted = JavaMethod("()Z")
    reverse = JavaMethod("()V")
    getAnimatedFraction = JavaMethod("()F")
    clone = JavaMethod("()Landroid/animation/ValueAnimator;")
    toString = JavaMethod("()Ljava/lang/String;")

    class AnimatorUpdateListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/ValueAnimator/AnimatorUpdateListener"
        onAnimationUpdate = JavaMethod("(Landroid/animation/ValueAnimator;)V")

    class DurationScaleChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/ValueAnimator/DurationScaleChangeListener"
        onChanged = JavaMethod("(F)V")