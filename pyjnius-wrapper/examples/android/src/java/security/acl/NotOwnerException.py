from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotOwnerException"]

class NotOwnerException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/acl/NotOwnerException"
    __javaconstructor__ = [("()V", False)]