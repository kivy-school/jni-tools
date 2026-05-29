from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaTimestamp"]

class MediaTimestamp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaTimestamp"
    __javaconstructor__ = [("(JJF)V", False)]
    TIMESTAMP_UNKNOWN = JavaStaticField("Landroid/media/MediaTimestamp;")
    getAnchorMediaTimeUs = JavaMethod("()J")
    getAnchorSystemNanoTime = JavaMethod("()J")
    getAnchorSytemNanoTime = JavaMethod("()J")
    getMediaClockRate = JavaMethod("()F")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")