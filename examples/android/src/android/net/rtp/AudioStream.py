from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioStream"]

class AudioStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/rtp/AudioStream"
    __javaconstructor__ = [("(Ljava/net/InetAddress;)V", False)]
    isBusy = JavaMethod("()Z")
    getGroup = JavaMethod("()Landroid/net/rtp/AudioGroup;")
    join = JavaMethod("(Landroid/net/rtp/AudioGroup;)V")
    getCodec = JavaMethod("()Landroid/net/rtp/AudioCodec;")
    setCodec = JavaMethod("(Landroid/net/rtp/AudioCodec;)V")
    getDtmfType = JavaMethod("()I")
    setDtmfType = JavaMethod("(I)V")