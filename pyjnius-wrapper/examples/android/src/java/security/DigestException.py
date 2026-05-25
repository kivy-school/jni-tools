from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DigestException"]

class DigestException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DigestException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False)]