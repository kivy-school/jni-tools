from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnsatisfiedLinkError"]

class UnsatisfiedLinkError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/UnsatisfiedLinkError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]