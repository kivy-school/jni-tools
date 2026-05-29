from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WorkDuration"]

class WorkDuration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/WorkDuration"
    __javaconstructor__ = [("()V", False)]
    setActualTotalDurationNanos = JavaMethod("(J)V")
    setWorkPeriodStartTimestampNanos = JavaMethod("(J)V")
    setActualCpuDurationNanos = JavaMethod("(J)V")
    setActualGpuDurationNanos = JavaMethod("(J)V")
    getActualTotalDurationNanos = JavaMethod("()J")
    getWorkPeriodStartTimestampNanos = JavaMethod("()J")
    getActualCpuDurationNanos = JavaMethod("()J")
    getActualGpuDurationNanos = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")