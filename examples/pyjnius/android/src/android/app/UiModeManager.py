from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UiModeManager"]

class UiModeManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/UiModeManager"
    ACTION_ENTER_CAR_MODE = JavaStaticField("Ljava/lang/String;")
    ACTION_ENTER_DESK_MODE = JavaStaticField("Ljava/lang/String;")
    ACTION_EXIT_CAR_MODE = JavaStaticField("Ljava/lang/String;")
    ACTION_EXIT_DESK_MODE = JavaStaticField("Ljava/lang/String;")
    DISABLE_CAR_MODE_GO_HOME = JavaStaticField("I")
    ENABLE_CAR_MODE_ALLOW_SLEEP = JavaStaticField("I")
    ENABLE_CAR_MODE_GO_CAR_HOME = JavaStaticField("I")
    MODE_NIGHT_AUTO = JavaStaticField("I")
    MODE_NIGHT_CUSTOM = JavaStaticField("I")
    MODE_NIGHT_NO = JavaStaticField("I")
    MODE_NIGHT_YES = JavaStaticField("I")
    enableCarMode = JavaMethod("(I)V")
    disableCarMode = JavaMethod("(I)V")
    getCurrentModeType = JavaMethod("()I")
    setNightMode = JavaMethod("(I)V")
    setApplicationNightMode = JavaMethod("(I)V")
    getNightMode = JavaMethod("()I")
    getCustomNightModeStart = JavaMethod("()Ljava/time/LocalTime;")
    setCustomNightModeStart = JavaMethod("(Ljava/time/LocalTime;)V")
    getCustomNightModeEnd = JavaMethod("()Ljava/time/LocalTime;")
    setCustomNightModeEnd = JavaMethod("(Ljava/time/LocalTime;)V")
    getContrast = JavaMethod("()F")
    addContrastChangeListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/app/UiModeManager$ContrastChangeListener;)V")
    removeContrastChangeListener = JavaMethod("(Landroid/app/UiModeManager$ContrastChangeListener;)V")

    class ContrastChangeListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/UiModeManager/ContrastChangeListener"
        onContrastChanged = JavaMethod("(F)V")