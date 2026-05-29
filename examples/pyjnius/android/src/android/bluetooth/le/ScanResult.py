from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTimestampNanos = JavaMethod("()J")
    getAdvertisingSid = JavaMethod("()I")
    getDataStatus = JavaMethod("()I")
    getPeriodicAdvertisingInterval = JavaMethod("()I")
    getPrimaryPhy = JavaMethod("()I")
    getScanRecord = JavaMethod("()Landroid/bluetooth/le/ScanRecord;")
    getSecondaryPhy = JavaMethod("()I")
    getTxPower = JavaMethod("()I")
    isConnectable = JavaMethod("()Z")
    isLegacy = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getRssi = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getDevice = JavaMethod("()Landroid/bluetooth/BluetoothDevice;")