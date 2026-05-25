from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PollingFrame"]

class PollingFrame(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/cardemulation/PollingFrame"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    POLLING_LOOP_TYPE_A = JavaStaticField("I")
    POLLING_LOOP_TYPE_B = JavaStaticField("I")
    POLLING_LOOP_TYPE_F = JavaStaticField("I")
    POLLING_LOOP_TYPE_OFF = JavaStaticField("I")
    POLLING_LOOP_TYPE_ON = JavaStaticField("I")
    POLLING_LOOP_TYPE_UNKNOWN = JavaStaticField("I")
    getType = JavaMethod("()I")
    getData = JavaMethod("()[B")
    getVendorSpecificGain = JavaMethod("()I")
    getTimestamp = JavaMethod("()J")
    getTriggeredAutoTransact = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")