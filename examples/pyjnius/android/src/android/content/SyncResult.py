from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    clear = JavaMethod("()V")
    hasError = JavaMethod("()Z")
    hasHardError = JavaMethod("()Z")
    hasSoftError = JavaMethod("()Z")
    madeSomeProgress = JavaMethod("()Z")
    toDebugString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")