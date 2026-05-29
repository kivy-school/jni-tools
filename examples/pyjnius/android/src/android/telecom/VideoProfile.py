from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    videoStateToString = JavaStaticMethod("(I)Ljava/lang/String;")
    isAudioOnly = JavaStaticMethod("(I)Z")
    isReceptionEnabled = JavaStaticMethod("(I)Z")
    isBidirectional = JavaStaticMethod("(I)Z")
    isTransmissionEnabled = JavaStaticMethod("(I)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getVideoState = JavaMethod("()I")
    getQuality = JavaMethod("()I")
    isPaused = JavaStaticMethod("(I)Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    isVideo = JavaStaticMethod("(I)Z")

    class CameraCapabilities(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telecom/VideoProfile$CameraCapabilities"
        __javaconstructor__ = [("(II)V", False), ("(IIZF)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getHeight = JavaMethod("()I")
        getWidth = JavaMethod("()I")
        getMaxZoom = JavaMethod("()F")
        isZoomSupported = JavaMethod("()Z")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")