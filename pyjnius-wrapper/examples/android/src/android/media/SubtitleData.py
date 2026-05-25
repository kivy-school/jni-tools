from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SubtitleData"]

class SubtitleData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/SubtitleData"
    __javaconstructor__ = [("(IJJ[B)V", False)]
    getTrackIndex = JavaMethod("()I")
    getStartTimeUs = JavaMethod("()J")
    getDurationUs = JavaMethod("()J")
    getData = JavaMethod("()[B")