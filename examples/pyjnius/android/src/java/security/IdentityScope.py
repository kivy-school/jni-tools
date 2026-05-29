from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IdentityScope"]

class IdentityScope(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/IdentityScope"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/security/IdentityScope;)V", False)]
    getIdentity = JavaMultipleMethod([("(Ljava/security/Principal;)Ljava/security/Identity;", False, False), ("(Ljava/security/PublicKey;)Ljava/security/Identity;", False, False), ("(Ljava/lang/String;)Ljava/security/Identity;", False, False)])
    size = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    addIdentity = JavaMethod("(Ljava/security/Identity;)V")
    getSystemScope = JavaStaticMethod("()Ljava/security/IdentityScope;")
    removeIdentity = JavaMethod("(Ljava/security/Identity;)V")
    identities = JavaMethod("()Ljava/util/Enumeration;")