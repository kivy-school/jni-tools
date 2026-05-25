from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AggregateRecordsGroupedByDurationResponse"]

class AggregateRecordsGroupedByDurationResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/AggregateRecordsGroupedByDurationResponse"
    getStartTime = JavaMethod("()Ljava/time/Instant;")
    getEndTime = JavaMethod("()Ljava/time/Instant;")
    get = JavaMethod("(Landroid/health/connect/datatypes/AggregationType;)Ljava/lang/Object;")
    getZoneOffset = JavaMethod("(Landroid/health/connect/datatypes/AggregationType;)Ljava/time/ZoneOffset;")
    getDataOrigins = JavaMethod("(Landroid/health/connect/datatypes/AggregationType;)Ljava/util/Set;")