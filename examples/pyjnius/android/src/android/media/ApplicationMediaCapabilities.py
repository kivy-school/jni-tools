from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ApplicationMediaCapabilities"]

class ApplicationMediaCapabilities(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/ApplicationMediaCapabilities"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSupportedHdrTypes = JavaMethod("()Ljava/util/List;")
    isHdrTypeSupported = JavaMethod("(Ljava/lang/String;)Z")
    isFormatSpecified = JavaMethod("(Ljava/lang/String;)Z")
    getSupportedVideoMimeTypes = JavaMethod("()Ljava/util/List;")
    getUnsupportedHdrTypes = JavaMethod("()Ljava/util/List;")
    getUnsupportedVideoMimeTypes = JavaMethod("()Ljava/util/List;")
    isVideoMimeTypeSupported = JavaMethod("(Ljava/lang/String;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    createFromXml = JavaStaticMethod("(Lorg/xmlpull/v1/XmlPullParser;)Landroid/media/ApplicationMediaCapabilities;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/ApplicationMediaCapabilities$Builder"
        __javaconstructor__ = [("()V", False)]
        addUnsupportedHdrType = JavaMethod("(Ljava/lang/String;)Landroid/media/ApplicationMediaCapabilities$Builder;")
        addUnsupportedVideoMimeType = JavaMethod("(Ljava/lang/String;)Landroid/media/ApplicationMediaCapabilities$Builder;")
        addSupportedHdrType = JavaMethod("(Ljava/lang/String;)Landroid/media/ApplicationMediaCapabilities$Builder;")
        addSupportedVideoMimeType = JavaMethod("(Ljava/lang/String;)Landroid/media/ApplicationMediaCapabilities$Builder;")
        build = JavaMethod("()Landroid/media/ApplicationMediaCapabilities;")