from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GnssAutomaticGainControl"]

class GnssAutomaticGainControl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GnssAutomaticGainControl"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLevelDb = JavaMethod("()D")
    getConstellationType = JavaMethod("()I")
    getCarrierFrequencyHz = JavaMethod("()J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssAutomaticGainControl/Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/location/GnssAutomaticGainControl;)V", False)]
        setLevelDb = JavaMethod("(D)Landroid/location/GnssAutomaticGainControl$Builder;")
        setConstellationType = JavaMethod("(I)Landroid/location/GnssAutomaticGainControl$Builder;")
        setCarrierFrequencyHz = JavaMethod("(J)Landroid/location/GnssAutomaticGainControl$Builder;")
        build = JavaMethod("()Landroid/location/GnssAutomaticGainControl;")