from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsbEndpoint"]

class UsbEndpoint(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/usb/UsbEndpoint"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getAddress = JavaMethod("()I")
    getEndpointNumber = JavaMethod("()I")
    getDirection = JavaMethod("()I")
    getAttributes = JavaMethod("()I")
    getType = JavaMethod("()I")
    getMaxPacketSize = JavaMethod("()I")
    getInterval = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")