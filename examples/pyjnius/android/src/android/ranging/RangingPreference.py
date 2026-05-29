from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangingPreference"]

class RangingPreference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/RangingPreference"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DEVICE_ROLE_INITIATOR = JavaStaticField("I")
    DEVICE_ROLE_RESPONDER = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getRangingParams = JavaMethod("()Landroid/ranging/RangingConfig;")
    getSessionConfig = JavaMethod("()Landroid/ranging/SessionConfig;")
    getDeviceRole = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/RangingPreference$Builder"
        __javaconstructor__ = [("(ILandroid/ranging/RangingConfig;)V", False)]
        setSessionConfig = JavaMethod("(Landroid/ranging/SessionConfig;)Landroid/ranging/RangingPreference$Builder;")
        build = JavaMethod("()Landroid/ranging/RangingPreference;")