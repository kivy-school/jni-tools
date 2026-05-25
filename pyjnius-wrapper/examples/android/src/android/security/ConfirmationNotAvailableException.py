from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConfirmationNotAvailableException"]

class ConfirmationNotAvailableException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/ConfirmationNotAvailableException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]