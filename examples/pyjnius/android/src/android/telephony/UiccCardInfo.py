from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UiccCardInfo"]

class UiccCardInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/UiccCardInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    isEuicc = JavaMethod("()Z")
    getCardId = JavaMethod("()I")
    getEid = JavaMethod("()Ljava/lang/String;")
    getIccId = JavaMethod("()Ljava/lang/String;")
    getSlotIndex = JavaMethod("()I")
    getPhysicalSlotIndex = JavaMethod("()I")
    isRemovable = JavaMethod("()Z")
    isMultipleEnabledProfilesSupported = JavaMethod("()Z")
    getPorts = JavaMethod("()Ljava/util/Collection;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")