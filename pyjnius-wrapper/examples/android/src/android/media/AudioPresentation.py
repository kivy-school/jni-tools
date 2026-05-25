from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioPresentation"]

class AudioPresentation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioPresentation"
    CONTENT_COMMENTARY = JavaStaticField("I")
    CONTENT_DIALOG = JavaStaticField("I")
    CONTENT_EMERGENCY = JavaStaticField("I")
    CONTENT_HEARING_IMPAIRED = JavaStaticField("I")
    CONTENT_MAIN = JavaStaticField("I")
    CONTENT_MUSIC_AND_EFFECTS = JavaStaticField("I")
    CONTENT_UNKNOWN = JavaStaticField("I")
    CONTENT_VISUALLY_IMPAIRED = JavaStaticField("I")
    CONTENT_VOICEOVER = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    MASTERED_FOR_3D = JavaStaticField("I")
    MASTERED_FOR_HEADPHONE = JavaStaticField("I")
    MASTERED_FOR_STEREO = JavaStaticField("I")
    MASTERED_FOR_SURROUND = JavaStaticField("I")
    MASTERING_NOT_INDICATED = JavaStaticField("I")
    PRESENTATION_ID_UNKNOWN = JavaStaticField("I")
    PROGRAM_ID_UNKNOWN = JavaStaticField("I")
    getPresentationId = JavaMethod("()I")
    getProgramId = JavaMethod("()I")
    getLabels = JavaMethod("()Ljava/util/Map;")
    getLocale = JavaMethod("()Ljava/util/Locale;")
    getMasteringIndication = JavaMethod("()I")
    hasAudioDescription = JavaMethod("()Z")
    hasSpokenSubtitles = JavaMethod("()Z")
    hasDialogueEnhancement = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/AudioPresentation/Builder"
        __javaconstructor__ = [("(I)V", False)]
        setProgramId = JavaMethod("(I)Landroid/media/AudioPresentation$Builder;")
        setLocale = JavaMethod("(Landroid/icu/util/ULocale;)Landroid/media/AudioPresentation$Builder;")
        setMasteringIndication = JavaMethod("(I)Landroid/media/AudioPresentation$Builder;")
        setLabels = JavaMethod("(Ljava/util/Map;)Landroid/media/AudioPresentation$Builder;")
        setHasAudioDescription = JavaMethod("(Z)Landroid/media/AudioPresentation$Builder;")
        setHasSpokenSubtitles = JavaMethod("(Z)Landroid/media/AudioPresentation$Builder;")
        setHasDialogueEnhancement = JavaMethod("(Z)Landroid/media/AudioPresentation$Builder;")
        build = JavaMethod("()Landroid/media/AudioPresentation;")