from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Animator"]

class Animator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/Animator"
    __javaconstructor__ = [("()V", False)]
    DURATION_INFINITE = JavaStaticField("J")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/animation/Animator;", False, False)])
    end = JavaMethod("()V")
    start = JavaMethod("()V")
    cancel = JavaMethod("()V")
    isStarted = JavaMethod("()Z")
    setTarget = JavaMethod("(Ljava/lang/Object;)V")
    getDuration = JavaMethod("()J")
    pause = JavaMethod("()V")
    resume = JavaMethod("()V")
    removeAllListeners = JavaMethod("()V")
    getListeners = JavaMethod("()Ljava/util/ArrayList;")
    isPaused = JavaMethod("()Z")
    addPauseListener = JavaMethod("(Landroid/animation/Animator$AnimatorPauseListener;)V")
    removePauseListener = JavaMethod("(Landroid/animation/Animator$AnimatorPauseListener;)V")
    setupEndValues = JavaMethod("()V")
    setupStartValues = JavaMethod("()V")
    getTotalDuration = JavaMethod("()J")
    isRunning = JavaMethod("()Z")
    addListener = JavaMethod("(Landroid/animation/Animator$AnimatorListener;)V")
    getInterpolator = JavaMethod("()Landroid/animation/TimeInterpolator;")
    getStartDelay = JavaMethod("()J")
    removeListener = JavaMethod("(Landroid/animation/Animator$AnimatorListener;)V")
    setDuration = JavaMethod("(J)Landroid/animation/Animator;")
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)V")
    setStartDelay = JavaMethod("(J)V")

    class AnimatorPauseListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/Animator$AnimatorPauseListener"
        onAnimationPause = JavaMethod("(Landroid/animation/Animator;)V")
        onAnimationResume = JavaMethod("(Landroid/animation/Animator;)V")

    class AnimatorListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/Animator$AnimatorListener"
        onAnimationRepeat = JavaMethod("(Landroid/animation/Animator;)V")
        onAnimationCancel = JavaMethod("(Landroid/animation/Animator;)V")
        onAnimationEnd = JavaMultipleMethod([("(Landroid/animation/Animator;Z)V", False, False), ("(Landroid/animation/Animator;)V", False, False)])
        onAnimationStart = JavaMultipleMethod([("(Landroid/animation/Animator;Z)V", False, False), ("(Landroid/animation/Animator;)V", False, False)])