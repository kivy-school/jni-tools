from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintService"]

class PrintService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/printservice/PrintService"
    __javaconstructor__ = [("()V", False)]
    EXTRA_CAN_SELECT_PRINTER = JavaStaticField("Ljava/lang/String;")
    EXTRA_PRINTER_INFO = JavaStaticField("Ljava/lang/String;")
    EXTRA_PRINT_DOCUMENT_INFO = JavaStaticField("Ljava/lang/String;")
    EXTRA_PRINT_JOB_INFO = JavaStaticField("Ljava/lang/String;")
    EXTRA_SELECT_PRINTER = JavaStaticField("Ljava/lang/String;")
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    SERVICE_META_DATA = JavaStaticField("Ljava/lang/String;")
    attachBaseContext = JavaMethod("(Landroid/content/Context;)V")
    onConnected = JavaMethod("()V")
    onDisconnected = JavaMethod("()V")
    onCreatePrinterDiscoverySession = JavaMethod("()Landroid/printservice/PrinterDiscoverySession;")
    onRequestCancelPrintJob = JavaMethod("(Landroid/printservice/PrintJob;)V")
    onPrintJobQueued = JavaMethod("(Landroid/printservice/PrintJob;)V")
    getActivePrintJobs = JavaMethod("()Ljava/util/List;")
    generatePrinterId = JavaMethod("(Ljava/lang/String;)Landroid/print/PrinterId;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")