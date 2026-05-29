from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalAccessError"]

class IllegalAccessError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/IllegalAccessError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]