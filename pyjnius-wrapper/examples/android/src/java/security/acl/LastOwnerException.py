from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LastOwnerException"]

class LastOwnerException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/acl/LastOwnerException"
    __javaconstructor__ = [("()V", False)]