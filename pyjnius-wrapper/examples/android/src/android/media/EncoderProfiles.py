from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EncoderProfiles"]

class EncoderProfiles(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/EncoderProfiles"
    getDefaultDurationSeconds = JavaMethod("()I")
    getRecommendedFileFormat = JavaMethod("()I")
    getAudioProfiles = JavaMethod("()Ljava/util/List;")
    getVideoProfiles = JavaMethod("()Ljava/util/List;")

    class AudioProfile(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/EncoderProfiles/AudioProfile"
        getCodec = JavaMethod("()I")
        getMediaType = JavaMethod("()Ljava/lang/String;")
        getBitrate = JavaMethod("()I")
        getSampleRate = JavaMethod("()I")
        getChannels = JavaMethod("()I")
        getProfile = JavaMethod("()I")

    class VideoProfile(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/EncoderProfiles/VideoProfile"
        HDR_DOLBY_VISION = JavaStaticField("I")
        HDR_HDR10 = JavaStaticField("I")
        HDR_HDR10PLUS = JavaStaticField("I")
        HDR_HLG = JavaStaticField("I")
        HDR_NONE = JavaStaticField("I")
        YUV_420 = JavaStaticField("I")
        YUV_422 = JavaStaticField("I")
        YUV_444 = JavaStaticField("I")
        getCodec = JavaMethod("()I")
        getMediaType = JavaMethod("()Ljava/lang/String;")
        getBitrate = JavaMethod("()I")
        getFrameRate = JavaMethod("()I")
        getWidth = JavaMethod("()I")
        getHeight = JavaMethod("()I")
        getProfile = JavaMethod("()I")
        getBitDepth = JavaMethod("()I")
        getChromaSubsampling = JavaMethod("()I")
        getHdrFormat = JavaMethod("()I")