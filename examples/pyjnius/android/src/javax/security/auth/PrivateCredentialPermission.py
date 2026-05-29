from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrivateCredentialPermission"]

class PrivateCredentialPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/PrivateCredentialPermission"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getPrincipals = JavaMethod("()[[Ljava/lang/String;")
    getActions = JavaMethod("()Ljava/lang/String;")
    getCredentialClass = JavaMethod("()Ljava/lang/String;")
    newPermissionCollection = JavaMethod("()Ljava/security/PermissionCollection;")