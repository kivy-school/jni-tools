from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CustomViolation"]

class CustomViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/CustomViolation"