from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteReadOnlyDatabaseException"]

class SQLiteReadOnlyDatabaseException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteReadOnlyDatabaseException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]