from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothGattDescriptor"]

class BluetoothGattDescriptor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothGattDescriptor"
    __javaconstructor__ = [("(Ljava/util/UUID;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DISABLE_NOTIFICATION_VALUE = JavaStaticField("[B")
    ENABLE_INDICATION_VALUE = JavaStaticField("[B")
    ENABLE_NOTIFICATION_VALUE = JavaStaticField("[B")
    PERMISSION_READ = JavaStaticField("I")
    PERMISSION_READ_ENCRYPTED = JavaStaticField("I")
    PERMISSION_READ_ENCRYPTED_MITM = JavaStaticField("I")
    PERMISSION_WRITE = JavaStaticField("I")
    PERMISSION_WRITE_ENCRYPTED = JavaStaticField("I")
    PERMISSION_WRITE_ENCRYPTED_MITM = JavaStaticField("I")
    PERMISSION_WRITE_SIGNED = JavaStaticField("I")
    PERMISSION_WRITE_SIGNED_MITM = JavaStaticField("I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getCharacteristic = JavaMethod("()Landroid/bluetooth/BluetoothGattCharacteristic;")
    getUuid = JavaMethod("()Ljava/util/UUID;")
    getPermissions = JavaMethod("()I")
    getValue = JavaMethod("()[B")
    setValue = JavaMethod("([B)Z")