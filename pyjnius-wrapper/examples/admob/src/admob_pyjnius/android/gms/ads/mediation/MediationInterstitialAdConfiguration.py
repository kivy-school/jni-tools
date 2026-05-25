from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationInterstitialAdConfiguration"]

class MediationInterstitialAdConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationInterstitialAdConfiguration"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/lang/String;Landroid/os/Bundle;Landroid/os/Bundle;ZLandroid/location/Location;IILjava/lang/String;Ljava/lang/String;)V", False)]