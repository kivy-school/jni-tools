from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OisSample"]

class OisSample(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/OisSample"
    __javaconstructor__ = [("(JFF)V", False)]
    getTimestamp = JavaMethod("()J")
    getXshift = JavaMethod("()F")
    getYshift = JavaMethod("()F")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")