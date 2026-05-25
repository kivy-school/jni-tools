from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothHidDeviceAppQosSettings"]

class BluetoothHidDeviceAppQosSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothHidDeviceAppQosSettings"
    __javaconstructor__ = [("(IIIIII)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    MAX = JavaStaticField("I")
    SERVICE_BEST_EFFORT = JavaStaticField("I")
    SERVICE_GUARANTEED = JavaStaticField("I")
    SERVICE_NO_TRAFFIC = JavaStaticField("I")
    getServiceType = JavaMethod("()I")
    getTokenRate = JavaMethod("()I")
    getTokenBucketSize = JavaMethod("()I")
    getPeakBandwidth = JavaMethod("()I")
    getLatency = JavaMethod("()I")
    getDelayVariation = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")