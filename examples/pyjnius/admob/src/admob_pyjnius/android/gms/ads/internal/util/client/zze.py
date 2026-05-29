from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zze"]

class zze(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/util/client/zze"
    zza = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/internal/util/client/zzt;")