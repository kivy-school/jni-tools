from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LoudnessEnhancer"]

class LoudnessEnhancer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/audiofx/LoudnessEnhancer"
    __javaconstructor__ = [("(I)V", False)]
    PARAM_TARGET_GAIN_MB = JavaStaticField("I")
    setTargetGain = JavaMethod("(I)V")
    getTargetGain = JavaMethod("()F")