from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BassBoost"]

class BassBoost(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/audiofx/BassBoost"
    __javaconstructor__ = [("(II)V", False)]
    PARAM_STRENGTH = JavaStaticField("I")
    PARAM_STRENGTH_SUPPORTED = JavaStaticField("I")
    getStrengthSupported = JavaMethod("()Z")
    setStrength = JavaMethod("(S)V")
    getRoundedStrength = JavaMethod("()S")
    setParameterListener = JavaMethod("(Landroid/media/audiofx/BassBoost$OnParameterChangeListener;)V")
    getProperties = JavaMethod("()Landroid/media/audiofx/BassBoost$Settings;")
    setProperties = JavaMethod("(Landroid/media/audiofx/BassBoost$Settings;)V")

    class OnParameterChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/BassBoost/OnParameterChangeListener"
        onParameterChange = JavaMethod("(Landroid/media/audiofx/BassBoost;IIS)V")

    class Settings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/BassBoost/Settings"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]
        strength = JavaField("S")
        toString = JavaMethod("()Ljava/lang/String;")