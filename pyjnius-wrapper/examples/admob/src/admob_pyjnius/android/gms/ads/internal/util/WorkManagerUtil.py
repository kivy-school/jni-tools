from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WorkManagerUtil"]

class WorkManagerUtil(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/util/WorkManagerUtil"
    __javaconstructor__ = [("()V", False)]
    zze = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;Ljava/lang/String;Ljava/lang/String;)Z")
    zzg = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;Lcom/google/android/gms/ads/internal/offline/buffering/zza;)Z")
    zzf = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")