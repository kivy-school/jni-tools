from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothHidDeviceAppSdpSettings"]

class BluetoothHidDeviceAppSdpSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/BluetoothHidDeviceAppSdpSettings"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;B[B)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getName = JavaMethod("()Ljava/lang/String;")
    getDescription = JavaMethod("()Ljava/lang/String;")
    getProvider = JavaMethod("()Ljava/lang/String;")
    getSubclass = JavaMethod("()B")
    getDescriptors = JavaMethod("()[B")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")