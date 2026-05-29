from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentCaptureManager"]

class ContentCaptureManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/ContentCaptureManager"
    DATA_SHARE_ERROR_CONCURRENT_REQUEST = JavaStaticField("I")
    DATA_SHARE_ERROR_TIMEOUT_INTERRUPTED = JavaStaticField("I")
    DATA_SHARE_ERROR_UNKNOWN = JavaStaticField("I")
    removeData = JavaMethod("(Landroid/view/contentcapture/DataRemovalRequest;)V")
    shareData = JavaMethod("(Landroid/view/contentcapture/DataShareRequest;Ljava/util/concurrent/Executor;Landroid/view/contentcapture/DataShareWriteAdapter;)V")
    getContentCaptureConditions = JavaMethod("()Ljava/util/Set;")
    getServiceComponentName = JavaMethod("()Landroid/content/ComponentName;")
    isContentCaptureEnabled = JavaMethod("()Z")
    setContentCaptureEnabled = JavaMethod("(Z)V")