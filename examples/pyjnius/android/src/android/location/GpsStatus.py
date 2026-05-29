from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GpsStatus"]

class GpsStatus(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GpsStatus"
    GPS_EVENT_FIRST_FIX = JavaStaticField("I")
    GPS_EVENT_SATELLITE_STATUS = JavaStaticField("I")
    GPS_EVENT_STARTED = JavaStaticField("I")
    GPS_EVENT_STOPPED = JavaStaticField("I")
    create = JavaStaticMethod("(Landroid/location/GnssStatus;I)Landroid/location/GpsStatus;")
    getMaxSatellites = JavaMethod("()I")
    getSatellites = JavaMethod("()Ljava/lang/Iterable;")
    getTimeToFirstFix = JavaMethod("()I")

    class NmeaListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GpsStatus$NmeaListener"
        onNmeaReceived = JavaMethod("(JLjava/lang/String;)V")

    class Listener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/location/GpsStatus$Listener"
        onGpsStatusChanged = JavaMethod("(I)V")