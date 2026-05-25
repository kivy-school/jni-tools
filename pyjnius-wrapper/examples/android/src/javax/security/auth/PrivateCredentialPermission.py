from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrivateCredentialPermission"]

class PrivateCredentialPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/PrivateCredentialPermission"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    getCredentialClass = JavaMethod("()Ljava/lang/String;")
    getPrincipals = JavaMethod("()[[Ljava/lang/String;")
    implies = JavaMethod("(Ljava/security/Permission;)Z")
    getActions = JavaMethod("()Ljava/lang/String;")