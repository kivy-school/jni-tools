from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StaticIpConfiguration"]

class StaticIpConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/StaticIpConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDomains = JavaMethod("()Ljava/lang/String;")
    getDnsServers = JavaMethod("()Ljava/util/List;")
    getIpAddress = JavaMethod("()Landroid/net/LinkAddress;")
    getGateway = JavaMethod("()Ljava/net/InetAddress;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/StaticIpConfiguration$Builder"
        __javaconstructor__ = [("()V", False)]
        setGateway = JavaMethod("(Ljava/net/InetAddress;)Landroid/net/StaticIpConfiguration$Builder;")
        setIpAddress = JavaMethod("(Landroid/net/LinkAddress;)Landroid/net/StaticIpConfiguration$Builder;")
        build = JavaMethod("()Landroid/net/StaticIpConfiguration;")
        setDnsServers = JavaMethod("(Ljava/lang/Iterable;)Landroid/net/StaticIpConfiguration$Builder;")
        setDomains = JavaMethod("(Ljava/lang/String;)Landroid/net/StaticIpConfiguration$Builder;")