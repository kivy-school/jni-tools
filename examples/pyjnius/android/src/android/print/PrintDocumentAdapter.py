from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintDocumentAdapter"]

class PrintDocumentAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/PrintDocumentAdapter"
    __javaconstructor__ = [("()V", False)]
    EXTRA_PRINT_PREVIEW = JavaStaticField("Ljava/lang/String;")
    onLayout = JavaMethod("(Landroid/print/PrintAttributes;Landroid/print/PrintAttributes;Landroid/os/CancellationSignal;Landroid/print/PrintDocumentAdapter$LayoutResultCallback;Landroid/os/Bundle;)V")
    onStart = JavaMethod("()V")
    onFinish = JavaMethod("()V")
    onWrite = JavaMethod("([Landroid/print/PageRange;Landroid/os/ParcelFileDescriptor;Landroid/os/CancellationSignal;Landroid/print/PrintDocumentAdapter$WriteResultCallback;)V")

    class WriteResultCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/print/PrintDocumentAdapter$WriteResultCallback"
        onWriteFinished = JavaMethod("([Landroid/print/PageRange;)V")
        onWriteFailed = JavaMethod("(Ljava/lang/CharSequence;)V")
        onWriteCancelled = JavaMethod("()V")

    class LayoutResultCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/print/PrintDocumentAdapter$LayoutResultCallback"
        onLayoutFinished = JavaMethod("(Landroid/print/PrintDocumentInfo;Z)V")
        onLayoutFailed = JavaMethod("(Ljava/lang/CharSequence;)V")
        onLayoutCancelled = JavaMethod("()V")