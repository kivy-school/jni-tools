from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AEADBadTagException"]

class AEADBadTagException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/crypto/AEADBadTagException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]