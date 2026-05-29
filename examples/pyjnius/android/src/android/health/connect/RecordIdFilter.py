from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecordIdFilter"]

class RecordIdFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/RecordIdFilter"
    getId = JavaMethod("()Ljava/lang/String;")
    fromClientRecordId = JavaStaticMethod("(Ljava/lang/Class;Ljava/lang/String;)Landroid/health/connect/RecordIdFilter;")
    fromId = JavaStaticMethod("(Ljava/lang/Class;Ljava/lang/String;)Landroid/health/connect/RecordIdFilter;")
    getClientRecordId = JavaMethod("()Ljava/lang/String;")
    getRecordType = JavaMethod("()Ljava/lang/Class;")