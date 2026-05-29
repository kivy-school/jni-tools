from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CancellationSignal"]

class CancellationSignal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/CancellationSignal"
    __javaconstructor__ = [("()V", False)]
    cancel = JavaMethod("()V")
    throwIfCanceled = JavaMethod("()V")
    setOnCancelListener = JavaMethod("(Landroid/os/CancellationSignal$OnCancelListener;)V")
    isCanceled = JavaMethod("()Z")

    class OnCancelListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/CancellationSignal$OnCancelListener"
        onCancel = JavaMethod("()V")