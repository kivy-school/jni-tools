from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaDataSource"]

class MediaDataSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaDataSource"
    __javaconstructor__ = [("()V", False)]
    getSize = JavaMethod("()J")
    readAt = JavaMethod("(J[BII)I")