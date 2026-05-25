from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ApplicationMediaCapabilities"]

class ApplicationMediaCapabilities(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/ApplicationMediaCapabilities"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    isVideoMimeTypeSupported = JavaMethod("(Ljava/lang/String;)Z")
    isHdrTypeSupported = JavaMethod("(Ljava/lang/String;)Z")
    isFormatSpecified = JavaMethod("(Ljava/lang/String;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    getSupportedVideoMimeTypes = JavaMethod("()Ljava/util/List;")
    getUnsupportedVideoMimeTypes = JavaMethod("()Ljava/util/List;")
    getSupportedHdrTypes = JavaMethod("()Ljava/util/List;")
    getUnsupportedHdrTypes = JavaMethod("()Ljava/util/List;")
    createFromXml = JavaStaticMethod("(Lorg/xmlpull/v1/XmlPullParser;)Landroid/media/ApplicationMediaCapabilities;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/ApplicationMediaCapabilities/Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/media/ApplicationMediaCapabilities;")
        addSupportedVideoMimeType = JavaMethod("(Ljava/lang/String;)Landroid/media/ApplicationMediaCapabilities$Builder;")
        addUnsupportedVideoMimeType = JavaMethod("(Ljava/lang/String;)Landroid/media/ApplicationMediaCapabilities$Builder;")
        addSupportedHdrType = JavaMethod("(Ljava/lang/String;)Landroid/media/ApplicationMediaCapabilities$Builder;")
        addUnsupportedHdrType = JavaMethod("(Ljava/lang/String;)Landroid/media/ApplicationMediaCapabilities$Builder;")