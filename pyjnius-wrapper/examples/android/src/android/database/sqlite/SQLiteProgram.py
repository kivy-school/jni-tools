from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteProgram"]

class SQLiteProgram(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteProgram"
    getUniqueId = JavaMethod("()I")
    bindNull = JavaMethod("(I)V")
    bindLong = JavaMethod("(IJ)V")
    bindDouble = JavaMethod("(ID)V")
    bindString = JavaMethod("(ILjava/lang/String;)V")
    bindBlob = JavaMethod("(I[B)V")
    clearBindings = JavaMethod("()V")
    bindAllArgsAsStrings = JavaMethod("([Ljava/lang/String;)V")
    onAllReferencesReleased = JavaMethod("()V")