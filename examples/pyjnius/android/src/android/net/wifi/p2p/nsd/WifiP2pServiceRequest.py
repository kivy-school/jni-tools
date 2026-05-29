from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pServiceRequest"]

class WifiP2pServiceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pServiceRequest"
    __javaconstructor__ = [("(Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig;)V", False)]
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    newInstance = JavaMultipleMethod([("(I)Landroid/net/wifi/p2p/nsd/WifiP2pServiceRequest;", True, False), ("(ILjava/lang/String;)Landroid/net/wifi/p2p/nsd/WifiP2pServiceRequest;", True, False)])
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getWifiP2pUsdBasedServiceConfig = JavaMethod("()Landroid/net/wifi/p2p/nsd/WifiP2pUsdBasedServiceConfig;")