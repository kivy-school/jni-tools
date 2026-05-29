from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AggregateRecordsGroupedByPeriodResponse"]

class AggregateRecordsGroupedByPeriodResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/AggregateRecordsGroupedByPeriodResponse"
    get = JavaMethod("(Landroid/health/connect/datatypes/AggregationType;)Ljava/lang/Object;")
    getStartTime = JavaMethod("()Ljava/time/LocalDateTime;")
    getDataOrigins = JavaMethod("(Landroid/health/connect/datatypes/AggregationType;)Ljava/util/Set;")
    getEndTime = JavaMethod("()Ljava/time/LocalDateTime;")
    getZoneOffset = JavaMethod("(Landroid/health/connect/datatypes/AggregationType;)Ljava/time/ZoneOffset;")