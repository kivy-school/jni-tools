from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzw"]

class zzw(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/util/client/zzw"
    __javaconstructor__ = [("()V", False)]
    zza = JavaMethod("()I")
    zzb = JavaMethod("()I")
    zzc = JavaMethod("()Z")
    zzd = JavaStaticMethod("(Lorg/json/JSONObject;)Lcom/google/android/gms/ads/internal/util/client/zzw;")