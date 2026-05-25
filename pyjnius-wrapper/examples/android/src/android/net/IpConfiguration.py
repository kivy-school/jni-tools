from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IpConfiguration"]

class IpConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/IpConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getStaticIpConfiguration = JavaMethod("()Landroid/net/StaticIpConfiguration;")
    getHttpProxy = JavaMethod("()Landroid/net/ProxyInfo;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/IpConfiguration/Builder"
        __javaconstructor__ = [("()V", False)]
        setStaticIpConfiguration = JavaMethod("(Landroid/net/StaticIpConfiguration;)Landroid/net/IpConfiguration$Builder;")
        setHttpProxy = JavaMethod("(Landroid/net/ProxyInfo;)Landroid/net/IpConfiguration$Builder;")
        build = JavaMethod("()Landroid/net/IpConfiguration;")