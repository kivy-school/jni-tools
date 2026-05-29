from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaCasException"]

class MediaCasException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaCasException"

    class UnsupportedCasException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCasException$UnsupportedCasException"

    class ResourceBusyException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCasException$ResourceBusyException"

    class NotProvisionedException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCasException$NotProvisionedException"

    class InsufficientResourceException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCasException$InsufficientResourceException"

    class DeniedByServerException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCasException$DeniedByServerException"