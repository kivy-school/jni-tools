from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    allowDefaults = JavaMethod("()Landroid/media/SyncParams;")
    setAudioAdjustMode = JavaMethod("(I)Landroid/media/SyncParams;")
    getAudioAdjustMode = JavaMethod("()I")
    setSyncSource = JavaMethod("(I)Landroid/media/SyncParams;")
    getSyncSource = JavaMethod("()I")
    setTolerance = JavaMethod("(F)Landroid/media/SyncParams;")
    getTolerance = JavaMethod("()F")
    setFrameRate = JavaMethod("(F)Landroid/media/SyncParams;")
    getFrameRate = JavaMethod("()F")