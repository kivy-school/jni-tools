from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LensShadingMap"]

class LensShadingMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/LensShadingMap"
    MINIMUM_GAIN_FACTOR = JavaStaticField("F")
    getRowCount = JavaMethod("()I")
    getColumnCount = JavaMethod("()I")
    getGainFactorCount = JavaMethod("()I")
    getGainFactor = JavaMethod("(III)F")
    getGainFactorVector = JavaMethod("(II)Landroid/hardware/camera2/params/RggbChannelVector;")
    copyGainFactors = JavaMethod("([FI)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")