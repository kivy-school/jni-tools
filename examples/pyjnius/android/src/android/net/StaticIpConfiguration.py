from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StaticIpConfiguration"]

class StaticIpConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/StaticIpConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getIpAddress = JavaMethod("()Landroid/net/LinkAddress;")
    getGateway = JavaMethod("()Ljava/net/InetAddress;")
    getDnsServers = JavaMethod("()Ljava/util/List;")
    getDomains = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/StaticIpConfiguration/Builder"
        __javaconstructor__ = [("()V", False)]
        setIpAddress = JavaMethod("(Landroid/net/LinkAddress;)Landroid/net/StaticIpConfiguration$Builder;")
        setGateway = JavaMethod("(Ljava/net/InetAddress;)Landroid/net/StaticIpConfiguration$Builder;")
        setDnsServers = JavaMethod("(Ljava/lang/Iterable;)Landroid/net/StaticIpConfiguration$Builder;")
        setDomains = JavaMethod("(Ljava/lang/String;)Landroid/net/StaticIpConfiguration$Builder;")
        build = JavaMethod("()Landroid/net/StaticIpConfiguration;")