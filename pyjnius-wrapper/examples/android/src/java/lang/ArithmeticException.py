from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArithmeticException"]

class ArithmeticException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ArithmeticException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]