from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InsertRecordsResponse"]

class InsertRecordsResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/InsertRecordsResponse"
    getRecords = JavaMethod("()Ljava/util/List;")