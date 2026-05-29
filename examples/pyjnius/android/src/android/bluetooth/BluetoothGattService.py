from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothGattService"]

class BluetoothGattService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothGattService"
    __javaconstructor__ = [("(Ljava/util/UUID;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SERVICE_TYPE_PRIMARY = JavaStaticField("I")
    SERVICE_TYPE_SECONDARY = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    addService = JavaMethod("(Landroid/bluetooth/BluetoothGattService;)Z")
    getInstanceId = JavaMethod("()I")
    getCharacteristic = JavaMethod("(Ljava/util/UUID;)Landroid/bluetooth/BluetoothGattCharacteristic;")
    addCharacteristic = JavaMethod("(Landroid/bluetooth/BluetoothGattCharacteristic;)Z")
    getCharacteristics = JavaMethod("()Ljava/util/List;")
    getIncludedServices = JavaMethod("()Ljava/util/List;")
    getType = JavaMethod("()I")
    getUuid = JavaMethod("()Ljava/util/UUID;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")