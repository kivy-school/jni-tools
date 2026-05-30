from typing import Any, ClassVar, overload

class ImsRegistrationImplBase:
    REGISTRATION_TECH_3G: ClassVar[int]
    REGISTRATION_TECH_CROSS_SIM: ClassVar[int]
    REGISTRATION_TECH_IWLAN: ClassVar[int]
    REGISTRATION_TECH_LTE: ClassVar[int]
    REGISTRATION_TECH_NONE: ClassVar[int]
    REGISTRATION_TECH_NR: ClassVar[int]

