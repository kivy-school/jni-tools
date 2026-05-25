from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaDescrambler"]

class MediaDescrambler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaDescrambler"
    __javaconstructor__ = [("(I)V", False)]
    SCRAMBLE_CONTROL_EVEN_KEY = JavaStaticField("B")
    SCRAMBLE_CONTROL_ODD_KEY = JavaStaticField("B")
    SCRAMBLE_CONTROL_RESERVED = JavaStaticField("B")
    SCRAMBLE_CONTROL_UNSCRAMBLED = JavaStaticField("B")
    SCRAMBLE_FLAG_PES_HEADER = JavaStaticField("B")
    requiresSecureDecoderComponent = JavaMethod("(Ljava/lang/String;)Z")
    setMediaCasSession = JavaMethod("(Landroid/media/MediaCas$Session;)V")
    descramble = JavaMethod("(Ljava/nio/ByteBuffer;Ljava/nio/ByteBuffer;Landroid/media/MediaCodec$CryptoInfo;)I")
    close = JavaMethod("()V")
    finalize = JavaMethod("()V")