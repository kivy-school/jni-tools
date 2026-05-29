from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentCaptureManager"]

class ContentCaptureManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/ContentCaptureManager"
    DATA_SHARE_ERROR_CONCURRENT_REQUEST = JavaStaticField("I")
    DATA_SHARE_ERROR_TIMEOUT_INTERRUPTED = JavaStaticField("I")
    DATA_SHARE_ERROR_UNKNOWN = JavaStaticField("I")
    getServiceComponentName = JavaMethod("()Landroid/content/ComponentName;")
    isContentCaptureEnabled = JavaMethod("()Z")
    getContentCaptureConditions = JavaMethod("()Ljava/util/Set;")
    setContentCaptureEnabled = JavaMethod("(Z)V")
    removeData = JavaMethod("(Landroid/view/contentcapture/DataRemovalRequest;)V")
    shareData = JavaMethod("(Landroid/view/contentcapture/DataShareRequest;Ljava/util/concurrent/Executor;Landroid/view/contentcapture/DataShareWriteAdapter;)V")