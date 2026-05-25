from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GameManager"]

class GameManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/GameManager"
    GAME_MODE_BATTERY = JavaStaticField("I")
    GAME_MODE_CUSTOM = JavaStaticField("I")
    GAME_MODE_PERFORMANCE = JavaStaticField("I")
    GAME_MODE_STANDARD = JavaStaticField("I")
    GAME_MODE_UNSUPPORTED = JavaStaticField("I")
    getGameMode = JavaMethod("()I")
    setGameState = JavaMethod("(Landroid/app/GameState;)V")