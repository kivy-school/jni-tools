from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaDataSource"]

class MediaDataSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaDataSource"
    __javaconstructor__ = [("()V", False)]
    readAt = JavaMethod("(J[BII)I")
    getSize = JavaMethod("()J")