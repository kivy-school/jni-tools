from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BadPaddingException"]

class BadPaddingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/BadPaddingException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]