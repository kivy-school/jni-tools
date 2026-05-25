from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Ringtone"]

class Ringtone(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/Ringtone"
    setStreamType = JavaMethod("(I)V")
    getStreamType = JavaMethod("()I")
    setAudioAttributes = JavaMethod("(Landroid/media/AudioAttributes;)V")
    getAudioAttributes = JavaMethod("()Landroid/media/AudioAttributes;")
    setLooping = JavaMethod("(Z)V")
    isLooping = JavaMethod("()Z")
    setVolume = JavaMethod("(F)V")
    getVolume = JavaMethod("()F")
    setHapticGeneratorEnabled = JavaMethod("(Z)Z")
    isHapticGeneratorEnabled = JavaMethod("()Z")
    getTitle = JavaMethod("(Landroid/content/Context;)Ljava/lang/String;")
    play = JavaMethod("()V")
    stop = JavaMethod("()V")
    isPlaying = JavaMethod("()Z")
    finalize = JavaMethod("()V")