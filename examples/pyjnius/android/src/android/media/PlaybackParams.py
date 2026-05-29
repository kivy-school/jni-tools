from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PlaybackParams"]

class PlaybackParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/PlaybackParams"
    __javaconstructor__ = [("()V", False)]
    AUDIO_FALLBACK_MODE_DEFAULT = JavaStaticField("I")
    AUDIO_FALLBACK_MODE_FAIL = JavaStaticField("I")
    AUDIO_FALLBACK_MODE_MUTE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    allowDefaults = JavaMethod("()Landroid/media/PlaybackParams;")
    getAudioFallbackMode = JavaMethod("()I")
    setAudioFallbackMode = JavaMethod("(I)Landroid/media/PlaybackParams;")
    setSpeed = JavaMethod("(F)Landroid/media/PlaybackParams;")
    getSpeed = JavaMethod("()F")
    setPitch = JavaMethod("(F)Landroid/media/PlaybackParams;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getPitch = JavaMethod("()F")