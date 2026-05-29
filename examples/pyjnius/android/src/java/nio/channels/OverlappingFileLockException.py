from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OverlappingFileLockException"]

class OverlappingFileLockException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/OverlappingFileLockException"
    __javaconstructor__ = [("()V", False)]