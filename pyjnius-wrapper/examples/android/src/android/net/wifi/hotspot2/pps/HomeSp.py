from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HomeSp"]

class HomeSp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/hotspot2/pps/HomeSp"
    __javaconstructor__ = [("()V", False), ("(Landroid/net/wifi/hotspot2/pps/HomeSp;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    setFqdn = JavaMethod("(Ljava/lang/String;)V")
    getFqdn = JavaMethod("()Ljava/lang/String;")
    setFriendlyName = JavaMethod("(Ljava/lang/String;)V")
    getFriendlyName = JavaMethod("()Ljava/lang/String;")
    setMatchAllOis = JavaMethod("([J)V")
    getMatchAllOis = JavaMethod("()[J")
    setMatchAnyOis = JavaMethod("([J)V")
    getMatchAnyOis = JavaMethod("()[J")
    setOtherHomePartnersList = JavaMethod("(Ljava/util/Collection;)V")
    getOtherHomePartnersList = JavaMethod("()Ljava/util/Collection;")
    setRoamingConsortiumOis = JavaMethod("([J)V")
    getRoamingConsortiumOis = JavaMethod("()[J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")