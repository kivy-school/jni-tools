from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RawResponderRangingConfig"]

class RawResponderRangingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/raw/RawResponderRangingConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    RANGING_SESSION_OOB = JavaStaticField("I")
    RANGING_SESSION_RAW = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getRawRangingDevice = JavaMethod("()Landroid/ranging/raw/RawRangingDevice;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/raw/RawResponderRangingConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setRawRangingDevice = JavaMethod("(Landroid/ranging/raw/RawRangingDevice;)Landroid/ranging/raw/RawResponderRangingConfig$Builder;")
        build = JavaMethod("()Landroid/ranging/raw/RawResponderRangingConfig;")