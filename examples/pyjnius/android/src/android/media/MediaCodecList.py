from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaCodecList"]

class MediaCodecList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaCodecList"
    __javaconstructor__ = [("(I)V", False)]
    ALL_CODECS = JavaStaticField("I")
    REGULAR_CODECS = JavaStaticField("I")
    getCodecCount = JavaStaticMethod("()I")
    getCodecInfoAt = JavaStaticMethod("(I)Landroid/media/MediaCodecInfo;")
    getCodecInfos = JavaMethod("()[Landroid/media/MediaCodecInfo;")
    findDecoderForFormat = JavaMethod("(Landroid/media/MediaFormat;)Ljava/lang/String;")
    findEncoderForFormat = JavaMethod("(Landroid/media/MediaFormat;)Ljava/lang/String;")