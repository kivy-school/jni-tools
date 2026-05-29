from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteStatement"]

class SQLiteStatement(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteStatement"
    execute = JavaMethod("()V")
    executeUpdateDelete = JavaMethod("()I")
    executeInsert = JavaMethod("()J")
    simpleQueryForLong = JavaMethod("()J")
    simpleQueryForString = JavaMethod("()Ljava/lang/String;")
    simpleQueryForBlobFileDescriptor = JavaMethod("()Landroid/os/ParcelFileDescriptor;")
    toString = JavaMethod("()Ljava/lang/String;")