from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConfirmationCallback"]

class ConfirmationCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/ConfirmationCallback"
    __javaconstructor__ = [("()V", False)]
    onConfirmed = JavaMethod("([B)V")
    onDismissed = JavaMethod("()V")
    onCanceled = JavaMethod("()V")
    onError = JavaMethod("(Ljava/lang/Throwable;)V")