from typing import Any, ClassVar, overload

class Build:
    BOARD: ClassVar[str]
    BOOTLOADER: ClassVar[str]
    BRAND: ClassVar[str]
    CPU_ABI: ClassVar[str]
    CPU_ABI2: ClassVar[str]
    DEVICE: ClassVar[str]
    DISPLAY: ClassVar[str]
    FINGERPRINT: ClassVar[str]
    HARDWARE: ClassVar[str]
    HOST: ClassVar[str]
    ID: ClassVar[str]
    MANUFACTURER: ClassVar[str]
    MODEL: ClassVar[str]
    ODM_SKU: ClassVar[str]
    PRODUCT: ClassVar[str]
    RADIO: ClassVar[str]
    SERIAL: ClassVar[str]
    SKU: ClassVar[str]
    SOC_MANUFACTURER: ClassVar[str]
    SOC_MODEL: ClassVar[str]
    SUPPORTED_32_BIT_ABIS: ClassVar[Any]
    SUPPORTED_64_BIT_ABIS: ClassVar[Any]
    SUPPORTED_ABIS: ClassVar[Any]
    TAGS: ClassVar[str]
    TIME: ClassVar[int]
    TYPE: ClassVar[str]
    UNKNOWN: ClassVar[str]
    USER: ClassVar[str]
    def __init__(self) -> None: ...
    @staticmethod
    def getRadioVersion() -> str: ...
    @staticmethod
    def getFingerprintedPartitions() -> list: ...
    @staticmethod
    def getSerial() -> str: ...

    class VERSION_CODES:
        BASE: ClassVar[int]
        BASE_1_1: ClassVar[int]
        CUPCAKE: ClassVar[int]
        CUR_DEVELOPMENT: ClassVar[int]
        DONUT: ClassVar[int]
        ECLAIR: ClassVar[int]
        ECLAIR_0_1: ClassVar[int]
        ECLAIR_MR1: ClassVar[int]
        FROYO: ClassVar[int]
        GINGERBREAD: ClassVar[int]
        GINGERBREAD_MR1: ClassVar[int]
        HONEYCOMB: ClassVar[int]
        HONEYCOMB_MR1: ClassVar[int]
        HONEYCOMB_MR2: ClassVar[int]
        ICE_CREAM_SANDWICH: ClassVar[int]
        ICE_CREAM_SANDWICH_MR1: ClassVar[int]
        JELLY_BEAN: ClassVar[int]
        JELLY_BEAN_MR1: ClassVar[int]
        JELLY_BEAN_MR2: ClassVar[int]
        KITKAT: ClassVar[int]
        KITKAT_WATCH: ClassVar[int]
        LOLLIPOP: ClassVar[int]
        LOLLIPOP_MR1: ClassVar[int]
        M: ClassVar[int]
        N: ClassVar[int]
        N_MR1: ClassVar[int]
        O: ClassVar[int]
        O_MR1: ClassVar[int]
        P: ClassVar[int]
        Q: ClassVar[int]
        R: ClassVar[int]
        S: ClassVar[int]
        S_V2: ClassVar[int]
        TIRAMISU: ClassVar[int]
        UPSIDE_DOWN_CAKE: ClassVar[int]
        VANILLA_ICE_CREAM: ClassVar[int]
        def __init__(self) -> None: ...

    class VERSION:
        BASE_OS: ClassVar[str]
        CODENAME: ClassVar[str]
        INCREMENTAL: ClassVar[str]
        MEDIA_PERFORMANCE_CLASS: ClassVar[int]
        PREVIEW_SDK_INT: ClassVar[int]
        RELEASE: ClassVar[str]
        RELEASE_OR_CODENAME: ClassVar[str]
        RELEASE_OR_PREVIEW_DISPLAY: ClassVar[str]
        SDK: ClassVar[str]
        SDK_INT: ClassVar[int]
        SECURITY_PATCH: ClassVar[str]
        def __init__(self) -> None: ...

    class Partition:
        PARTITION_NAME_SYSTEM: ClassVar[str]
        def getFingerprint(self) -> str: ...
        def getBuildTimeMillis(self) -> int: ...
        def getName(self) -> str: ...
        def equals(self, p0: Any) -> bool: ...
        def hashCode(self) -> int: ...
