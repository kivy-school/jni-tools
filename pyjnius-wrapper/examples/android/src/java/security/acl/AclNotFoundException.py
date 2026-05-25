from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AclNotFoundException"]

class AclNotFoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/acl/AclNotFoundException"
    __javaconstructor__ = [("()V", False)]