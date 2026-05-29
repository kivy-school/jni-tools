from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteCantOpenDatabaseException"]

class SQLiteCantOpenDatabaseException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteCantOpenDatabaseException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]