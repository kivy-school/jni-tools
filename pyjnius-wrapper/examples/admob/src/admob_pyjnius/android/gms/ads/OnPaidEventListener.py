from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnPaidEventListener"]

class OnPaidEventListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/OnPaidEventListener"
    onPaidEvent = JavaMethod("(Lcom/google/android/gms/ads/AdValue;)V")