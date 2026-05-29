from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidMarkException"]

class InvalidMarkException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/InvalidMarkException"
    __javaconstructor__ = [("()V", False)]