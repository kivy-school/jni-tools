from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaDrmException"]

class MediaDrmException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaDrmException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getOemError = JavaMethod("()I")
    getErrorContext = JavaMethod("()I")
    getVendorError = JavaMethod("()I")