from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzey"]

class zzey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzey"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    zza = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/rewarded/RewardedAd;")