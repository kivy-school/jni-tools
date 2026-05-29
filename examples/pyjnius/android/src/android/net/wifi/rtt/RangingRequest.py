from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangingRequest"]

class RangingRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/rtt/RangingRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SECURITY_MODE_OPEN = JavaStaticField("I")
    SECURITY_MODE_OPPORTUNISTIC = JavaStaticField("I")
    SECURITY_MODE_SECURE_AUTH = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDefaultRttBurstSize = JavaStaticMethod("()I")
    getMaxPeers = JavaStaticMethod("()I")
    getMaxRttBurstSize = JavaStaticMethod("()I")
    getMinRttBurstSize = JavaStaticMethod("()I")
    getRttBurstSize = JavaMethod("()I")
    getSecurityMode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/rtt/RangingRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setSecurityMode = JavaMethod("(I)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        addWifiAwarePeer = JavaMultipleMethod([("(Landroid/net/MacAddress;)Landroid/net/wifi/rtt/RangingRequest$Builder;", False, False), ("(Landroid/net/wifi/aware/PeerHandle;)Landroid/net/wifi/rtt/RangingRequest$Builder;", False, False)])
        setRttBurstSize = JavaMethod("(I)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        addAccessPoints = JavaMethod("(Ljava/util/List;)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        addNon80211mcCapableAccessPoint = JavaMethod("(Landroid/net/wifi/ScanResult;)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        addNon80211mcCapableAccessPoints = JavaMethod("(Ljava/util/List;)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        addResponder = JavaMethod("(Landroid/net/wifi/rtt/ResponderConfig;)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        addAccessPoint = JavaMethod("(Landroid/net/wifi/ScanResult;)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        addResponders = JavaMethod("(Ljava/util/List;)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        build = JavaMethod("()Landroid/net/wifi/rtt/RangingRequest;")