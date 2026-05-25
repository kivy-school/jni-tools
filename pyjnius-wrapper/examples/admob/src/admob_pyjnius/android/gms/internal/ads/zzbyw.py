from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbyw"]

class zzbyw(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbyw"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zzbnc;)V", False)]
    getText = JavaMethod("(Ljava/lang/String;)Ljava/lang/CharSequence;")
    getImage = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/nativead/NativeAd$Image;")
    getMediaContent = JavaMethod("()Lcom/google/android/gms/ads/MediaContent;")
    getAvailableAssetNames = JavaMethod("()Ljava/util/List;")
    getCustomFormatId = JavaMethod("()Ljava/lang/String;")
    performClick = JavaMethod("(Ljava/lang/String;)V")
    recordImpression = JavaMethod("()V")
    getDisplayOpenMeasurement = JavaMethod("()Lcom/google/android/gms/ads/nativead/NativeCustomFormatAd$DisplayOpenMeasurement;")
    destroy = JavaMethod("()V")