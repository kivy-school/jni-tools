from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LoudnessCodecController"]

class LoudnessCodecController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/LoudnessCodecController"
    create = JavaMultipleMethod([("(I)Landroid/media/LoudnessCodecController;", True, False), ("(ILjava/util/concurrent/Executor;Landroid/media/LoudnessCodecController$OnLoudnessCodecUpdateListener;)Landroid/media/LoudnessCodecController;", True, False)])
    addMediaCodec = JavaMethod("(Landroid/media/MediaCodec;)Z")
    removeMediaCodec = JavaMethod("(Landroid/media/MediaCodec;)V")
    getLoudnessCodecParams = JavaMethod("(Landroid/media/MediaCodec;)Landroid/os/Bundle;")
    close = JavaMethod("()V")

    class OnLoudnessCodecUpdateListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/LoudnessCodecController/OnLoudnessCodecUpdateListener"
        onLoudnessCodecUpdate = JavaMethod("(Landroid/media/MediaCodec;Landroid/os/Bundle;)Landroid/os/Bundle;")