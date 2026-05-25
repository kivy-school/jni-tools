from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JobWorkItem"]

class JobWorkItem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/job/JobWorkItem"
    __javaconstructor__ = [("(Landroid/content/Intent;)V", False), ("(Landroid/content/Intent;JJ)V", False), ("(Landroid/content/Intent;JJJ)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getExtras = JavaMethod("()Landroid/os/PersistableBundle;")
    getIntent = JavaMethod("()Landroid/content/Intent;")
    getEstimatedNetworkDownloadBytes = JavaMethod("()J")
    getEstimatedNetworkUploadBytes = JavaMethod("()J")
    getMinimumNetworkChunkBytes = JavaMethod("()J")
    getDeliveryCount = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/job/JobWorkItem/Builder"
        __javaconstructor__ = [("()V", False)]
        setExtras = JavaMethod("(Landroid/os/PersistableBundle;)Landroid/app/job/JobWorkItem$Builder;")
        setIntent = JavaMethod("(Landroid/content/Intent;)Landroid/app/job/JobWorkItem$Builder;")
        setEstimatedNetworkBytes = JavaMethod("(JJ)Landroid/app/job/JobWorkItem$Builder;")
        setMinimumNetworkChunkBytes = JavaMethod("(J)Landroid/app/job/JobWorkItem$Builder;")
        build = JavaMethod("()Landroid/app/job/JobWorkItem;")