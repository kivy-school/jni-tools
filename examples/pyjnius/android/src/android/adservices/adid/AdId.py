from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdId"]

class AdId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adid/AdId"
    __javaconstructor__ = [("(Ljava/lang/String;Z)V", False)]
    ZERO_OUT = JavaStaticField("Ljava/lang/String;")
    getAdId = JavaMethod("()Ljava/lang/String;")
    isLimitAdTrackingEnabled = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")