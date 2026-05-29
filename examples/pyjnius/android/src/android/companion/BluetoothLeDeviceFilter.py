from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothLeDeviceFilter"]

class BluetoothLeDeviceFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/BluetoothLeDeviceFilter"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getRenamePrefixLengthLimit = JavaStaticMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/companion/BluetoothLeDeviceFilter$Builder"
        __javaconstructor__ = [("()V", False)]
        setNamePattern = JavaMethod("(Ljava/util/regex/Pattern;)Landroid/companion/BluetoothLeDeviceFilter$Builder;")
        setRenameFromBytes = JavaMethod("(Ljava/lang/String;Ljava/lang/String;IILjava/nio/ByteOrder;)Landroid/companion/BluetoothLeDeviceFilter$Builder;")
        setRenameFromName = JavaMethod("(Ljava/lang/String;Ljava/lang/String;II)Landroid/companion/BluetoothLeDeviceFilter$Builder;")
        setScanFilter = JavaMethod("(Landroid/bluetooth/le/ScanFilter;)Landroid/companion/BluetoothLeDeviceFilter$Builder;")
        setRawDataFilter = JavaMethod("([B[B)Landroid/companion/BluetoothLeDeviceFilter$Builder;")
        build = JavaMethod("()Landroid/companion/BluetoothLeDeviceFilter;")