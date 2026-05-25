from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdapterStatus"]

class AdapterStatus(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/initialization/AdapterStatus"
    getInitializationState = JavaMethod("()Lcom/google/android/gms/ads/initialization/AdapterStatus$State;")
    getDescription = JavaMethod("()Ljava/lang/String;")
    getLatency = JavaMethod("()I")

    class State(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/initialization/AdapterStatus/State"
        values = JavaStaticMethod("()[Lcom/google/android/gms/ads/initialization/AdapterStatus$State;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/google/android/gms/ads/initialization/AdapterStatus$State;")
        NOT_READY = JavaStaticField("Lcom/google/android/gms/ads/initialization/AdapterStatus/State;")
        READY = JavaStaticField("Lcom/google/android/gms/ads/initialization/AdapterStatus/State;")