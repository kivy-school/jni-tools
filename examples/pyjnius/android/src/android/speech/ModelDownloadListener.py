from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ModelDownloadListener"]

class ModelDownloadListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/ModelDownloadListener"
    onError = JavaMethod("(I)V")
    onProgress = JavaMethod("(I)V")
    onScheduled = JavaMethod("()V")
    onSuccess = JavaMethod("()V")