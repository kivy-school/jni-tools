from typing import Any, ClassVar, overload

class AclEntryFlag:
    FILE_INHERIT: ClassVar["AclEntryFlag"]
    DIRECTORY_INHERIT: ClassVar["AclEntryFlag"]
    NO_PROPAGATE_INHERIT: ClassVar["AclEntryFlag"]
    INHERIT_ONLY: ClassVar["AclEntryFlag"]
    @staticmethod
    def values() -> list["AclEntryFlag"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "AclEntryFlag": ...
