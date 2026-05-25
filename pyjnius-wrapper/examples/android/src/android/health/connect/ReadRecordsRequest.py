from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadRecordsRequest"]

class ReadRecordsRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/ReadRecordsRequest"
    getRecordType = JavaMethod("()Ljava/lang/Class;")