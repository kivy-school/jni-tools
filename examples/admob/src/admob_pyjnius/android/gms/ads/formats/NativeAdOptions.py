from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NativeAdOptions"]

class NativeAdOptions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/formats/NativeAdOptions"
    ORIENTATION_ANY = JavaStaticField("I")
    ORIENTATION_PORTRAIT = JavaStaticField("I")
    ORIENTATION_LANDSCAPE = JavaStaticField("I")
    NATIVE_MEDIA_ASPECT_RATIO_UNKNOWN = JavaStaticField("I")
    NATIVE_MEDIA_ASPECT_RATIO_ANY = JavaStaticField("I")
    NATIVE_MEDIA_ASPECT_RATIO_LANDSCAPE = JavaStaticField("I")
    NATIVE_MEDIA_ASPECT_RATIO_PORTRAIT = JavaStaticField("I")
    NATIVE_MEDIA_ASPECT_RATIO_SQUARE = JavaStaticField("I")
    ADCHOICES_TOP_LEFT = JavaStaticField("I")
    ADCHOICES_TOP_RIGHT = JavaStaticField("I")
    ADCHOICES_BOTTOM_RIGHT = JavaStaticField("I")
    ADCHOICES_BOTTOM_LEFT = JavaStaticField("I")
    shouldReturnUrlsForImageAssets = JavaMethod("()Z")
    getImageOrientation = JavaMethod("()I")
    getMediaAspectRatio = JavaMethod("()I")
    shouldRequestMultipleImages = JavaMethod("()Z")
    getAdChoicesPlacement = JavaMethod("()I")
    getVideoOptions = JavaMethod("()Lcom/google/android/gms/ads/VideoOptions;")
    zza = JavaMethod("()Z")

    class AdChoicesPlacement(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/formats/NativeAdOptions/AdChoicesPlacement"

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/formats/NativeAdOptions/Builder"
        __javaconstructor__ = [("()V", False)]
        setReturnUrlsForImageAssets = JavaMethod("(Z)Lcom/google/android/gms/ads/formats/NativeAdOptions$Builder;")
        setImageOrientation = JavaMethod("(I)Lcom/google/android/gms/ads/formats/NativeAdOptions$Builder;")
        setMediaAspectRatio = JavaMethod("(I)Lcom/google/android/gms/ads/formats/NativeAdOptions$Builder;")
        setRequestMultipleImages = JavaMethod("(Z)Lcom/google/android/gms/ads/formats/NativeAdOptions$Builder;")
        setAdChoicesPlacement = JavaMethod("(I)Lcom/google/android/gms/ads/formats/NativeAdOptions$Builder;")
        setVideoOptions = JavaMethod("(Lcom/google/android/gms/ads/VideoOptions;)Lcom/google/android/gms/ads/formats/NativeAdOptions$Builder;")
        setRequestCustomMuteThisAd = JavaMethod("(Z)Lcom/google/android/gms/ads/formats/NativeAdOptions$Builder;")
        build = JavaMethod("()Lcom/google/android/gms/ads/formats/NativeAdOptions;")

    class NativeMediaAspectRatio(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/formats/NativeAdOptions/NativeMediaAspectRatio"