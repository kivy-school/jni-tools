from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Policy"]

class Policy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Policy"
    __javaconstructor__ = [("()V", False)]
    UNSUPPORTED_EMPTY_COLLECTION = JavaStaticField("Ljava/security/PermissionCollection;")
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Policy$Parameters;Ljava/security/Provider;)Ljava/security/Policy;", True, False), ("(Ljava/lang/String;Ljava/security/Policy$Parameters;Ljava/lang/String;)Ljava/security/Policy;", True, False), ("(Ljava/lang/String;Ljava/security/Policy$Parameters;)Ljava/security/Policy;", True, False)])
    getPolicy = JavaStaticMethod("()Ljava/security/Policy;")
    implies = JavaMethod("(Ljava/security/ProtectionDomain;Ljava/security/Permission;)Z")
    getPermissions = JavaMultipleMethod([("(Ljava/security/ProtectionDomain;)Ljava/security/PermissionCollection;", False, False), ("(Ljava/security/CodeSource;)Ljava/security/PermissionCollection;", False, False)])
    getType = JavaMethod("()Ljava/lang/String;")
    getParameters = JavaMethod("()Ljava/security/Policy$Parameters;")
    refresh = JavaMethod("()V")
    setPolicy = JavaStaticMethod("(Ljava/security/Policy;)V")

    class Parameters(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/Policy$Parameters"