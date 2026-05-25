from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncRequest"]

class SyncRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/SyncRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/SyncRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        syncOnce = JavaMethod("()Landroid/content/SyncRequest$Builder;")
        syncPeriodic = JavaMethod("(JJ)Landroid/content/SyncRequest$Builder;")
        setDisallowMetered = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setRequiresCharging = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setSyncAdapter = JavaMethod("(Landroid/accounts/Account;Ljava/lang/String;)Landroid/content/SyncRequest$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/content/SyncRequest$Builder;")
        setNoRetry = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setIgnoreSettings = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setIgnoreBackoff = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setManual = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setExpedited = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setScheduleAsExpeditedJob = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        build = JavaMethod("()Landroid/content/SyncRequest;")