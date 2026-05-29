from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteStatement"]

class SQLiteStatement(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteStatement"
    simpleQueryForLong = JavaMethod("()J")
    executeInsert = JavaMethod("()J")
    executeUpdateDelete = JavaMethod("()I")
    simpleQueryForBlobFileDescriptor = JavaMethod("()Landroid/os/ParcelFileDescriptor;")
    simpleQueryForString = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    execute = JavaMethod("()V")