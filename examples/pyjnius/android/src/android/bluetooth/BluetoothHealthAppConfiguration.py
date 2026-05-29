from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothHealthAppConfiguration"]

class BluetoothHealthAppConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothHealthAppConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    getDataType = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    getRole = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")