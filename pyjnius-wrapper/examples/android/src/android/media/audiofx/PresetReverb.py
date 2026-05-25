from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PresetReverb"]

class PresetReverb(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/audiofx/PresetReverb"
    __javaconstructor__ = [("(II)V", False)]
    PARAM_PRESET = JavaStaticField("I")
    PRESET_LARGEHALL = JavaStaticField("S")
    PRESET_LARGEROOM = JavaStaticField("S")
    PRESET_MEDIUMHALL = JavaStaticField("S")
    PRESET_MEDIUMROOM = JavaStaticField("S")
    PRESET_NONE = JavaStaticField("S")
    PRESET_PLATE = JavaStaticField("S")
    PRESET_SMALLROOM = JavaStaticField("S")
    setPreset = JavaMethod("(S)V")
    getPreset = JavaMethod("()S")
    setParameterListener = JavaMethod("(Landroid/media/audiofx/PresetReverb$OnParameterChangeListener;)V")
    getProperties = JavaMethod("()Landroid/media/audiofx/PresetReverb$Settings;")
    setProperties = JavaMethod("(Landroid/media/audiofx/PresetReverb$Settings;)V")

    class OnParameterChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/PresetReverb/OnParameterChangeListener"
        onParameterChange = JavaMethod("(Landroid/media/audiofx/PresetReverb;IIS)V")

    class Settings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/PresetReverb/Settings"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]
        preset = JavaField("S")
        toString = JavaMethod("()Ljava/lang/String;")