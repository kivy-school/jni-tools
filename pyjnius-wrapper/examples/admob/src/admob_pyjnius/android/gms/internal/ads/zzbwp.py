from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbwp"]

class zzbwp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbwp"
    __javaconstructor__ = [("(Ljava/util/Date;ILjava/util/Set;Landroid/location/Location;ZILcom/google/android/gms/internal/ads/zzbma;Ljava/util/List;ZILjava/lang/String;)V", False)]
    getBirthday = JavaMethod("()Ljava/util/Date;")
    getGender = JavaMethod("()I")
    getKeywords = JavaMethod("()Ljava/util/Set;")
    getLocation = JavaMethod("()Landroid/location/Location;")
    isTesting = JavaMethod("()Z")
    taggedForChildDirectedTreatment = JavaMethod("()I")
    getNativeAdOptions = JavaMethod("()Lcom/google/android/gms/ads/formats/NativeAdOptions;")
    getNativeAdRequestOptions = JavaMethod("()Lcom/google/android/gms/ads/nativead/NativeAdOptions;")
    isAdMuted = JavaMethod("()Z")
    getAdVolume = JavaMethod("()F")
    isUnifiedNativeAdRequested = JavaMethod("()Z")
    zza = JavaMethod("()Z")
    zzb = JavaMethod("()Ljava/util/Map;")
    isDesignedForFamilies = JavaMethod("()Z")