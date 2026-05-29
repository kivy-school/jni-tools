from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioPlaybackCaptureConfiguration"]

class AudioPlaybackCaptureConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioPlaybackCaptureConfiguration"
    getMediaProjection = JavaMethod("()Landroid/media/projection/MediaProjection;")
    getMatchingUsages = JavaMethod("()[I")
    getMatchingUids = JavaMethod("()[I")
    getExcludeUsages = JavaMethod("()[I")
    getExcludeUids = JavaMethod("()[I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/AudioPlaybackCaptureConfiguration/Builder"
        __javaconstructor__ = [("(Landroid/media/projection/MediaProjection;)V", False)]
        addMatchingUsage = JavaMethod("(I)Landroid/media/AudioPlaybackCaptureConfiguration$Builder;")
        addMatchingUid = JavaMethod("(I)Landroid/media/AudioPlaybackCaptureConfiguration$Builder;")
        excludeUsage = JavaMethod("(I)Landroid/media/AudioPlaybackCaptureConfiguration$Builder;")
        excludeUid = JavaMethod("(I)Landroid/media/AudioPlaybackCaptureConfiguration$Builder;")
        build = JavaMethod("()Landroid/media/AudioPlaybackCaptureConfiguration;")