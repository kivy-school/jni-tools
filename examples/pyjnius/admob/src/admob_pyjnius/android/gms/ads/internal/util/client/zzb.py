from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzb"]

class zzb(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/util/client/zzb"
    zza = JavaStaticField("Ljava/util/concurrent/ThreadPoolExecutor;")
    zzb = JavaStaticField("Ljava/util/concurrent/ExecutorService;")