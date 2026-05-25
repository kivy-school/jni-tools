from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiAwareManager"]

class WifiAwareManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/WifiAwareManager"
    ACTION_WIFI_AWARE_RESOURCE_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_WIFI_AWARE_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    EXTRA_AWARE_RESOURCES = JavaStaticField("Ljava/lang/String;")
    WIFI_AWARE_DATA_PATH_ROLE_INITIATOR = JavaStaticField("I")
    WIFI_AWARE_DATA_PATH_ROLE_RESPONDER = JavaStaticField("I")
    WIFI_AWARE_DISCOVERY_LOST_REASON_PEER_NOT_VISIBLE = JavaStaticField("I")
    WIFI_AWARE_DISCOVERY_LOST_REASON_UNKNOWN = JavaStaticField("I")
    isAvailable = JavaMethod("()Z")
    isDeviceAttached = JavaMethod("()Z")
    isSetChannelOnDataPathSupported = JavaMethod("()Z")
    isInstantCommunicationModeEnabled = JavaMethod("()Z")
    getCharacteristics = JavaMethod("()Landroid/net/wifi/aware/Characteristics;")
    getAvailableAwareResources = JavaMethod("()Landroid/net/wifi/aware/AwareResources;")
    attach = JavaMultipleMethod([("(Landroid/net/wifi/aware/AttachCallback;Landroid/os/Handler;)V", False, False), ("(Landroid/net/wifi/aware/AttachCallback;Landroid/net/wifi/aware/IdentityChangedListener;Landroid/os/Handler;)V", False, False)])
    setOpportunisticModeEnabled = JavaMethod("(Z)V")
    isOpportunisticModeEnabled = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    resetPairedDevices = JavaMethod("()V")
    removePairedDevice = JavaMethod("(Ljava/lang/String;)V")
    getPairedDevices = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")