from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pGroup"]

class WifiP2pGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/WifiP2pGroup"
    __javaconstructor__ = [("()V", False), ("(Landroid/net/wifi/p2p/WifiP2pGroup;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    NETWORK_ID_PERSISTENT = JavaStaticField("I")
    NETWORK_ID_TEMPORARY = JavaStaticField("I")
    SECURITY_TYPE_UNKNOWN = JavaStaticField("I")
    SECURITY_TYPE_WPA2_PSK = JavaStaticField("I")
    SECURITY_TYPE_WPA3_COMPATIBILITY = JavaStaticField("I")
    SECURITY_TYPE_WPA3_SAE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getNetworkName = JavaMethod("()Ljava/lang/String;")
    getClientList = JavaMethod("()Ljava/util/Collection;")
    getGroupOwnerBssid = JavaMethod("()Landroid/net/MacAddress;")
    getFrequency = JavaMethod("()I")
    getPassphrase = JavaMethod("()Ljava/lang/String;")
    getSecurityType = JavaMethod("()I")
    isGroupOwner = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getInterface = JavaMethod("()Ljava/lang/String;")
    getOwner = JavaMethod("()Landroid/net/wifi/p2p/WifiP2pDevice;")
    getNetworkId = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")