from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangingRequest"]

class RangingRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/rtt/RangingRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getMaxPeers = JavaStaticMethod("()I")
    getDefaultRttBurstSize = JavaStaticMethod("()I")
    getMinRttBurstSize = JavaStaticMethod("()I")
    getMaxRttBurstSize = JavaStaticMethod("()I")
    getRttBurstSize = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/rtt/RangingRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        setRttBurstSize = JavaMethod("(I)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        addAccessPoint = JavaMethod("(Landroid/net/wifi/ScanResult;)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        addAccessPoints = JavaMethod("(Ljava/util/List;)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        addResponder = JavaMethod("(Landroid/net/wifi/rtt/ResponderConfig;)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        addResponders = JavaMethod("(Ljava/util/List;)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        addNon80211mcCapableAccessPoint = JavaMethod("(Landroid/net/wifi/ScanResult;)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        addNon80211mcCapableAccessPoints = JavaMethod("(Ljava/util/List;)Landroid/net/wifi/rtt/RangingRequest$Builder;")
        addWifiAwarePeer = JavaMultipleMethod([("(Landroid/net/MacAddress;)Landroid/net/wifi/rtt/RangingRequest$Builder;", False, False), ("(Landroid/net/wifi/aware/PeerHandle;)Landroid/net/wifi/rtt/RangingRequest$Builder;", False, False)])
        build = JavaMethod("()Landroid/net/wifi/rtt/RangingRequest;")