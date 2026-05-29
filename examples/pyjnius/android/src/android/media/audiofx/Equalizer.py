from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Equalizer"]

class Equalizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/audiofx/Equalizer"
    __javaconstructor__ = [("(II)V", False)]
    PARAM_BAND_FREQ_RANGE = JavaStaticField("I")
    PARAM_BAND_LEVEL = JavaStaticField("I")
    PARAM_CENTER_FREQ = JavaStaticField("I")
    PARAM_CURRENT_PRESET = JavaStaticField("I")
    PARAM_GET_BAND = JavaStaticField("I")
    PARAM_GET_NUM_OF_PRESETS = JavaStaticField("I")
    PARAM_GET_PRESET_NAME = JavaStaticField("I")
    PARAM_LEVEL_RANGE = JavaStaticField("I")
    PARAM_NUM_BANDS = JavaStaticField("I")
    PARAM_STRING_SIZE_MAX = JavaStaticField("I")
    getNumberOfBands = JavaMethod("()S")
    getBandLevelRange = JavaMethod("()[S")
    setBandLevel = JavaMethod("(SS)V")
    getBandLevel = JavaMethod("(S)S")
    getCenterFreq = JavaMethod("(S)I")
    getBandFreqRange = JavaMethod("(S)[I")
    getBand = JavaMethod("(I)S")
    getCurrentPreset = JavaMethod("()S")
    usePreset = JavaMethod("(S)V")
    getNumberOfPresets = JavaMethod("()S")
    getPresetName = JavaMethod("(S)Ljava/lang/String;")
    setParameterListener = JavaMethod("(Landroid/media/audiofx/Equalizer$OnParameterChangeListener;)V")
    getProperties = JavaMethod("()Landroid/media/audiofx/Equalizer$Settings;")
    setProperties = JavaMethod("(Landroid/media/audiofx/Equalizer$Settings;)V")

    class OnParameterChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/Equalizer/OnParameterChangeListener"
        onParameterChange = JavaMethod("(Landroid/media/audiofx/Equalizer;IIII)V")

    class Settings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/Equalizer/Settings"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]
        bandLevels = JavaField("[S")
        curPreset = JavaField("S")
        numBands = JavaField("S")
        toString = JavaMethod("()Ljava/lang/String;")