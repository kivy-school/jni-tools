from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MbmsDownloadSessionCallback"]

class MbmsDownloadSessionCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/MbmsDownloadSessionCallback"
    __javaconstructor__ = [("()V", False)]
    onError = JavaMethod("(ILjava/lang/String;)V")
    onFileServicesUpdated = JavaMethod("(Ljava/util/List;)V")
    onMiddlewareReady = JavaMethod("()V")