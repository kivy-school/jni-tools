from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbzz"]

class zzbzz(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbzz"
    __javaconstructor__ = [("(Landroid/content/Context;Lcom/google/android/gms/ads/AdFormat;Lcom/google/android/gms/ads/internal/client/zzeh;Ljava/lang/String;)V", False)]
    zza = JavaStaticMethod("(Landroid/content/Context;)Lcom/google/android/gms/internal/ads/zzcet;")
    zzb = JavaMethod("(Lcom/google/android/gms/ads/query/QueryInfoGenerationCallback;)V")