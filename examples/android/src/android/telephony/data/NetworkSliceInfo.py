from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkSliceInfo"]

class NetworkSliceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/data/NetworkSliceInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SLICE_DIFFERENTIATOR_NO_SLICE = JavaStaticField("I")
    SLICE_SERVICE_TYPE_EMBB = JavaStaticField("I")
    SLICE_SERVICE_TYPE_MIOT = JavaStaticField("I")
    SLICE_SERVICE_TYPE_NONE = JavaStaticField("I")
    SLICE_SERVICE_TYPE_URLLC = JavaStaticField("I")
    SLICE_STATUS_ALLOWED = JavaStaticField("I")
    SLICE_STATUS_CONFIGURED = JavaStaticField("I")
    SLICE_STATUS_DEFAULT_CONFIGURED = JavaStaticField("I")
    SLICE_STATUS_REJECTED_NOT_AVAILABLE_IN_PLMN = JavaStaticField("I")
    SLICE_STATUS_REJECTED_NOT_AVAILABLE_IN_REGISTERED_AREA = JavaStaticField("I")
    SLICE_STATUS_UNKNOWN = JavaStaticField("I")
    getSliceServiceType = JavaMethod("()I")
    getSliceDifferentiator = JavaMethod("()I")
    getMappedHplmnSliceServiceType = JavaMethod("()I")
    getMappedHplmnSliceDifferentiator = JavaMethod("()I")
    getStatus = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/data/NetworkSliceInfo/Builder"
        __javaconstructor__ = [("()V", False)]
        setSliceServiceType = JavaMethod("(I)Landroid/telephony/data/NetworkSliceInfo$Builder;")
        setSliceDifferentiator = JavaMethod("(I)Landroid/telephony/data/NetworkSliceInfo$Builder;")
        setMappedHplmnSliceServiceType = JavaMethod("(I)Landroid/telephony/data/NetworkSliceInfo$Builder;")
        setMappedHplmnSliceDifferentiator = JavaMethod("(I)Landroid/telephony/data/NetworkSliceInfo$Builder;")
        setStatus = JavaMethod("(I)Landroid/telephony/data/NetworkSliceInfo$Builder;")
        build = JavaMethod("()Landroid/telephony/data/NetworkSliceInfo;")