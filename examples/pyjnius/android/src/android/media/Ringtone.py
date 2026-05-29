from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Ringtone"]

class Ringtone(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/Ringtone"
    getAudioAttributes = JavaMethod("()Landroid/media/AudioAttributes;")
    isLooping = JavaMethod("()Z")
    setLooping = JavaMethod("(Z)V")
    isHapticGeneratorEnabled = JavaMethod("()Z")
    setHapticGeneratorEnabled = JavaMethod("(Z)Z")
    setVolume = JavaMethod("(F)V")
    setStreamType = JavaMethod("(I)V")
    getStreamType = JavaMethod("()I")
    getTitle = JavaMethod("(Landroid/content/Context;)Ljava/lang/String;")
    isPlaying = JavaMethod("()Z")
    setAudioAttributes = JavaMethod("(Landroid/media/AudioAttributes;)V")
    stop = JavaMethod("()V")
    getVolume = JavaMethod("()F")
    play = JavaMethod("()V")