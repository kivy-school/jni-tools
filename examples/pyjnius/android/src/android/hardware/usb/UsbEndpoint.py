from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsbEndpoint"]

class UsbEndpoint(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/usb/UsbEndpoint"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDirection = JavaMethod("()I")
    getEndpointNumber = JavaMethod("()I")
    getInterval = JavaMethod("()I")
    getMaxPacketSize = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()I")
    getAddress = JavaMethod("()I")
    getAttributes = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")