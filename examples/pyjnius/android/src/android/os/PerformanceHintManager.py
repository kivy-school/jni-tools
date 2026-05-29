from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PerformanceHintManager"]

class PerformanceHintManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/PerformanceHintManager"
    createHintSession = JavaMethod("([IJ)Landroid/os/PerformanceHintManager$Session;")
    getPreferredUpdateRateNanos = JavaMethod("()J")

    class Session(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/PerformanceHintManager$Session"
        close = JavaMethod("()V")
        setThreads = JavaMethod("([I)V")
        setPreferPowerEfficiency = JavaMethod("(Z)V")
        updateTargetWorkDuration = JavaMethod("(J)V")
        reportActualWorkDuration = JavaMultipleMethod([("(Landroid/os/WorkDuration;)V", False, False), ("(J)V", False, False)])