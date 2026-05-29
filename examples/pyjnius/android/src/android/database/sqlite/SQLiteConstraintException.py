from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteConstraintException"]

class SQLiteConstraintException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteConstraintException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]