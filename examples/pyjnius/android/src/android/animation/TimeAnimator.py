from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeAnimator"]

class TimeAnimator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/animation/TimeAnimator"
    __javaconstructor__ = [("()V", False)]
    start = JavaMethod("()V")
    setCurrentPlayTime = JavaMethod("(J)V")
    setTimeListener = JavaMethod("(Landroid/animation/TimeAnimator$TimeListener;)V")

    class TimeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/animation/TimeAnimator/TimeListener"
        onTimeUpdate = JavaMethod("(Landroid/animation/TimeAnimator;JJ)V")