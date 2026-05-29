from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangingDevice"]

class RangingDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/RangingDevice"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getUuid = JavaMethod("()Ljava/util/UUID;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/RangingDevice$Builder"
        __javaconstructor__ = [("()V", False)]
        setUuid = JavaMethod("(Ljava/util/UUID;)Landroid/ranging/RangingDevice$Builder;")
        build = JavaMethod("()Landroid/ranging/RangingDevice;")