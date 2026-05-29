from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GnssMeasurementsEvent"]

class GnssMeasurementsEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GnssMeasurementsEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    hasIsFullTracking = JavaMethod("()Z")
    getClock = JavaMethod("()Landroid/location/GnssClock;")
    getMeasurements = JavaMethod("()Ljava/util/Collection;")
    getGnssAutomaticGainControls = JavaMethod("()Ljava/util/Collection;")
    toString = JavaMethod("()Ljava/lang/String;")
    isFullTracking = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssMeasurementsEvent$Callback"
        __javaconstructor__ = [("()V", False)]
        STATUS_LOCATION_DISABLED = JavaStaticField("I")
        STATUS_NOT_ALLOWED = JavaStaticField("I")
        STATUS_NOT_SUPPORTED = JavaStaticField("I")
        STATUS_READY = JavaStaticField("I")
        onStatusChanged = JavaMethod("(I)V")
        onGnssMeasurementsReceived = JavaMethod("(Landroid/location/GnssMeasurementsEvent;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssMeasurementsEvent$Builder"
        __javaconstructor__ = [("(Landroid/location/GnssMeasurementsEvent;)V", False), ("()V", False)]
        setClock = JavaMethod("(Landroid/location/GnssClock;)Landroid/location/GnssMeasurementsEvent$Builder;")
        setIsFullTracking = JavaMethod("(Z)Landroid/location/GnssMeasurementsEvent$Builder;")
        setMeasurements = JavaMethod("(Ljava/util/Collection;)Landroid/location/GnssMeasurementsEvent$Builder;")
        clearIsFullTracking = JavaMethod("()Landroid/location/GnssMeasurementsEvent$Builder;")
        setGnssAutomaticGainControls = JavaMethod("(Ljava/util/Collection;)Landroid/location/GnssMeasurementsEvent$Builder;")
        build = JavaMethod("()Landroid/location/GnssMeasurementsEvent;")