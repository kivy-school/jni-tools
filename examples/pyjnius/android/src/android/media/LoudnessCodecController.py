from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LoudnessCodecController"]

class LoudnessCodecController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/LoudnessCodecController"
    removeMediaCodec = JavaMethod("(Landroid/media/MediaCodec;)V")
    addMediaCodec = JavaMethod("(Landroid/media/MediaCodec;)Z")
    getLoudnessCodecParams = JavaMethod("(Landroid/media/MediaCodec;)Landroid/os/Bundle;")
    close = JavaMethod("()V")
    create = JavaMultipleMethod([("(ILjava/util/concurrent/Executor;Landroid/media/LoudnessCodecController$OnLoudnessCodecUpdateListener;)Landroid/media/LoudnessCodecController;", True, False), ("(I)Landroid/media/LoudnessCodecController;", True, False)])

    class OnLoudnessCodecUpdateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/LoudnessCodecController$OnLoudnessCodecUpdateListener"
        onLoudnessCodecUpdate = JavaMethod("(Landroid/media/MediaCodec;Landroid/os/Bundle;)Landroid/os/Bundle;")