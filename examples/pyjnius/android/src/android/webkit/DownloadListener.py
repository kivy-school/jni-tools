from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DownloadListener"]

class DownloadListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/DownloadListener"
    onDownloadStart = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;J)V")