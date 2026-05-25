from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteException"]

class SQLiteException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]