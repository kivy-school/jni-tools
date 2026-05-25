from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataShareRequest"]

class DataShareRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/DataShareRequest"
    __javaconstructor__ = [("(Landroid/content/LocusId;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getLocusId = JavaMethod("()Landroid/content/LocusId;")
    getMimeType = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")