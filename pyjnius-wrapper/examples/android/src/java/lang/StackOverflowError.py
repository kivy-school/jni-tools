from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StackOverflowError"]

class StackOverflowError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/StackOverflowError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]