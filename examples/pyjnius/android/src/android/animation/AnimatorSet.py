from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimatorSet"]

class AnimatorSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/AnimatorSet"
    __javaconstructor__ = [("()V", False)]
    playTogether = JavaMultipleMethod([("([Landroid/animation/Animator;)V", False, True), ("(Ljava/util/Collection;)V", False, False)])
    playSequentially = JavaMultipleMethod([("([Landroid/animation/Animator;)V", False, True), ("(Ljava/util/List;)V", False, False)])
    getChildAnimations = JavaMethod("()Ljava/util/ArrayList;")
    setTarget = JavaMethod("(Ljava/lang/Object;)V")
    setInterpolator = JavaMethod("(Landroid/animation/TimeInterpolator;)V")
    getInterpolator = JavaMethod("()Landroid/animation/TimeInterpolator;")
    play = JavaMethod("(Landroid/animation/Animator;)Landroid/animation/AnimatorSet$Builder;")
    cancel = JavaMethod("()V")
    end = JavaMethod("()V")
    isRunning = JavaMethod("()Z")
    isStarted = JavaMethod("()Z")
    getStartDelay = JavaMethod("()J")
    setStartDelay = JavaMethod("(J)V")
    getDuration = JavaMethod("()J")
    setDuration = JavaMethod("(J)Landroid/animation/AnimatorSet;")
    setupStartValues = JavaMethod("()V")
    setupEndValues = JavaMethod("()V")
    pause = JavaMethod("()V")
    resume = JavaMethod("()V")
    start = JavaMethod("()V")
    setCurrentPlayTime = JavaMethod("(J)V")
    getCurrentPlayTime = JavaMethod("()J")
    clone = JavaMethod("()Landroid/animation/AnimatorSet;")
    reverse = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    getTotalDuration = JavaMethod("()J")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/AnimatorSet/Builder"
        with = JavaMethod("(Landroid/animation/Animator;)Landroid/animation/AnimatorSet$Builder;")
        before = JavaMethod("(Landroid/animation/Animator;)Landroid/animation/AnimatorSet$Builder;")
        after = JavaMultipleMethod([("(Landroid/animation/Animator;)Landroid/animation/AnimatorSet$Builder;", False, False), ("(J)Landroid/animation/AnimatorSet$Builder;", False, False)])