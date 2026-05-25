from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationAdConfiguration"]

class MediationAdConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationAdConfiguration"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/lang/String;Landroid/os/Bundle;Landroid/os/Bundle;ZLandroid/location/Location;IILjava/lang/String;Ljava/lang/String;)V", False)]
    TAG_FOR_CHILD_DIRECTED_TREATMENT_TRUE = JavaStaticField("I")
    TAG_FOR_CHILD_DIRECTED_TREATMENT_FALSE = JavaStaticField("I")
    TAG_FOR_CHILD_DIRECTED_TREATMENT_UNSPECIFIED = JavaStaticField("I")
    getBidResponse = JavaMethod("()Ljava/lang/String;")
    getServerParameters = JavaMethod("()Landroid/os/Bundle;")
    getMediationExtras = JavaMethod("()Landroid/os/Bundle;")
    getContext = JavaMethod("()Landroid/content/Context;")
    taggedForChildDirectedTreatment = JavaMethod("()I")
    isTestRequest = JavaMethod("()Z")
    taggedForUnderAgeTreatment = JavaMethod("()I")
    getMaxAdContentRating = JavaMethod("()Ljava/lang/String;")
    getWatermark = JavaMethod("()Ljava/lang/String;")

    class TagForChildDirectedTreatment(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/mediation/MediationAdConfiguration/TagForChildDirectedTreatment"