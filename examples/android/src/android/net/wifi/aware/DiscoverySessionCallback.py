from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DiscoverySessionCallback"]

class DiscoverySessionCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/DiscoverySessionCallback"
    __javaconstructor__ = [("()V", False)]
    onPublishStarted = JavaMethod("(Landroid/net/wifi/aware/PublishDiscoverySession;)V")
    onSubscribeStarted = JavaMethod("(Landroid/net/wifi/aware/SubscribeDiscoverySession;)V")
    onSessionConfigUpdated = JavaMethod("()V")
    onSessionConfigFailed = JavaMethod("()V")
    onSessionTerminated = JavaMethod("()V")
    onServiceDiscovered = JavaMultipleMethod([("(Landroid/net/wifi/aware/PeerHandle;[BLjava/util/List;)V", False, False), ("(Landroid/net/wifi/aware/ServiceDiscoveryInfo;)V", False, False)])
    onServiceDiscoveredWithinRange = JavaMultipleMethod([("(Landroid/net/wifi/aware/PeerHandle;[BLjava/util/List;I)V", False, False), ("(Landroid/net/wifi/aware/ServiceDiscoveryInfo;I)V", False, False)])
    onMessageSendSucceeded = JavaMethod("(I)V")
    onMessageSendFailed = JavaMethod("(I)V")
    onMessageReceived = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;[B)V")
    onServiceLost = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;I)V")
    onPairingSetupRequestReceived = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;I)V")
    onPairingSetupSucceeded = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;Ljava/lang/String;)V")
    onPairingSetupFailed = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;)V")
    onPairingVerificationSucceed = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;Ljava/lang/String;)V")
    onPairingVerificationFailed = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;)V")
    onBootstrappingSucceeded = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;I)V")
    onBootstrappingFailed = JavaMethod("(Landroid/net/wifi/aware/PeerHandle;)V")