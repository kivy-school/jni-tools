from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteCursorDriver"]

class SQLiteCursorDriver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteCursorDriver"
    cursorClosed = JavaMethod("()V")
    cursorDeactivated = JavaMethod("()V")
    cursorRequeried = JavaMethod("(Landroid/database/Cursor;)V")
    setBindArguments = JavaMethod("([Ljava/lang/String;)V")
    query = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase$CursorFactory;[Ljava/lang/String;)Landroid/database/Cursor;")