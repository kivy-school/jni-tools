from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationAdRequest"]

class MediationAdRequest(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationAdRequest"
    TAG_FOR_CHILD_DIRECTED_TREATMENT_TRUE = JavaStaticField("I")
    TAG_FOR_CHILD_DIRECTED_TREATMENT_FALSE = JavaStaticField("I")
    TAG_FOR_CHILD_DIRECTED_TREATMENT_UNSPECIFIED = JavaStaticField("I")
    getBirthday = JavaMethod("()Ljava/util/Date;")
    getGender = JavaMethod("()I")
    getKeywords = JavaMethod("()Ljava/util/Set;")
    getLocation = JavaMethod("()Landroid/location/Location;")
    taggedForChildDirectedTreatment = JavaMethod("()I")
    isTesting = JavaMethod("()Z")
    isDesignedForFamilies = JavaMethod("()Z")