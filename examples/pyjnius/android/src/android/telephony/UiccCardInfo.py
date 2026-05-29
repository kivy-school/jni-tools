from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UiccCardInfo"]

class UiccCardInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/UiccCardInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPorts = JavaMethod("()Ljava/util/Collection;")
    getCardId = JavaMethod("()I")
    getEid = JavaMethod("()Ljava/lang/String;")
    isEuicc = JavaMethod("()Z")
    isRemovable = JavaMethod("()Z")
    getPhysicalSlotIndex = JavaMethod("()I")
    isMultipleEnabledProfilesSupported = JavaMethod("()Z")
    getIccId = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getSlotIndex = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")