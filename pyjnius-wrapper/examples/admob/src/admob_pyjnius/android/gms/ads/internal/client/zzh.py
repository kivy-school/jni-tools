from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzh"]

class zzh(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzh"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/AdLoadCallback;Ljava/lang/Object;)V", False)]
    zzb = JavaMethod("()V")
    zzc = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")