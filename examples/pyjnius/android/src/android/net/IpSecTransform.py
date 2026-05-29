from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IpSecTransform"]

class IpSecTransform(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/IpSecTransform"
    requestIpSecTransformState = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    close = JavaMethod("()V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/IpSecTransform$Builder"
        __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
        setAuthentication = JavaMethod("(Landroid/net/IpSecAlgorithm;)Landroid/net/IpSecTransform$Builder;")
        setEncryption = JavaMethod("(Landroid/net/IpSecAlgorithm;)Landroid/net/IpSecTransform$Builder;")
        buildTransportModeTransform = JavaMethod("(Ljava/net/InetAddress;Landroid/net/IpSecManager$SecurityParameterIndex;)Landroid/net/IpSecTransform;")
        setAuthenticatedEncryption = JavaMethod("(Landroid/net/IpSecAlgorithm;)Landroid/net/IpSecTransform$Builder;")
        setIpv4Encapsulation = JavaMethod("(Landroid/net/IpSecManager$UdpEncapsulationSocket;I)Landroid/net/IpSecTransform$Builder;")