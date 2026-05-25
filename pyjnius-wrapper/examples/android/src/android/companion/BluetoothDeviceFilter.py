from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothDeviceFilter"]

class BluetoothDeviceFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/BluetoothDeviceFilter"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/companion/BluetoothDeviceFilter/Builder"
        __javaconstructor__ = [("()V", False)]
        setNamePattern = JavaMethod("(Ljava/util/regex/Pattern;)Landroid/companion/BluetoothDeviceFilter$Builder;")
        setAddress = JavaMethod("(Ljava/lang/String;)Landroid/companion/BluetoothDeviceFilter$Builder;")
        addServiceUuid = JavaMethod("(Landroid/os/ParcelUuid;Landroid/os/ParcelUuid;)Landroid/companion/BluetoothDeviceFilter$Builder;")
        build = JavaMethod("()Landroid/companion/BluetoothDeviceFilter;")