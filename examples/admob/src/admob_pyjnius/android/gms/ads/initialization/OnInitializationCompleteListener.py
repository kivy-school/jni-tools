from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnInitializationCompleteListener"]

class OnInitializationCompleteListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/initialization/OnInitializationCompleteListener"
    onInitializationComplete = JavaMethod("(Lcom/google/android/gms/ads/initialization/InitializationStatus;)V")