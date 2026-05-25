from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbys"]

class zzbys(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbys"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zzboc;)V", False)]
    performClick = JavaMethod("(Landroid/os/Bundle;)V")
    recordImpression = JavaMethod("(Landroid/os/Bundle;)Z")
    reportTouchEvent = JavaMethod("(Landroid/os/Bundle;)V")
    getHeadline = JavaMethod("()Ljava/lang/String;")
    getImages = JavaMethod("()Ljava/util/List;")
    getBody = JavaMethod("()Ljava/lang/String;")
    getIcon = JavaMethod("()Lcom/google/android/gms/ads/nativead/NativeAd$Image;")
    getCallToAction = JavaMethod("()Ljava/lang/String;")
    getStarRating = JavaMethod("()Ljava/lang/Double;")
    getStore = JavaMethod("()Ljava/lang/String;")
    getPrice = JavaMethod("()Ljava/lang/String;")
    getAdChoicesInfo = JavaMethod("()Lcom/google/android/gms/ads/nativead/NativeAd$AdChoicesInfo;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    enableCustomClickGesture = JavaMethod("()V")
    isCustomClickGestureEnabled = JavaMethod("()Z")
    recordCustomClickGesture = JavaMethod("()V")
    getMuteThisAdReasons = JavaMethod("()Ljava/util/List;")
    isCustomMuteThisAdEnabled = JavaMethod("()Z")
    destroy = JavaMethod("()V")
    setUnconfirmedClickListener = JavaMethod("(Lcom/google/android/gms/ads/nativead/NativeAd$UnconfirmedClickListener;)V")
    muteThisAd = JavaMethod("(Lcom/google/android/gms/ads/MuteThisAdReason;)V")
    setMuteThisAdListener = JavaMethod("(Lcom/google/android/gms/ads/MuteThisAdListener;)V")
    cancelUnconfirmedClick = JavaMethod("()V")
    getAdvertiser = JavaMethod("()Ljava/lang/String;")
    getMediaContent = JavaMethod("()Lcom/google/android/gms/ads/MediaContent;")
    getResponseInfo = JavaMethod("()Lcom/google/android/gms/ads/ResponseInfo;")
    setOnPaidEventListener = JavaMethod("(Lcom/google/android/gms/ads/OnPaidEventListener;)V")
    recordEvent = JavaMethod("(Landroid/os/Bundle;)V")
    getPlacementId = JavaMethod("()J")
    setPlacementId = JavaMethod("(J)V")