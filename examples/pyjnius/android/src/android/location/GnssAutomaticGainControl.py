from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GnssAutomaticGainControl"]

class GnssAutomaticGainControl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GnssAutomaticGainControl"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getConstellationType = JavaMethod("()I")
    getCarrierFrequencyHz = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getLevelDb = JavaMethod("()D")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssAutomaticGainControl$Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/location/GnssAutomaticGainControl;)V", False)]
        setLevelDb = JavaMethod("(D)Landroid/location/GnssAutomaticGainControl$Builder;")
        setCarrierFrequencyHz = JavaMethod("(J)Landroid/location/GnssAutomaticGainControl$Builder;")
        setConstellationType = JavaMethod("(I)Landroid/location/GnssAutomaticGainControl$Builder;")
        build = JavaMethod("()Landroid/location/GnssAutomaticGainControl;")