from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChangeLogsResponse"]

class ChangeLogsResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/changelog/ChangeLogsResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getUpsertedRecords = JavaMethod("()Ljava/util/List;")
    getDeletedLogs = JavaMethod("()Ljava/util/List;")
    getNextChangesToken = JavaMethod("()Ljava/lang/String;")
    hasMorePages = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class DeletedLog(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/changelog/ChangeLogsResponse/DeletedLog"
        __javaconstructor__ = [("(Ljava/lang/String;J)V", False)]
        getDeletedRecordId = JavaMethod("()Ljava/lang/String;")
        getDeletedTime = JavaMethod("()Ljava/time/Instant;")