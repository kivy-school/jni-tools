from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteCursor"]

class SQLiteCursor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteCursor"
    __javaconstructor__ = [("(Landroid/database/sqlite/SQLiteCursorDriver;Ljava/lang/String;Landroid/database/sqlite/SQLiteQuery;)V", False), ("(Landroid/database/sqlite/SQLiteDatabase;Landroid/database/sqlite/SQLiteCursorDriver;Ljava/lang/String;Landroid/database/sqlite/SQLiteQuery;)V", False)]
    FIELD_TYPE_BLOB = JavaStaticField("I")
    FIELD_TYPE_FLOAT = JavaStaticField("I")
    FIELD_TYPE_INTEGER = JavaStaticField("I")
    FIELD_TYPE_NULL = JavaStaticField("I")
    FIELD_TYPE_STRING = JavaStaticField("I")
    onMove = JavaMethod("(II)Z")
    setWindow = JavaMethod("(Landroid/database/CursorWindow;)V")
    getDatabase = JavaMethod("()Landroid/database/sqlite/SQLiteDatabase;")
    setFillWindowForwardOnly = JavaMethod("(Z)V")
    setSelectionArguments = JavaMethod("([Ljava/lang/String;)V")
    close = JavaMethod("()V")
    getCount = JavaMethod("()I")
    deactivate = JavaMethod("()V")
    getColumnIndex = JavaMethod("(Ljava/lang/String;)I")
    getColumnNames = JavaMethod("()[Ljava/lang/String;")
    requery = JavaMethod("()Z")