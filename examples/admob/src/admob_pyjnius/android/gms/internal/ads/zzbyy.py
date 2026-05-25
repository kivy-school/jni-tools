from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbyy"]

class zzbyy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbyy"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/nativead/NativeAd$UnconfirmedClickListener;)V", False)]
    zze = JavaMethod("(Ljava/lang/String;)V")
    zzf = JavaMethod("()V")