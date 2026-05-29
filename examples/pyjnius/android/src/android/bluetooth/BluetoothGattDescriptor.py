from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCharacteristic = JavaMethod("()Landroid/bluetooth/BluetoothGattCharacteristic;")
    getValue = JavaMethod("()[B")
    getPermissions = JavaMethod("()I")
    setValue = JavaMethod("([B)Z")
    getUuid = JavaMethod("()Ljava/util/UUID;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")