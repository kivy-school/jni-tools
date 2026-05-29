from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getVendorSpecificGain = JavaMethod("()I")
    getTriggeredAutoTransact = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()I")
    getData = JavaMethod("()[B")
    getTimestamp = JavaMethod("()J")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")