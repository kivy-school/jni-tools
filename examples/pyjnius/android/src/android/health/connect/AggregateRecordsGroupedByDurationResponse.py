from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AggregateRecordsGroupedByDurationResponse"]

class AggregateRecordsGroupedByDurationResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/AggregateRecordsGroupedByDurationResponse"
    get = JavaMethod("(Landroid/health/connect/datatypes/AggregationType;)Ljava/lang/Object;")
    getStartTime = JavaMethod("()Ljava/time/Instant;")
    getDataOrigins = JavaMethod("(Landroid/health/connect/datatypes/AggregationType;)Ljava/util/Set;")
    getEndTime = JavaMethod("()Ljava/time/Instant;")
    getZoneOffset = JavaMethod("(Landroid/health/connect/datatypes/AggregationType;)Ljava/time/ZoneOffset;")