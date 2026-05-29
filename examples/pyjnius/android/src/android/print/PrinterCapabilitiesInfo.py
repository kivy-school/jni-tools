from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrinterCapabilitiesInfo"]

class PrinterCapabilitiesInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/PrinterCapabilitiesInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMinMargins = JavaMethod("()Landroid/print/PrintAttributes$Margins;")
    getMediaSizes = JavaMethod("()Ljava/util/List;")
    getDuplexModes = JavaMethod("()I")
    getDefaults = JavaMethod("()Landroid/print/PrintAttributes;")
    getResolutions = JavaMethod("()Ljava/util/List;")
    getColorModes = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/print/PrinterCapabilitiesInfo$Builder"
        __javaconstructor__ = [("(Landroid/print/PrinterId;)V", False)]
        addResolution = JavaMethod("(Landroid/print/PrintAttributes$Resolution;Z)Landroid/print/PrinterCapabilitiesInfo$Builder;")
        setColorModes = JavaMethod("(II)Landroid/print/PrinterCapabilitiesInfo$Builder;")
        setDuplexModes = JavaMethod("(II)Landroid/print/PrinterCapabilitiesInfo$Builder;")
        addMediaSize = JavaMethod("(Landroid/print/PrintAttributes$MediaSize;Z)Landroid/print/PrinterCapabilitiesInfo$Builder;")
        setMinMargins = JavaMethod("(Landroid/print/PrintAttributes$Margins;)Landroid/print/PrinterCapabilitiesInfo$Builder;")
        build = JavaMethod("()Landroid/print/PrinterCapabilitiesInfo;")