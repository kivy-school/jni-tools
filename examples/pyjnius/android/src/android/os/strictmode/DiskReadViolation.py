from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DiskReadViolation"]

class DiskReadViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/DiskReadViolation"