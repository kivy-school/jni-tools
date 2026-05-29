from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OobInitiatorRangingConfig"]

class OobInitiatorRangingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/oob/OobInitiatorRangingConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RANGING_MODE_AUTO = JavaStaticField("I")
    RANGING_MODE_FUSED = JavaStaticField("I")
    RANGING_MODE_HIGH_ACCURACY = JavaStaticField("I")
    RANGING_MODE_HIGH_ACCURACY_PREFERRED = JavaStaticField("I")
    SECURITY_LEVEL_BASIC = JavaStaticField("I")
    SECURITY_LEVEL_SECURE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    RANGING_SESSION_OOB = JavaStaticField("I")
    RANGING_SESSION_RAW = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getSecurityLevel = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getDeviceHandles = JavaMethod("()Ljava/util/List;")
    getSlowestRangingInterval = JavaMethod("()Ljava/time/Duration;")
    getFastestRangingInterval = JavaMethod("()Ljava/time/Duration;")
    getRangingIntervalRange = JavaMethod("()Landroid/util/Range;")
    getRangingMode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/oob/OobInitiatorRangingConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setSecurityLevel = JavaMethod("(I)Landroid/ranging/oob/OobInitiatorRangingConfig$Builder;")
        addDeviceHandle = JavaMethod("(Landroid/ranging/oob/DeviceHandle;)Landroid/ranging/oob/OobInitiatorRangingConfig$Builder;")
        setFastestRangingInterval = JavaMethod("(Ljava/time/Duration;)Landroid/ranging/oob/OobInitiatorRangingConfig$Builder;")
        setRangingMode = JavaMethod("(I)Landroid/ranging/oob/OobInitiatorRangingConfig$Builder;")
        setSlowestRangingInterval = JavaMethod("(Ljava/time/Duration;)Landroid/ranging/oob/OobInitiatorRangingConfig$Builder;")
        addDeviceHandles = JavaMethod("(Ljava/util/List;)Landroid/ranging/oob/OobInitiatorRangingConfig$Builder;")
        build = JavaMethod("()Landroid/ranging/oob/OobInitiatorRangingConfig;")