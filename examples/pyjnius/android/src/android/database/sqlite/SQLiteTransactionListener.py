from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteTransactionListener"]

class SQLiteTransactionListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteTransactionListener"
    onRollback = JavaMethod("()V")
    onCommit = JavaMethod("()V")
    onBegin = JavaMethod("()V")