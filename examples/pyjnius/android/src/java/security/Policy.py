from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Policy"]

class Policy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/Policy"
    __javaconstructor__ = [("()V", False)]
    UNSUPPORTED_EMPTY_COLLECTION = JavaStaticField("Ljava/security/PermissionCollection;")
    getPolicy = JavaStaticMethod("()Ljava/security/Policy;")
    setPolicy = JavaStaticMethod("(Ljava/security/Policy;)V")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;Ljava/security/Policy$Parameters;)Ljava/security/Policy;", True, False), ("(Ljava/lang/String;Ljava/security/Policy$Parameters;Ljava/lang/String;)Ljava/security/Policy;", True, False), ("(Ljava/lang/String;Ljava/security/Policy$Parameters;Ljava/security/Provider;)Ljava/security/Policy;", True, False)])
    getProvider = JavaMethod("()Ljava/security/Provider;")
    getType = JavaMethod("()Ljava/lang/String;")
    getParameters = JavaMethod("()Ljava/security/Policy$Parameters;")
    getPermissions = JavaMultipleMethod([("(Ljava/security/CodeSource;)Ljava/security/PermissionCollection;", False, False), ("(Ljava/security/ProtectionDomain;)Ljava/security/PermissionCollection;", False, False)])
    implies = JavaMethod("(Ljava/security/ProtectionDomain;Ljava/security/Permission;)Z")
    refresh = JavaMethod("()V")

    class Parameters(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/security/Policy/Parameters"