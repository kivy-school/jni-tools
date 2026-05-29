from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NsdServiceInfo"]

class NsdServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/nsd/NsdServiceInfo"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    setPort = JavaMethod("(I)V")
    getNetwork = JavaMethod("()Landroid/net/Network;")
    getHostname = JavaMethod("()Ljava/lang/String;")
    getServiceType = JavaMethod("()Ljava/lang/String;")
    setServiceName = JavaMethod("(Ljava/lang/String;)V")
    setNetwork = JavaMethod("(Landroid/net/Network;)V")
    getHostAddresses = JavaMethod("()Ljava/util/List;")
    getSubtypes = JavaMethod("()Ljava/util/Set;")
    setSubtypes = JavaMethod("(Ljava/util/Set;)V")
    setServiceType = JavaMethod("(Ljava/lang/String;)V")
    removeAttribute = JavaMethod("(Ljava/lang/String;)V")
    setHost = JavaMethod("(Ljava/net/InetAddress;)V")
    setHostAddresses = JavaMethod("(Ljava/util/List;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    getHost = JavaMethod("()Ljava/net/InetAddress;")
    getPort = JavaMethod("()I")
    getAttributes = JavaMethod("()Ljava/util/Map;")
    getServiceName = JavaMethod("()Ljava/lang/String;")
    setAttribute = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")