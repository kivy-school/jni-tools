from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackupDataInput"]

class BackupDataInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/backup/BackupDataInput"
    finalize = JavaMethod("()V")
    readNextHeader = JavaMethod("()Z")
    getKey = JavaMethod("()Ljava/lang/String;")
    getDataSize = JavaMethod("()I")
    readEntityData = JavaMethod("([BII)I")
    skipEntityData = JavaMethod("()V")