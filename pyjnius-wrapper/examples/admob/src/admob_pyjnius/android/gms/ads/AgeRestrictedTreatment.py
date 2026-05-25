from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AgeRestrictedTreatment"]

class AgeRestrictedTreatment(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/AgeRestrictedTreatment"
    values = JavaStaticMethod("()[Lcom/google/android/gms/ads/AgeRestrictedTreatment;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/AgeRestrictedTreatment;")
    getValue = JavaMethod("()I")
    UNSPECIFIED = JavaStaticField("Lcom/google/android/gms/ads/AgeRestrictedTreatment;")
    CHILD = JavaStaticField("Lcom/google/android/gms/ads/AgeRestrictedTreatment;")
    TEEN = JavaStaticField("Lcom/google/android/gms/ads/AgeRestrictedTreatment;")