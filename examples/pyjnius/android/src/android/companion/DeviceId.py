from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeviceId"]

class DeviceId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/DeviceId"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCustomId = JavaMethod("()Ljava/lang/String;")
    getMacAddress = JavaMethod("()Landroid/net/MacAddress;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/companion/DeviceId$Builder"
        __javaconstructor__ = [("()V", False)]
        setCustomId = JavaMethod("(Ljava/lang/String;)Landroid/companion/DeviceId$Builder;")
        setMacAddress = JavaMethod("(Landroid/net/MacAddress;)Landroid/companion/DeviceId$Builder;")
        build = JavaMethod("()Landroid/companion/DeviceId;")