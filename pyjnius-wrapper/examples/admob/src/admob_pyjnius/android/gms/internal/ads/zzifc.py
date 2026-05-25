from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzifc"]

class zzifc(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzifc"
    zza = JavaStaticField("[B")
    zzb = JavaStaticField("Ljava/nio/ByteBuffer;")
    zza = JavaStaticMethod("()I")
    zzb = JavaStaticMethod("(Z)I")