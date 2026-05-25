from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CdmaCellLocation"]

class CdmaCellLocation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/cdma/CdmaCellLocation"
    __javaconstructor__ = [("()V", False), ("(Landroid/os/Bundle;)V", False)]
    getBaseStationId = JavaMethod("()I")
    getBaseStationLatitude = JavaMethod("()I")
    getBaseStationLongitude = JavaMethod("()I")
    getSystemId = JavaMethod("()I")
    getNetworkId = JavaMethod("()I")
    setStateInvalid = JavaMethod("()V")
    setCellLocationData = JavaMultipleMethod([("(III)V", False, False), ("(IIIII)V", False, False)])
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    fillInNotifierBundle = JavaMethod("(Landroid/os/Bundle;)V")
    convertQuartSecToDecDegrees = JavaStaticMethod("(I)D")