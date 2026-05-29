from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoSuchPaddingException"]

class NoSuchPaddingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/NoSuchPaddingException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]