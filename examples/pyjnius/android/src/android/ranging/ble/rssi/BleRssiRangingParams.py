from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BleRssiRangingParams"]

class BleRssiRangingParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/ble/rssi/BleRssiRangingParams"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getPeerBluetoothAddress = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getRangingUpdateRate = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/ble/rssi/BleRssiRangingParams$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setRangingUpdateRate = JavaMethod("(I)Landroid/ranging/ble/rssi/BleRssiRangingParams$Builder;")
        build = JavaMethod("()Landroid/ranging/ble/rssi/BleRssiRangingParams;")