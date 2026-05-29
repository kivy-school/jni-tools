from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RawInitiatorRangingConfig"]

class RawInitiatorRangingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/raw/RawInitiatorRangingConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    RANGING_SESSION_OOB = JavaStaticField("I")
    RANGING_SESSION_RAW = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getRawRangingDevices = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/raw/RawInitiatorRangingConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/ranging/raw/RawInitiatorRangingConfig;")
        addRawRangingDevices = JavaMethod("(Ljava/util/List;)Landroid/ranging/raw/RawInitiatorRangingConfig$Builder;")
        addRawRangingDevice = JavaMethod("(Landroid/ranging/raw/RawRangingDevice;)Landroid/ranging/raw/RawInitiatorRangingConfig$Builder;")