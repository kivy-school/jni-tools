from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NativeAdOptions"]

class NativeAdOptions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/nativead/NativeAdOptions"
    NATIVE_MEDIA_ASPECT_RATIO_UNKNOWN = JavaStaticField("I")
    NATIVE_MEDIA_ASPECT_RATIO_ANY = JavaStaticField("I")
    NATIVE_MEDIA_ASPECT_RATIO_LANDSCAPE = JavaStaticField("I")
    NATIVE_MEDIA_ASPECT_RATIO_PORTRAIT = JavaStaticField("I")
    NATIVE_MEDIA_ASPECT_RATIO_SQUARE = JavaStaticField("I")
    ADCHOICES_TOP_LEFT = JavaStaticField("I")
    ADCHOICES_TOP_RIGHT = JavaStaticField("I")
    ADCHOICES_BOTTOM_RIGHT = JavaStaticField("I")
    ADCHOICES_BOTTOM_LEFT = JavaStaticField("I")
    SWIPE_GESTURE_DIRECTION_RIGHT = JavaStaticField("I")
    SWIPE_GESTURE_DIRECTION_LEFT = JavaStaticField("I")
    SWIPE_GESTURE_DIRECTION_UP = JavaStaticField("I")
    SWIPE_GESTURE_DIRECTION_DOWN = JavaStaticField("I")
    shouldReturnUrlsForImageAssets = JavaMethod("()Z")
    getMediaAspectRatio = JavaMethod("()I")
    shouldRequestMultipleImages = JavaMethod("()Z")
    getAdChoicesPlacement = JavaMethod("()I")
    getVideoOptions = JavaMethod("()Lcom/google/android/gms/ads/VideoOptions;")
    zza = JavaMethod("()Z")
    zzb = JavaMethod("()I")
    zzc = JavaMethod("()Z")
    zzd = JavaMethod("()I")

    class AdChoicesPlacement(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/nativead/NativeAdOptions/AdChoicesPlacement"

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/nativead/NativeAdOptions/Builder"
        __javaconstructor__ = [("()V", False)]
        setReturnUrlsForImageAssets = JavaMethod("(Z)Lcom/google/android/gms/ads/nativead/NativeAdOptions$Builder;")
        setMediaAspectRatio = JavaMethod("(I)Lcom/google/android/gms/ads/nativead/NativeAdOptions$Builder;")
        setRequestMultipleImages = JavaMethod("(Z)Lcom/google/android/gms/ads/nativead/NativeAdOptions$Builder;")
        setAdChoicesPlacement = JavaMethod("(I)Lcom/google/android/gms/ads/nativead/NativeAdOptions$Builder;")
        setVideoOptions = JavaMethod("(Lcom/google/android/gms/ads/VideoOptions;)Lcom/google/android/gms/ads/nativead/NativeAdOptions$Builder;")
        enableCustomClickGestureDirection = JavaMethod("(IZ)Lcom/google/android/gms/ads/nativead/NativeAdOptions$Builder;")
        setRequestCustomMuteThisAd = JavaMethod("(Z)Lcom/google/android/gms/ads/nativead/NativeAdOptions$Builder;")
        build = JavaMethod("()Lcom/google/android/gms/ads/nativead/NativeAdOptions;")
        zzi = JavaMethod("(I)Lcom/google/android/gms/ads/nativead/NativeAdOptions$Builder;")

    class NativeMediaAspectRatio(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/nativead/NativeAdOptions/NativeMediaAspectRatio"

    class SwipeGestureDirection(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/nativead/NativeAdOptions/SwipeGestureDirection"