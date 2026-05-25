from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncResult"]

class SyncResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/SyncResult"
    __javaconstructor__ = [("()V", False)]
    ALREADY_IN_PROGRESS = JavaStaticField("Landroid/content/SyncResult;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    databaseError = JavaField("Z")
    delayUntil = JavaField("J")
    fullSyncRequested = JavaField("Z")
    moreRecordsToGet = JavaField("Z")
    partialSyncUnavailable = JavaField("Z")
    stats = JavaField("Landroid/content/SyncStats;")
    syncAlreadyInProgress = JavaField("Z")
    tooManyDeletions = JavaField("Z")
    tooManyRetries = JavaField("Z")
    hasHardError = JavaMethod("()Z")
    hasSoftError = JavaMethod("()Z")
    hasError = JavaMethod("()Z")
    madeSomeProgress = JavaMethod("()Z")
    clear = JavaMethod("()V")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    toDebugString = JavaMethod("()Ljava/lang/String;")