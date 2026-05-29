from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GnssAntennaInfo"]

class GnssAntennaInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GnssAntennaInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getCarrierFrequencyMHz = JavaMethod("()D")
    getPhaseCenterOffset = JavaMethod("()Landroid/location/GnssAntennaInfo$PhaseCenterOffset;")
    getPhaseCenterVariationCorrections = JavaMethod("()Landroid/location/GnssAntennaInfo$SphericalCorrections;")
    getSignalGainCorrections = JavaMethod("()Landroid/location/GnssAntennaInfo$SphericalCorrections;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssAntennaInfo/Builder"
        __javaconstructor__ = [("()V", False), ("(DLandroid/location/GnssAntennaInfo$PhaseCenterOffset;)V", False), ("(Landroid/location/GnssAntennaInfo;)V", False)]
        setCarrierFrequencyMHz = JavaMethod("(D)Landroid/location/GnssAntennaInfo$Builder;")
        setPhaseCenterOffset = JavaMethod("(Landroid/location/GnssAntennaInfo$PhaseCenterOffset;)Landroid/location/GnssAntennaInfo$Builder;")
        setPhaseCenterVariationCorrections = JavaMethod("(Landroid/location/GnssAntennaInfo$SphericalCorrections;)Landroid/location/GnssAntennaInfo$Builder;")
        setSignalGainCorrections = JavaMethod("(Landroid/location/GnssAntennaInfo$SphericalCorrections;)Landroid/location/GnssAntennaInfo$Builder;")
        build = JavaMethod("()Landroid/location/GnssAntennaInfo;")

    class Listener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssAntennaInfo/Listener"
        onGnssAntennaInfoReceived = JavaMethod("(Ljava/util/List;)V")

    class PhaseCenterOffset(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssAntennaInfo/PhaseCenterOffset"
        __javaconstructor__ = [("(DDDDDD)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        getXOffsetMm = JavaMethod("()D")
        getXOffsetUncertaintyMm = JavaMethod("()D")
        getYOffsetMm = JavaMethod("()D")
        getYOffsetUncertaintyMm = JavaMethod("()D")
        getZOffsetMm = JavaMethod("()D")
        getZOffsetUncertaintyMm = JavaMethod("()D")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        toString = JavaMethod("()Ljava/lang/String;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class SphericalCorrections(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssAntennaInfo/SphericalCorrections"
        __javaconstructor__ = [("([[D[[D)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        getCorrectionsArray = JavaMethod("()[[D")
        getCorrectionUncertaintiesArray = JavaMethod("()[[D")
        getDeltaTheta = JavaMethod("()D")
        getDeltaPhi = JavaMethod("()D")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        toString = JavaMethod("()Ljava/lang/String;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")