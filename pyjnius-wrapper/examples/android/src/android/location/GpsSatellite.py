from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GpsSatellite"]

class GpsSatellite(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GpsSatellite"
    getPrn = JavaMethod("()I")
    getSnr = JavaMethod("()F")
    getElevation = JavaMethod("()F")
    getAzimuth = JavaMethod("()F")
    hasEphemeris = JavaMethod("()Z")
    hasAlmanac = JavaMethod("()Z")
    usedInFix = JavaMethod("()Z")