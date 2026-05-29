from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbnk"]

class zzbnk(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbnk"
    zze = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbnc;Ljava/lang/String;)V")