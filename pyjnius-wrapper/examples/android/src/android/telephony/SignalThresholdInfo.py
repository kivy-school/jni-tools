from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    getRadioAccessNetworkType = JavaMethod("()I")
    getSignalMeasurementType = JavaMethod("()I")
    getHysteresisDb = JavaMethod("()I")
    getThresholds = JavaMethod("()[I")
    getMinimumNumberOfThresholdsAllowed = JavaStaticMethod("()I")
    getMaximumNumberOfThresholdsAllowed = JavaStaticMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/SignalThresholdInfo/Builder"
        __javaconstructor__ = [("()V", False)]
        setRadioAccessNetworkType = JavaMethod("(I)Landroid/telephony/SignalThresholdInfo$Builder;")
        setSignalMeasurementType = JavaMethod("(I)Landroid/telephony/SignalThresholdInfo$Builder;")
        setHysteresisDb = JavaMethod("(I)Landroid/telephony/SignalThresholdInfo$Builder;")
        setThresholds = JavaMethod("([I)Landroid/telephony/SignalThresholdInfo$Builder;")
        build = JavaMethod("()Landroid/telephony/SignalThresholdInfo;")