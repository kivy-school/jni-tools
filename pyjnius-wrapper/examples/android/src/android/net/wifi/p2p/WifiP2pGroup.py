from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pGroup"]

class WifiP2pGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/WifiP2pGroup"
    __javaconstructor__ = [("()V", False), ("(Landroid/net/wifi/p2p/WifiP2pGroup;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    NETWORK_ID_PERSISTENT = JavaStaticField("I")
    NETWORK_ID_TEMPORARY = JavaStaticField("I")
    getNetworkName = JavaMethod("()Ljava/lang/String;")
    isGroupOwner = JavaMethod("()Z")
    getOwner = JavaMethod("()Landroid/net/wifi/p2p/WifiP2pDevice;")
    getClientList = JavaMethod("()Ljava/util/Collection;")
    getPassphrase = JavaMethod("()Ljava/lang/String;")
    getInterface = JavaMethod("()Ljava/lang/String;")
    getNetworkId = JavaMethod("()I")
    getFrequency = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")