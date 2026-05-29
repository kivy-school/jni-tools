from typing import Any, ClassVar, overload
from java.lang.annotation.RetentionPolicy import RetentionPolicy

class Retention:
    def value(self) -> RetentionPolicy: ...
