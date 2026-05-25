from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceConnectionLeakedViolation"]

class ServiceConnectionLeakedViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/ServiceConnectionLeakedViolation"