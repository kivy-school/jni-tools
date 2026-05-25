from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GnssNavigationMessage"]

class GnssNavigationMessage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GnssNavigationMessage"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STATUS_PARITY_PASSED = JavaStaticField("I")
    STATUS_PARITY_REBUILT = JavaStaticField("I")
    STATUS_UNKNOWN = JavaStaticField("I")
    TYPE_BDS_CNAV1 = JavaStaticField("I")
    TYPE_BDS_CNAV2 = JavaStaticField("I")
    TYPE_BDS_D1 = JavaStaticField("I")
    TYPE_BDS_D2 = JavaStaticField("I")
    TYPE_GAL_F = JavaStaticField("I")
    TYPE_GAL_I = JavaStaticField("I")
    TYPE_GLO_L1CA = JavaStaticField("I")
    TYPE_GPS_CNAV2 = JavaStaticField("I")
    TYPE_GPS_L1CA = JavaStaticField("I")
    TYPE_GPS_L2CNAV = JavaStaticField("I")
    TYPE_GPS_L5CNAV = JavaStaticField("I")
    TYPE_IRN_L1 = JavaStaticField("I")
    TYPE_IRN_L5 = JavaStaticField("I")
    TYPE_IRN_L5CA = JavaStaticField("I")
    TYPE_QZS_L1CA = JavaStaticField("I")
    TYPE_SBS = JavaStaticField("I")
    TYPE_UNKNOWN = JavaStaticField("I")
    getType = JavaMethod("()I")
    getSvid = JavaMethod("()I")
    getMessageId = JavaMethod("()I")
    getSubmessageId = JavaMethod("()I")
    getData = JavaMethod("()[B")
    getStatus = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssNavigationMessage/Callback"
        __javaconstructor__ = [("()V", False)]
        STATUS_LOCATION_DISABLED = JavaStaticField("I")
        STATUS_NOT_SUPPORTED = JavaStaticField("I")
        STATUS_READY = JavaStaticField("I")
        onGnssNavigationMessageReceived = JavaMethod("(Landroid/location/GnssNavigationMessage;)V")
        onStatusChanged = JavaMethod("(I)V")