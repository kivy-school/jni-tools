from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatabaseErrorHandler"]

class DatabaseErrorHandler(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/DatabaseErrorHandler"
    onCorruption = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")