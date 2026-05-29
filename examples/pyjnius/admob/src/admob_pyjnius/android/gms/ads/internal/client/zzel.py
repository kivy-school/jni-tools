from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzel"]

class zzel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzel"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    zza = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/appopen/AppOpenAd;")