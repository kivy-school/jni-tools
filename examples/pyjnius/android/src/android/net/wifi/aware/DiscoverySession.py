from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DiscoverySession"]

class DiscoverySession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/DiscoverySession"
    createNetworkSpecifierOpen = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;)Landroid/net/NetworkSpecifier;")
    createNetworkSpecifierPassphrase = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;Ljava/lang/String;)Landroid/net/NetworkSpecifier;")
    initiateBootstrappingRequest = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;I)V")
    initiatePairingRequest = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;Ljava/lang/String;ILjava/lang/String;)V")
    acceptPairingRequest = JavaMethod("(ILandroid/net/wifi/aware/PeerHandle;Ljava/lang/String;ILjava/lang/String;)V")
    rejectPairingRequest = JavaMethod("(ILandroid/net/wifi/aware/PeerHandle;)V")
    close = JavaMethod("()V")
    sendMessage = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;I[B)V")