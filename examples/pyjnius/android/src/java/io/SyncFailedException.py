from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncFailedException"]

class SyncFailedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/SyncFailedException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]