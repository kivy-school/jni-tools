from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediationAdapter"]

class MediationAdapter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/MediationAdapter"
    onDestroy = JavaMethod("()V")
    onPause = JavaMethod("()V")
    onResume = JavaMethod("()V")