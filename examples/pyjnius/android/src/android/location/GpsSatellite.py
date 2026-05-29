from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GpsSatellite"]

class GpsSatellite(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/location/GpsSatellite"
    hasEphemeris = JavaMethod("()Z")
    hasAlmanac = JavaMethod("()Z")
    getSnr = JavaMethod("()F")
    usedInFix = JavaMethod("()Z")
    getElevation = JavaMethod("()F")
    getAzimuth = JavaMethod("()F")
    getPrn = JavaMethod("()I")