from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdValue"]

class AdValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/AdValue"
    getPrecisionType = JavaMethod("()I")
    getCurrencyCode = JavaMethod("()Ljava/lang/String;")
    getValueMicros = JavaMethod("()J")
    zza = JavaStaticMethod("(ILjava/lang/String;J)Lcom/google/android/gms/ads/AdValue;")

    class PrecisionType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/AdValue/PrecisionType"
        UNKNOWN = JavaStaticField("I")
        ESTIMATED = JavaStaticField("I")
        PUBLISHER_PROVIDED = JavaStaticField("I")
        PRECISE = JavaStaticField("I")