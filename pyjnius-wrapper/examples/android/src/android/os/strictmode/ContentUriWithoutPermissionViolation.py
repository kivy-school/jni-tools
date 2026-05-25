from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentUriWithoutPermissionViolation"]

class ContentUriWithoutPermissionViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/ContentUriWithoutPermissionViolation"