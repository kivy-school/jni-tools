from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteCursorDriver"]

class SQLiteCursorDriver(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteCursorDriver"
    query = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase$CursorFactory;[Ljava/lang/String;)Landroid/database/Cursor;")
    cursorDeactivated = JavaMethod("()V")
    cursorRequeried = JavaMethod("(Landroid/database/Cursor;)V")
    cursorClosed = JavaMethod("()V")
    setBindArguments = JavaMethod("([Ljava/lang/String;)V")