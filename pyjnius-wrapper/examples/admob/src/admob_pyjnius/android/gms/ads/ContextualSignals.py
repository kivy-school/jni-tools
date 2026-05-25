from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContextualSignals"]

class ContextualSignals(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/ContextualSignals"