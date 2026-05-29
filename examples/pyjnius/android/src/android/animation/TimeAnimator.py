from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeAnimator"]

class TimeAnimator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/TimeAnimator"
    __javaconstructor__ = [("()V", False)]
    INFINITE = JavaStaticField("I")
    RESTART = JavaStaticField("I")
    REVERSE = JavaStaticField("I")
    DURATION_INFINITE = JavaStaticField("J")
    setTimeListener = JavaMethod("(Landroid/animation/TimeAnimator$TimeListener;)V")
    start = JavaMethod("()V")
    setCurrentPlayTime = JavaMethod("(J)V")

    class TimeListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/TimeAnimator$TimeListener"
        onTimeUpdate = JavaMethod("(Landroid/animation/TimeAnimator;JJ)V")