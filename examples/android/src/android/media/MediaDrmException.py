from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaDrmException"]

class MediaDrmException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaDrmException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getVendorError = JavaMethod("()I")
    getOemError = JavaMethod("()I")
    getErrorContext = JavaMethod("()I")