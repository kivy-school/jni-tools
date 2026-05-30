from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class WifiP2pUpnpServiceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pUpnpServiceRequest"
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    newInstance = JavaMultipleMethod([("()Landroid/net/wifi/p2p/nsd/WifiP2pUpnpServiceRequest;", True, False), ("(Ljava/lang/String;)Landroid/net/wifi/p2p/nsd/WifiP2pUpnpServiceRequest;", True, False)])

class WifiP2pServiceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pServiceRequest"
    __javaconstructor__ = [("(Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig;)V", False)]
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getWifiP2pUsdBasedServiceConfig = JavaMethod("()Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    newInstance = JavaMultipleMethod([("(ILjava/lang/String;)Landroid/net/wifi/p2p/nsd/WifiP2pServiceRequest;", True, False), ("(I)Landroid/net/wifi/p2p/nsd/WifiP2pServiceRequest;", True, False)])
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class WifiP2pDnsSdServiceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pDnsSdServiceRequest"
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    newInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Landroid/net/wifi/p2p/nsd/WifiP2pDnsSdServiceRequest;", True, False), ("(Ljava/lang/String;)Landroid/net/wifi/p2p/nsd/WifiP2pDnsSdServiceRequest;", True, False), ("()Landroid/net/wifi/p2p/nsd/WifiP2pDnsSdServiceRequest;", True, False)])

class WifiP2pUpnpServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pUpnpServiceInfo"
    SERVICE_TYPE_ALL = JavaStaticField("I")
    SERVICE_TYPE_BONJOUR = JavaStaticField("I")
    SERVICE_TYPE_UPNP = JavaStaticField("I")
    SERVICE_TYPE_VENDOR_SPECIFIC = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    newInstance = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/List;)Landroid/net/wifi/p2p/nsd/WifiP2pUpnpServiceInfo;")

class WifiP2pUsdBasedServiceConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SERVICE_PROTOCOL_TYPE_BONJOUR = JavaStaticField("I")
    SERVICE_PROTOCOL_TYPE_GENERIC = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getServiceName = JavaMethod("()Ljava/lang/String;")
    getServiceSpecificInfo = JavaMethod("()[B")
    getServiceProtocolType = JavaMethod("()I")
    getMaxAllowedServiceSpecificInfoLength = JavaStaticMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setServiceSpecificInfo = JavaMethod("([B)Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig$Builder;")
        setServiceProtocolType = JavaMethod("(I)Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig;")

class WifiP2pServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pServiceInfo"
    __javaconstructor__ = [("(Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig;)V", False)]
    SERVICE_TYPE_ALL = JavaStaticField("I")
    SERVICE_TYPE_BONJOUR = JavaStaticField("I")
    SERVICE_TYPE_UPNP = JavaStaticField("I")
    SERVICE_TYPE_VENDOR_SPECIFIC = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getWifiP2pUsdBasedServiceConfig = JavaMethod("()Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class WifiP2pDnsSdServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pDnsSdServiceInfo"
    SERVICE_TYPE_ALL = JavaStaticField("I")
    SERVICE_TYPE_BONJOUR = JavaStaticField("I")
    SERVICE_TYPE_UPNP = JavaStaticField("I")
    SERVICE_TYPE_VENDOR_SPECIFIC = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    newInstance = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;)Landroid/net/wifi/p2p/nsd/WifiP2pDnsSdServiceInfo;")

class WifiP2pUsdBasedServiceResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getServiceSpecificInfo = JavaMethod("()[B")
    getServiceProtocolType = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")