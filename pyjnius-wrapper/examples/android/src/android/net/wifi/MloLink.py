from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MloLink"]

class MloLink(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/MloLink"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    INVALID_MLO_LINK_ID = JavaStaticField("I")
    MLO_LINK_STATE_ACTIVE = JavaStaticField("I")
    MLO_LINK_STATE_IDLE = JavaStaticField("I")
    MLO_LINK_STATE_INVALID = JavaStaticField("I")
    MLO_LINK_STATE_UNASSOCIATED = JavaStaticField("I")
    getBand = JavaMethod("()I")
    getChannel = JavaMethod("()I")
    getLinkId = JavaMethod("()I")
    getState = JavaMethod("()I")
    getApMacAddress = JavaMethod("()Landroid/net/MacAddress;")
    getStaMacAddress = JavaMethod("()Landroid/net/MacAddress;")
    getRxLinkSpeedMbps = JavaMethod("()I")
    getTxLinkSpeedMbps = JavaMethod("()I")
    getRssi = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")