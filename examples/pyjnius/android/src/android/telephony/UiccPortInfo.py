from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UiccPortInfo"]

class UiccPortInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/UiccPortInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    ICCID_REDACTED = JavaStaticField("Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getIccId = JavaMethod("()Ljava/lang/String;")
    getPortIndex = JavaMethod("()I")
    isActive = JavaMethod("()Z")
    getLogicalSlotIndex = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")