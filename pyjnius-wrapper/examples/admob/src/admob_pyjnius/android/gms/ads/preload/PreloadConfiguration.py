from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PreloadConfiguration"]

class PreloadConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/preload/PreloadConfiguration"
    getAdUnitId = JavaMethod("()Ljava/lang/String;")
    getAdFormat = JavaMethod("()Lcom/google/android/gms/ads/AdFormat;")
    getAdRequest = JavaMethod("()Lcom/google/android/gms/ads/AdRequest;")
    getBufferSize = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/preload/PreloadConfiguration/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Lcom/google/android/gms/ads/AdFormat;)V", False), ("(Ljava/lang/String;)V", False)]
        setAdRequest = JavaMethod("(Lcom/google/android/gms/ads/AdRequest;)Lcom/google/android/gms/ads/preload/PreloadConfiguration$Builder;")
        setBufferSize = JavaMethod("(I)Lcom/google/android/gms/ads/preload/PreloadConfiguration$Builder;")
        build = JavaMethod("()Lcom/google/android/gms/ads/preload/PreloadConfiguration;")