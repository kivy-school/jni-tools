from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PublisherAdViewOptions"]

class PublisherAdViewOptions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/formats/PublisherAdViewOptions"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    zza = JavaMethod("()Z")
    zzb = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzcl;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/formats/PublisherAdViewOptions/Builder"
        __javaconstructor__ = [("()V", False)]
        setShouldDelayBannerRenderingListener = JavaMethod("(Lcom/google/android/gms/ads/formats/ShouldDelayBannerRenderingListener;)Lcom/google/android/gms/ads/formats/PublisherAdViewOptions$Builder;")