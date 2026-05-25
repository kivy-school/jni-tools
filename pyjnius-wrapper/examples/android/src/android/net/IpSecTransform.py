from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IpSecTransform"]

class IpSecTransform(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/IpSecTransform"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    close = JavaMethod("()V")
    finalize = JavaMethod("()V")
    requestIpSecTransformState = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/IpSecTransform/Builder"
        __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
        setEncryption = JavaMethod("(Landroid/net/IpSecAlgorithm;)Landroid/net/IpSecTransform$Builder;")
        setAuthentication = JavaMethod("(Landroid/net/IpSecAlgorithm;)Landroid/net/IpSecTransform$Builder;")
        setAuthenticatedEncryption = JavaMethod("(Landroid/net/IpSecAlgorithm;)Landroid/net/IpSecTransform$Builder;")
        setIpv4Encapsulation = JavaMethod("(Landroid/net/IpSecManager$UdpEncapsulationSocket;I)Landroid/net/IpSecTransform$Builder;")
        buildTransportModeTransform = JavaMethod("(Ljava/net/InetAddress;Landroid/net/IpSecManager$SecurityParameterIndex;)Landroid/net/IpSecTransform;")