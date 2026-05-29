from typing import Any, ClassVar, overload

class PosixFilePermission:
    OWNER_READ: ClassVar["PosixFilePermission"]
    OWNER_WRITE: ClassVar["PosixFilePermission"]
    OWNER_EXECUTE: ClassVar["PosixFilePermission"]
    GROUP_READ: ClassVar["PosixFilePermission"]
    GROUP_WRITE: ClassVar["PosixFilePermission"]
    GROUP_EXECUTE: ClassVar["PosixFilePermission"]
    OTHERS_READ: ClassVar["PosixFilePermission"]
    OTHERS_WRITE: ClassVar["PosixFilePermission"]
    OTHERS_EXECUTE: ClassVar["PosixFilePermission"]
    OWNER_READ: ClassVar["PosixFilePermission"]
    OWNER_WRITE: ClassVar["PosixFilePermission"]
    OWNER_EXECUTE: ClassVar["PosixFilePermission"]
    GROUP_READ: ClassVar["PosixFilePermission"]
    GROUP_WRITE: ClassVar["PosixFilePermission"]
    GROUP_EXECUTE: ClassVar["PosixFilePermission"]
    OTHERS_READ: ClassVar["PosixFilePermission"]
    OTHERS_WRITE: ClassVar["PosixFilePermission"]
    OTHERS_EXECUTE: ClassVar["PosixFilePermission"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "PosixFilePermission": ...
