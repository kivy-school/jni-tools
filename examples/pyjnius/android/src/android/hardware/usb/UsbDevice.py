from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsbDevice"]

class UsbDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/usb/UsbDevice"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getInterface = JavaMethod("(I)Landroid/hardware/usb/UsbInterface;")
    getInterfaceCount = JavaMethod("()I")
    getConfigurationCount = JavaMethod("()I")
    getVendorId = JavaMethod("()I")
    getDeviceName = JavaMultipleMethod([("(I)Ljava/lang/String;", True, False), ("()Ljava/lang/String;", False, False)])
    getDeviceProtocol = JavaMethod("()I")
    getDeviceSubclass = JavaMethod("()I")
    getManufacturerName = JavaMethod("()Ljava/lang/String;")
    getProductId = JavaMethod("()I")
    getProductName = JavaMethod("()Ljava/lang/String;")
    getDeviceClass = JavaMethod("()I")
    getConfiguration = JavaMethod("(I)Landroid/hardware/usb/UsbConfiguration;")
    getDeviceId = JavaMultipleMethod([("(Ljava/lang/String;)I", True, False), ("()I", False, False)])
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSerialNumber = JavaMethod("()Ljava/lang/String;")
    getVersion = JavaMethod("()Ljava/lang/String;")