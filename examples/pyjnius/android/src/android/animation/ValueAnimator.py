from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ValueAnimator"]

class ValueAnimator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/ValueAnimator"
    __javaconstructor__ = [("()V", False)]
    INFINITE = JavaStaticField("I")
    RESTART = JavaStaticField("I")
    REVERSE = JavaStaticField("I")
    DURATION_INFINITE = JavaStaticField("J")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMultipleMethod([("()Landroid/animation/Animator;", False, False), ("()Ljava/lang/Object;", False, False), ("()Landroid/animation/ValueAnimator;", False, False)])
    reverse = JavaMethod("()V")
    end = JavaMethod("()V")
    start = JavaMethod("()V")
    cancel = JavaMethod("()V")
    isStarted = JavaMethod("()Z")
    getValues = JavaMethod("()[Landroid/animation/PropertyValuesHolder;")
    setValues = JavaMethod("([Landroid/animation/PropertyValuesHolder;)V", varargs=True)
    getRepeatMode = JavaMethod("()I")
    setRepeatCount = JavaMethod("(I)V")
    setRepeatMode = JavaMethod("(I)V")
    getDuration = JavaMethod("()J")
    pause = JavaMethod("()V")
    resume = JavaMethod("()V")
    getCurrentPlayTime = JavaMethod("()J")
    ofInt = JavaStaticMethod("([I)Landroid/animation/ValueAnimator;", varargs=True)
    addUpdateListener = JavaMethod("(Landroid/animation/ValueAnimator$AnimatorUpdateListener;)V")
    getDurationScale = JavaStaticMethod("()F")
    ofObject = JavaStaticMethod("(Landroid/animation/TypeEvaluator;[Ljava/lang/Object;)Landroid/animation/ValueAnimator;", varargs=True)
    ofArgb = JavaStaticMethod("([I)Landroid/animation/ValueAnimator;", varargs=True)
    setObjectValues = JavaMethod("([Ljava/lang/Object;)V", varargs=True)
    setIntValues = JavaMethod("([I)V", varargs=True)
    getAnimatedValue = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(Ljava/lang/String;)Ljava/lang/Object;", False, False)])
    setFloatValues = JavaMethod("([F)V", varargs=True)
    ofFloat = JavaStaticMethod("([F)Landroid/animation/ValueAnimator;", varargs=True)
    ofPropertyValuesHolder = JavaStaticMethod("([Landroid/animation/PropertyValuesHolder;)Landroid/animation/ValueAnimator;", varargs=True)
    areAnimatorsEnabled = JavaStaticMethod("()Z")
    getAnimatedFraction = JavaMethod("()F")
    getFrameDelay = JavaStaticMethod("()J")
    getTotalDuration = JavaMethod("()J")
    isRunning = JavaMethod("()Z")
    registerDurationScaleChangeListener = JavaStaticMethod("(Landroid/animation/ValueAnimator$DurationScaleChangeListener;)Z")
    removeAllUpdateListeners = JavaMethod("()V")
    removeUpdateListener = JavaMethod("(Landroid/animation/ValueAnimator$AnimatorUpdateListener;)V")
    setCurrentFraction = JavaMethod("(F)V")
    setCurrentPlayTime = JavaMethod("(J)V")
    setEvaluator = JavaMethod("(Landroid/animation/TypeEvaluator;)V")
    setFrameDelay = JavaStaticMethod("(J)V")
    unregisterDurationScaleChangeListener = JavaStaticMethod("(Landroid/animation/ValueAnimator$DurationScaleChangeListener;)Z")
    getRepeatCount = JavaMethod("()I")
    getInterpolator = JavaMethod("()Landroid/animation/TimeInterpolator;")
    getStartDelay = JavaMethod("()J")
    setDuration = JavaMultipleMethod([("(J)Landroid/animation/Animator;", False, False), ("(J)Landroid/animation/ValueAnimator;", False, False)])
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)V")
    setStartDelay = JavaMethod("(J)V")

    class DurationScaleChangeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/ValueAnimator$DurationScaleChangeListener"
        onChanged = JavaMethod("(F)V")

    class AnimatorUpdateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/ValueAnimator$AnimatorUpdateListener"
        onAnimationUpdate = JavaMethod("(Landroid/animation/ValueAnimator;)V")