from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocationProvider"]

class LocationProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/LocationProvider"
    AVAILABLE = JavaStaticField("I")
    OUT_OF_SERVICE = JavaStaticField("I")
    TEMPORARILY_UNAVAILABLE = JavaStaticField("I")
    requiresNetwork = JavaMethod("()Z")
    requiresSatellite = JavaMethod("()Z")
    requiresCell = JavaMethod("()Z")
    hasMonetaryCost = JavaMethod("()Z")
    supportsAltitude = JavaMethod("()Z")
    supportsSpeed = JavaMethod("()Z")
    supportsBearing = JavaMethod("()Z")
    getPowerRequirement = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    getAccuracy = JavaMethod("()I")
    meetsCriteria = JavaMethod("(Landroid/location/Criteria;)Z")