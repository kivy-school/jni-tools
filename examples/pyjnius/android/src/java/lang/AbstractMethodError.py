from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractMethodError"]

class AbstractMethodError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/AbstractMethodError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]