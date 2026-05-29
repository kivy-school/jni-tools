from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnContextChangedListener"]

class OnContextChangedListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/OnContextChangedListener"
    onContextChanged = JavaMethod("(Landroid/content/Context;)V")