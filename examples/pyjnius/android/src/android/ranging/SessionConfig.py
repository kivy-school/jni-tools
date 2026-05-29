from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SessionConfig"]

class SessionConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/SessionConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getDataNotificationConfig = JavaMethod("()Landroid/ranging/DataNotificationConfig;")
    getRangingMeasurementsLimit = JavaMethod("()I")
    getSensorFusionParams = JavaMethod("()Landroid/ranging/SensorFusionParams;")
    isAngleOfArrivalNeeded = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/SessionConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setRangingMeasurementsLimit = JavaMethod("(I)Landroid/ranging/SessionConfig$Builder;")
        setSensorFusionParams = JavaMethod("(Landroid/ranging/SensorFusionParams;)Landroid/ranging/SessionConfig$Builder;")
        setAngleOfArrivalNeeded = JavaMethod("(Z)Landroid/ranging/SessionConfig$Builder;")
        setDataNotificationConfig = JavaMethod("(Landroid/ranging/DataNotificationConfig;)Landroid/ranging/SessionConfig$Builder;")
        build = JavaMethod("()Landroid/ranging/SessionConfig;")