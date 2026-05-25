from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DnsOptions"]

class DnsOptions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/DnsOptions"
    DNS_OPTION_DISABLED = JavaStaticField("I")
    DNS_OPTION_ENABLED = JavaStaticField("I")
    DNS_OPTION_UNSPECIFIED = JavaStaticField("I")
    getUseHttpStackDnsResolver = JavaMethod("()I")
    getPersistHostCache = JavaMethod("()I")
    getStaleDns = JavaMethod("()I")
    getPersistHostCachePeriod = JavaMethod("()Ljava/time/Duration;")
    getPreestablishConnectionsToStaleDnsResults = JavaMethod("()I")
    getStaleDnsOptions = JavaMethod("()Landroid/net/http/DnsOptions$StaleDnsOptions;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/DnsOptions/Builder"
        __javaconstructor__ = [("()V", False)]
        setUseHttpStackDnsResolver = JavaMethod("(I)Landroid/net/http/DnsOptions$Builder;")
        setStaleDns = JavaMethod("(I)Landroid/net/http/DnsOptions$Builder;")
        setStaleDnsOptions = JavaMethod("(Landroid/net/http/DnsOptions$StaleDnsOptions;)Landroid/net/http/DnsOptions$Builder;")
        setPreestablishConnectionsToStaleDnsResults = JavaMethod("(I)Landroid/net/http/DnsOptions$Builder;")
        setPersistHostCache = JavaMethod("(I)Landroid/net/http/DnsOptions$Builder;")
        setPersistHostCachePeriod = JavaMethod("(Ljava/time/Duration;)Landroid/net/http/DnsOptions$Builder;")
        build = JavaMethod("()Landroid/net/http/DnsOptions;")

    class StaleDnsOptions(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/DnsOptions/StaleDnsOptions"
        getFreshLookupTimeout = JavaMethod("()Ljava/time/Duration;")
        getMaxExpiredDelay = JavaMethod("()Ljava/time/Duration;")
        getAllowCrossNetworkUsage = JavaMethod("()I")
        getUseStaleOnNameNotResolved = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/net/http/DnsOptions/StaleDnsOptions/Builder"
            __javaconstructor__ = [("()V", False)]
            setFreshLookupTimeout = JavaMethod("(Ljava/time/Duration;)Landroid/net/http/DnsOptions$StaleDnsOptions$Builder;")
            setMaxExpiredDelay = JavaMethod("(Ljava/time/Duration;)Landroid/net/http/DnsOptions$StaleDnsOptions$Builder;")
            setAllowCrossNetworkUsage = JavaMethod("(I)Landroid/net/http/DnsOptions$StaleDnsOptions$Builder;")
            setUseStaleOnNameNotResolved = JavaMethod("(I)Landroid/net/http/DnsOptions$StaleDnsOptions$Builder;")
            build = JavaMethod("()Landroid/net/http/DnsOptions$StaleDnsOptions;")