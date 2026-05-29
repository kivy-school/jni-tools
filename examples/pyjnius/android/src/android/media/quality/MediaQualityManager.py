from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaQualityManager"]

class MediaQualityManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/quality/MediaQualityManager"
    addActiveProcessingPictureListener = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getAvailablePictureProfiles = JavaMethod("(Landroid/media/quality/MediaQualityManager$ProfileQueryParams;)Ljava/util/List;")
    getAvailableSoundProfiles = JavaMethod("(Landroid/media/quality/MediaQualityManager$ProfileQueryParams;)Ljava/util/List;")
    getParameterCapabilities = JavaMethod("(Ljava/util/List;)Ljava/util/List;")
    createPictureProfile = JavaMethod("(Landroid/media/quality/PictureProfile;)V")
    createSoundProfile = JavaMethod("(Landroid/media/quality/SoundProfile;)V")
    getPictureProfile = JavaMethod("(ILjava/lang/String;Landroid/media/quality/MediaQualityManager$ProfileQueryParams;)Landroid/media/quality/PictureProfile;")
    getSoundProfile = JavaMethod("(ILjava/lang/String;Landroid/media/quality/MediaQualityManager$ProfileQueryParams;)Landroid/media/quality/SoundProfile;")
    isAmbientBacklightEnabled = JavaMethod("()Z")
    isAutoPictureQualityEnabled = JavaMethod("()Z")
    isAutoSoundQualityEnabled = JavaMethod("()Z")
    isSuperResolutionEnabled = JavaMethod("()Z")
    registerAmbientBacklightCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/quality/MediaQualityManager$AmbientBacklightCallback;)V")
    registerPictureProfileCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/quality/MediaQualityManager$PictureProfileCallback;)V")
    registerSoundProfileCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/quality/MediaQualityManager$SoundProfileCallback;)V")
    removeActiveProcessingPictureListener = JavaMethod("(Ljava/util/function/Consumer;)V")
    removePictureProfile = JavaMethod("(Ljava/lang/String;)V")
    removeSoundProfile = JavaMethod("(Ljava/lang/String;)V")
    setAmbientBacklightEnabled = JavaMethod("(Z)V")
    setAmbientBacklightSettings = JavaMethod("(Landroid/media/quality/AmbientBacklightSettings;)V")
    unregisterAmbientBacklightCallback = JavaMethod("(Landroid/media/quality/MediaQualityManager$AmbientBacklightCallback;)V")
    unregisterPictureProfileCallback = JavaMethod("(Landroid/media/quality/MediaQualityManager$PictureProfileCallback;)V")
    unregisterSoundProfileCallback = JavaMethod("(Landroid/media/quality/MediaQualityManager$SoundProfileCallback;)V")
    updatePictureProfile = JavaMethod("(Ljava/lang/String;Landroid/media/quality/PictureProfile;)V")
    updateSoundProfile = JavaMethod("(Ljava/lang/String;Landroid/media/quality/SoundProfile;)V")

    class SoundProfileCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/quality/MediaQualityManager$SoundProfileCallback"
        __javaconstructor__ = [("()V", False)]
        onSoundProfileAdded = JavaMethod("(Ljava/lang/String;Landroid/media/quality/SoundProfile;)V")
        onSoundProfileRemoved = JavaMethod("(Ljava/lang/String;Landroid/media/quality/SoundProfile;)V")
        onSoundProfileUpdated = JavaMethod("(Ljava/lang/String;Landroid/media/quality/SoundProfile;)V")
        onParameterCapabilitiesChanged = JavaMethod("(Ljava/lang/String;Ljava/util/List;)V")
        onError = JavaMethod("(Ljava/lang/String;I)V")

    class ProfileQueryParams(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/quality/MediaQualityManager$ProfileQueryParams"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        areParametersIncluded = JavaMethod("()Z")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/media/quality/MediaQualityManager$ProfileQueryParams$Builder"
            __javaconstructor__ = [("()V", False)]
            setParametersIncluded = JavaMethod("(Z)Landroid/media/quality/MediaQualityManager$ProfileQueryParams$Builder;")
            build = JavaMethod("()Landroid/media/quality/MediaQualityManager$ProfileQueryParams;")

    class PictureProfileCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/quality/MediaQualityManager$PictureProfileCallback"
        __javaconstructor__ = [("()V", False)]
        onPictureProfileAdded = JavaMethod("(Ljava/lang/String;Landroid/media/quality/PictureProfile;)V")
        onPictureProfileRemoved = JavaMethod("(Ljava/lang/String;Landroid/media/quality/PictureProfile;)V")
        onPictureProfileUpdated = JavaMethod("(Ljava/lang/String;Landroid/media/quality/PictureProfile;)V")
        onParameterCapabilitiesChanged = JavaMethod("(Ljava/lang/String;Ljava/util/List;)V")
        onError = JavaMethod("(Ljava/lang/String;I)V")

    class AmbientBacklightCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/quality/MediaQualityManager$AmbientBacklightCallback"
        onAmbientBacklightEvent = JavaMethod("(Landroid/media/quality/AmbientBacklightEvent;)V")