from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LeakedClosableViolation"]

class LeakedClosableViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/LeakedClosableViolation"