from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbsf"]

class zzbsf(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbsf"
    __javaconstructor__ = [("(Ljava/util/Map;)V", False)]
    getAdapterStatusMap = JavaMethod("()Ljava/util/Map;")