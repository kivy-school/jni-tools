from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothDeviceFilter"]

class BluetoothDeviceFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/BluetoothDeviceFilter"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/companion/BluetoothDeviceFilter$Builder"
        __javaconstructor__ = [("()V", False)]
        setNamePattern = JavaMethod("(Ljava/util/regex/Pattern;)Landroid/companion/BluetoothDeviceFilter$Builder;")
        setAddress = JavaMethod("(Ljava/lang/String;)Landroid/companion/BluetoothDeviceFilter$Builder;")
        addServiceUuid = JavaMethod("(Landroid/os/ParcelUuid;Landroid/os/ParcelUuid;)Landroid/companion/BluetoothDeviceFilter$Builder;")
        build = JavaMethod("()Landroid/companion/BluetoothDeviceFilter;")