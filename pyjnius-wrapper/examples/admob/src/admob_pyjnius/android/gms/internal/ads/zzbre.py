from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbre"]

class zzbre(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbre"
    __javaconstructor__ = [("(Landroid/content/Context;Lcom/google/android/gms/ads/h5/OnH5AdsEventListener;)V", False)]
    zza = JavaMethod("(Ljava/lang/String;)Z")
    zzb = JavaMethod("()V")
    zzc = JavaStaticMethod("(Ljava/lang/String;)Z")