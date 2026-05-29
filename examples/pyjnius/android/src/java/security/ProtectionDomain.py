from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProtectionDomain"]

class ProtectionDomain(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/ProtectionDomain"
    __javaconstructor__ = [("(Ljava/security/CodeSource;Ljava/security/PermissionCollection;)V", False), ("(Ljava/security/CodeSource;Ljava/security/PermissionCollection;Ljava/lang/ClassLoader;[Ljava/security/Principal;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getClassLoader = JavaMethod("()Ljava/lang/ClassLoader;")
    getCodeSource = JavaMethod("()Ljava/security/CodeSource;")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getPrincipals = JavaMethod("()[Ljava/security/Principal;")
    getPermissions = JavaMethod("()Ljava/security/PermissionCollection;")
    staticPermissionsOnly = JavaMethod("()Z")