from typing import Any, ClassVar, overload

class MediaCasException:

    class UnsupportedCasException:
        ...

    class ResourceBusyException:
        ...

    class NotProvisionedException:
        ...

    class InsufficientResourceException:
        ...

    class DeniedByServerException:
        ...
