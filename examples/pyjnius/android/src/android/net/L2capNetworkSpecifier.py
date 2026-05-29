from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["L2capNetworkSpecifier"]

class L2capNetworkSpecifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/L2capNetworkSpecifier"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    HEADER_COMPRESSION_6LOWPAN = JavaStaticField("I")
    HEADER_COMPRESSION_ANY = JavaStaticField("I")
    HEADER_COMPRESSION_NONE = JavaStaticField("I")
    PSM_ANY = JavaStaticField("I")
    ROLE_ANY = JavaStaticField("I")
    ROLE_CLIENT = JavaStaticField("I")
    ROLE_SERVER = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getRole = JavaMethod("()I")
    canBeSatisfiedBy = JavaMethod("(Landroid/net/NetworkSpecifier;)Z")
    getPsm = JavaMethod("()I")
    getHeaderCompression = JavaMethod("()I")
    redact = JavaMethod("()Landroid/net/NetworkSpecifier;")
    getRemoteAddress = JavaMethod("()Landroid/net/MacAddress;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/L2capNetworkSpecifier$Builder"
        __javaconstructor__ = [("()V", False)]
        setRemoteAddress = JavaMethod("(Landroid/net/MacAddress;)Landroid/net/L2capNetworkSpecifier$Builder;")
        setPsm = JavaMethod("(I)Landroid/net/L2capNetworkSpecifier$Builder;")
        setHeaderCompression = JavaMethod("(I)Landroid/net/L2capNetworkSpecifier$Builder;")
        setRole = JavaMethod("(I)Landroid/net/L2capNetworkSpecifier$Builder;")
        build = JavaMethod("()Landroid/net/L2capNetworkSpecifier;")