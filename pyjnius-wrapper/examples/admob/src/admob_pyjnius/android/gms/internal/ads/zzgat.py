from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgat"]

class zzgat(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgat"
    zza = JavaMethod("(I)Ljava/util/concurrent/ExecutorService;")
    zzb = JavaMethod("(ILjava/util/concurrent/ThreadFactory;I)Ljava/util/concurrent/ExecutorService;")
    zzc = JavaMethod("(I)Ljava/util/concurrent/ExecutorService;")
    zzd = JavaMethod("(Ljava/util/concurrent/ThreadFactory;I)Ljava/util/concurrent/ExecutorService;")