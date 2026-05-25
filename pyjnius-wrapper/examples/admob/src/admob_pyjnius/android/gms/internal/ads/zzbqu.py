from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbqu"]

class zzbqu(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbqu"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/h5/OnH5AdsEventListener;)V", False)]
    zzb = JavaMethod("(Ljava/lang/String;)V")