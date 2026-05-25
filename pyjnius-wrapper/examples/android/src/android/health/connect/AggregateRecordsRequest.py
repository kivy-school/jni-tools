from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AggregateRecordsRequest"]

class AggregateRecordsRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/AggregateRecordsRequest"
    getTimeRangeFilter = JavaMethod("()Landroid/health/connect/TimeRangeFilter;")
    getAggregationTypes = JavaMethod("()Ljava/util/Set;")
    getDataOriginsFilters = JavaMethod("()Ljava/util/Set;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/AggregateRecordsRequest/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/TimeRangeFilter;)V", False)]
        addAggregationType = JavaMethod("(Landroid/health/connect/datatypes/AggregationType;)Landroid/health/connect/AggregateRecordsRequest$Builder;")
        addDataOriginsFilter = JavaMethod("(Landroid/health/connect/datatypes/DataOrigin;)Landroid/health/connect/AggregateRecordsRequest$Builder;")
        build = JavaMethod("()Landroid/health/connect/AggregateRecordsRequest;")