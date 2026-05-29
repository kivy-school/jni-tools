from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteOutOfMemoryException"]

class SQLiteOutOfMemoryException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteOutOfMemoryException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]