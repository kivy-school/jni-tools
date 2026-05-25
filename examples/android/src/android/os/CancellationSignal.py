from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CancellationSignal"]

class CancellationSignal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/CancellationSignal"
    __javaconstructor__ = [("()V", False)]
    isCanceled = JavaMethod("()Z")
    throwIfCanceled = JavaMethod("()V")
    cancel = JavaMethod("()V")
    setOnCancelListener = JavaMethod("(Landroid/os/CancellationSignal$OnCancelListener;)V")

    class OnCancelListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/CancellationSignal/OnCancelListener"
        onCancel = JavaMethod("()V")