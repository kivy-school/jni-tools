from typing import Any, ClassVar, overload

class MediaCasException:

    class DeniedByServerException:
        ...

    class InsufficientResourceException:
        ...

    class NotProvisionedException:
        ...

    class ResourceBusyException:
        ...

    class UnsupportedCasException:
        ...
