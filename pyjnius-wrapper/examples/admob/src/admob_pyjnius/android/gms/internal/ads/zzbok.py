from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbok"]

class zzbok(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbok"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/formats/OnAdManagerAdViewLoadedListener;)V", False)]
    zze = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzbu;Lcom/google/android/gms/dynamic/IObjectWrapper;)V")