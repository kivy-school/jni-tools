from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteBindOrColumnIndexOutOfRangeException"]

class SQLiteBindOrColumnIndexOutOfRangeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteBindOrColumnIndexOutOfRangeException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]