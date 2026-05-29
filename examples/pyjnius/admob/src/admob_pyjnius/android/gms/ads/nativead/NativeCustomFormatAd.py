from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NativeCustomFormatAd"]

class NativeCustomFormatAd(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/nativead/NativeCustomFormatAd"
    ASSET_NAME_VIDEO = JavaStaticField("Ljava/lang/String;")
    getText = JavaMethod("(Ljava/lang/String;)Ljava/lang/CharSequence;")
    getImage = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/nativead/NativeAd$Image;")
    getMediaContent = JavaMethod("()Lcom/google/android/gms/ads/MediaContent;")
    getAvailableAssetNames = JavaMethod("()Ljava/util/List;")
    getCustomFormatId = JavaMethod("()Ljava/lang/String;")
    performClick = JavaMethod("(Ljava/lang/String;)V")
    recordImpression = JavaMethod("()V")
    getDisplayOpenMeasurement = JavaMethod("()Lcom/google/android/gms/ads/nativead/NativeCustomFormatAd$DisplayOpenMeasurement;")
    destroy = JavaMethod("()V")

    class DisplayOpenMeasurement(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/nativead/NativeCustomFormatAd/DisplayOpenMeasurement"
        start = JavaMethod("()Z")
        setView = JavaMethod("(Landroid/view/View;)V")

    class OnCustomClickListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/nativead/NativeCustomFormatAd/OnCustomClickListener"
        onCustomClick = JavaMethod("(Lcom/google/android/gms/ads/nativead/NativeCustomFormatAd;Ljava/lang/String;)V")

    class OnCustomFormatAdLoadedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/nativead/NativeCustomFormatAd/OnCustomFormatAdLoadedListener"
        onCustomFormatAdLoaded = JavaMethod("(Lcom/google/android/gms/ads/nativead/NativeCustomFormatAd;)V")