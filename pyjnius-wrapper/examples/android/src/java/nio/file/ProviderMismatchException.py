from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProviderMismatchException"]

class ProviderMismatchException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/ProviderMismatchException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]