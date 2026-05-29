from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzblr"]

class zzblr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzblr"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    zza = JavaMethod("(Lcom/google/android/gms/internal/ads/zzcal;)V")