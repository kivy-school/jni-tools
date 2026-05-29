from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DiscoverySession"]

class DiscoverySession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/DiscoverySession"
    close = JavaMethod("()V")
    finalize = JavaMethod("()V")
    sendMessage = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;I[B)V")
    initiatePairingRequest = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;Ljava/lang/String;ILjava/lang/String;)V")
    acceptPairingRequest = JavaMethod("(ILandroid/net/wifi/aware/PeerHandle;Ljava/lang/String;ILjava/lang/String;)V")
    rejectPairingRequest = JavaMethod("(ILandroid/net/wifi/aware/PeerHandle;)V")
    initiateBootstrappingRequest = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;I)V")
    createNetworkSpecifierOpen = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;)Landroid/net/NetworkSpecifier;")
    createNetworkSpecifierPassphrase = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;Ljava/lang/String;)Landroid/net/NetworkSpecifier;")