from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NumberFormatException"]

class NumberFormatException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/NumberFormatException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]