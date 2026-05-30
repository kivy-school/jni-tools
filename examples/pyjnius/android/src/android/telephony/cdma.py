from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CdmaCellLocation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/cdma/CdmaCellLocation"
    __javaconstructor__ = [("()V", False), ("(Landroid/os/Bundle;)V", False)]
    getNetworkId = JavaMethod("()I")
    fillInNotifierBundle = JavaMethod("(Landroid/os/Bundle;)V")
    setStateInvalid = JavaMethod("()V")
    getSystemId = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    convertQuartSecToDecDegrees = JavaStaticMethod("(I)D")
    getBaseStationId = JavaMethod("()I")
    getBaseStationLatitude = JavaMethod("()I")
    getBaseStationLongitude = JavaMethod("()I")
    setCellLocationData = JavaMultipleMethod([("(IIIII)V", False, False), ("(III)V", False, False)])