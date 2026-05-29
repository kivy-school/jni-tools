from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnknownError"]

class UnknownError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/UnknownError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]