from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zziej"]

class zziej(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zziej"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zziep;)V", False)]
    zza = JavaField("Lcom/google/android/gms/internal/ads/zziep;")
    zzbg = JavaMethod("()V")
    zzbh = JavaMethod("()V")
    zzbi = JavaMethod("()Z")
    zzbj = JavaMethod("()Lcom/google/android/gms/internal/ads/zziej;")
    zzbk = JavaMethod("()Lcom/google/android/gms/internal/ads/zziej;")
    zzbl = JavaMethod("()Lcom/google/android/gms/internal/ads/zziep;")
    zzbm = JavaMethod("()Lcom/google/android/gms/internal/ads/zziep;")
    zzbn = JavaMethod("(Lcom/google/android/gms/internal/ads/zziep;)Lcom/google/android/gms/internal/ads/zziej;")
    zzbo = JavaMethod("(Lcom/google/android/gms/internal/ads/zziep;)Lcom/google/android/gms/internal/ads/zziej;")
    zzbp = JavaMethod("([BIILcom/google/android/gms/internal/ads/zzidz;)Lcom/google/android/gms/internal/ads/zziej;")
    zzbq = JavaMethod("([BII)Lcom/google/android/gms/internal/ads/zziej;")
    zzbr = JavaMethod("(Lcom/google/android/gms/internal/ads/zzidp;Lcom/google/android/gms/internal/ads/zzidz;)Lcom/google/android/gms/internal/ads/zziej;")
    zzbs = JavaMethod("()Lcom/google/android/gms/internal/ads/zziep;")