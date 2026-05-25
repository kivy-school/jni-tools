from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzccu"]

class zzccu(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzccu"
    zze = JavaMethod("()V")
    zzf = JavaMethod("(I)V")
    zzg = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")