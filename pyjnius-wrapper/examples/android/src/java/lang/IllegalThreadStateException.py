from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalThreadStateException"]

class IllegalThreadStateException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/IllegalThreadStateException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]