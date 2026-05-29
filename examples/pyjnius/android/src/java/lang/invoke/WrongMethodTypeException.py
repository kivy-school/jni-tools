from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WrongMethodTypeException"]

class WrongMethodTypeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/invoke/WrongMethodTypeException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("()V", False)]