from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScanResult"]

class ScanResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/ScanResult"
    __javaconstructor__ = [("(Landroid/bluetooth/BluetoothDevice;Landroid/bluetooth/le/ScanRecord;IJ)V", False), ("(Landroid/bluetooth/BluetoothDevice;IIIIIIILandroid/bluetooth/le/ScanRecord;J)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DATA_COMPLETE = JavaStaticField("I")
    DATA_TRUNCATED = JavaStaticField("I")
    PERIODIC_INTERVAL_NOT_PRESENT = JavaStaticField("I")
    PHY_UNUSED = JavaStaticField("I")
    SID_NOT_PRESENT = JavaStaticField("I")
    TX_POWER_NOT_PRESENT = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getDevice = JavaMethod("()Landroid/bluetooth/BluetoothDevice;")
    getScanRecord = JavaMethod("()Landroid/bluetooth/le/ScanRecord;")
    getRssi = JavaMethod("()I")
    getTimestampNanos = JavaMethod("()J")
    isLegacy = JavaMethod("()Z")
    isConnectable = JavaMethod("()Z")
    getDataStatus = JavaMethod("()I")
    getPrimaryPhy = JavaMethod("()I")
    getSecondaryPhy = JavaMethod("()I")
    getAdvertisingSid = JavaMethod("()I")
    getTxPower = JavaMethod("()I")
    getPeriodicAdvertisingInterval = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")