from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConfirmationAlreadyPresentingException"]

class ConfirmationAlreadyPresentingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/ConfirmationAlreadyPresentingException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]