from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ModelDownloadListener"]

class ModelDownloadListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/ModelDownloadListener"
    onProgress = JavaMethod("(I)V")
    onSuccess = JavaMethod("()V")
    onScheduled = JavaMethod("()V")
    onError = JavaMethod("(I)V")