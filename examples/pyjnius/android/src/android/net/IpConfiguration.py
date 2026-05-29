from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IpConfiguration"]

class IpConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/IpConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getHttpProxy = JavaMethod("()Landroid/net/ProxyInfo;")
    getStaticIpConfiguration = JavaMethod("()Landroid/net/StaticIpConfiguration;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/IpConfiguration$Builder"
        __javaconstructor__ = [("()V", False)]
        setStaticIpConfiguration = JavaMethod("(Landroid/net/StaticIpConfiguration;)Landroid/net/IpConfiguration$Builder;")
        build = JavaMethod("()Landroid/net/IpConfiguration;")
        setHttpProxy = JavaMethod("(Landroid/net/ProxyInfo;)Landroid/net/IpConfiguration$Builder;")