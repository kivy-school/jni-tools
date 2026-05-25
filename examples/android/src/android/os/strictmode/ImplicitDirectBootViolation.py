from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImplicitDirectBootViolation"]

class ImplicitDirectBootViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/ImplicitDirectBootViolation"