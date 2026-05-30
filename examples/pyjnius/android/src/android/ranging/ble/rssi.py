from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class BleRssiRangingParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/ble/rssi/BleRssiRangingParams"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getRangingUpdateRate = JavaMethod("()I")
    getPeerBluetoothAddress = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/ble/rssi/BleRssiRangingParams$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setRangingUpdateRate = JavaMethod("(I)Landroid/ranging/ble/rssi/BleRssiRangingParams$Builder;")
        build = JavaMethod("()Landroid/ranging/ble/rssi/BleRssiRangingParams;")