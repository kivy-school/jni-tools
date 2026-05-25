from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothGattService"]

class BluetoothGattService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothGattService"
    __javaconstructor__ = [("(Ljava/util/UUID;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SERVICE_TYPE_PRIMARY = JavaStaticField("I")
    SERVICE_TYPE_SECONDARY = JavaStaticField("I")
    mCharacteristics = JavaField("Ljava/util/List;")
    mIncludedServices = JavaField("Ljava/util/List;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    addService = JavaMethod("(Landroid/bluetooth/BluetoothGattService;)Z")
    addCharacteristic = JavaMethod("(Landroid/bluetooth/BluetoothGattCharacteristic;)Z")
    getUuid = JavaMethod("()Ljava/util/UUID;")
    getInstanceId = JavaMethod("()I")
    getType = JavaMethod("()I")
    getIncludedServices = JavaMethod("()Ljava/util/List;")
    getCharacteristics = JavaMethod("()Ljava/util/List;")
    getCharacteristic = JavaMethod("(Ljava/util/UUID;)Landroid/bluetooth/BluetoothGattCharacteristic;")