from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GeomagneticField"]

class GeomagneticField(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/GeomagneticField"
    __javaconstructor__ = [("(FFFJ)V", False)]
    getX = JavaMethod("()F")
    getY = JavaMethod("()F")
    getZ = JavaMethod("()F")
    getDeclination = JavaMethod("()F")
    getInclination = JavaMethod("()F")
    getHorizontalStrength = JavaMethod("()F")
    getFieldStrength = JavaMethod("()F")