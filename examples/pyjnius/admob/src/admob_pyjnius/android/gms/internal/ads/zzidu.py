from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzidu"]

class zzidu(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzidu"
    zzb = JavaMethod("(II)V")
    zzc = JavaMethod("(II)V")
    zzd = JavaMethod("(II)V")
    zze = JavaMethod("(II)V")
    zzf = JavaMethod("(IJ)V")
    zzg = JavaMethod("(IJ)V")
    zzh = JavaMethod("(IZ)V")
    zzi = JavaMethod("(ILjava/lang/String;)V")
    zzj = JavaMethod("(ILcom/google/android/gms/internal/ads/zzidl;)V")
    zzm = JavaMethod("(ILcom/google/android/gms/internal/ads/zzifz;)V")
    zzn = JavaMethod("(ILcom/google/android/gms/internal/ads/zzidl;)V")
    zzq = JavaMethod("(I)V")
    zzr = JavaMethod("(I)V")
    zzs = JavaMethod("(I)V")
    zzt = JavaMethod("(J)V")
    zzu = JavaMethod("(J)V")
    zzw = JavaMethod("(Ljava/lang/String;)V")
    zzk = JavaMethod("(Lcom/google/android/gms/internal/ads/zzidl;)V")
    zzo = JavaMethod("(Lcom/google/android/gms/internal/ads/zzifz;)V")
    zzp = JavaMethod("(B)V")
    zzF = JavaStaticMethod("(I)I")
    zzG = JavaStaticMethod("(J)I")
    zzH = JavaStaticMethod("(Lcom/google/android/gms/internal/ads/zzifz;)I")
    zzx = JavaMethod("()V")
    zzy = JavaMethod("()I")
    zzI = JavaMethod("()V")