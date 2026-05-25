from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcbx"]

class zzcbx(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcbx"
    zze = JavaMethod("(Lcom/google/android/gms/internal/ads/zzcbw;Ljava/lang/String;Ljava/lang/String;)V")