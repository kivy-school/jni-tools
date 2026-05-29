from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteCursor"]

class SQLiteCursor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteCursor"
    __javaconstructor__ = [("(Landroid/database/sqlite/SQLiteDatabase;Landroid/database/sqlite/SQLiteCursorDriver;Ljava/lang/String;Landroid/database/sqlite/SQLiteQuery;)V", False), ("(Landroid/database/sqlite/SQLiteCursorDriver;Ljava/lang/String;Landroid/database/sqlite/SQLiteQuery;)V", False)]
    getDatabase = JavaMethod("()Landroid/database/sqlite/SQLiteDatabase;")
    onMove = JavaMethod("(II)Z")
    getCount = JavaMethod("()I")
    getColumnIndex = JavaMethod("(Ljava/lang/String;)I")
    getColumnNames = JavaMethod("()[Ljava/lang/String;")
    deactivate = JavaMethod("()V")
    close = JavaMethod("()V")
    requery = JavaMethod("()Z")
    setWindow = JavaMethod("(Landroid/database/CursorWindow;)V")
    setSelectionArguments = JavaMethod("([Ljava/lang/String;)V")
    setFillWindowForwardOnly = JavaMethod("(Z)V")
    finalize = JavaMethod("()V")