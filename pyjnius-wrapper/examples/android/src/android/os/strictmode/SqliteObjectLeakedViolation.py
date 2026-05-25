from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SqliteObjectLeakedViolation"]

class SqliteObjectLeakedViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/SqliteObjectLeakedViolation"