from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AclEntry"]

class AclEntry(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/acl/AclEntry"
    setPrincipal = JavaMethod("(Ljava/security/Principal;)Z")
    getPrincipal = JavaMethod("()Ljava/security/Principal;")
    setNegativePermissions = JavaMethod("()V")
    isNegative = JavaMethod("()Z")
    addPermission = JavaMethod("(Ljava/security/acl/Permission;)Z")
    removePermission = JavaMethod("(Ljava/security/acl/Permission;)Z")
    checkPermission = JavaMethod("(Ljava/security/acl/Permission;)Z")
    permissions = JavaMethod("()Ljava/util/Enumeration;")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")