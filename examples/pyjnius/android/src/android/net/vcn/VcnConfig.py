from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VcnConfig"]

class VcnConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/vcn/VcnConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getGatewayConnectionConfigs = JavaMethod("()Ljava/util/Set;")
    getRestrictedUnderlyingNetworkTransports = JavaMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/vcn/VcnConfig$Builder"
        __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
        addGatewayConnectionConfig = JavaMethod("(Landroid/net/vcn/VcnGatewayConnectionConfig;)Landroid/net/vcn/VcnConfig$Builder;")
        setRestrictedUnderlyingNetworkTransports = JavaMethod("(Ljava/util/Set;)Landroid/net/vcn/VcnConfig$Builder;")
        build = JavaMethod("()Landroid/net/vcn/VcnConfig;")