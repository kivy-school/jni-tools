from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnbufferedIoViolation"]

class UnbufferedIoViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/UnbufferedIoViolation"