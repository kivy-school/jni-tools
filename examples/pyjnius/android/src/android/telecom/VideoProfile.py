from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VideoProfile"]

class VideoProfile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/VideoProfile"
    __javaconstructor__ = [("(I)V", False), ("(II)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    QUALITY_DEFAULT = JavaStaticField("I")
    QUALITY_HIGH = JavaStaticField("I")
    QUALITY_LOW = JavaStaticField("I")
    QUALITY_MEDIUM = JavaStaticField("I")
    STATE_AUDIO_ONLY = JavaStaticField("I")
    STATE_BIDIRECTIONAL = JavaStaticField("I")
    STATE_PAUSED = JavaStaticField("I")
    STATE_RX_ENABLED = JavaStaticField("I")
    STATE_TX_ENABLED = JavaStaticField("I")
    getVideoState = JavaMethod("()I")
    getQuality = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    videoStateToString = JavaStaticMethod("(I)Ljava/lang/String;")
    isAudioOnly = JavaStaticMethod("(I)Z")
    isVideo = JavaStaticMethod("(I)Z")
    isTransmissionEnabled = JavaStaticMethod("(I)Z")
    isReceptionEnabled = JavaStaticMethod("(I)Z")
    isBidirectional = JavaStaticMethod("(I)Z")
    isPaused = JavaStaticMethod("(I)Z")

    class CameraCapabilities(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telecom/VideoProfile/CameraCapabilities"
        __javaconstructor__ = [("(II)V", False), ("(IIZF)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        getWidth = JavaMethod("()I")
        getHeight = JavaMethod("()I")
        isZoomSupported = JavaMethod("()Z")
        getMaxZoom = JavaMethod("()F")