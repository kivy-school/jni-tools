from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsbAccessory"]

class UsbAccessory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/usb/UsbAccessory"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getManufacturer = JavaMethod("()Ljava/lang/String;")
    getModel = JavaMethod("()Ljava/lang/String;")
    getDescription = JavaMethod("()Ljava/lang/String;")
    getVersion = JavaMethod("()Ljava/lang/String;")
    getUri = JavaMethod("()Ljava/lang/String;")
    getSerial = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")