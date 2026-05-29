from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsbInterface"]

class UsbInterface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/usb/UsbInterface"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getId = JavaMethod("()I")
    getAlternateSetting = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    getInterfaceClass = JavaMethod("()I")
    getInterfaceSubclass = JavaMethod("()I")
    getInterfaceProtocol = JavaMethod("()I")
    getEndpointCount = JavaMethod("()I")
    getEndpoint = JavaMethod("(I)Landroid/hardware/usb/UsbEndpoint;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")