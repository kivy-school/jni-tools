from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JobWorkItem"]

class JobWorkItem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/job/JobWorkItem"
    __javaconstructor__ = [("(Landroid/content/Intent;JJJ)V", False), ("(Landroid/content/Intent;JJ)V", False), ("(Landroid/content/Intent;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getDeliveryCount = JavaMethod("()I")
    getEstimatedNetworkDownloadBytes = JavaMethod("()J")
    getEstimatedNetworkUploadBytes = JavaMethod("()J")
    getMinimumNetworkChunkBytes = JavaMethod("()J")
    getIntent = JavaMethod("()Landroid/content/Intent;")
    getExtras = JavaMethod("()Landroid/os/PersistableBundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/job/JobWorkItem$Builder"
        __javaconstructor__ = [("()V", False)]
        setEstimatedNetworkBytes = JavaMethod("(JJ)Landroid/app/job/JobWorkItem$Builder;")
        setMinimumNetworkChunkBytes = JavaMethod("(J)Landroid/app/job/JobWorkItem$Builder;")
        setIntent = JavaMethod("(Landroid/content/Intent;)Landroid/app/job/JobWorkItem$Builder;")
        setExtras = JavaMethod("(Landroid/os/PersistableBundle;)Landroid/app/job/JobWorkItem$Builder;")
        build = JavaMethod("()Landroid/app/job/JobWorkItem;")