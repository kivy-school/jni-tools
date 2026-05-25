from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimeInstantRangeFilter"]

class TimeInstantRangeFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/TimeInstantRangeFilter"
    getStartTime = JavaMethod("()Ljava/time/Instant;")
    getEndTime = JavaMethod("()Ljava/time/Instant;")
    isBounded = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/TimeInstantRangeFilter/Builder"
        __javaconstructor__ = [("()V", False)]
        setStartTime = JavaMethod("(Ljava/time/Instant;)Landroid/health/connect/TimeInstantRangeFilter$Builder;")
        setEndTime = JavaMethod("(Ljava/time/Instant;)Landroid/health/connect/TimeInstantRangeFilter$Builder;")
        build = JavaMethod("()Landroid/health/connect/TimeInstantRangeFilter;")