from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RawRangingDevice"]

class RawRangingDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/raw/RawRangingDevice"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    UPDATE_RATE_FREQUENT = JavaStaticField("I")
    UPDATE_RATE_INFREQUENT = JavaStaticField("I")
    UPDATE_RATE_NORMAL = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getCsRangingParams = JavaMethod("()Landroid/ranging/ble/cs/BleCsRangingParams;")
    getBleRssiRangingParams = JavaMethod("()Landroid/ranging/ble/rssi/BleRssiRangingParams;")
    getRttRangingParams = JavaMethod("()Landroid/ranging/wifi/rtt/RttRangingParams;")
    getUwbRangingParams = JavaMethod("()Landroid/ranging/uwb/UwbRangingParams;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getRangingDevice = JavaMethod("()Landroid/ranging/RangingDevice;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/raw/RawRangingDevice$Builder"
        __javaconstructor__ = [("()V", False)]
        setRangingDevice = JavaMethod("(Landroid/ranging/RangingDevice;)Landroid/ranging/raw/RawRangingDevice$Builder;")
        setCsRangingParams = JavaMethod("(Landroid/ranging/ble/cs/BleCsRangingParams;)Landroid/ranging/raw/RawRangingDevice$Builder;")
        setBleRssiRangingParams = JavaMethod("(Landroid/ranging/ble/rssi/BleRssiRangingParams;)Landroid/ranging/raw/RawRangingDevice$Builder;")
        setRttRangingParams = JavaMethod("(Landroid/ranging/wifi/rtt/RttRangingParams;)Landroid/ranging/raw/RawRangingDevice$Builder;")
        setUwbRangingParams = JavaMethod("(Landroid/ranging/uwb/UwbRangingParams;)Landroid/ranging/raw/RawRangingDevice$Builder;")
        build = JavaMethod("()Landroid/ranging/raw/RawRangingDevice;")