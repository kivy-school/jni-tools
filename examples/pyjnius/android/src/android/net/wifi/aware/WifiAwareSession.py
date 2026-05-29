from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiAwareSession"]

class WifiAwareSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/WifiAwareSession"
    createNetworkSpecifierOpen = JavaMethod("(I[B)Landroid/net/NetworkSpecifier;")
    createNetworkSpecifierPassphrase = JavaMethod("(I[BLjava/lang/String;)Landroid/net/NetworkSpecifier;")
    close = JavaMethod("()V")
    publish = JavaMethod("(Landroid/net/wifi/aware/PublishConfig;Landroid/net/wifi/aware/DiscoverySessionCallback;Landroid/os/Handler;)V")
    subscribe = JavaMethod("(Landroid/net/wifi/aware/SubscribeConfig;Landroid/net/wifi/aware/DiscoverySessionCallback;Landroid/os/Handler;)V")