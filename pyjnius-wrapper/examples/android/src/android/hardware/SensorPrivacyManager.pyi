from typing import Any, ClassVar, overload

class SensorPrivacyManager:
    TOGGLE_TYPE_HARDWARE: ClassVar[int]
    TOGGLE_TYPE_SOFTWARE: ClassVar[int]
    @overload
    def supportsSensorToggle(self, arg0: int) -> bool: ...
    @overload
    def supportsSensorToggle(self, arg0: int, arg1: int) -> bool: ...

    class Sensors:
        CAMERA: ClassVar[int]
        MICROPHONE: ClassVar[int]
