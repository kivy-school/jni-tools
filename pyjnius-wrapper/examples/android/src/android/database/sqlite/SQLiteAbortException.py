from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteAbortException"]

class SQLiteAbortException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteAbortException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]