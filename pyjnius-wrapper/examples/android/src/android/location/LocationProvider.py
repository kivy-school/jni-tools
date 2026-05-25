from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocationProvider"]

class LocationProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/LocationProvider"
    AVAILABLE = JavaStaticField("I")
    OUT_OF_SERVICE = JavaStaticField("I")
    TEMPORARILY_UNAVAILABLE = JavaStaticField("I")
    getName = JavaMethod("()Ljava/lang/String;")
    meetsCriteria = JavaMethod("(Landroid/location/Criteria;)Z")
    requiresNetwork = JavaMethod("()Z")
    requiresSatellite = JavaMethod("()Z")
    requiresCell = JavaMethod("()Z")
    hasMonetaryCost = JavaMethod("()Z")
    supportsAltitude = JavaMethod("()Z")
    supportsSpeed = JavaMethod("()Z")
    supportsBearing = JavaMethod("()Z")
    getPowerRequirement = JavaMethod("()I")
    getAccuracy = JavaMethod("()I")