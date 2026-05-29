from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbln"]

class zzbln(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbln"
    zza = JavaMethod("(Ljava/lang/String;Z)Ljava/lang/Boolean;")
    zzb = JavaMethod("(Ljava/lang/String;J)Ljava/lang/Long;")
    zzc = JavaMethod("(Ljava/lang/String;D)Ljava/lang/Double;")
    zzd = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")