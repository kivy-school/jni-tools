from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrinterCapabilitiesInfo"]

class PrinterCapabilitiesInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/PrinterCapabilitiesInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getMediaSizes = JavaMethod("()Ljava/util/List;")
    getResolutions = JavaMethod("()Ljava/util/List;")
    getMinMargins = JavaMethod("()Landroid/print/PrintAttributes$Margins;")
    getColorModes = JavaMethod("()I")
    getDuplexModes = JavaMethod("()I")
    getDefaults = JavaMethod("()Landroid/print/PrintAttributes;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/print/PrinterCapabilitiesInfo/Builder"
        __javaconstructor__ = [("(Landroid/print/PrinterId;)V", False)]
        addMediaSize = JavaMethod("(Landroid/print/PrintAttributes$MediaSize;Z)Landroid/print/PrinterCapabilitiesInfo$Builder;")
        addResolution = JavaMethod("(Landroid/print/PrintAttributes$Resolution;Z)Landroid/print/PrinterCapabilitiesInfo$Builder;")
        setMinMargins = JavaMethod("(Landroid/print/PrintAttributes$Margins;)Landroid/print/PrinterCapabilitiesInfo$Builder;")
        setColorModes = JavaMethod("(II)Landroid/print/PrinterCapabilitiesInfo$Builder;")
        setDuplexModes = JavaMethod("(II)Landroid/print/PrinterCapabilitiesInfo$Builder;")
        build = JavaMethod("()Landroid/print/PrinterCapabilitiesInfo;")