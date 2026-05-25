from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioEffect"]

class AudioEffect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/audiofx/AudioEffect"
    ACTION_CLOSE_AUDIO_EFFECT_CONTROL_SESSION = JavaStaticField("Ljava/lang/String;")
    ACTION_DISPLAY_AUDIO_EFFECT_CONTROL_PANEL = JavaStaticField("Ljava/lang/String;")
    ACTION_OPEN_AUDIO_EFFECT_CONTROL_SESSION = JavaStaticField("Ljava/lang/String;")
    ALREADY_EXISTS = JavaStaticField("I")
    CONTENT_TYPE_GAME = JavaStaticField("I")
    CONTENT_TYPE_MOVIE = JavaStaticField("I")
    CONTENT_TYPE_MUSIC = JavaStaticField("I")
    CONTENT_TYPE_VOICE = JavaStaticField("I")
    EFFECT_AUXILIARY = JavaStaticField("Ljava/lang/String;")
    EFFECT_INSERT = JavaStaticField("Ljava/lang/String;")
    EFFECT_POST_PROCESSING = JavaStaticField("Ljava/lang/String;")
    EFFECT_PRE_PROCESSING = JavaStaticField("Ljava/lang/String;")
    EFFECT_TYPE_AEC = JavaStaticField("Ljava/util/UUID;")
    EFFECT_TYPE_AGC = JavaStaticField("Ljava/util/UUID;")
    EFFECT_TYPE_BASS_BOOST = JavaStaticField("Ljava/util/UUID;")
    EFFECT_TYPE_DYNAMICS_PROCESSING = JavaStaticField("Ljava/util/UUID;")
    EFFECT_TYPE_ENV_REVERB = JavaStaticField("Ljava/util/UUID;")
    EFFECT_TYPE_EQUALIZER = JavaStaticField("Ljava/util/UUID;")
    EFFECT_TYPE_HAPTIC_GENERATOR = JavaStaticField("Ljava/util/UUID;")
    EFFECT_TYPE_LOUDNESS_ENHANCER = JavaStaticField("Ljava/util/UUID;")
    EFFECT_TYPE_NS = JavaStaticField("Ljava/util/UUID;")
    EFFECT_TYPE_PRESET_REVERB = JavaStaticField("Ljava/util/UUID;")
    EFFECT_TYPE_VIRTUALIZER = JavaStaticField("Ljava/util/UUID;")
    ERROR = JavaStaticField("I")
    ERROR_BAD_VALUE = JavaStaticField("I")
    ERROR_DEAD_OBJECT = JavaStaticField("I")
    ERROR_INVALID_OPERATION = JavaStaticField("I")
    ERROR_NO_INIT = JavaStaticField("I")
    ERROR_NO_MEMORY = JavaStaticField("I")
    EXTRA_AUDIO_SESSION = JavaStaticField("Ljava/lang/String;")
    EXTRA_CONTENT_TYPE = JavaStaticField("Ljava/lang/String;")
    EXTRA_PACKAGE_NAME = JavaStaticField("Ljava/lang/String;")
    SUCCESS = JavaStaticField("I")
    release = JavaMethod("()V")
    finalize = JavaMethod("()V")
    getDescriptor = JavaMethod("()Landroid/media/audiofx/AudioEffect$Descriptor;")
    queryEffects = JavaStaticMethod("()[Landroid/media/audiofx/AudioEffect$Descriptor;")
    setEnabled = JavaMethod("(Z)I")
    getId = JavaMethod("()I")
    getEnabled = JavaMethod("()Z")
    hasControl = JavaMethod("()Z")
    setEnableStatusListener = JavaMethod("(Landroid/media/audiofx/AudioEffect$OnEnableStatusChangeListener;)V")
    setControlStatusListener = JavaMethod("(Landroid/media/audiofx/AudioEffect$OnControlStatusChangeListener;)V")

    class Descriptor(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/AudioEffect/Descriptor"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
        connectMode = JavaField("Ljava/lang/String;")
        implementor = JavaField("Ljava/lang/String;")
        name = JavaField("Ljava/lang/String;")
        type = JavaField("Ljava/util/UUID;")
        uuid = JavaField("Ljava/util/UUID;")
        hashCode = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")

    class OnControlStatusChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/AudioEffect/OnControlStatusChangeListener"
        onControlStatusChange = JavaMethod("(Landroid/media/audiofx/AudioEffect;Z)V")

    class OnEnableStatusChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/audiofx/AudioEffect/OnEnableStatusChangeListener"
        onEnableStatusChange = JavaMethod("(Landroid/media/audiofx/AudioEffect;Z)V")