from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaActionSound"]

class MediaActionSound(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaActionSound"
    __javaconstructor__ = [("()V", False)]
    FOCUS_COMPLETE = JavaStaticField("I")
    SHUTTER_CLICK = JavaStaticField("I")
    START_VIDEO_RECORDING = JavaStaticField("I")
    STOP_VIDEO_RECORDING = JavaStaticField("I")
    mustPlayShutterSound = JavaStaticMethod("()Z")
    load = JavaMethod("(I)V")
    play = JavaMethod("(I)V")
    release = JavaMethod("()V")