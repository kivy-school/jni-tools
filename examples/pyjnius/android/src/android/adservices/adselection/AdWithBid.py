from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdWithBid"]

class AdWithBid(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AdWithBid"
    __javaconstructor__ = [("(Landroid/adservices/common/AdData;D)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBid = JavaMethod("()D")
    getAdData = JavaMethod("()Landroid/adservices/common/AdData;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")