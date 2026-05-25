from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgui"]

class zzgui(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgui"
    zza = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    zzb = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    zzc = JavaStaticMethod("(Ljava/lang/String;)Z")
    zzd = JavaStaticMethod("(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;", varargs=True)