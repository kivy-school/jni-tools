from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteDatatypeMismatchException"]

class SQLiteDatatypeMismatchException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteDatatypeMismatchException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]