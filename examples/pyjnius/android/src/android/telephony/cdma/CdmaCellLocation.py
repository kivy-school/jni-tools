from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CdmaCellLocation"]

class CdmaCellLocation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/cdma/CdmaCellLocation"
    __javaconstructor__ = [("()V", False), ("(Landroid/os/Bundle;)V", False)]
    setStateInvalid = JavaMethod("()V")
    fillInNotifierBundle = JavaMethod("(Landroid/os/Bundle;)V")
    getBaseStationId = JavaMethod("()I")
    convertQuartSecToDecDegrees = JavaStaticMethod("(I)D")
    getBaseStationLatitude = JavaMethod("()I")
    getBaseStationLongitude = JavaMethod("()I")
    setCellLocationData = JavaMultipleMethod([("(III)V", False, False), ("(IIIII)V", False, False)])
    getSystemId = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getNetworkId = JavaMethod("()I")