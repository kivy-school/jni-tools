from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GsmCellLocation"]

class GsmCellLocation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/gsm/GsmCellLocation"
    __javaconstructor__ = [("()V", False), ("(Landroid/os/Bundle;)V", False)]
    getLac = JavaMethod("()I")
    getCid = JavaMethod("()I")
    getPsc = JavaMethod("()I")
    setStateInvalid = JavaMethod("()V")
    setLacAndCid = JavaMethod("(II)V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    fillInNotifierBundle = JavaMethod("(Landroid/os/Bundle;)V")