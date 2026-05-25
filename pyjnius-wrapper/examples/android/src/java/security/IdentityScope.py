from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IdentityScope"]

class IdentityScope(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/IdentityScope"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/security/IdentityScope;)V", False)]
    getSystemScope = JavaStaticMethod("()Ljava/security/IdentityScope;")
    setSystemScope = JavaStaticMethod("(Ljava/security/IdentityScope;)V")
    size = JavaMethod("()I")
    getIdentity = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/security/Identity;", False, False), ("(Ljava/security/Principal;)Ljava/security/Identity;", False, False), ("(Ljava/security/PublicKey;)Ljava/security/Identity;", False, False)])
    addIdentity = JavaMethod("(Ljava/security/Identity;)V")
    removeIdentity = JavaMethod("(Ljava/security/Identity;)V")
    identities = JavaMethod("()Ljava/util/Enumeration;")
    toString = JavaMethod("()Ljava/lang/String;")