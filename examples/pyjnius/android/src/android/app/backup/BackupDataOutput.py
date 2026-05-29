from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackupDataOutput"]

class BackupDataOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/backup/BackupDataOutput"
    getQuota = JavaMethod("()J")
    getTransportFlags = JavaMethod("()I")
    writeEntityData = JavaMethod("([BI)I")
    writeEntityHeader = JavaMethod("(Ljava/lang/String;I)I")