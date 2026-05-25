from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgsz"]

class zzgsz(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgsz"
    zza = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    zzb = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    zzc = JavaStaticMethod("(C)Z")
    zzd = JavaStaticMethod("(C)Z")
    zze = JavaStaticMethod("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z")