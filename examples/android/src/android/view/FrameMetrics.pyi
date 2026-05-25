from typing import Any, ClassVar, overload

class FrameMetrics:
    ANIMATION_DURATION: ClassVar[int]
    COMMAND_ISSUE_DURATION: ClassVar[int]
    DEADLINE: ClassVar[int]
    DRAW_DURATION: ClassVar[int]
    FIRST_DRAW_FRAME: ClassVar[int]
    GPU_DURATION: ClassVar[int]
    INPUT_HANDLING_DURATION: ClassVar[int]
    INTENDED_VSYNC_TIMESTAMP: ClassVar[int]
    LAYOUT_MEASURE_DURATION: ClassVar[int]
    SWAP_BUFFERS_DURATION: ClassVar[int]
    SYNC_DURATION: ClassVar[int]
    TOTAL_DURATION: ClassVar[int]
    UNKNOWN_DELAY_DURATION: ClassVar[int]
    VSYNC_TIMESTAMP: ClassVar[int]
    def __init__(self, arg0: "FrameMetrics") -> None: ...
    def getMetric(self, arg0: int) -> int: ...
