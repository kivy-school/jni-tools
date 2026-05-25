from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocationRequest"]

class LocationRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/LocationRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PASSIVE_INTERVAL = JavaStaticField("J")
    QUALITY_BALANCED_POWER_ACCURACY = JavaStaticField("I")
    QUALITY_HIGH_ACCURACY = JavaStaticField("I")
    QUALITY_LOW_POWER = JavaStaticField("I")
    getQuality = JavaMethod("()I")
    getIntervalMillis = JavaMethod("()J")
    getDurationMillis = JavaMethod("()J")
    getMaxUpdates = JavaMethod("()I")
    getMinUpdateIntervalMillis = JavaMethod("()J")
    getMinUpdateDistanceMeters = JavaMethod("()F")
    getMaxUpdateDelayMillis = JavaMethod("()J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/LocationRequest/Builder"
        __javaconstructor__ = [("(J)V", False), ("(Landroid/location/LocationRequest;)V", False)]
        setIntervalMillis = JavaMethod("(J)Landroid/location/LocationRequest$Builder;")
        setQuality = JavaMethod("(I)Landroid/location/LocationRequest$Builder;")
        setDurationMillis = JavaMethod("(J)Landroid/location/LocationRequest$Builder;")
        setMaxUpdates = JavaMethod("(I)Landroid/location/LocationRequest$Builder;")
        setMinUpdateIntervalMillis = JavaMethod("(J)Landroid/location/LocationRequest$Builder;")
        clearMinUpdateIntervalMillis = JavaMethod("()Landroid/location/LocationRequest$Builder;")
        setMinUpdateDistanceMeters = JavaMethod("(F)Landroid/location/LocationRequest$Builder;")
        setMaxUpdateDelayMillis = JavaMethod("(J)Landroid/location/LocationRequest$Builder;")
        build = JavaMethod("()Landroid/location/LocationRequest;")