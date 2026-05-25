from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NullPointerException"]

class NullPointerException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/NullPointerException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]