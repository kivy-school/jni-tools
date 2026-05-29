from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatabaseErrorHandler"]

class DatabaseErrorHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/DatabaseErrorHandler"
    onCorruption = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")