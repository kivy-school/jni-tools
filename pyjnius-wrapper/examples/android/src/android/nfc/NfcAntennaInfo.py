from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcAntennaInfo"]

class NfcAntennaInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/NfcAntennaInfo"
    __javaconstructor__ = [("(IIZLjava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getDeviceWidth = JavaMethod("()I")
    getDeviceHeight = JavaMethod("()I")
    isDeviceFoldable = JavaMethod("()Z")
    getAvailableNfcAntennas = JavaMethod("()Ljava/util/List;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")