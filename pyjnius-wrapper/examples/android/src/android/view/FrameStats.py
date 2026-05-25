from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FrameStats"]

class FrameStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/FrameStats"
    __javaconstructor__ = [("()V", False)]
    UNDEFINED_TIME_NANO = JavaStaticField("J")
    getRefreshPeriodNano = JavaMethod("()J")
    getFrameCount = JavaMethod("()I")
    getStartTimeNano = JavaMethod("()J")
    getEndTimeNano = JavaMethod("()J")
    getFramePresentedTimeNano = JavaMethod("(I)J")