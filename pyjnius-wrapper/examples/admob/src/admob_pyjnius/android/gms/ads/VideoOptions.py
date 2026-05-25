from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VideoOptions"]

class VideoOptions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/VideoOptions"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/internal/client/zzfw;)V", False)]
    getStartMuted = JavaMethod("()Z")
    getCustomControlsRequested = JavaMethod("()Z")
    getClickToExpandRequested = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/VideoOptions/Builder"
        __javaconstructor__ = [("()V", False)]
        setStartMuted = JavaMethod("(Z)Lcom/google/android/gms/ads/VideoOptions$Builder;")
        setCustomControlsRequested = JavaMethod("(Z)Lcom/google/android/gms/ads/VideoOptions$Builder;")
        setClickToExpandRequested = JavaMethod("(Z)Lcom/google/android/gms/ads/VideoOptions$Builder;")
        build = JavaMethod("()Lcom/google/android/gms/ads/VideoOptions;")