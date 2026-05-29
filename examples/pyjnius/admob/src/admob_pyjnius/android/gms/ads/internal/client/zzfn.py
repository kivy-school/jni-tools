from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzfn"]

class zzfn(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzfn"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/rewarded/OnAdMetadataChangedListener;)V", False)]
    zze = JavaMethod("()V")