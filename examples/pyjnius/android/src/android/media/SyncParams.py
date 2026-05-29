from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncParams"]

class SyncParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/SyncParams"
    __javaconstructor__ = [("()V", False)]
    AUDIO_ADJUST_MODE_DEFAULT = JavaStaticField("I")
    AUDIO_ADJUST_MODE_RESAMPLE = JavaStaticField("I")
    AUDIO_ADJUST_MODE_STRETCH = JavaStaticField("I")
    SYNC_SOURCE_AUDIO = JavaStaticField("I")
    SYNC_SOURCE_DEFAULT = JavaStaticField("I")
    SYNC_SOURCE_SYSTEM_CLOCK = JavaStaticField("I")
    SYNC_SOURCE_VSYNC = JavaStaticField("I")
    getFrameRate = JavaMethod("()F")
    getAudioAdjustMode = JavaMethod("()I")
    getSyncSource = JavaMethod("()I")
    getTolerance = JavaMethod("()F")
    setAudioAdjustMode = JavaMethod("(I)Landroid/media/SyncParams;")
    setSyncSource = JavaMethod("(I)Landroid/media/SyncParams;")
    setTolerance = JavaMethod("(F)Landroid/media/SyncParams;")
    allowDefaults = JavaMethod("()Landroid/media/SyncParams;")
    setFrameRate = JavaMethod("(F)Landroid/media/SyncParams;")