from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IpSecManager"]

class IpSecManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/IpSecManager"
    DIRECTION_IN = JavaStaticField("I")
    DIRECTION_OUT = JavaStaticField("I")
    allocateSecurityParameterIndex = JavaMultipleMethod([("(Ljava/net/InetAddress;)Landroid/net/IpSecManager$SecurityParameterIndex;", False, False), ("(Ljava/net/InetAddress;I)Landroid/net/IpSecManager$SecurityParameterIndex;", False, False)])
    applyTransportModeTransform = JavaMultipleMethod([("(Ljava/net/Socket;ILandroid/net/IpSecTransform;)V", False, False), ("(Ljava/net/DatagramSocket;ILandroid/net/IpSecTransform;)V", False, False), ("(Ljava/io/FileDescriptor;ILandroid/net/IpSecTransform;)V", False, False)])
    removeTransportModeTransforms = JavaMultipleMethod([("(Ljava/net/Socket;)V", False, False), ("(Ljava/net/DatagramSocket;)V", False, False), ("(Ljava/io/FileDescriptor;)V", False, False)])
    openUdpEncapsulationSocket = JavaMultipleMethod([("(I)Landroid/net/IpSecManager$UdpEncapsulationSocket;", False, False), ("()Landroid/net/IpSecManager$UdpEncapsulationSocket;", False, False)])

    class ResourceUnavailableException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/IpSecManager/ResourceUnavailableException"

    class SecurityParameterIndex(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/IpSecManager/SecurityParameterIndex"
        getSpi = JavaMethod("()I")
        close = JavaMethod("()V")
        finalize = JavaMethod("()V")
        toString = JavaMethod("()Ljava/lang/String;")

    class SpiUnavailableException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/IpSecManager/SpiUnavailableException"
        getSpi = JavaMethod("()I")

    class UdpEncapsulationSocket(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/IpSecManager/UdpEncapsulationSocket"
        getFileDescriptor = JavaMethod("()Ljava/io/FileDescriptor;")
        getPort = JavaMethod("()I")
        close = JavaMethod("()V")
        finalize = JavaMethod("()V")
        toString = JavaMethod("()Ljava/lang/String;")