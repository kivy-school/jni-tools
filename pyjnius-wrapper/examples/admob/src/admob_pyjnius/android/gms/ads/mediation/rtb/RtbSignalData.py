from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RtbSignalData"]

class RtbSignalData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/rtb/RtbSignalData"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/util/List;Landroid/os/Bundle;Lcom/google/android/gms/ads/AdSize;)V", False)]
    getContext = JavaMethod("()Landroid/content/Context;")
    getConfigurations = JavaMethod("()Ljava/util/List;")
    getNetworkExtras = JavaMethod("()Landroid/os/Bundle;")
    getAdSize = JavaMethod("()Lcom/google/android/gms/ads/AdSize;")