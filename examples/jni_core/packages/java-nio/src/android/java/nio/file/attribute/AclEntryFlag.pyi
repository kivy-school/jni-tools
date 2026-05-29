from typing import Any, ClassVar, overload

class AclEntryFlag:
    FILE_INHERIT: ClassVar["AclEntryFlag"]
    DIRECTORY_INHERIT: ClassVar["AclEntryFlag"]
    NO_PROPAGATE_INHERIT: ClassVar["AclEntryFlag"]
    INHERIT_ONLY: ClassVar["AclEntryFlag"]
    FILE_INHERIT: ClassVar["AclEntryFlag"]
    DIRECTORY_INHERIT: ClassVar["AclEntryFlag"]
    NO_PROPAGATE_INHERIT: ClassVar["AclEntryFlag"]
    INHERIT_ONLY: ClassVar["AclEntryFlag"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "AclEntryFlag": ...
