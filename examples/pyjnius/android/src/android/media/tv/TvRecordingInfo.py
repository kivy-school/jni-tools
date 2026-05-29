from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TvRecordingInfo"]

class TvRecordingInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TvRecordingInfo"
    __javaconstructor__ = [("(Ljava/lang/String;JJILjava/lang/String;Ljava/lang/String;JJLandroid/net/Uri;Landroid/net/Uri;Ljava/util/List;Landroid/net/Uri;JJ)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FRIDAY = JavaStaticField("I")
    MONDAY = JavaStaticField("I")
    RECORDING_ALL = JavaStaticField("I")
    RECORDING_IN_PROGRESS = JavaStaticField("I")
    RECORDING_SCHEDULED = JavaStaticField("I")
    SATURDAY = JavaStaticField("I")
    SUNDAY = JavaStaticField("I")
    THURSDAY = JavaStaticField("I")
    TUESDAY = JavaStaticField("I")
    WEDNESDAY = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getChannelUri = JavaMethod("()Landroid/net/Uri;")
    getContentRatings = JavaMethod("()Ljava/util/List;")
    getProgramUri = JavaMethod("()Landroid/net/Uri;")
    getEndPaddingMillis = JavaMethod("()J")
    getRecordingDurationMillis = JavaMethod("()J")
    getRecordingId = JavaMethod("()Ljava/lang/String;")
    getRecordingStartTimeMillis = JavaMethod("()J")
    getRecordingUri = JavaMethod("()Landroid/net/Uri;")
    getRepeatDays = JavaMethod("()I")
    getScheduledDurationMillis = JavaMethod("()J")
    getScheduledStartTimeMillis = JavaMethod("()J")
    getStartPaddingMillis = JavaMethod("()J")
    getName = JavaMethod("()Ljava/lang/String;")
    setName = JavaMethod("(Ljava/lang/String;)V")
    setDescription = JavaMethod("(Ljava/lang/String;)V")
    getDescription = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")