from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UwbRangingCapabilities"]

class UwbRangingCapabilities(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/uwb/UwbRangingCapabilities"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getMinimumRangingInterval = JavaMethod("()Ljava/time/Duration;")
    getSupportedChannels = JavaMethod("()Ljava/util/List;")
    getSupportedConfigIds = JavaMethod("()Ljava/util/List;")
    getSupportedNotificationConfigurations = JavaMethod("()Ljava/util/List;")
    getSupportedPreambleIndexes = JavaMethod("()Ljava/util/List;")
    getSupportedRangingUpdateRates = JavaMethod("()Ljava/util/List;")
    getSupportedSlotDurations = JavaMethod("()Ljava/util/List;")
    isElevationAngleSupported = JavaMethod("()Z")
    isRangingIntervalReconfigurationSupported = JavaMethod("()Z")
    isAzimuthalAngleSupported = JavaMethod("()Z")
    isBackgroundRangingSupported = JavaMethod("()Z")
    isDistanceMeasurementSupported = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")