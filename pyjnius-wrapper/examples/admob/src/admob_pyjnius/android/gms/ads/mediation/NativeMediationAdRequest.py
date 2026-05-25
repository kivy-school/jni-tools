from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NativeMediationAdRequest"]

class NativeMediationAdRequest(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/NativeMediationAdRequest"
    getNativeAdOptions = JavaMethod("()Lcom/google/android/gms/ads/formats/NativeAdOptions;")
    getNativeAdRequestOptions = JavaMethod("()Lcom/google/android/gms/ads/nativead/NativeAdOptions;")
    isUnifiedNativeAdRequested = JavaMethod("()Z")
    isAdMuted = JavaMethod("()Z")
    getAdVolume = JavaMethod("()F")
    zza = JavaMethod("()Z")
    zzb = JavaMethod("()Ljava/util/Map;")