from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppOpenAd"]

class AppOpenAd(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/appopen/AppOpenAd"
    __javaconstructor__ = [("()V", False)]
    load = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;Lcom/google/android/gms/ads/AdRequest;Lcom/google/android/gms/ads/appopen/AppOpenAd$AppOpenAdLoadCallback;)V")
    isAdAvailable = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Z")
    pollAd = JavaStaticMethod("(Landroid/content/Context;Ljava/lang/String;)Lcom/google/android/gms/ads/appopen/AppOpenAd;")
    show = JavaMethod("(Landroid/app/Activity;)V")
    getResponseInfo = JavaMethod("()Lcom/google/android/gms/ads/ResponseInfo;")
    getAdUnitId = JavaMethod("()Ljava/lang/String;")
    setFullScreenContentCallback = JavaMethod("(Lcom/google/android/gms/ads/FullScreenContentCallback;)V")
    getFullScreenContentCallback = JavaMethod("()Lcom/google/android/gms/ads/FullScreenContentCallback;")
    setOnPaidEventListener = JavaMethod("(Lcom/google/android/gms/ads/OnPaidEventListener;)V")
    getOnPaidEventListener = JavaMethod("()Lcom/google/android/gms/ads/OnPaidEventListener;")
    setImmersiveMode = JavaMethod("(Z)V")
    getPlacementId = JavaMethod("()J")
    setPlacementId = JavaMethod("(J)V")

    class AppOpenAdLoadCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/appopen/AppOpenAd/AppOpenAdLoadCallback"
        __javaconstructor__ = [("()V", False)]