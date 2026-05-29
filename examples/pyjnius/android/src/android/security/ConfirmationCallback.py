from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConfirmationCallback"]

class ConfirmationCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/ConfirmationCallback"
    __javaconstructor__ = [("()V", False)]
    onDismissed = JavaMethod("()V")
    onConfirmed = JavaMethod("([B)V")
    onError = JavaMethod("(Ljava/lang/Throwable;)V")
    onCanceled = JavaMethod("()V")