from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnAdInspectorClosedListener"]

class OnAdInspectorClosedListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/OnAdInspectorClosedListener"
    onAdInspectorClosed = JavaMethod("(Lcom/google/android/gms/ads/AdInspectorError;)V")