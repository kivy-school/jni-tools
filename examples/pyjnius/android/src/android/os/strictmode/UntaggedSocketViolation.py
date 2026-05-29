from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UntaggedSocketViolation"]

class UntaggedSocketViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/UntaggedSocketViolation"