from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinkProperties"]

class LinkProperties(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/LinkProperties"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    setInterfaceName = JavaMethod("(Ljava/lang/String;)V")
    getInterfaceName = JavaMethod("()Ljava/lang/String;")
    getLinkAddresses = JavaMethod("()Ljava/util/List;")
    setLinkAddresses = JavaMethod("(Ljava/util/Collection;)V")
    setDnsServers = JavaMethod("(Ljava/util/Collection;)V")
    getDnsServers = JavaMethod("()Ljava/util/List;")
    isPrivateDnsActive = JavaMethod("()Z")
    setDhcpServerAddress = JavaMethod("(Ljava/net/Inet4Address;)V")
    getDhcpServerAddress = JavaMethod("()Ljava/net/Inet4Address;")
    getPrivateDnsServerName = JavaMethod("()Ljava/lang/String;")
    setDomains = JavaMethod("(Ljava/lang/String;)V")
    getDomains = JavaMethod("()Ljava/lang/String;")
    setMtu = JavaMethod("(I)V")
    getMtu = JavaMethod("()I")
    addRoute = JavaMethod("(Landroid/net/RouteInfo;)Z")
    getRoutes = JavaMethod("()Ljava/util/List;")
    setHttpProxy = JavaMethod("(Landroid/net/ProxyInfo;)V")
    getHttpProxy = JavaMethod("()Landroid/net/ProxyInfo;")
    getNat64Prefix = JavaMethod("()Landroid/net/IpPrefix;")
    setNat64Prefix = JavaMethod("(Landroid/net/IpPrefix;)V")
    clear = JavaMethod("()V")
    describeContents = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    isWakeOnLanSupported = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")