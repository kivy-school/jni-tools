from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnAdManagerAdViewLoadedListener"]

class OnAdManagerAdViewLoadedListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/formats/OnAdManagerAdViewLoadedListener"
    onAdManagerAdViewLoaded = JavaMethod("(Lcom/google/android/gms/ads/admanager/AdManagerAdView;)V")