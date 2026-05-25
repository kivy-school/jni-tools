from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgtf"]

class zzgtf(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgtf"
    __javaconstructor__ = [("()V", False)]
    zzc = JavaStaticMethod("()Lcom/google/android/gms/internal/ads/zzgtf;")
    zzd = JavaStaticMethod("(C)Lcom/google/android/gms/internal/ads/zzgtf;")
    zzb = JavaMethod("(C)Z")