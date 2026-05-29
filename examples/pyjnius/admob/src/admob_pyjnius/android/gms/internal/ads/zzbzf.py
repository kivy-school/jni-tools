from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbzf"]

class zzbzf(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbzf"
    __javaconstructor__ = [("()V", False)]
    zza = JavaMethod("(Landroid/app/Activity;)Lcom/google/android/gms/internal/ads/zzbzi;")