from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GnssAntennaInfo"]

class GnssAntennaInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GnssAntennaInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPhaseCenterOffset = JavaMethod("()Landroid/location/GnssAntennaInfo$PhaseCenterOffset;")
    getCarrierFrequencyMHz = JavaMethod("()D")
    getPhaseCenterVariationCorrections = JavaMethod("()Landroid/location/GnssAntennaInfo$SphericalCorrections;")
    getSignalGainCorrections = JavaMethod("()Landroid/location/GnssAntennaInfo$SphericalCorrections;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class SphericalCorrections(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssAntennaInfo$SphericalCorrections"
        __javaconstructor__ = [("([[D[[D)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        getCorrectionUncertaintiesArray = JavaMethod("()[[D")
        getCorrectionsArray = JavaMethod("()[[D")
        getDeltaPhi = JavaMethod("()D")
        getDeltaTheta = JavaMethod("()D")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")

    class PhaseCenterOffset(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssAntennaInfo$PhaseCenterOffset"
        __javaconstructor__ = [("(DDDDDD)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        getZOffsetMm = JavaMethod("()D")
        getXOffsetMm = JavaMethod("()D")
        getYOffsetMm = JavaMethod("()D")
        getXOffsetUncertaintyMm = JavaMethod("()D")
        getYOffsetUncertaintyMm = JavaMethod("()D")
        getZOffsetUncertaintyMm = JavaMethod("()D")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")

    class Listener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssAntennaInfo$Listener"
        onGnssAntennaInfoReceived = JavaMethod("(Ljava/util/List;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssAntennaInfo$Builder"
        __javaconstructor__ = [("(DLandroid/location/GnssAntennaInfo$PhaseCenterOffset;)V", False), ("(Landroid/location/GnssAntennaInfo;)V", False), ("()V", False)]
        setCarrierFrequencyMHz = JavaMethod("(D)Landroid/location/GnssAntennaInfo$Builder;")
        setPhaseCenterOffset = JavaMethod("(Landroid/location/GnssAntennaInfo$PhaseCenterOffset;)Landroid/location/GnssAntennaInfo$Builder;")
        setPhaseCenterVariationCorrections = JavaMethod("(Landroid/location/GnssAntennaInfo$SphericalCorrections;)Landroid/location/GnssAntennaInfo$Builder;")
        setSignalGainCorrections = JavaMethod("(Landroid/location/GnssAntennaInfo$SphericalCorrections;)Landroid/location/GnssAntennaInfo$Builder;")
        build = JavaMethod("()Landroid/location/GnssAntennaInfo;")