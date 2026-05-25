from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CredentialProtectedWhileLockedViolation"]

class CredentialProtectedWhileLockedViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/CredentialProtectedWhileLockedViolation"