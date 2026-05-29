from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SubtitleData"]

class SubtitleData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/SubtitleData"
    __javaconstructor__ = [("(IJJ[B)V", False)]
    getDurationUs = JavaMethod("()J")
    getStartTimeUs = JavaMethod("()J")
    getTrackIndex = JavaMethod("()I")
    getData = JavaMethod("()[B")