from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaDrmThrowable"]

class MediaDrmThrowable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaDrmThrowable"
    getOemError = JavaMethod("()I")
    getErrorContext = JavaMethod("()I")
    getVendorError = JavaMethod("()I")