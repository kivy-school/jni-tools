from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteDoneException"]

class SQLiteDoneException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteDoneException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]