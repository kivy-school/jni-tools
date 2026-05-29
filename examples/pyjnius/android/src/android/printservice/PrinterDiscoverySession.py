from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrinterDiscoverySession"]

class PrinterDiscoverySession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/printservice/PrinterDiscoverySession"
    __javaconstructor__ = [("()V", False)]
    onValidatePrinters = JavaMethod("(Ljava/util/List;)V")
    getPrinters = JavaMethod("()Ljava/util/List;")
    removePrinters = JavaMethod("(Ljava/util/List;)V")
    getTrackedPrinters = JavaMethod("()Ljava/util/List;")
    addPrinters = JavaMethod("(Ljava/util/List;)V")
    isPrinterDiscoveryStarted = JavaMethod("()Z")
    onRequestCustomPrinterIcon = JavaMethod("(Landroid/print/PrinterId;Landroid/os/CancellationSignal;Landroid/printservice/CustomPrinterIconCallback;)V")
    onStartPrinterDiscovery = JavaMethod("(Ljava/util/List;)V")
    onStartPrinterStateTracking = JavaMethod("(Landroid/print/PrinterId;)V")
    onStopPrinterDiscovery = JavaMethod("()V")
    onStopPrinterStateTracking = JavaMethod("(Landroid/print/PrinterId;)V")
    isDestroyed = JavaMethod("()Z")
    onDestroy = JavaMethod("()V")