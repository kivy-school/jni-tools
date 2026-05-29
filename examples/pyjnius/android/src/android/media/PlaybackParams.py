from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PlaybackParams"]

class PlaybackParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/PlaybackParams"
    __javaconstructor__ = [("()V", False)]
    AUDIO_FALLBACK_MODE_DEFAULT = JavaStaticField("I")
    AUDIO_FALLBACK_MODE_FAIL = JavaStaticField("I")
    AUDIO_FALLBACK_MODE_MUTE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    allowDefaults = JavaMethod("()Landroid/media/PlaybackParams;")
    setAudioFallbackMode = JavaMethod("(I)Landroid/media/PlaybackParams;")
    getAudioFallbackMode = JavaMethod("()I")
    setPitch = JavaMethod("(F)Landroid/media/PlaybackParams;")
    getPitch = JavaMethod("()F")
    setSpeed = JavaMethod("(F)Landroid/media/PlaybackParams;")
    getSpeed = JavaMethod("()F")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")