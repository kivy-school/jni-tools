from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MbmsDownloadSessionCallback"]

class MbmsDownloadSessionCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/MbmsDownloadSessionCallback"
    __javaconstructor__ = [("()V", False)]
    onMiddlewareReady = JavaMethod("()V")
    onFileServicesUpdated = JavaMethod("(Ljava/util/List;)V")
    onError = JavaMethod("(ILjava/lang/String;)V")