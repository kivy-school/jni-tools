from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GnssStatus"]

class GnssStatus(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GnssStatus"
    CONSTELLATION_BEIDOU = JavaStaticField("I")
    CONSTELLATION_GALILEO = JavaStaticField("I")
    CONSTELLATION_GLONASS = JavaStaticField("I")
    CONSTELLATION_GPS = JavaStaticField("I")
    CONSTELLATION_IRNSS = JavaStaticField("I")
    CONSTELLATION_QZSS = JavaStaticField("I")
    CONSTELLATION_SBAS = JavaStaticField("I")
    CONSTELLATION_UNKNOWN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getSatelliteCount = JavaMethod("()I")
    getConstellationType = JavaMethod("(I)I")
    getSvid = JavaMethod("(I)I")
    getCn0DbHz = JavaMethod("(I)F")
    getElevationDegrees = JavaMethod("(I)F")
    getAzimuthDegrees = JavaMethod("(I)F")
    hasEphemerisData = JavaMethod("(I)Z")
    hasAlmanacData = JavaMethod("(I)Z")
    usedInFix = JavaMethod("(I)Z")
    hasCarrierFrequencyHz = JavaMethod("(I)Z")
    getCarrierFrequencyHz = JavaMethod("(I)F")
    hasBasebandCn0DbHz = JavaMethod("(I)Z")
    getBasebandCn0DbHz = JavaMethod("(I)F")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssStatus/Builder"
        __javaconstructor__ = [("()V", False)]
        addSatellite = JavaMethod("(IIFFFZZZZFZF)Landroid/location/GnssStatus$Builder;")
        clearSatellites = JavaMethod("()Landroid/location/GnssStatus$Builder;")
        build = JavaMethod("()Landroid/location/GnssStatus;")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssStatus/Callback"
        __javaconstructor__ = [("()V", False)]
        onStarted = JavaMethod("()V")
        onStopped = JavaMethod("()V")
        onFirstFix = JavaMethod("(I)V")
        onSatelliteStatusChanged = JavaMethod("(Landroid/location/GnssStatus;)V")