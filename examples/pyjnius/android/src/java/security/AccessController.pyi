from typing import Any, ClassVar, overload
from java.security.AccessControlContext import AccessControlContext
from java.security.Permission import Permission
from java.security.PrivilegedAction import PrivilegedAction
from java.security.PrivilegedExceptionAction import PrivilegedExceptionAction

class AccessController:
    @staticmethod
    def getContext() -> AccessControlContext: ...
    @staticmethod
    def checkPermission(p0: Permission) -> None: ...
    @overload
    @staticmethod
    def doPrivileged(p0: PrivilegedAction) -> Any: ...
    @overload
    @staticmethod
    def doPrivileged(p0: PrivilegedExceptionAction, p1: AccessControlContext, p2: Any) -> Any: ...
    @overload
    @staticmethod
    def doPrivileged(p0: PrivilegedExceptionAction, p1: AccessControlContext) -> Any: ...
    @overload
    @staticmethod
    def doPrivileged(p0: PrivilegedAction, p1: AccessControlContext) -> Any: ...
    @overload
    @staticmethod
    def doPrivileged(p0: PrivilegedAction, p1: AccessControlContext, p2: Any) -> Any: ...
    @overload
    @staticmethod
    def doPrivileged(p0: PrivilegedExceptionAction) -> Any: ...
    @overload
    @staticmethod
    def doPrivilegedWithCombiner(p0: PrivilegedExceptionAction) -> Any: ...
    @overload
    @staticmethod
    def doPrivilegedWithCombiner(p0: PrivilegedExceptionAction, p1: AccessControlContext, p2: Any) -> Any: ...
    @overload
    @staticmethod
    def doPrivilegedWithCombiner(p0: PrivilegedAction) -> Any: ...
    @overload
    @staticmethod
    def doPrivilegedWithCombiner(p0: PrivilegedAction, p1: AccessControlContext, p2: Any) -> Any: ...
