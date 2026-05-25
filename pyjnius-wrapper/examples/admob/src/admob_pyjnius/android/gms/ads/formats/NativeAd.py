from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NativeAd"]

class NativeAd(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/formats/NativeAd"
    __javaconstructor__ = [("()V", False)]
    ASSET_ADCHOICES_CONTAINER_VIEW = JavaStaticField("Ljava/lang/String;")
    performClick = JavaMethod("(Landroid/os/Bundle;)V")
    recordImpression = JavaMethod("(Landroid/os/Bundle;)Z")
    reportTouchEvent = JavaMethod("(Landroid/os/Bundle;)V")

    class AdChoicesInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/formats/NativeAd/AdChoicesInfo"
        __javaconstructor__ = [("()V", False)]
        getText = JavaMethod("()Ljava/lang/CharSequence;")
        getImages = JavaMethod("()Ljava/util/List;")

    class Image(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/formats/NativeAd/Image"
        __javaconstructor__ = [("()V", False)]
        getDrawable = JavaMethod("()Landroid/graphics/drawable/Drawable;")
        getUri = JavaMethod("()Landroid/net/Uri;")
        getScale = JavaMethod("()D")
        zza = JavaMethod("()I")
        zzb = JavaMethod("()I")