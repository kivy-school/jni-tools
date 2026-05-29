from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcAntennaInfo"]

class NfcAntennaInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/NfcAntennaInfo"
    __javaconstructor__ = [("(IIZLjava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDeviceHeight = JavaMethod("()I")
    getAvailableNfcAntennas = JavaMethod("()Ljava/util/List;")
    getDeviceWidth = JavaMethod("()I")
    isDeviceFoldable = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")