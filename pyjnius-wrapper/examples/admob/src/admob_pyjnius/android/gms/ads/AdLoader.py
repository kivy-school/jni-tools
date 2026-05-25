from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdLoader"]

class AdLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/AdLoader"
    loadAd = JavaMultipleMethod([("(Lcom/google/android/gms/ads/AdRequest;)V", False, False), ("(Lcom/google/android/gms/ads/admanager/AdManagerAdRequest;)V", False, False)])
    loadAds = JavaMethod("(Lcom/google/android/gms/ads/AdRequest;I)V")
    isLoading = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/AdLoader/Builder"
        __javaconstructor__ = [("(Landroid/content/Context;Ljava/lang/String;)V", False)]
        forNativeAd = JavaMethod("(Lcom/google/android/gms/ads/nativead/NativeAd$OnNativeAdLoadedListener;)Lcom/google/android/gms/ads/AdLoader$Builder;")
        forCustomFormatAd = JavaMethod("(Ljava/lang/String;Lcom/google/android/gms/ads/nativead/NativeCustomFormatAd$OnCustomFormatAdLoadedListener;Lcom/google/android/gms/ads/nativead/NativeCustomFormatAd$OnCustomClickListener;)Lcom/google/android/gms/ads/AdLoader$Builder;")
        forAdManagerAdView = JavaMethod("(Lcom/google/android/gms/ads/formats/OnAdManagerAdViewLoadedListener;[Lcom/google/android/gms/ads/AdSize;)Lcom/google/android/gms/ads/AdLoader$Builder;", varargs=True)
        withAdListener = JavaMethod("(Lcom/google/android/gms/ads/AdListener;)Lcom/google/android/gms/ads/AdLoader$Builder;")
        withNativeAdOptions = JavaMethod("(Lcom/google/android/gms/ads/nativead/NativeAdOptions;)Lcom/google/android/gms/ads/AdLoader$Builder;")
        withAdManagerAdViewOptions = JavaMethod("(Lcom/google/android/gms/ads/formats/AdManagerAdViewOptions;)Lcom/google/android/gms/ads/AdLoader$Builder;")
        build = JavaMethod("()Lcom/google/android/gms/ads/AdLoader;")
        zza = JavaMethod("(Lcom/google/android/gms/ads/formats/zzg;)Lcom/google/android/gms/ads/AdLoader$Builder;")
        zzb = JavaMethod("(Ljava/lang/String;Lcom/google/android/gms/ads/formats/zze;Lcom/google/android/gms/ads/formats/zzd;)Lcom/google/android/gms/ads/AdLoader$Builder;")
        zzc = JavaMethod("(Lcom/google/android/gms/ads/formats/NativeAdOptions;)Lcom/google/android/gms/ads/AdLoader$Builder;")