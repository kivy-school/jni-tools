from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationNativeAdConfiguration"]

class MediationNativeAdConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationNativeAdConfiguration"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/lang/String;Landroid/os/Bundle;Landroid/os/Bundle;ZLandroid/location/Location;IILjava/lang/String;Ljava/lang/String;Lcom/google/android/gms/internal/ads/zzbma;)V", False)]
    getNativeAdOptions = JavaMethod("()Lcom/google/android/gms/ads/nativead/NativeAdOptions;")