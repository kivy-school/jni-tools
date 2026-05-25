from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzidl"]

class zzidl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzidl"
    zza = JavaStaticField("Lcom/google/android/gms/internal/ads/zzidl;")
    zzr = JavaMethod("()Lcom/google/android/gms/internal/ads/zzidg;")
    zzb = JavaMethod("()I")
    zzs = JavaMethod("()Z")
    zzc = JavaMethod("(II)Lcom/google/android/gms/internal/ads/zzidl;")
    zzd = JavaMethod("(II)Lcom/google/android/gms/internal/ads/zzidl;")
    zzt = JavaStaticMethod("([BII)Lcom/google/android/gms/internal/ads/zzidl;")
    zzx = JavaStaticMethod("(Ljava/lang/String;)Lcom/google/android/gms/internal/ads/zzidl;")
    zzy = JavaStaticMethod("(Ljava/lang/Iterable;)Lcom/google/android/gms/internal/ads/zzidl;")
    zzz = JavaMethod("([BIII)V")
    zze = JavaMethod("([BIII)V")
    zzA = JavaMethod("()[B")
    zzf = JavaMethod("()Ljava/nio/ByteBuffer;")
    zzB = JavaMethod("(Ljava/nio/charset/Charset;)Ljava/lang/String;")
    zzh = JavaMethod("(Ljava/nio/charset/Charset;)Ljava/lang/String;")
    zzi = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    zzj = JavaMethod("(Lcom/google/android/gms/internal/ads/zzidl;)Z")
    hashCode = JavaMethod("()I")
    zzm = JavaMethod("()Lcom/google/android/gms/internal/ads/zzidp;")
    zzC = JavaStaticMethod("()Lcom/google/android/gms/internal/ads/zzidk;")
    zzp = JavaMethod("()I")
    zzq = JavaMethod("()Z")
    zzl = JavaMethod("(III)I")
    toString = JavaMethod("()Ljava/lang/String;")