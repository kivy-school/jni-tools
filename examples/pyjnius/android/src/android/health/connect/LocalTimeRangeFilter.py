from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocalTimeRangeFilter"]

class LocalTimeRangeFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/LocalTimeRangeFilter"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getStartTime = JavaMethod("()Ljava/time/LocalDateTime;")
    getEndTime = JavaMethod("()Ljava/time/LocalDateTime;")
    isBounded = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/LocalTimeRangeFilter$Builder"
        __javaconstructor__ = [("()V", False)]
        setStartTime = JavaMethod("(Ljava/time/LocalDateTime;)Landroid/health/connect/LocalTimeRangeFilter$Builder;")
        build = JavaMethod("()Landroid/health/connect/LocalTimeRangeFilter;")
        setEndTime = JavaMethod("(Ljava/time/LocalDateTime;)Landroid/health/connect/LocalTimeRangeFilter$Builder;")