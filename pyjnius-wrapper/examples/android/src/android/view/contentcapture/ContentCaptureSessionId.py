from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentCaptureSessionId"]

class ContentCaptureSessionId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/ContentCaptureSessionId"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")