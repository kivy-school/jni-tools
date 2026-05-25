from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnImmersiveModeUpdatedListener"]

class OnImmersiveModeUpdatedListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/OnImmersiveModeUpdatedListener"
    onImmersiveModeUpdated = JavaMethod("(Z)V")