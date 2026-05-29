from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ShortBufferException"]

class ShortBufferException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/ShortBufferException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]