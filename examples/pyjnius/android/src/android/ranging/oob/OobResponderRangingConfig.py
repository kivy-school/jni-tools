from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OobResponderRangingConfig"]

class OobResponderRangingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/oob/OobResponderRangingConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    RANGING_SESSION_OOB = JavaStaticField("I")
    RANGING_SESSION_RAW = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getDeviceHandle = JavaMethod("()Landroid/ranging/oob/DeviceHandle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/oob/OobResponderRangingConfig$Builder"
        __javaconstructor__ = [("(Landroid/ranging/oob/DeviceHandle;)V", False)]
        build = JavaMethod("()Landroid/ranging/oob/OobResponderRangingConfig;")