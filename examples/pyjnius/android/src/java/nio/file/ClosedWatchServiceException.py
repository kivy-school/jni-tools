from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClosedWatchServiceException"]

class ClosedWatchServiceException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/ClosedWatchServiceException"
    __javaconstructor__ = [("()V", False)]