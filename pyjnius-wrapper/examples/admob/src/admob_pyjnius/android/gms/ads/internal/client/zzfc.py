from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzfc"]

class zzfc(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzfc"
    __javaconstructor__ = [("()V", False)]
    zza = JavaMethod("(Landroid/content/Context;)Lcom/google/android/gms/ads/internal/client/zzcy;")