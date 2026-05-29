from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoClassDefFoundError"]

class NoClassDefFoundError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/NoClassDefFoundError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]