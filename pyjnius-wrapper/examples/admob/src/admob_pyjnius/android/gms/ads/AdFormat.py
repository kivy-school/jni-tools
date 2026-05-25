from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdFormat"]

class AdFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/AdFormat"
    values = JavaStaticMethod("()[Lcom/google/android/gms/ads/AdFormat;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/AdFormat;")
    getValue = JavaMethod("()I")
    getAdFormat = JavaStaticMethod("(I)Lcom/google/android/gms/ads/AdFormat;")
    BANNER = JavaStaticField("Lcom/google/android/gms/ads/AdFormat;")
    INTERSTITIAL = JavaStaticField("Lcom/google/android/gms/ads/AdFormat;")
    REWARDED = JavaStaticField("Lcom/google/android/gms/ads/AdFormat;")
    REWARDED_INTERSTITIAL = JavaStaticField("Lcom/google/android/gms/ads/AdFormat;")
    NATIVE = JavaStaticField("Lcom/google/android/gms/ads/AdFormat;")
    APP_OPEN_AD = JavaStaticField("Lcom/google/android/gms/ads/AdFormat;")