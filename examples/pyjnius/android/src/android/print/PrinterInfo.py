from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrinterInfo"]

class PrinterInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/PrinterInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STATUS_BUSY = JavaStaticField("I")
    STATUS_IDLE = JavaStaticField("I")
    STATUS_UNAVAILABLE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getStatus = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()Landroid/print/PrinterId;")
    getCapabilities = JavaMethod("()Landroid/print/PrinterCapabilitiesInfo;")
    getDescription = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/print/PrinterInfo$Builder"
        __javaconstructor__ = [("(Landroid/print/PrinterId;Ljava/lang/String;I)V", False), ("(Landroid/print/PrinterInfo;)V", False)]
        setIconResourceId = JavaMethod("(I)Landroid/print/PrinterInfo$Builder;")
        setStatus = JavaMethod("(I)Landroid/print/PrinterInfo$Builder;")
        setCapabilities = JavaMethod("(Landroid/print/PrinterCapabilitiesInfo;)Landroid/print/PrinterInfo$Builder;")
        setInfoIntent = JavaMethod("(Landroid/app/PendingIntent;)Landroid/print/PrinterInfo$Builder;")
        setHasCustomPrinterIcon = JavaMethod("(Z)Landroid/print/PrinterInfo$Builder;")
        setName = JavaMethod("(Ljava/lang/String;)Landroid/print/PrinterInfo$Builder;")
        setDescription = JavaMethod("(Ljava/lang/String;)Landroid/print/PrinterInfo$Builder;")
        build = JavaMethod("()Landroid/print/PrinterInfo;")