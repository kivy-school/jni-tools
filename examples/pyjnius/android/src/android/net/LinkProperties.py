from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinkProperties"]

class LinkProperties(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/LinkProperties"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getHttpProxy = JavaMethod("()Landroid/net/ProxyInfo;")
    getDomains = JavaMethod("()Ljava/lang/String;")
    getDhcpServerAddress = JavaMethod("()Ljava/net/Inet4Address;")
    getDnsServers = JavaMethod("()Ljava/util/List;")
    addRoute = JavaMethod("(Landroid/net/RouteInfo;)Z")
    getInterfaceName = JavaMethod("()Ljava/lang/String;")
    getLinkAddresses = JavaMethod("()Ljava/util/List;")
    getMtu = JavaMethod("()I")
    getNat64Prefix = JavaMethod("()Landroid/net/IpPrefix;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    clear = JavaMethod("()V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    isPrivateDnsActive = JavaMethod("()Z")
    getRoutes = JavaMethod("()Ljava/util/List;")
    isWakeOnLanSupported = JavaMethod("()Z")
    getPrivateDnsServerName = JavaMethod("()Ljava/lang/String;")
    setDhcpServerAddress = JavaMethod("(Ljava/net/Inet4Address;)V")
    setDnsServers = JavaMethod("(Ljava/util/Collection;)V")
    setDomains = JavaMethod("(Ljava/lang/String;)V")
    setHttpProxy = JavaMethod("(Landroid/net/ProxyInfo;)V")
    setInterfaceName = JavaMethod("(Ljava/lang/String;)V")
    setLinkAddresses = JavaMethod("(Ljava/util/Collection;)V")
    setMtu = JavaMethod("(I)V")
    setNat64Prefix = JavaMethod("(Landroid/net/IpPrefix;)V")