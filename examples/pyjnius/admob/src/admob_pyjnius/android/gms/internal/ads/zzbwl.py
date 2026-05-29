from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbwl"]

class zzbwl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbwl"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/mediation/MediationInterscrollerAd;)V", False)]
    zze = JavaMethod("()Lcom/google/android/gms/dynamic/IObjectWrapper;")
    zzf = JavaMethod("()Z")