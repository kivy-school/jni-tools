from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProviderProperties"]

class ProviderProperties(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/provider/ProviderProperties"
    ACCURACY_COARSE = JavaStaticField("I")
    ACCURACY_FINE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    POWER_USAGE_HIGH = JavaStaticField("I")
    POWER_USAGE_LOW = JavaStaticField("I")
    POWER_USAGE_MEDIUM = JavaStaticField("I")
    hasNetworkRequirement = JavaMethod("()Z")
    hasSatelliteRequirement = JavaMethod("()Z")
    hasCellRequirement = JavaMethod("()Z")
    hasMonetaryCost = JavaMethod("()Z")
    hasAltitudeSupport = JavaMethod("()Z")
    hasSpeedSupport = JavaMethod("()Z")
    hasBearingSupport = JavaMethod("()Z")
    getPowerUsage = JavaMethod("()I")
    getAccuracy = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/provider/ProviderProperties/Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/location/provider/ProviderProperties;)V", False)]
        setHasNetworkRequirement = JavaMethod("(Z)Landroid/location/provider/ProviderProperties$Builder;")
        setHasSatelliteRequirement = JavaMethod("(Z)Landroid/location/provider/ProviderProperties$Builder;")
        setHasCellRequirement = JavaMethod("(Z)Landroid/location/provider/ProviderProperties$Builder;")
        setHasMonetaryCost = JavaMethod("(Z)Landroid/location/provider/ProviderProperties$Builder;")
        setHasAltitudeSupport = JavaMethod("(Z)Landroid/location/provider/ProviderProperties$Builder;")
        setHasSpeedSupport = JavaMethod("(Z)Landroid/location/provider/ProviderProperties$Builder;")
        setHasBearingSupport = JavaMethod("(Z)Landroid/location/provider/ProviderProperties$Builder;")
        setPowerUsage = JavaMethod("(I)Landroid/location/provider/ProviderProperties$Builder;")
        setAccuracy = JavaMethod("(I)Landroid/location/provider/ProviderProperties$Builder;")
        build = JavaMethod("()Landroid/location/provider/ProviderProperties;")