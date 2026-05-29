from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsbInterface"]

class UsbInterface(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/usb/UsbInterface"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getAlternateSetting = JavaMethod("()I")
    getEndpoint = JavaMethod("(I)Landroid/hardware/usb/UsbEndpoint;")
    getEndpointCount = JavaMethod("()I")
    getInterfaceClass = JavaMethod("()I")
    getInterfaceProtocol = JavaMethod("()I")
    getInterfaceSubclass = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")