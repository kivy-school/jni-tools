from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaMuxer"]

class MediaMuxer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaMuxer"
    __javaconstructor__ = [("(Ljava/io/FileDescriptor;I)V", False), ("(Ljava/lang/String;I)V", False)]
    setOrientationHint = JavaMethod("(I)V")
    start = JavaMethod("()V")
    release = JavaMethod("()V")
    setLocation = JavaMethod("(FF)V")
    stop = JavaMethod("()V")
    writeSampleData = JavaMethod("(ILjava/nio/ByteBuffer;Landroid/media/MediaCodec$BufferInfo;)V")
    addTrack = JavaMethod("(Landroid/media/MediaFormat;)I")

    class OutputFormat(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaMuxer$OutputFormat"
        MUXER_OUTPUT_3GPP = JavaStaticField("I")
        MUXER_OUTPUT_HEIF = JavaStaticField("I")
        MUXER_OUTPUT_MPEG_4 = JavaStaticField("I")
        MUXER_OUTPUT_OGG = JavaStaticField("I")
        MUXER_OUTPUT_WEBM = JavaStaticField("I")