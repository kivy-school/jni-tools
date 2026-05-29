from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChangeLogsResponse"]

class ChangeLogsResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/changelog/ChangeLogsResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getUpsertedRecords = JavaMethod("()Ljava/util/List;")
    hasMorePages = JavaMethod("()Z")
    getDeletedLogs = JavaMethod("()Ljava/util/List;")
    getNextChangesToken = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class DeletedLog(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/changelog/ChangeLogsResponse$DeletedLog"
        __javaconstructor__ = [("(Ljava/lang/String;J)V", False)]
        getDeletedRecordId = JavaMethod("()Ljava/lang/String;")
        getDeletedTime = JavaMethod("()Ljava/time/Instant;")