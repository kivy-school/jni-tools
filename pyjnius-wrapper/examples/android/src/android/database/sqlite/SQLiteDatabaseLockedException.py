from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteDatabaseLockedException"]

class SQLiteDatabaseLockedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteDatabaseLockedException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]