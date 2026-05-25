from typing import Any, ClassVar, overload

class AclEntryPermission:
    READ_DATA: ClassVar["AclEntryPermission"]
    WRITE_DATA: ClassVar["AclEntryPermission"]
    APPEND_DATA: ClassVar["AclEntryPermission"]
    READ_NAMED_ATTRS: ClassVar["AclEntryPermission"]
    WRITE_NAMED_ATTRS: ClassVar["AclEntryPermission"]
    EXECUTE: ClassVar["AclEntryPermission"]
    DELETE_CHILD: ClassVar["AclEntryPermission"]
    READ_ATTRIBUTES: ClassVar["AclEntryPermission"]
    WRITE_ATTRIBUTES: ClassVar["AclEntryPermission"]
    DELETE: ClassVar["AclEntryPermission"]
    READ_ACL: ClassVar["AclEntryPermission"]
    WRITE_ACL: ClassVar["AclEntryPermission"]
    WRITE_OWNER: ClassVar["AclEntryPermission"]
    SYNCHRONIZE: ClassVar["AclEntryPermission"]
    ADD_FILE: ClassVar["AclEntryPermission"]
    ADD_SUBDIRECTORY: ClassVar["AclEntryPermission"]
    LIST_DIRECTORY: ClassVar["AclEntryPermission"]
    @staticmethod
    def values() -> list["AclEntryPermission"]: ...
    @staticmethod
    def valueOf(arg0: str) -> "AclEntryPermission": ...
