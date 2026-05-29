from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DefaultDatabaseErrorHandler"]

class DefaultDatabaseErrorHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/DefaultDatabaseErrorHandler"
    __javaconstructor__ = [("()V", False)]
    onCorruption = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")