from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DestroyFailedException"]

class DestroyFailedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/DestroyFailedException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]