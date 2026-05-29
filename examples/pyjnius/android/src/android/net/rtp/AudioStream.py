from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioStream"]

class AudioStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/rtp/AudioStream"
    __javaconstructor__ = [("(Ljava/net/InetAddress;)V", False)]
    MODE_NORMAL = JavaStaticField("I")
    MODE_RECEIVE_ONLY = JavaStaticField("I")
    MODE_SEND_ONLY = JavaStaticField("I")
    setDtmfType = JavaMethod("(I)V")
    getCodec = JavaMethod("()Landroid/net/rtp/AudioCodec;")
    setCodec = JavaMethod("(Landroid/net/rtp/AudioCodec;)V")
    getDtmfType = JavaMethod("()I")
    isBusy = JavaMethod("()Z")
    join = JavaMethod("(Landroid/net/rtp/AudioGroup;)V")
    getGroup = JavaMethod("()Landroid/net/rtp/AudioGroup;")