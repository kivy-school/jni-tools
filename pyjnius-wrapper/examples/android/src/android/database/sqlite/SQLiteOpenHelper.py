from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteOpenHelper"]

class SQLiteOpenHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteOpenHelper"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/lang/String;Landroid/database/sqlite/SQLiteDatabase$CursorFactory;I)V", False), ("(Landroid/content/Context;Ljava/lang/String;Landroid/database/sqlite/SQLiteDatabase$CursorFactory;ILandroid/database/DatabaseErrorHandler;)V", False), ("(Landroid/content/Context;Ljava/lang/String;ILandroid/database/sqlite/SQLiteDatabase$OpenParams;)V", False)]
    getDatabaseName = JavaMethod("()Ljava/lang/String;")
    setWriteAheadLoggingEnabled = JavaMethod("(Z)V")
    setLookasideConfig = JavaMethod("(II)V")
    setOpenParams = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase$OpenParams;)V")
    setIdleConnectionTimeout = JavaMethod("(J)V")
    getWritableDatabase = JavaMethod("()Landroid/database/sqlite/SQLiteDatabase;")
    getReadableDatabase = JavaMethod("()Landroid/database/sqlite/SQLiteDatabase;")
    close = JavaMethod("()V")
    onConfigure = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")
    onCreate = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")
    onUpgrade = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;II)V")
    onDowngrade = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;II)V")
    onOpen = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")