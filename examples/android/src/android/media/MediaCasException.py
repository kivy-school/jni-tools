from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaCasException"]

class MediaCasException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaCasException"

    class DeniedByServerException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCasException/DeniedByServerException"

    class InsufficientResourceException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCasException/InsufficientResourceException"

    class NotProvisionedException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCasException/NotProvisionedException"

    class ResourceBusyException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCasException/ResourceBusyException"

    class UnsupportedCasException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCasException/UnsupportedCasException"