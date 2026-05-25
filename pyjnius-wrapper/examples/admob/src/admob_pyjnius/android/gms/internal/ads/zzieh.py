from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzieh"]

class zzieh(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzieh"
    __javaconstructor__ = [("()V", False)]
    zza = JavaMethod("()Lcom/google/android/gms/internal/ads/zzidz;")