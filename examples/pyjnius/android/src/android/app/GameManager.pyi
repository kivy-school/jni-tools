from typing import Any, ClassVar, overload
from android.app.GameState import GameState

class GameManager:
    GAME_MODE_BATTERY: ClassVar[int]
    GAME_MODE_CUSTOM: ClassVar[int]
    GAME_MODE_PERFORMANCE: ClassVar[int]
    GAME_MODE_STANDARD: ClassVar[int]
    GAME_MODE_UNSUPPORTED: ClassVar[int]
    def getGameMode(self) -> int: ...
    def setGameState(self, p0: GameState) -> None: ...
