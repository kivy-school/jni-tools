from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pManager"]

class WifiP2pManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/WifiP2pManager"
    ACTION_WIFI_P2P_LISTEN_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_WIFI_P2P_REQUEST_RESPONSE_CHANGED = JavaStaticField("Ljava/lang/String;")
    BUSY = JavaStaticField("I")
    CONNECTION_REQUEST_ACCEPT = JavaStaticField("I")
    CONNECTION_REQUEST_DEFER_SHOW_PIN_TO_SERVICE = JavaStaticField("I")
    CONNECTION_REQUEST_DEFER_TO_SERVICE = JavaStaticField("I")
    CONNECTION_REQUEST_REJECT = JavaStaticField("I")
    ERROR = JavaStaticField("I")
    EXTRA_DISCOVERY_STATE = JavaStaticField("Ljava/lang/String;")
    EXTRA_LISTEN_STATE = JavaStaticField("Ljava/lang/String;")
    EXTRA_NETWORK_INFO = JavaStaticField("Ljava/lang/String;")
    EXTRA_P2P_DEVICE_LIST = JavaStaticField("Ljava/lang/String;")
    EXTRA_REQUEST_CONFIG = JavaStaticField("Ljava/lang/String;")
    EXTRA_REQUEST_RESPONSE = JavaStaticField("Ljava/lang/String;")
    EXTRA_WIFI_P2P_DEVICE = JavaStaticField("Ljava/lang/String;")
    EXTRA_WIFI_P2P_GROUP = JavaStaticField("Ljava/lang/String;")
    EXTRA_WIFI_P2P_INFO = JavaStaticField("Ljava/lang/String;")
    EXTRA_WIFI_STATE = JavaStaticField("Ljava/lang/String;")
    GROUP_CREATION_FAILURE_REASON_CONNECTION_CANCELLED = JavaStaticField("I")
    GROUP_CREATION_FAILURE_REASON_GROUP_REMOVED = JavaStaticField("I")
    GROUP_CREATION_FAILURE_REASON_INVITATION_FAILED = JavaStaticField("I")
    GROUP_CREATION_FAILURE_REASON_PROVISION_DISCOVERY_FAILED = JavaStaticField("I")
    GROUP_CREATION_FAILURE_REASON_TIMED_OUT = JavaStaticField("I")
    GROUP_CREATION_FAILURE_REASON_USER_REJECTED = JavaStaticField("I")
    NO_PERMISSION = JavaStaticField("I")
    NO_SERVICE_REQUESTS = JavaStaticField("I")
    P2P_UNSUPPORTED = JavaStaticField("I")
    WIFI_P2P_CONNECTION_CHANGED_ACTION = JavaStaticField("Ljava/lang/String;")
    WIFI_P2P_DISCOVERY_CHANGED_ACTION = JavaStaticField("Ljava/lang/String;")
    WIFI_P2P_DISCOVERY_STARTED = JavaStaticField("I")
    WIFI_P2P_DISCOVERY_STOPPED = JavaStaticField("I")
    WIFI_P2P_LISTEN_STARTED = JavaStaticField("I")
    WIFI_P2P_LISTEN_STOPPED = JavaStaticField("I")
    WIFI_P2P_PEERS_CHANGED_ACTION = JavaStaticField("Ljava/lang/String;")
    WIFI_P2P_SCAN_FULL = JavaStaticField("I")
    WIFI_P2P_SCAN_SINGLE_FREQ = JavaStaticField("I")
    WIFI_P2P_SCAN_SOCIAL = JavaStaticField("I")
    WIFI_P2P_STATE_CHANGED_ACTION = JavaStaticField("Ljava/lang/String;")
    WIFI_P2P_STATE_DISABLED = JavaStaticField("I")
    WIFI_P2P_STATE_ENABLED = JavaStaticField("I")
    WIFI_P2P_THIS_DEVICE_CHANGED_ACTION = JavaStaticField("Ljava/lang/String;")
    connect = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pConfig;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    discoverServices = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    addExternalApprover = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/MacAddress;Landroid/net/wifi/p2p/WifiP2pManager$ExternalApproverRequestListener;)V")
    addLocalService = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/nsd/WifiP2pServiceInfo;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    addServiceRequest = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/nsd/WifiP2pServiceRequest;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    cancelConnect = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    clearLocalServices = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    clearServiceRequests = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    discoverPeers = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    discoverPeersOnSocialChannels = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    discoverPeersOnSpecificFrequency = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;ILandroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    discoverUsdBasedServices = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pUsdBasedServiceDiscoveryConfig;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    getListenState = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getP2pMaxAllowedVendorElementsLengthBytes = JavaStaticMethod("()I")
    isChannelConstrainedDiscoverySupported = JavaMethod("()Z")
    isGroupClientRemovalSupported = JavaMethod("()Z")
    isGroupOwnerIPv6LinkLocalAddressProvided = JavaMethod("()Z")
    isPccModeSupported = JavaMethod("()Z")
    isSetVendorElementsSupported = JavaMethod("()Z")
    isWiFiDirectR2Supported = JavaMethod("()Z")
    registerWifiP2pListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/net/wifi/p2p/WifiP2pManager$WifiP2pListener;)V")
    removeClient = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/MacAddress;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    removeExternalApprover = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/MacAddress;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    removeLocalService = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/nsd/WifiP2pServiceInfo;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    removeServiceRequest = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/nsd/WifiP2pServiceRequest;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    requestConnectionInfo = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$ConnectionInfoListener;)V")
    requestDeviceInfo = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$DeviceInfoListener;)V")
    requestDirInfo = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    requestDiscoveryState = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$DiscoveryStateListener;)V")
    requestGroupInfo = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$GroupInfoListener;)V")
    requestNetworkInfo = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$NetworkInfoListener;)V")
    requestP2pState = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$P2pStateListener;)V")
    requestPeers = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$PeerListListener;)V")
    setConnectionRequestResult = JavaMultipleMethod([("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/MacAddress;ILjava/lang/String;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V", False, False), ("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/MacAddress;ILandroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V", False, False)])
    setDnsSdResponseListeners = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$DnsSdServiceResponseListener;Landroid/net/wifi/p2p/WifiP2pManager$DnsSdTxtRecordListener;)V")
    setServiceResponseListener = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$ServiceResponseListener;)V")
    setUpnpServiceResponseListener = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$UpnpServiceResponseListener;)V")
    setVendorElements = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Ljava/util/List;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    setWfdInfo = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pWfdInfo;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    startPeerDiscovery = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pDiscoveryConfig;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    startUsdBasedLocalServiceAdvertisement = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/nsd/WifiP2pServiceInfo;Landroid/net/wifi/p2p/WifiP2pUsdBasedLocalServiceAdvertisementConfig;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    stopPeerDiscovery = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    unregisterWifiP2pListener = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$WifiP2pListener;)V")
    validateDirInfo = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pDirInfo;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    createGroup = JavaMultipleMethod([("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V", False, False), ("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pConfig;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V", False, False)])
    initialize = JavaMethod("(Landroid/content/Context;Landroid/os/Looper;Landroid/net/wifi/p2p/WifiP2pManager$ChannelListener;)Landroid/net/wifi/p2p/WifiP2pManager$Channel;")
    startListening = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    stopListening = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")
    removeGroup = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pManager$Channel;Landroid/net/wifi/p2p/WifiP2pManager$ActionListener;)V")

    class WifiP2pListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$WifiP2pListener"
        onFrequencyChanged = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pInfo;Landroid/net/wifi/p2p/WifiP2pGroup;)V")
        onDeviceConfigurationChanged = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pDevice;)V")
        onDiscoveryStateChanged = JavaMethod("(I)V")
        onGroupCreated = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pInfo;Landroid/net/wifi/p2p/WifiP2pGroup;)V")
        onGroupCreating = JavaMethod("()V")
        onGroupCreationFailed = JavaMethod("(I)V")
        onGroupNegotiationRejectedByUser = JavaMethod("()V")
        onGroupRemoved = JavaMethod("()V")
        onListenStateChanged = JavaMethod("(I)V")
        onP2pStateChanged = JavaMethod("(I)V")
        onPeerClientDisconnected = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pInfo;Landroid/net/wifi/p2p/WifiP2pGroup;)V")
        onPeerClientJoined = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pInfo;Landroid/net/wifi/p2p/WifiP2pGroup;)V")
        onPeerListChanged = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pDeviceList;)V")

    class UpnpServiceResponseListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$UpnpServiceResponseListener"
        onUpnpServiceAvailable = JavaMethod("(Ljava/util/List;Landroid/net/wifi/p2p/WifiP2pDevice;)V")

    class ServiceResponseListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$ServiceResponseListener"
        onServiceAvailable = JavaMethod("(I[BLandroid/net/wifi/p2p/WifiP2pDevice;)V")
        onUsdBasedServiceAvailable = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pDevice;Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceResponse;)V")

    class PeerListListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$PeerListListener"
        onPeersAvailable = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pDeviceList;)V")

    class P2pStateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$P2pStateListener"
        onP2pStateAvailable = JavaMethod("(I)V")

    class NetworkInfoListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$NetworkInfoListener"
        onNetworkInfoAvailable = JavaMethod("(Landroid/net/NetworkInfo;)V")

    class GroupInfoListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$GroupInfoListener"
        onGroupInfoAvailable = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pGroup;)V")

    class ExternalApproverRequestListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$ExternalApproverRequestListener"
        APPROVER_DETACH_REASON_CLOSE = JavaStaticField("I")
        APPROVER_DETACH_REASON_FAILURE = JavaStaticField("I")
        APPROVER_DETACH_REASON_REMOVE = JavaStaticField("I")
        APPROVER_DETACH_REASON_REPLACE = JavaStaticField("I")
        REQUEST_TYPE_INVITATION = JavaStaticField("I")
        REQUEST_TYPE_JOIN = JavaStaticField("I")
        REQUEST_TYPE_NEGOTIATION = JavaStaticField("I")
        onAttached = JavaMethod("(Landroid/net/MacAddress;)V")
        onDetached = JavaMethod("(Landroid/net/MacAddress;I)V")
        onPinGenerated = JavaMethod("(Landroid/net/MacAddress;Ljava/lang/String;)V")
        onConnectionRequested = JavaMethod("(ILandroid/net/wifi/p2p/WifiP2pConfig;Landroid/net/wifi/p2p/WifiP2pDevice;)V")

    class DnsSdTxtRecordListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$DnsSdTxtRecordListener"
        onDnsSdTxtRecordAvailable = JavaMethod("(Ljava/lang/String;Ljava/util/Map;Landroid/net/wifi/p2p/WifiP2pDevice;)V")

    class DnsSdServiceResponseListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$DnsSdServiceResponseListener"
        onDnsSdServiceAvailable = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/net/wifi/p2p/WifiP2pDevice;)V")

    class DiscoveryStateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$DiscoveryStateListener"
        onDiscoveryStateAvailable = JavaMethod("(I)V")

    class DeviceInfoListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$DeviceInfoListener"
        onDeviceInfoAvailable = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pDevice;)V")

    class ConnectionInfoListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$ConnectionInfoListener"
        onConnectionInfoAvailable = JavaMethod("(Landroid/net/wifi/p2p/WifiP2pInfo;)V")

    class ChannelListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$ChannelListener"
        onChannelDisconnected = JavaMethod("()V")

    class Channel(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$Channel"
        close = JavaMethod("()V")

    class ActionListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/WifiP2pManager$ActionListener"
        onFailure = JavaMethod("(I)V")
        onSuccess = JavaMethod("()V")