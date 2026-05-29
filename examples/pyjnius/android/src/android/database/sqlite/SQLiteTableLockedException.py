from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteTableLockedException"]

class SQLiteTableLockedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteTableLockedException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]