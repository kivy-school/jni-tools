from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LiteSdkInfo"]

class LiteSdkInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/LiteSdkInfo"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    getLiteSdkVersion = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzez;")
    getAdapterCreator = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbvj;")