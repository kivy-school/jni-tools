from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PolicySpi"]

class PolicySpi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/PolicySpi"
    __javaconstructor__ = [("()V", False)]
    engineImplies = JavaMethod("(Ljava/security/ProtectionDomain;Ljava/security/Permission;)Z")
    engineRefresh = JavaMethod("()V")
    engineGetPermissions = JavaMultipleMethod([("(Ljava/security/CodeSource;)Ljava/security/PermissionCollection;", False, False), ("(Ljava/security/ProtectionDomain;)Ljava/security/PermissionCollection;", False, False)])