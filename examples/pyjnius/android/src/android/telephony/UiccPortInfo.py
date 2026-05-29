from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UiccPortInfo"]

class UiccPortInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/UiccPortInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    ICCID_REDACTED = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getIccId = JavaMethod("()Ljava/lang/String;")
    getPortIndex = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getLogicalSlotIndex = JavaMethod("()I")
    isActive = JavaMethod("()Z")