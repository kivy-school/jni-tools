from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RequestConfiguration"]

class RequestConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/RequestConfiguration"
    TAG_FOR_CHILD_DIRECTED_TREATMENT_UNSPECIFIED = JavaStaticField("I")
    TAG_FOR_CHILD_DIRECTED_TREATMENT_FALSE = JavaStaticField("I")
    TAG_FOR_CHILD_DIRECTED_TREATMENT_TRUE = JavaStaticField("I")
    TAG_FOR_UNDER_AGE_OF_CONSENT_TRUE = JavaStaticField("I")
    TAG_FOR_UNDER_AGE_OF_CONSENT_FALSE = JavaStaticField("I")
    TAG_FOR_UNDER_AGE_OF_CONSENT_UNSPECIFIED = JavaStaticField("I")
    MAX_AD_CONTENT_RATING_UNSPECIFIED = JavaStaticField("Ljava/lang/String;")
    MAX_AD_CONTENT_RATING_G = JavaStaticField("Ljava/lang/String;")
    MAX_AD_CONTENT_RATING_PG = JavaStaticField("Ljava/lang/String;")
    MAX_AD_CONTENT_RATING_T = JavaStaticField("Ljava/lang/String;")
    MAX_AD_CONTENT_RATING_MA = JavaStaticField("Ljava/lang/String;")
    zza = JavaStaticField("Ljava/util/List;")
    getAgeRestrictedTreatment = JavaMethod("()Lcom/google/android/gms/ads/AgeRestrictedTreatment;")
    getTagForChildDirectedTreatment = JavaMethod("()I")
    getTagForUnderAgeOfConsent = JavaMethod("()I")
    getMaxAdContentRating = JavaMethod("()Ljava/lang/String;")
    getTestDeviceIds = JavaMethod("()Ljava/util/List;")
    getPublisherPrivacyPersonalizationState = JavaMethod("()Lcom/google/android/gms/ads/RequestConfiguration$PublisherPrivacyPersonalizationState;")
    toBuilder = JavaMethod("()Lcom/google/android/gms/ads/RequestConfiguration$Builder;")
    zza = JavaMethod("()Lcom/google/android/gms/ads/AgeRestrictedTreatment;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/RequestConfiguration/Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Lcom/google/android/gms/ads/RequestConfiguration;")
        setAgeRestrictedTreatment = JavaMethod("(Lcom/google/android/gms/ads/AgeRestrictedTreatment;)Lcom/google/android/gms/ads/RequestConfiguration$Builder;")
        setTagForChildDirectedTreatment = JavaMethod("(I)Lcom/google/android/gms/ads/RequestConfiguration$Builder;")
        setTagForUnderAgeOfConsent = JavaMethod("(I)Lcom/google/android/gms/ads/RequestConfiguration$Builder;")
        setMaxAdContentRating = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/RequestConfiguration$Builder;")
        setTestDeviceIds = JavaMethod("(Ljava/util/List;)Lcom/google/android/gms/ads/RequestConfiguration$Builder;")
        setPublisherPrivacyPersonalizationState = JavaMethod("(Lcom/google/android/gms/ads/RequestConfiguration$PublisherPrivacyPersonalizationState;)Lcom/google/android/gms/ads/RequestConfiguration$Builder;")

    class MaxAdContentRating(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/RequestConfiguration/MaxAdContentRating"

    class PublisherPrivacyPersonalizationState(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/RequestConfiguration/PublisherPrivacyPersonalizationState"
        values = JavaStaticMethod("()[Lcom/google/android/gms/ads/RequestConfiguration$PublisherPrivacyPersonalizationState;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/RequestConfiguration$PublisherPrivacyPersonalizationState;")
        getValue = JavaMethod("()I")
        DEFAULT = JavaStaticField("Lcom/google/android/gms/ads/RequestConfiguration/PublisherPrivacyPersonalizationState;")
        ENABLED = JavaStaticField("Lcom/google/android/gms/ads/RequestConfiguration/PublisherPrivacyPersonalizationState;")
        DISABLED = JavaStaticField("Lcom/google/android/gms/ads/RequestConfiguration/PublisherPrivacyPersonalizationState;")

    class TagForChildDirectedTreatment(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/RequestConfiguration/TagForChildDirectedTreatment"

    class TagForUnderAgeOfConsent(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/RequestConfiguration/TagForUnderAgeOfConsent"