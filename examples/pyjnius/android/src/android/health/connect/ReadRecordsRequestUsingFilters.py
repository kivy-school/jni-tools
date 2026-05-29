from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadRecordsRequestUsingFilters"]

class ReadRecordsRequestUsingFilters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/ReadRecordsRequestUsingFilters"
    getPageToken = JavaMethod("()J")
    isAscending = JavaMethod("()Z")
    getPageSize = JavaMethod("()I")
    getDataOrigins = JavaMethod("()Ljava/util/Set;")
    getTimeRangeFilter = JavaMethod("()Landroid/health/connect/TimeRangeFilter;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/ReadRecordsRequestUsingFilters$Builder"
        __javaconstructor__ = [("(Ljava/lang/Class;)V", False)]
        setPageSize = JavaMethod("(I)Landroid/health/connect/ReadRecordsRequestUsingFilters$Builder;")
        build = JavaMethod("()Landroid/health/connect/ReadRecordsRequestUsingFilters;")
        setPageToken = JavaMethod("(J)Landroid/health/connect/ReadRecordsRequestUsingFilters$Builder;")
        setTimeRangeFilter = JavaMethod("(Landroid/health/connect/TimeRangeFilter;)Landroid/health/connect/ReadRecordsRequestUsingFilters$Builder;")
        addDataOrigins = JavaMethod("(Landroid/health/connect/datatypes/DataOrigin;)Landroid/health/connect/ReadRecordsRequestUsingFilters$Builder;")
        setAscending = JavaMethod("(Z)Landroid/health/connect/ReadRecordsRequestUsingFilters$Builder;")