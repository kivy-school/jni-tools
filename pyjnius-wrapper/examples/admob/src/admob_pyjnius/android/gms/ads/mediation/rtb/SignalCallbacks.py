from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SignalCallbacks"]

class SignalCallbacks(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/rtb/SignalCallbacks"
    onSuccess = JavaMethod("(Ljava/lang/String;)V")
    onFailure = JavaMethod("(Lcom/google/android/gms/ads/AdError;)V")