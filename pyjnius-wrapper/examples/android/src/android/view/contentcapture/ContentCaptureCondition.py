from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentCaptureCondition"]

class ContentCaptureCondition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/ContentCaptureCondition"
    __javaconstructor__ = [("(Landroid/content/LocusId;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_IS_REGEX = JavaStaticField("I")
    getLocusId = JavaMethod("()Landroid/content/LocusId;")
    getFlags = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")