from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadRecordsRequestUsingFilters"]

class ReadRecordsRequestUsingFilters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/ReadRecordsRequestUsingFilters"
    getTimeRangeFilter = JavaMethod("()Landroid/health/connect/TimeRangeFilter;")
    getDataOrigins = JavaMethod("()Ljava/util/Set;")
    getPageSize = JavaMethod("()I")
    getPageToken = JavaMethod("()J")
    isAscending = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/ReadRecordsRequestUsingFilters/Builder"
        __javaconstructor__ = [("(Ljava/lang/Class;)V", False)]
        addDataOrigins = JavaMethod("(Landroid/health/connect/datatypes/DataOrigin;)Landroid/health/connect/ReadRecordsRequestUsingFilters$Builder;")
        setTimeRangeFilter = JavaMethod("(Landroid/health/connect/TimeRangeFilter;)Landroid/health/connect/ReadRecordsRequestUsingFilters$Builder;")
        setPageSize = JavaMethod("(I)Landroid/health/connect/ReadRecordsRequestUsingFilters$Builder;")
        setPageToken = JavaMethod("(J)Landroid/health/connect/ReadRecordsRequestUsingFilters$Builder;")
        setAscending = JavaMethod("(Z)Landroid/health/connect/ReadRecordsRequestUsingFilters$Builder;")
        build = JavaMethod("()Landroid/health/connect/ReadRecordsRequestUsingFilters;")