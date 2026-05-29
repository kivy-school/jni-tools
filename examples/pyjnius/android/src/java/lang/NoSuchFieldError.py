from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoSuchFieldError"]

class NoSuchFieldError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/NoSuchFieldError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]