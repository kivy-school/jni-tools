from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UploadDataSink"]

class UploadDataSink(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/UploadDataSink"
    __javaconstructor__ = [("()V", False)]
    onReadError = JavaMethod("(Ljava/lang/Exception;)V")
    onRewindError = JavaMethod("(Ljava/lang/Exception;)V")
    onReadSucceeded = JavaMethod("(Z)V")
    onRewindSucceeded = JavaMethod("()V")