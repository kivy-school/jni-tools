from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncRequest"]

class SyncRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/SyncRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/SyncRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/content/SyncRequest$Builder;")
        build = JavaMethod("()Landroid/content/SyncRequest;")
        setIgnoreBackoff = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setIgnoreSettings = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setExpedited = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setDisallowMetered = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setManual = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setNoRetry = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setRequiresCharging = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setScheduleAsExpeditedJob = JavaMethod("(Z)Landroid/content/SyncRequest$Builder;")
        setSyncAdapter = JavaMethod("(Landroid/accounts/Account;Ljava/lang/String;)Landroid/content/SyncRequest$Builder;")
        syncOnce = JavaMethod("()Landroid/content/SyncRequest$Builder;")
        syncPeriodic = JavaMethod("(JJ)Landroid/content/SyncRequest$Builder;")