from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkViolation"]

class NetworkViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/NetworkViolation"