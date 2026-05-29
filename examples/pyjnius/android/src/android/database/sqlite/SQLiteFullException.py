from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteFullException"]

class SQLiteFullException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteFullException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]