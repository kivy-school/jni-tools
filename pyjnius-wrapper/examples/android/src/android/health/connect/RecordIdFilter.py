from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecordIdFilter"]

class RecordIdFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/RecordIdFilter"
    fromClientRecordId = JavaStaticMethod("(Ljava/lang/Class;Ljava/lang/String;)Landroid/health/connect/RecordIdFilter;")
    fromId = JavaStaticMethod("(Ljava/lang/Class;Ljava/lang/String;)Landroid/health/connect/RecordIdFilter;")
    getRecordType = JavaMethod("()Ljava/lang/Class;")
    getId = JavaMethod("()Ljava/lang/String;")
    getClientRecordId = JavaMethod("()Ljava/lang/String;")