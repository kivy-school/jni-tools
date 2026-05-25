from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BootstrapMethodError"]

class BootstrapMethodError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/BootstrapMethodError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False)]