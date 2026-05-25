from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcdb"]

class zzcdb(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcdb"
    __javaconstructor__ = [("()V", False)]
    zza = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;Lcom/google/android/gms/internal/ads/zzbvj;)Lcom/google/android/gms/internal/ads/zzccp;")