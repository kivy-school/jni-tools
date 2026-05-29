from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbse"]

class zzbse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbse"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/initialization/AdapterStatus$State;Ljava/lang/String;I)V", False)]
    getInitializationState = JavaMethod("()Lcom/google/android/gms/ads/initialization/AdapterStatus$State;")
    getDescription = JavaMethod("()Ljava/lang/String;")
    getLatency = JavaMethod("()I")