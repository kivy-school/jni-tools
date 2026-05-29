from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IpSecManager"]

class IpSecManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/IpSecManager"
    DIRECTION_IN = JavaStaticField("I")
    DIRECTION_OUT = JavaStaticField("I")
    openUdpEncapsulationSocket = JavaMultipleMethod([("(I)Landroid/net/IpSecManager$UdpEncapsulationSocket;", False, False), ("()Landroid/net/IpSecManager$UdpEncapsulationSocket;", False, False)])
    allocateSecurityParameterIndex = JavaMultipleMethod([("(Ljava/net/InetAddress;I)Landroid/net/IpSecManager$SecurityParameterIndex;", False, False), ("(Ljava/net/InetAddress;)Landroid/net/IpSecManager$SecurityParameterIndex;", False, False)])
    applyTransportModeTransform = JavaMultipleMethod([("(Ljava/net/DatagramSocket;ILandroid/net/IpSecTransform;)V", False, False), ("(Ljava/net/Socket;ILandroid/net/IpSecTransform;)V", False, False), ("(Ljava/io/FileDescriptor;ILandroid/net/IpSecTransform;)V", False, False)])
    removeTransportModeTransforms = JavaMultipleMethod([("(Ljava/io/FileDescriptor;)V", False, False), ("(Ljava/net/DatagramSocket;)V", False, False), ("(Ljava/net/Socket;)V", False, False)])

    class UdpEncapsulationSocket(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/IpSecManager$UdpEncapsulationSocket"
        toString = JavaMethod("()Ljava/lang/String;")
        close = JavaMethod("()V")
        getPort = JavaMethod("()I")
        getFileDescriptor = JavaMethod("()Ljava/io/FileDescriptor;")

    class SpiUnavailableException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/IpSecManager$SpiUnavailableException"
        getSpi = JavaMethod("()I")

    class SecurityParameterIndex(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/IpSecManager$SecurityParameterIndex"
        getSpi = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")
        close = JavaMethod("()V")

    class ResourceUnavailableException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/IpSecManager$ResourceUnavailableException"