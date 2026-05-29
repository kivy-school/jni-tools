from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FrameStats"]

class FrameStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/FrameStats"
    __javaconstructor__ = [("()V", False)]
    UNDEFINED_TIME_NANO = JavaStaticField("J")
    getEndTimeNano = JavaMethod("()J")
    getStartTimeNano = JavaMethod("()J")
    getFrameCount = JavaMethod("()I")
    getFramePresentedTimeNano = JavaMethod("(I)J")
    getRefreshPeriodNano = JavaMethod("()J")