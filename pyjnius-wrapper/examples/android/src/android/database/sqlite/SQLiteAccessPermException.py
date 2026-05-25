from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteAccessPermException"]

class SQLiteAccessPermException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteAccessPermException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]