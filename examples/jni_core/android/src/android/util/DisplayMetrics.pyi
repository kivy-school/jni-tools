from typing import Any, ClassVar, overload

class DisplayMetrics:
    DENSITY_140: ClassVar[int]
    DENSITY_180: ClassVar[int]
    DENSITY_200: ClassVar[int]
    DENSITY_220: ClassVar[int]
    DENSITY_260: ClassVar[int]
    DENSITY_280: ClassVar[int]
    DENSITY_300: ClassVar[int]
    DENSITY_340: ClassVar[int]
    DENSITY_360: ClassVar[int]
    DENSITY_390: ClassVar[int]
    DENSITY_400: ClassVar[int]
    DENSITY_420: ClassVar[int]
    DENSITY_440: ClassVar[int]
    DENSITY_450: ClassVar[int]
    DENSITY_520: ClassVar[int]
    DENSITY_560: ClassVar[int]
    DENSITY_600: ClassVar[int]
    DENSITY_DEFAULT: ClassVar[int]
    DENSITY_DEVICE_STABLE: ClassVar[int]
    DENSITY_HIGH: ClassVar[int]
    DENSITY_LOW: ClassVar[int]
    DENSITY_MEDIUM: ClassVar[int]
    DENSITY_TV: ClassVar[int]
    DENSITY_XHIGH: ClassVar[int]
    DENSITY_XXHIGH: ClassVar[int]
    DENSITY_XXXHIGH: ClassVar[int]
    density: float
    densityDpi: int
    heightPixels: int
    scaledDensity: float
    widthPixels: int
    xdpi: float
    ydpi: float
    def __init__(self) -> None: ...
    def setTo(self, p0: "DisplayMetrics") -> None: ...
    def setToDefaults(self) -> None: ...
    @overload
    def equals(self, p0: "DisplayMetrics") -> bool: ...
    @overload
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
