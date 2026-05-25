from typing import Any, ClassVar, overload
from java.security.AccessControlContext import AccessControlContext
from java.security.Permission import Permission
from java.security.PrivilegedAction import PrivilegedAction
from java.security.PrivilegedExceptionAction import PrivilegedExceptionAction

class AccessController:
    @overload
    @staticmethod
    def doPrivileged(arg0: PrivilegedAction) -> Any: ...
    @overload
    @staticmethod
    def doPrivileged(arg0: PrivilegedAction, arg1: AccessControlContext) -> Any: ...
    @overload
    @staticmethod
    def doPrivileged(arg0: PrivilegedExceptionAction) -> Any: ...
    @overload
    @staticmethod
    def doPrivileged(arg0: PrivilegedExceptionAction, arg1: AccessControlContext) -> Any: ...
    @overload
    @staticmethod
    def doPrivilegedWithCombiner(arg0: PrivilegedAction) -> Any: ...
    @overload
    @staticmethod
    def doPrivilegedWithCombiner(arg0: PrivilegedExceptionAction) -> Any: ...
    @staticmethod
    def getContext() -> AccessControlContext: ...
    @staticmethod
    def checkPermission(arg0: Permission) -> None: ...
