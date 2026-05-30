from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ChangeLogsRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/changelog/ChangeLogsRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getPageSize = JavaMethod("()I")
    getToken = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/changelog/ChangeLogsRequest$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setPageSize = JavaMethod("(I)Landroid/health/connect/changelog/ChangeLogsRequest$Builder;")
        build = JavaMethod("()Landroid/health/connect/changelog/ChangeLogsRequest;")

class ChangeLogsResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/changelog/ChangeLogsResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getDeletedLogs = JavaMethod("()Ljava/util/List;")
    getUpsertedRecords = JavaMethod("()Ljava/util/List;")
    getNextChangesToken = JavaMethod("()Ljava/lang/String;")
    hasMorePages = JavaMethod("()Z")

    class DeletedLog(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/changelog/ChangeLogsResponse$DeletedLog"
        __javaconstructor__ = [("(Ljava/lang/String;J)V", False)]
        getDeletedTime = JavaMethod("()Ljava/time/Instant;")
        getDeletedRecordId = JavaMethod("()Ljava/lang/String;")

class ChangeLogTokenRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/changelog/ChangeLogTokenRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getRecordTypes = JavaMethod("()Ljava/util/Set;")
    getDataOriginFilters = JavaMethod("()Ljava/util/Set;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/changelog/ChangeLogTokenRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        addDataOriginFilter = JavaMethod("(Landroid/health/connect/datatypes/DataOrigin;)Landroid/health/connect/changelog/ChangeLogTokenRequest$Builder;")
        addRecordType = JavaMethod("(Ljava/lang/Class;)Landroid/health/connect/changelog/ChangeLogTokenRequest$Builder;")
        build = JavaMethod("()Landroid/health/connect/changelog/ChangeLogTokenRequest;")

class ChangeLogTokenResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/changelog/ChangeLogTokenResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getToken = JavaMethod("()Ljava/lang/String;")