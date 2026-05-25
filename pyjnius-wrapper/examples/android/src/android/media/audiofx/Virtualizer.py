from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Virtualizer"]

class Virtualizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/audiofx/Virtualizer"
    __javaconstructor__ = [("(II)V", False)]
    PARAM_STRENGTH = JavaStaticField("I")
    PARAM_STRENGTH_SUPPORTED = JavaStaticField("I")
    VIRTUALIZATION_MODE_AUTO = JavaStaticField("I")
    VIRTUALIZATION_MODE_BINAURAL = JavaStaticField("I")
    VIRTUALIZATION_MODE_OFF = JavaStaticField("I")
    VIRTUALIZATION_MODE_TRANSAURAL = JavaStaticField("I")
    getStrengthSupported = JavaMethod("()Z")
    setStrength = JavaMethod("(S)V")
    getRoundedStrength = JavaMethod("()S")
    canVirtualize = JavaMethod("(II)Z")
    getSpeakerAngles = JavaMethod("(II[I)Z")
    forceVirtualizationMode = JavaMethod("(I)Z")
    getVirtualizationMode = JavaMethod("()I")
    setParameterListener = JavaMethod("(Landroid/media/audiofx/Virtualizer$OnParameterChangeListener;)V")
    getProperties = JavaMethod("()Landroid/media/audiofx/Virtualizer$Settings;")
    setProperties = JavaMethod("(Landroid/media/audiofx/Virtualizer$Settings;)V")

    class OnParameterChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/Virtualizer/OnParameterChangeListener"
        onParameterChange = JavaMethod("(Landroid/media/audiofx/Virtualizer;IIS)V")

    class Settings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/Virtualizer/Settings"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]
        strength = JavaField("S")
        toString = JavaMethod("()Ljava/lang/String;")