from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaDrmThrowable"]

class MediaDrmThrowable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaDrmThrowable"
    getVendorError = JavaMethod("()I")
    getOemError = JavaMethod("()I")
    getErrorContext = JavaMethod("()I")