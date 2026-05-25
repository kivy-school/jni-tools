from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalAccessException"]

class IllegalAccessException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/IllegalAccessException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]