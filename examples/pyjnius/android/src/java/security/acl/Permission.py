from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Permission"]

class Permission(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/acl/Permission"