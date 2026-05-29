from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getAdvancedIntOption = JavaMethod("(Ljava/lang/String;)I")
    getAdvancedStringOption = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    hasAdvancedOption = JavaMethod("(Ljava/lang/String;)Z")
    getCopies = JavaMethod("()I")
    getPrinterId = JavaMethod("()Landroid/print/PrinterId;")
    getPages = JavaMethod("()[Landroid/print/PageRange;")
    toString = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()Landroid/print/PrintJobId;")
    getState = JavaMethod("()I")
    getAttributes = JavaMethod("()Landroid/print/PrintAttributes;")
    getLabel = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getCreationTime = JavaMethod("()J")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/print/PrintJobInfo$Builder"
        __javaconstructor__ = [("(Landroid/print/PrintJobInfo;)V", False)]
        setPages = JavaMethod("([Landroid/print/PageRange;)V")
        putAdvancedOption = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;I)V", False, False)])
        setCopies = JavaMethod("(I)V")
        build = JavaMethod("()Landroid/print/PrintJobInfo;")
        setAttributes = JavaMethod("(Landroid/print/PrintAttributes;)V")