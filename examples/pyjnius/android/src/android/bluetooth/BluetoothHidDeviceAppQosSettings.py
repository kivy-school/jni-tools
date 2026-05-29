from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothHidDeviceAppQosSettings"]

class BluetoothHidDeviceAppQosSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothHidDeviceAppQosSettings"
    __javaconstructor__ = [("(IIIIII)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    MAX = JavaStaticField("I")
    SERVICE_BEST_EFFORT = JavaStaticField("I")
    SERVICE_GUARANTEED = JavaStaticField("I")
    SERVICE_NO_TRAFFIC = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDelayVariation = JavaMethod("()I")
    getPeakBandwidth = JavaMethod("()I")
    getTokenRate = JavaMethod("()I")
    getTokenBucketSize = JavaMethod("()I")
    getServiceType = JavaMethod("()I")
    getLatency = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")