from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScanSettings"]

class ScanSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/ScanSettings"
    AUTO_BATCH_MIN_REPORT_DELAY_MILLIS = JavaStaticField("J")
    CALLBACK_TYPE_ALL_MATCHES = JavaStaticField("I")
    CALLBACK_TYPE_ALL_MATCHES_AUTO_BATCH = JavaStaticField("I")
    CALLBACK_TYPE_FIRST_MATCH = JavaStaticField("I")
    CALLBACK_TYPE_MATCH_LOST = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    MATCH_MODE_AGGRESSIVE = JavaStaticField("I")
    MATCH_MODE_STICKY = JavaStaticField("I")
    MATCH_NUM_FEW_ADVERTISEMENT = JavaStaticField("I")
    MATCH_NUM_MAX_ADVERTISEMENT = JavaStaticField("I")
    MATCH_NUM_ONE_ADVERTISEMENT = JavaStaticField("I")
    PHY_LE_ALL_SUPPORTED = JavaStaticField("I")
    SCAN_MODE_BALANCED = JavaStaticField("I")
    SCAN_MODE_LOW_LATENCY = JavaStaticField("I")
    SCAN_MODE_LOW_POWER = JavaStaticField("I")
    SCAN_MODE_OPPORTUNISTIC = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getScanMode = JavaMethod("()I")
    getLegacy = JavaMethod("()Z")
    getPhy = JavaMethod("()I")
    getCallbackType = JavaMethod("()I")
    getScanResultType = JavaMethod("()I")
    getReportDelayMillis = JavaMethod("()J")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/bluetooth/le/ScanSettings$Builder"
        __javaconstructor__ = [("()V", False)]
        setMatchMode = JavaMethod("(I)Landroid/bluetooth/le/ScanSettings$Builder;")
        setNumOfMatches = JavaMethod("(I)Landroid/bluetooth/le/ScanSettings$Builder;")
        setPhy = JavaMethod("(I)Landroid/bluetooth/le/ScanSettings$Builder;")
        setReportDelay = JavaMethod("(J)Landroid/bluetooth/le/ScanSettings$Builder;")
        setLegacy = JavaMethod("(Z)Landroid/bluetooth/le/ScanSettings$Builder;")
        setScanMode = JavaMethod("(I)Landroid/bluetooth/le/ScanSettings$Builder;")
        setCallbackType = JavaMethod("(I)Landroid/bluetooth/le/ScanSettings$Builder;")
        build = JavaMethod("()Landroid/bluetooth/le/ScanSettings;")