from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InitializationStatus"]

class InitializationStatus(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/initialization/InitializationStatus"
    getAdapterStatusMap = JavaMethod("()Ljava/util/Map;")