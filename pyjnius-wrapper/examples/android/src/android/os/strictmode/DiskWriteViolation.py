from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DiskWriteViolation"]

class DiskWriteViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/DiskWriteViolation"