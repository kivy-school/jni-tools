from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteTransactionListener"]

class SQLiteTransactionListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteTransactionListener"
    onBegin = JavaMethod("()V")
    onCommit = JavaMethod("()V")
    onRollback = JavaMethod("()V")