from typing import Any, ClassVar, overload

class GroupPrincipal:
    ...

from typing import Any, ClassVar, overload
from java.nio.file.attribute.BasicFileAttributes import BasicFileAttributes
from java.nio.file.attribute.GroupPrincipal import GroupPrincipal
from java.nio.file.attribute.PosixFileAttributes import PosixFileAttributes

class PosixFileAttributeView:
    def setGroup(self, p0: GroupPrincipal) -> None: ...
    def setPermissions(self, p0: set) -> None: ...
    def name(self) -> str: ...
    @overload
    def readAttributes(self) -> PosixFileAttributes: ...
    @overload
    def readAttributes(self) -> BasicFileAttributes: ...

from typing import Any, ClassVar, overload

class FileAttribute:
    def name(self) -> str: ...
    def value(self) -> Any: ...

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

from typing import Any, ClassVar, overload
from java.nio.file.attribute.AclEntryType import AclEntryType
from java.nio.file.attribute.UserPrincipal import UserPrincipal

class AclEntry:
    def type(self) -> AclEntryType: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def flags(self) -> set: ...
    def hashCode(self) -> int: ...
    def permissions(self) -> set: ...
    def principal(self) -> UserPrincipal: ...
    @overload
    @staticmethod
    def newBuilder(p0: "AclEntry") -> Any: ...
    @overload
    @staticmethod
    def newBuilder() -> Any: ...

    class Builder:
        @overload
        def setPermissions(self, p0: set) -> Any: ...
        @overload
        def setPermissions(self, p0: Any) -> Any: ...
        @overload
        def setFlags(self, p0: set) -> Any: ...
        @overload
        def setFlags(self, p0: Any) -> Any: ...
        def setType(self, p0: AclEntryType) -> Any: ...
        def build(self) -> "AclEntry": ...
        def setPrincipal(self, p0: UserPrincipal) -> Any: ...

from typing import Any, ClassVar, overload
from java.nio.file.attribute.UserPrincipal import UserPrincipal

class FileOwnerAttributeView:
    def setOwner(self, p0: UserPrincipal) -> None: ...
    def name(self) -> str: ...
    def getOwner(self) -> UserPrincipal: ...

from typing import Any, ClassVar, overload

class UserPrincipal:
    ...

from typing import Any, ClassVar, overload
from java.nio.file.attribute.FileAttribute import FileAttribute

class PosixFilePermissions:
    @staticmethod
    def toString(p0: set) -> str: ...
    @staticmethod
    def fromString(p0: str) -> set: ...
    @staticmethod
    def asFileAttribute(p0: set) -> FileAttribute: ...

from typing import Any, ClassVar, overload
from java.nio.ByteBuffer import ByteBuffer

class UserDefinedFileAttributeView:
    def name(self) -> str: ...
    def size(self, p0: str) -> int: ...
    def list(self) -> list: ...
    def write(self, p0: str, p1: ByteBuffer) -> int: ...
    def read(self, p0: str, p1: ByteBuffer) -> int: ...
    def delete(self, p0: str) -> None: ...

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

from typing import Any, ClassVar, overload
from java.nio.file.attribute.BasicFileAttributes import BasicFileAttributes
from java.nio.file.attribute.FileTime import FileTime

class BasicFileAttributeView:
    def setTimes(self, p0: FileTime, p1: FileTime, p2: FileTime) -> None: ...
    def name(self) -> str: ...
    def readAttributes(self) -> BasicFileAttributes: ...

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
    LIST_DIRECTORY: ClassVar["AclEntryPermission"]
    ADD_FILE: ClassVar["AclEntryPermission"]
    ADD_SUBDIRECTORY: ClassVar["AclEntryPermission"]
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
    LIST_DIRECTORY: ClassVar["AclEntryPermission"]
    ADD_FILE: ClassVar["AclEntryPermission"]
    ADD_SUBDIRECTORY: ClassVar["AclEntryPermission"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "AclEntryPermission": ...

from typing import Any, ClassVar, overload

class FileStoreAttributeView:
    ...

from typing import Any, ClassVar, overload

class UserPrincipalNotFoundException:
    def __init__(self, p0: str) -> None: ...
    def getName(self) -> str: ...

from typing import Any, ClassVar, overload
from java.nio.file.attribute.BasicFileAttributes import BasicFileAttributes
from java.nio.file.attribute.DosFileAttributes import DosFileAttributes

class DosFileAttributeView:
    def setHidden(self, p0: bool) -> None: ...
    def name(self) -> str: ...
    def setReadOnly(self, p0: bool) -> None: ...
    @overload
    def readAttributes(self) -> BasicFileAttributes: ...
    @overload
    def readAttributes(self) -> DosFileAttributes: ...
    def setSystem(self, p0: bool) -> None: ...
    def setArchive(self, p0: bool) -> None: ...

from typing import Any, ClassVar, overload
from java.time.Instant import Instant
from java.util.concurrent.TimeUnit import TimeUnit

class FileTime:
    def toInstant(self) -> Instant: ...
    @staticmethod
    def fromMillis(p0: int) -> "FileTime": ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    @overload
    def compareTo(self, p0: "FileTime") -> int: ...
    @overload
    def compareTo(self, p0: Any) -> int: ...
    @overload
    @staticmethod
    def from_(p0: Instant) -> "FileTime": ...
    @overload
    @staticmethod
    def from_(p0: int, p1: TimeUnit) -> "FileTime": ...
    def to(self, p0: TimeUnit) -> int: ...
    def toMillis(self) -> int: ...

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

from typing import Any, ClassVar, overload
from java.nio.file.attribute.FileTime import FileTime

class BasicFileAttributes:
    def lastAccessTime(self) -> FileTime: ...
    def lastModifiedTime(self) -> FileTime: ...
    def isSymbolicLink(self) -> bool: ...
    def fileKey(self) -> Any: ...
    def creationTime(self) -> FileTime: ...
    def isOther(self) -> bool: ...
    def size(self) -> int: ...
    def isRegularFile(self) -> bool: ...
    def isDirectory(self) -> bool: ...

from typing import Any, ClassVar, overload
from java.nio.file.attribute.GroupPrincipal import GroupPrincipal
from java.nio.file.attribute.UserPrincipal import UserPrincipal

class PosixFileAttributes:
    def group(self) -> GroupPrincipal: ...
    def permissions(self) -> set: ...
    def owner(self) -> UserPrincipal: ...

from typing import Any, ClassVar, overload
from java.nio.file.attribute.GroupPrincipal import GroupPrincipal
from java.nio.file.attribute.UserPrincipal import UserPrincipal

class UserPrincipalLookupService:
    def lookupPrincipalByName(self, p0: str) -> UserPrincipal: ...
    def lookupPrincipalByGroupName(self, p0: str) -> GroupPrincipal: ...

from typing import Any, ClassVar, overload

class FileAttributeView:
    ...

from typing import Any, ClassVar, overload

class DosFileAttributes:
    def isHidden(self) -> bool: ...
    def isSystem(self) -> bool: ...
    def isReadOnly(self) -> bool: ...
    def isArchive(self) -> bool: ...

from typing import Any, ClassVar, overload

class AttributeView:
    def name(self) -> str: ...

from typing import Any, ClassVar, overload

class AclFileAttributeView:
    def name(self) -> str: ...
    def getAcl(self) -> list: ...
    def setAcl(self, p0: list) -> None: ...

