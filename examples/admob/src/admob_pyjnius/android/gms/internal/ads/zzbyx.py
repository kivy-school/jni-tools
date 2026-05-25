from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbyx"]

class zzbyx(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbyx"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/nativead/NativeAd$OnNativeAdLoadedListener;)V", False)]
    zze = JavaMethod("(Lcom/google/android/gms/internal/ads/zzboc;)V")