from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzdh"]

class zzdh(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzdh"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/internal/client/zzdg;)V", False)]
    getDescription = JavaMethod("()Ljava/lang/String;")
    zza = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzdg;")
    toString = JavaMethod("()Ljava/lang/String;")