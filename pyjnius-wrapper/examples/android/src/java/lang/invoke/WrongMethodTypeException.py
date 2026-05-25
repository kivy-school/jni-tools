from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WrongMethodTypeException"]

class WrongMethodTypeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/invoke/WrongMethodTypeException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]