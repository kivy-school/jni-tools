from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBand = JavaMethod("()I")
    getStaMacAddress = JavaMethod("()Landroid/net/MacAddress;")
    getLinkId = JavaMethod("()I")
    getApMacAddress = JavaMethod("()Landroid/net/MacAddress;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getState = JavaMethod("()I")
    getRssi = JavaMethod("()I")
    getChannel = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getRxLinkSpeedMbps = JavaMethod("()I")
    getTxLinkSpeedMbps = JavaMethod("()I")