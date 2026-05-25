from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pServiceRequest"]

class WifiP2pServiceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pServiceRequest"
    newInstance = JavaMultipleMethod([("(ILjava/lang/String;)Landroid/net/wifi/p2p/nsd/WifiP2pServiceRequest;", True, False), ("(I)Landroid/net/wifi/p2p/nsd/WifiP2pServiceRequest;", True, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")