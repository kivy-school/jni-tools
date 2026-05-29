from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AssociatedDevice"]

class AssociatedDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/AssociatedDevice"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getWifiDevice = JavaMethod("()Landroid/net/wifi/ScanResult;")
    getBluetoothDevice = JavaMethod("()Landroid/bluetooth/BluetoothDevice;")
    getBleDevice = JavaMethod("()Landroid/bluetooth/le/ScanResult;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")