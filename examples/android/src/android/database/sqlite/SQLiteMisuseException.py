from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteMisuseException"]

class SQLiteMisuseException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteMisuseException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]