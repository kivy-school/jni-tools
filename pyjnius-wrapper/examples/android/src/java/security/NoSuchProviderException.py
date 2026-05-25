from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoSuchProviderException"]

class NoSuchProviderException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/NoSuchProviderException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]