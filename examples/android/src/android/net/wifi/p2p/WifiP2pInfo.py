from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pInfo"]

class WifiP2pInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/WifiP2pInfo"
    __javaconstructor__ = [("()V", False), ("(Landroid/net/wifi/p2p/WifiP2pInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    groupFormed = JavaField("Z")
    groupOwnerAddress = JavaField("Ljava/net/InetAddress;")
    isGroupOwner = JavaField("Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")