from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteClosable"]

class SQLiteClosable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteClosable"
    __javaconstructor__ = [("()V", False)]
    onAllReferencesReleased = JavaMethod("()V")
    onAllReferencesReleasedFromContainer = JavaMethod("()V")
    acquireReference = JavaMethod("()V")
    releaseReference = JavaMethod("()V")
    releaseReferenceFromContainer = JavaMethod("()V")
    close = JavaMethod("()V")