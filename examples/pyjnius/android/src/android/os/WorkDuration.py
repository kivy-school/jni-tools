from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WorkDuration"]

class WorkDuration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/WorkDuration"
    __javaconstructor__ = [("()V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getActualCpuDurationNanos = JavaMethod("()J")
    getActualGpuDurationNanos = JavaMethod("()J")
    getActualTotalDurationNanos = JavaMethod("()J")
    getWorkPeriodStartTimestampNanos = JavaMethod("()J")
    setActualCpuDurationNanos = JavaMethod("(J)V")
    setActualGpuDurationNanos = JavaMethod("(J)V")
    setActualTotalDurationNanos = JavaMethod("(J)V")
    setWorkPeriodStartTimestampNanos = JavaMethod("(J)V")