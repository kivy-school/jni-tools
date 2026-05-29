from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteDatabaseCorruptException"]

class SQLiteDatabaseCorruptException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteDatabaseCorruptException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]