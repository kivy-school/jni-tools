from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaCrypto"]

class MediaCrypto(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaCrypto"
    __javaconstructor__ = [("(Ljava/util/UUID;[B)V", False)]
    isCryptoSchemeSupported = JavaStaticMethod("(Ljava/util/UUID;)Z")
    requiresSecureDecoderComponent = JavaMethod("(Ljava/lang/String;)Z")
    setMediaDrmSession = JavaMethod("([B)V")
    finalize = JavaMethod("()V")
    release = JavaMethod("()V")