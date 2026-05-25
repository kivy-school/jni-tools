from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CustomEvent"]

class CustomEvent(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/customevent/CustomEvent"
    onDestroy = JavaMethod("()V")
    onPause = JavaMethod("()V")
    onResume = JavaMethod("()V")