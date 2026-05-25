from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbet"]

class zzbet(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbet"
    zze = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;Ljava/lang/String;)V")
    zzf = JavaMethod("()V")
    zzg = JavaMethod("([I)V")
    zzh = JavaMethod("([B)V")
    zzi = JavaMethod("(I)V")
    zzj = JavaMethod("(I)V")