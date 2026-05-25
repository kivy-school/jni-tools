from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrinterDiscoverySession"]

class PrinterDiscoverySession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/printservice/PrinterDiscoverySession"
    __javaconstructor__ = [("()V", False)]
    getPrinters = JavaMethod("()Ljava/util/List;")
    addPrinters = JavaMethod("(Ljava/util/List;)V")
    removePrinters = JavaMethod("(Ljava/util/List;)V")
    onStartPrinterDiscovery = JavaMethod("(Ljava/util/List;)V")
    onStopPrinterDiscovery = JavaMethod("()V")
    onValidatePrinters = JavaMethod("(Ljava/util/List;)V")
    onStartPrinterStateTracking = JavaMethod("(Landroid/print/PrinterId;)V")
    onRequestCustomPrinterIcon = JavaMethod("(Landroid/print/PrinterId;Landroid/os/CancellationSignal;Landroid/printservice/CustomPrinterIconCallback;)V")
    onStopPrinterStateTracking = JavaMethod("(Landroid/print/PrinterId;)V")
    getTrackedPrinters = JavaMethod("()Ljava/util/List;")
    onDestroy = JavaMethod("()V")
    isDestroyed = JavaMethod("()Z")
    isPrinterDiscoveryStarted = JavaMethod("()Z")