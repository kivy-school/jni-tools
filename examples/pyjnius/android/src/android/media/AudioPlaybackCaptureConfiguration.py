from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioPlaybackCaptureConfiguration"]

class AudioPlaybackCaptureConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioPlaybackCaptureConfiguration"
    getMatchingUsages = JavaMethod("()[I")
    getExcludeUids = JavaMethod("()[I")
    getExcludeUsages = JavaMethod("()[I")
    getMatchingUids = JavaMethod("()[I")
    getMediaProjection = JavaMethod("()Landroid/media/projection/MediaProjection;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/AudioPlaybackCaptureConfiguration$Builder"
        __javaconstructor__ = [("(Landroid/media/projection/MediaProjection;)V", False)]
        excludeUsage = JavaMethod("(I)Landroid/media/AudioPlaybackCaptureConfiguration$Builder;")
        excludeUid = JavaMethod("(I)Landroid/media/AudioPlaybackCaptureConfiguration$Builder;")
        addMatchingUid = JavaMethod("(I)Landroid/media/AudioPlaybackCaptureConfiguration$Builder;")
        addMatchingUsage = JavaMethod("(I)Landroid/media/AudioPlaybackCaptureConfiguration$Builder;")
        build = JavaMethod("()Landroid/media/AudioPlaybackCaptureConfiguration;")