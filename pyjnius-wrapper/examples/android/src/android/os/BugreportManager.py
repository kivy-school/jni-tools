from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BugreportManager"]

class BugreportManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/BugreportManager"
    startConnectivityBugreport = JavaMethod("(Landroid/os/ParcelFileDescriptor;Ljava/util/concurrent/Executor;Landroid/os/BugreportManager$BugreportCallback;)V")
    cancelBugreport = JavaMethod("()V")

    class BugreportCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/BugreportManager/BugreportCallback"
        __javaconstructor__ = [("()V", False)]
        BUGREPORT_ERROR_ANOTHER_REPORT_IN_PROGRESS = JavaStaticField("I")
        BUGREPORT_ERROR_INVALID_INPUT = JavaStaticField("I")
        BUGREPORT_ERROR_NO_BUGREPORT_TO_RETRIEVE = JavaStaticField("I")
        BUGREPORT_ERROR_RUNTIME = JavaStaticField("I")
        BUGREPORT_ERROR_USER_CONSENT_TIMED_OUT = JavaStaticField("I")
        BUGREPORT_ERROR_USER_DENIED_CONSENT = JavaStaticField("I")
        onProgress = JavaMethod("(F)V")
        onError = JavaMethod("(I)V")
        onFinished = JavaMethod("()V")
        onEarlyReportFinished = JavaMethod("()V")