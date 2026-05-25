from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintJobInfo"]

class PrintJobInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/PrintJobInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STATE_BLOCKED = JavaStaticField("I")
    STATE_CANCELED = JavaStaticField("I")
    STATE_COMPLETED = JavaStaticField("I")
    STATE_CREATED = JavaStaticField("I")
    STATE_FAILED = JavaStaticField("I")
    STATE_QUEUED = JavaStaticField("I")
    STATE_STARTED = JavaStaticField("I")
    getId = JavaMethod("()Landroid/print/PrintJobId;")
    getLabel = JavaMethod("()Ljava/lang/String;")
    getPrinterId = JavaMethod("()Landroid/print/PrinterId;")
    getState = JavaMethod("()I")
    getCreationTime = JavaMethod("()J")
    getCopies = JavaMethod("()I")
    getPages = JavaMethod("()[Landroid/print/PageRange;")
    getAttributes = JavaMethod("()Landroid/print/PrintAttributes;")
    hasAdvancedOption = JavaMethod("(Ljava/lang/String;)Z")
    getAdvancedStringOption = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getAdvancedIntOption = JavaMethod("(Ljava/lang/String;)I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/print/PrintJobInfo/Builder"
        __javaconstructor__ = [("(Landroid/print/PrintJobInfo;)V", False)]
        setCopies = JavaMethod("(I)V")
        setAttributes = JavaMethod("(Landroid/print/PrintAttributes;)V")
        setPages = JavaMethod("([Landroid/print/PageRange;)V")
        putAdvancedOption = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;I)V", False, False)])
        build = JavaMethod("()Landroid/print/PrintJobInfo;")