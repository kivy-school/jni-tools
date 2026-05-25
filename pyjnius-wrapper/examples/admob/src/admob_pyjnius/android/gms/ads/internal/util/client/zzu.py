from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzu"]

class zzu(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/util/client/zzu"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/lang/String;)V", False)]
    zzb = JavaMethod("()Ljava/lang/String;")
    zza = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/internal/util/client/zzt;")
    zzc = JavaMethod("(Ljava/lang/String;Ljava/util/Map;)Lcom/google/android/gms/ads/internal/util/client/zzt;")