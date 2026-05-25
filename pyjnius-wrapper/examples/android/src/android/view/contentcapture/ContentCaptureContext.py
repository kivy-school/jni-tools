from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentCaptureContext"]

class ContentCaptureContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/contentcapture/ContentCaptureContext"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getLocusId = JavaMethod("()Landroid/content/LocusId;")
    forLocusId = JavaStaticMethod("(Ljava/lang/String;)Landroid/view/contentcapture/ContentCaptureContext;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/contentcapture/ContentCaptureContext/Builder"
        __javaconstructor__ = [("(Landroid/content/LocusId;)V", False)]
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/contentcapture/ContentCaptureContext$Builder;")
        build = JavaMethod("()Landroid/view/contentcapture/ContentCaptureContext;")