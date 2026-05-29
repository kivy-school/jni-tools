from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DnsEvent"]

class DnsEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/DnsEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getHostname = JavaMethod("()Ljava/lang/String;")
    getInetAddresses = JavaMethod("()Ljava/util/List;")
    getTotalResolvedAddressCount = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")