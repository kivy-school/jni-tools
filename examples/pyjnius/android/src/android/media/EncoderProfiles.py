from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EncoderProfiles"]

class EncoderProfiles(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/EncoderProfiles"
    getAudioProfiles = JavaMethod("()Ljava/util/List;")
    getDefaultDurationSeconds = JavaMethod("()I")
    getRecommendedFileFormat = JavaMethod("()I")
    getVideoProfiles = JavaMethod("()Ljava/util/List;")

    class VideoProfile(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/EncoderProfiles$VideoProfile"
        HDR_DOLBY_VISION = JavaStaticField("I")
        HDR_HDR10 = JavaStaticField("I")
        HDR_HDR10PLUS = JavaStaticField("I")
        HDR_HLG = JavaStaticField("I")
        HDR_NONE = JavaStaticField("I")
        YUV_420 = JavaStaticField("I")
        YUV_422 = JavaStaticField("I")
        YUV_444 = JavaStaticField("I")
        getFrameRate = JavaMethod("()I")
        getChromaSubsampling = JavaMethod("()I")
        getHdrFormat = JavaMethod("()I")
        getBitDepth = JavaMethod("()I")
        getMediaType = JavaMethod("()Ljava/lang/String;")
        getCodec = JavaMethod("()I")
        getBitrate = JavaMethod("()I")
        getHeight = JavaMethod("()I")
        getWidth = JavaMethod("()I")
        getProfile = JavaMethod("()I")

    class AudioProfile(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/EncoderProfiles$AudioProfile"
        getChannels = JavaMethod("()I")
        getSampleRate = JavaMethod("()I")
        getMediaType = JavaMethod("()Ljava/lang/String;")
        getCodec = JavaMethod("()I")
        getBitrate = JavaMethod("()I")
        getProfile = JavaMethod("()I")