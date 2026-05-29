from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaCryptoException"]

class MediaCryptoException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaCryptoException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getOemError = JavaMethod("()I")
    getErrorContext = JavaMethod("()I")
    getVendorError = JavaMethod("()I")