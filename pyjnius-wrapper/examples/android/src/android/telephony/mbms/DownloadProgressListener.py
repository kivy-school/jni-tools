from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DownloadProgressListener"]

class DownloadProgressListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/DownloadProgressListener"
    __javaconstructor__ = [("()V", False)]
    onProgressUpdated = JavaMethod("(Landroid/telephony/mbms/DownloadRequest;Landroid/telephony/mbms/FileInfo;IIII)V")