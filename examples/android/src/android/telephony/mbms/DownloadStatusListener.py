from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DownloadStatusListener"]

class DownloadStatusListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/DownloadStatusListener"
    __javaconstructor__ = [("()V", False)]
    onStatusUpdated = JavaMethod("(Landroid/telephony/mbms/DownloadRequest;Landroid/telephony/mbms/FileInfo;I)V")