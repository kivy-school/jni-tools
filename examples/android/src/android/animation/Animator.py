from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Animator"]

class Animator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/Animator"
    __javaconstructor__ = [("()V", False)]
    DURATION_INFINITE = JavaStaticField("J")
    start = JavaMethod("()V")
    cancel = JavaMethod("()V")
    end = JavaMethod("()V")
    pause = JavaMethod("()V")
    resume = JavaMethod("()V")
    isPaused = JavaMethod("()Z")
    getStartDelay = JavaMethod("()J")
    setStartDelay = JavaMethod("(J)V")
    setDuration = JavaMethod("(J)Landroid/animation/Animator;")
    getDuration = JavaMethod("()J")
    getTotalDuration = JavaMethod("()J")
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)V")
    getInterpolator = JavaMethod("()Landroid/animation/TimeInterpolator;")
    isRunning = JavaMethod("()Z")
    isStarted = JavaMethod("()Z")
    addListener = JavaMethod("(Landroid/animation/Animator$AnimatorListener;)V")
    removeListener = JavaMethod("(Landroid/animation/Animator$AnimatorListener;)V")
    getListeners = JavaMethod("()Ljava/util/ArrayList;")
    addPauseListener = JavaMethod("(Landroid/animation/Animator$AnimatorPauseListener;)V")
    removePauseListener = JavaMethod("(Landroid/animation/Animator$AnimatorPauseListener;)V")
    removeAllListeners = JavaMethod("()V")
    clone = JavaMethod("()Landroid/animation/Animator;")
    setupStartValues = JavaMethod("()V")
    setupEndValues = JavaMethod("()V")
    setTarget = JavaMethod("(Ljava/lang/Object;)V")

    class AnimatorListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/Animator/AnimatorListener"
        onAnimationStart = JavaMultipleMethod([("(Landroid/animation/Animator;Z)V", False, False), ("(Landroid/animation/Animator;)V", False, False)])
        onAnimationEnd = JavaMultipleMethod([("(Landroid/animation/Animator;Z)V", False, False), ("(Landroid/animation/Animator;)V", False, False)])
        onAnimationCancel = JavaMethod("(Landroid/animation/Animator;)V")
        onAnimationRepeat = JavaMethod("(Landroid/animation/Animator;)V")

    class AnimatorPauseListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/Animator/AnimatorPauseListener"
        onAnimationPause = JavaMethod("(Landroid/animation/Animator;)V")
        onAnimationResume = JavaMethod("(Landroid/animation/Animator;)V")