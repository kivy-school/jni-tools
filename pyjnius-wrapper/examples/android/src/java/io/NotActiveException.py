from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotActiveException"]

class NotActiveException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/NotActiveException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("()V", False)]