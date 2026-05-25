from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdWithBid"]

class AdWithBid(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AdWithBid"
    __javaconstructor__ = [("(Landroid/adservices/common/AdData;D)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getAdData = JavaMethod("()Landroid/adservices/common/AdData;")
    getBid = JavaMethod("()D")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")