from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LensShadingMap"]

class LensShadingMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/LensShadingMap"
    MINIMUM_GAIN_FACTOR = JavaStaticField("F")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getGainFactorCount = JavaMethod("()I")
    getGainFactor = JavaMethod("(III)F")
    copyGainFactors = JavaMethod("([FI)V")
    getGainFactorVector = JavaMethod("(II)Landroid/hardware/camera2/params/RggbChannelVector;")
    getColumnCount = JavaMethod("()I")
    getRowCount = JavaMethod("()I")