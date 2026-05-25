from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaTimestamp"]

class MediaTimestamp(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaTimestamp"
    __javaconstructor__ = [("(JJF)V", False)]
    TIMESTAMP_UNKNOWN = JavaStaticField("Landroid/media/MediaTimestamp;")
    getAnchorMediaTimeUs = JavaMethod("()J")
    getAnchorSytemNanoTime = JavaMethod("()J")
    getAnchorSystemNanoTime = JavaMethod("()J")
    getMediaClockRate = JavaMethod("()F")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")