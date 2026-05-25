from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UploadDataSink"]

class UploadDataSink(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/UploadDataSink"
    __javaconstructor__ = [("()V", False)]
    onReadSucceeded = JavaMethod("(Z)V")
    onReadError = JavaMethod("(Ljava/lang/Exception;)V")
    onRewindSucceeded = JavaMethod("()V")
    onRewindError = JavaMethod("(Ljava/lang/Exception;)V")