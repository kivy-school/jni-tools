from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AggregateRecordsResponse"]

class AggregateRecordsResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/AggregateRecordsResponse"
    get = JavaMethod("(Landroid/health/connect/datatypes/AggregationType;)Ljava/lang/Object;")
    getZoneOffset = JavaMethod("(Landroid/health/connect/datatypes/AggregationType;)Ljava/time/ZoneOffset;")
    getDataOrigins = JavaMethod("(Landroid/health/connect/datatypes/AggregationType;)Ljava/util/Set;")