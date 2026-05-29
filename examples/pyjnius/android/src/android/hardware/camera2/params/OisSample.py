from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OisSample"]

class OisSample(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/OisSample"
    __javaconstructor__ = [("(JFF)V", False)]
    getXshift = JavaMethod("()F")
    getYshift = JavaMethod("()F")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getTimestamp = JavaMethod("()J")