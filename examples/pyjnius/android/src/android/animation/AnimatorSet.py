from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimatorSet"]

class AnimatorSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/AnimatorSet"
    __javaconstructor__ = [("()V", False)]
    DURATION_INFINITE = JavaStaticField("J")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMultipleMethod([("()Landroid/animation/Animator;", False, False), ("()Ljava/lang/Object;", False, False), ("()Landroid/animation/AnimatorSet;", False, False)])
    reverse = JavaMethod("()V")
    end = JavaMethod("()V")
    start = JavaMethod("()V")
    cancel = JavaMethod("()V")
    isStarted = JavaMethod("()Z")
    setTarget = JavaMethod("(Ljava/lang/Object;)V")
    getDuration = JavaMethod("()J")
    pause = JavaMethod("()V")
    resume = JavaMethod("()V")
    getCurrentPlayTime = JavaMethod("()J")
    setupEndValues = JavaMethod("()V")
    setupStartValues = JavaMethod("()V")
    getTotalDuration = JavaMethod("()J")
    isRunning = JavaMethod("()Z")
    setCurrentPlayTime = JavaMethod("(J)V")
    getChildAnimations = JavaMethod("()Ljava/util/ArrayList;")
    playSequentially = JavaMultipleMethod([("([Landroid/animation/Animator;)V", False, True), ("(Ljava/util/List;)V", False, False)])
    playTogether = JavaMultipleMethod([("([Landroid/animation/Animator;)V", False, True), ("(Ljava/util/Collection;)V", False, False)])
    play = JavaMethod("(Landroid/animation/Animator;)Landroid/animation/AnimatorSet$Builder;")
    getInterpolator = JavaMethod("()Landroid/animation/TimeInterpolator;")
    getStartDelay = JavaMethod("()J")
    setDuration = JavaMultipleMethod([("(J)Landroid/animation/Animator;", False, False), ("(J)Landroid/animation/AnimatorSet;", False, False)])
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)V")
    setStartDelay = JavaMethod("(J)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/AnimatorSet$Builder"
        with = JavaMethod("(Landroid/animation/Animator;)Landroid/animation/AnimatorSet$Builder;")
        before = JavaMethod("(Landroid/animation/Animator;)Landroid/animation/AnimatorSet$Builder;")
        after = JavaMultipleMethod([("(Landroid/animation/Animator;)Landroid/animation/AnimatorSet$Builder;", False, False), ("(J)Landroid/animation/AnimatorSet$Builder;", False, False)])