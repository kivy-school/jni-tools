from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoSuchMethodError"]

class NoSuchMethodError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/NoSuchMethodError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]