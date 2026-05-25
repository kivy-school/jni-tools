from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationUtils"]

class MediationUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/MediationUtils"
    __javaconstructor__ = [("()V", False)]
    findClosestSize = JavaStaticMethod("(Landroid/content/Context;Lcom/google/android/gms/ads/AdSize;Ljava/util/List;)Lcom/google/android/gms/ads/AdSize;")