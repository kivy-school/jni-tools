from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GsmCellLocation"]

class GsmCellLocation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/gsm/GsmCellLocation"
    __javaconstructor__ = [("()V", False), ("(Landroid/os/Bundle;)V", False)]
    getPsc = JavaMethod("()I")
    getLac = JavaMethod("()I")
    getCid = JavaMethod("()I")
    setStateInvalid = JavaMethod("()V")
    setLacAndCid = JavaMethod("(II)V")
    fillInNotifierBundle = JavaMethod("(Landroid/os/Bundle;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")