from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    getRecordingId = JavaMethod("()Ljava/lang/String;")
    getStartPaddingMillis = JavaMethod("()J")
    getEndPaddingMillis = JavaMethod("()J")
    getRepeatDays = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    setName = JavaMethod("(Ljava/lang/String;)V")
    getDescription = JavaMethod("()Ljava/lang/String;")
    setDescription = JavaMethod("(Ljava/lang/String;)V")
    getScheduledStartTimeMillis = JavaMethod("()J")
    getScheduledDurationMillis = JavaMethod("()J")
    getChannelUri = JavaMethod("()Landroid/net/Uri;")
    getProgramUri = JavaMethod("()Landroid/net/Uri;")
    getContentRatings = JavaMethod("()Ljava/util/List;")
    getRecordingUri = JavaMethod("()Landroid/net/Uri;")
    getRecordingStartTimeMillis = JavaMethod("()J")
    getRecordingDurationMillis = JavaMethod("()J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")