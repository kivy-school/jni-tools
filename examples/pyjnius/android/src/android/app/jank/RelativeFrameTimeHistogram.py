from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RelativeFrameTimeHistogram"]

class RelativeFrameTimeHistogram(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/jank/RelativeFrameTimeHistogram"
    __javaconstructor__ = [("()V", False)]
    getBucketCounters = JavaMethod("()[I")
    getBucketEndpointsMillis = JavaMethod("()[I")
    addRelativeFrameTimeMillis = JavaMethod("(I)V")