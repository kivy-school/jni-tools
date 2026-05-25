from typing import Any, ClassVar, overload

class AclEntryType:
    ALLOW: ClassVar["AclEntryType"]
    DENY: ClassVar["AclEntryType"]
    AUDIT: ClassVar["AclEntryType"]
    ALARM: ClassVar["AclEntryType"]
    @staticmethod
    def values() -> list["AclEntryType"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "AclEntryType": ...
