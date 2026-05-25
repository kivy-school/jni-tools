from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackupDataInputStream"]

class BackupDataInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/backup/BackupDataInputStream"
    read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False), ("([B)I", False, False)])
    getKey = JavaMethod("()Ljava/lang/String;")
    size = JavaMethod("()I")