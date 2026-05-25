from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AssociatedDevice"]

class AssociatedDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/AssociatedDevice"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getBluetoothDevice = JavaMethod("()Landroid/bluetooth/BluetoothDevice;")
    getBleDevice = JavaMethod("()Landroid/bluetooth/le/ScanResult;")
    getWifiDevice = JavaMethod("()Landroid/net/wifi/ScanResult;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")