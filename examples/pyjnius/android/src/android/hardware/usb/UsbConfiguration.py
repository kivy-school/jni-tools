from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsbConfiguration"]

class UsbConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/usb/UsbConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()I")
    getInterface = JavaMethod("(I)Landroid/hardware/usb/UsbInterface;")
    getInterfaceCount = JavaMethod("()I")
    isRemoteWakeup = JavaMethod("()Z")
    isSelfPowered = JavaMethod("()Z")
    getMaxPower = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")