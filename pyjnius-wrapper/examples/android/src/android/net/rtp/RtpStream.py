from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RtpStream"]

class RtpStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/rtp/RtpStream"
    MODE_NORMAL = JavaStaticField("I")
    MODE_RECEIVE_ONLY = JavaStaticField("I")
    MODE_SEND_ONLY = JavaStaticField("I")
    getLocalAddress = JavaMethod("()Ljava/net/InetAddress;")
    getLocalPort = JavaMethod("()I")
    getRemoteAddress = JavaMethod("()Ljava/net/InetAddress;")
    getRemotePort = JavaMethod("()I")
    isBusy = JavaMethod("()Z")
    getMode = JavaMethod("()I")
    setMode = JavaMethod("(I)V")
    associate = JavaMethod("(Ljava/net/InetAddress;I)V")
    release = JavaMethod("()V")
    finalize = JavaMethod("()V")