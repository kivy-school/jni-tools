from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VideoController"]

class VideoController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/VideoController"
    __javaconstructor__ = [("()V", False)]
    PLAYBACK_STATE_UNKNOWN = JavaStaticField("I")
    PLAYBACK_STATE_PLAYING = JavaStaticField("I")
    PLAYBACK_STATE_PAUSED = JavaStaticField("I")
    PLAYBACK_STATE_ENDED = JavaStaticField("I")
    PLAYBACK_STATE_READY = JavaStaticField("I")
    play = JavaMethod("()V")
    pause = JavaMethod("()V")
    stop = JavaMethod("()V")
    mute = JavaMethod("(Z)V")
    isMuted = JavaMethod("()Z")
    getPlaybackState = JavaMethod("()I")
    isCustomControlsEnabled = JavaMethod("()Z")
    isClickToExpandEnabled = JavaMethod("()Z")
    setVideoLifecycleCallbacks = JavaMethod("(Lcom/google/android/gms/ads/VideoController$VideoLifecycleCallbacks;)V")
    getVideoLifecycleCallbacks = JavaMethod("()Lcom/google/android/gms/ads/VideoController$VideoLifecycleCallbacks;")
    hasVideoContent = JavaMethod("()Z")
    zza = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzea;)V")
    zzb = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzea;")

    class VideoLifecycleCallbacks(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/VideoController/VideoLifecycleCallbacks"
        __javaconstructor__ = [("()V", False)]
        onVideoStart = JavaMethod("()V")
        onVideoPlay = JavaMethod("()V")
        onVideoPause = JavaMethod("()V")
        onVideoEnd = JavaMethod("()V")
        onVideoMute = JavaMethod("(Z)V")