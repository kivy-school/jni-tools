from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinkageError"]

class LinkageError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/LinkageError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]