from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadRecordsResponse"]

class ReadRecordsResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/ReadRecordsResponse"
    getRecords = JavaMethod("()Ljava/util/List;")
    getNextPageToken = JavaMethod("()J")