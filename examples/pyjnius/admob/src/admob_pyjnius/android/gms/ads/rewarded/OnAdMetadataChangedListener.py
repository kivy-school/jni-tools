from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnAdMetadataChangedListener"]

class OnAdMetadataChangedListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/rewarded/OnAdMetadataChangedListener"
    onAdMetadataChanged = JavaMethod("()V")