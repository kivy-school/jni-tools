from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class RttRangingParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/wifi/rtt/RttRangingParams"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getRangingUpdateRate = JavaMethod("()I")
    getMatchFilter = JavaMethod("()[B")
    getServiceName = JavaMethod("()Ljava/lang/String;")
    isPeriodicRangingHwFeatureEnabled = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/wifi/rtt/RttRangingParams$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setRangingUpdateRate = JavaMethod("(I)Landroid/ranging/wifi/rtt/RttRangingParams$Builder;")
        setMatchFilter = JavaMethod("([B)Landroid/ranging/wifi/rtt/RttRangingParams$Builder;")
        setPeriodicRangingHwFeatureEnabled = JavaMethod("(Z)Landroid/ranging/wifi/rtt/RttRangingParams$Builder;")
        build = JavaMethod("()Landroid/ranging/wifi/rtt/RttRangingParams;")

class RttRangingCapabilities(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/wifi/rtt/RttRangingCapabilities"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    hasPeriodicRangingHardwareFeature = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")