from typing import Any, ClassVar, overload

class Repeatable:
    def value(self) -> type: ...

from typing import Any, ClassVar, overload
from java.lang.annotation.RetentionPolicy import RetentionPolicy

class Retention:
    def value(self) -> RetentionPolicy: ...

from typing import Any, ClassVar, overload

class Target:
    def value(self) -> Any: ...

from typing import Any, ClassVar, overload

class Documented:
    ...

from typing import Any, ClassVar, overload
from java.lang.Throwable import Throwable

class AnnotationFormatError:
    @overload
    def __init__(self, p0: str) -> None: ...
    @overload
    def __init__(self, p0: str, p1: Throwable) -> None: ...
    @overload
    def __init__(self, p0: Throwable) -> None: ...

from typing import Any, ClassVar, overload

class IncompleteAnnotationException:
    def __init__(self, p0: type, p1: str) -> None: ...
    def annotationType(self) -> type: ...
    def elementName(self) -> str: ...

from typing import Any, ClassVar, overload

class Native:
    ...

from typing import Any, ClassVar, overload

class Inherited:
    ...

from typing import Any, ClassVar, overload
from java.lang.reflect.Method import Method

class AnnotationTypeMismatchException:
    def __init__(self, p0: Method, p1: str) -> None: ...
    def element(self) -> Method: ...
    def foundType(self) -> str: ...

from typing import Any, ClassVar, overload

class RetentionPolicy:
    SOURCE: ClassVar["RetentionPolicy"]
    CLASS: ClassVar["RetentionPolicy"]
    RUNTIME: ClassVar["RetentionPolicy"]
    SOURCE: ClassVar["RetentionPolicy"]
    CLASS: ClassVar["RetentionPolicy"]
    RUNTIME: ClassVar["RetentionPolicy"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "RetentionPolicy": ...

from typing import Any, ClassVar, overload

class ElementType:
    TYPE: ClassVar["ElementType"]
    FIELD: ClassVar["ElementType"]
    METHOD: ClassVar["ElementType"]
    PARAMETER: ClassVar["ElementType"]
    CONSTRUCTOR: ClassVar["ElementType"]
    LOCAL_VARIABLE: ClassVar["ElementType"]
    ANNOTATION_TYPE: ClassVar["ElementType"]
    PACKAGE: ClassVar["ElementType"]
    TYPE_PARAMETER: ClassVar["ElementType"]
    TYPE_USE: ClassVar["ElementType"]
    MODULE: ClassVar["ElementType"]
    RECORD_COMPONENT: ClassVar["ElementType"]
    TYPE: ClassVar["ElementType"]
    FIELD: ClassVar["ElementType"]
    METHOD: ClassVar["ElementType"]
    PARAMETER: ClassVar["ElementType"]
    CONSTRUCTOR: ClassVar["ElementType"]
    LOCAL_VARIABLE: ClassVar["ElementType"]
    ANNOTATION_TYPE: ClassVar["ElementType"]
    PACKAGE: ClassVar["ElementType"]
    TYPE_PARAMETER: ClassVar["ElementType"]
    TYPE_USE: ClassVar["ElementType"]
    MODULE: ClassVar["ElementType"]
    RECORD_COMPONENT: ClassVar["ElementType"]
    @staticmethod
    def values() -> Any: ...
    @staticmethod
    def valueOf(p0: str) -> "ElementType": ...

from typing import Any, ClassVar, overload

class Annotation:
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def annotationType(self) -> type: ...

