from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsbDevice"]

class UsbDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/usb/UsbDevice"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getDeviceName = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(I)Ljava/lang/String;", True, False)])
    getManufacturerName = JavaMethod("()Ljava/lang/String;")
    getProductName = JavaMethod("()Ljava/lang/String;")
    getVersion = JavaMethod("()Ljava/lang/String;")
    getSerialNumber = JavaMethod("()Ljava/lang/String;")
    getDeviceId = JavaMultipleMethod([("()I", False, False), ("(Ljava/lang/String;)I", True, False)])
    getVendorId = JavaMethod("()I")
    getProductId = JavaMethod("()I")
    getDeviceClass = JavaMethod("()I")
    getDeviceSubclass = JavaMethod("()I")
    getDeviceProtocol = JavaMethod("()I")
    getConfigurationCount = JavaMethod("()I")
    getConfiguration = JavaMethod("(I)Landroid/hardware/usb/UsbConfiguration;")
    getInterfaceCount = JavaMethod("()I")
    getInterface = JavaMethod("(I)Landroid/hardware/usb/UsbInterface;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")