from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteProgram"]

class SQLiteProgram(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteProgram"
    bindString = JavaMethod("(ILjava/lang/String;)V")
    bindBlob = JavaMethod("(I[B)V")
    clearBindings = JavaMethod("()V")
    bindNull = JavaMethod("(I)V")
    bindDouble = JavaMethod("(ID)V")
    bindLong = JavaMethod("(IJ)V")
    bindAllArgsAsStrings = JavaMethod("([Ljava/lang/String;)V")
    getUniqueId = JavaMethod("()I")