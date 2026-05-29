from typing import Any, ClassVar, overload

class AclEntryType:
    ALLOW: ClassVar["AclEntryType"]
    DENY: ClassVar["AclEntryType"]
    AUDIT: ClassVar["AclEntryType"]
    ALARM: ClassVar["AclEntryType"]
    ALLOW: ClassVar["AclEntryType"]
    DENY: ClassVar["AclEntryType"]
    AUDIT: ClassVar["AclEntryType"]
    ALARM: ClassVar["AclEntryType"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "AclEntryType": ...
