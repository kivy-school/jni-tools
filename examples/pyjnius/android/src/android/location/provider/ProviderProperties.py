from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProviderProperties"]

class ProviderProperties(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/provider/ProviderProperties"
    ACCURACY_COARSE = JavaStaticField("I")
    ACCURACY_FINE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    POWER_USAGE_HIGH = JavaStaticField("I")
    POWER_USAGE_LOW = JavaStaticField("I")
    POWER_USAGE_MEDIUM = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    hasMonetaryCost = JavaMethod("()Z")
    getPowerUsage = JavaMethod("()I")
    hasAltitudeSupport = JavaMethod("()Z")
    hasBearingSupport = JavaMethod("()Z")
    hasCellRequirement = JavaMethod("()Z")
    hasNetworkRequirement = JavaMethod("()Z")
    hasSatelliteRequirement = JavaMethod("()Z")
    hasSpeedSupport = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getAccuracy = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/provider/ProviderProperties$Builder"
        __javaconstructor__ = [("(Landroid/location/provider/ProviderProperties;)V", False), ("()V", False)]
        setHasAltitudeSupport = JavaMethod("(Z)Landroid/location/provider/ProviderProperties$Builder;")
        setHasBearingSupport = JavaMethod("(Z)Landroid/location/provider/ProviderProperties$Builder;")
        setHasCellRequirement = JavaMethod("(Z)Landroid/location/provider/ProviderProperties$Builder;")
        setHasMonetaryCost = JavaMethod("(Z)Landroid/location/provider/ProviderProperties$Builder;")
        setHasNetworkRequirement = JavaMethod("(Z)Landroid/location/provider/ProviderProperties$Builder;")
        setHasSatelliteRequirement = JavaMethod("(Z)Landroid/location/provider/ProviderProperties$Builder;")
        setHasSpeedSupport = JavaMethod("(Z)Landroid/location/provider/ProviderProperties$Builder;")
        setPowerUsage = JavaMethod("(I)Landroid/location/provider/ProviderProperties$Builder;")
        setAccuracy = JavaMethod("(I)Landroid/location/provider/ProviderProperties$Builder;")
        build = JavaMethod("()Landroid/location/provider/ProviderProperties;")