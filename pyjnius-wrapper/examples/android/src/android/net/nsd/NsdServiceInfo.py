from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NsdServiceInfo"]

class NsdServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/nsd/NsdServiceInfo"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getServiceName = JavaMethod("()Ljava/lang/String;")
    setServiceName = JavaMethod("(Ljava/lang/String;)V")
    getServiceType = JavaMethod("()Ljava/lang/String;")
    setServiceType = JavaMethod("(Ljava/lang/String;)V")
    getHost = JavaMethod("()Ljava/net/InetAddress;")
    setHost = JavaMethod("(Ljava/net/InetAddress;)V")
    getPort = JavaMethod("()I")
    setPort = JavaMethod("(I)V")
    getHostAddresses = JavaMethod("()Ljava/util/List;")
    setHostAddresses = JavaMethod("(Ljava/util/List;)V")
    setAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    removeAttribute = JavaMethod("(Ljava/lang/String;)V")
    getAttributes = JavaMethod("()Ljava/util/Map;")
    getNetwork = JavaMethod("()Landroid/net/Network;")
    setNetwork = JavaMethod("(Landroid/net/Network;)V")
    setSubtypes = JavaMethod("(Ljava/util/Set;)V")
    getSubtypes = JavaMethod("()Ljava/util/Set;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")