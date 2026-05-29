from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdvertisingRequest"]

class AdvertisingRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/nsd/AdvertisingRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_SKIP_PROBING = JavaStaticField("J")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getProtocolType = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getServiceInfo = JavaMethod("()Landroid/net/nsd/NsdServiceInfo;")
    getFlags = JavaMethod("()J")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/nsd/AdvertisingRequest$Builder"
        __javaconstructor__ = [("(Landroid/net/nsd/NsdServiceInfo;)V", False)]
        setProtocolType = JavaMethod("(I)Landroid/net/nsd/AdvertisingRequest$Builder;")
        setFlags = JavaMethod("(J)Landroid/net/nsd/AdvertisingRequest$Builder;")
        build = JavaMethod("()Landroid/net/nsd/AdvertisingRequest;")