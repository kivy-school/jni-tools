from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaMuxer"]

class MediaMuxer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaMuxer"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False), ("(Ljava/io/FileDescriptor;I)V", False)]
    setOrientationHint = JavaMethod("(I)V")
    setLocation = JavaMethod("(FF)V")
    start = JavaMethod("()V")
    stop = JavaMethod("()V")
    finalize = JavaMethod("()V")
    addTrack = JavaMethod("(Landroid/media/MediaFormat;)I")
    writeSampleData = JavaMethod("(ILjava/nio/ByteBuffer;Landroid/media/MediaCodec$BufferInfo;)V")
    release = JavaMethod("()V")

    class OutputFormat(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaMuxer/OutputFormat"
        MUXER_OUTPUT_3GPP = JavaStaticField("I")
        MUXER_OUTPUT_HEIF = JavaStaticField("I")
        MUXER_OUTPUT_MPEG_4 = JavaStaticField("I")
        MUXER_OUTPUT_OGG = JavaStaticField("I")
        MUXER_OUTPUT_WEBM = JavaStaticField("I")