from typing import Any, ClassVar, overload
from java.util.regex.Matcher import Matcher
from java.util.regex.Pattern import Pattern

class Patterns:
    DOMAIN_NAME: ClassVar[Pattern]
    EMAIL_ADDRESS: ClassVar[Pattern]
    GOOD_IRI_CHAR: ClassVar[str]
    IP_ADDRESS: ClassVar[Pattern]
    PHONE: ClassVar[Pattern]
    TOP_LEVEL_DOMAIN: ClassVar[Pattern]
    TOP_LEVEL_DOMAIN_STR: ClassVar[str]
    TOP_LEVEL_DOMAIN_STR_FOR_WEB_URL: ClassVar[str]
    WEB_URL: ClassVar[Pattern]
    @staticmethod
    def concatGroups(p0: Matcher) -> str: ...
    @staticmethod
    def digitsAndPlusOnly(p0: Matcher) -> str: ...
