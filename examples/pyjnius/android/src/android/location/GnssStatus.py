from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getConstellationType = JavaMethod("(I)I")
    getCarrierFrequencyHz = JavaMethod("(I)F")
    getAzimuthDegrees = JavaMethod("(I)F")
    getBasebandCn0DbHz = JavaMethod("(I)F")
    getCn0DbHz = JavaMethod("(I)F")
    getElevationDegrees = JavaMethod("(I)F")
    getSatelliteCount = JavaMethod("()I")
    getSvid = JavaMethod("(I)I")
    hasAlmanacData = JavaMethod("(I)Z")
    hasBasebandCn0DbHz = JavaMethod("(I)Z")
    hasCarrierFrequencyHz = JavaMethod("(I)Z")
    hasEphemerisData = JavaMethod("(I)Z")
    usedInFix = JavaMethod("(I)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssStatus$Callback"
        __javaconstructor__ = [("()V", False)]
        onStarted = JavaMethod("()V")
        onStopped = JavaMethod("()V")
        onFirstFix = JavaMethod("(I)V")
        onSatelliteStatusChanged = JavaMethod("(Landroid/location/GnssStatus;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssStatus$Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/location/GnssStatus;")
        addSatellite = JavaMethod("(IIFFFZZZZFZF)Landroid/location/GnssStatus$Builder;")
        clearSatellites = JavaMethod("()Landroid/location/GnssStatus$Builder;")