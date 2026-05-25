from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pDeviceList"]

class WifiP2pDeviceList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/WifiP2pDeviceList"
    __javaconstructor__ = [("()V", False), ("(Landroid/net/wifi/p2p/WifiP2pDeviceList;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    get = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/p2p/WifiP2pDevice;")
    getDeviceList = JavaMethod("()Ljava/util/Collection;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")