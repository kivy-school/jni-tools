from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrinterInfo"]

class PrinterInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/PrinterInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STATUS_BUSY = JavaStaticField("I")
    STATUS_IDLE = JavaStaticField("I")
    STATUS_UNAVAILABLE = JavaStaticField("I")
    getId = JavaMethod("()Landroid/print/PrinterId;")
    getName = JavaMethod("()Ljava/lang/String;")
    getStatus = JavaMethod("()I")
    getDescription = JavaMethod("()Ljava/lang/String;")
    getCapabilities = JavaMethod("()Landroid/print/PrinterCapabilitiesInfo;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/print/PrinterInfo/Builder"
        __javaconstructor__ = [("(Landroid/print/PrinterId;Ljava/lang/String;I)V", False), ("(Landroid/print/PrinterInfo;)V", False)]
        setStatus = JavaMethod("(I)Landroid/print/PrinterInfo$Builder;")
        setIconResourceId = JavaMethod("(I)Landroid/print/PrinterInfo$Builder;")
        setHasCustomPrinterIcon = JavaMethod("(Z)Landroid/print/PrinterInfo$Builder;")
        setName = JavaMethod("(Ljava/lang/String;)Landroid/print/PrinterInfo$Builder;")
        setDescription = JavaMethod("(Ljava/lang/String;)Landroid/print/PrinterInfo$Builder;")
        setInfoIntent = JavaMethod("(Landroid/app/PendingIntent;)Landroid/print/PrinterInfo$Builder;")
        setCapabilities = JavaMethod("(Landroid/print/PrinterCapabilitiesInfo;)Landroid/print/PrinterInfo$Builder;")
        build = JavaMethod("()Landroid/print/PrinterInfo;")