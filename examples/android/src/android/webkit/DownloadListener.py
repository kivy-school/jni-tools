from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DownloadListener"]

class DownloadListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/DownloadListener"
    onDownloadStart = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;J)V")