from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteOpenHelper"]

class SQLiteOpenHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteOpenHelper"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/lang/String;Landroid/database/sqlite/SQLiteDatabase$CursorFactory;ILandroid/database/DatabaseErrorHandler;)V", False), ("(Landroid/content/Context;Ljava/lang/String;ILandroid/database/sqlite/SQLiteDatabase$OpenParams;)V", False), ("(Landroid/content/Context;Ljava/lang/String;Landroid/database/sqlite/SQLiteDatabase$CursorFactory;I)V", False)]
    setIdleConnectionTimeout = JavaMethod("(J)V")
    setLookasideConfig = JavaMethod("(II)V")
    onDowngrade = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;II)V")
    onOpen = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")
    getReadableDatabase = JavaMethod("()Landroid/database/sqlite/SQLiteDatabase;")
    getWritableDatabase = JavaMethod("()Landroid/database/sqlite/SQLiteDatabase;")
    getDatabaseName = JavaMethod("()Ljava/lang/String;")
    onConfigure = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")
    onUpgrade = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;II)V")
    setOpenParams = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase$OpenParams;)V")
    setWriteAheadLoggingEnabled = JavaMethod("(Z)V")
    close = JavaMethod("()V")
    onCreate = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")