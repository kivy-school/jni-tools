from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VerifyError"]

class VerifyError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/VerifyError"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]