from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackupDataInput"]

class BackupDataInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/backup/BackupDataInput"
    getDataSize = JavaMethod("()I")
    skipEntityData = JavaMethod("()V")
    readNextHeader = JavaMethod("()Z")
    readEntityData = JavaMethod("([BII)I")
    getKey = JavaMethod("()Ljava/lang/String;")