from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncStats"]

class SyncStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/SyncStats"
    __javaconstructor__ = [("()V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    numAuthExceptions = JavaField("J")
    numConflictDetectedExceptions = JavaField("J")
    numDeletes = JavaField("J")
    numEntries = JavaField("J")
    numInserts = JavaField("J")
    numIoExceptions = JavaField("J")
    numParseExceptions = JavaField("J")
    numSkippedEntries = JavaField("J")
    numUpdates = JavaField("J")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    clear = JavaMethod("()V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")