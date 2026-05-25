from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FullBackupDataOutput"]

class FullBackupDataOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/backup/FullBackupDataOutput"
    getQuota = JavaMethod("()J")
    getTransportFlags = JavaMethod("()I")