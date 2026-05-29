from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RtpStream"]

class RtpStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/rtp/RtpStream"
    MODE_NORMAL = JavaStaticField("I")
    MODE_RECEIVE_ONLY = JavaStaticField("I")
    MODE_SEND_ONLY = JavaStaticField("I")
    associate = JavaMethod("(Ljava/net/InetAddress;I)V")
    isBusy = JavaMethod("()Z")
    getRemoteAddress = JavaMethod("()Ljava/net/InetAddress;")
    getRemotePort = JavaMethod("()I")
    release = JavaMethod("()V")
    getMode = JavaMethod("()I")
    setMode = JavaMethod("(I)V")
    getLocalAddress = JavaMethod("()Ljava/net/InetAddress;")
    getLocalPort = JavaMethod("()I")