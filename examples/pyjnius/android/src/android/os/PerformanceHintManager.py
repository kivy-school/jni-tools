from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PerformanceHintManager"]

class PerformanceHintManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/PerformanceHintManager"
    getPreferredUpdateRateNanos = JavaMethod("()J")
    createHintSession = JavaMethod("([IJ)Landroid/os/PerformanceHintManager$Session;")

    class Session(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/PerformanceHintManager/Session"
        finalize = JavaMethod("()V")
        updateTargetWorkDuration = JavaMethod("(J)V")
        reportActualWorkDuration = JavaMultipleMethod([("(J)V", False, False), ("(Landroid/os/WorkDuration;)V", False, False)])
        close = JavaMethod("()V")
        setPreferPowerEfficiency = JavaMethod("(Z)V")
        setThreads = JavaMethod("([I)V")