from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzi"]

class zzi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzi"
    __javaconstructor__ = [("()V", False)]
    zza = JavaMethod("(Landroid/content/Context;Ljava/lang/String;Lcom/google/android/gms/internal/ads/zzbvj;)Lcom/google/android/gms/ads/internal/client/zzbq;")