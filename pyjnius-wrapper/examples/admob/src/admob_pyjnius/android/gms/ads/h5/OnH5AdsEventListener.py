from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnH5AdsEventListener"]

class OnH5AdsEventListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/h5/OnH5AdsEventListener"
    onH5AdsEvent = JavaMethod("(Ljava/lang/String;)V")