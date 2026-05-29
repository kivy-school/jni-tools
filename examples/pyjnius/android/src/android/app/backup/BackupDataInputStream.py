from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackupDataInputStream"]

class BackupDataInputStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/backup/BackupDataInputStream"
    size = JavaMethod("()I")
    getKey = JavaMethod("()Ljava/lang/String;")
    read = JavaMultipleMethod([("([B)I", False, False), ("([BII)I", False, False), ("()I", False, False)])