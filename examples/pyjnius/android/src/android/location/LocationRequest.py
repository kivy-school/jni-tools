from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocationRequest"]

class LocationRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/LocationRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PASSIVE_INTERVAL = JavaStaticField("J")
    QUALITY_BALANCED_POWER_ACCURACY = JavaStaticField("I")
    QUALITY_HIGH_ACCURACY = JavaStaticField("I")
    QUALITY_LOW_POWER = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDurationMillis = JavaMethod("()J")
    getIntervalMillis = JavaMethod("()J")
    getMaxUpdateDelayMillis = JavaMethod("()J")
    getMaxUpdates = JavaMethod("()I")
    getMinUpdateDistanceMeters = JavaMethod("()F")
    getMinUpdateIntervalMillis = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getQuality = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/LocationRequest$Builder"
        __javaconstructor__ = [("(J)V", False), ("(Landroid/location/LocationRequest;)V", False)]
        setQuality = JavaMethod("(I)Landroid/location/LocationRequest$Builder;")
        setMaxUpdates = JavaMethod("(I)Landroid/location/LocationRequest$Builder;")
        clearMinUpdateIntervalMillis = JavaMethod("()Landroid/location/LocationRequest$Builder;")
        setMaxUpdateDelayMillis = JavaMethod("(J)Landroid/location/LocationRequest$Builder;")
        setMinUpdateDistanceMeters = JavaMethod("(F)Landroid/location/LocationRequest$Builder;")
        setMinUpdateIntervalMillis = JavaMethod("(J)Landroid/location/LocationRequest$Builder;")
        setDurationMillis = JavaMethod("(J)Landroid/location/LocationRequest$Builder;")
        setIntervalMillis = JavaMethod("(J)Landroid/location/LocationRequest$Builder;")
        build = JavaMethod("()Landroid/location/LocationRequest;")