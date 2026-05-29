from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioCodec"]

class AudioCodec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/rtp/AudioCodec"
    AMR = JavaStaticField("Landroid/net/rtp/AudioCodec;")
    GSM = JavaStaticField("Landroid/net/rtp/AudioCodec;")
    GSM_EFR = JavaStaticField("Landroid/net/rtp/AudioCodec;")
    PCMA = JavaStaticField("Landroid/net/rtp/AudioCodec;")
    PCMU = JavaStaticField("Landroid/net/rtp/AudioCodec;")
    fmtp = JavaField("Ljava/lang/String;")
    rtpmap = JavaField("Ljava/lang/String;")
    type = JavaField("I")
    getCodec = JavaStaticMethod("(ILjava/lang/String;Ljava/lang/String;)Landroid/net/rtp/AudioCodec;")
    getCodecs = JavaStaticMethod("()[Landroid/net/rtp/AudioCodec;")