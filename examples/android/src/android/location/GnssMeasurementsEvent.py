from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GnssMeasurementsEvent"]

class GnssMeasurementsEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GnssMeasurementsEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getClock = JavaMethod("()Landroid/location/GnssClock;")
    getMeasurements = JavaMethod("()Ljava/util/Collection;")
    getGnssAutomaticGainControls = JavaMethod("()Ljava/util/Collection;")
    isFullTracking = JavaMethod("()Z")
    hasIsFullTracking = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssMeasurementsEvent/Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/location/GnssMeasurementsEvent;)V", False)]
        setClock = JavaMethod("(Landroid/location/GnssClock;)Landroid/location/GnssMeasurementsEvent$Builder;")
        setMeasurements = JavaMethod("(Ljava/util/Collection;)Landroid/location/GnssMeasurementsEvent$Builder;")
        setGnssAutomaticGainControls = JavaMethod("(Ljava/util/Collection;)Landroid/location/GnssMeasurementsEvent$Builder;")
        setIsFullTracking = JavaMethod("(Z)Landroid/location/GnssMeasurementsEvent$Builder;")
        clearIsFullTracking = JavaMethod("()Landroid/location/GnssMeasurementsEvent$Builder;")
        build = JavaMethod("()Landroid/location/GnssMeasurementsEvent;")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GnssMeasurementsEvent/Callback"
        __javaconstructor__ = [("()V", False)]
        STATUS_LOCATION_DISABLED = JavaStaticField("I")
        STATUS_NOT_ALLOWED = JavaStaticField("I")
        STATUS_NOT_SUPPORTED = JavaStaticField("I")
        STATUS_READY = JavaStaticField("I")
        onGnssMeasurementsReceived = JavaMethod("(Landroid/location/GnssMeasurementsEvent;)V")
        onStatusChanged = JavaMethod("(I)V")