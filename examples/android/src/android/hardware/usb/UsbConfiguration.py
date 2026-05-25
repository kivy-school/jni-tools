from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsbConfiguration"]

class UsbConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/usb/UsbConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getId = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    isSelfPowered = JavaMethod("()Z")
    isRemoteWakeup = JavaMethod("()Z")
    getMaxPower = JavaMethod("()I")
    getInterfaceCount = JavaMethod("()I")
    getInterface = JavaMethod("(I)Landroid/hardware/usb/UsbInterface;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")