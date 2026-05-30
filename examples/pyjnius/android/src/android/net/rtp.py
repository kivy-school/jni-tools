from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AudioGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/rtp/AudioGroup"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;)V", False)]
    MODE_ECHO_SUPPRESSION = JavaStaticField("I")
    MODE_MUTED = JavaStaticField("I")
    MODE_NORMAL = JavaStaticField("I")
    MODE_ON_HOLD = JavaStaticField("I")
    getStreams = JavaMethod("()[Landroid/net/rtp/AudioStream;")
    sendDtmf = JavaMethod("(I)V")
    clear = JavaMethod("()V")
    getMode = JavaMethod("()I")
    setMode = JavaMethod("(I)V")

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

class RtpStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/rtp/RtpStream"
    MODE_NORMAL = JavaStaticField("I")
    MODE_RECEIVE_ONLY = JavaStaticField("I")
    MODE_SEND_ONLY = JavaStaticField("I")
    associate = JavaMethod("(Ljava/net/InetAddress;I)V")
    isBusy = JavaMethod("()Z")
    getRemoteAddress = JavaMethod("()Ljava/net/InetAddress;")
    getRemotePort = JavaMethod("()I")
    getMode = JavaMethod("()I")
    setMode = JavaMethod("(I)V")
    release = JavaMethod("()V")
    getLocalAddress = JavaMethod("()Ljava/net/InetAddress;")
    getLocalPort = JavaMethod("()I")

class AudioStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/rtp/AudioStream"
    __javaconstructor__ = [("(Ljava/net/InetAddress;)V", False)]
    MODE_NORMAL = JavaStaticField("I")
    MODE_RECEIVE_ONLY = JavaStaticField("I")
    MODE_SEND_ONLY = JavaStaticField("I")
    isBusy = JavaMethod("()Z")
    getCodec = JavaMethod("()Landroid/net/rtp/AudioCodec;")
    getDtmfType = JavaMethod("()I")
    setCodec = JavaMethod("(Landroid/net/rtp/AudioCodec;)V")
    setDtmfType = JavaMethod("(I)V")
    join = JavaMethod("(Landroid/net/rtp/AudioGroup;)V")
    getGroup = JavaMethod("()Landroid/net/rtp/AudioGroup;")