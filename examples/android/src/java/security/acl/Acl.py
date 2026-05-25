from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Acl"]

class Acl(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/acl/Acl"
    setName = JavaMethod("(Ljava/security/Principal;Ljava/lang/String;)V")
    getName = JavaMethod("()Ljava/lang/String;")
    addEntry = JavaMethod("(Ljava/security/Principal;Ljava/security/acl/AclEntry;)Z")
    removeEntry = JavaMethod("(Ljava/security/Principal;Ljava/security/acl/AclEntry;)Z")
    getPermissions = JavaMethod("(Ljava/security/Principal;)Ljava/util/Enumeration;")
    entries = JavaMethod("()Ljava/util/Enumeration;")
    checkPermission = JavaMethod("(Ljava/security/Principal;Ljava/security/acl/Permission;)Z")
    toString = JavaMethod("()Ljava/lang/String;")