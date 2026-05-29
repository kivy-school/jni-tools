from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HomeSp"]

class HomeSp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/hotspot2/pps/HomeSp"
    __javaconstructor__ = [("(Landroid/net/wifi/hotspot2/pps/HomeSp;)V", False), ("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getFqdn = JavaMethod("()Ljava/lang/String;")
    getFriendlyName = JavaMethod("()Ljava/lang/String;")
    getMatchAllOis = JavaMethod("()[J")
    getMatchAnyOis = JavaMethod("()[J")
    getOtherHomePartnersList = JavaMethod("()Ljava/util/Collection;")
    getRoamingConsortiumOis = JavaMethod("()[J")
    setFqdn = JavaMethod("(Ljava/lang/String;)V")
    setFriendlyName = JavaMethod("(Ljava/lang/String;)V")
    setMatchAllOis = JavaMethod("([J)V")
    setMatchAnyOis = JavaMethod("([J)V")
    setOtherHomePartnersList = JavaMethod("(Ljava/util/Collection;)V")
    setRoamingConsortiumOis = JavaMethod("([J)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")