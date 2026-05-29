from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeviceHandle"]

class DeviceHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/oob/DeviceHandle"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getRangingDevice = JavaMethod("()Landroid/ranging/RangingDevice;")
    getTransportHandle = JavaMethod("()Landroid/ranging/oob/TransportHandle;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/oob/DeviceHandle$Builder"
        __javaconstructor__ = [("(Landroid/ranging/RangingDevice;Landroid/ranging/oob/TransportHandle;)V", False)]
        build = JavaMethod("()Landroid/ranging/oob/DeviceHandle;")