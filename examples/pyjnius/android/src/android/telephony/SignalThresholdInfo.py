from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SignalThresholdInfo"]

class SignalThresholdInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/SignalThresholdInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SIGNAL_MEASUREMENT_TYPE_ECNO = JavaStaticField("I")
    SIGNAL_MEASUREMENT_TYPE_RSCP = JavaStaticField("I")
    SIGNAL_MEASUREMENT_TYPE_RSRP = JavaStaticField("I")
    SIGNAL_MEASUREMENT_TYPE_RSRQ = JavaStaticField("I")
    SIGNAL_MEASUREMENT_TYPE_RSSI = JavaStaticField("I")
    SIGNAL_MEASUREMENT_TYPE_RSSNR = JavaStaticField("I")
    SIGNAL_MEASUREMENT_TYPE_SSRSRP = JavaStaticField("I")
    SIGNAL_MEASUREMENT_TYPE_SSRSRQ = JavaStaticField("I")
    SIGNAL_MEASUREMENT_TYPE_SSSINR = JavaStaticField("I")
    SIGNAL_MEASUREMENT_TYPE_UNKNOWN = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getThresholds = JavaMethod("()[I")
    getHysteresisDb = JavaMethod("()I")
    getMaximumNumberOfThresholdsAllowed = JavaStaticMethod("()I")
    getMinimumNumberOfThresholdsAllowed = JavaStaticMethod("()I")
    getRadioAccessNetworkType = JavaMethod("()I")
    getSignalMeasurementType = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/SignalThresholdInfo$Builder"
        __javaconstructor__ = [("()V", False)]
        setHysteresisDb = JavaMethod("(I)Landroid/telephony/SignalThresholdInfo$Builder;")
        setThresholds = JavaMethod("([I)Landroid/telephony/SignalThresholdInfo$Builder;")
        setRadioAccessNetworkType = JavaMethod("(I)Landroid/telephony/SignalThresholdInfo$Builder;")
        setSignalMeasurementType = JavaMethod("(I)Landroid/telephony/SignalThresholdInfo$Builder;")
        build = JavaMethod("()Landroid/telephony/SignalThresholdInfo;")