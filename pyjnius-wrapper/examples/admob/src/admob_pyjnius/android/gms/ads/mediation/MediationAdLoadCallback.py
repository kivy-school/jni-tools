from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationAdLoadCallback"]

class MediationAdLoadCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationAdLoadCallback"
    onSuccess = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    onFailure = JavaMethod("(Lcom/google/android/gms/ads/AdError;)V")