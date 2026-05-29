from typing import Any, ClassVar, overload
from java.nio.file.attribute.GroupPrincipal import GroupPrincipal
from java.nio.file.attribute.UserPrincipal import UserPrincipal

class UserPrincipalLookupService:
    def lookupPrincipalByName(self, p0: str) -> UserPrincipal: ...
    def lookupPrincipalByGroupName(self, p0: str) -> GroupPrincipal: ...
