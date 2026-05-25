from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PermissionCollection"]

class PermissionCollection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PermissionCollection"
    __javaconstructor__ = [("()V", False)]
    add = JavaMethod("(Ljava/security/Permission;)V")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    elements = JavaMethod("()Ljava/util/Enumeration;")
    setReadOnly = JavaMethod("()V")
    isReadOnly = JavaMethod("()Z")