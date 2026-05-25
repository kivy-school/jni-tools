from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VpnService"]

class VpnService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/VpnService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    SERVICE_META_DATA_SUPPORTS_ALWAYS_ON = JavaStaticField("Ljava/lang/String;")
    prepare = JavaStaticMethod("(Landroid/content/Context;)Landroid/content/Intent;")
    protect = JavaMultipleMethod([("(I)Z", False, False), ("(Ljava/net/Socket;)Z", False, False), ("(Ljava/net/DatagramSocket;)Z", False, False)])
    setUnderlyingNetworks = JavaMethod("([Landroid/net/Network;)Z")
    isAlwaysOn = JavaMethod("()Z")
    isLockdownEnabled = JavaMethod("()Z")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onRevoke = JavaMethod("()V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/VpnService/Builder"
        __javaconstructor__ = [("(Landroid/net/VpnService;)V", False)]
        setSession = JavaMethod("(Ljava/lang/String;)Landroid/net/VpnService$Builder;")
        setConfigureIntent = JavaMethod("(Landroid/app/PendingIntent;)Landroid/net/VpnService$Builder;")
        setMtu = JavaMethod("(I)Landroid/net/VpnService$Builder;")
        setHttpProxy = JavaMethod("(Landroid/net/ProxyInfo;)Landroid/net/VpnService$Builder;")
        addAddress = JavaMultipleMethod([("(Ljava/net/InetAddress;I)Landroid/net/VpnService$Builder;", False, False), ("(Ljava/lang/String;I)Landroid/net/VpnService$Builder;", False, False)])
        addRoute = JavaMultipleMethod([("(Ljava/net/InetAddress;I)Landroid/net/VpnService$Builder;", False, False), ("(Landroid/net/IpPrefix;)Landroid/net/VpnService$Builder;", False, False), ("(Ljava/lang/String;I)Landroid/net/VpnService$Builder;", False, False)])
        excludeRoute = JavaMethod("(Landroid/net/IpPrefix;)Landroid/net/VpnService$Builder;")
        addDnsServer = JavaMultipleMethod([("(Ljava/net/InetAddress;)Landroid/net/VpnService$Builder;", False, False), ("(Ljava/lang/String;)Landroid/net/VpnService$Builder;", False, False)])
        addSearchDomain = JavaMethod("(Ljava/lang/String;)Landroid/net/VpnService$Builder;")
        allowFamily = JavaMethod("(I)Landroid/net/VpnService$Builder;")
        addAllowedApplication = JavaMethod("(Ljava/lang/String;)Landroid/net/VpnService$Builder;")
        addDisallowedApplication = JavaMethod("(Ljava/lang/String;)Landroid/net/VpnService$Builder;")
        allowBypass = JavaMethod("()Landroid/net/VpnService$Builder;")
        setBlocking = JavaMethod("(Z)Landroid/net/VpnService$Builder;")
        setUnderlyingNetworks = JavaMethod("([Landroid/net/Network;)Landroid/net/VpnService$Builder;")
        setMetered = JavaMethod("(Z)Landroid/net/VpnService$Builder;")
        establish = JavaMethod("()Landroid/os/ParcelFileDescriptor;")