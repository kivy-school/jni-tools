from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteDiskIOException"]

class SQLiteDiskIOException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteDiskIOException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]