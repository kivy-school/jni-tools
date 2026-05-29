from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UploadDataProvider"]

class UploadDataProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/UploadDataProvider"
    __javaconstructor__ = [("()V", False)]
    getLength = JavaMethod("()J")
    close = JavaMethod("()V")
    read = JavaMethod("(Landroid/net/http/UploadDataSink;Ljava/nio/ByteBuffer;)V")
    rewind = JavaMethod("(Landroid/net/http/UploadDataSink;)V")