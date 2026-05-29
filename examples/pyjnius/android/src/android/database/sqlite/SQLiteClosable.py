from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteClosable"]

class SQLiteClosable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteClosable"
    __javaconstructor__ = [("()V", False)]
    close = JavaMethod("()V")
    releaseReference = JavaMethod("()V")
    acquireReference = JavaMethod("()V")
    releaseReferenceFromContainer = JavaMethod("()V")