from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RttRangingParams"]

class RttRangingParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/wifi/rtt/RttRangingParams"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getMatchFilter = JavaMethod("()[B")
    getServiceName = JavaMethod("()Ljava/lang/String;")
    isPeriodicRangingHwFeatureEnabled = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getRangingUpdateRate = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/wifi/rtt/RttRangingParams$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setRangingUpdateRate = JavaMethod("(I)Landroid/ranging/wifi/rtt/RttRangingParams$Builder;")
        setMatchFilter = JavaMethod("([B)Landroid/ranging/wifi/rtt/RttRangingParams$Builder;")
        setPeriodicRangingHwFeatureEnabled = JavaMethod("(Z)Landroid/ranging/wifi/rtt/RttRangingParams$Builder;")
        build = JavaMethod("()Landroid/ranging/wifi/rtt/RttRangingParams;")