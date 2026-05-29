from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NativeAd"]

class NativeAd(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/nativead/NativeAd"
    __javaconstructor__ = [("()V", False)]
    getHeadline = JavaMethod("()Ljava/lang/String;")
    getImages = JavaMethod("()Ljava/util/List;")
    getBody = JavaMethod("()Ljava/lang/String;")
    getIcon = JavaMethod("()Lcom/google/android/gms/ads/nativead/NativeAd$Image;")
    getCallToAction = JavaMethod("()Ljava/lang/String;")
    getAdvertiser = JavaMethod("()Ljava/lang/String;")
    getStarRating = JavaMethod("()Ljava/lang/Double;")
    getStore = JavaMethod("()Ljava/lang/String;")
    getPrice = JavaMethod("()Ljava/lang/String;")
    getAdChoicesInfo = JavaMethod("()Lcom/google/android/gms/ads/nativead/NativeAd$AdChoicesInfo;")
    isCustomMuteThisAdEnabled = JavaMethod("()Z")
    getMuteThisAdReasons = JavaMethod("()Ljava/util/List;")
    muteThisAd = JavaMethod("(Lcom/google/android/gms/ads/MuteThisAdReason;)V")
    setMuteThisAdListener = JavaMethod("(Lcom/google/android/gms/ads/MuteThisAdListener;)V")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    destroy = JavaMethod("()V")
    setUnconfirmedClickListener = JavaMethod("(Lcom/google/android/gms/ads/nativead/NativeAd$UnconfirmedClickListener;)V")
    cancelUnconfirmedClick = JavaMethod("()V")
    enableCustomClickGesture = JavaMethod("()V")
    isCustomClickGestureEnabled = JavaMethod("()Z")
    recordCustomClickGesture = JavaMethod("()V")
    performClick = JavaMethod("(Landroid/os/Bundle;)V")
    recordImpression = JavaMethod("(Landroid/os/Bundle;)Z")
    reportTouchEvent = JavaMethod("(Landroid/os/Bundle;)V")
    getMediaContent = JavaMethod("()Lcom/google/android/gms/ads/MediaContent;")
    getResponseInfo = JavaMethod("()Lcom/google/android/gms/ads/ResponseInfo;")
    setOnPaidEventListener = JavaMethod("(Lcom/google/android/gms/ads/OnPaidEventListener;)V")
    recordEvent = JavaMethod("(Landroid/os/Bundle;)V")
    getPlacementId = JavaMethod("()J")
    setPlacementId = JavaMethod("(J)V")
    zza = JavaMethod("()Ljava/lang/Object;")

    class AdChoicesInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/nativead/NativeAd/AdChoicesInfo"
        __javaconstructor__ = [("()V", False)]
        getText = JavaMethod("()Ljava/lang/CharSequence;")
        getImages = JavaMethod("()Ljava/util/List;")

    class Image(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/nativead/NativeAd/Image"
        __javaconstructor__ = [("()V", False)]
        zza = JavaField("Ljava/util/Map;")
        getDrawable = JavaMethod("()Landroid/graphics/drawable/Drawable;")
        getUri = JavaMethod("()Landroid/net/Uri;")
        getScale = JavaMethod("()D")
        zza = JavaMethod("()I")
        zzb = JavaMethod("()I")

    class OnNativeAdLoadedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/nativead/NativeAd/OnNativeAdLoadedListener"
        onNativeAdLoaded = JavaMethod("(Lcom/google/android/gms/ads/nativead/NativeAd;)V")

    class UnconfirmedClickListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/nativead/NativeAd/UnconfirmedClickListener"
        onUnconfirmedClickReceived = JavaMethod("(Ljava/lang/String;)V")
        onUnconfirmedClickCancelled = JavaMethod("()V")