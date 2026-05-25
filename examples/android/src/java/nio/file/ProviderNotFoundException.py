from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProviderNotFoundException"]

class ProviderNotFoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/ProviderNotFoundException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]